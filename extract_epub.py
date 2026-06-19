#!/usr/bin/env python3
from __future__ import annotations

import argparse
import copy
import json
from html.parser import HTMLParser
import re
import shutil
import zipfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, unquote
from xml.etree import ElementTree as ET

import html as html_lib


SECTION_TAGS = {"section", "article"}
CONTAINER_TAGS = {"section", "article", "div", "body", "main"}
SKIP_TAGS = {"script", "style", "nav", "footer", "header"}
BLOCK_TAGS = {
    "p",
    "div",
    "section",
    "article",
    "main",
    "body",
    "ul",
    "ol",
    "table",
    "blockquote",
    "pre",
}
HEADING_TAGS = {f"h{i}" for i in range(1, 7)}
VOID_TAGS = {"br", "img", "hr", "meta", "link", "input", "source", "area", "base", "col"}


@dataclass
class TocNode:
    index: int
    href: str
    title: str
    level: int
    parent: "TocNode | None" = None
    children: list["TocNode"] = field(default_factory=list)

    @property
    def breadcrumbs(self) -> list[str]:
        items: list[str] = []
        node: TocNode | None = self
        while node is not None:
            items.append(node.title)
            node = node.parent
        return list(reversed(items))

    @property
    def descendant_hrefs(self) -> set[str]:
        out: set[str] = set()
        stack = list(self.children)
        while stack:
            node = stack.pop()
            out.add(node.href)
            stack.extend(node.children)
        return out


@dataclass
class RenderContext:
    extract_root: Path
    output_dir: Path
    source_file: str
    href_to_filename: dict[str, str]
    assets_dir_name: str = "assets"

    def source_dir(self) -> Path:
        return (self.extract_root / self.source_file).parent

    def output_assets_dir(self) -> Path:
        return self.output_dir / self.assets_dir_name

    def resolve_epub_relative(self, raw_href: str) -> tuple[str, str]:
        file_part, frag = urldefrag(unquote(raw_href))
        if not file_part:
            file_part = self.source_file
        source_dir = self.source_dir()
        abs_path = (source_dir / file_part).resolve()
        try:
            rel_path = abs_path.relative_to(self.extract_root).as_posix()
        except ValueError:
            rel_path = file_part
        return rel_path, frag

    def rewrite_link(self, raw_href: str) -> str:
        rel_path, frag = self.resolve_epub_relative(raw_href)
        target_href = rel_path if not frag else f"{rel_path}#{frag}"
        if target_href in self.href_to_filename:
            return self.href_to_filename[target_href]
        if rel_path in self.href_to_filename:
            return self.href_to_filename[rel_path]
        return raw_href

    def copy_asset(self, raw_src: str) -> str:
        rel_path, _ = self.resolve_epub_relative(raw_src)
        src_path = self.extract_root / rel_path
        if not src_path.exists():
            return raw_src
        dest_path = self.output_assets_dir() / rel_path
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        if not dest_path.exists():
            shutil.copy2(src_path, dest_path)
        return f"{self.assets_dir_name}/{rel_path}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract an EPUB manual into scoped markdown article chunks."
    )
    parser.add_argument("epub", type=Path, help="Path to EPUB file")
    parser.add_argument("--output-dir", type=Path, default=Path("articles"))
    parser.add_argument("--extract-dir", type=Path, default=Path(".epub_extracted"))
    parser.add_argument("--manifest", type=Path, default=Path("article_manifest.json"))
    parser.add_argument("--zip-output", type=Path, default=None)
    parser.add_argument("--pdf", type=Path, default=None)
    parser.add_argument("--pdf-outline-output", type=Path, default=Path("pdf_outline.json"))
    parser.add_argument("--keep-extracted", action="store_true")
    return parser.parse_args()


def reset_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def element_text(element: ET.Element) -> str:
    return "".join(element.itertext())


def compact_whitespace(text: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(text)).strip()


def slugify(text: str) -> str:
    text = compact_whitespace(text)
    text = re.sub(r"[^0-9A-Za-zА-Яа-я._ -]+", "", text)
    text = text.replace("/", " ")
    text = re.sub(r"\s+", "_", text).strip("._")
    return text[:120] or "article"


def markdown_escape_pipe(text: str) -> str:
    return text.replace("|", "\\|")


def clean_md(text: str) -> str:
    text = html_lib.unescape(text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"(?m)^[ \t]+$", "", text)
    text = text.strip()
    return text + "\n" if text else ""


def build_parent_map(root: ET.Element) -> dict[ET.Element, ET.Element | None]:
    parent_map: dict[ET.Element, ET.Element | None] = {root: None}
    for parent in root.iter():
        for child in list(parent):
            parent_map[child] = parent
    return parent_map


def find_first(root: ET.Element, names: Iterable[str]) -> ET.Element | None:
    wanted = set(names)
    for el in root.iter():
        if local_name(el.tag) in wanted:
            return el
    return None


def find_by_attr(root: ET.Element, attr: str, value: str) -> ET.Element | None:
    for el in root.iter():
        if el.attrib.get(attr) == value:
            return el
    return None


def find_nav_file(extract_dir: Path) -> Path:
    candidates = list(extract_dir.rglob("nav.xhtml")) + list(extract_dir.rglob("toc.xhtml"))
    if not candidates:
        raise FileNotFoundError("Could not find nav.xhtml or toc.xhtml in EPUB")
    return sorted(candidates)[0]


def parse_xml(path: Path) -> ET.Element:
    text = path.read_text(encoding="utf-8", errors="ignore")
    try:
        return ET.fromstring(text)
    except ET.ParseError:
        parser = LenientHTMLTreeBuilder()
        parser.feed(text)
        parser.close()
        return parser.root


class LenientHTMLTreeBuilder(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.root = ET.Element("document")
        self.stack: list[ET.Element] = [self.root]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        element = ET.Element(tag.lower(), {k: v or "" for k, v in attrs})
        self.stack[-1].append(element)
        if tag.lower() not in VOID_TAGS:
            self.stack.append(element)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        for idx in range(len(self.stack) - 1, 0, -1):
            if self.stack[idx].tag == tag:
                del self.stack[idx:]
                return

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        element = ET.Element(tag.lower(), {k: v or "" for k, v in attrs})
        self.stack[-1].append(element)

    def handle_data(self, data: str) -> None:
        if not data:
            return
        current = self.stack[-1]
        if len(current):
            last = current[-1]
            last.tail = (last.tail or "") + data
        else:
            current.text = (current.text or "") + data


def parse_nav(nav_file: Path) -> list[TocNode]:
    root = parse_xml(nav_file)
    nav = find_first(root, {"nav"})
    if nav is None:
        raise ValueError(f"No <nav> found in {nav_file}")
    root_ol = find_first(nav, {"ol"})
    if root_ol is None:
        raise ValueError(f"No <ol> found in {nav_file}")

    nodes: list[TocNode] = []
    seen: set[str] = set()
    counter = 0

    def direct_children(el: ET.Element, name: str) -> list[ET.Element]:
        return [child for child in list(el) if local_name(child.tag) == name]

    def walk(ol: ET.Element, parent: TocNode | None, level: int) -> None:
        nonlocal counter
        for li in direct_children(ol, "li"):
            links = direct_children(li, "a")
            child_ols = direct_children(li, "ol")
            if not links:
                for child_ol in child_ols:
                    walk(child_ol, parent, level)
                continue
            a = links[0]
            href = unquote(a.attrib.get("href", "").strip())
            title = compact_whitespace(element_text(a))
            if not href or href in seen:
                continue
            counter += 1
            node = TocNode(index=counter, href=href, title=title or "Untitled", level=level, parent=parent)
            nodes.append(node)
            seen.add(href)
            if parent is not None:
                parent.children.append(node)
            for child_ol in child_ols:
                walk(child_ol, node, level + 1)

    walk(root_ol, None, 0)
    return nodes


def find_target(body: ET.Element, frag: str) -> ET.Element:
    if not frag:
        main = find_first(body, {"main", "article"})
        return main if main is not None else body

    target = find_by_attr(body, "id", frag)
    if target is None:
        target = find_by_attr(body, "name", frag)
    if target is None:
        raise ValueError(f"Anchor #{frag} not found")

    parent_map = build_parent_map(body)
    current = target
    while current is not None and local_name(current.tag) not in CONTAINER_TAGS:
        current = parent_map.get(current)
    return current if current is not None else target


def remove_descendant_toc_sections(scoped: ET.Element, node: TocNode) -> None:
    descendant_frags = sorted(
        {urldefrag(href)[1] for href in node.descendant_hrefs if urldefrag(href)[1]},
        key=len,
        reverse=True,
    )
    parent_map = build_parent_map(scoped)

    for frag in descendant_frags:
        child = find_by_attr(scoped, "id", frag)
        if child is None:
            continue
        removable = child
        while removable is not None and removable is not scoped and local_name(removable.tag) not in SECTION_TAGS:
            removable = parent_map.get(removable)
        if removable is None or removable is scoped:
            continue
        parent = parent_map.get(removable)
        if parent is not None:
            parent.remove(removable)


def strip_duplicate_heading(scoped: ET.Element, title: str) -> None:
    parent_map = build_parent_map(scoped)
    for el in scoped.iter():
        if local_name(el.tag) in HEADING_TAGS:
            heading_text = compact_whitespace(element_text(el))
            if heading_text.lower() == compact_whitespace(title).lower():
                parent = parent_map.get(el)
                if parent is not None:
                    parent.remove(el)
            return


def render_children(element: ET.Element, ctx: RenderContext) -> str:
    parts: list[str] = []
    if element.text:
        parts.append(re.sub(r"\s+", " ", element.text))
    for child in list(element):
        parts.append(node_to_md(child, ctx))
        if child.tail:
            parts.append(re.sub(r"\s+", " ", child.tail))
    return "".join(parts)


def list_to_md(element: ET.Element, ordered: bool, ctx: RenderContext) -> str:
    lines: list[str] = [""]
    start = int(element.attrib.get("start", "1")) if element.attrib.get("start", "1").isdigit() else 1
    idx = start
    for child in list(element):
        if local_name(child.tag) != "li":
            continue
        marker = f"{idx}. " if ordered else "- "
        content = clean_md(render_children(child, ctx)).strip()
        content = re.sub(r"\n{2,}", "\n", content)
        lines.append(marker + content.replace("\n", "\n  "))
        idx += 1
    lines.append("")
    return "\n".join(lines) + "\n"


def table_to_md(element: ET.Element) -> str:
    rows: list[list[str]] = []
    for tr in element.iter():
        if local_name(tr.tag) != "tr":
            continue
        cells: list[str] = []
        for cell in list(tr):
            if local_name(cell.tag) in {"th", "td"}:
                cells.append(markdown_escape_pipe(compact_whitespace(element_text(cell))))
        if cells:
            rows.append(cells)
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    rows = [row + [""] * (width - len(row)) for row in rows]
    out = ["", "| " + " | ".join(rows[0]) + " |", "| " + " | ".join(["---"] * width) + " |"]
    out.extend("| " + " | ".join(row) + " |" for row in rows[1:])
    out.append("")
    return "\n".join(out) + "\n"


def node_to_md(element: ET.Element, ctx: RenderContext) -> str:
    name = local_name(element.tag)
    if name in SKIP_TAGS:
        return ""

    if name in HEADING_TAGS:
        text = compact_whitespace(element_text(element))
        return f"\n\n{'#' * int(name[1])} {text}\n\n" if text else ""

    if name == "p":
        text = clean_md(render_children(element, ctx)).strip()
        return f"\n\n{text}\n\n" if text else ""

    if name in {"strong", "b"}:
        text = clean_md(render_children(element, ctx)).strip()
        return f"**{text}**" if text else ""

    if name in {"em", "i"}:
        text = clean_md(render_children(element, ctx)).strip()
        return f"*{text}*" if text else ""

    if name == "code":
        text = compact_whitespace(element_text(element))
        return f"`{text}`" if text else ""

    if name == "pre":
        text = element_text(element).strip("\n")
        return f"\n\n```\n{text}\n```\n\n" if text else ""

    if name == "a":
        text = clean_md(render_children(element, ctx)).strip() or compact_whitespace(element_text(element))
        href = element.attrib.get("href", "").strip()
        if href and not href.startswith("#"):
            rewritten = ctx.rewrite_link(href)
            return f"[{text}]({rewritten})" if text else rewritten
        return text

    if name == "img":
        alt = compact_whitespace(element.attrib.get("alt", ""))
        src = element.attrib.get("src", "").strip()
        copied = ctx.copy_asset(src) if src else ""
        return f"![{alt}]({copied})" if copied else ""

    if name == "blockquote":
        text = clean_md(render_children(element, ctx)).strip()
        if not text:
            return ""
        return "\n\n" + "\n".join("> " + line for line in text.splitlines()) + "\n\n"

    if name == "br":
        return "\n"

    if name == "ul":
        return list_to_md(element, ordered=False, ctx=ctx)

    if name == "ol":
        return list_to_md(element, ordered=True, ctx=ctx)

    if name == "table":
        return table_to_md(element)

    if name in BLOCK_TAGS:
        return "".join(node_to_md(child, ctx) for child in list(element))

    return render_children(element, ctx)


def extract_scoped_markdown(src_path: Path, node: TocNode, ctx: RenderContext) -> str:
    root = parse_xml(src_path)
    body = find_first(root, {"body"})
    if body is None:
        body = root
    _, frag = urldefrag(node.href)
    target = find_target(body, frag)
    scoped = copy.deepcopy(target)
    remove_descendant_toc_sections(scoped, node)
    strip_duplicate_heading(scoped, node.title)
    return clean_md(node_to_md(scoped, ctx))


def build_filename(node: TocNode) -> str:
    parts = [slugify(part) for part in node.breadcrumbs]
    deduped: list[str] = []
    for part in parts:
        if not deduped or deduped[-1] != part:
            deduped.append(part)
    return f"{node.index:03d}_L{node.level}_{'__'.join(deduped)}.md"


def write_frontmatter(node: TocNode, epub_path: Path, source_file: str, source_anchor: str) -> str:
    canonical_title = " / ".join(node.breadcrumbs)
    fields = {
        "source_epub": epub_path.name,
        "source_href": node.href,
        "source_file": source_file,
        "source_anchor": source_anchor,
        "title": node.title,
        "canonical_title": canonical_title,
        "toc_level": node.level,
        "breadcrumbs": canonical_title,
    }
    lines = ["---"]
    for key, value in fields.items():
        lines.append(f'{key}: "{str(value).replace(chr(34), chr(39))}"')
    lines.append("---")
    lines.append("")
    return "\n".join(lines)


def nontrivial(md_body: str) -> bool:
    return len(re.sub(r"\W+", "", md_body)) >= 20


def zip_directory(source_dir: Path, output_zip: Path) -> None:
    if output_zip.exists():
        output_zip.unlink()
    shutil.make_archive(str(output_zip.with_suffix("")), "zip", source_dir)


def extract_pdf_outline(pdf_path: Path, output_path: Path) -> None:
    try:
        from pypdf import PdfReader

        reader = PdfReader(str(pdf_path))
        outline_rows: list[dict[str, int | str | None]] = []

        def walk(items: Iterable, level: int = 0) -> None:
            for item in items:
                if isinstance(item, list):
                    walk(item, level + 1)
                    continue
                try:
                    title = item.title
                    page = reader.get_destination_page_number(item) + 1
                except Exception:
                    title = str(item)
                    page = None
                outline_rows.append({"level": level, "title": title, "page": page})

        walk(reader.outline)
        output_path.write_text(json.dumps(outline_rows, ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as exc:
        output_path.write_text(json.dumps({"error": str(exc)}, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> None:
    args = parse_args()
    epub_path = args.epub.resolve()
    output_dir = args.output_dir.resolve()
    extract_dir = args.extract_dir.resolve()
    manifest_path = args.manifest.resolve()
    zip_output = args.zip_output.resolve() if args.zip_output else None
    repo_root = Path.cwd().resolve()

    if not epub_path.exists():
        raise FileNotFoundError(epub_path)
    if output_dir == repo_root:
        raise ValueError("Refusing to use the current repository root as --output-dir")
    if extract_dir == repo_root:
        raise ValueError("Refusing to use the current repository root as --extract-dir")

    if args.keep_extracted:
        extract_dir.mkdir(parents=True, exist_ok=True)
    else:
        reset_dir(extract_dir)
    reset_dir(output_dir)

    with zipfile.ZipFile(epub_path, "r") as archive:
        archive.extractall(extract_dir)

    nav_file = find_nav_file(extract_dir)
    toc_nodes = parse_nav(nav_file)
    href_to_filename = {node.href: build_filename(node) for node in toc_nodes}
    manifest: list[dict[str, str | int]] = []
    written = 0

    for node in toc_nodes:
        file_part, frag = urldefrag(node.href)
        src_path = (nav_file.parent / file_part).resolve()
        if not src_path.exists() or src_path.suffix.lower() not in {".xhtml", ".html", ".htm"}:
            continue
        try:
            ctx = RenderContext(
                extract_root=extract_dir,
                output_dir=output_dir,
                source_file=file_part,
                href_to_filename=href_to_filename,
            )
            md_body = extract_scoped_markdown(src_path, node, ctx)
        except Exception as exc:
            print(f"skip {node.href}: {exc}")
            continue
        if not nontrivial(md_body):
            continue

        filename = build_filename(node)
        frontmatter = write_frontmatter(node, epub_path, file_part, frag)
        (output_dir / filename).write_text(frontmatter + md_body, encoding="utf-8")
        manifest.append(
            {
                "markdown_file": filename,
                "title": node.title,
                "canonical_title": " / ".join(node.breadcrumbs),
                "breadcrumbs": " / ".join(node.breadcrumbs),
                "source_href": node.href,
                "source_file": file_part,
                "source_anchor": frag,
                "toc_level": node.level,
                "chars": len(md_body),
            }
        )
        written += 1

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    if zip_output is not None:
        zip_directory(output_dir, zip_output)
    if args.pdf is not None:
        extract_pdf_outline(args.pdf.resolve(), args.pdf_outline_output.resolve())

    print(f"TOC hrefs: {len(toc_nodes)}")
    print(f"Markdown chunks written: {written}")
    print(f"Output dir: {output_dir}")
    print(f"Manifest: {manifest_path}")
    if zip_output is not None:
        print(f"Zip: {zip_output}")


if __name__ == "__main__":
    main()

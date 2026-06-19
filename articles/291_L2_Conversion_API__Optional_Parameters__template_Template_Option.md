---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#template-template-option"
source_file: "docs/conversion_api.xhtml"
source_anchor: "template-template-option"
title: "template – Template Option"
canonical_title: "Conversion API / Optional Parameters / template – Template Option"
toc_level: "2"
breadcrumbs: "Conversion API / Optional Parameters / template – Template Option"
---
New in version 25.04.8.1.

This option allows specifying a template document whose styles are applied to the imported document. When a Markdown file is imported, Collabora Online uses built-in default styles for headings, body text, lists, etc. By providing a template, you can override these defaults with your own formatting — for example, custom fonts, colors, spacing, or page layout.

The template is an ODT or DOCX file that contains only style definitions (no content). To create one, start with an empty document, modify the paragraph styles (e.g. `Heading 1`, `Heading 2`, `Text Body`), and save it.

Example — convert a Markdown file to PDF using a custom template for styling:

```
curl -k -F "data=@test.md" -F "template=@corporate-style.docx" -F "format=pdf" \
     https://localhost:9980/cool/convert-to > out.pdf
```

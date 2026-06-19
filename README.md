# Collabora Online SDK 25.04 Markdown Corpus

Markdown corpus generated from the **Collabora Online SDK Manual 25.04**.

The repository is intended for study, onboarding, search, and LLM/RAG navigation.

## Contents

* `CO-SDK-manual-25.04.epub` — source EPUB
* `extract_epub.py` — EPUB to Markdown extractor
* `articles/` — generated Markdown articles
* `articles/assets/` — extracted images and assets
* `article_manifest.json` — generated article manifest
* `llms.txt` — curated navigation map for LLMs and coding agents

## Generate

Run from the repository root:

```bash
python3 extract_epub.py CO-SDK-manual-25.04.epub \
  --output-dir articles \
  --extract-dir .epub_tmp \
  --manifest article_manifest.json

rm -rf .epub_tmp __pycache__
```

## Notes

* Articles are split by the EPUB table-of-contents structure.
* Images and assets are copied into `articles/assets/`.
* Internal EPUB links are rewritten to local Markdown links where possible.
* Some empty/container TOC parents may not produce standalone Markdown files.
* `llms.txt` is the recommended entrypoint for LLM/RAG use.

## Attribution

Collabora Online and the Collabora Online SDK documentation belong to Collabora.

This repository contains a derived Markdown corpus generated from the Collabora Online SDK Manual 25.04.

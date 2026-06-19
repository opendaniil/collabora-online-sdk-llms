---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id13"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id13"
title: "Screenshot"
canonical_title: "Extract/Transform API / Slides / Screenshot"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Slides / Screenshot"
---
![../_images/SlidesScreenshot.png](assets/_images/SlidesScreenshot.png)

**Image explanation for LLM/RAG:**
This screenshot demonstrates the Extract/Transform API for presentation slides. It shows an original slide deck on the left, a JSON transform in the center, and the resulting slide deck on the right.

**What is explicitly visible:**

* The left side is labeled `Original Document` and shows a deck with five slides.
* The center is labeled `Transform` and shows a JSON-like object containing `SlideCommands`.
* The visible slide commands include operations such as jumping to a slide, moving a slide, renaming a slide, deleting slides, duplicating a slide, inserting a master slide, changing layout, inserting text, and setting text.
* The right side is labeled `Result Document` and shows the transformed deck with seven slides.
* The result deck has reordered, duplicated, inserted, renamed, and modified slides compared with the original deck.

**Why it matters:**
The screenshot shows that presentation slides can be transformed programmatically through structured slide commands. For LLM/RAG use, the key point is that the API can modify a slide deck’s structure and content, not just extract data from it.

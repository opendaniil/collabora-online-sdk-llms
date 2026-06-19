---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#screenshot"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "screenshot"
title: "Screenshot"
canonical_title: "Extract/Transform API / Content Controls / Screenshot"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Content Controls / Screenshot"
---
![../_images/ContentControlScreenshot.png](assets/_images/ContentControlScreenshot.png)

**Image explanation for LLM/RAG:**
This screenshot demonstrates the Extract/Transform API for content controls. It shows an original document on the left, a JSON transform in the center, and the resulting document on the right.

**What is explicitly visible:**

* The left side is labeled `Original Document`.
* The original document contains content controls for plain text, rich text, check box, combo box, drop-down list, and date.
* The center is labeled `Transform` and shows a JSON-like transform object.
* The transform targets content controls by index, tag, alias, and ID.
* The right side is labeled `Result Document`.
* In the result document, the rich text, check box, combo box, drop-down list, and date values have changed.
* One field is reset to `Click here to enter text`.

**Why it matters:**
The screenshot shows that content controls can be updated programmatically through structured transform instructions. For LLM/RAG use, the key point is that the API can locate content controls in different ways and produce a modified result document.

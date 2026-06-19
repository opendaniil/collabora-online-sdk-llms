---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id7"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id7"
title: "Screenshot"
canonical_title: "Extract/Transform API / Document Properties / Screenshot"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Document Properties / Screenshot"
---
![../_images/DocPropertiesExampleScreenShot.png](assets/_images/DocPropertiesExampleScreenShot.png)

**Image explanation for LLM/RAG:**
This screenshot demonstrates the Extract/Transform API for document properties. It shows an original document on the left, a JSON transform in the center, the resulting document on the right, and extracted document structure data from the result.

**What is explicitly visible:**

* The left side shows the original document properties dialog for `docStructureChartExampleOriginal`.
* The original document includes properties tabs such as `General`, `Description`, `Custom Properties`, `Font`, and `Statistics`.
* The center shows a JSON-like transform object for `DocumentProperties`.
* The transform updates metadata fields such as author, title, subject, description, keywords, language, modified date, template fields, and document statistics.
* The transform also adds, overwrites, and deletes custom properties.
* The right side shows the result document properties dialog for `temp2`.
* The result document contains updated general, description, and custom property values.
* The far-right JSON-like block is labeled as extracted from the result document.

**Why it matters:**
The screenshot shows that document metadata can be transformed programmatically and then extracted again from the resulting document. For LLM/RAG use, the key point is that the API can modify built-in document properties, custom properties, and document structure metadata through structured transform instructions.


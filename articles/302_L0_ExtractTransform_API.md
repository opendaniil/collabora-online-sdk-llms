---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: ""
title: "Extract/Transform API"
canonical_title: "Extract/Transform API"
toc_level: "0"
breadcrumbs: "Extract/Transform API"
---
# Extract/Transform Document Structure API

This API was added in Collabora Online version 24.04.5.3

Collabora Online allows you to extract the structure of a Writer or an Impress document, and transform it. The structure is extracted as a JSON document for easy parsing with JavaScript and other languages. The transformation is done following a recipe that is also uploaded as a JSON document.

Currently Collabora Online supports those features only in:

Writer documents:

- Content controls
- Charts
- Document properties
- Tracked changes

Impress documents (presentations):

- Slides

Important

Starting version 24.04.13 some of the JSON data will change. While an attempt it made to ensure compatibility, it is recommended to adapt your code to this new syntax. For more info, check JSON validity changes

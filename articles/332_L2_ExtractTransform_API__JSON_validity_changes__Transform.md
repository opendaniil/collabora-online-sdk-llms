---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id16"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id16"
title: "Transform"
canonical_title: "Extract/Transform API / JSON validity changes / Transform"
toc_level: "2"
breadcrumbs: "Extract/Transform API / JSON validity changes / Transform"
---
On the transform side, while t6he old format is still supported, requiring no changes, it is recommended, whenever possible, to move to the new format that produces a valid JSON document:

All command list like objects (with properties) should be changed to an array of objects with 1-1 property:

| Old format | New format |
| --- | --- |
| “Transforms”: { “Charts.ByEmbedIndex.0”: { | “Transforms”: [ { “Charts.ByEmbedIndex.0”: { |

It affects only 3 items:

- `Transforms`
- `Charts.`
- `UserDefinedProperties`

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id15"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id15"
title: "Extract"
canonical_title: "Extract/Transform API / JSON validity changes / Extract"
toc_level: "2"
breadcrumbs: "Extract/Transform API / JSON validity changes / Extract"
---
Previously, the extraction produced data that was not valid JSON. The following changes are introduced so that the data is now a valid JSON document:

For charts, the `DataValues` values format changed to:

| Old format | New format |
| --- | --- |
| “DataValues”: [ “Row.0”: [ “22”, “24”], “Row.1”: [ “18”, “16”], “Row.2”: [ “32”, “32”], “Row.3”: [ “25”, “23”] ] | “DataValues”: [ [ “22”, “24”], [ “18”, “16”], [ “32”, “32”], [ “25”, “23”] ] |

For slides, the following properties changed from arrays to be objects:

| Old format | New format |
| --- | --- |
| “MasterSlides” [ ] “Slides” [ ] “Objects” [ ] “Texts” [ ] | “MasterSlides” { } “Slides” { } “Objects” { } “Texts” { } |

Their elements are always unique, so they can be object properties. An array cannot have properties directly like it produced previously, causing the data to not be valid JSON.

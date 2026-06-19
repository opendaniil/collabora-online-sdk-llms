---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id8"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id8"
title: "Example Files"
canonical_title: "Extract/Transform API / Document Properties / Example Files"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Document Properties / Example Files"
---
`Original Document`

`Transform JSON`

Command for transform:

```
curl -v -k -F "data=@docStructureChartExampleOriginal.odt" -F "transform=$(cat DocPropTransform.JSON)" https://localhost:9980/cool/transform-document-structure > DocPropResult.odt
```

Command for extract:

```
curl -k -F "data=@temp2.odt" -F "filter=docprops" https://localhost:9980/cool/extract-document-structure > DocPropExtract.JSON
```

`Extracted JSON`

`Extracted JSON Pretty printed`

`Transformed Result Document`

`Screenshot`

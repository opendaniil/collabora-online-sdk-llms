---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id4"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id4"
title: "Example Files"
canonical_title: "Extract/Transform API / Charts / Example Files"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Charts / Example Files"
---
`Original Document`

`Transform JSON`

Command for transform:

```
curl -v -k -F "data=@docStructureChartExampleOriginal.odt" -F "transform=$(cat ChartsTransform.JSON)" https://localhost:9980/cool/transform-document-structure > docStructureChartResult.odt
```

Command for extract:

```
curl -k -F "data=@docStructureChartExampleOriginal.odt" -F "filter=charts" https://localhost:9980/cool/extract-document-structure > ChartsExtractOriginal.JSON
```

`Extracted JSON`

`Extracted JSON Pretty printed`

`Transformed Result Document`

`Screenshot`

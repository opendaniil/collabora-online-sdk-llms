---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id14"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id14"
title: "Example Files"
canonical_title: "Extract/Transform API / Slides / Example Files"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Slides / Example Files"
---
`Original Document`

`Transform JSON`

Command for transform:

```
curl -v -k -F "data=@SlidesExampleOriginal.odp" -F "transform=$(cat SlidesTransform.JSON)" https://localhost:9980/cool/transform-document-structure > SlidesResult.odp
```

Command for extract:

```
curl -k -F "data=@SlidesExampleOriginal.odp" -F "filter=slides" https://localhost:9980/cool/extract-document-structure > SlidesExtractOriginal.JSON
```

`Extracted JSON`

`Extracted JSON Pretty printed`

`Transformed Result Document`

`Screenshot`

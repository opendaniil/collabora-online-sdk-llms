---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#example-files"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "example-files"
title: "Example Files"
canonical_title: "Extract/Transform API / Content Controls / Example Files"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Content Controls / Example Files"
---
`Original Document`

`Transform JSON`

Command for transform:

```
curl -v -k -F "data=@contentControlsExampleOriginal.odt" -F "transform=$(cat contentControlsTransform.JSON)" https://localhost:9980/cool/transform-document-structure > contentControlsResult.odt
```

Command for extract:

```
curl -k -F "data=@contentControlsExampleOriginal.odt" -F "filter=contentcontrol" https://localhost:9980/cool/extract-document-structure > contentControlsOriginalExtract.JSON
curl -k -F "data=@contentControlsResult.odt" -F "filter=contentcontrol" https://localhost:9980/cool/extract-document-structure > contentControlsResultExtract.JSON
```

`Extracted JSON from result odt`

`Extracted JSON from result odt, Pretty printed`

`Extracted JSON from original odt, Pretty printed`

`Transformed Result Document`

`Screenshot`

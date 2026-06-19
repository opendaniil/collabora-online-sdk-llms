---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id10"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id10"
title: "Example Files"
canonical_title: "Extract/Transform API / Tracked changes / Example Files"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Tracked changes / Example Files"
---
`Original Document`

Command for extract:

```
curl -F "data=@trackedChangesExampleOriginal.fodt" -F "filter=trackchanges,contextLen:100,startPageNumber:true" https://localhost:9980/cool/extract-document-structure > trackedChangesExampleOriginal.json
```

`Extracted JSON from original fodt, Pretty printed`

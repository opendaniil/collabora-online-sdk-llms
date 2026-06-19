---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/linking_api.xhtml"
source_file: "docs/linking_api.xhtml"
source_anchor: ""
title: "Linking API"
canonical_title: "Linking API"
toc_level: "0"
breadcrumbs: "Linking API"
---
Collabora Online allows you to extract list of objects inside document you can link to. Received targets can be then used to open document at specific position or generate it’s thumbnail.

> **API:** HTTP POST to `/cool/extract-link-targets`

- the file itself in the payload.

Example:

```
curl -F "data=@file.docx" https://localhost:9980/cool/extract-link-targets > targets.json
```

Example output:

```
{
    "Targets": {
        "Tables": {
            "Table1": "Table1|table"
        },
        "Frames": {},
        "Images": {
            "image7.png": "image7.png|graphic"
        },
        "OLE objects": {},
        "Sections": {
            "Table of Contents1": "Table of Contents1|region"
        },
        "Headings": {},
        "Bookmarks": {
            "_lh2zfxamp5al": "_lh2zfxamp5al"
        },
        "Drawing objects": {}
    }
}
```

Hint

You can open document at specific target by using additional URL parameter for example: `&target=Table1|table`

> **API:** HTTP POST to `/cool/get-thumbnail`

- the file itself in the payload.
- optional: target parameter for which we want to generate thumbnail `Table1|table`

Example:

```
curl -F "data=@file.docx" -F "target=Table1|table" https://localhost:9980/cool/get-thumbnail > thumb.png
```

Important

The endpoints are restricted to allowed host addresses that can be set in the `/etc/coolwsd/coolwsd.xml` configuration file. The IP addresses have to be added as dot-escaped `net.post_allow.host` entries.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#pdf-export"
source_file: "docs/conversion_api.xhtml"
source_anchor: "pdf-export"
title: "PDF Export"
canonical_title: "Conversion API / Examples / PDF Export"
toc_level: "2"
breadcrumbs: "Conversion API / Examples / PDF Export"
---
In the following, more complex PDF conversion example the page 1 and pages from 8 to 30 are extracted from a book, a red watermark is put across the pages in 45° saying “DO NOT DISTRIBUTE”, and the output document can only be opened with a password “S3cret”.

```
{
    "PageRange": {
        "type": "string",
        "value": "1,8-30"
    },
    "Watermark": {
        "type": "string",
        "value": "DO NOT DISTRIBUTE"
    },
    "WatermarkColor": {
        "type": "long",
        "value": "16711680"
    },
    "WatermarkRotateAngle": {
        "type": "long",
        "value": "450"
    },
    "EncryptFile": {
        "type": "boolean",
        "value": "true"
    },
    "DocumentOpenPassword": {
        "type": "string",
        "value": "S3cret"
    }
}
```

```
curl -k -F "data=@Book.pdf" -F "format=pdf" -F "options={\"PageRange\":{\"type\":\"string\",\"value\":\"1,8-30\"},\"Watermark\":{\"type\":\"string\",\"value\":\"DO NOT DISTRIBUTE\"},\"WatermarkColor\":{\"type\":\"long\",\"value\":\"16711680\"},\"WatermarkRotateAngle\":{\"type\":\"long\",\"value\":\"450\"},\"EncryptFile\":{\"type\":\"boolean\",\"value\":\"true\"},\"DocumentOpenPassword\":{\"type\":\"string\",\"value\":\"S3cret\"}}" http://localhost:9980/cool/convert-to > out.pdf
```

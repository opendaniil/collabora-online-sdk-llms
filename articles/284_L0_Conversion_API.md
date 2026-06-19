---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml"
source_file: "docs/conversion_api.xhtml"
source_anchor: ""
title: "Conversion API"
canonical_title: "Conversion API"
toc_level: "0"
breadcrumbs: "Conversion API"
---
Collabora Online allows you to convert between various file formats easily. To do so, all you need to do is to HTTP POST the content of the file to the specific endpoint and send optional parameters to change the defaults of the conversion process.

> **API:** HTTP POST to `/cool/convert-to/<format>`

Important

The `convert-to` endpoint is restricted to allowed host addresses that can be set in the `coolwsd.xml` configuration file. The IP addresses have to be added as dot-escaped `net.post_allow.host` entries.

Note

Alternatively you can omit the `<format>`, and instead provide it as another parameter (`format=<format>`).

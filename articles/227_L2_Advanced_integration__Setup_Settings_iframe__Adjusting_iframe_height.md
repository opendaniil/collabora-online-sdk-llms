---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#adjusting-iframe-height"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "adjusting-iframe-height"
title: "Adjusting iframe height"
canonical_title: "Advanced integration / Setup Settings iframe / Adjusting iframe height"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Adjusting iframe height"
---
To make the iframe appear seamless (i.e. without scrollbars), Collabora Online sends an `Iframe_Height` postMessage to adjust the height of the embedded iframe. For more details, see [Setting Iframe](257_L0_PostMessage_API.md) in the PostMessage API documentation.

Example:

```
{
  "MessageId": "Iframe_Height",
  "Values": {
    "ContentHeight": "1000px"
  }
}
```

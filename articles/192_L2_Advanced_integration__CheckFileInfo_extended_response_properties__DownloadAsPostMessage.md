---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#downloadaspostmessage"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "downloadaspostmessage"
title: "DownloadAsPostMessage"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / DownloadAsPostMessage"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / DownloadAsPostMessage"
---
Indicate that the integration wants to handle the downloading of pdf for printing or svg for slideshows or exported document, because it cannot rely on browser’s support for downloading.

When this is set to true, the user’s eg. Print action will trigger a postMessage called [Download_As](257_L0_PostMessage_API.md), with the following JSON in the Values:

```
{ Type: 'print'|'slideshow'|'export', URL: ...url you use for the actual downloading... }
```

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#saveaspostmessage"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "saveaspostmessage"
title: "SaveAsPostmessage"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / SaveAsPostmessage"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / SaveAsPostmessage"
---
Similar to download as, doctype extensions can be provided for save-as. In this case the new file is loaded in the integration instead of downloaded.

```
{format: '<extension>' }
```

To achieve this, `args: {format: '<extension>' }` parameter needs to be sent inside [UI_SaveAs](257_L0_PostMessage_API.md). The integration should provide dialog with filename, there the extension will be set after the filename. The remaining work is already handled by save-as.

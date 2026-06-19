---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#override-checkfileinfo"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "override-checkfileinfo"
title: "Override CheckFileInfo"
canonical_title: "Advanced integration / Override CheckFileInfo"
toc_level: "1"
breadcrumbs: "Advanced integration / Override CheckFileInfo"
---
DownloadAsPostMessage property of the CheckFileInfo can be overridden. This is controlled by:

```
<input name="checkfileinfo_override" value="DownloadAsPostMessage=VALUE" type="hidden"/>
```

during sending the form when the iframe is being set up (similarly as the access_token). The VALUE can be either true or false. This will override `DownloadAsPostMessage` value from CheckFileInfo response.

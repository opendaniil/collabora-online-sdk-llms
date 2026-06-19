---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#sharedsettings"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "sharedsettings"
title: "SharedSettings"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / SharedSettings"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / SharedSettings"
---
Used to provide shared or system-wide settings (commonly managed by administrators). The format is similar to UserSettings and should follow the same structure.

**Example:**

```
{
  "url": "<base_url>/wopi/settings?access_token=<token>&type=systemconfig&fileId=-1",
  "stamp": "<valid_stamp>"
}
```

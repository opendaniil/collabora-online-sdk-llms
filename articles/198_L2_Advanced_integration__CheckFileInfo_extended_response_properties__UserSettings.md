---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#usersettings"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "usersettings"
title: "UserSettings"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / UserSettings"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / UserSettings"
---
Provides a URL to fetch the user’s personal settings using the settings iframe. This must be integrated with the Settings iframe feature.

The URL should include required parameters, as documented in Fetch settings. The `stamp` should reflect the last update time of the settings (commonly a timestamp or hash). It should only change when the settings have been modified. If the stamp changes without actual updates, Collabora Online will unnecessarily re-fetch the settings from your WOPI host.

**Example:**

```
{
  "url": "<base_url>/wopi/settings?access_token=<token>&type=userconfig&fileId=-1",
  "stamp": "<valid_stamp>"
}
```

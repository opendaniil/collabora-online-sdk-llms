---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#browser-settings"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "browser-settings"
title: "Browser settings"
canonical_title: "Advanced integration / Setup Settings iframe / Browser settings"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Browser settings"
---
Collabora Online can persist user-specific interface preferences (e.g., dark mode, UI element visibility) using the WOPI host storage. This replaces browser local storage, ensuring settings are consistent across user sessions and devices.

These browser settings are handled as files, interacting with the WOPI host setting endpoints:

1. **Saving Preferences**: When UI preferences change, Collabora Online sends the updated browser settings file to the WOPI host using the POST mechanism from Upload settings (typically `POST https://<WOPI host URL>/<...>/wopi/settings/upload`). The `fileId` in the request targets a path `/settings/userconfig/browsersettting/browsersetting.json`.
2. **Loading Preferences**: For Collabora Online to load these settings, the WOPI host Fetch settings GET response (typically `GET https://<WOPI host URL>/<...>/wopi/settings?access_token=<token>&type=userconfig&fileId=-1`) must include an entry for the browser settings file under the `"browsersetting"` key, providing its `stamp` and `uri`.

Example of added “browsersetting” object in userconfig json

```
{
    "kind": "user",
    "autotext": [
        {
            "stamp": "cd7832c07eba1cb0e282acbb0f22bd13",
            "uri": "https://<WOPI host URL>/<...>/autotext/test.bau"
        }
    ],
    "xcu": [
        {
            "stamp": "f2ffd58fb9c8e86359d33ec0c7a28c15",
            "uri": "https://<WOPI host URL>/<...>/xcu/documentView.xcu"
        }
    ],
    "browsersetting": [
        {
            "stamp": "f2ffd58fb9c8e86359d33ec0c7a28c15",
            "uri": "https://<WOPI host URL>/settings/userconfig/browsersetting/browsersetting.json"
        }
    ]
}
```

The content of this settings file is a JSON object. The structure typically includes a general `darkTheme` preference and module-specific UI states for `presentation`, `spreadsheet`, and `text` documents, as illustrated below:

Example JSON for Persisted Browser Settings

```
{
  "darkTheme": "true",
  "presentation": {
    "A11yCheckDeck": "false",
    "NavigatorDeck": "false",
    "PropertyDeck": "true",
    "ShowSidebar": "true",
    "ShowStatusbar": "true",
    "StyleListDeck": "false"
  },
  "spreadsheet": {
    "A11yCheckDeck": "false",
    "NavigatorDeck": "false",
    "PropertyDeck": "true",
    "ShowSidebar": "true",
    "ShowStatusbar": "true",
    "StyleListDeck": "false"
  },
  "text": {
    "A11yCheckDeck": "false",
    "NavigatorDeck": "false",
    "PropertyDeck": "true",
    "ShowSidebar": "true",
    "ShowStatusbar": "true",
    "StyleListDeck": "false"
  }
}
```

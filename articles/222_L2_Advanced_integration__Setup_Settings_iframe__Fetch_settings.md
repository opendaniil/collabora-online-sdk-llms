---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#fetch-settings"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "fetch-settings"
title: "Fetch settings"
canonical_title: "Advanced integration / Setup Settings iframe / Fetch settings"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Fetch settings"
---
In order to fetch settings, the WOPI client (Collabora Online) expects the following endpoint:

```
GET https://<WOPI host URL>/<...>/wopi/settings?access_token=<token>&type=<type>&fileId=-1
```

Here, `<type>` is either `userconfig` or `systemconfig`, accordingly.

This endpoint is expected to return JSON in the following format:

```
{
    kind: < 'shared' || 'user' >,
    <Any Settings> : [
        {
            stamp: <etag>
            uri: <file url>
        }
        ....
    ]
}
```

New in version 25.04.7.1.

Note

You can override the displayed filename in the iframe UI by adding `file_name=<desired_name>` as a query parameter in the settings file URI. This affects only how the file name appears in the UI; the file content and actual URL remain unchanged.

Here, the `kind` should be set to `shared` if it’s an admin iframe and `user` if it’s a user iframe. Every setting must include a list of object which contains stamp and uri.

Below is a sample JSON structure for a `user` iframe:

```
{
    "kind": "user",
    "autotext": [
        {
            "stamp": "cd7832c07eba1cb0e282acbb0f22bd13",
            "uri": "<Wopi Host>/autotext/test.bau"
        }
    ],
    "xcu": [
        {
            "stamp": "f2ffd58fb9c8e86359d33ec0c7a28c15",
            "uri": "<Wopi Host>/xcu/documentView.xcu"
        }
    ],
}
```

Note

We use the stamp value to manage caching for each settings file. **Always update the stamp when the corresponding file has changed to invalidate the cache.**

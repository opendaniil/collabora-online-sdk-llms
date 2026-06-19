---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#delete-settings-file"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "delete-settings-file"
title: "Delete settings file"
canonical_title: "Advanced integration / Setup Settings iframe / Delete settings file"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Delete settings file"
---
To delete a settings file, make a DELETE request to the following endpoint:

```
DELETE https://<WOPI host URL>/<...>/wopi/settings?access_token=<token>&fileId=<fileId>
```

The `fileId` should follow the same path format as used for upload, for example:`/settings/{TYPE}/{SETTING_NAME}/{FILE_NAME}.{FILE_EXTENSION}`

The endpoint should return a JSON response similar to:

```
{
    "status": "success",
    "message": "<success_message>"
}
```

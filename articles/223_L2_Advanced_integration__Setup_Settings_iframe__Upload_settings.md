---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#upload-settings"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "upload-settings"
title: "Upload settings"
canonical_title: "Advanced integration / Setup Settings iframe / Upload settings"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Upload settings"
---
Collabora Online iframe always sends settings as a file, which can be uploaded as follows:

```
POST https://<WOPI host URL>/<...>/wopi/settings/upload?access_token=<token>&fileId=<fileId>&file=<file>
```

Along with the `access_token`, the setting iframe sends:

- `fileId`: The file path, formatted as: `/settings/{TYPE}/{SETTING_NAME}/{FILE_NAME}.{FILE_EXTENSION}`
  > - `{TYPE}`: Either `userconfig` or `systemconfig`
  > - `{SETTING_NAME}`: The setting name provided by the setting iframe (e.g., wordbook, autotext)
  > - `{FILE_NAME}.{FILE_EXTENSION}`: The file name with its extension, used later to uniquely identify the file.
- `file`: The setting file to be uploaded.

**Note:** If multiple requests are received with the same `fileId`, the file should be overridden in storage and stored as a new file.

For example, a valid `fileId` would be: `/settings/userconfig/wordbook/en_US.dic`

This file should be stored inside the directory `userconfig/wordbook` with the file name `en_US.dic`.

The upload route should return JSON similar to the following example:

```
{
    "status": "success",
    "filename": "<file_name>",
    "details": {
        "stamp": "<stamp>",
        "uri": "<file_url>"
    }
}
```

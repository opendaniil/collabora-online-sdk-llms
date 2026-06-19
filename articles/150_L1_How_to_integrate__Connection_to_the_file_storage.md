---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/How_to_integrate.xhtml#connection-to-the-file-storage"
source_file: "docs/How_to_integrate.xhtml"
source_anchor: "connection-to-the-file-storage"
title: "Connection to the file storage"
canonical_title: "How to integrate / Connection to the file storage"
toc_level: "1"
breadcrumbs: "How to integrate / Connection to the file storage"
---
As the *WOPI host*, your existing solution has to implement few entry points for Collabora Online (the *WOPI client*), so that Collabora Online can download files that the user wants to edit, and upload back the updates.

The *WOPI client* (Collabora Online) invokes the WOPI url created above to download the file:

```
GET https://<WOPI host URL>/<...>/wopi/files/<id>/contents?access_token=<token>
```

And to upload a file:

```
POST https://<WOPI host URL>/<...>/wopi/files/<id>/contents?access_token=<token>
```

Currently, Collabora Online only depends on WOPI File Operation functions (GetFile/PutFile/CheckFileInfo). As a bare minimum, your application has to support the following four functions:

1. A function that generates a token for a given file and user (probably you want to store that in a DB, optionally with expiration).
2. **GetFile** that sends back the content of the file when the
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>/contents?access_token=<token>
  ```

3. **PutFile** that replaces the file with the body of the POST verb when invoked with the
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>/contents?access_token=<token>
  ```
  URL.
  - An optional LastModifiedTime field, containing the ISO8601 round-trip time format indicating the new/updated file’s modified time in storage after successful save, can be added to the JSON response. See Further differences to WOPI for more details.

4. (Optional) **PutRelativeFile** that creates a new file with the body of the POST verb for the needs of the Save As operation when invoked with
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>?access_token=<token>
  ```
  URL. If you do not want to support the Save As operation, please add **UserCanNotWriteRelative** with value **true** to your CheckFileInfo answer.
  It requires the request header `X-WOPI-Override` to contain the value `PUT_FILE` and the header `X-WOPI-SuggestedTarget` is the full file name (including the extension). It is a string encoded in UTF-7.

5. (Optional) **RenameFile** that rename the document. Use the POST verb with
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>?access_token=<token>
  ```
  URL. It requires the request header `X-WOPI-Override` to contain the value `RENAME_FILE` and the header `X-WOPI-RequestedName` to contain the new file name **without extension**. The string encoding is UTF-7. See [Microsoft 365 documentation](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/files/renamefile) [https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/files/renamefile] for more details.

Important

If the integration supports renaming files by implementing RenameFile, the WOPI response property [SupportsRename](169_L2_Advanced_integration__CheckFileInfo_response_properties__SupportsRename.md) in CheckFileInfo should be set to **true**.

6. **CheckFileInfo** that returns (at least) the BaseFileName and Size of the file as json when the
  ```
  https://<WOPI host URL>/<...>/wopi/files/<id>?access_token=<token>
  ```
  URL is invoked. Collabora Online takes the following required CheckFileInfo properties:
  - `BaseFileName` – The string name of the file without a path. Used for display in user interface (UI), and determining the extension of the file.
  - `OwnerId` – A string that uniquely identifies the owner of the file.
  - `Size` – The size of the file in bytes, expressed as a long, a 64-bit signed integer.
  - `UserId` – A string value uniquely identifying the user currently accessing the file.
  Collabora Online takes the following optional CheckFileInfo properties:
  - `UserFriendlyName` – The name of the user, suitable for displaying on the UI.
  - `UserCanWrite` – It has to be set to true if the file is opened for editing.
  - `UserCanNotWriteRelative` - Set to `true` (default) if the user can not write a file relative to the open document. This mean disabling Save As.
  - `PostMessageOrigin` – It is used by [PostMessage API](257_L0_PostMessage_API.md).
  - `HidePrintOption` – Hides print button from UI but accessible using [PostMessage API](257_L0_PostMessage_API.md) so hosts can implement their own UI for this.
  - `DisablePrint` – Disables printing of documents. Additionally, hides print option from UI.
  - `HideSaveOption` – Hides save button from UI. Manual save can still triggered using [PostMessage API](257_L0_PostMessage_API.md). Does not affect automatic save.
  - `HideExportOption` – Hides ‘Download as’ button/menubar item from UI. Can still be triggered using [PostMessage API](257_L0_PostMessage_API.md).
  - `HideRepairOption` - hide the repair button.
  - `DisableExport` – Disable export of the document in any format. Additionally, hides the ‘Download as’ button from the UI.
  - `DisableCopy` – Disable copying from the document.
  - `EnableOwnerTermination` – This gives document owners the ability to terminate all sessions currently having that document opened.
  - `LastModifiedTime` – ISO8601 round-trip time format for file’s last modified time in storage.
  - `IsUserLocked` – Lock the user from using certain feature(s) which can be later be unlock by user.
  - `IsUserRestricted` – Disable feature(s) for the user.
  - `SupportsRename` - Set to false (default) if renaming isn’t supported. However renaming might still be possible in the UI is `UserCanNotWriteRelative` is false.
  - `UserCanRename` - Set to false (default) if the user can not rename the file. Requires `SupportsRename` to be true.

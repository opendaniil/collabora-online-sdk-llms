---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/How_to_integrate.xhtml#further-differences-to-wopi"
source_file: "docs/How_to_integrate.xhtml"
source_anchor: "further-differences-to-wopi"
title: "Further differences to WOPI"
canonical_title: "How to integrate / Further differences to WOPI"
toc_level: "1"
breadcrumbs: "How to integrate / Further differences to WOPI"
---
In addition to the basics of WOPI as described in [WOPI specifications](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/) [https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/], Collabora Online implements various extensions, in addition to those outlined above primarily associated with CheckFileInfo, to support some features that you may find useful.

1. **Custom Button API**: It is possible to add your own custom buttons to the editor’s UI. For more information, you can check [insert_button](257_L0_PostMessage_API.md) and [clicked_button](257_L0_PostMessage_API.md) API [PostMessage API](257_L0_PostMessage_API.md).
2. **Detecting external document change**: In some cases, when the document is updated in your storage while being edited in Collabora Online and there are unsaved changes, we detect it as soon as possible and ask the user if he/she would like to overwrite the changes or reload the new document from the storage.
  In case there are no unsaved changes, we reload the new document without asking the user.
  To be able to support this feature, you need to specify LastModifiedTime field in both CheckFileInfo and PutFile calls as described above in its documentation.
  Additionally, WOPI hosts must check for a header in PutFile response – `X-COOL-WOPI-Timestamp`. This header contains the ISO8601 round-trip formatted time of file’s last modified time in storage, as known by Collabora Online. In case, this header is present and its value doesn’t match with the file’s modified time in storage, it indicates that document being edited is not the one that is present in the storage. WOPI hosts should not save the file to storage in such cases and respond with [HTTP 409](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/409) [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/409] along with Collabora Online specific status code for this purpose in JSON response against the field *COOLStatusCode*. The COOLStatusCode for this purpose is 1010. So, the desired response should be:
   HTTP 409 with JSON
  ```
  1{
  2    'COOLStatusCode': 1010
  3}
  ```

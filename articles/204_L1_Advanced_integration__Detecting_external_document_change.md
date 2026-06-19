---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#detecting-external-document-change"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "detecting-external-document-change"
title: "Detecting external document change"
canonical_title: "Advanced integration / Detecting external document change"
toc_level: "1"
breadcrumbs: "Advanced integration / Detecting external document change"
---
Locking is omitted from our WOPI-like protocol since it goes against common EFSS solutions usage. Instead, Collabora Online uses timestamps to detect document changes.

When the document is updated in your storage while being edited in Collabora Online and there are unsaved changes, we detect it as soon as possible and ask the user if he/she would like to overwrite the changes or reload the new document from the storage.

In case there are no unsaved changes, we reload the new document without asking the user.

To support this feature, the host implementation has to specify [LastModifiedTime](146_L0_How_to_integrate.md) field in both CheckFileInfo and PutFile calls.

Additionally, hosts must check for a header in PutFile response:

```
X-COOL-WOPI-Timestamp
```

This header contains the ISO8601 round-trip formatted time of file’s last modified time in storage, as known by Collabora Online. In case this header is present and its value does not match the file’s modified time in storage, it indicates that document being edited is not the one that is present in the storage.

Hosts should not save the file to storage in such cases and respond with HTTP 409 along with Collabora Online specific status code:

HTTP 409 with JSON

```
1 {
2     'COOLStatusCode': 1010
3 }
```

When the user chooses “overwrite” when asked how to resolve the conflict, Collabora Online will attempt one more save operation, but this time it will lack the `X-COOL-WOPI-Timestamp` header, which means “save regardless of state of the file”.

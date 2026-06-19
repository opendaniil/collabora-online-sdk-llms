---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id3"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id3"
title: "WOPI host to editor"
canonical_title: "PostMessage API / Version Restore / WOPI host to editor"
toc_level: "2"
breadcrumbs: "PostMessage API / Version Restore / WOPI host to editor"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Host_VersionRestore | Status: <string> | The Only possible value is Pre_Restore. This message is sent by the host before actually restoring the document and after user showed the intent to restore the document. This is so such that if there are any unsaved changes, Online can save them to storage before document is restored. |

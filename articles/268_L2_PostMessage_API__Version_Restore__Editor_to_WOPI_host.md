---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id4"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id4"
title: "Editor to WOPI host"
canonical_title: "PostMessage API / Version Restore / Editor to WOPI host"
toc_level: "2"
breadcrumbs: "PostMessage API / Version Restore / Editor to WOPI host"
---
| MessageId | Values | Description |
| --- | --- | --- |
| App_VersionRestore | Status: <string> | This is the reply for the Host_VersionRestore message. Possible values for Status (for now) is: Pre_Restore_Ack. It means that host can go ahead with restoring the document to an earlier revision. |

Note

These messages are only emitted if *App_LoadingStatus* contains *VersionStates* in *Features*. Otherwise, host can immediately restore the version to earlier revision.

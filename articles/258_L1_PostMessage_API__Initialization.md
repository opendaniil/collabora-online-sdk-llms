---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#initialization"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "initialization"
title: "Initialization"
canonical_title: "PostMessage API / Initialization"
toc_level: "1"
breadcrumbs: "PostMessage API / Initialization"
---
Editor to WOPI host

| MessageId | Values | Description |
| --- | --- | --- |
| App_LoadingStatus | Status: <String> DocumentLoadedTime: <Timestamp> | If status is Frame_Ready, Collabora Online frame is loaded and UI can be shown. Accompanying keys: Features: This client’s capabilities. Supported values are: VersionStates: Tells the host that client supports different version states. See Version Restore for more details. When Status is Document_Loaded, document has been completely loaded and host can also start using PostMessage API. Accompanying keys: DocumentLoadedTime. When Status is Failed, document hasn’t been loaded but host can show the Collabora Online frame to present an error for a user. When Status is Initialized, postMessage listener in editor has been initialized. WOPI host can start to send postMessages. It is used to send early postMessages even before Frame_Ready. |

WOPI host to editor

| MessageId | Values | Description |
| --- | --- | --- |
| Host_PostmessageReady |  | See WOPI docs for details. |

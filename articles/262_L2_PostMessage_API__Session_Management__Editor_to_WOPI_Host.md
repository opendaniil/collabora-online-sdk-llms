---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#editor-to-wopi-host"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "editor-to-wopi-host"
title: "Editor to WOPI Host"
canonical_title: "PostMessage API / Session Management / Editor to WOPI Host"
toc_level: "2"
breadcrumbs: "PostMessage API / Session Management / Editor to WOPI Host"
---
| MessageId | Values | Description |
| --- | --- | --- |
| View_Added | ViewId: <Number> UserId: <String> UserName: <String> Color: <Number> ReadOnly:<Boolean> Deprecated: true; | A new member is added. ViewId is unique integer identifying a session/view. UserId is user identity. UserName is display name of the user. Color is RGB color integer value. ReadOnly tells if the new view is opened as read-only. This message is deprecated, opened as read-only. This message is deprecated, instead implement just handling of Views_List which holds the same payload as Get_Views_Resp. |
| View_Removed | ViewId: <Number> Deprecated: true; | View with ViewId has closed the document. This message is deprecated, instead implement just handling of Get_Views_Resp and if you need the info which view has been added / removed, check against the previous state. This message is deprecated, instead implement just handling of Views_List which holds the same payload as Get_Views_Resp. |
| Session_Closed | Reason: <String> | The session has closed. The reason fied details the origin: OwnerTermination, DocumentIdle, OOM Out-of-memory, ShuttingDown server is shutting down for maintenance, DocumentDisconnected an issue with the document |
| Views_List | See Get_Views_Resp. | Complete information about the currently connected views. |
| User_Idle |  | Indicates that user become idle. It happens after longer inactivity time defined in the configuration file /etc/coolwsd/coolwsd.xml |
| User_Active |  | Indicates that user become active again. It happens after user clicked on the idle screen. |

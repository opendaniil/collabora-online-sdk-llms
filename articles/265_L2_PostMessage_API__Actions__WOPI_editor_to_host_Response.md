---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#wopi-editor-to-host-response"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "wopi-editor-to-host-response"
title: "WOPI editor to host (Response)"
canonical_title: "PostMessage API / Actions / WOPI editor to host (Response)"
toc_level: "2"
breadcrumbs: "PostMessage API / Actions / WOPI editor to host (Response)"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Action_Load_Resp | success: <boolean> result: <string> errorMsg: <string> errorType: <string> | Acknowledgment when load finishes. success tells if COOL was able to load the document successfully. result contains the reason the document was not loaded. errorMsg contains a detailed error message in case loading failed. Probably it will contain the error message returned from the WOPI host. errorType contains optional error identifier based on which WOPI host can customize error message. |
| Action_Save_Resp | success: <boolean> result: <string> errorMsg: <string> fileName: <string> | Acknowledgment when save finishes. This response is only emitted if Notify parameter is mentioned by Action_Save PostMessage API. success tells if COOL was able to save the document successfully. result contains the reason the document was not saved. In case, document was not saved because it was not modified, then this parameter contains the string ‘unmodified’. In this case, WOPI hosts can be sure that there are no changes pending in the document to be saved to the storage. errorMsg contains a detailed error message in case saving failed. Probably it will contain the error message returned from the WOPI host. fileName if success equals true then contains saved file name. |
| FollowUser_Changed | FollowedViewId: <Number> IsFollowUser: <Boolean> IsFollowEditor: <Boolean> | Notification about current following state. FollowedViewId tells which user is followed. IsFollowUser determines if following the specific user is activated. IsFollowEditor determines if following the editor is activated. If both IsFollowUser and IsFollowEditor are false then following is inactive. |
| Action_ChangeUIMode_Resp | Mode: <string> | Notification about UI mode switch (Tabbed/Compact) Mode tells which mode will be used. |
| Action_GoToComment_Resp | Id: <string> success: <boolean> errorMsg: <string> | New in version 25.04.10.3. Response to Action_GoToComment. Id echoes back the comment identifier from the request. success indicates whether the navigation succeeded. errorMsg is present only when success is false, and describes the reason for failure (e.g. comment not found). |

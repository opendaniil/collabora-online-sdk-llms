---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id9"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id9"
title: "WOPI host to editor"
canonical_title: "PostMessage API / Comments / WOPI host to editor"
toc_level: "2"
breadcrumbs: "PostMessage API / Comments / WOPI host to editor"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Action_ResolveComment | Id: <string> | Marks the comment identified by Id as resolved. If the comment is already resolved, this message has no effect. Only supported in Writer documents. |
| Action_GoToComment | Id: <string> | New in version 25.04.10.3. Navigates to the comment identified by Id. Scrolls the document to make the comment visible and places the cursor at the comment’s anchor. In Calc, this includes switching to the correct sheet if necessary. Supported in Writer and Calc. Response is returned in form of Action_GoToComment_Resp. |
| Get_Comments |  | New in version 25.04.10.3. Queries the editor for all comments in the document. Response is returned in form of Get_Comments_Resp. |

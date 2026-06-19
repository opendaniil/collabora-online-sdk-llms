---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id10"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id10"
title: "Editor to WOPI host"
canonical_title: "PostMessage API / Comments / Editor to WOPI host"
toc_level: "2"
breadcrumbs: "PostMessage API / Comments / Editor to WOPI host"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Clicked_Comment | Id: <string> | This event is emitted when the user clicks on a comment in the document. Id is the identifier of the clicked comment. Supported in Writer, Calc, and Impress. |
| Get_Comments_Resp | Comments: [ { Id: <String> Author: <String> DateTime: <String> Text: <String> Resolved: <Boolean> Parent: <String> } ] | New in version 25.04.10.3. Response to query Get_Comments. Comments is an array of objects with the following properties: Resolved and Parent are optional: present for Writer comments and Calc threaded comments, absent for Calc notes. DateTime is in ISO 8601 format. Parent is “0” for root comments. |

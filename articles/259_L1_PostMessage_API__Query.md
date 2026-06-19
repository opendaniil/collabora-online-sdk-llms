---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#query"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "query"
title: "Query"
canonical_title: "PostMessage API / Query"
toc_level: "1"
breadcrumbs: "PostMessage API / Query"
---
You can query data from the editor using post message API. All responses are returned with query’s MessageId suffixed with ‘_Resp’ as shown below Getters

WOPI Host to Editor

| MessageId | Values | Description |
| --- | --- | --- |
| Get_Views |  | Queries the editor for currently active views of the document. Response is returned in form of Get_Views_Resp |
| Get_Export_Formats |  | Queries the editor for all the supported export formats for currently opened document. Response is returned in form of Get_Export_Formats_Resp |
| Get_User_State |  | Queries the editor for current user activity state (is idle or active). Response is returned in form of Get_User_State_Resp |

Getters response

Editor to WOPI host

| MessageId | Values | Description |
| --- | --- | --- |
| Get_Views_Resp | ViewId: <Number> UserId: <String> UserName: <String> Color: <Number> ReadOnly: <Boolean> IsCurrentView: <Boolean> | Give details of all current views when queried using Get_Views |
| Get_Export_Formats_Resp | Label: <String> Format: <String> | Response to query Get_Export_Formats. Label would contain a localized string explaining about the format. Format is the file extension of the format which is required while requesting export of the document. |
| Get_User_State_Resp | State: <String> Elapsed: <Number> | Response to query Get_User_State. State would contain a non-localized string with the activity state (“active” or “idle”). Elapsed is the number of seconds since the last activity of the user. |
| Action_Copy_Resp | content: <String> | New in version 25.04.8.1. Give content of the current text selection when queried using Action_Copy. |

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id9"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id9"
title: "Extract"
canonical_title: "Extract/Transform API / Tracked changes / Extract"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Tracked changes / Extract"
---
Use `filter=trackchanges` to extract the tracked changes list. The filter string may optionally contain arguments after a comma, as a sequence of name:value pairs, separated by commas. The supported arguments are:

| Argument | Description |
| --- | --- |
| contextLen | A non-negative integer, defines maximum text length in textBefore and textAfter (see below). Default is 200. |
| startPageNumber | New in version 25.04.6.1. When true, the result includes startPageNumber properties, with numbers of pages where the changes start. Default is false. |

Example output (pretty printed):

```
{
    "DocStructure": {
        "TrackChanges.ByIndex.0": {
            "type": "Delete",
            "dateTime": "2025-06-12T14:15:21",
            "author": "John Doe",
            "description": "Delete “Foo”",
            "comment": "Some comment",
            "startPageNumber": 1,
            "textBefore": " preceding text 1, up to contextLen characters ...",
            "textAfter": " following text 1, up to contextLen characters ...",
            "textChanged": "Foo",
        },
        "TrackChanges.ByIndex.1": {
            "type": "Insert",
            "dateTime": "2025-06-12T14:15:24",
            "author": "Jane Smith",
            "description": "Insert “Bar”",
            "comment": "Another comment",
            "startPageNumber": 1,
            "textBefore": " preceding text 2, up to contextLen characters ...",
            "textAfter": " following text 2, up to contextLen characters ...",
            "textChanged": "Bar",
        },
        "TrackChanges.ByIndex.2": {
            "type": "Format",
            "dateTime": "2025-06-12T14:15:31",
            "author": "Jane Smith",
            "description": "Attributes changed",
            "comment": "",
            "startPageNumber": 1,
            "textBefore": " preceding text 3, up to contextLen characters ...",
            "textAfter": "",
            "textChanged": "Baz",
        },
    }
}
```

Each tracked change is defined by its properties. `type`, `dateTime`, `author`, `description`, `comment`, `textBefore`, `textAfter`, `textChanged` are present (some may be empty) for every tracked change:

| Property | Description |
| --- | --- |
| type | One of the types listed in the following table. |
| dateTime | ISO 8601 datetime string, when the change was made. |
| author | The name of the author of the change. |
| description | Brief auto-generated description, may include (part of) added or removed text. |
| comment | A comment to the change that a reviewer made. |
| startPageNumber | New in version 25.04.6.1. The number of page where the change starts. |
| textBefore | The text in the document, that immediately precedes the change. Up to contextLen characters long. It shows the text in the state it was at the moment when the change occured; i.e., all older changes are shown as if accepted; all later changes are shown as if rejected. |
| textAfter | The text in the document, that goes immediately after the change. Up to contextLen characters long. It shows the text in the state it was at the moment when the change occured; i.e., all older changes are shown as if accepted; all later changes are shown as if rejected. |
| textChanged | The text in the document, that constitutes the change (an added, inserted, or formatted text) in full. |

Tracked change types:

| Type | Content properties |
| --- | --- |
| Insert | A text was added to the document. |
| Delete | A text was deleted from the document. |
| Format | Formatting of a part of the existing text was changed. |

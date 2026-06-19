---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id1"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id1"
title: "WOPI host to editor"
canonical_title: "PostMessage API / Actions / WOPI host to editor"
toc_level: "2"
breadcrumbs: "PostMessage API / Actions / WOPI host to editor"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Action_Save | DontTerminateEdit: <boolean> DontSaveIfUnmodified: <boolean> Notify: <boolean> ExtendedData: <String> | Saves the document. DontTerminateEdit is relevant for spreadsheets where saving a document can terminate the edit mode (text cursor disappearing). Setting this to true won’t terminate the edit mode and can be used to save document without disrupting user’s editing session in spreadsheets. DontSaveIfUnmodified prevents coolwsd to save the file back to storage if document is unmodified (only cursor position changed etc.) but still saved. This can be helpful to prevent creating unnecessary file revisions. Notify when present and set to true notifies the host when document is saved. See Action_Save_Resp for details. ExtendedData optional data carried over to the WOPI host if provided in the X-COOL-WOPI-ExtendedData header. The contents are preserved as-is, however, care must be taken to avoid using anything that HTTP headers do not allow, also, special values such as new-line, null character, non-printable characters, etc. are not allowed. The client can use this to pass multiple values to the WOPI host which can then act on them. |
| Action_SaveAs | Filename: <String> Notify: <boolean> | Creates copy of the document with given Filename. Filename is the requested filename for the new file. Notify when present and set to true notifies the host when document is saved. See Action_Save_Resp for details. |
| Action_FollowUser | Follow: <Boolean> ViewId: <Number> | Turn on or off the follow user feature. When Follow is set to true or is not define set to true or is not enables following the editor, disables following when set to false When Follow is set to true or is not defined ViewId parameter specifies user to follow. When ViewId is not defined, the current editor is followed. |
| Action_Close |  | Closes the document. |
| Close_Session |  | Allows closing documents before they are completely loaded. |
| Action_Fullscreen |  | Switch to fullscreen mode. |
| Action_FullscreenPresentation | StartSlideNumber: <Number> CurrentSlide: <Boolean> | Start the presentation in Impress. StartSlideNumber optionally specify the starting slide (from 0) If CurrentSlide is true, then the presentation starts from the current slide. |
| Action_Print |  | Prints the document. |
| Action_Export | Format: <String> Notify: <boolean> | Downloads the document in format specified by Format. Format must be from the list returned in Get_Export_Formats. Notify when present and set to true notifies the host when document is saved. See Action_Save_Resp for details. |
| Action_InsertGraphic | url: <String> | Downloads image from the url and inserts it to the document. This is usually the response to a successful UI_InsertGraphic |
| Action_InsertLink | url: <String> | Insert a link into the document. This is usually the response to a successful UI_PickLink |
| Action_InsertMultimedia | url: <String> | New in version 24.04.10. Downloads multimedia from the url and inserts it to the document. This may be the response to a successful UI_InsertFile. |
| Action_CompareDocuments | url: <String> | New in version 25.04.9.1. Downloads an old document from the url and compares it with the current new document. This may be the response to a successful UI_InsertFile. |
| Action_ShowBusy | Label: <String> | Shows an in-progress overlay, just like what appears when saving the document, with the given Label. |
| Action_HideBusy |  | Hides any in-progress overlay, if present. |
| Action_ChangeUIMode | Mode: 'classic' \| 'notebookbar' | Changes the user interface: Classic Toolbar or Notebookbar. |
| Action_Paste | Mimetype: <string> Data: <string> | Pastes the data directly to the document bypassing the internal paste mechanism. Example: Values: {Mimetype: "text/plain;charset=utf-8", Data: "foo"}}; Valid MIME types include text/plain, text/markdown and text/html. |
| Action_Copy | Mimetype: <string> | New in version 25.04.8.1. Copies the text content from the document. Example: Values: {Mimetype: "text/markdown;charset=utf-8"}}; Response is returned in form of Action_Copy_Resp. Valid MIME types include text/plain, text/markdown and text/html. |

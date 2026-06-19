---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id6"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id6"
title: "Editor to WOPI host"
canonical_title: "PostMessage API / Miscellaneous / Editor to WOPI host"
toc_level: "2"
breadcrumbs: "PostMessage API / Miscellaneous / Editor to WOPI host"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Clicked_Button | id: <string> | This event is emitted when the custom button added via Insert_Button is clicked. |
| Clicked_ContextualButton | id: <string> | This event is emitted when the custom button added via Insert_ContextualButton is clicked. |
| Download_As | Type: 'print'\|'slideshow'\|'export' URL: <string> | This event is emitted when the user chooses ‘Print’ or ‘Show slideshow’ or ‘Download As [some type'] and the integration indicates via DownloadAsPostMessage in the CheckFileInfo that it wants to handle the downloading of pdf for printing or svg for slideshows or exported document. This is in situations when the integration cannot rely on browser’s support for downloading like in mobile apps that use the Online in a Web View. |
| UI_OpenDocument |  | Requests WOPI host to open a popup window where user can pick another document to view & edit. |
| UI_CreateFile |  | Requests WOPI host to open a new browser tab and create a new document. The document type is passed as DocumentType argument, and can be ‘text’,’spreadsheet’,’presentation’ or ‘drawing’. |
| UI_SaveAs | Args: {format: '<extension>' } | Requests WOPI host to create appropriate UI, so that the user can choose path and File name for creating a copy of the current file. Response to this query is sent via Action_SaveAs message. Optional arguments: file extension. When this parameter is passed a dropdown appears and the newly saved file is loaded in the integration instead of downloaded. |
| UI_InsertGraphic |  | Requests WOPI host to open a popup window where user can pick an image to insert. A successful pick would lead to the WOPI host sending a Action_InsertGraphic postMessage back. Require the WOPI property EnableInsertRemoteImage to be set to enable the button. |
| UI_PickLink |  | Requests WOPI host to open a popup windo where users can pick a link to insert. A successful pick would lead to the WOPI host sending a Action_InsertLink postMessage back. |
| UI_InsertFile | callback: <string> mimeTypeFilter: <array_of_strings> | New in version 24.04.10. Requests WOPI host to open a popup window where user can pick a file to insert. A successful pick would lead to the WOPI host sending a postMessage defined in ‘callback’ argument back. Required arguments: callback: the name of the postMessage to send back on success. It must take a single ‘url’ argument. mimeTypeFilter: an array of MIME types that the host uses to filter the assets suggested to the user in the window. |
| UI_InsertAIContent |  | New in version 24.04.12. Request WOPI host to open a popup window where the user can select to insert AI generated content. A successful selection would lead the WOPI host sending some content like a Action_Paste or Action_InsertGraphic postMessage. |
| UI_Cancel_Password |  | Notifies WOPI host that the user clicked on the ‘cancel’ option when opening a password protected file, instead of providing the password to decrypt it. |
| UI_Hyperlink |  | Notifies WOPI host that the user clicked a hyperlink and confirmed they really want to leave the document to follow the hyperlink. This is especially useful for integrations that embed Collabora Online into an iframe in a mobile app, where actually trying to open a new window should trigger starting a new Activity on Android (or something similar on iOS). The integration using this most probably also wants to trigger the Disable_Default_UIAction for UI_Hyperlink. |
| UI_Paste |  | Sent on mobile when pasting is requested. This allow the embedding mobile application to take action with the clipboard content. This is to work around limitations imposed by the mobile platform. |
| Doc_ModifiedStatus |  | Notification to update the modified status of the document. Values.Modified will be true, if the document has been modified since the last save, otherwise, it will be false if the document has been saved. Note that this notification may be published without a change from the prior value, so care must be taken to check the Values.Modified value and not assume the notification itself implies the modified state of the document on its own. |

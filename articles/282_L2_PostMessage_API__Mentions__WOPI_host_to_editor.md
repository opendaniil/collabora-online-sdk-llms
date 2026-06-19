---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id12"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id12"
title: "WOPI host to editor"
canonical_title: "PostMessage API / Mentions / WOPI host to editor"
toc_level: "2"
breadcrumbs: "PostMessage API / Mentions / WOPI host to editor"
---
| MessageId | Values | Description |
| --- | --- | --- |
| Action_Mention | list: [{ username: "example-username1/example-uid1", profile: "link-to-the-profile", label: "Example Displayname1" }, { username: "example-username2/example-uid2", profile: "link-to-the-profile", label: "Example Displayname2" }.....] | The integrator should send this message in response to the UI_Mention message of type autocomplete. The message must include a list of user objects, where each object contains the following fields: username: A unique identifier for the user, such as a username or user ID. profile: A link to the user’s profile. label: (Optional) A display name for the user. This field is useful when the username represents a user ID or another non-descriptive identifier. It allows the integrator to provide a more user-friendly display name while still using the unique username for identification in subsequent messages, such as the selected message sent from the editor to the host. Since 24.04.10.2. |

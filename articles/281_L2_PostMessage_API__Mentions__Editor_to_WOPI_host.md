---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#id11"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "id11"
title: "Editor to WOPI host"
canonical_title: "PostMessage API / Mentions / Editor to WOPI host"
toc_level: "2"
breadcrumbs: "PostMessage API / Mentions / Editor to WOPI host"
---
| MessageId | Values | Description |
| --- | --- | --- |
| UI_Mention | type: autocomplete text: <string> | When the user starts typing with “@”, Collabora Online will send this postMessage with partial text followed by “@” to get the list of usernames from the integrator. |
| UI_Mention | type: selected username: <string> | When the user selects a username from the list given by the integrator, this message gets fired. |

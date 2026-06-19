---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/cookies_and_local_storage.xhtml"
source_file: "docs/cookies_and_local_storage.xhtml"
source_anchor: ""
title: "Cookies and local storage"
canonical_title: "Cookies and local storage"
toc_level: "0"
breadcrumbs: "Cookies and local storage"
---
Collabora Online (the online office suite) does not use cookies. However the [admin console](045_L2_Installation_guide__Configuration__Admin_Console.md) of Collabora Online uses a session cookie to store a JSON Web Token (JWT) for authentication.

User preferences are stored in browser’s local storage. For example:

- dark mode or light mode
- compact view (classic menu + toolbar) or tabbed view (notebookbar)
- whether to show sidebar
- whether to show document navigator
- whether to show status bar
- automatic spell checking on or off
- last used colors in color palettes
- accessibility support on or off (when it’s enabled on server’s side)
- last used citation style (when Zotero integration is present)

The local storage is also used to store data to control the display of Welcome and User Feedback dialogs in CODE.

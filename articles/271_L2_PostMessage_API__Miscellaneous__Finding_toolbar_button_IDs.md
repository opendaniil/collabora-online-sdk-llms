---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#finding-toolbar-button-ids"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "finding-toolbar-button-ids"
title: "Finding toolbar button IDs"
canonical_title: "PostMessage API / Miscellaneous / Finding toolbar button IDs"
toc_level: "2"
breadcrumbs: "PostMessage API / Miscellaneous / Finding toolbar button IDs"
---
Toolbar button IDs are defined in `getToolItems/create` functions in:

- [Control.TopToolbar.js](https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.TopToolbar.js) [https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.TopToolbar.js] for the top toolbar on desktop or tablet.
- [Control.MobileTopBar.ts](https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.MobileTopBar.ts) [https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.MobileTopBar.ts] for the top toolbar on smartphone.
- [Control.MobileBottomBar.js](https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.MobileBottomBar.js) [https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.MobileBottomBar.js] for the bottom toolbar on smartphone.
- [Control.StatusBar.js](https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.StatusBar.js) [https://github.com/CollaboraOnline/online/blob/main/browser/src/control/Control.StatusBar.js] for the statusbar on desktop.

Note that they usually don’t change but there is no guarantee that they are stable.

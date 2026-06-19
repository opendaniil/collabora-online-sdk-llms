---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#userfriendlyname"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "userfriendlyname"
title: "UserFriendlyName"
canonical_title: "Advanced integration / CheckFileInfo response properties / UserFriendlyName"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo response properties / UserFriendlyName"
---
A string representing the name of the user for display in the UI.

While nominally an optional field, it is used to identify the author of changes in documents. When missing, `UnknownUser` will be used instead, with a possible suffix with the `UserId`.

Strongly recommended to set it to a valid value.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#feature-restriction"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "feature-restriction"
title: "Feature Restriction"
canonical_title: "Installation guide / Configuration / Feature Restriction"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Feature Restriction"
---
Collabora provides a way to completely disable/hide certain features from the user. You can specify the feature’s UNO command to disable it in `restricted_commands`. To mark a user restricted, the WOPI client should return `CheckFileInfo` containing a field `IsUserRestricted` with a boolean value.

Note

This is not available in CODE.

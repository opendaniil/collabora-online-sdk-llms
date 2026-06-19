---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#putfile-headers"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "putfile-headers"
title: "PutFile headers"
canonical_title: "Advanced integration / PutFile headers"
toc_level: "1"
breadcrumbs: "Advanced integration / PutFile headers"
---
PutFile additionally indicates whether the user has modified the document before the save, or if they just pressed the Save button without any modification. The following header:

```
X-COOL-WOPI-IsModifiedByUser
```

will have the value `true` or `false` accordingly.

To distinguish auto-save vs. explicit user requests to save, the following header:

```
X-COOL-WOPI-IsAutosave
```

will have the value `true` when the PutFile is triggered by auto-save, and `false` when triggered by explicit user operation (Save button or menu entry).

When the document gets cleaned up from memory (e.g. when all users disconnect), an automatic save will be triggered. In this case the following header will be set to `true`:

```
X-COOL-WOPI-IsExitSave
```

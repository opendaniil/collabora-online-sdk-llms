---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#modifying-discovery-xml"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "modifying-discovery-xml"
title: "Modifying discovery.xml"
canonical_title: "Advanced integration / Modifying discovery.xml"
toc_level: "1"
breadcrumbs: "Advanced integration / Modifying discovery.xml"
---
The discovery.xml defines which part of Collabora Online can be used for a certain file type and what action should be used.

The following is a snippet from discovery.xml:

```
...
<app name="writer" favIconUrl="images/x-office-document.svg">
   <action name="view" default="true" ext="sxw"/>
   <action name="edit" default="true" ext="odt"/>
   ...
</app>
...
<app name="draw">
   ...
   <action name="view_comment" ext="pdf"/>
</app>
```

The supported actions are “edit”, “view” and a special “view_comment”. When the action is “edit”, the document will open for editing. When the action is “view”, the document will open in read-only mode for viewing. When the action is set to “view_comment”, the document will open read-only, but adding or editing comments will still be possible.

The “view_comment” mode is useful for PDF documents, where adding and editing comments is allowed, but otherwise no other editing should be allowed to be performed.

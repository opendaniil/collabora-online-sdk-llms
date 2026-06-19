---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#templatesource"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "templatesource"
title: "TemplateSource"
canonical_title: "Advanced integration / CheckFileInfo response properties / TemplateSource"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo response properties / TemplateSource"
---
The ID of file (like the wopi/files/ID) can be a non-existing file. In that case, the file will be created from a template when the template (eg. an OTT file) is specified as `TemplateSource` in the CheckFileInfo response.

The TemplateSource is supposed to be an URL like `https://somewhere/accessible/file.ott` that is accessible by the Collabora Online server.

For the actual saving of the content, normal [PutFile](146_L0_How_to_integrate.md) mechanism will be used.

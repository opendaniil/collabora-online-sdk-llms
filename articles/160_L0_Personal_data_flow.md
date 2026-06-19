---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/personal_data_flow.xhtml"
source_file: "docs/personal_data_flow.xhtml"
source_anchor: ""
title: "Personal data flow"
canonical_title: "Personal data flow"
toc_level: "0"
breadcrumbs: "Personal data flow"
---
The only place where Collabora Online interacts with user data is what it gets from CheckFileInfo (including the document name). That goes to two places: logs and user interface. The logs can be disabled via the anonymize feature, and the user interface is transient (no storage).

![Collabora Online Personal Data Flow](assets/_images/data-flow-diagram.png)

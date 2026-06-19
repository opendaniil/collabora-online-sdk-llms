---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#server-audit"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "server-audit"
title: "Server Audit"
canonical_title: "Installation guide / Configuration / Server Audit"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Server Audit"
---
The server audit might display some unwanted information. You can disable the functionality with the following option:

in logging block of coolwsd.xml

```
 <disable_server_audit type="bool">true</disable_server_audit>
```

or

in command line

```
 --o:logging.disable_server_audit=true
```

Ideally the integration would ensure that [IsAdminUser](177_L2_Advanced_integration__CheckFileInfo_extended_response_properties__IsAdminUser.md) is set properly in the `CheckFileInfo` WOPI call as this ensure the server audit is only show to administrators.

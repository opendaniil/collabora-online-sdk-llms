---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/How_to_integrate.xhtml#re-using-our-development-demo-servers"
source_file: "docs/How_to_integrate.xhtml"
source_anchor: "re-using-our-development-demo-servers"
title: "Re-using our development / demo-servers"
canonical_title: "How to integrate / Re-using our development / demo-servers"
toc_level: "1"
breadcrumbs: "How to integrate / Re-using our development / demo-servers"
---
One easy way to test your WOPI integration without even needing to setup Collabora Online for both development, and your users is to target one of our demo servers [read how to do that properly](https://www.collaboraonline.com/blog/collabora-online-demo-servers-provide-fast-and-easy-user-access/) [https://www.collaboraonline.com/blog/collabora-online-demo-servers-provide-fast-and-easy-user-access/] you can provide users’ a list of servers [from this end-point](https://www.collaboraoffice.com/demo-servers.json) [https://www.collaboraoffice.com/demo-servers.json] however please bear in mind these factors:

> - you must have a publicly routable and resolvable WOPI server. If you pass our demo servers a WOPI URL to 192.168.1.5 we will not be able to get to the document data (obviously) to load, save and render it. Of course, it can be rather easier to trace protocol problems in the logs of your own server too.
> - it is vitally important to let the user know that their data will be shared with others and that they should not include personally identifying information into their test documents.
> - it is worth reminding users that the performance of such a shared test server can be extremely variable and is not representative of a properly setup on-premise installation.

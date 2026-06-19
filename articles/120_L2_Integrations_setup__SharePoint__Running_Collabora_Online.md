---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/integrations/sharepoint.xhtml#running-collabora-online"
source_file: "docs/integrations/sharepoint.xhtml"
source_anchor: "running-collabora-online"
title: "Running Collabora Online"
canonical_title: "Integrations setup / SharePoint / Running Collabora Online"
toc_level: "2"
breadcrumbs: "Integrations setup / SharePoint / Running Collabora Online"
---
Collabora Online runs on Linux servers. In a Microsoft environment it can be difficult. If you can’t install a Linux server (even virtualised) you can use Docker for Windows. It is recommended that this be a different server than SharePoint in any case.

You can run Collabora Online on Azure with a Linux server.

SharePoint doesn’t seem to work with self-signed certificates, and we don’t recommend using it HTTP only. Using Collabora Online with a Let’s Encrypt provided certificate worked.

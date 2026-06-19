---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#webserver-restart"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "webserver-restart"
title: "Webserver restart"
canonical_title: "Troubleshooting / Package upgrade issues / Webserver restart"
toc_level: "2"
breadcrumbs: "Troubleshooting / Package upgrade issues / Webserver restart"
---
The WOPI discovery.xml file may be cached at WOPI host. It contains versioned URLs that will point to a non-existing location after coolwsd upgrade. The symptom is that the content is not loaded into the iframe, and there are error message in the coolwsd log file, related to missing files. In this case restart the web server.

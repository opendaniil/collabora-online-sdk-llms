---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#unauthorized-wopi-host-error-when-opening-a-file"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "unauthorized-wopi-host-error-when-opening-a-file"
title: "‘Unauthorized WOPI host error’ when opening a file."
canonical_title: "Troubleshooting / Symptom-based Troubleshooting / ‘Unauthorized WOPI host error’ when opening a file."
toc_level: "2"
breadcrumbs: "Troubleshooting / Symptom-based Troubleshooting / ‘Unauthorized WOPI host error’ when opening a file."
---
The document storage host is not among the allowed WOPI hosts in /etc/coolwsd/coolwsd.xml configuration file (under element wopi). Add the domain name or the IP address, and restart coolwsd.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#case-study-no-2"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "case-study-no-2"
title: "Case study No. 2"
canonical_title: "Troubleshooting / Case studies / Case study No. 2"
toc_level: "2"
breadcrumbs: "Troubleshooting / Case studies / Case study No. 2"
---
A partner installed Collabora Online from the provided packages, and set up the configuration to access files locally (enabled setting storage / filesystem), but was not able to access files. In a different, container-based setup, accessing local files worked.

Browser console logs showed that the server was accessed without the required port, and the requested file was not found. At first the reverse proxy seemed to be the culprit, but the issue persisted without proxy as well.

The /hosting/discovery file already listed the target host and path without the port. This pointed to the ‘server_name’ setting in /etc/coolwsd/coolwsd.xml, which was set, but without the necessary port. However in this case the setting was not necessary at all, and clearing it fixed the issue.

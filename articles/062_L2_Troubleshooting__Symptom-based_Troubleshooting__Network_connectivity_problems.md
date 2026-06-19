---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#network-connectivity-problems"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "network-connectivity-problems"
title: "Network connectivity problems"
canonical_title: "Troubleshooting / Symptom-based Troubleshooting / Network connectivity problems"
toc_level: "2"
breadcrumbs: "Troubleshooting / Symptom-based Troubleshooting / Network connectivity problems"
---
Collabora Online host, document storage host and user‘s browser have to see each other all times. To this end, it is always recommended to set up a **reverse proxy** on Collabora Online host, because the default port of Collabora Online, port 9980 is sometimes blocked by users‘ corporate firewall, only standard https port 443 is allowed.

If the reverse proxy is not preserving the Collabora Online host name, it has to be set in server_name setting.

Preferably do not use non-routable internal IP addresses or domain names that DNS cannot resolve on all hosts (otherwise they have to be present in the /etc/hosts file).

A command line example: `coolconfig set server_name office.example.com`.

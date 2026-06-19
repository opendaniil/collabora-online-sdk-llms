---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#load-balancing-problems"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "load-balancing-problems"
title: "Load balancing problems"
canonical_title: "Troubleshooting / Symptom-based Troubleshooting / Load balancing problems"
toc_level: "2"
breadcrumbs: "Troubleshooting / Symptom-based Troubleshooting / Load balancing problems"
---
In incorrectly configured load balanced multi-node Collabora Online cluster you can experience different characteristic symptoms:

Pasting into document doesn’t work. The browser’s request gets response 400 Bad Request and in the server logs you can find: `ERR Cluster configuration error: mis-matching serverid AAAAAAA vs. BBBBBBB`

When two users join to the same document but doesn’t see each other edits or saved content is lost or overwritten by other users working on the same file.

That means the HTTP requests related to the same file are not directed to the same Collabora Online node.

Read more at [Load balancing](056_L2_Installation_guide__Proxy_settings__Load_balancing.md).

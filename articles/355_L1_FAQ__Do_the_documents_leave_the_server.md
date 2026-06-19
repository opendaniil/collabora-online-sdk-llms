---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/faq.xhtml#do-the-documents-leave-the-server"
source_file: "docs/faq.xhtml"
source_anchor: "do-the-documents-leave-the-server"
title: "Do the documents leave the server?"
canonical_title: "FAQ / Do the documents leave the server?"
toc_level: "1"
breadcrumbs: "FAQ / Do the documents leave the server?"
---
Collabora Online uses an adapted versions of the WOPI standard protocol, and we can use data stores which can provide their own policies. When your document data comes down into Collabora Online we isolate and protect your document in your on-premise server inside a series of concentric security onion shells:

![../_images/security-onion.png](assets/_images/security-onion.png)

Collabora keeps your document data on the server, and can send only tiled images to the client. These can also be watermarked with the viewer’s name. With granular permissions to restrict copy & paste, download, print and so on – Collabora protects your documents like no other.

![../_images/security-onion-connections.png](assets/_images/security-onion-connections.png)

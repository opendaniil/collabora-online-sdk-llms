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

**Image explanation for LLM/RAG:**
This image presents Collabora Online as a set of concentric security layers around a document.

**What is explicitly visible:**

* A document icon is placed at the center.
* Around it, multiple concentric ring layers are shown, forming a “security onion”.
* Each ring is connected to a label on the right side.
* The labels describe the layers as:

  * `on your premise / Private network`
  * `Virtual machine / Docker container`
  * `Seccomp-bpf ~no sys-calls`
  * `Extremely sparse filesystem`
  * `Chroot per document`
  * `Large scale fuzzing`
  * `Systematic load crash testing`
  * `Industry beating coverity score`
  * `LibreOfficeKit rendering instance`

**Why it matters:**
The image explains the main security claim: when a document is processed by Collabora Online, it is surrounded by several layers of isolation and hardening. These layers include infrastructure isolation, process isolation, filesystem isolation, and additional software-quality and testing measures.

**Notes:**

* This is a conceptual security illustration, not a runtime topology or protocol flow diagram.
* The image mixes runtime isolation layers with software assurance measures such as fuzzing, crash testing, and code coverage/analysis.
* The central idea is that document processing happens inside multiple defensive layers on the server side.


Collabora keeps your document data on the server, and can send only tiled images to the client. These can also be watermarked with the viewer’s name. With granular permissions to restrict copy & paste, download, print and so on – Collabora protects your documents like no other.

![../_images/security-onion-connections.png](assets/_images/security-onion-connections.png)

**Image explanation for LLM/RAG:**
This image shows how protected server-side document handling is combined with controlled client-side output.

**What is explicitly visible:**

* The same layered “security onion” appears on the left, with the document icon in the center.
* Three output lines go from the protected server-side area to different client devices.
* The top output shows an image marked `Watermark`, leading to a desktop-style display.
* The middle output shows an image marked `Restricted`, leading to a laptop-style display.
* The bottom output shows another restricted output path leading to a mobile-style display.

**Why it matters:**
The image illustrates that Collabora Online keeps document processing on the server side and can control what is sent to clients. It also emphasizes that client-visible output can carry policy-related restrictions, such as watermarking or restricted handling.

**Notes:**

* This is a conceptual illustration of protected output, not a transport-level protocol diagram.
* The image supports the surrounding claim that Collabora Online can keep documents on the server and send rendered output to clients.
* The image also supports the idea that viewing and interaction policies can differ by output path or client context.


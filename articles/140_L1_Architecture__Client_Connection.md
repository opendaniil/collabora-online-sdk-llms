---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#client-connection"
source_file: "docs/architecture.xhtml"
source_anchor: "client-connection"
title: "Client Connection"
canonical_title: "Architecture / Client Connection"
toc_level: "1"
breadcrumbs: "Architecture / Client Connection"
---
A request from a client to load a document will trigger the following chain of events.

- WSD public socket will receive the connection request followed by a “load” command. The connection includes the `wopiSrc` unique URL, which includes the user’s token.
- An instance of DocumentBroker with the given `wopiSrc` (without the user token) is searched for, if one exists, the document was loaded and this is a new view to the existing document. Otherwise, a new DocumentBroker instance is created and registered internally.
- WSD finds an available Kit process. If none is available, a request is made to ForKit to spawn more.
- A ClientSession (ToClient) is created and takes ownership of the incoming socket to handle the client traffic.
- ForKit sends Kit request to host URI via internal Unix-Socket.
- Kit connects to WSD on an internal port.
- The Kit internally creates Document and ChildSession instances to abstract the document and views on it, respectively.
- WSD creates another ClientSession (ToPrisoner) to service Kit.
- ClientSession (ToClient) is linked to the ToPrisoner instance, copies the document into jail (first load only) and sends (via ToPrisoner) the load request to Kit.
- Kit loads the document and sets up callbacks with LOKit.
- ClientSession (ToClient) and ClientSession (ToPrisoner) tunnel the traffic between clients and the Kit both ways.

![../_images/client-connection.png](assets/_images/client-connection.png)

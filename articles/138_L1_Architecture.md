---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#id1"
source_file: "docs/architecture.xhtml"
source_anchor: "id1"
title: "Architecture"
canonical_title: "Architecture / Architecture"
toc_level: "1"
breadcrumbs: "Architecture / Architecture"
---
There are three processes: CoolWSD, CoolForKit, and CoolKit.

WSD is the top-level server and is intended to run as a service. It is responsible for spawning ForKit and listening on public port for client connections.

The ForKit is only responsible for forking Kit instances. There is only one ForKit per WSD instance and there is one Kit instance per document.

WSD listens on a public port and using internal pipes requests the ForKit to fire a child (Kit) instance to host documents. The ForKit then has to find an existing Kit that hosts that document, based on the public URI as unique key, and forward the request to this existing Kit, which then loads a new view to the document.

There is a singleton Admin class that gets notified of all the important changes and update the AdminModel object accordingly. AdminModel object has subscribers which corresponds to admin panel sessions. Subscriber can subscribe to specific commands to get live notifications about, and to update the UI accordingly.

Whether a document is loaded for the first time, or this is a new view on an existing one, the Kit connects via a socket to WSD on an internal port. WSD acts as a bridge between the client and Kit by tunnelling the traffic between the two sockets (that which is between the client and WSD and the one between WSD and Kit).

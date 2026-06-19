---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#threading"
source_file: "docs/architecture.xhtml"
source_anchor: "threading"
title: "Threading"
canonical_title: "Architecture / Threading"
toc_level: "1"
breadcrumbs: "Architecture / Threading"
---
The threading model is as simple as possible. Specifically, each document is handled on the WSD side with a single thread. Similarly, in the Kit, each document has a primary single thread. In both of these cases, this primary thread is responsible for the socket communication as well as the handling of commands/events.

On the WSD side, the DocumentBroker is the owner of this thread. It is regulated through the poll system call, which, when there is no new data in the sockets to read, and no data to write, puts the thread into efficient wait state for new input from any of the sockets (belonging to that particular document), or a timeout. This approach is both simple (minimal thread synchronization concerns) and efficient.

Similarly, in the Kit, the same thread that handles document input, commands, and events, is the same thread that handles the socket logic. The way this is done is through the `runLoop()` Kit API that registers callbacks that the document’s main thread calls in its main loop.

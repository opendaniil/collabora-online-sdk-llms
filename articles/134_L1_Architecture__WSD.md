---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#wsd"
source_file: "docs/architecture.xhtml"
source_anchor: "wsd"
title: "WSD"
canonical_title: "Architecture / WSD"
toc_level: "1"
breadcrumbs: "Architecture / WSD"
---
The main process, WSD (Web Service Daemon), is responsible for spawning ForKit, setting up the childroot directory, and listening for incoming client connections. WSD is the top-level server and is intended to run as a service.

Once ready, the WSD process accepts incoming connections on the incoming port (9980 by default). This is the primary server connection which accepts client connection.

Typically, WSD runs behind a reverse proxy. Although it is fully capable of communicating directly with clients over SSL encrypted web-sockets, it is often more practical to run it without SSL, but behind a reverse proxy that terminates external SSL connections. That is, externally, connections are encrypted, but internally (between the reverse proxy and WSD) the data is unencrypted. This simplifies the topology as it’s easier now to move and scale WSD instances without impacting the client-visible end-point. And since all external connections must be encrypted, the reverse proxy must have SSL enabled for incoming connections, but there is rarely a need to encrypt internal connections between the reverse proxy and WSD. Although that is, of course, possible and supported.

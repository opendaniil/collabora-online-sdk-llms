---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#protocol"
source_file: "docs/architecture.xhtml"
source_anchor: "protocol"
title: "Protocol"
canonical_title: "Architecture / Protocol"
toc_level: "1"
breadcrumbs: "Architecture / Protocol"
---
The protocol between the client and server uses plain-text with the occasional JSON, if structured data is needed. It is documented [separately](https://github.com/CollaboraOnline/online/blob/main/wsd/protocol.txt/) [https://github.com/CollaboraOnline/online/blob/main/wsd/protocol.txt/].

Payloads, in some cases, need to be in binary. This is the case, for example, for rendered tiles. These tile responses must contain the binary data of the tiles they contain.

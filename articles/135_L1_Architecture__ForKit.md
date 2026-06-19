---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#forkit"
source_file: "docs/architecture.xhtml"
source_anchor: "forkit"
title: "ForKit"
canonical_title: "Architecture / ForKit"
toc_level: "1"
breadcrumbs: "Architecture / ForKit"
---
The ForKit process is responsible for loading the Collabora Office dynamic shared object libraries (DSO, for short) to its memory and, subsequently, for forking Kit instances on demand.

These DSO’s implement the core logic of viewing and editing the document. This is referred to as the Core.

In addition to the core logic, these libraries also implement the API to communicate with WSD and therefore implement the interface with the Collabora Online. This layer is called the Kit.

There is only one ForKit per WSD instance and there is one Kit process instance per document.

Once the Kit and Core libraries are loaded into the Forkit process, it (Forkit) is ready to fork additional processes that can load documents. The ForKit process never loads documents, however. It is only responsible for forking additional processes to load documents, per WSD’s demands. It forks Kit instances ahead of time, to make loading documents faster. The number of ahead-of-time instances is controlled through the num_prespawn_children config setting.

The name ‘ForKit’ is a play on both ‘fork it’ and ‘fork Kit’ by contracting the latter into a single word.

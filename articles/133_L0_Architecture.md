---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml"
source_file: "docs/architecture.xhtml"
source_anchor: ""
title: "Architecture"
canonical_title: "Architecture"
toc_level: "0"
breadcrumbs: "Architecture"
---
Collabora Online is designed to be self-contained and secure out of the box. It has its own built-in web-server, which is often ran behind a reverse proxy for flexibility and added security, as well as isolated per-document processes.

Internally, each document is loaded in a separate process, which is isolated on multiple levels.

Conceptually, there are three (3) groups of processes: WSD, ForKit, and Kit.

A high-level sketch looks as follows:

![Architecture Sketch](assets/_images/architecture-sketch.svg)

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#tile-rendering"
source_file: "docs/architecture.xhtml"
source_anchor: "tile-rendering"
title: "Tile Rendering"
canonical_title: "Architecture / Tile Rendering"
toc_level: "1"
breadcrumbs: "Architecture / Tile Rendering"
---
The document is rendered into raster images on the server (the Kit) and sent to the client in pre-defined dimensions called tiles. The tiles are tracked on the client and displayed.

When there is a modification (by any other user, or the current one) the Kit will send invalidation notifications to all (active) clients. Each client in its turn will send requests to render the tiles that are out of date.

The server tracks the requests from all clients and renders each unique tile request only once. A tile is not unique only by its coordinates and size, but also by the zoom factor. This makes sure that no tile is rendered more than once. The tiles are cached, so subsequent requests to the same unique tile is served from cache.

Rendering is expensive, and it pays to be minimize them where possible.

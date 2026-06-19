---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#url-query-parameters"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "url-query-parameters"
title: "URL query parameters"
canonical_title: "Advanced integration / URL query parameters"
toc_level: "1"
breadcrumbs: "Advanced integration / URL query parameters"
---
Some additional options can be passed using URL query parameters.

Those suported are:

- `closebutton`: allows to display a close button, that will emit the `UI_Close` message on the postMessage API, with the parameter `EverModified`, telling if the file had any modification. Example: `&closebutton=true`
- `revisionhistory`: allows to display the See history option in the File tab or File menu. This button, when clicked, emits the `UI_FileVersions` message on the postMessage API. Example: `&revisionhistory=true`
- `target`: allows to focus a section in the document opened upon loading. Example: `&target=image6.png|graphic`
- `timestamp`: allows to pass in the modification time of the document as a Unix timestamp that will be passed to the server.

New in version 24.04.

- `startPresentation`: in Impress, allows to start in presentation mode. Due to browser restriction, this can only render in the current tab rather than in fullscreen. Example: `&startPresentation=true`. ppsx or pps files load by default with this mode, this can be disabled with `&startPresentation=false`.

And some debug and testing utilities:

- `lang`: allows to manually overwrite the language. Example `&lang=ar` or `&lang=fr`
- `permission`: allows to load a document in readonly mode. Example: `&permission=readonly`
- `debug`: enables debug mode, displaying controls useful to debug Collabora Online. Example: `&debug=true`, there is a shortcut Ctrl+Shift+Alt+D.
- `randomUser`: enables debug mode and loads a random language. Example: `&randomUser=true`

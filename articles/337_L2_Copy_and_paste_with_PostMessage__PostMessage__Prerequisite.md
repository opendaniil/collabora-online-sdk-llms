---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml#prerequisite"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: "prerequisite"
title: "Prerequisite"
canonical_title: "Copy and paste with PostMessage / PostMessage / Prerequisite"
toc_level: "2"
breadcrumbs: "Copy and paste with PostMessage / PostMessage / Prerequisite"
---
For the sample code below to work, you need the following function. This is just an example and you should adapt it to your needs.

```
function post(msg) {
    // This assumes the Collabora Online iframe has the id `collabora-online`
    document.querySelector('#collabora-online').postMessage(JSON.stringify(msg), '*');
}
```

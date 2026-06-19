---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#full-screen"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "full-screen"
title: "Full Screen"
canonical_title: "Advanced integration / Full Screen"
toc_level: "1"
breadcrumbs: "Advanced integration / Full Screen"
---
The Impress slideshow allow playing a presentation in full screen mode. However to allow full screen presentation, an explicit permission must be granted. This is done by setting the allow value on the `<iframe>` element to contain `fullscreen` like this:

```
<iframe allow="fullscreen"/>
```

Note

This is the exact same place where you grant permissions for the clipboard handling. See the MDN documentation for [HTMLIframeElement.allow](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/allow) [https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement/allow] to know the syntax on how to combine these permissions.

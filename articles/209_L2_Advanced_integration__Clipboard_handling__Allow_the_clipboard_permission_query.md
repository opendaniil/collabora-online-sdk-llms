---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#allow-the-clipboard-permission-query"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "allow-the-clipboard-permission-query"
title: "Allow the clipboard permission query"
canonical_title: "Advanced integration / Clipboard handling / Allow the clipboard permission query"
toc_level: "2"
breadcrumbs: "Advanced integration / Clipboard handling / Allow the clipboard permission query"
---
Chrome implements a JavaScript API to paste from the clipboard without using the keyboard. This relies on cross-origin iframes, which is disabled by default. To enable it in your integration, use a new attribute in the iframe element of your integration:

```
<iframe allow="clipboard-read *; clipboard-write *"/>
```

Once this is in place, the user will see a popup to allow access to the clipboard on first use.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml#html"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: "html"
title: "HTML"
canonical_title: "Copy and paste with PostMessage / Paste / HTML"
toc_level: "2"
breadcrumbs: "Copy and paste with PostMessage / Paste / HTML"
---
If you need some formatting you can also paste HTML using the following snippet. The MIME type to use is `text/html`.

```
post({
    'MessageId': 'Action_Paste',
    'Values': {
        'Mimetype': 'text/html;charset=utf-8',
        'Data': '<h1>heading</h1><ul><li>List 1</li><li>List 2</li></ul>',
    }
});
```

This will create a heading and insert a list, as the following HTML.

```
<h1>heading</h1>
<ul>
<li>List 1</li>
<li>List 2</li>
</ul>
```

The text will follow the semantics of the HTML markup and the formatting will use the stylesheets from the document.

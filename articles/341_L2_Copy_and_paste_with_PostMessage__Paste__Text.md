---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml#text"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: "text"
title: "Text"
canonical_title: "Copy and paste with PostMessage / Paste / Text"
toc_level: "2"
breadcrumbs: "Copy and paste with PostMessage / Paste / Text"
---
```
post({
    'MessageId': 'Action_Paste',
    'Values': {
        'Mimetype': 'text/plain;charset=utf-8',
        'Data': 'Some inserted text.',
    }
});
```

This will paste `Some inserted text.` at the current insertion point or overriding the selection using the current formatting at that location.

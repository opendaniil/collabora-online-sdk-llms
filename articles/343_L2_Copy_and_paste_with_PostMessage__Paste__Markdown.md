---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml#markdown"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: "markdown"
title: "Markdown"
canonical_title: "Copy and paste with PostMessage / Paste / Markdown"
toc_level: "2"
breadcrumbs: "Copy and paste with PostMessage / Paste / Markdown"
---
New in version 25.04.8.1.

Markdown support was recently added. You can paste markdown text using the following snippet. The MIMI type to use is `text/markdown`.

```
post({
    'MessageId': 'Action_Paste',
    'Values': {
        'Mimetype': 'text/markdown;charset=utf-8',
        'Data': `# heading
- List 1
- List 2`,
    }
});
```

This will insert the following markdown snippet:

```
# heading
- List 1
- List 2
```

The text will follow the semantics of the markdown and the formatting will use the stylesheets from the document. Note the use of JavaScript template string the code to ensure the proper formatting as markdown heavily depends on whitespace.

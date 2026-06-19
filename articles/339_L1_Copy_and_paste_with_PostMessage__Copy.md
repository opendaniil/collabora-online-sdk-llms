---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml#copy"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: "copy"
title: "Copy"
canonical_title: "Copy and paste with PostMessage / Copy"
toc_level: "1"
breadcrumbs: "Copy and paste with PostMessage / Copy"
---
New in version 25.04.8.1.

Copy works by sending the `Action_Copy` PostMessage. This will take the content of the selection, just like if the user pressed Ctrl-C, but instead will send the content back that through an `Action_Copy_Resp` PostMessage sent back. The following snippet show a standalone solution.

```
let pasteBoard;
window.addEventListener('message', receiveMessage, false);

function receiveMessage(event) {
    let msg = JSON.parse(event.data);
    if (msg.MessageId == 'Action_Copy_Resp') {
        pasteBoard = msg.Values.content;
    }
}

post({
    'MessageId': 'Action_Copy',
    'Values': {
        'Mimetype': 'text/markdown;charset=utf-8',
    }
});
```

This outputs the current selection into the variable `pasteBoard`.

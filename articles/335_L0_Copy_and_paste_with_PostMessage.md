---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/technotes/copy_paste_postmessage.xhtml"
source_file: "docs/technotes/copy_paste_postmessage.xhtml"
source_anchor: ""
title: "Copy and paste with PostMessage"
canonical_title: "Copy and paste with PostMessage"
toc_level: "0"
breadcrumbs: "Copy and paste with PostMessage"
---
# How to copy and insert text with PostMessage

This tech note will show you how to copy and insert text with the [PostMessage API](257_L0_PostMessage_API.md).

There are essentially two different post messages: `Action_Copy` and `Action_Paste`. The former will copy the current selection in the specified format and then reply with an `Action_Copy_Resp` message, while the latter will insert the data at the insertion point, with the specified type.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/postmessage_api.xhtml#embedding-iframe"
source_file: "docs/postmessage_api.xhtml"
source_anchor: "embedding-iframe"
title: "Embedding Iframe"
canonical_title: "PostMessage API / Embedding Iframe"
toc_level: "1"
breadcrumbs: "PostMessage API / Embedding Iframe"
---
**Editor to WOPI Host**

Collabora Online sends an `Iframe_Height` postMessage to the WOPI host to dynamically adjust the height of the embedded iframe and prevent scrollbars.

| MessageId | Values | Description |
| --- | --- | --- |
| Iframe_Height | ContentHeight: <String> | Sent by editor to the WOPI Host. Use the ContentHeight value to set the height of the embedded iframe dynamically in your UI, ensuring a seamless user experience without scrollbars. |

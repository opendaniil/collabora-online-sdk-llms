---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#using-different-domain-for-collabora-online-and-embedding-application"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "using-different-domain-for-collabora-online-and-embedding-application"
title: "Using different domain for Collabora Online and embedding application."
canonical_title: "Troubleshooting / Further symptoms / Using different domain for Collabora Online and embedding application."
toc_level: "2"
breadcrumbs: "Troubleshooting / Further symptoms / Using different domain for Collabora Online and embedding application."
---
In this case, you might encounter such errors:

```
Uncaught SecurityError: Failed to read a named property 'print' from 'Window': Blocked a frame with origin "https://collabora-online.local" from accessing a cross-origin frame.
```

This error is due to browser security mecanism, [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy]. It restricts what content can be loaded on the page and what can iframe do.

Use this reference Content-Security-Policy on the page serving the Collabora Online <iframe>:

```
Content-Security-Policy: default-src 'none';base-uri 'none';manifest-src 'self';style-src 'self' 'unsafe-inline';img-src 'self' data: blob: https://collabora-online.local;font-src 'self' data:;connect-src 'self';media-src 'self';frame-src 'self' https://collabora-online.local;worker-src 'self';frame-ancestors 'self' https://collabora-online.local;form-action 'self' https://collabora-online.local
```

Replace https://collabora-online.local by the url of your Collabora Online instance.

This is a restrictive policy that you might need to adjust. In particular, `font-src`, `image-src` or `media-src` if in your page you need to load resources from other domains, `frame-src` if you need to have other iframe inserted.

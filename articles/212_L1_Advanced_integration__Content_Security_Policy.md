---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#content-security-policy"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "content-security-policy"
title: "Content Security Policy"
canonical_title: "Advanced integration / Content Security Policy"
toc_level: "1"
breadcrumbs: "Advanced integration / Content Security Policy"
---
Content Security Policy, or CSP, declares the policy for the web content. Please refer to MDN for the [documentation on CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy) [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy].

You can set this security policy by changing the `content_security_policy` value in the `net` section of the coolwsd.xml file. The format is the exact same as for the HTTP headers.

One important directive for the CSP is the `frame-ancestors`. It determines where the COOL frame can be embedded. This is important if your WOPI host is a different domain from the Collabora Online server. It is strongly discouraged to set it as being a wildcard `*`. If you get an error when embedding Collabora Online, you probably need to change the policy.

Another important directive is for the displaying avatar. Given that the URL might redirect to a different service, it should be explicitely allowed by a CSP directive for `image-src`. If you are unsure about whether the CSP needs to be adjusted, the console in the web browser will show errors for the `image-src`.

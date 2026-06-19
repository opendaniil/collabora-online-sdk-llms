---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#authentication"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "authentication"
title: "Authentication"
canonical_title: "Advanced integration / Setup Settings iframe / Authentication"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Authentication"
---
To securely access files, your application must pass an authentication token named `access_token` to the iframe settings.

**Note:** Ensure that you generate separate tokens for admin and user, and validate them accordingly.

You can pass `access_token_ttl` during iframe creation to specify the token’s expiration time.

We follow a process similar to the Collabora Online document iframe, so you can [read more about how we pass authentication token](146_L0_How_to_integrate.md).

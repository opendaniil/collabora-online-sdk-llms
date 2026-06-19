---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/How_to_integrate.xhtml#authentication"
source_file: "docs/How_to_integrate.xhtml"
source_anchor: "authentication"
title: "Authentication"
canonical_title: "How to integrate / Authentication"
toc_level: "1"
breadcrumbs: "How to integrate / Authentication"
---
To be able to access files securely, your application has to pass an authentication token to Collabora Online `access_token`. From the Collabora Online point of view, it can be any random number / string, that will be passed as part of the URL when accessing the document storage.

The only requirements are that it has to be unique for the user, that the file storage denies access with wrong authentication token, and that it can be passed in an URL (ie. contains just characters / numbers / underlines).

Note

The `access_token` is also passed as part of the HTTP headers in the [Authorization](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Authorization) [https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Authorization] header with a `Bearer` scheme. This is done for compatibility reasons if you use OAuth as part of your authentication stack. See [Microsoft 365 FAQ](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/faq/access-token-header-and-url) [https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/faq/access-token-header-and-url].

You can also pass `access_token_ttl` during the iframe creation to specify when the token expires. The value is a UNIX timestamp, the number of milliseconds since the UNIX epoch, i.e. January 1st 1970. This TTL indicate when Collabora Online should notify the users, 15 minutes prior, that the session will expire. You pass it at the same time as the `access_token` for the [iframe creation](153_L0_Step-by-step_tutorial.md).

Currently this is the only supported way of authentication (`access_header` has been deprecated).

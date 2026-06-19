---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#checking-for-an-update"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "checking-for-an-update"
title: "Checking for an update"
canonical_title: "Advanced integration / Update checker / Checking for an update"
toc_level: "2"
breadcrumbs: "Advanced integration / Update checker / Checking for an update"
---
You can check which version is released by checking an endpoint URL provided by Collabora Productivity. The URL is `https://rating.collaboraonline.com/UpdateCheck` and it will return a JSON payload. The endpoint takes two optional query parameters.

- `product`: if it is omitted or equal to `Collabora Online Development Edition` the update version of CODE will be returned. Any other value will result the update version of COOL. You can pass the `productName` that you extracted from the response of `/hosting/capabilities` endpoint.
- `version`: the endpoint may return different update versions depending on the current version. You can pass the `productVersion` that you extracted from the response of `/hosting/capabilities` endpoint.

#### Examples

```
$ curl https://rating.collaboraonline.com/UpdateCheck
{"coolwsd_version": "24.04.11.2"}
```

This returns the version of CODE (product name is assumed to be `Collabora Online Development Edition`).

```
$ curl https://rating.collaboraonline.com/UpdateCheck?product=Collabora%20Online%20Development%20Edition
{"coolwsd_version": "24.04.11.2"}
```

This returns the version of CODE (product name is `Collabora Online Development Edition`).

```
$ curl https://rating.collaboraonline.com/UpdateCheck?product=Collabora%20Online
{"coolwsd_version": "24.04.10.4"}
```

This returns the version of COOL (product name is `Collabora Online`).

```
$ curl https://rating.collaboraonline.com/UpdateCheck?product=cool
{"coolwsd_version": "24.04.10.4"}
```

This returns the version of COOL (because whatever else you pass in the `product` query parameter, the endpoint returns the update version of COOL).

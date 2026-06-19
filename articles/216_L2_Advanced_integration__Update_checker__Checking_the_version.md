---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#checking-the-version"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "checking-the-version"
title: "Checking the version"
canonical_title: "Advanced integration / Update checker / Checking the version"
toc_level: "2"
breadcrumbs: "Advanced integration / Update checker / Checking the version"
---
The `/hosting/capabilities` endpoint provide a JSON payload that contain information about the capabilities of the running Collabora Online instance. Two of the fields of interest are:

- `productName`: the name of the product. `Collabora Online` and `Collabora Online Development Edition` are two of the know values. Some branded versions of Collabora Online may return other product names.
- `productVersion`: the product version as a string. Usually in the form of x.y.z.a but it can contain arbitrary values.

Use this to determine which product and version are installed.

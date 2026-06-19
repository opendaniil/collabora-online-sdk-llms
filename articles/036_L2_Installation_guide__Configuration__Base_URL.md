---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#base-url"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "base-url"
title: "Base URL"
canonical_title: "Installation guide / Configuration / Base URL"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Base URL"
---
It is possible to use a different base URL than the toplevel as the service root by setting `net.service_root` in the configuration file. The value is prefixed to any URL path for Collabora Online, including the discovery file.

This is useful if the rules of your organization do not permit running services in the root, requiring you to use a subpath for it, like `https://example.org/IT/CollaboraOnline`. By setting `/IT/CollaboraOnline` as the value `net.service_root` in the configuration file, all the Collabora Online URL would be under `https://example.org/IT/CollaboraOnline`, inluding the discovery file that would become `https://example.org/IT/CollaboraOnline/hosting/discovery`.

This is also useful if you want to proxy all the http requests through the same host, but have a namespace for the URL as to not conflict with the rest.

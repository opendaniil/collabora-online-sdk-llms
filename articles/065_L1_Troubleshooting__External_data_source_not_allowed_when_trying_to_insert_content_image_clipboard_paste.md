---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#external-data-source-not-allowed-when-trying-to-insert-content-image-clipboard-paste"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "external-data-source-not-allowed-when-trying-to-insert-content-image-clipboard-paste"
title: "‘External data source not allowed’ when trying to insert content (image, clipboard paste)."
canonical_title: "Troubleshooting / ‘External data source not allowed’ when trying to insert content (image, clipboard paste)."
toc_level: "1"
breadcrumbs: "Troubleshooting / ‘External data source not allowed’ when trying to insert content (image, clipboard paste)."
---
We block requests from the Collabora Online server to the hosts which are not trusted. If you want to enable access to some hosts then you have to add regex into coolwsd.xml file in the``net.lok_allow`` section (host without port or scheme, IP or domain name depending on which one will be used in the request, we don’t resolve names). Hosts already defined in `storage.wopi.alias_groups` or `net.post_allow` should be enabled automatically.

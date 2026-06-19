---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#validating-digital-signatures"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "validating-digital-signatures"
title: "Validating digital signatures"
canonical_title: "Installation guide / Configuration / Validating digital signatures"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Validating digital signatures"
---
Collabora Online uses NSS (Mozilla’s Network Security Services) for validation of digital signatures. NSS comes with default configuration that includes a few trusted root CAs, but users may want to import their own trusted root CAs. The `certificates.database_path` configuration option in `/etc/coolwsd/coolwsd.xml` specifies the NSS certificate database that should be used with Collabora Online. This database should be readable by the coolwsd process. Custom root certificates can be imported into this database. For detailed instructions about creating NSS certificate database and importing certificates, please refer to the [manual of the certutil tool](http://udn.realityripple.com/docs/Mozilla/Projects/NSS/tools/NSS_Tools_certutil) [http://udn.realityripple.com/docs/Mozilla/Projects/NSS/tools/NSS_Tools_certutil], that is provided by mozilla-nss-tools, nss-tools or libnss3-tools package, depending on the Linux distribution.

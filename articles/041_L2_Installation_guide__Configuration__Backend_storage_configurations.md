---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#backend-storage-configurations"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "backend-storage-configurations"
title: "Backend storage configurations"
canonical_title: "Installation guide / Configuration / Backend storage configurations"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Backend storage configurations"
---
Currently there are two backend storages are implemented: **file system** and **WOPI**.

File system storage is disabled by default, and should not be used in production environment. It is insecure by nature, because it serves any file that the *cool* user can read from the local file system, including `/etc/coolwsd/coolwsd.xml`, `/etc/passwd` and so on. It can be used for testing only. To enable:

in storage block of coolwsd.xml

```
 <filesystem allow=”true” />
```

or

in command line

```
 --o:storage.filesystem[@allow]=true
```

WOPI on the other hand is the recommended backend storage. WOPI is Web Application Open Platform Interface, a protocol based on open standard for remote document access with authentication. Collabora Online accepts connection requests only from trusted WOPI hosts. The administrator has to list the host names and/or IP addresses of these trusted WOPI hosts in the storage.wopi block. Please note that connection requests from the same machine are always accepted.

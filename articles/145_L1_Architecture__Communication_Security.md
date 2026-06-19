---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#communication-security"
source_file: "docs/architecture.xhtml"
source_anchor: "communication-security"
title: "Communication Security"
canonical_title: "Architecture / Communication Security"
toc_level: "1"
breadcrumbs: "Architecture / Communication Security"
---
When the host integration client initiates a request to view or edit a document in Collabora Online, it will generate and transmit an [authentication token](146_L0_How_to_integrate.md) to the WSD. The WSD will send back this authentication token with any WOPI request used to read or save the document. This token will need to be verified by the host (the WOPI Server). The WOPI request is done over HTTPS, and WSD will verify the validity of the TLS certificate of the host when performing WOPI request. This is the access control mechanism for the publicly facing part of Collabora Online.

Behind, the WSD will establish a client connection between itself and a new instance of LOKit that was just created, instance contained in a chroot jail, where system calls and file system access are limited and where only one document is loaded at a time. The LOKit instance and WSD are run the same machine and the communication is done over UNIX domain socket. The legitimacy of the connection is verified using the standard UNIX socket peer credentials mechanism and matching of uid / gid.

Note that this doesn’t protect against any tampering done by the super-user (root) on the machine running WSD and LOKit.

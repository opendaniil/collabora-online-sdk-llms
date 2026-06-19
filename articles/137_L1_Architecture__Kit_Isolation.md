---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/architecture.xhtml#kit-isolation"
source_file: "docs/architecture.xhtml"
source_anchor: "kit-isolation"
title: "Kit Isolation"
canonical_title: "Architecture / Kit Isolation"
toc_level: "1"
breadcrumbs: "Architecture / Kit Isolation"
---
Before isolating the Kit process, it needs to create a shadow file system (see below for details). Preparing the shadow file system can be done either by bind-mount from a template directory (preferred) or by linking (if possible) or, failing that, by copying the files. The template directory contains important files to run the Core as well as various files from the system (from /etc) for the timezone, hosts, and similar files.

When bind-mount is enabled (default) and available (some systems and especially containers might not allow it), it is very fast to set up and is done with read-only permissions, which adds yet another layer of security.

After the shadow file system is ready, chroot(2) is called to change the visible root file system for the current Kit process to be that of the shadow file system. No files outside of this root is visible or accessible to the Kit process, isolating it completely from the host system.

Next, since certain capabilities are needed to execute the above (specifically, mount and chroot are privileged), capabilities are dropped to minimize the available system calls.

Finally, all system calls are disabled, even the unprivileged ones, with the exception of the strictly required ones. For example, the kill(2) sys- call is disabled, as well accept(2) and listen(2), which are used to create listening sockets.

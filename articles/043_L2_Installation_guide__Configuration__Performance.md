---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#performance"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "performance"
title: "Performance"
canonical_title: "Installation guide / Configuration / Performance"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Performance"
---
There are two performance categories.

One is related to how fast new processes to load documents are spawned. There are two settings related to that. The first is `num_prespawn_children`. It is the number of child processes to keep started in advance and waiting for new clients. More prespawn children consume more memory, but server answers more quickly to requests under load. The default is `1`.

The second is `mount_jail_tree`. Setting it to `true` (the default) allows for setting up the files used in the jailed document process quickly. This, however, requires `CAP_SYS_ADMIN`, which might not be available especially in containers. If this is enabled and mounting fails, the Server Audit will show this as a failure. Alternatively, when it is disabled, the files necessary for the jailed process will either be linked (if possible) or copied (when linking is not available), which are much slower than bind-mounting. When bind-mounting is disabled from the config the Server Audit will show this as recommendation and will not fail.

The other performance category is `per_document.max_concurrency` which limits the number of threads to use while processing a document. The default here is `4`. The rule is that **the value should be lower or equal to the number of CPU threads** (see the command `nproc`), making the default suitable for a machine with at least 4 CPU threads and is most suited for the general use. A value bigger than the number of CPU threads may have a negative impact on the performance and will be ignored (set to the number of available CPU threads). A value bigger than 16 shall be avoided in general.

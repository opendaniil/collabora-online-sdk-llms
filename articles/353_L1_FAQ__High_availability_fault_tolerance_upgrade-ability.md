---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/faq.xhtml#high-availability-fault-tolerance-upgrade-ability"
source_file: "docs/faq.xhtml"
source_anchor: "high-availability-fault-tolerance-upgrade-ability"
title: "High availability, fault tolerance, upgrade-ability?"
canonical_title: "FAQ / High availability, fault tolerance, upgrade-ability?"
toc_level: "1"
breadcrumbs: "FAQ / High availability, fault tolerance, upgrade-ability?"
---
Clearly you want a high availability setup, not only to provide extra scalability, but also to provide redundancy against faults. Collabora Online has a clean and attractive architecture – which scales with your routing network:

> - Each document is served by a single node to which all requests and edits are sent for that document by the HA gateway: F5, HA proxy etc..
> - Each node is ultimately stateless and needs only limited local storage).
> - Collabora Online requires no third party services except of course it needs to connect to your existing file-storage solution.
> - Collabora Online regularly saves documents to your existing storage.
> - Collabora Online requires only a standard, basic Linux base-system to run on top of.

![../_images/architecture.png](assets/_images/architecture.png)

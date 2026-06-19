---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: ""
title: "Collabora Online on OpenShift"
canonical_title: "Installation guide / Collabora Online on OpenShift"
toc_level: "1"
breadcrumbs: "Installation guide / Collabora Online on OpenShift"
---
OpenShift deployments of Collabora Online (COOL) need two OpenShift-specific decisions on top of the generic Kubernetes flow documented in [Collabora Online for Kubernetes](014_L1_Installation_guide__Collabora_Online_for_Kubernetes.md):

1. **Ingress controller.** OpenShift’s default Router cannot do URL-parameter consistent hashing on a per-Route basis - its `haproxy.router.openshift.io/balance` annotation only accepts `roundrobin`, `leastconn`, and `source`, none of which keep requests for the same document pinned to the same pod. A separate Ingress controller (HAProxy Kubernetes Ingress) has to be installed in the cluster.
2. **Security Context Constraints (SCCs).** OpenShift’s pod admission denies the capabilities COOL needs for jail creation unless an appropriate SCC is granted. Three options are described below, from most to least restrictive.

The rest of the deployment, including the bulk of the `cool_values.yaml` reference (replica count, autoscaling caveats, `aliasgroups`, resource sizing, dynamic configuration, custom fonts, monitoring), mirrors [Collabora Online for Kubernetes](014_L1_Installation_guide__Collabora_Online_for_Kubernetes.md) exactly. This page only documents the OpenShift-specific bits and links back where the generic guidance applies.

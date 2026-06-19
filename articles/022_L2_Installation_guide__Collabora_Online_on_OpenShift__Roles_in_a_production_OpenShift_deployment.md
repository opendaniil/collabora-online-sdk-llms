---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml#roles-in-a-production-openshift-deployment"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: "roles-in-a-production-openshift-deployment"
title: "Roles in a production OpenShift deployment"
canonical_title: "Installation guide / Collabora Online on OpenShift / Roles in a production OpenShift deployment"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online on OpenShift / Roles in a production OpenShift deployment"
---
In production OpenShift (ROSA, ARO, on-prem with governance) app teams typically have namespace-admin at most, not cluster-admin. The work splits across two roles:

| Role | Responsibility |
| --- | --- |
| Cluster administrator (platform / SRE team, one-time per cluster) | Install HAProxy Kubernetes Ingress, create the collabora namespace, create and bind the SCC for the chosen option, and grant the app team admin on the namespace. |
| App team developer (per deployment) | Write cool_values.yaml against the prepared namespace and helm install the chart. Manage rollouts and configuration. |

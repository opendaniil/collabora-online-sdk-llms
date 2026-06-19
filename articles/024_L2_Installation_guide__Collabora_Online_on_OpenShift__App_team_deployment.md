---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml#app-team-deployment"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: "app-team-deployment"
title: "App team deployment"
canonical_title: "Installation guide / Collabora Online on OpenShift / App team deployment"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online on OpenShift / App team deployment"
---
Run these steps as the app team’s developer account (e.g. `developer` on CRC). The cluster administrator must have completed the setup section above first.

### Step D1: Write cool_values.yaml

The Ingress block and the `securityContext` block are OpenShift-specific; everything else (`replicaCount`, `collabora`, `autoscaling`, `resources`) follows the same rules as [Collabora Online for Kubernetes](014_L1_Installation_guide__Collabora_Online_for_Kubernetes.md).

Start from this base, then merge in the `securityContext` / `serviceAccount` block from the SCC option your admin applied (Security Context Constraints (SCCs)):

```
replicaCount: 3

ingress:
  enabled: true
  className: "haproxy"
  annotations:
    haproxy.org/timeout-tunnel: "3600s"
    haproxy.org/backend-config-snippet: |
      balance url_param WOPISrc check_post
  hosts:
    - host: test.collabora.online
      paths:
        - path: /
          pathType: Prefix
  tls:
    - secretName: tls-secret-name
      hosts:
        - test.collabora.online

autoscaling:
  enabled: false

collabora:
  aliasgroups:
    - host: "https://example.integrator.com:443"
  extra_params: >
    --o:ssl.enable=false
    --o:ssl.termination=true
    --o:num_prespawn_children=4

resources:
  limits:
    cpu: "4000m"
    memory: "8000Mi"
  requests:
    cpu: "4000m"
    memory: "6000Mi"
```

Note

See [Collabora Online for Kubernetes](014_L1_Installation_guide__Collabora_Online_for_Kubernetes.md) for the full `cool_values.yaml` reference (multiple aliasgroups, `server_name` for reverse-proxied hostnames, HPA caveats, custom fonts, dynamic configuration, monitoring) - all of it applies unchanged on OpenShift.

### Step D2: Install the chart

```
helm repo add collabora https://collaboraonline.github.io/online/
helm install --namespace collabora \
  collabora-online collabora/collabora-online \
  -f cool_values.yaml
```

Wait for the pod to reach `Ready`:

```
oc -n collabora get pod -w
```

If the pod fails to start with a `SecurityContextConstraints` error, the SCC was not bound correctly - escalate back to your cluster administrator and re-check step CA3.

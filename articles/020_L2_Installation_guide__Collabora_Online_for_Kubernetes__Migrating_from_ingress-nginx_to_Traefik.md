---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Kubernetes.xhtml#migrating-from-ingress-nginx-to-traefik"
source_file: "docs/installation/Kubernetes.xhtml"
source_anchor: "migrating-from-ingress-nginx-to-traefik"
title: "Migrating from ingress-nginx to Traefik"
canonical_title: "Installation guide / Collabora Online for Kubernetes / Migrating from ingress-nginx to Traefik"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online for Kubernetes / Migrating from ingress-nginx to Traefik"
---
[ingress-nginx](https://github.com/kubernetes/ingress-nginx) [https://github.com/kubernetes/ingress-nginx] is reaching end of life. Existing COOL deployments can move to Traefik without changing any of their Ingress YAMLs - the `nginx.ingress.kubernetes.io/*` annotation set used throughout this guide is also understood by Traefik’s `kubernetesIngressNGINX` provider.

### Prerequisites

- Traefik **3.7.0** or later (the minimum version with `upstream-hash-by` support).
- Helm install of Traefik with the `kubernetesIngressNginx` provider enabled - see Setting up Traefik with the kubernetesIngressNGINX provider for the full install steps.

Note

Traefik’s default `kubernetesIngress` provider does **not** implement URL-parameter consistent hashing. If you enable Traefik but leave the `kubernetesIngressNGINX` provider disabled (the default), the `upstream-hash-by` annotation is parsed but ignored, and requests are round-robined across COOL pods. This silently breaks collaborative editing. The verification step below confirms hashing is actually working.

### Migration steps

1. **Preserve the existing IngressClass before uninstalling ingress-nginx.** Traefik’s `kubernetesIngressNGINX` provider will continue to use the same `nginx` IngressClass to claim your Ingresses, so it must not be deleted when ingress-nginx goes away. Per the upstream [Traefik NGINX migration guide](https://doc.traefik.io/traefik/master/migrate/nginx-to-traefik/) [https://doc.traefik.io/traefik/master/migrate/nginx-to-traefik/]:
  ```
  helm upgrade ingress-nginx ingress-nginx \
    --repo https://kubernetes.github.io/ingress-nginx \
    --namespace ingress-nginx \
    --reuse-values \
    --set-json 'controller.ingressClassResource.annotations={"helm.sh/resource-policy": "keep"}'
  ```
2. **Install Traefik** with the `kubernetesIngressNGINX` provider enabled (see Setting up Traefik with the kubernetesIngressNGINX provider).
3. **Uninstall ingress-nginx.** The IngressClass remains thanks to the `helm.sh/resource-policy: keep` annotation set in step 1.
4. **Restart the COOL pods** so they re-establish any monitor WebSocket connections through the new ingress:
  ```
  kubectl -n collabora rollout restart deployment
  ```
5. **Verify URL-parameter hashing works.** Run this against your external endpoint - any path works, the hash key is the query parameter:
  ```
  for i in $(seq 1 10); do
    curl -sk "https://test.collabora.online/hosting/capabilities?WOPISrc=test1" \
      | grep -oE '"serverId":[^,}]+'
  done | sort | uniq -c
  ```
  - **Pass**: exactly one line - the same `serverId` for all 10 requests with the same `WOPISrc`.
  - **Fail**: multiple lines - requests are being round-robined and collaborative editing will be broken. Check that the `kubernetesIngressNginx` provider is enabled (`kubectl -n traefik logs ... | grep ingressnginx`) and that your Ingress’s `className` matches the IngressClass the provider claims.
  For the COOL Controller umbrella, use `RouteToken` instead of `WOPISrc` in the curl URL.

### Fresh install

If you do not have an existing ingress-nginx install to migrate from, follow Setting up Traefik with the kubernetesIngressNGINX provider in the Prerequisites section instead. The standard `cool_values.yaml` and `umbrella_values.yaml` examples in this guide already use `className: "nginx"` and `nginx.ingress.kubernetes.io/*` annotations, which work as-is with Traefik 3.7+.

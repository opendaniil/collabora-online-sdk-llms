---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Kubernetes.xhtml#prerequisites"
source_file: "docs/installation/Kubernetes.xhtml"
source_anchor: "prerequisites"
title: "Prerequisites"
canonical_title: "Installation guide / Collabora Online for Kubernetes / Prerequisites"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online for Kubernetes / Prerequisites"
---
1. Install [helm](https://helm.sh/docs/intro/install/) [https://helm.sh/docs/intro/install/]
2. Setting up Kubernetes Ingress Controller
  COOL relies on the ingress to consistently route requests for the same document to the same pod, using URL-parameter hashing on `WOPISrc` (standard chart) or `RouteToken` (COOL Controller umbrella). The following controllers support the required hashing:
  - **Traefik 3.7+** with the `kubernetesIngressNGINX` provider enabled (recommended). See Setting up Traefik with the kubernetesIngressNGINX provider below. The Ingress YAML examples in this guide use `className: "nginx"` and `nginx.ingress.kubernetes.io/*` annotations; with this Traefik provider, those work unchanged.
  - [HAproxy Ingress Controller by HAproxy Technologies](https://www.haproxy.com/documentation/kubernetes-ingress) [https://www.haproxy.com/documentation/kubernetes-ingress]. For HAproxy, swap to the commented HAproxy blocks shown alongside each example below.
  - [HAproxy Ingress Controller by jcmoraisjr](https://github.com/jcmoraisjr/haproxy-ingress) [https://github.com/jcmoraisjr/haproxy-ingress].
  - [Nginx Ingress Controller](https://kubernetes.github.io/ingress-nginx/deploy/) [https://kubernetes.github.io/ingress-nginx/deploy/].
    Warning
    `ingress-nginx` is reaching end of life and is no longer recommended for new deployments. Existing installations can migrate to Traefik without changing any Ingress YAMLs - see Migrating from ingress-nginx to Traefik.
  Note
  - The deployment examples below use `className: "nginx"` and `nginx.ingress.kubernetes.io/*` annotations. With Traefik 3.7+ and the `kubernetesIngressNGINX` provider enabled, this YAML works unchanged. For HAproxy, swap to the commented HAproxy blocks alongside each example.
  - **OpenShift**: the default Router cannot be used as the ingress for COOL. See [Collabora Online on OpenShift](021_L1_Installation_guide__Collabora_Online_on_OpenShift.md) for the OpenShift-specific ingress (HAproxy Kubernetes Ingress) and SCC guidance.

### Setting up Traefik with the kubernetesIngressNGINX provider

Traefik’s default Kubernetes Ingress provider parses `nginx.ingress.kubernetes.io/upstream-hash-by` but does *not* implement URL-parameter consistent hashing - it round-robins, which silently breaks collaborative editing. Traefik 3.7+ ships a separate `kubernetesIngressNGINX` provider that does implement the hashing; it is disabled by default and must be enabled at install time.

For more background, see the upstream [Traefik NGINX migration guide](https://doc.traefik.io/traefik/master/migrate/nginx-to-traefik/) [https://doc.traefik.io/traefik/master/migrate/nginx-to-traefik/].

1. Install Traefik 3.7.0 or later with the `kubernetesIngressNginx` provider enabled:
  ```
  helm repo add traefik https://traefik.github.io/charts
  helm repo update
  helm install traefik traefik/traefik \
    --namespace traefik --create-namespace \
    --set image.tag=v3.7.0 \
    --set providers.kubernetesIngressNginx.enabled=true
  ```
  Pin or use a newer 3.7.x release as appropriate; v3.7.0 is the minimum that includes `upstream-hash-by` support.
2. Apply an `IngressClass` so the new provider can claim Ingresses that use `className: "nginx"`. For a fresh cluster with no prior ingress-nginx install:
  ```
  apiVersion: networking.k8s.io/v1
  kind: IngressClass
  metadata:
    name: nginx
  spec:
    controller: k8s.io/ingress-nginx
  ```
  Save the above as `ingressclass-nginx.yaml` and apply with `kubectl apply -f ingressclass-nginx.yaml`.
  If you are migrating from an existing ingress-nginx install, do not create a new IngressClass - instead, preserve the existing one when uninstalling ingress-nginx as described in Migrating from ingress-nginx to Traefik.
3. Confirm the new provider has started by checking Traefik logs:
  ```
  kubectl -n traefik logs -l app.kubernetes.io/name=traefik | grep ingressnginx
  ```
  A line containing `Starting provider *ingressnginx.Provider` confirms the provider is running.
4. After deploying the COOL chart (see the next section), verify that URL-parameter hashing actually takes effect. See the verification one-liner in Migrating from ingress-nginx to Traefik.

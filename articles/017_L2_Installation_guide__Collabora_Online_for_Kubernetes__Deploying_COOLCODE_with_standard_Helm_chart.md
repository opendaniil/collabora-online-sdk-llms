---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Kubernetes.xhtml#deploying-cool-code-with-standard-helm-chart"
source_file: "docs/installation/Kubernetes.xhtml"
source_anchor: "deploying-cool-code-with-standard-helm-chart"
title: "Deploying COOL/CODE with standard Helm chart"
canonical_title: "Installation guide / Collabora Online for Kubernetes / Deploying COOL/CODE with standard Helm chart"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online for Kubernetes / Deploying COOL/CODE with standard Helm chart"
---
In order for collaborative editing to operate, it is vital to ensure that all users editing the same document and all the clipboard request end up being served by the same pod. Using the WOPI protocol, the https URL includes a unique identifier (`WOPISrc`) for use with this document. Thus load balancing can be done by using `WOPISrc` – ensuring that all URLs that contain the same `WOPISrc` are sent to the same pod.

1. Create an `cool_values.yaml` (if your setup differs e.g. take an look in then [collabora-online/values.yaml](https://github.com/CollaboraOnline/online/blob/main/kubernetes/helm/collabora-online/values.yaml) [https://github.com/CollaboraOnline/online/blob/main/kubernetes/helm/collabora-online/values.yaml] ) of the helmchart
  ```
  replicaCount: 3
  ingress:
    enabled: true
    className: "nginx"
    annotations:
      nginx.ingress.kubernetes.io/enable-access-log: "true"
      nginx.ingress.kubernetes.io/upstream-hash-by: "$arg_WOPISrc"
      nginx.ingress.kubernetes.io/proxy-body-size: "0"
      nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
      nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
    hosts:
      - host: test.collabora.online
        paths:
          - path: /
            pathType: Prefix
    tls:
      - secretName: tls-secret-name
        hosts:
          - test.collabora.online
  # Ingress settings for HAproxy Ingress Controller by HAproxy Technologies
  # ingress:
  #    enabled: true
  #    className: "haproxy"
  #    annotations:
  #        haproxy.org/timeout-tunnel: "3600s"
  #        haproxy.org/backend-config-snippet: |
  #          balance url_param WOPISrc check_post
  #    hosts:
  #        - host: test.collabora.online
  #          paths:
  #          - path: /
  #            pathType: Prefix
  #    tls:
  #    - secretName: tls-secret-name
  #      hosts:
  #        - test.collabora.online
  # Ingress settings for HAproxy Ingress Controller by jcmoraisjr
  # ingress:
  #    enabled: true
  #    className: "haproxy"
  #    annotations:
  #        haproxy-ingress.github.io/timeout-tunnel: 3600s
  #        haproxy-ingress.github.io/balance-algorithm: url_param WOPISrc check_post
  #    hosts:
  #        - host: test.collabora.online
  #          paths:
  #          - path: /
  #            pathType: Prefix
  #    tls:
  #    - secretName: tls-secret-name
  #      hosts:
  #        - test.collabora.online
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
  - **Horizontal Pod Autoscaling (HPA) is disabled for now.** Because after scaling it breaks the collaborative editing and copy/paste. Therefore please set `replicaCount` as per your needs.
  - If you have multiple host and aliases setup set aliasgroups in `my_values.yaml`:
    ```
    collabora:
      - host: "<protocol>://<host-name>:<port>"
        # if there are no aliases you can ignore the below line
        aliases: ["<protocol>://<its-first-alias>:<port>, <protocol>://<its-second-alias>:<port>"]
      # more host and aliases list is possible
    ```
  - Specify `server_name` when the hostname is not reachable directly for example behind reverse-proxy
    ```
    collabora:
      server_name: <hostname>:<port>
    ```
2. Install the helm chart using the command below, it should deploy the Collabora Online
  ```
  helm repo add collabora https://collaboraonline.github.io/online/
  helm install --create-namespace --namespace collabora collabora-online collabora/collabora-online -f cool_values.yaml
  ```
3. To check if everything is setup correctly you can run:

> ```
> curl 'https://test.collabora.online/'
> ```
>
> It should return a similar output as below:
>
> ```
> HTTP/1.1 200 OK
> last-modified: Tue, 18 May 2021 10:46:29
> user-agent: COOLWSD WOPI Agent 6.4.8
> content-length: 2
> content-type: text/plain
> ```

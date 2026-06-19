---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Kubernetes.xhtml#cool-controller"
source_file: "docs/installation/Kubernetes.xhtml"
source_anchor: "cool-controller"
title: "COOL Controller"
canonical_title: "Installation guide / Collabora Online for Kubernetes / COOL Controller"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online for Kubernetes / COOL Controller"
---
## COOL Controller [https://www.collaboraonline.com/collabora-online-controller/]

The COOL Controller is a solution designed to address specific challenges encountered when deploying Collabora Online (COOL) in a Kubernetes cluster. This controller tackles two main problems: ensuring requests for the same document are routed to the same pod, and managing the performance impact during scale up/down events. Additionally, it provides a cluster overview page and allows administrators to access individual pod admin consoles.

The first problem arises from the need to maintain session consistency in COOL deployments. To achieve this, the controller creates a mapping of Server IDs and RouteTokens. The RouteToken acts as a unique identifier for each pod, ensuring that requests containing the corresponding token are always directed to the correct pod. By maintaining this mapping, the controller guarantees that collaborative editing and copy-paste functionalities work correctly, even in scaled deployments.

During scale up/down events in a COOL deployment within a Kubernetes cluster, performance degradation occurs due to an uneven distribution of requests. Existing sessions remain connected to older pods while new requests are directed to the newly scaled pods, causing potential bottlenecks and sub optimal user experience. The COOL Kubernetes Controller addresses this problem with a document migrator. The controller continuously monitors memory utilization of COOL pods, with a target utilization percentage defined by administrators. If a pod’s memory utilization surpasses the target threshold, it is marked as overloaded. The controller initiates document migration from overloaded pods to less loaded pods, ensuring an even distribution of resources and requests. By actively migrating documents from overloaded to less loaded pods, the COOL Kubernetes Controller ensures a balanced distribution of requests and resources, mitigating performance degradation during scale up/down events. This optimization results in an enhanced user experience and smoother collaborative editing.

In addition to these core functionalities, the COOL Controller provides a cluster overview page that offers a centralized view of the deployment. Administrators can access individual pod admin consoles directly from this page, simplifying the management and monitoring of COOL deployments.

Overall, the COOL Controller enhances the deployment and management of Collabora Online in Kubernetes clusters. By addressing session consistency and performance optimization challenges, it enables a smooth and efficient collaborative editing experience for users.

### Access credentials

The COOL Controller can be offered to Collabora partners and customers. Please contact your Collabora Account Manager to learn more, and get credentials.

### Get latest version information

- Get latest tag name of helm charts, Collabora Online Docker image and COOL Controller Docker image
  - Create a env variable `CONTROLLER_PRIVATE_TOKEN` with your private access token
    ```
    export CONTROLLER_PRIVATE_TOKEN=<access_token>
    ```
  - run the following script
    ```
    repositories=(1578 1579 1719 1583 1581 1582)
    for repo_id in "${repositories[@]}"; do
      curl -s --header "PRIVATE-TOKEN: $CONTROLLER_PRIVATE_TOKEN" \
        --url "https://gitlab.collabora.com/api/v4/projects/5116/registry/repositories/$repo_id/tags?per_page=100" | \
        jq -r '.[] | select(.name | test("^(latest.*|snapshot.*|sha256.*)$") | not) | .location' | \
        sort -V | \
        tail -n 1
    done
    ```

### Deploying Collabora Online with COOL Controller

0. Prerequisites

> You should have a username and access token to access Collabora’s gitlab private container registry to download Docker images of COOL Controller and Collabora Online umbrella helm chart

1. Login to the gitlab private registry for Collabora Online Umbrella Helm Chart
  ```
  export CONTROLLER_PRIVATE_TOKEN=<access_token>
  helm registry login -u <username> -p $CONTROLLER_PRIVATE_TOKEN registry.gitlab.collabora.com/productivity/cool-controller-registry
  ```
  Use your access_token as password
2. Steps to Create a Kubernetes secret for pulling Collabora private registry
  1. Create namespace for Collabora Online and COOL Controller:
    ```
    kubectl create namespace collabora
    ```
  2. Setup Kubernetes Secret for COOL Controller in the Collabora Namespace:
    1. Docker login
      ```
      docker login registry.gitlab.collabora.com/productivity/cool-controller-registry -u <username> -p <controller_access_token>
      ```
    2. Create Kubernetes secret
      ```
      kubectl create secret generic controller-regcred --namespace collabora --from-file=.dockerconfigjson=<path/to/.docker/config.json> --type=kubernetes.io/dockerconfigjson
      ```
      replace `<path/to/.docker/config.json>` with path where `config.json` is located. Usually, the path would be `/home/your_username/.docker/config.json`
    - For more info [tutorial](https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials) [https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/#registry-secret-existing-credentials]
3. Deploy Collabora Online and COOL Controller
  Note
  Get latest tag version of COOL and COOL Controller using script
  1. create `umbrella_values.yaml`:
    ```
    collabora-online:
      replicaCount: 2
      ingress:
        enabled: true
        className: "nginx"
        annotations:
          nginx.ingress.kubernetes.io/upstream-hash-by: "$arg_RouteToken"
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
      # For this ingress we have filed a bug report related to inconsitent balancing https://github.com/haproxytech/kubernetes-ingress/issues/604
      # ingress:
      #    enabled: true
      #    className: "haproxy"
      #    annotations:
      #        haproxy.org/timeout-tunnel: "3600s"
      #        haproxy.org/backend-config-snippet: |
      #          balance url_param RouteToken check_post
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
      #        haproxy-ingress.github.io/balance-algorithm: url_param RouteToken check_post
      #    hosts:
      #        - host: test.collabora.online
      #          paths:
      #          - path: /
      #            pathType: Prefix
      #    tls:
      #    - secretName: tls-secret-name
      #      hosts:
      #        - test.collabora.online
      # to fetch COOL docker image
      imagePullSecrets:
        - name: controller-regcred
      collabora:
        aliasgroups:
          - host: "https://test.integrator.com:443"
        extra_params: --o:ssl.enable=false --o:indirection_endpoint.url=https://test.collabora.online/controller/routeToken --o:monitors.monitor[0]=ws://test.collabora.online/controller/ws --o:monitors.monitor[0][@retryInternal]=5
        # indirection_endpoint is used on client side to ask for routeToken from controller
        # monitor is used to maintain a socket connection with controller to get information about load, documents, etc
        username: <your-admin-console-username>
        password: <your-admin-console-password>
        env:
          - name: POD_NAME
            valueFrom:
              fieldRef:
                fieldPath: metadata.name
      autoscaling:
        enabled: true
        targetMemoryUtilizationPercentage: 80
        targetCPUUtilizationPercentage: 60
      resources:
        limits:
          cpu: "8000m"
          memory: "8000Mi"
        requests:
          cpu: "4000m"
          memory: "6000Mi"
    cool-controller:
      replicaCount: 2
      ingress:
        enabled: true
        # for haproxies you need "haproxy" as className
        # className: "haproxy"
        className: "nginx"
        annotations:
          nginx.ingress.kubernetes.io/proxy-read-timeout: "3600"
          nginx.ingress.kubernetes.io/proxy-send-timeout: "3600"
          nginx.ingress.kubernetes.io/proxy-body-size: "0"
        hosts:
          - host: test.collabora.online
            paths:
              - path: "/controller"
                pathType: Prefix
      imagePullSecrets:
        - name: controller-regcred # name of pull secret created on step 2
      controller:
        watchNamespace: "collabora" # namespace where collabora online is installed
        resourceName: "collabora-online" # resource to watch in that namespace
        ingressUrl: "https://test.collabora.online" ## url from which controller can access the COOL pods. The domain on which k8s cluster is exposed using LoadBalancer
        enableHashmapParallelization: true # whether to create hashmap parallely which is much faster
        # Note: Don't enable hashmap parallelization if your are using haproxy ingress controller
        namespacedRole: true # Set it to true so that all the role and role binding are restricted to collabora namespace
        statsInterval: 2000 # interval in millisecond at which the controller fetches new mem and cpu stats from socket connection
        documentMigrator:
          enabled: true
          coolMemoryUtilization: 80 # percentage utlization after which document migrator considers migrating documents, use the same value as targetMemoryUtilizationPercentage in online_values.yaml
          coolMemoryLimit: "8000Mi" # memory limit in megabytes by each cool pod should same as provided in online_values.yaml
        leaderElection:
          enabled: true # enables leader election for high availability
    ```
  > Note
  >
  > To view all configurable values for this chart, run the following Helm command:
  >
  > ```
  > helm show values oci://registry.gitlab.collabora.com/productivity/cool-controller-registry/helm-charts/collabora-online-umbrella
  > ```

> 2. Install using helm
>
> > Note
> >
> > Get latest tag version of COOL umbrella helm chart using script
> >
> > ```
> > helm install --create-namespace --namespace collabora collabora oci://registry.gitlab.collabora.com/productivity/cool-controller-registry/helm-charts/collabora-online-umbrella --version <version> -f /path/to/umbrella_values.yaml
> > # with nextcloud theming:
> > # helm install --create-namespace --namespace collabora collabora oci://registry.gitlab.collabora.com/productivity/cool-controller-registry/helm-charts/collabora-online-nc-umbrella --version <version> -f /path/to/umbrella_values.yaml
> > ```

- That’s it if everything is setup correctly, Collabora Online should return OK response. Admin cluster overview can be accessed on `https://test.collabora.online/browser/dist/admin/adminClusterOverview.html`

### Enable direct communication between COOL and COOL Controller within a Kubernetes cluster

This guide configures internal cluster communication between Collabora Online (COOL) and COOL Controller using Kubernetes DNS-based service discovery. By routing traffic through internal cluster DNS rather than external domains, you achieve:

- **Improved Performance**: Eliminates unnecessary network hops through external load balancers
- **Enhanced Security**: Keeps cluster-internal traffic isolated from the public internet

The key principle is using Kubernetes service DNS names (`<service>.<namespace>.svc.cluster.local`) for internal communication while maintaining external domains for client-facing endpoints.

0. Prerequisites
  > This feature requires **cool-controller:1.1.5** or later and helm chart version **1.1.8** or higher:
1. Locate Your Ingress Controller Service
  > First, identify your Ingress controller’s internal service name. Using Traefik as an example:
  >
  > ```
  > kubectl get svc -n traefik
  > ```
  >
  > **Example output:**
  >
  > ```
  > NAME      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
  > traefik   LoadBalancer   10.102.109.18   <pending>     80:30224/TCP,443:31987/TCP   1d
  > ```
  >
  > The internal DNS name follows this format:
  >
  > ```
  > <service-name>.<namespace>.svc.cluster.local
  > ```
  >
  > For Traefik installed per Setting up Traefik with the kubernetesIngressNGINX provider above: `traefik.traefik.svc.cluster.local`
  >
  > For a legacy ingress-nginx install, the equivalent would be `ingress-nginx-controller.ingress-nginx.svc.cluster.local`.
  >
  > **Note**: Your service name and namespace may differ depending on your Ingress controller type. Adjust accordingly in subsequent steps.
2. Locate COOL Controller Service
  > Identify the COOL Controller service in your deployment namespace:
  >
  > ```
  > kubectl get svc -n collabora
  > ```
  >
  > **Example output:**
  >
  > ```
  > NAME                         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
  > collabora-cool-controller    ClusterIP   10.106.76.189    <none>        9000/TCP   4h3m
  > ```
  >
  > The internal DNS name: `collabora-cool-controller.collabora.svc.cluster.local`
  >
  > Note
  >
  > Replace `collabora` with your actual namespace if different.
3. Configure Collabora Online
  > Update your Collabora Online configuration to use the internal COOL Controller DNS name for monitoring. The `monitors.monitor` parameter establishes WebSocket communication between COOL instances and the controller:
  >
  > ```
  > collabora:
  >   aliasgroups:
  >     - host: "https://integrator.local"
  >
  >   extra_params: >
  >     --o:ssl.enable=false
  >     --o:ssl.termination=true
  >     --o:ssl.verification=false
  >     --o:indirection_endpoint.url=https://test.collabora.online/controller/routeToken
  >     --o:monitors.monitor[0]=ws://collabora-cool-controller.collabora.svc.cluster.local:9000/controller/ws
  >     --o:monitors.monitor[0][@retryInterval]=5
  >     --o:logging.level=debug
  >
  >   username: admin
  >   password: admin123
  >
  >   env:
  >     - name: POD_NAME
  >       valueFrom:
  >         fieldRef:
  >           fieldPath: metadata.name
  > ```
  >
  > **Key configuration points:**
  >
  > - `indirection_endpoint.url`: Must remain as the external domain since clients use this endpoint
  > - `monitors.monitor[0]`: Uses internal DNS for cluster-only communication
  > - `retryInterval`: Controls reconnection attempts if the controller becomes unavailable
4. Configure COOL Controller
  > Update the controller to use the internal Ingress service while preserving the external hostname for proper routing:
  >
  > ```
  > controller:
  >   watchNamespace: "collabora"
  >   resourceName: "collabora-online"
  >   ingressUrl: "https://traefik.traefik.svc.cluster.local:443"
  >   ingressHostname: "test.collabora.online"
  >   enableHashmapParallelization: true
  >   skipTLSVerification: true
  >
  >   documentMigrator:
  >     enabled: true
  >     coolMemoryUtilization: "50"
  >     coolMemoryLimit: "2000Mi"
  >
  >   leaderElection:
  >     enabled: true
  > ```
  >
  > **Configuration explanation:**
  >
  > - `ingressUrl`: Internal cluster DNS address bypasses external load balancers
  > - `ingressHostname`: Original external domain added to the `Host` header for proper Ingress routing
  > - `skipTLSVerification`: Often required for internal communication with self-signed certificates

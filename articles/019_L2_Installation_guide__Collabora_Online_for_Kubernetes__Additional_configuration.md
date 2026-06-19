---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Kubernetes.xhtml#additional-configuration"
source_file: "docs/installation/Kubernetes.xhtml"
source_anchor: "additional-configuration"
title: "Additional configuration"
canonical_title: "Installation guide / Collabora Online for Kubernetes / Additional configuration"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online for Kubernetes / Additional configuration"
---
### Kubernetes cluster monitoring

1. Install [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) [https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack], a collection of [Grafana](https://grafana.com/) [https://grafana.com/] dashboards, and [Prometheus rules](https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/) [https://prometheus.io/docs/prometheus/latest/configuration/recording_rules/] combined with documentation and scripts to provide easy to operate end-to-end Kubernetes cluster monitoring with [Prometheus](https://prometheus.io/) [https://prometheus.io/] using the [Prometheus Operator](https://prometheus-operator.dev/) [https://prometheus-operator.dev/].
2. Enable prometheus service monitor, rules and grafana in your `my_values.yaml`:
  ```
  prometheus:
     servicemonitor:
        enabled: true
        labels:
           release: "kube-prometheus-stack"
     rules:
        enabled: true # will deploy alert rules
        additionalLabels:
           release: "kube-prometheus-stack"
  grafana:
     dashboards:
        enabled: true # will deploy default dashboards
  ```
  Note
  Use `kube-prometheus-stack` as release name when installing [kube-prometheus-stack](https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack) [https://artifacthub.io/packages/helm/prometheus-community/kube-prometheus-stack] helm chart because we have passed `release=kube-prometheus-stack` label in our `my_values.yaml`. For Grafana Dashboards you may need to enable scan in correct namespaces (or ALL), enabled by `sidecar.dashboards.searchNamespace` in [Helmchart of grafana](https://artifacthub.io/packages/helm/grafana/grafana) [https://artifacthub.io/packages/helm/grafana/grafana] (which is part of PrometheusOperator, so `grafana.sidecar.dashboards.searchNamespace`)

### Dynamic/Remote configuration in kubernetes

For big setups, you may not want to restart every pod to modify WOPI hosts. Therefore it is possible to setup an additional webserver to serve a ConfigMap for using [Remote/Dynamic Configuration](https://sdk.collaboraonline.com/docs/installation/Configuration.html#remote-dynamic-configuration) [https://sdk.collaboraonline.com/docs/installation/Configuration.html#remote-dynamic-configuration]

> ```
> collabora:
>    env:
>       - name: remoteconfigurl
>         value: https://dynconfig.public.example.com/config/config.json
>
>  dynamicConfig:
>    enabled: true
>
>    ingress:
>       enabled: true
>       annotations:
>       "cert-manager.io/issuer": letsencrypt-zprod
>       hosts:
>       - host: "dynconfig.public.example.com"
>       tls:
>       - secretName: "collabora-online-dynconfig-tls"
>          hosts:
>             - "dynconfig.public.example.com"
>
>    configuration:
>       kind: "configuration"
>       storage:
>          wopi:
>          alias_groups:
>             groups:
>             - host: "https://domain1\\.xyz\\.abc\\.com/"
>                allow: true
>             - host: "https://domain2\\.pqr\\.def\\.com/"
>                allow: true
>                aliases:
>                   - "https://domain2\\.ghi\\.leno\\.de/"
> ```
>
> Note
>
> In current state of COOL `remoteconfigurl` for [Remote/Dynamic Configuration](https://sdk.collaboraonline.com/docs/installation/Configuration.html#remote-dynamic-configuration) [https://sdk.collaboraonline.com/docs/installation/Configuration.html#remote-dynamic-configuration] should be HTTPS.

### Installing Custom Fonts

There are two primary methods for adding custom fonts to your Collabora Online deployment without building a custom Docker image.

1. **Remote Font Configuration**: This method involves pointing Collabora Online to a remote server that hosts your font files. See the details in [Remote configuration](031_L1_Installation_guide__Configuration.md) chapter.
2. **PersistentVolumeClaim (PVC)**: This method uses a Kubernetes PersistentVolume to store the fonts, which are then mounted directly into the Collabora Online pods. More details in [PersistentVolume(PVC)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) [https://kubernetes.io/docs/concepts/storage/persistent-volumes/]

This section focuses on the second method: using a PersistentVolumeClaim.

#### Method: Using a PersistentVolumeClaim (PVC)

This approach is ideal for managing fonts directly within your Kubernetes cluster. The process involves enabling a feature flag in your deployment configuration, which orchestrates the creation of a PVC and a temporary “font-loader” pod. You will copy your font files to this temporary pod, which saves them to the persistent volume. Finally, a restart of the main Collabora Online deployment will make the new fonts available.

#### Prerequisites

Before you begin, ensure you have the following:

- `kubectl` command-line tool configured to access your cluster.
- Your custom font files (e.g., `.ttf`, `.otf`) available on your local machine.

#### Step-by-Step Guide

**Step 1: Enable Custom Fonts in Your Deployment**

You need to enable the custom fonts feature in your Collabora Online configuration. If you are using a Helm chart, this is typically done in your `values.yaml` file.

Set `deployment.customFonts.enabled` to `true` within your deployment block.

Example `my_values.yaml` snippet:

Example values.yaml snippet

```
deployment:
  customFonts:
    enabled: true
    # pvc:
    #   size: 1Gi # Optional: Adjust storage size if needed
    #   storageClassName: "" # Optional: Specify a storage class
```

Apply the configuration change to your cluster. For Helm, you would run:

```
helm upgrade --install <release-name> <chart-name> -f my_values.yaml -n <namespace>
```

Applying this change will trigger the creation of a new PVC and a temporary pod named `<deployment-name>-custom-fonts`. This pod’s purpose is to provide a temporary mount point for you to upload your fonts to the PVC.

**Step 2: Copy Font Files to the PVC**

Once the temporary pod is in the `Running` state, use the `kubectl cp` command to copy your local font files into it. The pod mounts the PVC at the `/mnt/fonts` directory.

```
kubectl cp <path-to-local-fonts-directory> <namespace>/<deployment-name>-custom-fonts:/mnt/fonts
```

Replace the placeholders:

- `<path-to-local-fonts-directory>`: The path to the folder on your local machine containing your font files (e.g. path/to/custom_fonts/directory).
- `<namespace>`: The Kubernetes namespace where Collabora Online is deployed (e.g. collabora).
- `<deployment-name>`: The name of your Collabora Online deployment (e.g. collabora-online).

**Step 3: Restart the Collabora Online Deployment**

To make the main Collabora Online pods recognize the new fonts, you must perform a rolling restart of the deployment. This forces the pods to re-mount the PVC and rebuild their font cache.

```
kubectl -n <namespace> rollout restart deployment/<deployment-name>
```

**Step 4: Cleanup and Verification**

The temporary `<deployment-name>-custom-fonts` pod is designed for single use and will automatically terminate itself one hour after creation. You can also delete it manually if you wish.

To verify that the fonts were installed correctly:

1. Open a document in your Collabora Online instance.
2. Click the font selection dropdown menu in the toolbar.
3. Your newly added fonts should now appear in the list.

Note

The font cache is built when the Collabora Online pods start. If you add more fonts later, you will need to repeat step 3.

### Kubernetes Security Context for Restricted Environments

In Kubernetes environments with strict Pod Security Standards, CODE/COOL requires specific security configurations to maintain proper jail creation and isolation while adhering to security policies.

#### Running with Minimal Capabilities

CODE/COOL needs specific Linux capabilities for proper functionality. Configure the `securityContext` with only essential capabilities:

```
securityContext:
  allowPrivilegeEscalation: true
  privileged: false
  readOnlyRootFilesystem: false
  runAsNonRoot: true
  seccompProfile:
    type: "RuntimeDefault"
  capabilities:
    add:
      - "SYS_CHROOT"
      - "SYS_ADMIN"
```

Note

`allowPrivilegeEscalation` can’t be `false` with `SYS_ADMIN` capability.

#### Custom Seccomp Profile for Maximum Restriction

For environments requiring zero capabilities, use a custom seccomp profile to allow only necessary syscalls.

Enable `installCOOLSeccompProfile`, this creates DaemonSet which downloads [cool-seccomp-profile.json](https://github.com/CollaboraOnline/online/blob/main/docker/cool-seccomp-profile.json) [https://github.com/CollaboraOnline/online/blob/main/docker/cool-seccomp-profile.json] and installs seccomp profile to nodes’ `/var/lib/kubelet/seccomp` directory.

```
installCOOLSeccompProfile: true
```

Update `securityContext` to use `cool-seccomp-profile.json`

```
securityContext:
  privileged: false
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  seccompProfile:
    type: "Localhost"
    localhostProfile: "cool-seccomp-profile.json"
  capabilities:
    drop: ["ALL"]
```

### OpenShift

OpenShift deployments need OpenShift-specific Ingress and Security Context Constraints (SCC) configuration on top of the generic Kubernetes flow above. The full step-by-step guide, including the three SCC options (Custom Seccomp Profile, Restricted SCC, Privileged SCC), lives on its own page: [Collabora Online on OpenShift](021_L1_Installation_guide__Collabora_Online_on_OpenShift.md).

### Useful commands to check what is happening

Where is this pods, are they ready?

```
kubectl -n collabora get pod
```

Example output:

```
NAME                                READY   STATUS    RESTARTS   AGE
collabora-online-5fb4869564-dnzmk   1/1     Running   0          28h
collabora-online-5fb4869564-fb4cf   1/1     Running   0          28h
collabora-online-5fb4869564-wbrv2   1/1     Running   0          28h
```

What is the outside host that multiple coolwsd servers actually answering?

```
kubectl get ingress -n collabora
```

Example output:

```
|-----------|------------------|--------------------------|------------------------|-------|
| NAMESPACE |       NAME       |           HOSTS          |         ADDRESS        | PORTS |
|-----------|------------------|--------------------------|------------------------|-------|
| collabora | collabora-online |chart-example.local       |                        |  80   |
|-----------|------------------|--------------------------|------------------------|-------|
```

To uninstall the helm chart:

```
helm uninstall collabora-online -n collabora
```

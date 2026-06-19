---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml#cluster-administrator-setup-one-time-per-cluster"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: "cluster-administrator-setup-one-time-per-cluster"
title: "Cluster administrator setup (one-time per cluster)"
canonical_title: "Installation guide / Collabora Online on OpenShift / Cluster administrator setup (one-time per cluster)"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online on OpenShift / Cluster administrator setup (one-time per cluster)"
---
The steps in this section create cluster-scoped objects (`ClusterRoleBinding`, `SecurityContextConstraints`) and must be run by a user with cluster-admin. They are typically done once per cluster, not once per COOL deployment.

### Step CA1: Log in as cluster-admin

```
# CRC / OpenShift Local
oc login -u kubeadmin https://api.crc.testing:6443

# Production cluster - use your cluster's admin credentials
oc login --server=https://api.<cluster>.example.com:6443
```

Verify:

```
oc whoami
oc auth can-i create clusterrolebindings
```

The second command must answer `yes`.

### Step CA2: Install HAProxy Kubernetes Ingress

Install the [HAProxy Kubernetes Ingress](https://artifacthub.io/packages/helm/haproxytech/kubernetes-ingress) [https://artifacthub.io/packages/helm/haproxytech/kubernetes-ingress] controller. This creates the `haproxy` `IngressClass` that the COOL `Ingress` will later select.

```
oc create namespace collabora
```

The upstream chart’s pod template is not admissible under any of OpenShift’s built-in SCCs: it hard-codes `runAsUser: 1000` (outside the per-project UID range), adds the `NET_BIND_SERVICE` capability, and sets `seccompProfile: RuntimeDefault`. `anyuid` covers UID but not the capability add or seccomp; `privileged` covers everything but grants full host access. Neither is appropriate for production. Apply a narrow custom SCC that grants exactly what the chart needs and nothing more:

haproxy-ingress-scc.yaml

```
apiVersion: security.openshift.io/v1
kind: SecurityContextConstraints
metadata:
  name: haproxy-ingress
  annotations:
    kubernetes.io/description: |
      Narrow SCC for the haproxytech/kubernetes-ingress chart. Grants
      UID 1000 (hardcoded by the chart), NET_BIND_SERVICE, and the
      runtime/default seccomp profile. No host networking, no host
      paths, no privilege escalation.
allowHostDirVolumePlugin: false
allowHostIPC: false
allowHostNetwork: false
allowHostPID: false
allowHostPorts: false
allowPrivilegeEscalation: false
allowPrivilegedContainer: false
allowedCapabilities:
  - NET_BIND_SERVICE
defaultAddCapabilities: null
fsGroup:
  type: RunAsAny
groups: []
priority: 10
readOnlyRootFilesystem: false
requiredDropCapabilities:
  - ALL
runAsUser:
  type: MustRunAs
  uid: 1000
seLinuxContext:
  type: MustRunAs
seccompProfiles:
  - runtime/default
supplementalGroups:
  type: RunAsAny
users: []
volumes:
  - configMap
  - downwardAPI
  - emptyDir
  - projected
  - secret
```

Apply the SCC and bind it to the chart’s ServiceAccount. The SA name matches the release name, so the binding can be created before the chart is installed:

```
oc apply -f haproxy-ingress-scc.yaml
oc adm policy add-scc-to-user haproxy-ingress \
  -z haproxy-kubernetes-ingress -n collabora
```

Then install the chart:

```
helm repo add haproxytech https://haproxytech.github.io/helm-charts
helm repo update

helm install haproxy-kubernetes-ingress haproxytech/kubernetes-ingress \
  --namespace collabora
```

Confirm the controller pod becomes `Running` and the `haproxy` `IngressClass` is registered:

```
oc -n collabora get pod
oc get ingressclass
```

Note

The OpenShift Router cannot be used as the ingress for COOL. Source-IP hashing (the closest built-in algorithm) collapses to a single backend behind a WOPI host or proxy, and cookie-based affinity does not survive across the per-document WOPI calls that need consistent routing.

### Step CA3: Apply the chosen SCC option

See Security Context Constraints (SCCs) below for the comparison table and details of each option. Apply the admin commands for the option you’ve chosen:

- **Option 1 (Custom Seccomp Profile)** - admin steps required: create the custom SCC and bind it to the app team’s service accounts.
- **Option 2 (Restricted SCC)** - no admin SCC work required; skip to step CA4.
- **Option 3 (Privileged SCC)** - admin steps required: bind the built-in `privileged` SCC to the app team’s service account.

### Step CA4: Grant the app team admin on the namespace

Give the app team enough access to install the chart and manage the deployment, but no cluster-scoped rights:

```
oc adm policy add-role-to-user admin <developer-username> -n collabora
```

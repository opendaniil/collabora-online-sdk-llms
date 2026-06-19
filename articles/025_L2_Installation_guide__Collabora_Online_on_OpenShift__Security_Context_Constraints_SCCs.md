---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml#security-context-constraints-sccs"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: "security-context-constraints-sccs"
title: "Security Context Constraints (SCCs)"
canonical_title: "Installation guide / Collabora Online on OpenShift / Security Context Constraints (SCCs)"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online on OpenShift / Security Context Constraints (SCCs)"
---
OpenShift enforces strict security policies through Security Context Constraints (SCCs). Collabora Online requires specific configurations based on your environment’s security requirements and access level.

### Security Configuration Options

The following table helps you choose the appropriate security configuration:

| Security Configuration | Cluster-admin needed | Security Level | Use Case |
| --- | --- | --- | --- |
| Custom Seccomp Profile | Required | Maximum | Production with the minimum syscalls Collabora Online requires |
| Restricted SCC | Not Required | Medium | Limited admin access environments |
| Privileged SCC | Required | Minimal | Less secure |

### Option 1: Custom Seccomp Profile

**Best for**: Production environments requiring maximum security with fine-grained syscall control with syscalls required for Collabora Online allowed.

Custom SCC removes seccomp restrictions while maintaining all other security controls. Document isolation is handled through a custom seccomp profile that allows only necessary syscalls. Each document gets isolated with `Linux usernamespaces` and `chroot`, while benefiting from the optimization allowed by shared bind mounts.

#### Cluster administrator steps

1. Create the custom SCC:
   collabora-restricted-v2.yaml
  ```
  apiVersion: security.openshift.io/v1
  kind: SecurityContextConstraints
  metadata:
    annotations:
      kubernetes.io/description: |
        collabora-restricted-v2 maintains restricted-v2 security posture
        while enabling custom seccomp profiles for Collabora Online.
        No capabilities are granted. Custom seccomp profile allows necessary syscalls.
    name: collabora-restricted-v2
  allowHostDirVolumePlugin: false
  allowHostIPC: false
  allowHostNetwork: false
  allowHostPID: false
  allowHostPorts: false
  allowPrivilegeEscalation: false
  allowPrivilegedContainer: false
  allowedCapabilities: []
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
    uid: 1001
  seLinuxContext:
    type: MustRunAs
  seccompProfiles:
    - runtime/default
    - localhost/cool-seccomp-profile.json
  supplementalGroups:
    type: RunAsAny
  userNamespaceLevel: AllowHostLevel
  users: []
  volumes:
    - configMap
    - csi
    - downwardAPI
    - emptyDir
    - ephemeral
    - persistentVolumeClaim
    - projected
    - secret
  ```
  Apply it:
  ```
  oc apply -f collabora-restricted-v2.yaml
  ```
2. Bind the SCC to the service accounts the chart will create. The binding is by name, so this can be run before the chart is installed:
  ```
  # Bind custom SCC to application service account
  oc adm policy add-scc-to-user collabora-restricted-v2 -z collabora-online -n collabora
  # Bind privileged SCC to DaemonSet service account for seccomp profile installation
  oc adm policy add-scc-to-user privileged -z collabora-online-daemonset -n collabora
  ```

#### App team values block

Merge this block into the `cool_values.yaml` from step D1:

values.yaml (excerpt)

```
 serviceAccount:
   create: true

 daemonSetServiceAccount:
   create: true

 installCOOLSeccompProfile: true

 securityContext:
   allowPrivilegeEscalation: false
   privileged: false
   readOnlyRootFilesystem: false
   runAsNonRoot: true
   seccompProfile:
     type: "Localhost"
     localhostProfile: "cool-seccomp-profile.json"
   capabilities:
     drop: ["ALL"]
```

### Option 2: Restricted SCC Approach

**Best for**: Environments without admin access or where SCC modification is not permitted.

Uses the restricted SCC with emptyDir volumes and disabled capabilities. **No cluster-admin work is required** beyond namespace creation - the app team can deploy this option entirely on their own using OpenShift’s built-in `restricted-v2` SCC.

#### App team values block

Merge this block into the `cool_values.yaml` from step D1:

values.yaml (excerpt)

```
 securityContext:
   allowPrivilegeEscalation: false
   privileged: false
   readOnlyRootFilesystem: false
   runAsNonRoot: true
   seccompProfile:
     type: "RuntimeDefault"
   capabilities:
     drop: ["ALL"]

 collabora:
   extra_params: >
     --o:ssl.enable=false
     --o:security.capabilities=false
     --o:child_root_path=/tmp/coolwsd-child-roots
     --o:cache_files.path=/tmp/coolwsd-cache

 extraVolumeMounts:
   - name: coolwsd-child-roots
     mountPath: /tmp/coolwsd-child-roots
   - name: coolwsd-cache
     mountPath: /tmp/coolwsd-cache

 extraVolumes:
   - name: coolwsd-child-roots
     emptyDir: {}
   - name: coolwsd-cache
     emptyDir: {}
```

Warning

This approach disables Collabora’s document isolation security mechanisms. Without Linux user namespaces or chroot jails, documents from different users or sessions are not isolated at the process level. It is also slightly less memory-efficient due to optimizations not being available.

### Option 3: Privileged SCC

**Best for**: Environments where immediate functionality is required without security restrictions.

#### Cluster administrator step

```
oc adm policy add-scc-to-user privileged -z default -n collabora
```

#### App team values block

Merge this block into the `cool_values.yaml` from step D1:

values.yaml (excerpt)

```
 serviceAccount:
   create: true
```

Warning

This approach provides full host access and should be carefully evaluated against your security requirements before implementation.

Select the option that best aligns with your security requirements, administrative access level, and operational constraints.

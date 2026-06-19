---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/OpenShift.xhtml#verifying-the-deployment"
source_file: "docs/installation/OpenShift.xhtml"
source_anchor: "verifying-the-deployment"
title: "Verifying the deployment"
canonical_title: "Installation guide / Collabora Online on OpenShift / Verifying the deployment"
toc_level: "2"
breadcrumbs: "Installation guide / Collabora Online on OpenShift / Verifying the deployment"
---
These checks can be run as the app team’s developer account.

Check that the COOL pods are running:

```
oc -n collabora get pod
```

Example output:

```
NAME                                READY   STATUS    RESTARTS   AGE
collabora-online-5fb4869564-dnzmk   1/1     Running   0          28h
collabora-online-5fb4869564-fb4cf   1/1     Running   0          28h
collabora-online-5fb4869564-wbrv2   1/1     Running   0          28h
```

Check the Ingress is bound to the external hostname:

```
oc -n collabora get ingress
```

Hit the WOPI discovery endpoint to confirm COOL is serving:

```
curl 'https://test.collabora.online/'
```

It should return a similar output as below:

```
HTTP/1.1 200 OK
last-modified: Tue, 18 May 2021 10:46:29
user-agent: COOLWSD WOPI Agent 6.4.8
content-length: 2
content-type: text/plain
```

Finally, verify that URL-parameter consistent hashing actually pins requests to the same pod. Run this against the external endpoint - any path works, the hash key is the query parameter:

```
for i in $(seq 1 10); do
  curl -sk "https://test.collabora.online/hosting/capabilities?WOPISrc=test1" \
    | grep -oE '"serverId":[^,}]+'
done | sort | uniq -c
```

- **Pass**: exactly one line - the same `serverId` for all 10 requests with the same `WOPISrc`.
- **Fail**: multiple lines - requests are being round-robined and collaborative editing will be broken. Re-check that the Ingress’s `className` matches the IngressClass registered by HAproxy Kubernetes Ingress, and that the `haproxy.org/backend-config-snippet` annotation is on the Ingress object (`oc -n collabora describe ingress`).

For the COOL Controller umbrella, use `RouteToken` instead of `WOPISrc` in the curl URL.

To uninstall the chart:

```
helm uninstall collabora-online -n collabora
```

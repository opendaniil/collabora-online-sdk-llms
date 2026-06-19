---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/CODE_Docker_image.xhtml#container-security-and-capability-management"
source_file: "docs/installation/CODE_Docker_image.xhtml"
source_anchor: "container-security-and-capability-management"
title: "Container Security and Capability Management"
canonical_title: "Installation guide / CODE Docker image / Container Security and Capability Management"
toc_level: "2"
breadcrumbs: "Installation guide / CODE Docker image / Container Security and Capability Management"
---
For enhanced security, you may want to run the Collabora Online Docker container either with minimal capabilities or custom seccomp profiles while ensuring the container can still perform necessary isolation operations.

### Running with Minimal Capabilities

CODE requires specific Linux capabilities for proper jail creation and isolation. The essential capabilities needed are:

- `SYS_CHROOT` - Required for chroot operations during jail setup
- `SYS_ADMIN` - Needed for unshare syscalls and namespace creation

**Arch Linux and Minimal Distributions:**

```
# Drop all capabilities except required ones
docker run -t -d -p 127.0.0.1:9980:9980 \
  --user 1001:1001 \
  --cap-drop=ALL \
  --cap-add=SYS_CHROOT \
  --cap-add=SYS_ADMIN \
  --name collabora \
  collabora/code
```

**Debian and Debian-based Distributions (Ubuntu, Linux Mint, etc.):**

Debian enforces stricter AppArmor profiles by default, requiring additional capabilities for file ownership operations during jail creation:

- `FOWNER` - enables bypassing file ownership checks for permission operations during jail setup
- `CHOWN` - enables changing file and directory ownership to arbitrary users/groups during the jail creation process

```
docker run -t -d -p 127.0.0.1:9980:9980 \
  --user 1001:1001 \
  --cap-drop=ALL \
  --cap-add=SYS_CHROOT \
  --cap-add=SYS_ADMIN \
  --cap-add=FOWNER \
  --cap-add=CHOWN \
  --name collabora \
  collabora/code
```

### Custom Seccomp profile

If want to absolutely drop all the capabilities. You can use custom seccomp profile to allow syscalls that are required by Collabora Online for document isolation. You can pass the [cool-seccomp-profile.json](https://github.com/CollaboraOnline/online/blob/main/docker/cool-seccomp-profile.json) [https://github.com/CollaboraOnline/online/blob/main/docker/cool-seccomp-profile.json]

```
# Run with custom seccomp profile
docker run -t -d -p 127.0.0.1:9980:9980 \
  --security-opt seccomp=/path/to/cool-seccomp-profile.json \
  --user 1001:1001 \
  --name collabora \
  collabora/code
```

### Troubleshooting

After starting of the container, try:

```
curl -k https://localhost:9980
```

You should get the OK string, if everything is in order. Otherwise, you can check the log with:

```
docker logs collabora
```

### Misc

If you need customizations, for example additional fonts, you can build the docker image yourself. Please find everything in Collabora Online source code repository on [GitHub](https://github.com/CollaboraOnline/online/tree/main/docker) [https://github.com/CollaboraOnline/online/tree/main/docker].

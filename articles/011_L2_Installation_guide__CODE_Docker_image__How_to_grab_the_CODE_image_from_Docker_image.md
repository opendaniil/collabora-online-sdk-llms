---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/CODE_Docker_image.xhtml#how-to-grab-the-code-image-from-docker-image"
source_file: "docs/installation/CODE_Docker_image.xhtml"
source_anchor: "how-to-grab-the-code-image-from-docker-image"
title: "How to grab the CODE image from Docker image"
canonical_title: "Installation guide / CODE Docker image / How to grab the CODE image from Docker image"
toc_level: "2"
breadcrumbs: "Installation guide / CODE Docker image / How to grab the CODE image from Docker image"
---
Collabora Online Development Edition (CODE) is available as a Docker image from [Docker Hub](https://hub.docker.com/r/collabora/code/) [https://hub.docker.com/r/collabora/code/]. Currently, the supported platforms are `x86-64`, `ppc64le` and `arm64`, and the image was mostly tested on Linux. If you are not familiar with Docker concepts and basic commands, read the [Docker Get Started](https://docs.docker.com/get-started/) [https://docs.docker.com/get-started/] document first.

Grab the Docker image

```
 docker pull collabora/code
```

Start a new container:

```
 docker run -t -d -p 127.0.0.1:9980:9980 collabora/code
```

This is the minimal command line to start a new container. There are a few optional and recommended command line options:

- `--name collabora` gives a specific name to the container instead of a random one.
- `--restart always` restarts the container after a crash that may occur.
- `--privileged` starts the container with rights required for faster jail creation via bind mount.
- `-p '[::1]:9980:9980'` adds a port redirection for IPv6. If your host has IPv6 configured, you may want to add this if you get “Connection Refused” errors.
- with `-e` you can pass environment variables to the container, see below.

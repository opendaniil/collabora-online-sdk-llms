---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Docker_image.xhtml#pre-made-docker-images"
source_file: "docs/installation/Docker_image.xhtml"
source_anchor: "pre-made-docker-images"
title: "Pre-made Docker images"
canonical_title: "Installation guide / Docker images / Pre-made Docker images"
toc_level: "2"
breadcrumbs: "Installation guide / Docker images / Pre-made Docker images"
---
The [CODE Docker image](https://hub.docker.com/r/collabora/code/) [https://hub.docker.com/r/collabora/code/] can be installed to any `x86-64`, `ppc64le` or `arm64` host, and it is fully configurable. For more information about setup and configuration for deployment, please read the [CODE Docker page](010_L1_Installation_guide__CODE_Docker_image.md). If you want to try it out quickly, you can set up CODE docker image with file sharing integration in less than 5 minutes in a very basic way, following these instructions: [quick tryout with ownCloud](https://www.collaboraonline.com/quick-tryout-owncloud-docker/) [https://www.collaboraonline.com/quick-tryout-owncloud-docker/] or [quick tryout with Nextcloud](https://www.collaboraonline.com/quick-tryout-nextcloud-docker/) [https://www.collaboraonline.com/quick-tryout-nextcloud-docker/].

For customers Collabora provide pre-built Collabora Online images for the x86-64 platform.

- `registry.gitlab.collabora.com/collabora-online/docker` is the publicly available license key enabled version. License keys can be purchased via partners or from Collabora directly.
  The key can be passed to the `docker run` command as extra parameter: `-e "extra_params=--o:support_key=$(cat /path/to/collabora.key)"`
- `registry.gitlab.collabora.com/productivity/collabora-online` is the full version of Collabora online for customers. If you are a customer, and need this image, please contact support.

Docker images are tagged with the version number, however, usually it is the best to use the `:latest`.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Proxy_settings.xhtml"
source_file: "docs/installation/Proxy_settings.xhtml"
source_anchor: ""
title: "Proxy settings"
canonical_title: "Installation guide / Proxy settings"
toc_level: "1"
breadcrumbs: "Installation guide / Proxy settings"
---
Server part of Collabora Online (coolwsd daemon) is listening on port 9980 by default, and clients should be able to communicate with it through port `9980`. Sometimes it is not possible, for example a corporate firewall can allow only ports of well known services, such as port 80 (HTTP) and port 443 (HTTPS). The coolwsd daemon is configurable. It can use other ports than `9980`. Port can be set by the command line option `--port`. However we cannot use for example port `443`, when a web server is running on the same server, which is already bound to port `443`. Reverse proxy setup is also required if you would like to setup load balancing.

Attention

In some cases CODE can be packaged as part of integrator’s image and so, it might have different set of instructions. Thus, the easiest way to configure reverse proxy might be better documented in the integrator’s documentation.

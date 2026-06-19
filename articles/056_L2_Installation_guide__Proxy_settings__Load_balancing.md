---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Proxy_settings.xhtml#load-balancing"
source_file: "docs/installation/Proxy_settings.xhtml"
source_anchor: "load-balancing"
title: "Load balancing"
canonical_title: "Installation guide / Proxy settings / Load balancing"
toc_level: "2"
breadcrumbs: "Installation guide / Proxy settings / Load balancing"
---
For collaborative editing to function correctly, it is vital to ensure that all users editing the same document end up being served by the same Collabora Office instance. Using the WOPI protocol, the https URL includes a unique identifier (WOPISrc) for use with this document. Thus load balancing can be done by using WOPISrc – ensuring that all URLs that contain the same WOPISrc are sent to the same Collabora Office instance.

Note: for optimal performance all load balanced nodes must run the same version of Collabora Online. Currently Javascript, CSS and HTML that is served contains a unique version specific hash to enable browser caching while ensuring consistent upgrades. This version is provided in URLs provided from discovery.xml. When doing an incremental upgrade of a cluster an upgraded node will still provide new Javascript for an old version hash but will avoid sending ETag and CacheControl headers so that the files will be re-loaded when next fetched. This ensures that many minor upgrades can be done incrementally while an HA cluster continues running.

### Example with HAProxy

In this example we will do load balancing between two Collabora Online server instances, which are running in docker containers. Load balancing is based on `WOPISrc` URL parameter.

The browser reaches the proxy with HTTPS protocol. The proxy terminates the HTTPS connection and passes traffic to backends via HTTP. Therefore in Collabora Online’s config file, in `/etc/coolwsd/coolwsd.xml` , or in the command line which starts `coolwsd` daemon, SSL should be disabled, and SSL termination should be enabled.

add the following blocks to /etc/haproxy/haproxy.cfg

```
 1frontend coolwsd
 2  bind *:443 ssl crt /path/to/your/certificate_and_key.pem
 3  mode http
 4  default_backend coolwsd
 5backend coolwsd
 6  timeout tunnel 3600s
 7  mode http
 8  balance url_param WOPISrc check_post
 9  hash-type consistent
10  server coolwsd01 127.0.0.1:9993
11  server coolwsd02 127.0.0.1:9994
```

Start Docker containers as described above, with `-p 127.0.0.1:9993:9980` and `-p 127.0.0.1:9994:9980`.

### Example with Nginx

Just like in the previous section (`HAProxy`), the Nginx load balancer also utilizes the `WOPISrc` URL parameter. In this example SSL settings are managed by `Certbot` (see [https://letsencrypt.org/](https://letsencrypt.org/)). The load balancer server listens on standard HTTPS port 443, and HTTP port 80 is redirected to HTTPS port 443. The coolwsd servers are reached through port 9980 directly (private network). The address for the outside world (for WOPI hosts) is coolwsd.public.example.com.

```
 1upstream coolwsd {
 2  zone coolwsd 64k;
 3  hash $arg_WOPISrc;
 4
 5  server coolwsd1.private:9980;
 6  server coolwsd2.private:9980;
 7}
 8
 9server {
10  listen 80 default_server;
11  listen 443 ssl; # managed by Certbot
12  ssl_certificate /etc/letsencrypt/live/1b255632-ce4b-4581-9e80-16f701c27034.pub.cloud.scaleway.com/fullchain.pem; # managed by Certbot
13  ssl_certificate_key /etc/letsencrypt/live/1b255632-ce4b-4581-9e80-16f701c27034.pub.cloud.scaleway.com/privkey.pem; # managed by Certbot
14  include /etc/letsencrypt/options-ssl-nginx.conf; # managed by Certbot
15
16  if ($scheme != "https") {
17    return 301 https://$host$request_uri;
18  } # managed by Certbot
19
20  server_name coolwsd.public.example.com;
21
22  location / {
23    proxy_pass                 http://coolwsd;
24    proxy_set_header           Host $host;
25    proxy_http_version         1.1;
26    proxy_set_header           Upgrade $http_upgrade;
27    proxy_set_header           Connection "upgrade";
28    client_max_body_size       0;
29  }
30}
```

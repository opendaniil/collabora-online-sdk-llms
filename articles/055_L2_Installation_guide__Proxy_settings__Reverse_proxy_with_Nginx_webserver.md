---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Proxy_settings.xhtml#reverse-proxy-with-nginx-webserver"
source_file: "docs/installation/Proxy_settings.xhtml"
source_anchor: "reverse-proxy-with-nginx-webserver"
title: "Reverse proxy with Nginx webserver"
canonical_title: "Installation guide / Proxy settings / Reverse proxy with Nginx webserver"
toc_level: "2"
breadcrumbs: "Installation guide / Proxy settings / Reverse proxy with Nginx webserver"
---
### Reverse proxy settings in Nginx config (SSL)

Add a new `server` block to your Nginx config for `collaboraonline.example.com`.

In `coolwsd.xml` the corresponding setting is `ssl.enable=true`.

```
 1server {
 2 listen       443 ssl;
 3 server_name  collaboraonline.example.com;
 4
 5
 6 ssl_certificate /path/to/certificate;
 7 ssl_certificate_key /path/to/key;
 8
 9
10 # static files
11 location ^~ /browser {
12   proxy_pass https://127.0.0.1:9980;
13   proxy_set_header Host $host;
14 }
15
16
17 # WOPI discovery URL
18 location ^~ /hosting/discovery {
19   proxy_pass https://127.0.0.1:9980;
20   proxy_set_header Host $host;
21 }
22
23
24 # Capabilities
25 location ^~ /hosting/capabilities {
26   proxy_pass https://127.0.0.1:9980;
27   proxy_set_header Host $host;
28 }
29
30
31 # main websocket, download, presentation (legacy svg) and image upload
32 location ^~ /cool/ {
33   proxy_pass https://127.0.0.1:9980;
34   proxy_http_version 1.1;
35   proxy_set_header Upgrade $http_upgrade;
36   proxy_set_header Connection "Upgrade";
37   proxy_set_header Host $host;
38   proxy_read_timeout 36000s;
39 }
40}
```

### Reverse proxy settings in Nginx config (SSL termination)

Add a new `server` block to your Nginx config for `collaboraonline.example.com`. Basically the configuration is the same as above, but in this case we have HTTP-only connection between the proxy and the Collabora Online server.

In `coolwsd.xml` the corresponding setting is `ssl.enable=false` and `ssl.termination=true`.

```
 1server {
 2 listen       443 ssl;
 3 server_name  collaboraonline.example.com;
 4
 5
 6 ssl_certificate /path/to/certificate;
 7 ssl_certificate_key /path/to/key;
 8
 9
10 # static files
11 location ^~ /browser {
12   proxy_pass http://127.0.0.1:9980;
13   proxy_set_header Host $host;
14 }
15
16
17 # WOPI discovery URL
18 location ^~ /hosting/discovery {
19   proxy_pass http://127.0.0.1:9980;
20   proxy_set_header Host $host;
21 }
22
23
24 # Capabilities
25 location ^~ /hosting/capabilities {
26   proxy_pass http://127.0.0.1:9980;
27   proxy_set_header Host $host;
28 }
29
30
31 # main websocket, download, presentation (legacy svg) and image upload
32 location ^~ /cool/ {
33   proxy_pass http://127.0.0.1:9980;
34   proxy_http_version 1.1;
35   proxy_set_header Upgrade $http_upgrade;
36   proxy_set_header Connection "Upgrade";
37   proxy_set_header Host $host;
38   proxy_read_timeout 36000s;
39 }
40}
```

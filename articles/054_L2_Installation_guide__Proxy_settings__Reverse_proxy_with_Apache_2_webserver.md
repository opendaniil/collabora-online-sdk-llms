---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Proxy_settings.xhtml#reverse-proxy-with-apache-2-webserver"
source_file: "docs/installation/Proxy_settings.xhtml"
source_anchor: "reverse-proxy-with-apache-2-webserver"
title: "Reverse proxy with Apache 2 webserver"
canonical_title: "Installation guide / Proxy settings / Reverse proxy with Apache 2 webserver"
toc_level: "2"
breadcrumbs: "Installation guide / Proxy settings / Reverse proxy with Apache 2 webserver"
---
We assume that coolwsd and Apache2 are running on the same server: `collaboraonline.example.com`. For this to work, you have to follow the steps below:

- Set the server name in Collabora Online configuration
- Enable the required Apache2 modules
- Add reverse proxy settings to Apache2 configuration file

### Configure Collabora Online

Collabora Online’s configuration file is `/etc/coolwsd/coolwsd.xml`.

The proxy redirects incoming requests to `127.0.0.1`, but replies from coolwsd server must contain the original host name, otherwise the connection will fail. The service can usually figure out the external host name, except in more complex cases. In that case look for the setting `server_name` (empty by default), and enter the host name here, for example `collaboraonline.example.com`.

### Required Apache2 modules

Apache2 web server is modular. We need to enable the required modules for this reverse proxy setup. We can use the `a2enmod` command to enable modules. If a module has been enabled already, nothing happens.

- Enable proxy in general: `a2enmod proxy`
- Enable proxy for HTTP protocol: `a2enmod proxy_http`
- Enable SSL support: `a2enmod proxy_connect`
- Enable proxy of websockets: `a2enmod proxy_wstunnel`

On CentOS / RHEL there is no `a2enmod` available. Enabling the modules has to be done by adjusting a config file and adding the LoadModule manually. See [server-world.info on CentOS](https://www.server-world.info/en/note?os=CentOS_7&p=httpd2&f=5) [https://www.server-world.info/en/note?os=CentOS_7&p=httpd2&f=5].

### Reverse proxy settings in Apache2 config (SSL)

These lines should be inserted into `<VirtualHost>` definition of the site.

In `coolwsd.xml` the corresponding setting is `ssl.enable=true`.

```
 1 ########################################
 2
 3 # Reverse proxy for Collabora Online   #
 4
 5 ########################################
 6
 7
 8 AllowEncodedSlashes NoDecode
 9 SSLProxyEngine On
10 ProxyPreserveHost On
11
12
13 # cert is issued for collaboraonline.example.com and we proxy to localhost
14 SSLProxyVerify None
15 SSLProxyCheckPeerCN Off
16 SSLProxyCheckPeerName Off
17
18
19 # static html, js, images, etc. served from coolwsd
20 # browser is the client part of Collabora Online
21 ProxyPass           /browser https://127.0.0.1:9980/browser retry=0
22 ProxyPassReverse    /browser https://127.0.0.1:9980/browser
23
24
25 # WOPI discovery URL
26 ProxyPass           /hosting/discovery https://127.0.0.1:9980/hosting/discovery retry=0
27 ProxyPassReverse    /hosting/discovery https://127.0.0.1:9980/hosting/discovery
28
29
30 # Capabilities
31 ProxyPass           /hosting/capabilities https://127.0.0.1:9980/hosting/capabilities retry=0
32 ProxyPassReverse    /hosting/capabilities https://127.0.0.1:9980/hosting/capabilities
33
34 # Main websocket
35 ProxyPassMatch      "/cool/(.*)/ws$"      wss://127.0.0.1:9980/cool/$1/ws nocanon
36
37
38 # Admin Console websocket
39 ProxyPass           /cool/adminws wss://127.0.0.1:9980/cool/adminws
40
41
42 # Download as, presentation (legacy svg) and image upload operations
43 ProxyPass           /cool https://127.0.0.1:9980/cool
44 ProxyPassReverse    /cool https://127.0.0.1:9980/cool
```

### Reverse proxy settings in Apache2 config (SSL termination)

These lines should be inserted into `<VirtualHost>` definition of the site. Basically the configuration is the same as above, but in this case we have HTTP-only connection between the proxy and the Collabora Online server.

In `coolwsd.xml` the corresponding setting is `ssl.enable=false` and `ssl.termination=true`.

```
 1 ########################################
 2
 3 # Reverse proxy for Collabora Online   #
 4
 5 ########################################
 6
 7 AllowEncodedSlashes NoDecode
 8 ProxyPreserveHost On
 9
10 # static html, js, images, etc. served from coolwsd
11 # browser is the client part of Collabora Online
12 ProxyPass           /browser http://127.0.0.1:9980/browser retry=0
13 ProxyPassReverse    /browser http://127.0.0.1:9980/browser
14
15 # WOPI discovery URL
16 ProxyPass           /hosting/discovery http://127.0.0.1:9980/hosting/discovery retry=0
17 ProxyPassReverse    /hosting/discovery http://127.0.0.1:9980/hosting/discovery
18
19 # Capabilities
20 ProxyPass           /hosting/capabilities http://127.0.0.1:9980/hosting/capabilities retry=0
21 ProxyPassReverse    /hosting/capabilities http://127.0.0.1:9980/hosting/capabilities
22
23 # Main websocket
24 ProxyPassMatch      "/cool/(.*)/ws$"      ws://127.0.0.1:9980/cool/$1/ws nocanon
25
26 # Admin Console websocket
27 ProxyPass           /cool/adminws ws://127.0.0.1:9980/cool/adminws
28
29 # Download as, presentation (legacy svg) and image upload operations
30 ProxyPass           /cool http://127.0.0.1:9980/cool
31 ProxyPassReverse    /cool http://127.0.0.1:9980/cool
```

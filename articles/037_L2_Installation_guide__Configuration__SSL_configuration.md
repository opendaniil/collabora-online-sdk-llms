---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#ssl-configuration"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "ssl-configuration"
title: "SSL configuration"
canonical_title: "Installation guide / Configuration / SSL configuration"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / SSL configuration"
---
Collabora Online uses WOPI protocol, which mandates SSL. However, it is possible to run Collabora Online server without SSL, it is configurable. Basically there are 3 modes:

1. SSL
2. SSL termination
3. No SSL

When SSL is enabled, in `/etc/coolwsd/coolwsd.xml` the path to SSL key, SSL certificate and SSL CA certificate has to be given in the ssl block. This also implies that it is recommended to run coolwsd from a server which name is in DNS (e.g. hostname.example.com), and it has proper SSL certificate. Restart coolwsd, check the status of the service, and if it is running, you can try if you can connect to it via SSL:

```
curl -v https://hostname.example.com:9980/hosting/discovery
```

If it fails, you have to debug SSL settings.

For testing purposes or small deployments you can use self-signed certificates. The following example creates a certificate for `hostname.example.com` by a newly created dummy certificate authority. The resulting `.pem` files are copied to the default configuration directory of coolwsd.

```
 1 mkdir -p /opt/ssl/
 2 cd /opt/ssl/
 3 mkdir -p certs/ca
 4 openssl genrsa -out certs/ca/root.key.pem 2048
 5 openssl req -x509 -new -nodes -key certs/ca/root.key.pem -days 9131 -out certs/ca/root.crt.pem -subj "/C=DE/ST=BW/L=Stuttgart/O=Dummy Authority/CN=Dummy Authority"
 6 mkdir -p certs/{servers/hostname.example.com,tmp}
 7 openssl genrsa -out "certs/servers/hostname.example.com/privkey.pem" 2048
 8 openssl req -key "certs/servers/hostname.example.com/privkey.pem" -new -sha256 -out "certs/tmp/hostname.example.com.csr.pem" -subj "/C=DE/ST=BW/L=Stuttgart/O=Dummy Authority/CN=hostname.example.com"
 9 openssl x509 -req -in certs/tmp/hostname.example.com.csr.pem -CA certs/ca/root.crt.pem -CAkey certs/ca/root.key.pem -CAcreateserial -out certs/servers/hostname.example.com/cert.pem -days 9131
10 mv certs/servers/hostname.example.com/privkey.pem /etc/coolwsd/key.pem
11 mv certs/servers/hostname.example.com/cert.pem /etc/coolwsd/cert.pem
12 mv certs/ca/root.crt.pem /etc/coolwsd/ca-chain.cert.pem
```

The SSL termination option in the config file enables integration of Collabora Online with SSL termination proxies, which handle incoming SSL connections, decrypt the SSL and pass on the unencrypted request to the server. In this setup only the proxy server has to have proper SSL settings, Collabora Online server is hidden behind it, and Collabora Online communicates unencrypted with the proxy.

If you set both `enable` and `termination` settings to `false` in `/etc/coolwsd/coolwsd.xml`, then Collabora Online can be used in a HTTP-only environment, without encryption between browser and server. It is not recommended to use Collabora Online in this mode, but for testing only it is OK.

You can set the list of accepted SSL ciphers with the `cipher_list` setting. The default cipher list is: `ALL:!ADH:!LOW:!EXP:!MD5:@STRENGTH`.

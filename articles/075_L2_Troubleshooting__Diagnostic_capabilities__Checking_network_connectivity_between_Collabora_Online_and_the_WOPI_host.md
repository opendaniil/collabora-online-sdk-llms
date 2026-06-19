---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#checking-network-connectivity-between-collabora-online-and-the-wopi-host"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "checking-network-connectivity-between-collabora-online-and-the-wopi-host"
title: "Checking network connectivity between Collabora Online and the WOPI host"
canonical_title: "Troubleshooting / Diagnostic capabilities / Checking network connectivity between Collabora Online and the WOPI host"
toc_level: "2"
breadcrumbs: "Troubleshooting / Diagnostic capabilities / Checking network connectivity between Collabora Online and the WOPI host"
---
You can send a HTTP request at `https://<host>:<port>/hosting/wopiAccessCheck` passing a JSON `{"callbackUrl":"<wopi-host-to-check>"}` as content. Collabora Online will try to issue a HTTP request to wopi-host-to-check URL and give back a status in JSON, such as:

```
{"status":"NotHttps"}
```

The different possible status are:

> - Ok the network connectivity with the host is established and the request had a sucessful answer
> - NotHttpSuccess, the connection was successful but the response to the request was not 200
> - HostNotFound, DNS error, the host is not known by the Collabora Online server
> - WopiHostNotAllowed, the host for this request is not allowed to be used as a WOPI Host, this is likely a configuration issue in `coolwsd.xml`
> - ConnectionAborted, the connection was aborted by the destination server
> - CertificateValidation, the certificate of the response is invalid or otherwise not accepted
> - SelfSignedCertificate, the certificate is self-signed and configuration `ssl_verification` is true and thus Collabora Online does not allow self-signed certificate
> - ExpiredCertificate, the certificate has expired and configuration `ssl_verification` is true and thus Collabora Online does not allow expired certificate
> - SslHandshakeFail, couldn’t establish an SSL/TLS connection
> - MissingSsl, the response wasn’t using SSL/TLS contrary to expected
> - NotHttps, HTTPS is expected to connect to Collabora Online as the WOPI host uses it. This is necessary to prevent mixed content errors.
> - NoScheme, A scheme (`http://` or `https://`) for the WOPI host URL must be specified
> - Timeout, the request didn’t get a response within the time frame allowed
> - UnspecifiedError, an error not handled previously

Example:

```
$ curl -i https://localhost:9980/hosting/wopiAccessCheck --header "Content-Type: application/json" -d '{"callbackUrl":"https://wopi-host.local:8443"}'
```

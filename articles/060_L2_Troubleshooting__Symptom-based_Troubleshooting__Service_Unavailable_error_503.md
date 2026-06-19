---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#service-unavailable-error-503"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "service-unavailable-error-503"
title: "Service Unavailable (error 503)"
canonical_title: "Troubleshooting / Symptom-based Troubleshooting / Service Unavailable (error 503)"
toc_level: "2"
breadcrumbs: "Troubleshooting / Symptom-based Troubleshooting / Service Unavailable (error 503)"
---
When you see this error after trying to load a document, it is possible, that Collabora Online service (coolwsd) does not run properly.

First thing to try on the Collabora Online host from the administrator‘s (root) command line (commands listed for systemd):

`systemctl status coolwsd`

If the status is not active, and error is indicated, then check the logs:

`journalctl -r -u coolwsd`

The default log level is **warning**. If the root cause of the error is not clear, you can set the log level to be more detailed. Edit /etc/coolwsd/coolwsd.xml configuration file, and set the log level e.g. to **trace**. Then restart the service with:

`systemctl restart coolwsd`

and check the log again (reset log level afterwards, as verbose logging has performance implications).

The most common problem is **forgetting the SSL setup**. The path to SSL certificate, CA certificate and private key must be valid in /etc/coolwsd/coolwsd.xml. They can be set under ssl as cert_file_path, ca_file_path and key_file_path respectively.

Exit code 70 from coolwsd means internal software error, and this is most likely an issue with accessing certificates. Verify that certificates are set properly in the configuration file, and the files themselves are available with the correct access rights, i.e. readable by the cool user.

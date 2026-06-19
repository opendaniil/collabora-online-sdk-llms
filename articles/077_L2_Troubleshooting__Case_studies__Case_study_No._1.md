---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#case-study-no-1"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "case-study-no-1"
title: "Case study No. 1"
canonical_title: "Troubleshooting / Case studies / Case study No. 1"
toc_level: "2"
breadcrumbs: "Troubleshooting / Case studies / Case study No. 1"
---
A partner installed Collabora Online from the provided packages, and set up the configuration. However, upon starting, coolwsd service exited with an error.

The partner provided their configuration and logs (after setting log level to ‘trace’).

From the logs it was apparent the service exited with status code 70, and the error was also in the log file:

```
Error loading private key from file <file name> (error:0200100D:system
library:fopen:Permission denied).
```

After correcting file permissions, the service started successfully.

After this there was another issue, the WOPI host was missing from the /etc/coolwsd/coolwsd.xml configuration file. After adding host name to ‘wopi’ element the service was running and accessible.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#diagnostic-capabilities"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "diagnostic-capabilities"
title: "Diagnostic capabilities"
canonical_title: "Troubleshooting / Diagnostic capabilities"
toc_level: "1"
breadcrumbs: "Troubleshooting / Diagnostic capabilities"
---
- Opening http(s)://<host>:<port>/ (as set up) in browser shows “OK” if service is running correctly
- Opening http(s)://<host>:<port>/hosting/discovery (as set up) in browser brings up the WOPI discovery file
- Checking network connectivity between Collabora Online and the WOPI host
- The following command brings up logs for the web socket daemon service: `journalctl -r -u coolwsd`
  Preferably set log level to trace in /etc/coolwsd/coolwsd.xml configuration file under ‘logging’/’level’ beforehand
- When opening a file, the browser’s developer console logs potential errors and information related to the web page
- **Browser logging**: By default, Collabora Online’s internal console output is suppressed in the browser. When `<browser_logging>` is enabled in `coolwsd.xml`, this output becomes visible in the browser’s developer console, and `console.error()` calls and uncaught JavaScript exceptions are additionally forwarded to the server log as `jserror` messages at ERROR level. This is useful for diagnosing client-side issues without needing access to the end user’s browser. See [Browser logging](031_L1_Installation_guide__Configuration.md) for details on how to enable it.
- When a file is opened, Ctrl-Alt-Shift-D brings up a debug view that shows information related to rendered tiles, including server latency
- The admin console is accessible separately under the following location: http(s)://<host>:<port>/browser/dist/admin/admin.html
   `coolconfig set-admin-password`

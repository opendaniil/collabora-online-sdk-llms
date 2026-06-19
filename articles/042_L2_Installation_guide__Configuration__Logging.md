---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml#logging"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: "logging"
title: "Logging"
canonical_title: "Installation guide / Configuration / Logging"
toc_level: "2"
breadcrumbs: "Installation guide / Configuration / Logging"
---
See the `<logging>` section in `/etc/coolwsd/coolwsd.xml`. Set the log level and verbosity to one of: none (turns off logging), fatal, critical, error, warning, notice, information, debug, trace.

This can also be set on the coolwsd launch command line and docker run command using the option `--o:logging.file[@enable]=true --o:logging.level=trace`.

The default log level is warning. If `<color>` is set to true, then *coolwsd* will generate logging information containing console color codes. It is possible to redirect logs to a file. The trace file defined in `<trace>` section provides extra debug information.

### Browser logging

The `<browser_logging>` setting (disabled by default) controls browser-side logging. When disabled, Collabora Online’s internal `app.console.*` output is suppressed in the browser (replaced with no-ops). When enabled:

- Collabora Online’s internal console output (debug, info, warning, error, etc.) becomes visible in the browser’s developer console.
- `console.error()` calls and uncaught exceptions (`window.onerror`) are additionally forwarded to the server log at ERROR level as `jserror` messages.
- The messages are sent over the WebSocket connection when available, or via an HTTP POST to the `browser-logging` endpoint during early page load before the WebSocket is established.
- A SHA1 token is generated at server startup and embedded in the served HTML page, which the browser uses to authenticate its log messages.

To enable it, set it in `/etc/coolwsd/coolwsd.xml`:

```
<browser_logging>true</browser_logging>
```

Or via the command line: `--o:browser_logging=true`

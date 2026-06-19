---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Configuration.xhtml"
source_file: "docs/installation/Configuration.xhtml"
source_anchor: ""
title: "Configuration"
canonical_title: "Installation guide / Configuration"
toc_level: "1"
breadcrumbs: "Installation guide / Configuration"
---
The postinstall script of coolwsd package added a non-privileged user to the system: *cool* . Collabora Online service will be run by *cool* user. Also the service was registered to systemd, enabled on system start and started. Useful commands:

- `systemctl enable coolwsd` – enable coolwsd on system start
- `systemctl disable coolwsd` – disable coolwsd on system start
- `systemctl status coolwsd` – check status of coolwsd
- `systemctl stop coolwsd` – stop coolwsd service
- `systemctl start coolwsd` – start coolwsd service
- `systemctl restart coolwsd` – stop then start coolwsd service
- `journalctl -u coolwsd` – read the log produced by coolwsd

Collabora Online has to be configured before use. Most of the options have sensible defaults.

Collabora online has layered configuration, which means that settings are read from `/etc/coolwsd/coolwsd.xml` but can be overridden by command line switches (for example in systemd’s coolwsd.service file). By using `--o:name=value` the setting called `name` can be replaced by `value`. For example: `--o:per_document.max_concurrency=12`. This will override the `max_concurrency` to 12, regardless of what the XML has set.

Default configuration entries and values are set before loading the configuration file from disk. This ensures that an upgrade to the server with new configuration entries will not break the server when the XML is not upgraded, rather, the server will fallback to the defaults when it fails to find the entry in the XML.

The coolwsd service has to be restarted after a change in configuration.

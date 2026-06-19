---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/integrations/odoo.xhtml#configuration"
source_file: "docs/integrations/odoo.xhtml"
source_anchor: "configuration"
title: "Configuration"
canonical_title: "Integrations setup / Odoo / Configuration"
toc_level: "2"
breadcrumbs: "Integrations setup / Odoo / Configuration"
---
![../../_images/odoo-settings.png](assets/_images/odoo-settings.png)

These are the options you can set:

| Setting | Description |
| --- | --- |
| Collabora Online Server URL | The URL of the Collabora Online server. |
| Odoo URL | The URL of the Odoo server. |
| Disable certificate verification (insecure) | Disable the TLS certificate verification when connecting to the Collabora Online server. Caution Should only be “checked” for development, if you don’t have valid certificates. |
| JWT Secret | This secret is used to generate the token to access the documents. |
| Token TTL | How long the token is valid, in seconds. Default is 86,400 seconds (24 hours). |

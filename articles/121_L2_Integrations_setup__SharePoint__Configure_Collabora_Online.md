---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/integrations/sharepoint.xhtml#configure-collabora-online"
source_file: "docs/integrations/sharepoint.xhtml"
source_anchor: "configure-collabora-online"
title: "Configure Collabora Online"
canonical_title: "Integrations setup / SharePoint / Configure Collabora Online"
toc_level: "2"
breadcrumbs: "Integrations setup / SharePoint / Configure Collabora Online"
---
1. SharePoint uses WOPI security and requires using a proof key to authenticate WOPI applications. **The proof key is automatically generated at the package installation** of Collabora Online, so normally no user interaction is needed to set this up.

> In the unexpected case, when this automatic setup does not work, use this command to generate an RSA key:
>
> ```
> coolwsd-generate-proof-key
> ```
>
> In case your config dir is not /etc, you need to check coolwsd.log, which would contain a warning about missing proof-key in discovery. The warning would contain the command line to use for manual generation of the key, like this:
>
> ```
> ssh-keygen -t rsa -N "" -m PEM -f "/path/to/coolwsd/config/proof-key"
> ```

2. Authorize the SharePoint server in Collabora Online. Open `coolwsd.xml`, and add a host element under WOPI storage element for the SharePoint WOPI host (replace `sharepoint-host-name.example.com` with the actual host name):

> ```
> <host allow="true">sharepoint-host-name.example.com</host>
> ```
>
> If you do not authorize WOPI host, this will result in failure opening documents. The server’s name which was not matched would then be listed in coolwsd.log.

3. Start Collabora Online.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#setup-settings-iframe"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "setup-settings-iframe"
title: "Setup Settings iframe"
canonical_title: "Advanced integration / Setup Settings iframe"
toc_level: "1"
breadcrumbs: "Advanced integration / Setup Settings iframe"
---
New in version 24.04.12.4.

The settings iframe enables you to embed a variety of configuration options related to office documents directly within your application, allowing users to manage all their per-user settings in one convenient location of your choice.

There are two types of settings supported:

- **User settings** – These are per-user configuration files (e.g., AutoText, dictionaries) specific to individual users.
- **Shared settings** – These are system-level or global configurations that apply to all users. Typically editable only by administrators.

Currently these are the supported settings: Autotext, custom dictionaries, interface settings, and some of the registered advanced settings that can help customize document view.

Assuming you already know how to integrate Collabora Online. If not, refer to [How to integrate](146_L0_How_to_integrate.md).

To take advantage of per-user and shared settings, follow the additional two steps:

- **Setup the iframe** into your settings/admin/user page as described below.
- **Provide `CheckFileInfo` response** that includes the required `UserSettings` and/or `SharedSettings` fields. Refer to UserSettings and SharedSettings for structure and examples.

To set up the iframe, the WOPI host (your application) needs to read a discovery XML from a defined location on the WOPI client (the Collabora Online server). The discovery XML is available at:

```
https://<WOPI client URL>:<port>/hosting/discovery
```

The response is a discovery.xml file that contains a `Settings` app, and within it, an action with the value `iframe` which includes a `urlsrc` property to set the iframe URL.

You also need to pass the authentication token to Collabora Online via a form post (using a hidden field) along with the WOPI setting base URL where the iframe can communicate.

Example:

```
https://<WOPI host URL>/<...>/wopi/settings
```

Note

You must include wopi_setting_base_url as a hidden form field when posting to the iframe. For example:

`<your_wopi_base_url>/wopi/settings`

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#checking-for-available-features"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "checking-for-available-features"
title: "Checking for available features"
canonical_title: "Advanced integration / Checking for available features"
toc_level: "1"
breadcrumbs: "Advanced integration / Checking for available features"
---
With new features, it is important for the integrations to know if the Online they are using is supporting them. For this reason, we have introduced a `/hosting/capabilities` endpoint that returns a JSON with information about the availability of various features.

Currently the following are present:

- `convert-to:` `{ available: true/false }`
  The property `available` is `true` when the [convert-to functionality](284_L0_Conversion_API.md) is present, and is allowed from the requesting address. Because of that, the endpoint needs to be accessed from the WOPI host for it to return relevant result.
  A common use of the functionality is that WOPI hosts can use it to generate document previews to show in their file list.
- `hasTemplateSource`: `true/false`
  is `true` when Collabora Online supports the `TemplateSource` `CheckFileInfo` property.
- `hasMobileSupport`: `true/false`
  is `true` when Collabora Online has a good support for the mobile devices and responsive design.

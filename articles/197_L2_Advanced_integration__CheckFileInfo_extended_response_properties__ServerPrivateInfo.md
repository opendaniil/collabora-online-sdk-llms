---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#serverprivateinfo"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "serverprivateinfo"
title: "ServerPrivateInfo"
canonical_title: "Advanced integration / CheckFileInfo extended response properties / ServerPrivateInfo"
toc_level: "2"
breadcrumbs: "Advanced integration / CheckFileInfo extended response properties / ServerPrivateInfo"
---
New in version 24.04.11.

JSON object that contains credentials, but unlike `UserPrivateInfo`, it is meant to be per-server, not per-user.

#### Electronic signature handling

When the `ESignatureBaseUrl`, `ESignatureClientId` and `ESignatureSecret` keys in `ServerPrivateInfo` are specified, the electronic signing functionality for PDF files gets enabled in Collabora Online’s user interface (the Insert menu has an Electronic signature menu item).

For testing purposes it is OK to use the credentials from [eID Easy’s guide](https://docs.eideasy.com/guide/test-environment.html#test-environment-api-credentials) [https://docs.eideasy.com/guide/test-environment.html#test-environment-api-credentials]. The `smart-id-signature` provider has test ID-codes on their [test user page](https://docs.eideasy.com/guide/test-user/smartid.html) [https://docs.eideasy.com/guide/test-user/smartid.html].

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml#gray-document-area-no-document-loaded"
source_file: "docs/installation/Collabora_Online_Troubleshooting_Guide.xhtml"
source_anchor: "gray-document-area-no-document-loaded"
title: "Gray document area, no document loaded"
canonical_title: "Troubleshooting / Symptom-based Troubleshooting / Gray document area, no document loaded"
toc_level: "2"
breadcrumbs: "Troubleshooting / Symptom-based Troubleshooting / Gray document area, no document loaded"
---
When you see gray document are, i.e. the iframe of Collabora Online is not loaded, you can check the browser‘s console to see what is going on. For the browser‘s diagnostic tools, press **F12**, and see network activity.

A common mistake, when http and https content is mixed on the same page, and the browser refuses to load insecure http iframe into an https page. If SSL is used, which is highly recommended, make sure that all components, including Collabora Online is set up for SSL.

The iframe can be blocked due to a content security policy setting. The problem should be reported on the browser‘s console. See [Content Security Policy](212_L1_Advanced_integration__Content_Security_Policy.md).

Gray screen could be the result of incorrectly set up reverse proxy (see below), and related server_name setting.

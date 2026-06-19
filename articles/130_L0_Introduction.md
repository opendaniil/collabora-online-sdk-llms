---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/introduction.xhtml"
source_file: "docs/introduction.xhtml"
source_anchor: ""
title: "Introduction"
canonical_title: "Introduction"
toc_level: "0"
breadcrumbs: "Introduction"
---
This document will help you integrating with your existing solution (file storage) so that your users can edit the documents hosted in the file storage via web browser.

For this to work, you have to setup and connect several parts together:

- Server for hosting Collabora Online
- Website that presents iframe with the editing capabilities
- Authentication
- Connection to the file storage

The easiest way to integrate Collabora Online is using the WOPI protocol.

Collabora Online implements a protocol inspired by the WOPI (Web Application Open Platform Interface) protocol. Using the WOPI vocabulary as we do throughout this document, Collabora Online is a *WOPI client* that can be integrated with a *WOPI host* (your existing solution: web application and file storage). WOPI is a well documented open protocol, for more details please visit the [WOPI documentation](https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/) [https://learn.microsoft.com/en-us/microsoft-365/cloud-storage-partner-program/rest/].

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/How_to_integrate.xhtml#website-that-presents-the-editing-capabilities"
source_file: "docs/How_to_integrate.xhtml"
source_anchor: "website-that-presents-the-editing-capabilities"
title: "Website that presents the editing capabilities"
canonical_title: "How to integrate / Website that presents the editing capabilities"
toc_level: "1"
breadcrumbs: "How to integrate / Website that presents the editing capabilities"
---
We assume that you want to integrate the editing capabilities into your existing website. On the website, you need to present an iframe where the editing UI and the document itself will be present.

To set up the iframe, the *WOPI host* (your application) needs to read a discovery XML from a defined location on the *WOPI client* (the Collabora Online server). The discovery is available at:

```
https://<WOPI client URL>:<port>/hosting/discovery
```

The reply is discovery.xml that contains *urlsrc* for various file formats. The urlsrc specifies the address that you need to use for the iframe that you create for the document editing, and is set as an attribute of the HTML and or tag of the document.

You also need to pass the authentication token to Collabora Online via a form post, and the actual URL that your file storage can accept. The URL should look like:

```
https://<WOPI host URL>/<...>/wopi/files/<id>
```

Here `/wopi/` can actually be any string that starts with `wopi`, like `/wopifiles/` or `/wopi_implementation/`, but for simplicity, we will be using only `/wopi/` in the following text.

`<id>` should be URL-safe base64 (base64url) encoded, ie. only contain letters (`A-Z`, `a-z`), numerals (`0-9`), and `-` and `_` symbols.

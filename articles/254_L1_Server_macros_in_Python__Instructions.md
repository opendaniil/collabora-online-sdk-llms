---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/Using_Python_scripting_in_Collabora_Online.xhtml#instructions"
source_file: "docs/Using_Python_scripting_in_Collabora_Online.xhtml"
source_anchor: "instructions"
title: "Instructions"
canonical_title: "Server macros in Python / Instructions"
toc_level: "1"
breadcrumbs: "Server macros in Python / Instructions"
---
In the Online sources there is a web page `browser/html/framed.html` and `browser/html/framed.doc.html` that are examples of web pages that run an unmodified Collabora Online instance inside an HTML `iframe`, and then from the HTML code outside the iframe calls Python scripts in the underlying LibreOffice instance to manipulate data in the document open in the Collabora Online instance. Various parameters can be passed to the Python scripts, and return values handled.

Both `framed.html` and `framed.doc.html` are just for demonstration purposes and very bare-bones visually.

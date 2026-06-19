---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/theming.xhtml#content-of-hidden-field-css-variables"
source_file: "docs/theming.xhtml"
source_anchor: "content-of-hidden-field-css-variables"
title: "Content of hidden field “css_variables”"
canonical_title: "Theming of Collabora Online / Content of hidden field “css_variables”"
toc_level: "1"
breadcrumbs: "Theming of Collabora Online / Content of hidden field “css_variables”"
---
New in version 24.04: Server-side substitution of CSS variables passed via the `css_variables` hidden form field.

The default values of various css variables can be overridden by sending them in the post message in this format:

```
<input name="css_variables" value="--co-color-main-text=#000;--co-body-bg=#FFF;--co-primary-element=#2e1a47;" type="hidden"/>
```

Note that the variables in the form are formatted slightly different from how they look in the CSS file! The colon `:` found in CSS is replaced by an equal sign `=`.

You can also test your colours by adjusting the COOL url and append those values, so they can be passed via get and so you can see your changes instantaneously. Example:

```
http://localhost:9980/browser/debug.html?file_path=/cool/test/data/hello-world.odt&css_variables=--co-primary-element%3Dred;--co-body-bg%3D%23FDFDFD
```

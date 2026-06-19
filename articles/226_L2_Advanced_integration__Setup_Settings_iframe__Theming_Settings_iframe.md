---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#theming-settings-iframe"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "theming-settings-iframe"
title: "Theming Settings iframe"
canonical_title: "Advanced integration / Setup Settings iframe / Theming Settings iframe"
toc_level: "2"
breadcrumbs: "Advanced integration / Setup Settings iframe / Theming Settings iframe"
---
#### Dark/Light mode

The settings iframe supports both light and dark modes. To select the desired mode, pass the post message (hidden field) `ui_theme` parameter with either `light` or `dark`.

#### Content of hidden field css_variables

The default values of various CSS variables can be overridden by sending them as part of the post message using the following format:

```
<input name="css_variables" value="--co-settings-btn-primary: #0b87e7;
--co-settings-btn-primary-text: #fff; --co-settings-btn-light: #83beec;
--co-settings-btn-light-text: #0e242f; --co-settings-border: #b6b6b6;
--co--settings-border-contrast: #cecece; --co-settings-text: #fff;
--co-settings-text-maxcontrast: #f1f1f1; --co-settings-background: #F8F9FA;
--co-settings-background-hover: #e8e8e8;" type="hidden"/>
```

For more details, please refer to: [Extra hidden field in COOL frame integration](228_L0_Theming_of_Collabora_Online.md)

Various CSS variables can be overridden for the theming. Their names, and the default values that are used in COOL setting iframe:

```
--co-settings-btn-primary: #0b87e7;
--co-settings-btn-primary-text: #fff;
--co-settings-btn-light: #83beec;
--co-settings-btn-light-text: #0e242f;
--co-settings-border: #b6b6b6;
--co--settings-border-contrast: #cecece;
--co-settings-text: #fff;
--co-settings-text-maxcontrast: #f1f1f1;
--co-settings-background: #F8F9FA;
--co-settings-background-hover: #e8e8e8;
```

If your theme includes a sub-directory for your own custom theme, you can pass a string to the `ui_theme` parameter in the hidden post message. If this is not necessary, you can simply omit this field.

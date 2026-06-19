---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/accessibility.xhtml"
source_file: "docs/accessibility.xhtml"
source_anchor: ""
title: "Accessibility"
canonical_title: "Accessibility"
toc_level: "0"
breadcrumbs: "Accessibility"
---
# Accessibility in Collabora Online

Enabling accessibility support has a performance impact, therefore it is off by default. You can set it `true` in `coolwsd.xml`.

accessibility block of coolwsd.xml

```
 <accessibility desc="Accessibility settings">
     <enable type="bool" desc="Controls whether accessibility support should be enabled or not." default="false">true</enable>
 </accessibility>
```

Then you will have a `Screen Reading` button in the `Help` tab that you have to press.

 ![accessibility option demo](assets/_images/a11y-screen-reading.png)

In the Nextcloud integration there is a user view setting `In-document Screen Reader` to have this button always pressed.

 ![nextcloud setting demo](assets/_images/nextcloud-a11y-setting.png)

Note

The Screen Reading button only controls reading of the document content. All other UI components (such as navigator, tabs, sidebar and dialogs) remain accessible regardless of whether the button is enabled.

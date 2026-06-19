---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/theming.xhtml#how-values-are-applied"
source_file: "docs/theming.xhtml"
source_anchor: "how-values-are-applied"
title: "How values are applied"
canonical_title: "Theming of Collabora Online / How values are applied"
toc_level: "1"
breadcrumbs: "Theming of Collabora Online / How values are applied"
---
Each `key=value` pair is parsed server-side and emitted into a synthesised `:root { … }` block. The implementation lives in `wsd/FileServerUtil.cpp` (`FileServerRequestHandler::cssVarsToStyle`) and rejects tokens that contain `< > { } & | \ " ^ ` ' $ [ ]` or any control character. There is no allow-list for variable names: any custom property may be set, but only the ones that COOL’s stylesheets actually read will have a visible effect. The lists below cover those.

A small number of variables are set with `!important` inside the Collabora branding sheet (`browser/dist/branding.css`) and therefore cannot be overridden through `css_variables` alone:

- `--color-calc-header-selected`, `--color-calc-header-hover`
- `--color-text-calc-header-selected`
- `--color-doc-name-input-bg-hover`
- `--column-row-highlight`

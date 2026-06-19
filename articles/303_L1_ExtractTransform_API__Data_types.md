---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#data-types"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "data-types"
title: "Data types"
canonical_title: "Extract/Transform API / Data types"
toc_level: "1"
breadcrumbs: "Extract/Transform API / Data types"
---
Further on we’ll use the following conventions to specify the type of values and data.

- `<num>` An integer number value.
- `<string>` A string value. When it is the value in JSON it is surrounded by quotes `"`.
- `<text>` A text value.
- `<boolean>` A boolean value. The literals are `true` and `false`.
- `[<TYPE>,]` An array of <TYPE> of any length. Can be any of the known data type.
- `[<TYPE>,<TYPE>]` An fixed size array of <TYPE> value. Example: `[<num>,<num>]` for an array of two integer.
- `<value>` A JSON value of any type.
- `NONE` There is no value. To satisfy JSON syntax substitute with `""`.
- `|` Indicate alternative when several types are possible.

Not all types are valid in every situation, but when used as a JSON value, the proper JSON syntax should be used: strings and text are quoted, arrays are JSON arrays, etc.

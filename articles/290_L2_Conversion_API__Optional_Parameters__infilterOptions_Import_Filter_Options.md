---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#infilteroptions-import-filter-options"
source_file: "docs/conversion_api.xhtml"
source_anchor: "infilteroptions-import-filter-options"
title: "infilterOptions – Import Filter Options"
canonical_title: "Conversion API / Optional Parameters / infilterOptions – Import Filter Options"
toc_level: "2"
breadcrumbs: "Conversion API / Optional Parameters / infilterOptions – Import Filter Options"
---
This parameter can be used to change the default behaviour of the CSV import filter.

The legacy positional token format is described on the [Collabora Office Help – CSV Filter Options page](https://help.collaboraoffice.com/latest/en-US/text/shared/guide/csv_params.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/guide/csv_params.html]. For example `infilterOptions=44,34,76,1` sets the field separator to `,`, the text delimiter to `"`, the character set to UTF-8, and the reading will start from line 1.

New in version 25.04.9.3.

When `infilterOptions` starts with `{`, it is parsed as JSON. If no options are given, the defaults are UTF-8 encoding, comma field separator, and double-quote text delimiter. The following properties are supported:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| FieldSeparator | string | , | Field separator character (e.g. "," for comma, "\t" for tab) |
| TextDelimiter | string | " | Text quoting character. Use an empty string for no quoting. |
| CharacterSet | string | UTF-8 | Character set name (e.g. UTF-8, ISO-8859-1, Windows-1252) |
| MergeDelimiters | boolean | false | Treat consecutive separators as a single separator |
| RemoveSpace | boolean | false | Trim leading and trailing spaces from field values |
| QuotedFieldAsText | boolean | false | Always import quoted fields as text (do not convert to numbers) |
| DetectSpecialNumber | boolean | false | Detect special number formats (dates, scientific notation, etc.) |
| DetectScientificNumber | boolean | true | Detect scientific notation (e.g. 1.5E+3) |
| EvaluateFormulas | boolean | true | Evaluate cell contents that start with = as formulas |
| SkipEmptyCells | boolean | false | Skip empty cells and preserve previous cell content |
| StartRow | long | 1 | First row to import (1-based) |
| Language | string |  | BCP47 language tag for locale-dependent number parsing (e.g. en-US, de-DE). When omitted, the system locale is used. |
| FixedWidth | boolean | false | Parse the file as fixed-width columns instead of using a field separator. When true, ColumnFormat defines the column boundaries by character position. |
| ColumnFormat | string |  | Per-column format specification as slash-separated position/format pairs. Each pair consists of a 1-based column number (or character offset when FixedWidth is true) followed by a format code: 1 = Standard, 2 = Text, 3 = MM/DD/YY, 4 = DD/MM/YY, 5 = YY/MM/DD, 9 = skip column, 10 = US-English. Example: "1/2/2/1/3/9" imports column 1 as text, column 2 as standard, and skips column 3. |

It is also possible to use both `options` and `infilterOptions` in the same request. This is particularly useful for CSV-to-CSV conversions where the input and output files use different delimiters, character sets, or other settings.

See CSV Import and CSV-to-CSV Conversions for usage examples.

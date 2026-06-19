---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#compare-compare-option"
source_file: "docs/conversion_api.xhtml"
source_anchor: "compare-compare-option"
title: "compare – Compare Option"
canonical_title: "Conversion API / Optional Parameters / compare – Compare Option"
toc_level: "2"
breadcrumbs: "Conversion API / Optional Parameters / compare – Compare Option"
---
New in version 25.04.8.1.

This option allows comparing two versions of a Writer document (DOCX, ODT, RTF, etc.). The `data` parameter contains the new version, and the `compare` parameter contains the old (baseline) version. Collabora Online compares the two documents and inserts the differences as tracked changes (redlines) into the result: deleted text appears with strikethrough and inserted text is highlighted. The result can then be exported in any supported format.

This is useful for generating a visual diff of two document versions — for example, to produce a PDF that shows exactly what changed between two revisions of a contract.

Note

This option is only supported for Writer documents. Calc, Impress, and Draw documents do not produce meaningful visual output from document comparison.

Example — compare two versions of a DOCX file and export the differences as PDF:

```
curl -k -F "data=@new.docx" -F "compare=@old.docx" -F "format=pdf" \
     -o out.pdf https://localhost:9980/cool/convert-to
```

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id1"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id1"
title: "Extract"
canonical_title: "Extract/Transform API / Charts / Extract"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Charts / Extract"
---
Use `filter=charts` to extract the charts.

Example output: (it is pretty printed here):

```
{
    "DocStructure": {
        "Charts.ByEmbedIndex.0": {
            "name": "Object1",
            "title": "Paid leave days",
            "subtitle": "Subtitle2",
            "RowDescriptions": [ "James", "Mary", "Patricia", "David"],
            "ColumnDescriptions": [ "2022", "2023"],
            "DataValues": [
                [ "22", "24"],
                [ "18", "16"],
                [ "32", "32"],
                [ "25", "23"]
            ]
        }
    }
}
```

Data it extracts:

| Property | Description |
| --- | --- |
| name | Name of the embedded object of the chart, can be used as a filter in transform to select the needed chart. |
| title | The title of the chart, as a simple string. |
| subtitle | The Subtitle of the chart, as a simple string. |
| RowDescriptions | Array of strings, containing the descriptions of the rows. |
| ColumnDescriptions | Array of strings, containing the descriptions of the columns. |
| DataValues | Matrix of numbers, containing every cells data. |

Note

Some of the data values can be “NaN”, this means they are not set.

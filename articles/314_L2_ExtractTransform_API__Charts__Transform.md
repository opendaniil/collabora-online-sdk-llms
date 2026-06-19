---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id2"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id2"
title: "Transform"
canonical_title: "Extract/Transform API / Charts / Transform"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Charts / Transform"
---
Example Transform:

```
{
    "Transforms": [
        { "Charts.ByEmbedIndex.0": [
            {"modifyrow.1": [ 19, 15 ]},
            {"datayx.3.1": 37},
            {"deleterow.0": ""},
            {"insertrow.0": [ 15, 17 ]},
            {"setrowdesc.0": "Paul"},
            {"insertcolumn.1": [ 1,2,3,4,5,6 ]},
            {"setcolumndesc.0": "c0"},
            {"deletecolumn.3": ""}
        ]},
        { "Charts.ByEmbedName.Object3": [
            {"resize": [ 3, 3 ]},
            {"setrowdesc": [ "a", "b", "c"]}
        ]},
        { "Charts.ByTitle.Fixed issues": [
            {"data": [ [ 3,1 ],
                       [ 2,0,1 ],
                       [ 3 ] ]},
            {"setrowdesc": ["2023.01",".02",".03"]},
            {"setcolumndesc": ["Jennifer", "Charles", "Thomas"]}
        ]}
    ]
}
```

To select which chart you want to transform, you can use these selectors:

| Selector | Description |
| --- | --- |
| ByEmbedIndex.<num> | Index of the embedded object counted from 0. It is always unique, but the index may reference embed other than charts. |
| ByEmbedName.<string> | The unique name of the embedded object of the chart. |
| ByTitle.<string> | Title of the chart. (Title is optional) |
| BySubTitle.<string> | Subtitle of the chart. (Subtitle is optional) |

Note

While the values of the chart transformations can be represented by an object, it is recommended to use the new form as an array.

To transform a chart you can use these commands:

| Command | Value | Description |
| --- | --- | --- |
| deletecolumn.<num> | NONE | Delete the <num> column |
| deleterow.<num> | NONE | Delete the <num> row |
| modifycolumn.<num> | [<num>,] | Set the column <num> data to the values |
| modifyrow.<num> | [<num>,] | Set the row <num> data to the values |
| insertcolumn.<num> | NONE | Insert an empty column before column <num> |
| insertcolumn.<num> | [<num>,] | Insert a column before column <num>, with values |
| insertrow.<num> | NONE | Insert an empty row before row <num> |
| insertrow .<num> | [<num>,] | Insert a row before row <number>, with values |
| setcolumndesc.<num> | <text> | Set column <num> description to <text> |
| setcolumndesc | [<text>,] | Set the column description to the values from the first. |
| setrowdesc.<num> | <text> | Set the row <num> description to <text> |
| setrowdesc | [<text>,] | Set the row description to the values from the first. |
| resize | [<num>,<num>] | Resize data table <num> row and <num> column. Both numbers are required, and must be greater then 1. |
| datayx.<num>.<num> | <num> | Set the value of the cell row <num> and column <num> to the specified value. |
| data | [[<num>,],] | Set values of the data table to the values. The table size will grow as needed. |

Note

Commands that needs an array of values can be used with less values than the destination array. In that case it will only change the provided elements and leave the remaining one untouched.

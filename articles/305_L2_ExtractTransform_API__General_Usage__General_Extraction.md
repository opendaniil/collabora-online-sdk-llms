---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#general-extraction"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "general-extraction"
title: "General Extraction"
canonical_title: "Extract/Transform API / General Usage / General Extraction"
toc_level: "2"
breadcrumbs: "Extract/Transform API / General Usage / General Extraction"
---
The extraction API work simply by sending the document, and setting an optional filter specifying the data you are interested in. In return you receive a JSON document decribing the document.

> **API:** HTTP POST to `/cool/extract-document-structure`

Example:

```
curl -F "data=@test.docx" -F "filter=contentcontrol" https://localhost:9980/cool/extract-document-structure > out.json
```

Tip

Use `curl`’s `-k` argument in testing environment to disable certificate validation, as it is unlikely you have one in that situation. **On a production system, please make sure you have valid certificates and not disabled the validation with** `-k`.

> Or in HTML:

```
1<form action="https://localhost:9980/cool/extract-document-structure" enctype="multipart/form-data" method="post">
2 File: <input type="file" name="data"><br/>
3 Filter: <input type="text" name="filter" value="contentcontrol"><br/>
4 <input type="submit" value="Extract">
5</form>
```

| Query parameter | Description |
| --- | --- |
| data | The document file itself in the payload. |
| filter | The filter parameter (optional, recommended, see note) sets what to extract. Currently supported filter values are: contentcontrol: data for the content controls charts: data for the chart docprops: document properties trackchanges: list of tracked changes slides: presentation content |
| lang | The language parameter (optional) sets the default format language, useful for date type cells. If passed, the load language is used and it determines the display/output format. Example: lang=fr-FR |

Attention

Without setting `filter`, the API will extract everything. Avoid using it without filters. As the API is expanded, the extracted data will be expanded too, that may cause unexpected problems.

#### Items

The extracted document content JSON is structured in the following way. The top-level object contains a `DocStructure` object. It itself contains a bunch of objects, the items.

```
{
    "DocStructure": {
        "Charts.ByEmbedIndex.0": {
            "..."
        },
        "ContentControls.ByIndex.0": {
            "..."
        },
        "DocumentProperties": {
            "..."
        },
        "TrackChanges.ByIndex.0": {
            "..."
        }
    }
}
```

Each item is addressed by a selector.

Item selectors are used to represent an item in the document structure. They are specified by a string composed of up to three dot-separated components.

1. The type of the object. Current possible values are `Charts`, `ContentControls`, `DocumentProperties`, `TrackChanges`. Document properties are a singleton set so there is no need to address it.
2. The addressing method. `ByIndex`, `ById`, `ByAlias`, `ByTag` are valid for `ContentControls`, `ByEmbedIndex`, `ByEmbedName`, `ByTitle`, `BySubTitle` as valid for `Charts`; `ByIndex` is valid for `TrackChanges`.
3. The “index”, the parameter to the addressing. It is a string or a number depending on the method.

Examples:

```
Charts.ByTitle.Untitled Chart
Charts.ByEmbedIndex.2
ContentControls.ByTag.machine-readable
ContentControls.ByIndex.4
```

Each item is described by properties. The property names and their values are described in the corresponding section. They can be numbers, strings of text, arrays, or just another object. Transform involve changing these properties.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#general-transform"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "general-transform"
title: "General Transform"
canonical_title: "Extract/Transform API / General Usage / General Transform"
toc_level: "2"
breadcrumbs: "Extract/Transform API / General Usage / General Transform"
---
Much like the extract API, the transform API work simply by sending the document, and in addition, a transform reciepe. The result is a new document.

> **API:** HTTP POST to `/cool/transform-document-structure/<format>&<lang=xx-XX>`

`format` or `lang` parameters can be ommitted

> **API:** HTTP POST to `/cool/transform-document-structure`

Tip

You can provide format as another parameter. If no format defined, it will use the input file format.

Example:

```
curl -v -k -F "data=@test.docx" -F "format=docx" -F "transform=$(cat transform.JSON)" https://localhost:9980/cool/transform-document-structure > out.docx
curl -k -F "data=@test.docx" -F "format=odt" -F "transform={\"Transforms\":{\"ContentControls.ByIndex.1\":{\"content\":\"Short text\"},\"ContentControls.ByIndex.6\":{\"content\":\"5/14/2024\",\"alias\":\"date\"}}}}" https://localhost:9980/cool/transform-document-structure > out.odt
```

> Or in HTML:

```
1<form action="https://localhost:9980/cool/transform-document-structure" enctype="multipart/form-data" method="post">
2 File: <input type="file" name="data"><br/>
3 Format: <input type="text" name="format"><br/>
4 Transform: <input type="text" name="transform"><br/>
5 <input type="submit" value="Transform">
6</form>
```

| Query parameter | Description |
| --- | --- |
| data | The document file itself in the payload. |
| format | The format parameter (optional) is the format of the output document file. e.g. odt, docx |
| transform | The transform parameter (required) a JSON formatted string that contains the transformation commands. |
| lang | The language parameter (optional) sets the default format language, useful for date type cells. If passed, the load language is used and it determines the display/output format. Example: lang=fr-FR |

#### Commands

The JSON structure for transformations is close the extracted document structure. The top-level object contains any number of `Transforms` and `UnoCommand` objects, in any order. `Transforms` may be an array or object which itself contains a bunch of objects, the commands to transform.

Each command addresses items by a selector and contains a bunch of properties (or sub-objects) describing the actions to take on the items. The transform commands are executed in the order they are listed in the transform JSON. An item selector (for example `Charts.ByTitle.CommonName`) may match more than one item, and thus may transform more that one item. In that case the items will be handled one after the other, based on an item order (`ByIndex`, `ByEmbedIndex`, etc.). Once all of the matching items are processed, the next command is run, and so on. This behaviour can be useful in many cases, but be aware with complex cases and its side effects. Commands may overwrite, not only the previous commands results, but alter future commands.

Note

Some of the items can be an array of objects with 1:1 properties, or an object with properties. Please use the new form using arrays if possible. As in JSON, object properties must be unique, if some properties have the same name, then the result an invalid JSON document. Collabora Online might handle it despite being invalid JSON. For example the Transforms property value is supposed to be an array, but it can be an object as well.

#### UNO Commands

New in version 25.04.6.3.

In addition to `Transforms` objects, the top-level object of JSON can also contain any number of `UnoCommand` objects, each containing a `name`, and an optional `arguments`, subobjects of which define arguments for the command. The syntax for arguments follows that in [Conversion API](284_L0_Conversion_API.md), and includes a `type` (e.g., `string`, `long`, `boolean`), and a `value`. The `UnoCommand` elements are executed sequentially in the order of their appearance.

Example transform using `UnoCommand`, that enables change tracking:

```
{
    "UnoCommand": {
        "name": ".uno:TrackChanges",
        "arguments": {
            "TrackChanges": {
                "type": "boolean",
                "value": "true"
            }
        }
    }
}
```

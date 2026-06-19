---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id6"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id6"
title: "Transform"
canonical_title: "Extract/Transform API / Document Properties / Transform"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Document Properties / Transform"
---
Example Transform:

```
{
    "Transforms": [
        {"DocumentProperties": {
            "Author":"Author TxT",
            "Generator":"Generator TxT",
            "CreationDate":"2024-01-21T14:45:00",
            "Title":"Title TxT",
            "Subject":"Subject TxT",
            "Description":"Description TxT",
            "Keywords": [ ],
            "Language":"en-GB",
            "ModifiedBy":"ModifiedBy TxT",
            "ModificationDate":"2024-05-23T10:05:50.159530766",
            "PrintedBy":"PrintedBy TxT",
            "PrintDate":"0000-00-00T00:00:00",
            "TemplateName":"TemplateName TxT",
            "TemplateURL":"TemplateURL TxT",
            "TemplateDate":"0000-00-00T00:00:00",
            "AutoloadURL":"",
            "AutoloadSecs": 0,
            "DefaultTarget":"DefaultTarget TxT",
            "DocumentStatistics": {
                "PageCount": 300,
                "TableCount": 60,
                "ImageCount": 10,
                "ObjectCount": 0,
                "ParagraphCount": 2880,
                "WordCount": 78680,
                "CharacterCount": 485920,
                "NonWhitespaceCharacterCount": 411520
            },
            "EditingCycles":12,
            "EditingDuration":12345,
            "Contributor":["Contributor1 TxT","Contributor2 TXT"],
            "Coverage":"Coverage TxT",
            "Identifier":"Identifier TxT",
            "Publisher":["Publisher TxT","Publisher2 TXT"],
            "Relation":["Relation TxT","Relation2 TXT"],
            "Rights":"Rights TxT",
            "Source":"Source TxT",
            "Type":"Type TxT",
            "UserDefinedProperties":[
                {"Add.NewPropName Str": {
                    "type": "string",
                    "value": "this is a string"
                }},
                {"Add.NewPropName Str": {
                    "type": "boolean",
                    "value": false
                }},
                {"Add.NewPropName Bool": {
                    "type": "boolean",
                    "value": true
                }},
                {"Add.NewPropName Numb": {
                    "type": "long",
                    "value": 1245
                }},
                {"Add.NewPropName float": {
                    "type": "float",
                    "value": 12.45
                }},
                {"Add.NewPropName Double": {
                    "type": "double",
                    "value": 124.578
                }},
                {"Delete": "NewPropName Double"}
            ]
        }}
    ]
}
```

To transform a document property you can use the same named commands as the extracted data was named. There are some additional commands for `UserDefinedProperties` to add a remove properties:

| Command | Description |
| --- | --- |
| Delete | <string> It will delete the user defined property. |
| Add.<string> | {"type":<string>,"value":<value>} It adds a new named user defined property overwriting the existing value when already present. The new property will have a type and value. Types are limited, string, boolean, long, float. Date / time related types are not supported. |

Note

The value of the `UserDefinedProperties` (the commands) can be either an array or an object.

Note

Some property values are overwritten when the document is opened:

- `ModifiedBy` and `ModificationDate` are overwritten by any save. (That is why in the screenshot they have wrong values)
- `DocumentStatistics` are recalculated and overwritten when the document is opened, but it does not recalculated on extract.

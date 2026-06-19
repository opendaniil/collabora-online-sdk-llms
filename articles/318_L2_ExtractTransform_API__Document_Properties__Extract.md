---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id5"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id5"
title: "Extract"
canonical_title: "Extract/Transform API / Document Properties / Extract"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Document Properties / Extract"
---
Use `filter=docprops` to extract the document properties.

Example output: (it is pretty printed here):

```
{
    "DocStructure": {
        "DocumentProperties": {
            "Author": "Author TxT",
            "Generator": "Generator TxT",
            "CreationDate": "2024-01-21T14:45:00",
            "Title": "Title TxT",
            "Subject": "Subject TxT",
            "Description": "Description TxT",
            "Keywords": [ ],
            "Language": "en-GB",
            "ModifiedBy": "ModifiedBy TxT",
            "ModificationDate": "2024-05-23T10:05:50.159530766",
            "PrintedBy": "PrintedBy TxT",
            "PrintDate": "0000-00-00T00:00:00",
            "TemplateName": "TemplateName TxT",
            "TemplateURL": "TemplateURL TxT",
            "TemplateDate": "0000-00-00T00:00:00",
            "AutoloadURL": "",
            "AutoloadSecs": 0,
            "DefaultTarget": "DefaultTarget TxT",
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
            "EditingCycles": 12,
            "EditingDuration": 12345,
            "Contributor": [ "Contributor1 TxT", "Contributor2 TXT"],
            "Coverage": "Coverage TxT",
            "Identifier": "Identifier TxT",
            "Publisher": [ "Publisher TxT", "Publisher2 TXT"],
            "Relation": [ "Relation TxT", "Relation2 TXT"],
            "Rights": "Rights TxT",
            "Source": "Source TxT",
            "Type": "Type TxT",
            "UserDefinedProperties": {
                "NewPropName Bool": {
                    "type": "boolean",
                    "value": true
                },
                "NewPropName Numb": {
                    "type": "long",
                    "value": 1245
                },
                "NewPropName Str": {
                    "type": "string",
                    "value": "this is a string"
                },
                "NewPropName float": {
                    "type": "float",
                    "value": 12.45
                }
            }
        }
    }
}
```

The following properties are extracted:

| Property | Description |
| --- | --- |
| Author | The user name who saved the file first time. |
| Generator | Identifies which application was used to create or last modify the document. |
| CreationDate | The date and time when file was first saved. |
| Title | Title of the document. |
| Subject | Subject of the document. Can be used to group documents with similar contents. |
| Description | Comments to help identify the document. |
| Keywords | [string,] Words used to index the content of the document. Can contain white spaces. |
| Language | the default language of the document. |
| ModifiedBy | The user name when the file was last saved in a LibreOffice file format. |
| ModificationDate | The date and time when the file was last saved in a LibreOffice file format. |
| PrintedBy | The user name who printed the file last time. |
| PrintDate | The date and time when the file was last printed. |
| TemplateName | The template that was used to create the file. |
| TemplateURL | The URL of the template from which the document was created. The value is an empty string if the document was not created from a template or if it was detached from the template. |
| TemplateDate | The date and time of when the document was created or updated from the template. |
| AutoloadURL | The URL to load automatically at a specified time after the document is loaded into a desktop frame. An empty URL is valid and describes a case where the document shall be reloaded from its original location. An empty URL together with an AutoloadSecs value of 0 describes a case where no autoload is specified. |
| AutoloadSecs | The number of seconds after which a specified URL is to be loaded after the document is loaded into a desktop. A value of 0 is valid and describes a redirection. A value of 0 together with an empty string as AutoloadURL describes a case where no autoload is specified. |
| DefaultTarget | The name of the default frame into which links should be loaded if no target is specified. |
| DocumentStatistics | Statistics about the document, as separate properties. They will be recalculated and overwritten at document open. PageCount TableCount ImageCount ObjectCount ParagraphCount WordCount CharacterCount NonWhitespaceCharacterCount |
| EditingCycles | The number of times that the file has been saved. |
| EditingDuration | The amount of time that the file has been open for editing since the file was created. The editing time is updated when file saved. |
| Contributor | [string,] Names of the people, organizations, or other entities that have made contributions to the document. |
| Coverage | Time, place, or jurisdiction that the document is relevant to. For example, a range of dates, a place, or an institution that the document applies to. |
| Identifier | Some unique identifier like ISBN. |
| Publisher | [string,] Name of the entity that is making the document available. For example, a company, university, or government body. |
| Relation | [string,] Resources related to the document. For example, a set of volumes the document is part of, or the document’s edition number. |
| Rights | Intellectual property rights associated with the document. For example, a copyright statement, or information about who has permission to access the document. |
| Source | Information about other resources from which the document is derived. For example, the name or identifier of a hard copy that the document was scanned from, or a URL that the document was downloaded from. |
| Type | Information about the category or format of the document. For example, whether the document is a text document, image, or multimedia presentation. |
| UserDefinedProperties | List of user defined properties. Date/Time related types are not supported yet. Their Names, and types will be extracted but their values will not. |

Note

Extraction of `UserDefinedProperties` may retrieve other types, based on what type of document properties it has. Unfortunatelly the different parts of the LibreOffice have a bit different limitations for these types:

- With the recent LibreOffice these 6 types are found within the UI dialog: `string`, `boolean`, `double`, `com.sun.star.util.Date`, `com.sun.star.util.DateTime`, and `com.sun.star.util.Duration`
- There are other ways to make document properties, that can add different types. And probably older versions of LibreOffice allow to add different (deprecated) types as well, that can still be extracted from old documents.
- Unfortunatelly the exact limitation for the possible document property types aren’t well documented. Checking from the source code (when a property is added) hints at what types can be expected in some special cases. Seven more types have been identified: `typelib_TypeClass_FLOAT`, `typelib_TypeClass_HYPER`, `typelib_TypeClass_LONG`, `typelib_TypeClass_SHORT`, `Time`, `DateTimeWithTimezone`, and `DateWithTimezone`.

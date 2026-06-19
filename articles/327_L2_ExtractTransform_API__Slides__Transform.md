---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id12"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id12"
title: "Transform"
canonical_title: "Extract/Transform API / Slides / Transform"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Slides / Transform"
---
Example Transform:

```
{
    "Transforms": {
        "SlideCommands": [
            {"JumpToSlideByName": "Slide 3"},
            {"MoveSlide": 0},
            {"RenameSlide": "Slide3-Renamed"},
            {"DeleteSlide": 2},
            {"JumpToSlide": 2},
            {"DeleteSlide": ""},
            {"JumpToSlide": 1},
            {"DuplicateSlide": ""},
            {"RenameSlide": "Slide1-Duplicated"},
            {"InsertMasterSlide": 1},
            {"RenameSlide": "SlideInserted-1"},
            {"ChangeLayout": 18},
            {"JumpToSlide": "last"},
            {"InsertMasterSlideByName": "Topic Separator white"},
            {"RenameSlide": "SlideInserted-Name"},
            {"ChangeLayoutByName": "AUTOLAYOUT_TITLE_2CONTENT"},
            {"SetText.0": "first"},
            {"SetText.1": "second"},
            {"SetText.2": "third object para1\npara2\npara3"},
            {"EditTextObject.2": [
                {"SelectParagraph": 1},
                {"InsertText": "----\n++++"},
                {"UnoCommand": ".uno:DefaultNumbering"},
                {"SelectText": [0,6,0,12] },
                {"InsertText": "-Inserted-"},
                {"UnoCommand": ".uno:Underline"},
                {"UnoCommand": ".uno:Bold"},
                {"UnoCommand": ".uno:Italic"},
                {"UnoCommand": ".uno:Strikeout"},
                {"UnoCommand": ".uno:Shadowed"},
                {"UnoCommand": ".uno:JustifyPara"},
                {"UnoCommand": ".uno:DefaultBullet"},
                {"UnoCommand": ".uno:SuperScript"},
                {"SelectText": [0,17,0,20]},
                {"UnoCommand": ".uno:SubScript"},
                {"UnoCommand": ".uno:Color {\"Color.Color\":{\"type\":\"long\",\"value\":2777241}}"},
                {"UnoCommand": ".uno:CharBackColor {\"CharBackColor.Color\":{\"type\":\"long\",\"value\":6710886}}"},
                {"SelectParagraph": 1},
                {"UnoCommand": ".uno:CenterPara"},
                {"SelectParagraph": 2},
                {"UnoCommand": ".uno:RightPara"},
                {"SelectParagraph": 3},
                {"UnoCommand": ".uno:LeftPara"}
            ]},
            {"DuplicateSlide": 1},
            {"MoveSlide.2": 6}
        ]
    }
}
```

There is always a *current slide* that most commands do act on, and some commands that change the current slide. By default the current slide is the slide at index 0.

To transform a slide you can use these commands:

| Command | Value | Description |
| --- | --- | --- |
| JumpToSlide | <num> \| "last" | Jump to the slide a index, or to the last slide. The index is 0 based. Using last is useful to just add new slides at the end. |
| JumpToSlideByName | <string> | Jump to the named slide. Be careful with default slide names like “Slide 1”. Those names can change during slide deletion or insertion. |
| InsertMasterSlide | <num> | Insert a new slide after the current slide, based on the master slide at index. Jump to the newly created slide, setting the current slide. |
| InsertMasterSlideByName | <string> | Insert a new slide after the current slide, based on the named master slide. Jump to the newly created slide, setting the current slide. |
| DeleteSlide | NONE \| <num> | Delete the slide at index or if none, the current slide. Will jump to the previous slide, or to the new first slide if this was the first slide. If this is the current slide then it will jump to the previous slide. If needed the index of the current slide will be readjusted so the current slide is unchanged. As there must always be one slide left in the presentation, the last remainind slide can not be deleted. |
| MoveSlide | <num> | Move the the current slide to the new positon. The index the current slide is readjusterd to follow. |
| MoveSlide.<num> | <num> | Move the slide at index to a new position. If the index is the one of the current slide then it is like the previous command. Otherwise the current slide will be unchanged, but its index may be adjusted as needed. |
| DuplicateSlide | NONE \| <num> | Duplicate the slide at index, or if none, the current slide, and jump to this new slide. |
| ChangeLayout | <num> \| <string> | Change the layout of the current slide to the layout with the index or the named layout. For Layout names, you can use these: AUTOLAYOUT_TITLE_CONTENT AUTOLAYOUT_TITLE_CONTENT_OVER_CONTENT AUTOLAYOUT_TITLE_CONTENT_2CONTENT AUTOLAYOUT_TITLE_4CONTENT AUTOLAYOUT_ONLY_TEXT AUTOLAYOUT_TITLE_ONLY AUTOLAYOUT_TITLE_6CONTENT AUTOLAYOUT_TITLE AUTOLAYOUT_TITLE_2CONTENT_CONTENT AUTOLAYOUT_TITLE_2CONTENT_OVER_CONTENT AUTOLAYOUT_TITLE_2CONTENT AUTOLAYOUT_VTITLE_VCONTENT AUTOLAYOUT_VTITLE_VCONTENT_OVER_VCONTENT AUTOLAYOUT_TITLE_VCONTENT AUTOLAYOUT_TITLE_2VTEXT |
| RenameSlide | <string> | Rename the current slide. Use unique names. Two slides cannot have the same name. Default names like “Slide 1”, “Slide 43”, cannot be set. |
| SetText.<num> | <text> | Set the object text as index to text. Supported only on text based objects. |
| MarkObject | <num> | Mark (select) the object at index on the current slide. This allows to use UNO commands that work on selected objects. |
| UnMarkObject | <num> | Unmark (deselect) the object at index on the current slide. |
| UnoCommand | <string> | Call the UNO command. For example .uno:DefaultBullet will toggle the selected paragraphs bullets, to on/off. There are many more uno commands… Not checked yet wich works here and wich not. Be careful with these, some may even break the mechanism of transform. |
| EditTextObject.<num> | array of commands | Start to edit the object <num> on the current slide. It can contain an array of commands to edit the object |

To edit the text object with EditTextObject you can use the following commands:

| Command | Value | Description |
| --- | --- | --- |
| SelectParagraph | <num> | Select the text of paragraph <num> in the edited text object. |
| SelectText | [<num>,<num>, <num>,<num>] | Select text in the edited textobject. Can be used with 0-4 parameter: [1,2,3,4] = select text between 2. character of 1. paragraph and 4 character of 3. para. [1,2,3] = [1,2,3,*] = select text between 2. character of 1. paragraph and last character of 3. paragraph [1,2] = [1,2,1,2] = only position the cursor to 2. character of 1. paragraph. Does not select any text [1] = [1,0,1,*] = select all text in the 1. paragrah [] = [0,0,*,*] = select all text of the object. Where * means the last character or paragraph. |
| InsertText | <string> | Insert text <string> into the actual text object to the selected place. It can insert multiple paragraphs. ("1.\n2." = 2 paragraph text, \n = end of paragraph) If a text is selected, it will replace that If cursor was set without selection, then it will extend the text there. It will select the newly inserted text, so it can be formatted right away |
| UnoCommand | <string> | Call the UNO command. Same as UnoCommand in SlideCommands Can be used to format the selected text |

Usable (tested) UNO commands by categories:

Toggle (on/off) a format on the selected characters:

- `".uno:Bold"`
- `".uno:Italic"`
- `".uno:Strikeout"`
- `".uno:Shadowed"`
- `".uno:Underline"`
- `".uno:SuperScript"`
- `".uno:SubScript"`
- `".uno:DefaultBullet"` (it will affect whole paragraphs)
- `".uno:DefaultNumbering"` (it will affect whole paragraphs)

Set the horizontal alignment of whole paragraphs:

- `".uno:CenterPara"`
- `".uno:RightPara"`
- `".uno:LeftPara"`
- `".uno:JustifyPara"`

Set color of the selected text:

- `".uno:Color {\"Color.Color\":{\"type\":\"long\",\"value\":2777241}}"` Set the selected text color to 2777241, which is a blue.
- `".uno:CharBackColor {\"CharBackColor.Color\":{\"type\":\"long\",\"value\":6710886}}"` Set the background color of the selected text to 6710886 which is a gray.

Note

There are still more (untested) UNO commands that may can be used.

Note

The value of SlideCommands (the commands) can be an array, or an object.

To obtain the full list of enabled uno commands, you can check: `sfx2/source/control/unoctitm.cxx` under:

```
const std::map<std::u16string_view, KitUnoCommand>& GetKitUnoCommandList()
```

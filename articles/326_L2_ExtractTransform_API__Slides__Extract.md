---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/extract_transform_api.xhtml#id11"
source_file: "docs/extract_transform_api.xhtml"
source_anchor: "id11"
title: "Extract"
canonical_title: "Extract/Transform API / Slides / Extract"
toc_level: "2"
breadcrumbs: "Extract/Transform API / Slides / Extract"
---
Use `filter=slides` to extract the slides.

Example output (pretty printed):

```
{
    "DocStructure": {
        "SlideCount": 7,
        "MasterSlideCount": 8,
        "MasterSlides": {
            "MasterSlide 0": {
                "Name": "Topic_Separator_Purple"
            },
            "MasterSlide 1": {
                "Name": "Content_sidebar_White"
            },
            "MasterSlide 2": {
                "Name": "Topic Separator white"
            },
            "MasterSlide 3": {
                "Name": "Content_sidebar_White_"
            },
            "MasterSlide 4": {
                "Name": "Topic_Separator_Purple_"
            },
            "MasterSlide 5": {
                "Name": "Content_White_Purple_Sidebar"
            }
        },
        "Slides": {
            "Slide 0": {
                "SlideName": "Slide3-Renamed",
                "MasterSlideName": "Content_White_Purple_Sidebar",
                "LayoutId": 3,
                "LayoutName": "AUTOLAYOUT_TITLE_2CONTENT",
                "ObjectCount": 4,
                "Objects": {
                    "Objects 0": {
                        "TextCount": 1,
                        "Texts": {
                            "Text 0": {
                                "ParaCount": 1,
                                "Paragraphs": [
                                    "Friendly Open Source Project"
                                ]
                            }
                        }
                    },
                    "Objects 1": {},
                    "Objects 2": {
                        "TextCount": 1,
                        "Texts": {
                            "Text 0": {
                                "ParaCount": 9,
                                "Paragraphs": [
                                    "Real Open Source",
                                    "100% open-source code",
                                    "Built with LibreOffice technology",
                                    "Built with Free Software technology stacks: primarily C++",
                                    "Runs best on Linux",
                                    "Open Development",
                                    "Anyone can contribute & participate",
                                    "Follow commits and tickets",
                                    "Public community calls - forum has details"
                                ]
                            }
                        }
                    },
                    "Objects 3": {
                        "TextCount": 1,
                        "Texts": {
                            "Text 0": {
                                "ParaCount": 5,
                                "Paragraphs": [
                                    "Focus:",
                                    "a non-renewable resource.",
                                    "Office Productivity & Documents",
                                    "Excited about migrating your\u0001documents",
                                    "Grateful to our partners for solving\u0001other problems."
                                ]
                            }
                        }
                    }
                }
            },
            "Slide 1": {
                "SlideName": "Slide 2",
                "MasterSlideName": "Topic_Separator_Purple",
                "LayoutId": 3,
                "LayoutName": "AUTOLAYOUT_TITLE_2CONTENT",
                "ObjectCount": 1,
                "Objects": {
                    "Objects 0": {
                        "TextCount": 1,
                        "Texts": {
                            "Text 0": {
                                "ParaCount": 3,
                                "Paragraphs": [
                                    "Collabora Online",
                                    "",
                                    "Powerful Online Collaboration"
                                ]
                            }
                        }
                    }
                }
            }
        }
    }
}
```

Extracted properties from the Impress presentation:

| Property | Description |
| --- | --- |
| SlideCount | Number of slides in the presentation. |
| MasterSlideCount | Number of master slides in the presentation. These are real pages in the presentation, only used as template for slides. |
| MasterSlides | List of all the master slides, and some of their data. Currently only extract their name and ID. |
| Slides | List of all the slides, and some of their data. See table below. |

Extracted properties from a slide:

| Property | Description |
| --- | --- |
| SlideName | Name of the slide. If a slide doesn’t have a unique name they are named dynamically like “Slide 1”, “Slide 2”, etc. |
| MasterSlideName | Name of the master slide, this slide is made from. |
| LayoutId | The ID number of the actual layout used. |
| LayoutName | Name of the Layout. |
| ObjectCount | Number of elements in the slide. An elemet can be text, image, video, audio, shape and more… |
| Objects | List of all the elements and some of their data. See table below. |

Extracted properties from an object. Currently only text based information can be extracted:

| Property | Description |
| --- | --- |
| TextCount | Number of texts in this object. For example table objects can have more texts. |
| Texts | List of all the texts. See table below. |

Extracted properties from a text object. Currenbtly only text based information can be extracted:

| Property | Description |
| --- | --- |
| ParaCount | Number of paragraphs in this text object. |
| Paragraphs | Array of all its paragraphs, as simple strings. |

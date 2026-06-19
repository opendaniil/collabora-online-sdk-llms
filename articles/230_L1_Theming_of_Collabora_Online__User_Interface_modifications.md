---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/theming.xhtml#user-interface-modifications"
source_file: "docs/theming.xhtml"
source_anchor: "user-interface-modifications"
title: "User Interface modifications"
canonical_title: "Theming of Collabora Online / User Interface modifications"
toc_level: "1"
breadcrumbs: "Theming of Collabora Online / User Interface modifications"
---
Some parts of the user interface can be hidden or shown based or what the integration needs. This is controlled by:

```
<input name="ui_defaults" value="VALUES" type="hidden"/>
```

during sending the form when the iframe is being set up (similarly as the `access_token`). The VALUES can have a form like:

```
UIMode=notebookbar;TextRuler=false;PresentationStatusbar=false;SpreadsheetSidebar=false
```

With Collabora Online 21.11 use of `notebookbar` has been deprecated use `tabbed`:

```
UIMode=tabbed;TextRuler=false;PresentationStatusbar=false;SpreadsheetSidebar=false
```

where the:

- `UIMode` specifies the general mode of operator. Possible values are `compact` (`classic` is deprecated) or `tabbed` (`notebookbar` is deprecated).
- `Text`, `Presentation` or `Spreadsheet` - are prefixes to identify the component
- `Ruler`, `Statusbar`, `Sidebar` - are the UI parts that can be affected by this. These are boolean. For example `TextRuler=false` will hide the ruler in Writer.
- `SaveAsMode` when set to `group` will set the layout of the “Save As…” command menu to not be a submenu, but rather list the different format as part of the main menu. Any other value is ignored. By default the different formats are in a submenu from the “Save As…” command.
- `SavedUIState` set to `false` allow forcing the above changes if the user had customised the UI by bypassing the saved state. The use of this option should be limited for case where it’s important to always have this default UI.
- `OnscreenKeyboardHint` is tri-state. When set to `true`, assume the device has an onscreen keyboard. When set to `false` assume the device does not have an onscreen keyboard. When unset, the automatic detection is done. This should only used for specific embedding situation with specific devices.
- `TouchscreenHint` works like `OnscreenKeyboardHint` but force Collabora Online to think it is running on a touch device. This really should only be used as a last resort as well.

The `UIMode` can be also updated after Collabora Online iframe is set up based on a user action through a specific PostMessage call [endpoint](257_L0_PostMessage_API.md).

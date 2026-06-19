---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/Using_Python_scripting_in_Collabora_Online.xhtml#sample-scripts"
source_file: "docs/Using_Python_scripting_in_Collabora_Online.xhtml"
source_anchor: "sample-scripts"
title: "Sample Scripts"
canonical_title: "Server macros in Python / Instructions / Sample Scripts"
toc_level: "2"
breadcrumbs: "Server macros in Python / Instructions / Sample Scripts"
---
These scripts are provided as samples and as starting points for experimentation and further development. Users are encouraged to make copies of them and modify as necessary. Note that they may get overwritten when upgrading the Online packages, so making separate copies is highly recommended to avoid losing any changes.

#### SetCellColor:

The first form sets the colour of a cell in the (Calc) document open in the Collabora Online instance. The (zero-based) x and y coordinates of the cell, and the colour (in HTML format, like #A0FFA0 for a very light green) are input fields of the form. In this case the Python file is called `SetCellColor.py`, the function is called `SetCellColor`, and the parameters are the x and y coordinates and the colour.

#### GetNamedRanges:

The second form has no input fields and causes the function GetNamedRanges() in the Python file `NamedRanges.py` to be called. That function takes no parameter but returns a value that is a list of named ranges in the document. The `receiveMessage()` function inserts these into a textarea element.

#### AddNamedRange:

The third form is used to add a named range to the document. The input fields are as expected, the name and the range. The called Python function is `AddNamedRange`, also in `NamedRanges.py`. The JavaScript to call this is somewhat complicated because of different syntax used in the input fields and parameters passed to that Python function. One could as well put the parameter mangling into Python code, of course.

#### DeleteNamedRange:

Finally, and simplest sample, is a form to delete a named range.

#### InsertText:

This script demonstrates inserting a custom text into a Writer document, replacing any selection (if exists), otherwise inserting at the cursor’s position.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/Using_Python_scripting_in_Collabora_Online.xhtml#python-script-files"
source_file: "docs/Using_Python_scripting_in_Collabora_Online.xhtml"
source_anchor: "python-script-files"
title: "Python script files"
canonical_title: "Server macros in Python / Python script files"
toc_level: "1"
breadcrumbs: "Server macros in Python / Python script files"
---
The Python script files containing functions to be called should be located in the LibreOffice installation, in the folder `share/Scripts/python`. (In the LibreOffice sources, they are in `scripting/examples/python`.) Currently, this folder contains `Capitalise.py`, `HelloWorld.py`, `InsertText.py`, `NamedRanges.py`, and `SetCellColor.py` and files that are used by the demo web page `framed.html` (see below), and a few others. Customer-specific Python files should be placed in the same location. After editing script files, the Collabora Online instance must be restarted.

These server-side scripts are read-only during run-time and cannot be modified via Online. Furthermore, the execution of Python scripting is limited to the Python script files in the aforementioned directory, which are prepared in advance. Arbitrary Python code execution is not possible, nor is the execution of dynamically code generated code. These are to guarantee strong security constraints.

Additional security is provided by not enabling the Python script provider by default. To enable it, you need to explicitly install, from the respective customer or [CODE](004_L1_Installation_guide__Installation_from_packages.md) repositories, the following packages:

- `collaboraofficebasis-python-script-provider`, makes it possible to implement `uno` “scripts” in python,
- `collaboraofficebasis-pyuno`, makes it possible to implement `uno` components in python.

The UNO API is documented in the [LibreOffice Developers Guide](https://wiki.documentfoundation.org/Documentation/DevGuide) [https://wiki.documentfoundation.org/Documentation/DevGuide].

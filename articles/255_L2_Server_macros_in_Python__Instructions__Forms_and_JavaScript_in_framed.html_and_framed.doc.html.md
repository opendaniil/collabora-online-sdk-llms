---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/Using_Python_scripting_in_Collabora_Online.xhtml#forms-and-javascript-in-framed-html-and-framed-doc-html"
source_file: "docs/Using_Python_scripting_in_Collabora_Online.xhtml"
source_anchor: "forms-and-javascript-in-framed-html-and-framed-doc-html"
title: "Forms and JavaScript in framed.html and framed.doc.html"
canonical_title: "Server macros in Python / Instructions / Forms and JavaScript in framed.html and framed.doc.html"
toc_level: "2"
breadcrumbs: "Server macros in Python / Instructions / Forms and JavaScript in framed.html and framed.doc.html"
---
`framed.html` and `framed.doc.html` contain a set of small HTML forms and corresponding JavaScript functions that are invoked when a form is submitted. When a form is submitted, in this demonstration case, a corresponding JavaScript function is called. Of course in a real-life use case this could be constructed differently. The JavaScript function fetches the input fields and passes them to the JavaScript functionality of the Collabora Online running inside the iframe using the `postMessage()` standard JavaScript function.

The parameter to `postMessage` is a stringified JSON object. The interesting fields in that are: `MessageId`, which should be `CallPythonScript`, `ScriptFile`, which should be the file name of the Python source file containing the Python function to be called, `Function` which should be the name of the Python function to be called, and `Values` which should be a JSON object containing the (named) parameters to that Python function.

The JavaScript function `receiveMessage()` is set up to handle postMessage() events posted to the HTML page from the iframe, and handle especially those corresponding to return values from called Python functions. Those are distinguished by having a `MessageId` of `CallPythonScript-Result`.

Once `receiveMessage()` knows it is handling a return value from a Python script, it checks the `commandName` field which contains the LibreOffice `vnd.sun.star.script` URL of the called Python function. In the `demonstration framed.html` it is `receiveMessage` that then directly does what is necessary depending on the function called. In a more real-life use case, this could be done in some more generic and complex manner of course.

See the [postmessage API](257_L0_PostMessage_API.md) for more information.

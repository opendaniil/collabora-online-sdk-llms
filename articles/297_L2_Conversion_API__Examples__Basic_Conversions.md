---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#basic-conversions"
source_file: "docs/conversion_api.xhtml"
source_anchor: "basic-conversions"
title: "Basic Conversions"
canonical_title: "Conversion API / Examples / Basic Conversions"
toc_level: "2"
breadcrumbs: "Conversion API / Examples / Basic Conversions"
---
Here you convert a plain text file to OOXML format (docx).

```
curl -k -F "data=@test.txt" https://localhost:9980/cool/convert-to/docx > out.docx
```

> or here is an HTML form, that takes a file to be converted to docx:

```
1<form action="https://localhost:9980/cool/convert-to/docx" enctype="multipart/form-data" method="post">
2 File: <input type="file" name="data"><br/>
3 <input type="submit" value="Convert to DOCX">
4</form>
```

Alternatively you can omit the `<format>`, and instead provide it as another parameter. In this example you convert an OpenDocument Text (odt) file to PDF.

```
curl -k -F "data=@test.odt" -F "format=pdf" https://localhost:9980/cool/convert-to > out.pdf
```

> or here is an HTML form that takes a file and the output format:

```
1<form action="https://localhost:9980/cool/convert-to" enctype="multipart/form-data" method="post">
2 File: <input type="file" name="data"><br/>
3 Format: <input type="text" name="format"><br/>
4 <input type="submit" value="Convert">
5</form>
```

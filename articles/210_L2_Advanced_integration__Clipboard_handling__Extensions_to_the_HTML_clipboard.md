---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/advanced_integration.xhtml#extensions-to-the-html-clipboard"
source_file: "docs/advanced_integration.xhtml"
source_anchor: "extensions-to-the-html-clipboard"
title: "Extensions to the HTML clipboard"
canonical_title: "Advanced integration / Clipboard handling / Extensions to the HTML clipboard"
toc_level: "2"
breadcrumbs: "Advanced integration / Clipboard handling / Extensions to the HTML clipboard"
---
#### HTML marker

When Collabora Online puts HTML to the clipboard, it puts a marker into the body, so it can recognize this content comes from itself and this allows performing a better internal copy:

```
<body>
    <div id="meta-origin" data-coolorigin="...">
        ... original body content ...
    </div>
</body>
```

With this, the copy of complex content like charts is performed in an improved way (on the same COOL instance or between COOL instances), better than what’s possible via HTML export and HTML import.

#### Spreadsheet HTML extensions

Specific to spreadsheets, Collabora Online Calc implements the following HTML extensions to maintain better copy & paste when going via HTML:

- After the own Collabora Online marker, also a `<google-sheets-html-origin/>` marker is emitted to please Google Sheets.
- In case the value of a cell is text, and it should not be recognized as a number, that can be signalled explicitly:

```
<table>
    <tr>
        <td data-sheets-value="{"1":2,"2":"01"}">01</td>
    </tr>
</table>
```

The `data-sheets-value` attribute on the `td` element has a JSON value, where the `1` key is set to `2` to say the type is text, and the `2` key contains the `01` text which won’t be auto-converted to `1` on import.

- In case the value of a cell is boolean, the markup for that is:

```
<table>
    <tr>
        <td data-sheets-value="{"1":4,"4":1}">WAHR</td>
    </tr>
</table>
```

The `data-sheets-value` attribute on the `td` element has a JSON value, where the `1` key is set to `4` to say the type is boolean, and the `4` key contains 1, so even a localized `TRUE` value is recognized on export. `0` can be used to express `FALSE`.

- Formatted numbers can have metadata to express their float values:

```
<table>
    <tr>
        <td data-sheets-value="{"1":3,"3":1000}" data-sheets-numberformat="{"1":2,"2":"#,##0.00","3":1}">1,000.00</td>
    </tr>
</table>
```

The `data-sheets-value` attribute on the `td` element has a JSON value, where the `1` key is set to `3` to say the type is float, and the `3` key contains the original number. Additionally, the `data-sheets-numberformat` attribute also contains a JSON value. The `1` key is set to `2` to describe a number format, the `2` key contains the actual number format.

This allows copying not only the formatted number, but also the generator float value and its number format.

- In case the float number of a cell is a result of a formula, the original formula can be also described:

```
<table>
    <tr>
        <td data-sheets-value="{"1":3,"3":1}">1</td>
        <td data-sheets-value="{"1":3,"3":2}">2</td>
        <td data-sheets-value="{"1":3,"3":3}" data-sheets-formula="=SUM(R[0]C[-2]:R[0]C[-1])">3</td>
    </tr>
</table>
```

The `data-sheets-formula` attribute on the `td` element contains the formula, grammar is R1C1 reference style.

- In case one or multiple cells are copied, then one `table` element, one or more `tr` elements and one or more `td` elements are to be used. If a single cell is copied, then the above `data-*` attributes can be also emitted on a `span` element:

```
<span data-sheets-value="{"1":3,"3":3}" data-sheets-formula="=SUM(R[0]C[-2]:R[0]C[-1])">3</span>
```

This `<span>` syntax is read, but not written by Collabora Online.

Google Sheets seems to not publish a specification for their HTML extensions. We figured out, that the markup is something like the above. Comments regarding this markup are welcome on the `devel@documentliberation.org` mailing list.

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#options-export-filter-options"
source_file: "docs/conversion_api.xhtml"
source_anchor: "options-export-filter-options"
title: "options – Export Filter Options"
canonical_title: "Conversion API / Optional Parameters / options – Export Filter Options"
toc_level: "2"
breadcrumbs: "Conversion API / Optional Parameters / options – Export Filter Options"
---
With the `options` parameter it is possible to pass a large variety of export filter options. The supported value strings depend on the output format. In some cases the value is a JSON, that allows to pass a complicated option set to the filter in a maintainable manner.

#### PDF Filter Options

In the interactive PDF export options dialog there are many options, and it is also possible to set any of them in the JSON payload of the `options` parameter. There are also a few options, that are not available on the graphical user interface, but can be set via this API.

For example to set the range of the exported pages to export from page 2 to the end of the document, the following JSON should be sent:

```
{
    "PageRange": {
        "type": "string",
        "value": "2-"
    }
}
```

See PDF Export for more usage examples.

##### Options from the General tab of PDF Export dialog

For more information please refer to [Collabora Office Help – Export as PDF – General tab](https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_general.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_general.html].

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| PageRange | string | 1,3,5-6 | Export page range |
| UseLosslessCompression | boolean | true | Lossless compression of images |
| Quality | long | 90 | JPEG compression quality in % |
| ReduceImageResolution | boolean | true | Whether to reduce image resolution |
| MaxImageResolution | long | 75 | When ReduceImageResolution is true, this sets the maximal image resolution in DPI. Accepted values are: 75, 150, 300, 600, 1200. The default is 300. |
| Watermark | string | e.g. DRAFT, CONFIDENTIAL etc. | Draws a transparent watermark across each page |
| WatermarkColor | long | 255 | The red (R), green (G), blue (B) and transparency (T) values can be 0-255. The value is calculated as T<<24+R<<16+G<<8+B. |
| WatermarkFontName | string | Helvetica | The name of the font to be used |
| WatermarkFontHeight | long | 80 | Font size of watermark text in points. By default the text is resized to fit the page. |
| WatermarkRotateAngle | long | 450 | The rotation angle of watermark text in 1/10th of degree |
| TiledWatermark | string | e.g. DRAFT, CONFIDENTIAL etc. | This type of watermark is drawn across “tiles” of a document. A tile is e.g. 256×256 px area. Color, font, and rotation cannot be set via API. |
| SelectPdfVersion | long | 20 | By default the output is PDF 1.7, but other versions of the PDF standard can be forced. The possible values are 1, 2, 3, 4, 15, 16, 17, 20 for PDF/A-1b, PDF/A-2b, PDF/A-3b, PDF/A-4, PDF 1.5, PDF 1.6, PDF 1.7 and PDF 2.0 respectively. |
| PDFUACompliance | boolean | true | Universal Accessibility (PDF/UA) |
| IsAddStream | boolean | true | Hybrid PDF (embed ODF file) |
| ExportFormFields | boolean | true | Create PDF form |
| FormsType | string | FDF | Submit format: FDF, PDF, HTML or XML |
| AllowDuplicateFieldNames | boolean | true | Allow duplicate field names |
| UseTaggedPDF | boolean | true | Tagged PDF (add document structure) |
| ExportBookmarks | boolean | true | Export outlines |
| ExportNotes | boolean | true | Comments as PDF annotations |
| ExportNotesInMargin | boolean | true | Comments in margin |
| ExportNotesPages | boolean | true | Export notes pages (Impress) |
| ExportOnlyNotesPages | boolean | true | Export only notes pages, not slides (Impress) |
| ExportHiddenSlides | boolean | true | Export hidden slides/pages (Impress/Draw) |
| IsSkipEmptyPages | boolean | false | Export automatically inserted empty pages (Writer) – true = don’t export, false = export |
| ExportPlaceholders | boolean | true | Export placeholders (Writer) |
| SinglePageSheets | boolean | true | Whole sheet export |
| UseReferenceXObject | boolean | true | Use reference XObjects |
| ExportTrackedChanges | boolean |  | New in version 25.04.5.1. When present, explicitly controls the visibility of tracked changes in the produced document: true = show tracked changes, false = hide them (show the result as if all changes were accepted). If absent, the document settings are used. Not present on the GUI. |

##### Options from the Initial View tab of PDF Export dialog

For more information please refer to [Collabora Office Help – Export as PDF – Initial View tab](https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_initial_view.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_initial_view.html].

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| InitialView | long | 1 | 0 – Page only, 1 – Outline and page, 2 – Thumbnails and page |
| InitialPage | long | 2 | Set the page number of initial page. |
| Magnification | long | 3 | 0 – Default zoom, 1 – Fit in window, 2 – Fit width, 3 – Fit visible, 4 – Custom zoom factor |
| Zoom | long | 85 | Zoom level a PDF document is opened with, when Magnification is set to 4. |
| PageLayout | long | 2 | 0 – Default, 1 – Single page, 2 – Continuous, 3 – Continuous facing |
| FirstPageOnLeft | boolean | true | First page is left |

##### Options from the User Interface tab of PDF Export dialog

For more information please refer to [Collabora Office Help – Export as PDF – User Interface tab](https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_user_interface.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_user_interface.html].

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| ResizeWindowToInitialPage | boolean | true | Resize window to initial page |
| CenterWindow | boolean | true | Center window on screen |
| OpenInFullScreenMode | boolean | true | Open in full screen mode |
| DisplayPDFDocumentTitle | boolean | true | Display document title in window title of PDF viewer application |
| HideViewerMenubar | boolean | true | Hide menubar |
| HideViewerToolbar | boolean | true | Hide toolbar |
| HideViewerWindowControls | boolean | true | Hide window controls |
| OpenBookmarkLevels | long | 2 | Specifies how many bookmark levels should be opened in the reader application when the PDF gets opened. -1 means all levels. |
| UseTransitionEffects | boolean | true | Use transition effects (Impress) |

##### Options from the Links tab of PDF Export dialog

For more information please refer to [Collabora Office Help – Export as PDF – Links tab](https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_links.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_links.html].

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| ExportBookmarksToPDFDestination | boolean | true | Export bookmarks as named destinations |
| ConvertOOoTargetToPDFTarget | boolean | true | Convert document references to PDF targets |
| ExportLinksRelativeFsys | boolean | false | Export URLs relative to file system |
| PDFViewSelection | long | 1 | How to treat cross-document links: 0 – default mode, 1 – Open with PDF reader application, 2 – Open with internet browser |

##### Options from the Security tab of PDF Export dialog

For more information please refer to [Collabora Office Help – Export as PDF – Security tab](https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_security.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/01/ref_pdf_export_security.html].

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| EncryptFile | boolean | true | Whether to encrypt the PDF file. It has to be set together with DocumentOpenPassword. |
| DocumentOpenPassword | string |  | Password to open the PDF document |
| PermissionPassword | string |  | Password to change PDF permissions |
| Printing | long | 1 | Specifies what printing is allowed. 0 – Not permitted, 1 – Low resolution (150 dpi), 2 – High resolution |
| Changes | long | 1 | Specifies the change allowed to the document. 0 – Not permitted, 1 – Inserting, deleting, and rotating pages, 2 – Filling in form fields, 3 – Commenting, filling in form fields, 4 – Any, except extracting pages |
| EnableCopyingOfContent | boolean | false | Enable copying of content |
| EnableTextAccessForAccessibilityTools | boolean | false | Enable text access for accessibility tools |

##### Options for Digital Signatures

It is possible to digitally sign a PDF document via the conversion API, but it is a bit different than interactive document signing. (See [Document signing](162_L0_Advanced_integration.md).) The signing certificate and its key, and the CA certificate have to be passed as strings (PEM format) to the endpoint. The first four parameters are mandatory.

| Name | Type | Example value | Description |
| --- | --- | --- | --- |
| SignPDF | boolean | true | Set this true when you want to digitally sign the exported PDF |
| SignCertificateCertPem | string |  | The signing certificate in PEM format |
| SignCertificateKeyPem | string |  | The key for the signing certificate in PEM format |
| SignCertificateCaPem | string |  | The CA certificate of the signing certificate in PEM format |
| SignatureLocation | string | Cambridge, UK | Optional location information about the digital signature, that will be embedded into the PDF |
| SignatureReason | string | I am approving this document | Optional reason why you digitally signed this PDF |
| SignatureContactInfo | string | John Doe <john.doe@example.com> | Optional contact information of the signer of the document |
| SignaturePassword | string |  | The password used for protecting the private key associated with the selected certificate |
| SignatureTSA | string | https://freetsa.org/tsr | URL of the Time Stamp Authority. If not given, the signature will not be timestamped, but will use the current time from the Collabora Online server. |

#### CSV Export Filter Options

The CSV export filter options can be specified either in the legacy positional token format or as JSON. The legacy format is described in detail on the [Collabora Office Help – CSV Filter Options page](https://help.collaboraoffice.com/latest/en-US/text/shared/guide/csv_params.html) [https://help.collaboraoffice.com/latest/en-US/text/shared/guide/csv_params.html]. For example `options=44,34,76` sets the field separator to `,`, the text delimiter to `"`, and the character set to UTF-8.

New in version 25.04.9.3.

When `options` starts with `{`, it is parsed as JSON. The following properties are supported:

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| FieldSeparator | string | , | Field separator character |
| TextDelimiter | string | " | Text quoting character. Use an empty string for no quoting. |
| CharacterSet | string | UTF-8 | Character set name (e.g. UTF-8, ISO-8859-1, Windows-1252) |
| QuoteAllText | boolean | false | Quote all text cells, not just those that need quoting |
| SaveAsShown | boolean | false | Export numbers as displayed (formatted) rather than with full precision |
| SaveNumberAsSuch | boolean | true | Save number cells as numbers. When false, numbers are quoted as text. |
| SaveFormulas | boolean | false | Export formulas instead of their computed values |
| RemoveSpace | boolean | false | Remove leading and trailing spaces |
| EvaluateFormulas | boolean | true | Evaluate formulas before exporting |
| IncludeBOM | boolean | false | Include a byte-order mark in the output |
| Sheet | string or long |  | Sheet to export: a 1-based sheet number, or a sheet name. When omitted, the active sheet is exported. Use 0 for the active sheet. |

See CSV Export for usage examples.

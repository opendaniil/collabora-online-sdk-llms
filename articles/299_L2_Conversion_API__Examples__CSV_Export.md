---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#csv-export"
source_file: "docs/conversion_api.xhtml"
source_anchor: "csv-export"
title: "CSV Export"
canonical_title: "Conversion API / Examples / CSV Export"
toc_level: "2"
breadcrumbs: "Conversion API / Examples / CSV Export"
---
#### Export a specific sheet as tab-separated values

Assuming `input.xlsx` has a second sheet (“Sheet2”) with:

```
┌───────┬────────┐
│ Item  │ Price  │
├───────┼────────┤
│ Apple │  1.20  │
│ Bread │  3.50  │
└───────┴────────┘
```

```
curl -k -F "data=@input.xlsx" -F "format=csv" \
     -F 'options={"FieldSeparator":{"type":"string","value":"\t"},"Sheet":{"type":"long","value":"2"}}' \
     https://localhost:9980/cool/convert-to > out.csv
```

`out.csv`:

```
Item→Price
Apple→1.2
Bread→3.5
```

#### Export a sheet by name with semicolon separator and UTF-8 BOM

Assuming `input.xlsx` has a sheet named “Sales Data” with:

```
┌────────┬─────────┐
│ Region │ Revenue │
├────────┼─────────┤
│ North  │  45000  │
│ South  │  32000  │
└────────┴─────────┘
```

```
curl -k -F "data=@input.xlsx" -F "format=csv" \
     -F 'options={"FieldSeparator":{"type":"string","value":";"},"Sheet":{"type":"string","value":"Sales Data"},"IncludeBOM":{"type":"boolean","value":"true"}}' \
     https://localhost:9980/cool/convert-to > out.csv
```

`out.csv` (with UTF-8 BOM):

```
Region;Revenue
North;45000
South;32000
```

#### Export formulas instead of computed values

Assuming `input.xlsx` contains:

```
┌───┬───┬──────────┐
│ A │ B │    C     │
├───┼───┼──────────┤
│ 3 │ 7 │ =A1+B1   │
│ 5 │ 2 │ =A2*B2   │
└───┴───┴──────────┘
```

```
curl -k -F "data=@input.xlsx" -F "format=csv" \
     -F 'options={"SaveFormulas":{"type":"boolean","value":"true"}}' \
     https://localhost:9980/cool/convert-to > out.csv
```

`out.csv`:

```
3,7,=A1+B1
5,2,=A2*B2
```

#### Export with full numeric precision (not as displayed)

Assuming a cell in `input.xlsx` displays `3.14` but internally stores `3.14159265358979`:

```
curl -k -F "data=@input.xlsx" -F "format=csv" \
     -F 'options={"SaveAsShown":{"type":"boolean","value":"false"}}' \
     https://localhost:9980/cool/convert-to > out.csv
```

`out.csv` (full precision):

```
3.14159265358979
```

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#csv-import"
source_file: "docs/conversion_api.xhtml"
source_anchor: "csv-import"
title: "CSV Import"
canonical_title: "Conversion API / Examples / CSV Import"
toc_level: "2"
breadcrumbs: "Conversion API / Examples / CSV Import"
---
#### Import a tab-separated CSV file and convert to XLSX

`input.tsv`:

```
Name→Score→Grade
Alice→95→A
Bob→82→B
```

```
curl -k -F "data=@input.tsv" -F "format=xlsx" \
     -F 'infilterOptions={"FieldSeparator":{"type":"string","value":"\t"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx`:

```
┌───────┬───────┬───────┐
│ Name  │ Score │ Grade │
├───────┼───────┼───────┤
│ Alice │    95 │ A     │
│ Bob   │    82 │ B     │
└───────┴───────┴───────┘
```

#### Import a semicolon-separated German CSV file

`input.csv`:

```
Datum;Betrag;Beschreibung
15.01.2024;1.234,56;Miete
20.02.2024;45,90;Strom
```

```
curl -k -F "data=@input.csv" -F "format=xlsx" \
     -F 'infilterOptions={"FieldSeparator":{"type":"string","value":";"},"CharacterSet":{"type":"string","value":"Windows-1252"},"Language":{"type":"string","value":"de-DE"},"DetectSpecialNumber":{"type":"boolean","value":"true"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx` (dates and numbers correctly parsed with German locale):

```
┌────────────┬──────────┬──────────────┐
│ Datum      │   Betrag │ Beschreibung │
├────────────┼──────────┼──────────────┤
│ 2024-01-15 │  1234.56 │ Miete        │
│ 2024-02-20 │    45.90 │ Strom        │
└────────────┴──────────┴──────────────┘
```

#### Import columns as text to preserve leading zeros

`input.csv`:

```
00501,New York,10.50
02101,Boston,25.00
```

```
curl -k -F "data=@input.csv" -F "format=xlsx" \
     -F 'infilterOptions={"ColumnFormat":{"type":"string","value":"1/2/2/1/3/1"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx` (zip codes preserved as text with leading zeros):

```
┌───────┬──────────┬───────┐
│ Zip   │ City     │ Price │
├───────┼──────────┼───────┤
│ 00501 │ New York │ 10.50 │
│ 02101 │ Boston   │ 25.00 │
└───────┴──────────┴───────┘
```

#### Import a fixed-width file

`input.txt` (columns padded with spaces to fixed positions at character offsets 0, 10, and 20):

```
00501     New York  1500.00
02101     Boston    2300.50
```

```
curl -k -F "data=@input.txt" -F "format=xlsx" \
     -F 'infilterOptions={"FixedWidth":{"type":"boolean","value":"true"},"ColumnFormat":{"type":"string","value":"0/2/10/1/20/1"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx` (first column imported as text to preserve leading zeros, others as numbers):

```
┌───────┬──────────┬─────────┐
│ Zip   │ City     │  Amount │
├───────┼──────────┼─────────┤
│ 00501 │ New York │ 1500.00 │
│ 02101 │ Boston   │ 2300.50 │
└───────┴──────────┴─────────┘
```

#### Skip header rows and import starting from row 3

`input.csv`:

```
Report generated 2024-03-15
Confidential
Name,Amount
Alice,100
Bob,200
```

```
curl -k -F "data=@input.csv" -F "format=xlsx" \
     -F 'infilterOptions={"StartRow":{"type":"long","value":"3"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx` (first two lines skipped):

```
┌───────┬────────┐
│ Name  │ Amount │
├───────┼────────┤
│ Alice │    100 │
│ Bob   │    200 │
└───────┴────────┘
```

#### Import with quoted fields treated as text

`input.csv`:

```
ID,Code
1,"007"
2,"00042"
```

```
curl -k -F "data=@input.csv" -F "format=xlsx" \
     -F 'infilterOptions={"QuotedFieldAsText":{"type":"boolean","value":"true"}}' \
     https://localhost:9980/cool/convert-to > out.xlsx
```

`out.xlsx` (quoted values kept as text, leading zeros preserved):

```
┌────┬───────┐
│ ID │ Code  │
├────┼───────┤
│  1 │ 007   │
│  2 │ 00042 │
└────┴───────┘
```

---
source_epub: "CO-SDK-manual.epub"
source_href: "docs/conversion_api.xhtml#csv-to-csv-conversions"
source_file: "docs/conversion_api.xhtml"
source_anchor: "csv-to-csv-conversions"
title: "CSV-to-CSV Conversions"
canonical_title: "Conversion API / Examples / CSV-to-CSV Conversions"
toc_level: "2"
breadcrumbs: "Conversion API / Examples / CSV-to-CSV Conversions"
---
New in version 25.04.9.3.

These examples use both `options` (export) and `infilterOptions` (import) in the same request.

#### Convert a semicolon-separated CSV to a tab-separated CSV

`input.csv`:

```
Name;Amount;City
Alice;1500;London
Bob;2300;Paris
```

```
curl -k -F "data=@input.csv" -F "format=csv" \
     -F 'infilterOptions={"FieldSeparator":{"type":"string","value":";"}}' \
     -F 'options={"FieldSeparator":{"type":"string","value":"\t"}}' \
     https://localhost:9980/cool/convert-to > out.tsv
```

`out.tsv`:

```
Name→Amount→City
Alice→1500→London
Bob→2300→Paris
```

#### Clean up a CSV: preserve leading zeros, skip a column, change delimiter

Import with leading-zero preservation on the zip code column (column 1 as text), skip an unwanted notes column (column 3), and change the delimiter from comma to tab:

`input.csv`:

```
00501,New York,imported 2024-01-15,10.50
02101,Boston,imported 2024-02-20,25.00
90210,Beverly Hills,imported 2024-03-10,99.99
```

```
curl -k -F "data=@input.csv" -F "format=csv" \
     -F 'infilterOptions={"ColumnFormat":{"type":"string","value":"1/2/2/1/3/9/4/1"}}' \
     -F 'options={"FieldSeparator":{"type":"string","value":"\t"}}' \
     https://localhost:9980/cool/convert-to > out.tsv
```

`out.tsv` (zip codes preserve leading zeros, notes column skipped):

```
00501→New York→10.5
02101→Boston→25
90210→Beverly Hills→99.99
```

---
description: "P1: Tabelkolommen berekenen en regex-afhankelijkheid controleren"
---

# P1: Tabelkolommen berekenen en regex-afhankelijkheid controleren

**Calculate Columns** rekent met twee kolommen van dezelfde rij en schrijft de resultaatkolom. **Calculate in / CALC_COLUMNS_REGEX** voegt een regexvoorwaarde op een derde kolom toe. De regex bepaalt hier of wordt gerekend; zij haalt geen tekst op en vervangt geen tekst. De vroegere vervangingsuitleg beschrijft deze kaart niet.

Voorbeeld: `QTY=2`, `PRICE=10`, bewerking `*`, resultaat `TOTAL=20.0`. Gebruik voor de regexvariant `TYPE` en patroon `^A$`. Een A-rij wordt berekend. Voor een niet-passende B-rij schrijft de onderzochte code een leeg resultaat; een bestaande TOTAL blijft niet automatisch behouden.

De rekenhulp rondt getallen op vier decimalen af. Een afzonderlijke lege operand kan 0 worden; twee lege teksten geven leeg. Met `+` kan niet-numerieke tekst worden samengevoegd. `10/0` veroorzaakt in de onderzochte hulp een fout. Valideer getallen en vereiste cellen vooraf en maak een foutroute.

Bewaar een volledige voor/na-tabel: twee passende rijen, één niet-passende rij, lege invoer, ongeldige tekst en delen door nul. Verbind afhankelijke A→B-berekeningen expliciet en controleer de bijgewerkte waarde die B leest. Vergelijk elke rij en bestaande andere kolommen, niet alleen de documentstatus.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `calc_columns` · v2

Identiteit: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identiteit: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)

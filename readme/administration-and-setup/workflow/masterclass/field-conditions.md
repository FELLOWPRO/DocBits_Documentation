---
description: "P1: Field is, Docfield is of Compare two Fields kiezen"
---

# P1: Field is, Docfield is of Compare two Fields kiezen

Gebruik **Field is** voor leegte, **Docfield is** voor vergelijking met een ingestelde waarde en **Compare two Fields** voor twee waarden van het huidige document. Een leegtecontrole bewijst niet dat het veld in de indeling bestaat of zakelijk geldig is.

Bij Field is v2 gelden een ontbrekend veld, `null`, lege tekst, uitsluitend spaties en booleaanse `false` als leeg. Getal `0`, tekst `"0"` en tekst `"false"` zijn niet leeg. Deze acht gevallen zijn met volledige documentgegevens in Dev getest. Gebruik een expliciete checkboxvoorwaarde als waar/onwaar de zakelijke keuze is.

`"1000.01"` in een AMOUNT-veld verschilt van dezelfde tekens in een tekstveld. Het v2-oefenpakket gebruikt AMOUNT en decimale punten in JSON. Controleer technische sleutel, indeling en type samen. Een vertaalde naam is geen technische sleutel en een valutateken is geen getal.

Stel voor Compare two Fields linkerveld, operator en rechterveld in. Controleer verenigbare types en beide invoeren; ontbrekende of onvergelijkbare gegevens zijn een gegevensfout, geen bewezen ongelijkheid. Herhaal positief, negatief, ontbrekende invoer en exacte grens. Leg waarde, type en gekozen uitgang vast.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `condition_docfield_status` · v2

Identiteit: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identiteit: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identiteit: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Bewijs en grenzen

Geselecteerde kaart- en knoopresultaten zijn met synthetische gegevens in Advanced Test gecontroleerd. Antwoorden staan in het oefenpakket. Documentacties zijn gesimuleerd en bewijzen geen opgeslagen documentuitvoering of externe aflevering.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)

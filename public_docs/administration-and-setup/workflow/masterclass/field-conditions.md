---
description: "Field is, Docfield is of Compare two Fields kiezen"
---

# Field is, Docfield is of Compare two Fields kiezen

Drie voorwaardekaarten lijken in de ontwerper op elkaar, en hun verschil bepaalt wat een regel werkelijk kan opvangen. Deze pagina helpt u de juiste te kiezen en geeft daarna drie korte oefeningen die laten zien wat elke kaart teruggeeft. Aan het eind kunt u "leeg" van het getal `0`, "onwaar" van "ontbrekend" en een niet vervulde voorwaarde van een fout onderscheiden; technische `null` telt als leeg, het getal `0` niet.

Doe de oefeningen in Advanced Test, in uw eigen testorganisatie, met een synthetisch document. Hier wordt geen klantdocument aangeraakt.

## Welke kaart hebt u nodig?

| Als u wilt controleren ... | Gebruik | Kaart en versie |
| --- | --- | --- |
| of een veld überhaupt een waarde heeft | **Field is** | `condition_docfield_status` v2 |
| een veld tegen een waarde die u zelf invoert | **Docfield is** | `condition_docfield_operator_value` v2 |
| twee velden van hetzelfde document tegen elkaar | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Alle drie zijn voorwaarden: ze geven een resultaat terug en veranderen niets aan het document. Een controle op de lege status bewijst niet dat een veld in de layout bestaat of dat de inhoud ervan zakelijk geldig is. De afzonderlijke kaartpagina's noemen elke instelling: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) en [Compare two Fields](../and/document-field/compare-two-fields.md).

## Oefening 1: uitzoeken wat "leeg" betekent

**Doel:** weten welke waarden Field is versie 2 als leeg behandelt.

1. Voeg **Field is** versie 2 toe aan een regel in uw testorganisatie en kies een tekstveld uit uw layout.
2. Zet de veldstatus op `field_empty` (Empty or missing).
3. Voer acht Advanced Test-gevallen uit met volledige documentgegevens: ontbrekend veld, `null`, lege tekst `""`, alleen spaties `" "`, boolean `false`, getal `0`, tekst `"0"` en tekst `"false"`.

**Klaar wanneer:** de eerste vijf gevallen `field_empty=success` opleveren en de laatste drie `field_empty=failed_condition`. Deze acht gevallen zijn in Dev met volledige documentgegevens getest.

Getal `0`, tekst `"0"` en tekst `"false"` zijn waarden, geen afwezigheid. Als waar of onwaar uw zakelijke beslissing is, gebruik dan een expliciete selectievakje-voorwaarde in plaats van het veld op leegte te testen.

## Oefening 2: één veld met een waarde vergelijken

**Doel:** zien hoe de operator en het veldtype het antwoord veranderen.

1. Kies een numeriek veld zoals `total_amount`, de operator `gt` en de waarde `1000`.
2. Test `1000`, `1000.01`, een ontbrekend veld en een ongeldige waarde.

**Klaar wanneer:** `1000` `failed_condition` oplevert, omdat `gt` strikt groter betekent, `1000.01` `success` oplevert en een ontbrekende of ongeldige invoer `error` teruggeeft.

## Oefening 3: twee velden vergelijken

**Doel:** weten wanneer twee waarden worden vergeleken en wanneer de kaart ze helemaal niet kan vergelijken.

1. Stel het linkerveld, de operator en het rechterveld in. Gebruik twee velden met passende typen.
2. Test gelijke waarden, verschillende waarden en één ontbrekende invoer.

**Klaar wanneer:** gelijke waarden aan `eq` voldoen, verschillende waarden `failed_condition` opleveren en een ontbrekende invoer `error` teruggeeft in plaats van een bewezen ongelijkheid.

## Wat de drie resultaten betekenen

| Resultaat | Wat het u zegt |
| --- | --- |
| `success` | De kaart heeft de waarden vergeleken en de voorwaarde was vervuld. |
| `failed_condition` | De kaart heeft de waarden vergeleken en de voorwaarde was niet vervuld. `0` en `"0"` eindigen hier bij een controle op de lege status. |
| `error` | De kaart kon niet vergelijken, bijvoorbeeld omdat een waarde ontbreekt of ongeldig is. Een fout is niet hetzelfde antwoord als "ongelijk". |

## Het type hoort bij de vergelijking

Een waarde `"1000.01"` in een AMOUNT-veld is niet hetzelfde als dezelfde tekens in een tekstveld. Het v2-oefenpakket gebruikt AMOUNT en decimale punten in JSON. Controleer de technische veldsleutel, de layout en het type samen. Een vertaald label is geen technische sleutel, en een valutasymbool is geen numerieke waarde.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven parameters van afzonderlijke kaarten, niet een volledig importeerbare workflow. Vervang YOUR\_\* door uw eigen testkeuzes. De verborgen aanroeper-ID beheert de ontwerper. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer beschikbare versies en rechten in uw eigen organisatie.

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

| Geval | Invoer / opzet | Verwacht resultaat |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Bewijs en grenzen

Geselecteerde kaart- en knooppuntresultaten zijn met synthetische gegevens in Advanced Test gecontroleerd. De antwoorden staan in het oefenpakket. Documentacties zijn gesimuleerd; deze tests bewijzen geen opgeslagen documentuitvoering en geen externe levering.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)

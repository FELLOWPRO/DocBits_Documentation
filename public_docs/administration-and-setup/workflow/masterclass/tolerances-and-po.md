---
description: "P1: Referentie voor toleranties en PO-vergelijkingen vastleggen"
---

# P1: Referentie voor toleranties en PO-vergelijkingen vastleggen

Een procentuele tolerantie hangt af van de **referentiezijde**. In de onderzochte PO-kaart v5 vergelijkt `document_po` documentwaarde met bestelwaarde; de bestelling is de procentbasis. `po_document` draait vergelijking en basis om. De zes toegestane richtingen omvatten ook de ontvangen waarde. Kies richting, operator en Any/All expliciet.

Voorbeeld: bestelling 100, document 102.02, gelijkheid met 2 procent. Met bestelreferentie is het bereik 98–102: daarbuiten. Met documentreferentie is het 99.9796–104.0604: bestelwaarde 100 ligt erin. Document 102 ligt precies op de inbegrepen bovengrens van de eerste richting. Een absolute tolerantie 2 gebruikt de eenheid van de vergeleken waarde.

De kaart normaliseert prijzen per prijseenheid en gebruikt bestel- of ontvangstgegevens volgens de richting. Controleer koppeling, hoeveelheden en eenheden. Any vereist één passende vergelijking; All alle werkelijk uitgevoerde vergelijkingen. **Geen vergelijkbare regel** is in v5 een gegevensfout, geen automatisch voldane All. Tel ongekoppelde regels afzonderlijk.

Lees bij bestaande workflows opgeslagen versie, richting en operator opnieuw: migraties wijzigden instellingen. Oude namen zijn onvoldoende acceptatiebewijs. Leg waarden, referentie, exacte grens, kleinste overschrijding, precisie, ontbrekende bestelling en ongekoppelde regel vast. Dit rekenvoorbeeld vervangt geen acceptatie met eigen PO-stamgegevens.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven kaartparameters, geen volledig importeerbare workflow. Vervang YOUR_* door eigen testkeuzes. De ontwerper beheert het verborgen aanroeper-ID. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer versies en rechten van uw organisatie afzonderlijk.

### `condition_docfield_operator_docfield_tolerances` · v2

Identiteit: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identiteit: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parameter | Type / keuzes | Voorbeeld |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Zakelijke testgevallen

| Geval | Invoer / configuratie | Verwacht resultaat |
| --- | --- | --- |
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | gegevensfout |
| PO-05 | unmatched_rows>0 | controleer dekking apart |

## Bewijs en grenzen

Parameters en gedrag zijn vergeleken met de Dev-catalogus en onderzochte broncode. Zakelijke testgevallen vormen een acceptatieprocedure. Voor dit hoofdstuk zijn geen persoonlijke goedkeuringen, echte wijzigingen of afleveringen uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)

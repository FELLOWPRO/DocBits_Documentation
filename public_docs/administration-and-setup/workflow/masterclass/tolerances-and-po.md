---
description: "Referentie voor toleranties en PO-vergelijkingen vastleggen"
---

# Referentie voor toleranties en PO-vergelijkingen vastleggen

Een tolerantie van 2 procent is geen vast bedrag. Het is 2 procent van de zijde waarmee u vergelijkt, dus dezelfde factuurregel kan in de ene richting afvallen en in de andere slagen. Deze pagina laat dat zien op één waardepaar, geeft u drie oefeningen om het na te bouwen en noemt daarna de zes vergelijkingsrichtingen en de kaartparameters die u in uw eigen test kunt overnemen.

Doe de oefeningen in Advanced Test, in uw eigen testorganisatie, met een synthetisch document en een gekoppelde bestelling.

## De referentiezijde is de basis

In de onderzochte PO-kaart versie 5 vergelijkt `document_po` de documentwaarde met de bestelwaarde, dus de bestelling is de basis voor een procentuele tolerantie. `po_document` draait zowel de vergelijking als de basis om. De zes toegestane richtingen omvatten ook de ontvangen zijde. Kies richting, operator en Any/All uitdrukkelijk, in plaats van te vertrouwen op wat een opgeslagen kaart nog bevat.

## Oefening 1: dezelfde waarden, twee richtingen

**Doel:** zien hoe uit dezelfde getallen twee verschillende resultaten komen.

1. Maak een gekoppelde bestelling van `100` en een documenteenheidsprijs van `102.02`.
2. Vergelijk met de operator `eq` en een tolerantie van `2` procent, eerst met `document_po`. Verwacht `false`: 2 procent van 100 is 2, dus het gesloten interval loopt van 98 tot 102, en 102.02 ligt 0.02 daarboven.
3. Herhaal hetzelfde geval met `po_document`. Verwacht `true`: 2 procent van 102.02 is 2.0404, het interval loopt van 99.9796 tot 104.0604, en de bestelwaarde 100 valt erbinnen.

**Klaar wanneer:** beide resultaten en beide intervallen zijn genoteerd en u per richting kunt zeggen van welke waarde het percentage is berekend.

Een absolute tolerantie van `2` gedraagt zich anders: die gebruikt de eenheid van de vergeleken waarde en schuift niet mee met de referentie.

## Oefening 2: de exacte grens vinden

**Doel:** weten of de rand van het interval meetelt.

1. Houd `document_po`, `eq` en de tolerantie van 2 procent aan en wijzig de documentwaarde naar `102`.
2. Voer het geval uit en daarna nog eens met `102.01`.

**Klaar wanneer:** `102` `true` oplevert en `102.01` `false`. De grens is inbegrepen: 102 ligt precies op de bovengrens van het interval 98 tot 102.

## Oefening 3: Any, All en de vergeleken regels

**Doel:** weten wat de kaart met meerdere regels doet en wat er gebeurt als er niets te vergelijken valt.

1. Bouw een document met twee regels tegen dezelfde gekoppelde bestelling: één binnen de tolerantie en één erbuiten.
2. Voer de kaart uit met `match_any` en daarna met `match_all`.
3. Voer een document uit zonder enige vergelijkbare regel.

**Klaar wanneer:** `match_any` slaagt op de ene passende regel, `match_all` faalt zodra één vergelijking faalt, en het document zonder vergelijkbare regel een gegevensfout teruggeeft. In versie 5 is dat een fout en geen automatisch vervulde All.

## Welke zijde is de basis?

| Opgeslagen optie | Vergeleken zijde | Referentiezijde (procentbasis) |
| --- | --- | --- |
| `po_document` | Bestelling | Document |
| `received_document` | Ontvangen gegevens | Document |
| `po_received` | Bestelling | Ontvangen gegevens |
| `document_po` | Document | Bestelling |
| `document_received` | Document | Ontvangen gegevens |
| `received_po` | Ontvangen gegevens | Bestelling |

## Controleer voordat u een bestaande workflow vertrouwt

De kaart normaliseert prijzen per prijseenheid en gebruikt afhankelijk van de richting bestel- of ontvangstgegevens, dus controleer eerst de koppeling, de hoeveelheden en de eenheden. Any heeft één passende vergelijking nodig, All elke werkelijk uitgevoerde vergelijking. Niet-gekoppelde regels houdt u apart bij.

Lees bij bestaande workflows de opgeslagen versie, richting en operator opnieuw: migraties hebben vergelijkingsinstellingen gewijzigd, historische labels zijn dus geen toereikend acceptatiebewijs. Leg waarden en referentie vast, plus de exacte grens, de kleinste overschrijding, de afrondingsprecisie, de ontbrekende bestelling en de niet-gekoppelde regel. Deze berekening vervangt geen acceptatie met uw eigen PO-stamgegevens.

## Kaarten en voorbeeldparameters

Deze waarden beschrijven parameters van afzonderlijke kaarten, niet een volledig importeerbare workflow. Vervang YOUR\_\* door uw eigen testkeuzes. De verborgen aanroeper-ID beheert de ontwerper. Catalogus: Dev, DocFlow 2.10.38, 21 oktober 2026; controleer beschikbare versies en rechten in uw eigen organisatie.

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

| Geval | Invoer / opzet | Verwacht resultaat |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | gegevensfout |
| PO-05 | unmatched\_rows>0 | dekking apart controleren |

## Bewijs en grenzen

Parameters en gedrag zijn gecontroleerd tegen de Dev-catalogus en de onderzochte coderevisie. De zakelijke testgevallen zijn een acceptatieprocedure. Persoonlijke goedkeuringen, wijzigingen in echte gegevens en levering zijn voor dit hoofdstuk niet uitgevoerd.

[Verder leren](../workflow-learning-path.md) · [Oefenpakket](../workflow-training-kit.md)

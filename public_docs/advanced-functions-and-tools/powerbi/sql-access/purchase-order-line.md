# Inkooporderregel

## Tabel `public.purchase_order_line`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `po_number`: intern
* `line_number`: intern
* `item_number`: intern
* `quantity`: numeriek
* `unit_price`: numeriek
* `net_amount`: numeriek
* `description`: intern
* `created_on`: tijdstempel met tijdzone
* `po_header_id`: intern
* `erp_id`: intern

### Analyse & Beschrijving

## Technische documentatie voor `public.purchase_order_line` tabel

### Inleiding

De `public.purchase_order_line` tabel slaat gedetailleerde informatie op over individuele regels binnen een inkooporder. Dit omvat gegevens over de bestelde artikelen, hoeveelheden, prijzen en verwijzingen naar de hoofdinkooporder.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de inkooporderregel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden.

#### org\_id

* **Betekenis**: De identificatie van de organisatie waartoe de inkooporderregel behoort.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID-waarden.

#### po\_number

* **Betekenis**: Het nummer van de inkooporder waartoe de regel behoort.
* **Rol**: Referentieveld.
* **Typische inhoud**: Alfanumerieke tekenreeksen (bijv. "PO-2024-001").

#### line\_number

* **Betekenis**: Het volgnummer van de regel binnen de inkooporder.
* **Rol**: Volgordeveld.
* **Typische inhoud**: Gehele getallen (bijv. 1, 2, 3).

#### item\_number

* **Betekenis**: De identificatie of code van het bestelde artikel.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Artikelcodes (bijv. "ART-123").

#### quantity

* **Betekenis**: De bestelde hoeveelheid van het artikel.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Numerieke waarden.

#### unit\_price

* **Betekenis**: De prijs per eenheid van het artikel.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Numerieke waarden.

#### net\_amount

* **Betekenis**: Het nettobedrag voor de regel (Hoeveelheid * Eenheidsprijs).
* **Rol**: Berekend veld.
* **Typische inhoud**: Numerieke waarden.

#### description

* **Betekenis**: Een beschrijving van het bestelde artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekstuele beschrijvingen.

#### created\_on

* **Betekenis**: De datum en tijd waarop de regel is gemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels met tijdzone.

#### po\_header\_id

* **Betekenis**: De identificatie van de inkooporderkop (hoofdrecord).
* **Rol**: Vreemde sleutel, verwijzend naar de inkooporderkoptabel.
* **Typische inhoud**: UUID-waarden.

#### erp\_id

* **Betekenis**: De identificatie van de regel in het externe ERP-systeem.
* **Rol**: Integratieveld.
* **Typische inhoud**: Externe ID's.
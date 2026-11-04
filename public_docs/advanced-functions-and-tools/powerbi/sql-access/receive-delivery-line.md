# Ontvangstleveringsregel

## Tabel `public.receive_delivery_line`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `po_number`: intern
* `line_number`: intern
* `item_number`: intern
* `quantity`: numeriek
* `description`: intern
* `created_on`: tijdstempel met tijdzone
* `po_header_id`: intern
* `delivery_note`: intern
* `received_quantity`: numeriek

### Analyse & Beschrijving

## Technische documentatie voor `public.receive_delivery_line` tabel

### Inleiding

De `public.receive_delivery_line` tabel registreert details over ontvangen goederen of diensten tegen inkooporders. Het wordt gebruikt om leveringen te volgen en te vergelijken met bestellingen (matching).

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor de ontvangstregel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-waarden.

#### org\_id

* **Betekenis**: De identificatie van de organisatie.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID-waarden.

#### po\_number

* **Betekenis**: Het nummer van de bijbehorende inkooporder.
* **Rol**: Referentieveld.
* **Typische inhoud**: Alfanumerieke tekenreeksen.

#### line\_number

* **Betekenis**: Het regelnummer van de inkooporder waarnaar wordt verwezen.
* **Rol**: Referentieveld.
* **Typische inhoud**: Gehele getallen.

#### item\_number

* **Betekenis**: De code van het ontvangen artikel.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Artikelcodes.

#### quantity

* **Betekenis**: De hoeveelheid die op de leveringsbon staat vermeld.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Numerieke waarden.

#### description

* **Betekenis**: Beschrijving van het ontvangen artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst.

#### created\_on

* **Betekenis**: Tijdstempel van aanmaak.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempels.

#### po\_header\_id

* **Betekenis**: ID van de inkooporderkop.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID-waarden.

#### delivery\_note

* **Betekenis**: Het nummer van de leveringsbon of pakbon.
* **Rol**: Referentieveld.
* **Typische inhoud**: Alfanumerieke tekenreeksen.

#### received\_quantity

* **Betekenis**: De daadwerkelijk ontvangen en geaccepteerde hoeveelheid.
* **Rol**: Gegevensveld.
* **Typische inhoud**: Numerieke waarden.
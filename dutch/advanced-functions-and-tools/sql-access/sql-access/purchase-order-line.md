# Inkooporderregel

## Tabel `public.purchase_order_line`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `purchase_order_id`: intern
* `purchase_order_number`: intern
* `line_number`: intern
* `item_id`: intern
* `supplier_item_id`: intern
* `description`: intern
* `quantity`: double precision
* `unit_code`: intern
* `unit_price`: double precision
* `total_amount`: double precision
* `currency`: intern
* `status`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `deleted_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `open_quantity`: double precision
* `received_quantity`: double precision
* `confirmed_quantity`: double precision
* `note`: tekst
* `sub_org_id`: intern
* `sub_line_number`: intern
* `unit_price_per`: double precision
* `buyer_id`: intern
* `buyer_name`: intern
* `unit_code_price`: intern
* `geo_code`: intern
* `promised_delivery_date`: tijdstempel met tijdzone
* `delivery_method`: intern
* `requested_ship_date`: datum
* `received_base_mou_quantity`: double precision
* `extended_amount`: double precision

### Analyse & Beschrijving

## Technische documentatie voor de tabel `public.purchase_order_line`

### Inleiding

De tabel `public.purchase_order_line` is bedoeld voor het opslaan van gedetailleerde informatie over elke orderregel binnen een inkooporder. Ze legt diverse kenmerken van een inkooporderregel vast, zoals artikelgegevens, hoeveelheden, prijzen en statussen. Deze tabel is onmisbaar voor het beheren en volgen van inkooporders en de status van hun afhandeling binnen een organisatie.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elke inkooporderregel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-reeks die de inkooporderregel uniek identificeert.

#### org\_id

* **Betekenis**: Identificatie van de organisatie die aan de inkooporder is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-reeks die naar een organisatie verwijst.

#### purchase\_order\_id

* **Betekenis**: Identificatie van de inkooporder waartoe de orderregel behoort.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-reeks die naar een inkooporder verwijst.

#### purchase\_order\_number

* **Betekenis**: Het nummer dat aan de inkooporder is toegekend.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die het inkoopordernummer weergeeft.

#### line\_number

* **Betekenis**: Het regelnummer van het artikel binnen de inkooporder.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de volgorde van de regel in de inkooporder aangeeft.

#### item\_id

* **Betekenis**: Identificatie van het bestelde artikel.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekenreeks die de artikelcode weergeeft.

#### supplier\_item\_id

* **Betekenis**: Leverancierspecifieke identificatie van het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks, kan null zijn als de leverancier deze niet heeft opgegeven.

#### description

* **Betekenis**: Beschrijving van het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekstuele beschrijving van het artikel.

#### quantity

* **Betekenis**: Het aantal bestelde eenheden.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die de bestelde hoeveelheid aangeeft.

#### unit\_code

* **Betekenis**: Code die de maateenheid van het artikel weergeeft.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die eenheden weergeeft, bijv. 'EA' voor stuks.

#### unit\_price

* **Betekenis**: Prijs per eenheid van het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die de prijs per eenheid weergeeft.

#### total\_amount

* **Betekenis**: Totaalbedrag voor de orderregel (hoeveelheid \* eenheidsprijs).
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die het totaalbedrag weergeeft.

#### currency

* **Betekenis**: Valuta waarin de aankoop wordt gedaan.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de valutacode weergeeft, bijv. 'USD'.

#### status

* **Betekenis**: Huidige status van de inkooporderregel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de status aangeeft, bijv. 'Received', 'Invoiced'.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het item heeft aangemaakt.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een integer die het gebruikers-ID weergeeft.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop het item is aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, kan null zijn als het item nooit is gewijzigd.

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop het item als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie, kan null zijn als het item niet is verwijderd.

#### is\_deleted

* **Betekenis**: Geeft aan of het item als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarde (true/false).

#### open\_quantity

* **Betekenis**: Hoeveelheid die nog niet is ontvangen of gefactureerd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde, doorgaans nul als alles is ontvangen.

#### received\_quantity

* **Betekenis**: Hoeveelheid die is ontvangen.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die de ontvangen hoeveelheid aangeeft.

#### confirmed\_quantity

* **Betekenis**: Hoeveelheid die door de leverancier is bevestigd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde, kan null zijn als er geen bevestiging is.

#### note

* **Betekenis**: Aanvullende opmerkingen over de inkooporderregel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst, kan speciale instructies of opmerkingen bevatten.

#### sub\_org\_id

* **Betekenis**: Identificatie van de suborganisatie die aan de inkooporderregel is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekenreeks, mogelijk null indien niet van toepassing.

#### sub\_line\_number

* **Betekenis**: Subregelnummer binnen de inkooporder.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de volgorde van de subregel weergeeft.

#### unit\_price\_per

* **Betekenis**: Basiseenheidsprijs voor het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die de basiseenheidsprijs weergeeft.

#### buyer\_id

* **Betekenis**: Identificatie van de inkoper die verantwoordelijk is voor de aankoop.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekenreeks die het inkoper-ID weergeeft.

#### buyer\_name

* **Betekenis**: Naam van de verantwoordelijke inkoper.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de naam van de inkoper weergeeft.

#### unit\_code\_price

* **Betekenis**: Eenheidscode met betrekking tot de prijsstelling.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks, vergelijkbaar met unit\_code.

#### geo\_code

* **Betekenis**: Geografische code voor de levering.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die een geografische locatie weergeeft.

#### promised\_delivery\_date

* **Betekenis**: Datum die voor de levering is toegezegd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tijdstempel met tijdzone-informatie.

#### delivery\_method

* **Betekenis**: Leveringswijze voor de inkooporderregel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die de leveringswijze weergeeft.

#### requested\_ship\_date

* **Betekenis**: Gevraagde verzenddatum.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een datumwaarde.

#### received\_base\_mou\_quantity

* **Betekenis**: Ontvangen hoeveelheid in basismaateenheden.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die de ontvangen hoeveelheid in basismaateenheden (MOU) aangeeft.

#### extended\_amount

* **Betekenis**: Uitgebreid bedrag (extended amount) voor de orderregel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een numerieke waarde die het uitgebreide bedrag weergeeft, dat gelijk kan zijn aan total\_amount als er geen kortingen of extra kosten gelden.

# Leveringsontvangstregel

## Tabel `public.receive_delivery_line`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `receive_delivery_id`: intern
* `delivery_number`: intern
* `line_number`: intern
* `item_id`: intern
* `description`: intern
* `shipped_quantity`: double precision
* `status`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `deleted_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `purchase_order`: intern
* `sequence_number`: intern
* `sub_org_id`: intern
* `shipped_quantity_unit_code`: intern
* `packing_slip_quantity`: double precision
* `packing_slip_quantity_unit_code`: intern
* `received_quantity`: double precision
* `received_quantity_unit_code`: intern
* `purchase_order_line_number`: intern
* `status_effective_from`: tijdstempel met tijdzone
* `purchase_order_sub_line_number`: intern
* `invoiced_quantity`: double precision
* `invoice_matching_status`: intern
* `open_quantity`: double precision
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschrijving

## Tabeldocumentatie: `public.receive_delivery_line`

### Inleiding

De tabel `public.receive_delivery_line` lijkt een gedetailleerd register te zijn van lever- en ontvangstregels die horen bij de logistieke en supplychainactiviteiten van een organisatie. Elke rij in de tabel vertegenwoordigt een specifieke regel van een levering en legt details vast zoals de artikelomschrijving, de verzonden en ontvangen hoeveelheden en diverse statusvelden. De tabel is een essentieel onderdeel bij het volgen van de goederenstroom van verzending tot ontvangst, inclusief facturering en orderbeheer.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elke leveringsregel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een unieke, universeel unieke identificator (UUID).

#### org\_id

* **Betekenis**: Identificatie van de organisatie die aan de levering is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID die de organisatie vertegenwoordigt.

#### receive\_delivery\_id

* **Betekenis**: Identificatie die verwijst naar de totale leveringstransactie.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID die bij een specifieke leveringstransactie hoort.

#### delivery\_number

* **Betekenis**: Uniek nummer dat aan de levering is toegekend.
* **Rol**: Referentieveld.
* **Typische inhoud**: Een tekenreeks die het leveringsnummer weergeeft.

#### line\_number

* **Betekenis**: Specifiek regelnummer binnen een levering.
* **Rol**: Referentieveld.
* **Typische inhoud**: Numerieke tekenreeks die de volgorde van de regel aangeeft.

#### item\_id

* **Betekenis**: Identificatie van het artikel dat wordt verzonden.
* **Rol**: Referentieveld.
* **Typische inhoud**: Een numerieke tekenreeks die bij een artikel hoort.

#### description

* **Betekenis**: Beschrijving van het artikel.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekstuele beschrijving van het artikel, bijv. "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Betekenis**: Hoeveelheid van het artikel die is verzonden.
* **Rol**: Kwantitatief veld.
* **Typische inhoud**: Een decimaal getal dat de verzonden hoeveelheid aangeeft.

#### status

* **Betekenis**: Huidige status van de leveringsregel.
* **Rol**: Statusveld.
* **Typische inhoud**: Tekst zoals "Received".

#### created\_by

* **Betekenis**: Identificatie van de gebruiker of het systeem dat het record heeft aangemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Integer die een gebruikers-ID vertegenwoordigt.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop het record is aangemaakt.
* **Rol**: Auditveld.
* **Typische inhoud**: Datum en tijd met tijdzone.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging.
* **Rol**: Auditveld.
* **Typische inhoud**: Datum en tijd met tijdzone.

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop het record als verwijderd is gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: Datum en tijd met tijdzone, vaak null tenzij het record is verwijderd.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarde, true of false.

#### purchase\_order

* **Betekenis**: Verwijzing naar de bijbehorende inkooporder.
* **Rol**: Referentieveld.
* **Typische inhoud**: Alfanumerieke tekenreeks die een inkoopordernummer weergeeft.

#### sequence\_number

* **Betekenis**: Volgnummer voor de leveringsregel.
* **Rol**: Referentieveld.
* **Typische inhoud**: Numerieke tekenreeks, vaak null.

#### sub\_org\_id

* **Betekenis**: Identificatie van een betrokken suborganisatie.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID, vaak null.

#### shipped\_quantity\_unit\_code

* **Betekenis**: Maateenheid van de verzonden hoeveelheid.
* **Rol**: Referentieveld.
* **Typische inhoud**: Code die eenheden weergeeft, bijv. "LBP".

#### packing\_slip\_quantity

* **Betekenis**: Hoeveelheid volgens de pakbon.
* **Rol**: Kwantitatief veld.
* **Typische inhoud**: Decimaal getal, vaak null.

#### packing\_slip\_quantity\_unit\_code

* **Betekenis**: Eenheidscode voor de hoeveelheid op de pakbon.
* **Rol**: Referentieveld.
* **Typische inhoud**: Code die eenheden weergeeft, vaak null.

#### received\_quantity

* **Betekenis**: Hoeveelheid artikelen die daadwerkelijk is ontvangen.
* **Rol**: Kwantitatief veld.
* **Typische inhoud**: Decimaal getal dat de ontvangen hoeveelheid aangeeft.

#### received\_quantity\_unit\_code

* **Betekenis**: Eenheidscode voor de ontvangen hoeveelheid.
* **Rol**: Referentieveld.
* **Typische inhoud**: Code die eenheden weergeeft, bijv. "LBP".

#### purchase\_order\_line\_number

* **Betekenis**: Regelnummer binnen de inkooporder.
* **Rol**: Referentieveld.
* **Typische inhoud**: Numerieke tekenreeks.

#### status\_effective\_from

* **Betekenis**: De datum en tijd vanaf wanneer de status van kracht is.
* **Rol**: Statusveld.
* **Typische inhoud**: Datum en tijd met tijdzone, vaak null.

#### purchase\_order\_sub\_line\_number

* **Betekenis**: Subregelnummer binnen de inkooporder.
* **Rol**: Referentieveld.
* **Typische inhoud**: Numerieke tekenreeks, vaak "000".

#### invoiced\_quantity

* **Betekenis**: Hoeveelheid die is gefactureerd.
* **Rol**: Kwantitatief veld.
* **Typische inhoud**: Decimaal getal.

#### invoice\_matching\_status

* **Betekenis**: Status van het factuurmatchingproces.
* **Rol**: Statusveld.
* **Typische inhoud**: Tekstuele statuscode, bijv. "9.0".

#### open\_quantity

* **Betekenis**: Hoeveelheid die openstaat of nog niet is verwerkt.
* **Rol**: Kwantitatief veld.
* **Typische inhoud**: Decimaal getal.

#### last\_modified\_by

* **Betekenis**: Identificatie van de gebruiker die het record het laatst heeft gewijzigd.
* **Rol**: Auditveld.
* **Typische inhoud**: UUID van de gebruiker, vaak null.

#### deleted\_by

* **Betekenis**: Identificatie van de gebruiker die het record als verwijderd heeft gemarkeerd.
* **Rol**: Auditveld.
* **Typische inhoud**: UUID van de gebruiker, vaak null.

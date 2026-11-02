# Verkooporder

## Tabel `public.sales_order`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `sub_org_id`: intern
* `location_id`: intern
* `order_number`: intern
* `customer_purchase_order`: intern
* `customer_id`: intern
* `customer_name`: intern
* `warehouse_id`: intern
* `warehouse_name`: intern
* `transportation_method`: intern
* `requested_delivery_date`: tijdstempel met tijdzone
* `order_date`: tijdstempel met tijdzone
* `sales_person_id`: intern
* `sales_person_name`: intern
* `ship_to_party_id`: intern
* `ship_to_party_name`: intern
* `ship_to_party_city`: intern
* `ship_to_party_state`: intern
* `ship_to_party_country`: intern
* `ship_to_party_zip`: intern
* `status`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `preview_path`: intern
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschrijving

## Technische documentatie voor de tabel `public.sales_order`

### Inleiding

De tabel `public.sales_order` is bedoeld voor het vastleggen en opslaan van informatie over verkooporders in een zakelijke context. Dit omvat details over de order, de klant, de logistiek en diverse metadata die bij de levenscyclus van de order horen. De tabel fungeert als centrale opslagplaats voor het volgen van de status en de historie van verkooptransacties.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elke verkooporder.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een UUID-reeks (bijv. `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Betekenis**: Identificatie van de organisatie die de verkooporder heeft aangemaakt.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een UUID-reeks die de organisatie vertegenwoordigt (bijv. `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Betekenis**: Identificatie van een suborganisatie, indien van toepassing.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Kan `NULL` zijn indien niet van toepassing.

#### location\_id

* **Betekenis**: Identificatie van de locatie die aan de verkooporder is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekencode die een locatie vertegenwoordigt (bijv. `'028'`).

#### order\_number

* **Betekenis**: Uniek nummer dat aan de verkooporder is toegekend.
* **Rol**: Technisch veld voor ordertracking.
* **Typische inhoud**: Een tekenreeks (bijv. `'0010174175'`).

#### customer\_purchase\_order

* **Betekenis**: Referentienummer van de inkooporder van de klant.
* **Rol**: Technisch veld voor kruisverwijzingen.
* **Typische inhoud**: Een tekenreeks (bijv. `'1YFNC3'`).

#### customer\_id

* **Betekenis**: Identificatie van de klant die de order plaatst.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekencode (bijv. `'35623000'`).

#### customer\_name

* **Betekenis**: Naam van de klant.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Betekenis**: Identificatie van het magazijn dat verantwoordelijk is voor het uitvoeren van de order.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekencode (bijv. `'028'`).

#### warehouse\_name

* **Betekenis**: Naam van het magazijn.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'USCS - DENTON, TX'`).

#### transportation\_method

* **Betekenis**: Transportmethode voor het afleveren van de order.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekencode (bijv. `'001'`).

#### requested\_delivery\_date

* **Betekenis**: Datum waarop de klant om levering heeft gevraagd.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tijdstempel (bijv. `None`).

#### order\_date

* **Betekenis**: Datum waarop de order is geplaatst.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tijdstempel (bijv. `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Betekenis**: Identificatie van de verkoper die de order behandelt.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekenreeks (bijv. `'ROBERTDOCK'`).

#### sales\_person\_name

* **Betekenis**: Naam van de verkoper.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Betekenis**: Identificatie van de partij naar wie de order wordt verzonden.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: Een tekenreeks (bijv. `'35623000 009'`).

#### ship\_to\_party\_name

* **Betekenis**: Naam van de partij naar wie de order wordt verzonden.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Betekenis**: Plaats van het verzendadres.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Betekenis**: Staat of deelstaat van het verzendadres.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Kan `NULL` zijn.

#### ship\_to\_party\_country

* **Betekenis**: Land van het verzendadres.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'US'`).

#### ship\_to\_party\_zip

* **Betekenis**: Postcode van het verzendadres.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'78218'`).

#### status

* **Betekenis**: Huidige status van de verkooporder.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks (bijv. `'Allocated'`).

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het item heeft aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een integer (bijv. `1`).

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop het item is aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een tijdstempel (bijv. `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een tijdstempel (bijv. `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Betekenis**: Vlag die aangeeft of de order als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Een boolean (bijv. `False`).

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop de order als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Standaarddatum als de order niet is verwijderd (bijv. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Betekenis**: Pad naar een voorbeelddocument van de verkooporder.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Een tekenreeks die een bestandspad weergeeft (bijv. `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Betekenis**: Identificatie van de gebruiker die het item het laatst heeft gewijzigd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Kan `NULL` zijn.

#### deleted\_by

* **Betekenis**: Identificatie van de gebruiker die het item als verwijderd heeft gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Kan `NULL` zijn.

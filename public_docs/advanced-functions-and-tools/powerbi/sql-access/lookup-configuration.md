# Lookup-configuratie

## Tabel `public.lookup_configuration`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type`: DOC-type
* `lookup_dataset_name`: intern
* `lookup_name`: intern
* `conflict_handle`: intern
* `created_by`: geheel getal
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: booleaans
* `deleted_on`: tijdstempel met tijdzone
* `match_all`: booleaans
* `last_modified_by`: intern
* `deleted_by`: intern
* `context`: intern
* `context_detail`: intern

### Analyse & Beschrijving

## Technische documentatie voor `public.lookup_configuration` tabel

### Inleiding

De `public.lookup_configuration`-tabel is ontworpen om configuratie-instellingen op te slaan voor verschillende gegevensopzoekbewerkingen binnen een organisatie. Het bevat informatie over de organisatie, het type documenten dat erbij betrokken is, en specifieke datasets en namen die voor lookups worden gebruikt. De tabel houdt ook de aanmaak en wijziging van deze configuraties bij, evenals hun huidige status (actief of verwijderd).

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elke lookup-configuratie-invoer in de tabel.
* **Rol**: Primaire sleutel die elke rij uniek identificeert.
* **Typische inhoud**: UUID-waarden, bijv. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Betekenis**: Vertegenwoordigt de organisatie die is gekoppeld aan de lookup-configuratie.
* **Rol**: Vreemde sleutel, gekoppeld aan een organisatie in een andere tabel.
* **Typische inhoud**: UUID-waarden die organisatie-identificaties aangeven, bijv. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Betekenis**: Specificeert het type document waarop de lookup-configuratie van toepassing is.
* **Rol**: Beschrijvend veld dat de context van de configuratie aangeeft.
* **Typische inhoud**: Tekenreeksen zoals `'MEDI_ORDER'`, `'INVOICE'`, enz.

#### lookup\_dataset\_name

* **Betekenis**: De naam van de dataset die wordt gebruikt voor het uitvoeren van lookups.
* **Rol**: Beschrijvend veld dat wordt gebruikt om datasets te identificeren.
* **Typische inhoud**: Beschrijvende tekenreeksen zoals `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Betekenis**: De specifieke naam of alias die wordt gebruikt voor de lookup-bewerking.
* **Rol**: Beschrijvend veld dat de operationele naam aangeeft.
* **Typische inhoud**: Tekenreeksen zoals `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Betekenis**: Geeft de strategie aan om conflicten tijdens lookups af te handelen.
* **Rol**: Beschrijvend veld voor strategie voor conflictoplossing.
* **Typische inhoud**: Waarden zoals `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Betekenis**: De ID van de gebruiker die de lookup-configuratie heeft gemaakt.
* **Rol**: Technisch veld voor het volgen van de maker van de invoer.
* **Typische inhoud**: Gehele getallen die gebruikers-ID's vertegenwoordigen, bijv. `1`.

#### created\_on

* **Betekenis**: Tijdstempel wanneer de lookup-configuratie is gemaakt.
* **Rol**: Technisch veld voor het volgen van de aanmaaktijd.
* **Typische inhoud**: Tijdstempels, bijv. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging die is aangebracht in de lookup-configuratie.
* **Rol**: Technisch veld voor het volgen van de laatste updatetijd.
* **Typische inhoud**: Tijdstempels, meestal `None` indien niet gewijzigd.

#### is\_deleted

* **Betekenis**: Geeft aan of de lookup-configuratie als verwijderd is gemarkeerd.
* **Rol**: Booleaans veld voor statusregistratie.
* **Typische inhoud**: Booleaanse waarden, `False` voor actieve invoeren.

#### deleted\_on

* **Betekenis**: Tijdstempel van wanneer de lookup-configuratie als verwijderd is gemarkeerd.
* **Rol**: Technisch veld voor het volgen van de verwijderingstijd.
* **Typische inhoud**: Vaak standaard een plaatshouderdatum, bijv. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Betekenis**: Specificeert of de lookup aan alle voorwaarden moet voldoen.
* **Rol**: Booleaans veld voor configuratie-instellingen.
* **Typische inhoud**: Booleaanse waarden, meestal `False`.

#### last\_modified\_by

* **Betekenis**: De ID van de gebruiker die de lookup-configuratie voor het laatst heeft gewijzigd.
* **Rol**: Technisch veld voor het volgen van de gebruiker die de invoer voor het laatst heeft bijgewerkt.
* **Typische inhoud**: UUID of identificatie van de wijzigende gebruiker, vaak `None`.

#### deleted\_by

* **Betekenis**: De ID van de gebruiker die de lookup-configuratie als verwijderd heeft gemarkeerd.
* **Rol**: Technisch veld voor het volgen van de gebruiker die verantwoordelijk is voor verwijdering.
* **Typische inhoud**: UUID of identificatie, vaak `None`.

#### context

* **Betekenis**: De context waarin de lookup wordt toegepast, zoals een sectie van een document.
* **Rol**: Beschrijvend veld voor operationele context.
* **Typische inhoud**: Tekenreeksen zoals `'header'`.

#### context\_detail

* **Betekenis**: Aanvullende details over de context voor de lookup.
* **Rol**: Beschrijvend veld voor uitgebreide contextinformatie.
* **Typische inhoud**: Vaak `None`, gebruikt voor aanvullende contextbeschrijving.
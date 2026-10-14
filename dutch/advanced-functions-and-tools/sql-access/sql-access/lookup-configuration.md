# Lookup Configuration

## Tabel `public.lookup_configuration`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type`: DOC-type
* `lookup_dataset_name`: intern
* `lookup_name`: intern
* `conflict_handle`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `match_all`: boolean
* `last_modified_by`: intern
* `deleted_by`: intern
* `context`: intern
* `context_detail`: intern

### Analyse & beschrijving

## Technische documentatie voor de tabel `public.lookup_configuration`

### Inleiding

De tabel `public.lookup_configuration` is bedoeld om configuratie-instellingen voor diverse opzoekbewerkingen binnen een organisatie op te slaan. Ze bevat informatie over de organisatie, het type betrokken documenten en de specifieke datasets en namen die voor opzoekingen worden gebruikt. De tabel houdt ook de aanmaak en wijziging van deze configuraties bij, evenals hun huidige status (actief of verwijderd).

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identifier voor elke opzoekconfiguratie in de tabel.
* **Rol**: Primaire sleutel die elke rij uniek identificeert.
* **Typische inhoud**: UUID-waarden, bijv. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Betekenis**: Vertegenwoordigt de organisatie die bij de opzoekconfiguratie hoort.
* **Rol**: Refererende sleutel, die naar een organisatie in een andere tabel verwijst.
* **Typische inhoud**: UUID-waarden die organisatie-identifiers aangeven, bijv. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Betekenis**: Geeft het documenttype aan waarop de opzoekconfiguratie van toepassing is.
* **Rol**: Beschrijvend veld dat de context van de configuratie aangeeft.
* **Typische inhoud**: Tekenreeksen zoals `'MEDI_ORDER'`, `'INVOICE'`, enz.

#### lookup\_dataset\_name

* **Betekenis**: De naam van de dataset die voor opzoekingen wordt gebruikt.
* **Rol**: Beschrijvend veld om datasets te identificeren.
* **Typische inhoud**: Beschrijvende tekenreeksen zoals `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Betekenis**: De specifieke naam of alias die voor de opzoekbewerking wordt gebruikt.
* **Rol**: Beschrijvend veld dat de operationele naam aangeeft.
* **Typische inhoud**: Tekenreeksen zoals `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Betekenis**: Geeft de strategie aan voor het afhandelen van conflicten tijdens opzoekingen.
* **Rol**: Beschrijvend veld voor de strategie voor conflictoplossing.
* **Typische inhoud**: Waarden zoals `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Betekenis**: De ID van de gebruiker die de opzoekconfiguratie heeft aangemaakt.
* **Rol**: Technisch veld om de maker van de vermelding bij te houden.
* **Typische inhoud**: Gehele getallen die gebruikers-ID's vertegenwoordigen, bijv. `1`.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop de opzoekconfiguratie is aangemaakt.
* **Rol**: Technisch veld om het tijdstip van aanmaak bij te houden.
* **Typische inhoud**: Tijdstempels, bijv. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van de opzoekconfiguratie.
* **Rol**: Technisch veld om het tijdstip van de laatste update bij te houden.
* **Typische inhoud**: Tijdstempels, meestal `None` als niet gewijzigd.

#### is\_deleted

* **Betekenis**: Geeft aan of de opzoekconfiguratie als verwijderd is gemarkeerd.
* **Rol**: Booleaans veld voor statusbewaking.
* **Typische inhoud**: Booleaanse waarden, `False` voor actieve vermeldingen.

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop de opzoekconfiguratie als verwijderd is gemarkeerd.
* **Rol**: Technisch veld om het tijdstip van verwijdering bij te houden.
* **Typische inhoud**: Vaak standaard ingesteld op een plaatshoudersdatum, bijv. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Betekenis**: Geeft aan of de opzoeking aan alle voorwaarden moet voldoen.
* **Rol**: Booleaans veld voor configuratie-instellingen.
* **Typische inhoud**: Booleaanse waarden, meestal `False`.

#### last\_modified\_by

* **Betekenis**: De ID van de gebruiker die de opzoekconfiguratie het laatst heeft gewijzigd.
* **Rol**: Technisch veld om de gebruiker bij te houden die de vermelding het laatst heeft bijgewerkt.
* **Typische inhoud**: UUID of identifier van de gebruiker die de wijziging heeft doorgevoerd, vaak `None`.

#### deleted\_by

* **Betekenis**: De ID van de gebruiker die de opzoekconfiguratie als verwijderd heeft gemarkeerd.
* **Rol**: Technisch veld om de gebruiker bij te houden die voor de verwijdering verantwoordelijk is.
* **Typische inhoud**: UUID of identifier, vaak `None`.

#### context

* **Betekenis**: De context waarin de opzoeking wordt toegepast, zoals een gedeelte van een document.
* **Rol**: Beschrijvend veld voor de operationele context.
* **Typische inhoud**: Tekenreeksen zoals `'header'`.

#### context\_detail

* **Betekenis**: Aanvullende details over de context van de opzoeking.
* **Rol**: Beschrijvend veld voor uitgebreide contextinformatie.
* **Typische inhoud**: Vaak `None`, gebruikt voor een aanvullende contextbeschrijving.

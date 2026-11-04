# REST API-lookupconfiguraties

## Tabel `public.rest_api_lookup_configurations`

### Kolommen

* `id`: intern
* `org_id`: intern
* `doc_type`: intern
* `name`: intern
* `description`: intern
* `url`: intern
* `method`: intern
* `headers`: intern
* `body`: intern
* `auth_type`: intern
* `auth_token`: intern
* `created_on`: tijdstempel met tijdzone
* `created_by`: intern
* `last_modified_on`: tijdstempel met tijdzone
* `last_modified_by`: intern
* `is_active`: booleaans

### Analyse & Beschrijving

## Technische documentatie voor `public.rest_api_lookup_configurations` tabel

### Inleiding

De `public.rest_api_lookup_configurations` tabel slaat configuraties op voor het uitvoeren van gegevenslookups via externe REST API's. Hiermee kan het systeem verbinding maken met externe diensten om gegevens op te halen tijdens documentverwerking.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID.

#### org\_id

* **Betekenis**: Organisatie-ID.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID.

#### doc\_type

* **Betekenis**: Documenttype waarop de lookup van toepassing is.
* **Rol**: Filterveld.
* **Typische inhoud**: Documenttypecodes.

#### name

* **Betekenis**: Naam van de configuratie.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekst (bijv. "Leveranciersvalidatie API").

#### description

* **Betekenis**: Beschrijving van het doel.
* **Rol**: Documentatieveld.
* **Typische inhoud**: Tekst.

#### url

* **Betekenis**: Het eindpunt van de externe API.
* **Rol**: Configuratieveld.
* **Typische inhoud**: URL's (bijv. `https://api.example.com/v1/suppliers`).

#### method

* **Betekenis**: HTTP-methode (GET, POST, enz.).
* **Rol**: Configuratieveld.
* **Typische inhoud**: `'GET'`, `'POST'`.

#### headers

* **Betekenis**: HTTP-headers die moeten worden meegestuurd.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-object.

#### body

* **Betekenis**: De body van het verzoek (voor POST/PUT).
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-sjabloon of tekst.

#### auth\_type

* **Betekenis**: Authenticatiemethode.
* **Rol**: Beveiligingsveld.
* **Typische inhoud**: `'Basic'`, `'Bearer'`, `'API Key'`.

#### auth\_token

* **Betekenis**: Authenticatietoken of sleutel (versleuteld opgeslagen).
* **Rol**: Beveiligingsveld.
* **Typische inhoud**: Versleutelde tekenreeks.

#### created\_on

* **Betekenis**: Aanmaakdatum.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempel.

#### created\_by

* **Betekenis**: Gemaakt door gebruiker.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID.

#### last\_modified\_on

* **Betekenis**: Laatste wijzigingsdatum.
* **Rol**: Auditveld.
* **Typische inhoud**: Tijdstempel.

#### last\_modified\_by

* **Betekenis**: Gewijzigd door gebruiker.
* **Rol**: Auditveld.
* **Typische inhoud**: Gebruikers-ID.

#### is\_active

* **Betekenis**: Of de configuratie actief is.
* **Rol**: Statusvlag.
* **Typische inhoud**: `True`/`False`.
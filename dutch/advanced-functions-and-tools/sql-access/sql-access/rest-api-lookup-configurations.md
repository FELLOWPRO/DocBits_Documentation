# Opzoekconfiguraties via REST-API

## Tabel `public.rest_api_lookup_configurations`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `sub_org_id`: intern
* `data_key`: intern
* `url`: intern
* `method`: intern
* `params`: tekst
* `headers`: tekst
* `body`: tekst
* `body_type`: intern
* `authentication_type`: intern
* `authentication_json`: tekst
* `data_base_path`: intern
* `column_paths`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `is_template`: boolean
* `is_dynamic`: boolean

### Analyse & Beschrijving

## Technische documentatie: tabel `public.rest_api_lookup_configurations`

### Inleiding

De tabel `public.rest_api_lookup_configurations` is bedoeld voor het opslaan van configuraties voor REST API-lookups binnen een organisatie. Deze tabel bevat de essentiële informatie voor het uitvoeren van API-verzoeken, waaronder details over de endpoints, authenticatiemethoden en de configuratie van verzoeken en antwoorden. Ze wordt kennelijk gebruikt om API-aanroepen dynamisch op te bouwen en de resultaten ervan te verwerken.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elk configuratie-item.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: UUID-reeksen zoals `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Opmerking**: Dit is de unieke sleutel om een specifieke API-lookupconfiguratie te identificeren.

#### org\_id

* **Betekenis**: Identificatie van de organisatie die eigenaar is van de configuratie.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID-reeksen die organisatie-ID's vertegenwoordigen.
* **Opmerking**: Koppelt de configuratie aan een organisatie.

#### sub\_org\_id

* **Betekenis**: Identificatie van een suborganisatie binnen de hoofdorganisatie.
* **Rol**: Vreemde sleutel.
* **Typische inhoud**: UUID-reeksen die suborganisatie-ID's vertegenwoordigen.
* **Opmerking**: Maakt een fijnere granulariteit binnen organisaties mogelijk.

#### data\_key

* **Betekenis**: Een label of sleutel om de gegevens of het API-endpoint te identificeren.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Beschrijvende tekst zoals `bank_codes`.
* **Opmerking**: Wordt gebruikt om onderscheid te maken tussen verschillende typen gegevens of endpoints.

#### url

* **Betekenis**: De URL van het API-endpoint dat moet worden aangeroepen.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: URL-reeksen zoals `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Opmerking**: Vertegenwoordigt het endpoint waarnaar het HTTP-verzoek wordt verzonden.

#### method

* **Betekenis**: HTTP-methode die voor het API-verzoek wordt gebruikt.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Gangbare HTTP-methoden zoals `GET`.
* **Opmerking**: Bepaalt het type HTTP-verzoek dat wordt uitgevoerd.

#### params

* **Betekenis**: Parameters die in het API-verzoek worden opgenomen.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON of sleutel-waardeparen (vaak `None` als ze niet worden gebruikt).
* **Opmerking**: Bevat dynamische parameters voor het verzoek.

#### headers

* **Betekenis**: HTTP-headers die in het verzoek worden opgenomen.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON- of tekstgegevens (vaak `None` als ze niet worden gebruikt).
* **Opmerking**: Wordt gebruikt om extra metadata in het verzoek op te nemen.

#### body

* **Betekenis**: De body van het HTTP-verzoek.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-gegevens of andere geserialiseerde gegevens (vaak `None` als ze niet worden gebruikt).
* **Opmerking**: Bevat de payload voor POST-/PUT-verzoeken.

#### body\_type

* **Betekenis**: Geeft het formaat van de verzoekbody aan.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: MIME-types zoals `application/json`.
* **Opmerking**: Geeft het inhoudstype van de body aan.

#### authentication\_type

* **Betekenis**: Type authenticatie dat voor het API-verzoek wordt gebruikt.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Authenticatiemethoden zoals `ionapi`.
* **Opmerking**: Bepaalt hoe het verzoek wordt geauthenticeerd.

#### authentication\_json

* **Betekenis**: Details van de authenticatieconfiguratie in JSON-formaat.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-reeksen met authenticatie-informatie.
* **Opmerking**: Bevat inloggegevens en endpointdetails voor de authenticatie.

#### data\_base\_path

* **Betekenis**: Pad binnen het API-antwoord waaruit de gegevens worden gehaald.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-padexpressies zoals `$[results][0][records]`.
* **Opmerking**: Wordt gebruikt om de gegevens van het API-antwoord te verwerken.

#### column\_paths

* **Betekenis**: Koppelt gegevensvelden aan kolommen voor extractie.
* **Rol**: Configuratieveld.
* **Typische inhoud**: JSON-reeksen die velden uit het API-antwoord aan kolomnamen koppelen.
* **Opmerking**: Vergemakkelijkt de extractie van gegevens uit het API-antwoord.

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die de configuratie heeft aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Integer-ID's zoals `1`.
* **Opmerking**: Houdt bij wie de maker van het configuratie-item is.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop de configuratie is aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Tijdstempels zoals `2024-01-24T09:14:24.788788Z`.
* **Opmerking**: Geeft de aanmaakdatum en -tijd aan.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging.
* **Rol**: Technisch veld.
* **Typische inhoud**: Tijdstempels (vaak `None` als er niets is gewijzigd).
* **Opmerking**: Registreert het tijdstip van de laatste update.

#### is\_deleted

* **Betekenis**: Vlag die aangeeft of een configuratie als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarden zoals `False`.
* **Opmerking**: Wordt gebruikt om configuraties via soft delete te verwijderen.

#### deleted\_on

* **Betekenis**: Tijdstempel van het moment waarop de configuratie als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Tijdstempels (vaak een plaatshouder als de configuratie niet is verwijderd).
* **Opmerking**: Registreert wanneer de configuratie als verwijderd is gemarkeerd.

#### is\_template

* **Betekenis**: Geeft aan of de configuratie als sjabloon dient.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Boolean-waarden zoals `True`.
* **Opmerking**: Identificeert sjablonen voor hergebruik.

#### is\_dynamic

* **Betekenis**: Geeft aan of de configuratie dynamisch is.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Boolean-waarden zoals `False`.
* **Opmerking**: Bepaalt of de configuratie zich aanpast aan veranderende gegevens.

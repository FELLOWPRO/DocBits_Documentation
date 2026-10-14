# public.document\_log

## Tabel `public.document_log`

### Kolommen

* `id`: integer
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `action_type`: intern
* `action_description`: tekst
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: intern
* `current_status`: intern

### Analyse & Beschrijving

## Technische documentatie: tabel `public.document_log`

### Inleiding

De tabel `public.document_log` is bedoeld om de historie en statuswijzigingen van documenten binnen een organisatie vast te leggen. Ze registreert acties die op documenten zijn uitgevoerd, zoals statusupdates, samen met details over de gebruiker die de actie heeft uitgevoerd en tijdstempels die aangeven wanneer deze acties hebben plaatsgevonden. Deze tabel is essentieel voor het auditen van documentverwerkingsworkflows en voor het begrijpen van de levenscyclus van elk document.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elk logitem.
* **Rol**: Primaire sleutel. Deze kolom dient als unieke identificatie van elk record in de tabel.
* **Typische inhoud**: Integerwaarden die bij elk nieuw item oplopen.

#### org\_id

* **Betekenis**: Identificatie van de organisatie die aan het document is gekoppeld.
* **Rol**: Vreemde sleutel. Verwijst naar een organisatie-entiteit, hoewel dit in deze context niet expliciet is gedefinieerd.
* **Typische inhoud**: Tekenreeksen, waarschijnlijk UUID's, die organisatie-identificatoren vertegenwoordigen.

#### doc\_id

* **Betekenis**: Identificatie van het document dat aan het logitem is gekoppeld.
* **Rol**: Vreemde sleutel. Deze kolom verwijst naar een specifiek document binnen het systeem.
* **Typische inhoud**: Tekenreeksen, waarschijnlijk UUID's, die documentidentificatoren vertegenwoordigen.

#### action\_type

* **Betekenis**: Type actie dat is gelogd.
* **Rol**: Beschrijvend veld. Geeft de categorie van de uitgevoerde actie aan.
* **Typische inhoud**: Tekenreeksen zoals `STATUS_CHANGE`, die de aard van de actie aangeven.

#### action\_description

* **Betekenis**: Gedetailleerde beschrijving van de uitgevoerde actie.
* **Rol**: Beschrijvend veld. Biedt context of details over de actie.
* **Typische inhoud**: Tekstbeschrijvingen, bijv. "Data extraction started", "Error occurred processing document".

#### created\_by

* **Betekenis**: Identificatie van de gebruiker die het logitem heeft aangemaakt.
* **Rol**: Vreemde sleutel. Verwijst naar een gebruikersentiteit en geeft aan wie de actie heeft uitgevoerd.
* **Typische inhoud**: Integerwaarden die gebruikersidentificatoren vertegenwoordigen.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop het logitem is aangemaakt.
* **Rol**: Technisch veld. Legt het exacte tijdstip vast waarop een actie is gelogd.
* **Typische inhoud**: Tijdstempels met tijdzone-informatie, bijv. `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van het logitem.
* **Rol**: Technisch veld. Geeft het tijdstip van de laatste update van het logitem aan.
* **Typische inhoud**: Tijdstempels, mogelijk null als het item na aanmaak niet is gewijzigd.

#### is\_deleted

* **Betekenis**: Vlag die aangeeft of het logitem als verwijderd is gemarkeerd.
* **Rol**: Technisch veld. Wordt gebruikt voor logische verwijdering van items.
* **Typische inhoud**: Boolean-waarden, waarbij `False` actieve items aangeeft en `True` verwijderde items.

#### is\_hidden

* **Betekenis**: Vlag die aangeeft of het logitem in de normale weergave verborgen is.
* **Rol**: Technisch veld. Wordt gebruikt om de zichtbaarheid van logitems te regelen.
* **Typische inhoud**: Boolean-waarden, waarbij `False` zichtbare items aangeeft en `True` verborgen items.

#### previous\_status

* **Betekenis**: Status van het document voordat de actie werd uitgevoerd.
* **Rol**: Beschrijvend veld. Geeft de toestand van het document vóór de gelogde actie weer.
* **Typische inhoud**: Tekenreeksen zoals `new`, `validating`, `running`, die documentstatussen vertegenwoordigen.

#### current\_status

* **Betekenis**: Status van het document nadat de actie was uitgevoerd.
* **Rol**: Beschrijvend veld. Geeft de bijgewerkte toestand van het document na de actie aan.
* **Typische inhoud**: Tekenreeksen zoals `running`, `ready_for_validation`, `error`, die documentstatussen vertegenwoordigen.

Deze documentatie geeft een overzicht van de tabel `public.document_log` en beschrijft het doel en de structuur van elke kolom, wat van groot belang is voor ontwikkelaars die documentworkflows beheren en audittrails onderhouden.

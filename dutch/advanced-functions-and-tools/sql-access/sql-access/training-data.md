# Training data

## Tabel `public.training_data`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type`: DOC Type
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `doc_language`: Language
* `first_page_content`: tekst
* `supplier_name`: Supplier Name
* `supplier_vat`: intern
* `doc_created_on`: tijdstempel met tijdzone
* `is_training_sample`: boolean
* `sample_doc_id`: intern
* `sample_file_name`: intern
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Analyse & Beschrijving

## Technische documentatie voor de tabel `public.training_data`

### Inleiding

De tabel `public.training_data` is kennelijk bedoeld voor het opslaan van uiteenlopende documentgerelateerde gegevens, waarschijnlijk gebruikt voor het trainen van modellen of systemen die documentinhoud verwerken en analyseren. De tabel bevat informatie over het documenttype, de herkomst, de taal, leveranciersgegevens en tijdstempels voor het aanmaken en wijzigen van records, naast andere kenmerken. Ze lijkt zich met name te richten op facturen en medische bonnen, wat wijst op gebruik in toepassingen voor financiële of zorggerelateerde gegevensverwerking.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische inhoud**: Een universeel unieke identificator (UUID) in tekenformaat.
* **Opmerking**: Essentieel om elk item uniek te identificeren.

#### org\_id

* **Betekenis**: Identificatie van de organisatie die aan het document is gekoppeld.
* **Rol**: Vreemde sleutel die naar een organisatierecord verwijst.
* **Typische inhoud**: UUID die een organisatie vertegenwoordigt.
* **Opmerking**: Helpt bij het koppelen van documenten aan specifieke organisaties.

#### doc\_type

* **Betekenis**: Type document dat in het record is opgeslagen.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Waarden zoals 'INVOICE' of 'MEDICAL\_RECEIPT'.
* **Opmerking**: Nuttig voor het categoriseren van de documenten.

#### doc\_origin

* **Betekenis**: Herkomst of landcode van de bron van het document.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Landcode zoals 'DE' voor Duitsland.
* **Opmerking**: Geeft de geografische herkomst van het document aan.

#### doc\_locale

* **Betekenis**: Locale-informatie van het document.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Locale-code zoals 'en\_DE'.
* **Opmerking**: Combineert taal en regio voor lokalisatiedoeleinden.

#### doc\_language

* **Betekenis**: Taal waarin het document is geschreven.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Taalcode zoals 'en' of 'de'.
* **Opmerking**: Geeft de primaire taal aan die in het document wordt gebruikt.

#### first\_page\_content

* **Betekenis**: Inhoud van de eerste pagina van het document.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Tekstgegevens met de inhoud van de eerste pagina van het document.
* **Opmerking**: Kan worden gebruikt voor tekstanalyse of -verwerking.

#### supplier\_name

* **Betekenis**: Naam van de leverancier die aan het document is gekoppeld.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Naam van de leverancier in tekstformaat.
* **Opmerking**: Belangrijk om de bron of opsteller van het document te identificeren.

#### supplier\_vat

* **Betekenis**: Btw-identificatienummer van de leverancier.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Btw-ID, bijv. 'DE 129375678'.
* **Opmerking**: Nuttig voor fiscale en belastinggerelateerde processen.

#### doc\_created\_on

* **Betekenis**: Tijdstempel van het moment waarop het document is aangemaakt.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Datum en tijd in UTC-formaat.
* **Opmerking**: Biedt tijdscontext voor de aanmaak van het document.

#### is\_training\_sample

* **Betekenis**: Indicator die aangeeft of het record als trainingsvoorbeeld wordt gebruikt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarde (`True` of `False`).
* **Opmerking**: Identificeert records die specifiek voor trainingsdoeleinden zijn gemarkeerd.

#### sample\_doc\_id

* **Betekenis**: Identificatie van het voorbeelddocument.
* **Rol**: Beschrijvend veld of mogelijke vreemde sleutel.
* **Typische inhoud**: UUID die naar een ander document verwijst.
* **Opmerking**: Kan verwijzen naar een gerelateerd of oorspronkelijk document dat voor de steekproef is gebruikt.

#### sample\_file\_name

* **Betekenis**: Naam van het bestand dat bij het documentvoorbeeld hoort.
* **Rol**: Beschrijvend veld.
* **Typische inhoud**: Bestandsnaam in tekstformaat.
* **Opmerking**: Nuttig voor bestandsbeheer of ophaalprocessen.

#### created\_on

* **Betekenis**: Tijdstempel van het moment waarop het record is aangemaakt.
* **Rol**: Technisch veld.
* **Typische inhoud**: Datum en tijd in UTC-formaat.
* **Opmerking**: Geeft aan wanneer het record aan de database is toegevoegd.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van het record.
* **Rol**: Technisch veld.
* **Typische inhoud**: Datum en tijd in UTC-formaat.
* **Opmerking**: Houdt bij wanneer het record voor het laatst is bijgewerkt.

#### is\_deleted

* **Betekenis**: Indicator die aangeeft of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarde (`True` of `False`).
* **Opmerking**: Ondersteunt soft-delete-functionaliteit.

#### is\_table\_training\_sample

* **Betekenis**: Indicator die aangeeft of het record een tabelspecifiek trainingsvoorbeeld is.
* **Rol**: Technisch veld.
* **Typische inhoud**: Boolean-waarde (`True` of `False`).
* **Opmerking**: Maakt onderscheid met algemene trainingsvoorbeelden en richt zich op tabelgegevens.

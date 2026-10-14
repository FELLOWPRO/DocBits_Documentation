# Electronic document extraction attributes

## Tabel `public.electronic_document_extraction_attributes`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type_key`: intern
* `sub_doc_type_key`: intern
* `electronic_document_type`: intern
* `attribute_name`: intern
* `attribute_type`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_on`: tijdstempel met tijdzone
* `last_modified_by`: intern
* `deleted_by`: intern

### Analyse & Beschrijving

## Technische Documentatie voor `public.electronic_document_extraction_attributes`

### Inleiding

De tabel `public.electronic_document_extraction_attributes` beheert attributen die gerelateerd zijn aan de extractie van elektronische documenten. Dit omvat het opslaan van diverse kenmerken en metadata over elektronische documenttypen, hun verwerkingsmethoden en de bijbehorende organisaties. De tabel ondersteunt functionaliteiten zoals identificatie van documenttypen, transformaties, previews en structuurbeschrijvingen die essentieel zijn voor een effectieve afhandeling van elektronische documenten.

### Kolombeschrijvingen

#### id

* **Betekenis**: Een unieke identificatie voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Een UUID-reeks die elk item voor documentextractie-attributen uniek identificeert.
* **Opmerking**: Dit dient als de unieke referentie voor elke rij.

#### org\_id

* **Betekenis**: Identificatie voor de organisatie die gerelateerd is aan de documentattributen.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: Een UUID-reeks die linkt naar de bijbehorende organisatie.
* **Opmerking**: Dit verbindt de documentextractie-attributen aan een specifieke organisatie.

#### doc\_type\_key

* **Betekenis**: Een sleutel die het type document vertegenwoordigt.
* **Rol**: Identificatie voor het categoriseren van documenten.
* **Typische Inhoud**: Een reeks die het documenttype aangeeft, zoals 'INVOICE' of 'ORDER\_CONFIRMATION'.
* **Opmerking**: Gebruikt om de categorie van het document te bepalen.

#### sub\_doc\_type\_key

* **Betekenis**: Vertegenwoordigt een subcategorie van het hoofddocumenttype.
* **Rol**: Identificatie voor verdere classificatie.
* **Typische Inhoud**: Null of een specifieke sub-type reeks.
* **Opmerking**: Nuttig voor verdere granulariteit in documentclassificatie.

#### electronic\_document\_type

* **Betekenis**: Het formaat of de standaard van het elektronische document.
* **Rol**: Beschrijvend veld voor documentformaat.
* **Typische Inhoud**: Reeksen zoals 'EDI' of 'FACTURX'.
* **Opmerking**: Geeft de standaard of het formaat van het document aan.

#### attribute\_name

* **Betekenis**: De naam van het attribuut gerelateerd aan het documentextractieproces.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Reeksen zoals 'PREVIEW' of 'TRANSFORMATION'.
* **Opmerking**: Beschrijft het specifieke attribuut gerelateerd aan de documentafhandeling.

#### attribute\_type

* **Betekenis**: Het type attribuut gerelateerd aan de documentextractie.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Reeksen zoals 'XSLT' of 'JSON'.
* **Opmerking**: Specificeert het gegevensformaat of de methode die voor het attribuut wordt gebruikt.

#### created\_by

* **Betekenis**: ID van de gebruiker die het record heeft aangemaakt.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: Integer die een gebruikers-ID vertegenwoordigt.
* **Opmerking**: Houdt bij wie het record oorspronkelijk heeft aangemaakt.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het record is aangemaakt.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd in UTC.
* **Opmerking**: Geeft de aanmaaktijd van het record aan.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van de laatste wijziging van het record.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd in UTC, of null indien niet gewijzigd.
* **Opmerking**: Volgt de meest recente update van het record.

#### is\_deleted

* **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Boolean waarde, `True` of `False`.
* **Opmerking**: Helpt bij de afhandeling van soft-deletion.

#### deleted\_on

* **Betekenis**: Tijdstempel van wanneer het record als verwijderd is gemarkeerd.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd in UTC, of een standaard oude datum indien niet verwijderd.
* **Opmerking**: Wordt gebruikt om bij te houden wanneer het record is verwijderd.

#### last\_modified\_by

* **Betekenis**: ID van de gebruiker die het record voor het laatst heeft gewijzigd.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: UUID-reeks, of null indien niet gewijzigd.
* **Opmerking**: Identificeert de gebruiker die verantwoordelijk is voor de laatste wijziging.

#### deleted\_by

* **Betekenis**: ID van de gebruiker die het record als verwijderd heeft gemarkeerd.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: UUID-reeks, of null indien niet verwijderd.
* **Opmerking**: Houdt bij wie de verwijderingsactie heeft uitgevoerd.

Deze documentatie biedt een gedetailleerd overzicht van de tabelstructuur en de kolommen, wat een beter begrip en gebruik door ontwikkelaars en databasebeheerders mogelijk maakt.

# Organisatiedocumenttype

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `document_type_id`: intern
* `document_type_key`: intern
* `document_locale`: intern
* `classification_method`: intern
* `is_active`: boolean
* `extraction_type`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `sub_org_id`: intern

## Analyse & Beschrijving

```markdown
# Technische documentatie voor de tabel `public.organisation_document_type`

## Inleiding

De tabel `public.organisation_document_type` is bedoeld voor het beheren en opslaan van informatie over de diverse documenttypen die aan organisaties zijn gekoppeld. Dit omvat gegevens zoals de documenttypesleutel, de taalinstelling (locale), de classificatiemethoden en de status van het documenttype (actief, verwijderd, enzovoort). De tabel fungeert kennelijk als koppeling tussen organisaties en de typen documenten die zij gebruiken of beheren, aangevuld met metadata over deze documenten.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identificatie voor elk record in de tabel.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: Een UUID-reeks die een documenttype-item uniek identificeert.
- **Opmerking**: Essentieel om elk record te kunnen onderscheiden.

### org_id
- **Betekenis**: Identificatie van de organisatie waaraan het documenttype is gekoppeld.
- **Rol**: Vreemde sleutel, verwijst waarschijnlijk naar een organisatietabel.
- **Typische inhoud**: Een UUID-reeks.
- **Opmerking**: Koppelt het documenttype aan een specifieke organisatie.

### document_type_id
- **Betekenis**: Identificatie van het documenttype.
- **Rol**: Vreemde sleutel, mogelijk gekoppeld aan een referentietabel met documenttypen.
- **Typische inhoud**: Een UUID-reeks.
- **Opmerking**: Maakt de koppeling met specifieke documenttypen mogelijk.

### document_type_key
- **Betekenis**: Een sleutel of code die het documenttype vertegenwoordigt.
- **Rol**: Beschrijvend veld voor de classificatie van documenttypen.
- **Typische inhoud**: Een tekenreeks die dient als identificator of label voor het documenttype.
- **Opmerking**: Wordt gebruikt om het documenttype in een voor mensen leesbare vorm te identificeren.

### document_locale
- **Betekenis**: Locale- of taalinstelling voor het documenttype.
- **Rol**: Beschrijvend veld voor de locale-specificatie.
- **Typische inhoud**: Een tekenreeks, vaak 'auto', wat duidt op automatische bepaling van de locale.
- **Opmerking**: Nuttig voor internationalisering en lokalisatie.

### classification_method
- **Betekenis**: Methode die wordt gebruikt om het documenttype te classificeren.
- **Rol**: Beschrijvend veld dat aangeeft hoe het document wordt geclassificeerd.
- **Typische inhoud**: Een tekenreeks, vaak 'auto', wat wijst op automatische classificatie.
- **Opmerking**: Belangrijk om het classificatieproces te begrijpen.

### is_active
- **Betekenis**: Status die aangeeft of het documenttype actief is.
- **Rol**: Boolean statusveld.
- **Typische inhoud**: `True` of `False`.
- **Opmerking**: Bepaalt of het documenttype momenteel in gebruik is.

### extraction_type
- **Betekenis**: Type extractiemethode dat voor het document wordt gebruikt.
- **Rol**: Beschrijvend veld voor het extractieproces.
- **Typische inhoud**: Tekenreeksen zoals 'FIX_COORDINATES', 'FLEX_COORDINATES' of `None`.
- **Opmerking**: Geeft inzicht in hoe gegevens uit documenten worden geëxtraheerd.

### created_by
- **Betekenis**: Identificatie van de gebruiker die het record heeft aangemaakt.
- **Rol**: Technisch veld voor auditdoeleinden.
- **Typische inhoud**: Een integer die een gebruikers-ID vertegenwoordigt.
- **Opmerking**: Nuttig voor het bijhouden van wijzigingen en verantwoording.

### created_on
- **Betekenis**: Tijdstempel van het moment waarop het record is aangemaakt.
- **Rol**: Technisch veld voor auditdoeleinden.
- **Typische inhoud**: Een tijdstempel met tijdzone.
- **Opmerking**: Belangrijk om de aanmaakdatum en -tijd van het record bij te houden.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging van het record.
- **Rol**: Technisch veld voor auditdoeleinden.
- **Typische inhoud**: Een tijdstempel met tijdzone.
- **Opmerking**: Nuttig om bijwerkingen en wijzigingen van het record te volgen.

### is_deleted
- **Betekenis**: Status die aangeeft of het record als verwijderd is gemarkeerd.
- **Rol**: Boolean statusveld.
- **Typische inhoud**: `True` of `False`.
- **Opmerking**: Helpt bij het implementeren van soft-delete-functionaliteit.

### sub_org_id
- **Betekenis**: Identificatie van een suborganisatie die aan het documenttype is gekoppeld.
- **Rol**: Mogelijke vreemde sleutel, die een hiërarchische organisatiestructuur toevoegt.
- **Typische inhoud**: Een UUID-reeks of `None`.
- **Opmerking**: Biedt extra context voor de organisatiestructuur.

```

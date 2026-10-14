# Document type

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `document_key`: intern
* `document_name`: intern
* `title`: intern
* `translation_key`: intern
* `extraction_type`: intern
* `document_type_category`: intern
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

## Analyse & Beschrijving

```markdown
# Tabel: public.document_type

## Inleiding
De tabel `public.document_type` is ontworpen om informatie op te slaan over verschillende soorten documenten binnen een organisatie. Het bevat identificatoren en metadata voor documentcategorisatie, beheer en verwerking, zoals documentsleutels, namen, titels, vertaalsleutels en andere attributen die de afhandeling en het opvragen van documenten vergemakkelijken. De tabel houdt ook het aanmaken en wijzigen van deze items bij, en ondersteunt zowel actieve als verwijderde statussen.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk documenttype-item.
- **Rol**: Primaire Sleutel.
- **Typische Inhoud**: Een UUID-reeks die een documenttype-item uniek identificeert.

### org_id
- **Betekenis**: Identificatie voor de organisatie waartoe het documenttype behoort.
- **Rol**: Vreemde Sleutel.
- **Typische Inhoud**: Een UUID-reeks die verwijst naar een organisatie.

### document_key
- **Betekenis**: Een unieke sleutel voor het identificeren van het documenttype, mogelijk gebruikt in documentopslag- of verwerkingssystemen.
- **Rol**: Identificator.
- **Typische Inhoud**: Een reeks die informatie over het documenttype combineert met de organisatie-ID.

### document_name
- **Betekenis**: De interne naam voor het documenttype.
- **Rol**: Beschrijvend Veld.
- **Typische Inhoud**: Een reeks in hoofdletters die de naam van het documenttype vertegenwoordigt.

### title
- **Betekenis**: De weergavetitel van het documenttype voor gebruikersinterfaces.
- **Rol**: Beschrijvend Veld.
- **Typische Inhoud**: Een tekst in 'title case' die leesbaar en beschrijvend is voor het documenttype.

### translation_key
- **Betekenis**: Een sleutel die wordt gebruikt om de documenttitel of -naam te lokaliseren in verschillende talen.
- **Rol**: Ondersteuning voor Internationalisering.
- **Typische Inhoud**: Een reeks in kleine letters die dient als referentie voor vertaalsystemen.

### extraction_type
- **Betekenis**: Geeft de methode of het proces aan waarmee gegevens uit het document worden geëxtraheerd.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Momenteel niet ingevuld in de voorbeeldgegevens.

### document_type_category
- **Betekenis**: Categoriseert het documenttype in bredere categorieën of classificaties.
- **Rol**: Categoriseringsveld.
- **Typische Inhoud**: Momenteel niet ingevuld in de voorbeeldgegevens.

### has_table
- **Betekenis**: Geeft aan of het documenttype betrekking heeft op tabelgegevens.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Boolean waarde (`True` of `False`) die de aanwezigheid van tabelgegevens aangeeft.

### sort_order
- **Betekenis**: Definieert de volgorde waarin documenttypen worden gesorteerd of weergegeven.
- **Rol**: Sorteerveld.
- **Typische Inhoud**: Een integer die de volgorde voor sortering vertegenwoordigt.

### created_by
- **Betekenis**: Identificatie voor de gebruiker die het documenttype-item heeft aangemaakt.
- **Rol**: Metagegevensveld.
- **Typische Inhoud**: Een integer die verwijst naar een gebruikers-ID.

### created_on
- **Betekenis**: Tijdstempel die aangeeft wanneer het documenttype-item is aangemaakt.
- **Rol**: Auditveld.
- **Typische Inhoud**: Datum en tijd met tijdzone-informatie.

### last_modified_on
- **Betekenis**: Tijdstempel die de laatste wijzigingsdatum van het documenttype-item aangeeft.
- **Rol**: Auditveld.
- **Typische Inhoud**: Datum en tijd met tijdzone-informatie, `None` indien nooit gewijzigd.

### is_deleted
- **Betekenis**: Geeft aan of het documenttype-item als verwijderd is gemarkeerd.
- **Rol**: Statusveld.
- **Typische Inhoud**: Boolean waarde (`True` of `False`) die de verwijderingsstatus aangeeft.
```

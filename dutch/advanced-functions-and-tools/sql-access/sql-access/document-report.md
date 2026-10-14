# Document Report

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `doc_type`: DOC-type
* `sub_doc_type`: intern
* `time_spent`: intern
* `fields_total`: integer
* `fields_correct`: integer
* `checkbox_fields_total`: integer
* `checkbox_fields_correct`: integer
* `table_values_total`: integer
* `table_values_correct`: integer
* `detail_report`: text
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `validated_by`: integer
* `sub_org_id`: intern

## Analyse & Beschrijving

```markdown
# Documentatie voor de Tabel Document Report

## Inleiding
De tabel `public.document_report` is ontworpen om gedetailleerde informatie op te slaan over documentverwerkingsrapporten, specifiek gerelateerd aan de validatie en extractie van velden uit documenten zoals facturen. De tabel legt metadata over het document vast, evenals verwerkingsstatistieken en de validatieresultaten, die kunnen worden gebruikt voor auditing, tracking en het verbeteren van documentverwerkingsworkflows.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identificatie voor elk documentrapportitem.
- **Rol**: Primaire Sleutel (Primary Key)
- **Typische Inhoud**: Een UUID die het unieke documentrapport vertegenwoordigt.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan het document is gekoppeld.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Een UUID die linkt naar een organisatie.

### doc_id
- **Betekenis**: Identificatie voor het specifieke document waarover wordt gerapporteerd.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Een UUID die het unieke document vertegenwoordigt.

### doc_type
- **Betekenis**: Type van het document dat wordt verwerkt, zoals een factuur.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Waarden zoals `INVOICE`.

### sub_doc_type
- **Betekenis**: Subtype van het document, voor verdere categorisering.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Kan `null` zijn of specifieke subtypen zoals "Kostenfactuur".

### time_spent
- **Betekenis**: Tijd besteed aan de validatie van het document.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Meestal '0', waarbij de tijd in vooraf gedefinieerde eenheden wordt gemeten.

### fields_total
- **Betekenis**: Totaal aantal velden geëxtraheerd uit het document.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Een integer die het totaal aantal velden vertegenwoordigt, bijv. 13.

### fields_correct
- **Betekenis**: Aantal velden dat correct is geëxtraheerd en gevalideerd.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Een integer die correct verwerkte velden vertegenwoordigt, bijv. 12.

### checkbox_fields_total
- **Betekenis**: Totaal aantal verwerkte selectievakjes (checkbox fields).
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Meestal `0`, geeft aan hoeveel selectievakjes zijn verwerkt.

### checkbox_fields_correct
- **Betekenis**: Aantal selectievakjes dat correct is gevalideerd.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Meestal `0`, geeft het aantal correct gevalideerde selectievakjes aan.

### table_values_total
- **Betekenis**: Totaal aantal tabelwaarden geëxtraheerd uit het document.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Meestal `0`, geeft het totaal aantal verwerkte tabelwaarden aan.

### table_values_correct
- **Betekenis**: Aantal tabelwaarden dat correct is gevalideerd.
- **Rol**: Metrisch veld.
- **Typische Inhoud**: Meestal `0`, geeft het aantal correct gevalideerde tabelwaarden aan.

### detail_report
- **Betekenis**: JSON-inhoud die een gedetailleerd rapport geeft van de documentvelden en hun validatiestatus.
- **Rol**: Beschrijvend/Technisch veld.
- **Typische Inhoud**: JSON-reeks met gedetailleerde veldinformatie.

### created_on
- **Betekenis**: Tijdstempel van wanneer het documentrapportitem is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Tijdstempel in UTC, bijv. `2025-03-10 08:07:24+00`.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging aan het documentrapport.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Tijdstempel in UTC, die de laatste updatetijd aangeeft.

### is_deleted
- **Betekenis**: Geeft aan of het documentrapport als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde; `False` indien niet verwijderd.

### validated_by
- **Betekenis**: Identificatie van de gebruiker die het document heeft gevalideerd.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Integer die de ID van de validateur vertegenwoordigt, bijv. `1`.

### sub_org_id
- **Betekenis**: Identificatie voor een suborganisatie gerelateerd aan het document.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Een UUID die linkt naar een suborganisatie.
```

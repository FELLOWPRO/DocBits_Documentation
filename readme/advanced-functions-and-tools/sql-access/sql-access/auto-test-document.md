# Automatisch testdocument

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `doc_type`: DOC-type
* `extracted_data`: text
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `filename`: intern

## Analyse & beschrijving

```markdown
# Tabeldocumentatie: `public.auto_test_document`

## Inleiding

De tabel `public.auto_test_document` is bedoeld om metagegevens en extractieresultaten van documentverwerking binnen een organisatie op te slaan. De tabel legt informatie vast over documenten, hun typen en de daaruit geëxtraheerde gegevens. Ze bevat velden voor documentidentificatie, verwerkingsmetagegevens en statusvlaggen, die essentieel zijn voor het beheren van documentworkflows en het waarborgen van gegevensintegriteit.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identifier voor elke documentvermelding in de tabel.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: UUID-tekenreeks.
- **Opmerking**: Dient als unieke identifier voor records en zorgt ervoor dat elke vermelding uniek is.

### org_id
- **Betekenis**: Identifier van de organisatie die bij het document hoort.
- **Rol**: Refererende sleutel.
- **Typische inhoud**: UUID-tekenreeks.
- **Opmerking**: Koppelt het document aan een specifieke organisatie binnen het systeem.

### doc_id
- **Betekenis**: Identifier van het document dat wordt verwerkt.
- **Rol**: Refererende sleutel.
- **Typische inhoud**: UUID-tekenreeks.
- **Opmerking**: Wordt gebruikt om geëxtraheerde gegevens aan het oorspronkelijke document te koppelen.

### doc_type
- **Betekenis**: Type of categorie van het document.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Tekenreeks zoals "MEDI_ORDER".
- **Opmerking**: Helpt bij het categoriseren van documenten voor verwerking en analyse.

### extracted_data
- **Betekenis**: JSON-structuur met gedetailleerde gegevens die uit het document zijn geëxtraheerd.
- **Rol**: Gegevensveld.
- **Typische inhoud**: JSON-tekst met velden, waarden en extractiemetagegevens.
- **Opmerking**: Slaat de resultaten van het extractieproces van het document op.

### created_by
- **Betekenis**: Identifier van de gebruiker die het documentrecord heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Geheel getal dat een gebruikers-ID vertegenwoordigt.
- **Opmerking**: Houdt bij welke gebruiker het document in het systeem heeft ingevoerd.

### created_on
- **Betekenis**: Tijdstempel dat aangeeft wanneer het documentrecord is aangemaakt.
- **Rol**: Technisch veld.
- **Typische inhoud**: Datum en tijd met tijdzone-informatie.
- **Opmerking**: Nuttig voor auditing en het volgen van de levenscyclus van het document.

### last_modified_on
- **Betekenis**: Tijdstempel dat de laatste wijziging van het documentrecord aangeeft.
- **Rol**: Technisch veld.
- **Typische inhoud**: Datum en tijd met tijdzone-informatie.
- **Opmerking**: Helpt wijzigingen en updates van het documentrecord te volgen.

### is_deleted
- **Betekenis**: Vlag die aangeeft of het documentrecord als verwijderd is gemarkeerd.
- **Rol**: Statusveld.
- **Typische inhoud**: Booleaanse waarde.
- **Opmerking**: Maakt zachte verwijdering van records mogelijk, zodat herstel indien nodig mogelijk is.

### filename
- **Betekenis**: Naam van het bestand dat bij het document hoort.
- **Rol**: Beschrijvend veld.
- **Typische inhoud**: Tekenreeks, bijv. "7.pdf".
- **Opmerking**: Biedt een verwijzing naar het fysieke bestand dat bij de documentvermelding hoort.

```

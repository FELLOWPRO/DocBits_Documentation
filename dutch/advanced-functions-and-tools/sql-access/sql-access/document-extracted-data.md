# Document extracted data

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_id`: intern
* `field_name`: intern
* `field_value`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `field_type`: intern

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.document_extracted_data`

## Inleiding

De tabel `public.document_extracted_data` is ontworpen om geëxtraheerde gegevens uit diverse documenten op te slaan, waarschijnlijk ten behoeve van documentverwerking en -analyse. Elk item in de tabel komt overeen met een specifiek veld dat uit een document is geëxtraheerd, zoals een factuur, en bevat metadata over het extractieproces. De tabel vergemakkelijkt het volgen en beheren van documentgegevens door deze te koppelen aan organisaties en specifieke documenten.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk geëxtraheerd gegeven.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een als UUID geformatteerde reeks die het geëxtraheerde gegevensrecord uniek identificeert.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan de documentgegevens is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een als UUID geformatteerde reeks die de organisatie vertegenwoordigt.

### doc_id
- **Betekenis**: Identificatie voor het document waaruit de gegevens zijn geëxtraheerd.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een als UUID geformatteerde reeks die het document vertegenwoordigt.

### field_name
- **Betekenis**: De naam van het veld dat uit het document is geëxtraheerd.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeksen zoals 'invoice_id', 'invoice_date', enz., die het type geëxtraheerde gegevens aangeven.

### field_value
- **Betekenis**: De waarde die aan het geëxtraheerde veld is gekoppeld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeksen die verschillende gegevenstypen vertegenwoordigen, zoals factuurnummers, data of bedragen.

### created_by
- **Betekenis**: De identificatie van de gebruiker of het proces dat het gegeven heeft aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Integer die een gebruikers-ID of proces-ID vertegenwoordigt.

### created_on
- **Betekenis**: De tijdstempel van wanneer het gegeven is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Tijdstempel met tijdzonegegevens die de aanmaakdatum en -tijd aangeven.

### last_modified_on
- **Betekenis**: De tijdstempel van de laatste wijziging aan het gegeven.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Tijdstempel met tijdzonegegevens die de laatste wijzigingsdatum en -tijd aangeven (kan null zijn indien nooit gewijzigd).

### is_deleted
- **Betekenis**: Een vlag die aangeeft of het gegeven als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde, waarbij `False` actieve items aangeeft en `True` verwijderde items.

### field_type
- **Betekenis**: Het type gegevens dat in de kolom `field_value` is opgeslagen.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeksen zoals 'date', 'AMOUNT', of null als het type niet is gespecificeerd.

Dit gestructureerde gegevensmodel maakt efficiënte opslag en opvraging van documentgerelateerde gegevens mogelijk, ter ondersteuning van een reeks toepassingen van factuurverwerking tot compliancebeheer.
```

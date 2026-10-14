# Document table column

## Kolommen

* `id`: intern
* `document_table_id`: intern
* `table_name`: intern
* `org_id`: ID naar organisatie
* `column_name`: intern
* `column_type`: intern
* `title`: intern
* `translation_key`: intern
* `sort_order`: integer
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor `public.document_table_column`

## Inleiding

De tabel `public.document_table_column` lijkt te zijn ontworpen om metadata op te slaan over kolommen in diverse documentgerelateerde tabellen, zoals factuur- of pakbon-tabellen. Deze metadata bevat informatie over de naam, het type en de eigenschappen van elke kolom, evenals organisatorische en technische identificatoren. De tabel ondersteunt de dynamische generatie en het beheer van documentschema's binnen het systeem.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk kolomitem in de tabel.
- **Rol**: Primaire sleutel.
- **Opmerking**: Meestal een UUID-reeks die een rij in deze tabel uniek identificeert.

### document_table_id
- **Betekenis**: Verwijst naar de tabel die het document bevat waar deze kolom deel van uitmaakt.
- **Rol**: Vreemde sleutel.
- **Opmerking**: Waarschijnlijk een UUID die linkt naar een andere tabel waarin document-tabellen zijn gedefinieerd.

### table_name
- **Betekenis**: De naam van de documenttabel waartoe deze kolom behoort.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Namen zoals `INVOICE_TABLE`, `DELIVERY_NOTE_TABLE`.
- **Opmerking**: Vergemakkelijkt het begrip van tot welke documentstructuur de kolom behoort.

### org_id
- **Betekenis**: Identificatie voor de organisatie die eigenaar is van de documenttabel of deze beheert.
- **Rol**: Vreemde sleutel.
- **Opmerking**: Meestal een UUID die linkt naar een organisatie-entiteit.

### column_name
- **Betekenis**: De technische naam van de kolom binnen de documenttabel.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Namen zoals `COUNTRY_ORIGIN`, `ORDERED_QUANTITY`.
- **Opmerking**: Vertegenwoordigt de daadwerkelijke veldnaam in de documenttabel.

### column_type
- **Betekenis**: Beschrijft het gegevenstype van de kolom.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: `STRING`, `DATE`.
- **Opmerking**: Geeft aan welk soort gegevens in de kolom wordt opgeslagen.

### title
- **Betekenis**: Een leesbare titel of label voor de kolom.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: `COUNTRY_ORIGIN`, `Ordered Quantity`.
- **Opmerking**: Gebruikt voor het weergeven van kolomnamen op een gebruiksvriendelijke manier.

### translation_key
- **Betekenis**: Sleutel die wordt gebruikt voor internationalisering en lokalisatie van de kolomtitel.
- **Rol**: Technisch veld.
- **Opmerking**: Momenteel leeg in de voorbeeldgegevens, wat wijst op optioneel gebruik.

### sort_order
- **Betekenis**: Definieert de volgorde van kolommen bij weergave.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integers zoals `16`, `5`.
- **Opmerking**: Bepaalt de volgorde van kolommen in de documenttabelweergave.

### clean_field
- **Betekenis**: Geeft aan of de kolom opgeschoonde (sanitized) gegevens bevat.
- **Rol**: Boolean vlag.
- **Typische Inhoud**: `True` of `False`.
- **Opmerking**: Gebruikt voor gegevensvalidatie of opschoonstatus.

### alphanumeric_field
- **Betekenis**: Specificeert of de kolom moet worden behandeld als een alfanumeriek veld.
- **Rol**: Boolean vlag.
- **Typische Inhoud**: `True` of `False`.
- **Opmerking**: Nuttig voor invoervalidatie of formattering.

### created_by
- **Betekenis**: Identificatie van de gebruiker die dit kolomitem heeft aangemaakt.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integerwaarden zoals `1`, `8`.
- **Opmerking**: Linkt naar een gebruiker of systeementiteit die verantwoordelijk is voor de aanmaak.

### created_on
- **Betekenis**: Tijdstempel van wanneer het kolomitem is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Datum- en tijdwaarden in UTC.
- **Opmerking**: Nuttig voor auditing en het bijhouden van wijzigingen.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging aan het kolomitem.
- **Rol**: Technisch veld.
- **Opmerking**: Momenteel `None` in voorbeeldgegevens, wat aangeeft dat er na aanmaak geen wijziging heeft plaatsgevonden.

### is_deleted
- **Betekenis**: Geeft aan of het kolomitem logisch is verwijderd.
- **Rol**: Boolean vlag.
- **Typische Inhoud**: `True` of `False`.
- **Opmerking**: Helpt bij het beheren van soft-deletions zonder gegevens fysiek te verwijderen.
```

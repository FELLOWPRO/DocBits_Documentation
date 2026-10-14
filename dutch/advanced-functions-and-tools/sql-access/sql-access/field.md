# Field

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type`: DOC-type
* `is_sub_doc_type_field`: boolean
* `profile`: intern
* `field_name`: intern
* `field_type`: intern
* `title`: intern
* `translation_key`: intern
* `hide_label`: boolean
* `input_type`: intern
* `input_size`: intern
* `icon_left`: intern
* `icon_right`: intern
* `icon_above`: intern
* `group_id`: intern
* `row_order`: integer
* `sort_order`: integer
* `fuzzy_name`: intern
* `fuzzy_field`: intern
* `fuzzy_primary_field`: boolean
* `label_align`: intern
* `calculation_formula`: tekst
* `clean_field`: boolean
* `alphanumeric_field`: boolean
* `placeholder`: intern
* `coordinates`: intern
* `normalized_coordinates`: intern
* `threshold`: intern
* `reference_point`: intern
* `checkbox_group`: intern
* `list_of_values`: intern
* `enforce_list_of_values`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `costing_element`: intern
* `erp_field_name`: intern

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.field`

## Inleiding

De tabel `public.field` is ontworpen om metadata en configuratie te beheren voor verschillende velden die geassocieerd zijn met documenten, waarschijnlijk binnen een verzekeringsdomein. Elke rij in de tabel vertegenwoordigt een specifieke veldconfiguratie, inclusief het type, label, zichtbaarheidsinstellingen en andere eigenschappen die bepalen hoe het veld moet worden gepresenteerd en verwerkt.

## Kolommen

### id
- **Betekenis**: Unieke identificatie voor elke veldconfiguratie.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een UUID-reeks die elk item in de tabel uniek identificeert.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan de veldconfiguratie is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID die verwijst naar een organisatie.

### doc_type
- **Betekenis**: Specificeert het documenttype waarmee het veld is geassocieerd.
- **Rol**: Mogelijk een vreemde sleutel of een categorische identificatie.
- **Typische Inhoud**: Een reeks in het formaat `INSURANCE_DOCUMENTS_<UUID>` die het documenttype aangeeft.

### is_sub_doc_type_field
- **Betekenis**: Geeft aan of het veld een sub-type is van het documenttype.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### profile
- **Betekenis**: Definieert potentieel het profiel of de reikwijdte van het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Vaak leeg of een korte tekstuele beschrijving.

### field_name
- **Betekenis**: De interne naam van het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks die de naam van het veld in een technische context vertegenwoordigt (bijv. `Schadennummer`).

### field_type
- **Betekenis**: Definieert het type gegevens dat het veld bevat.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Beschrijvende reeksen zoals `STRING`, `AMOUNT`.

### title
- **Betekenis**: De weergavetitel voor het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks in hoofdletters die wordt gebruikt voor het weergeven van het label van het veld.

### translation_key
- **Betekenis**: Sleutel voor vertaling naar verschillende talen.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Reeks in kleine letters die de vertaalsleutel vertegenwoordigt.

### hide_label
- **Betekenis**: Geeft aan of het label van het veld verborgen moet worden in de UI.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### input_type
- **Betekenis**: Specificeert de invoermethode voor het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Kan leeg zijn of reeksen bevatten die het invoertype definiëren.

### input_size
- **Betekenis**: Bepaalt de grootte van het invoerveld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Kan leeg zijn of reeksen bevatten die de invoergrootte definiëren.

### icon_left
- **Betekenis**: Icoon dat aan de linkerkant van het veld wordt weergegeven.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat icoon-identificatoren.

### icon_right
- **Betekenis**: Icoon dat aan de rechterkant van het veld wordt weergegeven.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat icoon-identificatoren.

### icon_above
- **Betekenis**: Icoon dat boven het veld wordt weergegeven.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat icoon-identificatoren.

### group_id
- **Betekenis**: Identificatie voor de groep velden waartoe dit veld behoort.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID die verwijst naar een groep velden.

### row_order
- **Betekenis**: Bepaalt de volgorde van het veld in een lijst of formulier.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Integer die de positie aangeeft.

### sort_order
- **Betekenis**: Specificeert de sorteervolgorde voor het veld.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Integer die de sorteervoorrang definieert.

### fuzzy_name
- **Betekenis**: Een alternatieve naam voor fuzzy matching.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Vaak leeg of bevat een reeks voor matchingdoeleinden.

### fuzzy_field
- **Betekenis**: Specificeert of het veld wordt gebruikt in fuzzy matching.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat een reeks.

### fuzzy_primary_field
- **Betekenis**: Geeft aan of dit het primaire veld is voor fuzzy matching.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### label_align
- **Betekenis**: Uitlijningsinstelling voor het veldlabel.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Vaak leeg of bevat uitlijningsinformatie (bijv. left, right, center).

### calculation_formula
- **Betekenis**: Formule gebruikt voor berekeningen waarbij het veld betrokken is.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Tekst met een formule of berekeningslogica.

### clean_field
- **Betekenis**: Geeft aan of het veld onderworpen moet worden aan gegevensreiniging.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### alphanumeric_field
- **Betekenis**: Specificeert of het veld alleen alfanumerieke tekens mag accepteren.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### placeholder
- **Betekenis**: Placeholder-tekst voor het invoerveld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Vaak leeg of bevat sturende tekst.

### coordinates
- **Betekenis**: Coördinaatgegevens geassocieerd met het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat coördinaatinformatie.

### normalized_coordinates
- **Betekenis**: Genormaliseerde versie van coördinaten voor consistentie.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat genormaliseerde coördinaatgegevens.

### threshold
- **Betekenis**: Drempelwaarde gerelateerd aan veldvalidatie of -verwerking.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat drempelwaarden.

### reference_point
- **Betekenis**: Referentiepunt gebruikt in berekeningen of positionering.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Vaak leeg of bevat referentiepuntgegevens.

### checkbox_group
- **Betekenis**: Groeperings-ID voor checkbox-velden.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat groepsidentificatoren.

### list_of_values
- **Betekenis**: Specificeert een lijst met toegestane waarden voor het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat een lijst met waarden.

### enforce_list_of_values
- **Betekenis**: Geeft aan of de lijst met waarden strikt moet worden afgedwongen.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### created_by
- **Betekenis**: Identificatie voor de gebruiker die het velditem heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integer die naar een gebruikers-ID verwijst.

### created_on
- **Betekenis**: Tijdstempel van wanneer het veld is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Datum en tijd in UTC.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging aan het veld.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Datum en tijd in UTC.

### is_deleted
- **Betekenis**: Geeft aan of het veld als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Boolean waarde (True of False).

### costing_element
- **Betekenis**: Kosten-element geassocieerd met het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat kosten-element-identificatoren.

### erp_field_name
- **Betekenis**: Naam van het veld zoals gebruikt in ERP-systemen.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal leeg of bevat ERP-specifieke veldnamen.

Deze documentatie biedt een gedetailleerd overzicht van de structuur en het doel van elke kolom binnen de tabel `public.field`. Het dient als gids voor ontwikkelaars om het gegevensmodel en de toepassing ervan in het systeem te begrijpen.
```

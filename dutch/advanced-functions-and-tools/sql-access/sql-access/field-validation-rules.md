# Field validation rules

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `field_id`: intern
* `doc_type`: DOC-type
* `is_sub_doc_type_field`: boolean
* `profile`: intern
* `field_name`: intern
* `field_length`: integer
* `field_label`: intern
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: intern
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `additional_attributes`: tekst

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.field_validation_rules`

## Inleiding

De tabel `public.field_validation_rules` lijkt metadata en validatieregels op te slaan voor velden die geassocieerd zijn met diverse documenttypen binnen een organisatie. Het wordt waarschijnlijk gebruikt om gegevensintegriteit en consistentie over formulieren of documenten af te dwingen door vereisten te specificeren, zoals of een veld verplicht is, de lengte, zichtbaarheid en eventuele validatiepatronen die moeten worden toegepast.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elke veldvalidatieregel.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een UUID-reeks die een record uniek identificeert.

### org_id
- **Betekenis**: Identificatie voor de organisatie waarop de validatieregel van toepassing is.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die verwijst naar een specifieke organisatie.

### field_id
- **Betekenis**: Identificatie voor het specifieke veld waarmee de validatieregel is geassocieerd.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die verwijst naar een specifiek veld.

### doc_type
- **Betekenis**: Specificeert het documenttype waarmee de veldvalidatieregel is geassocieerd.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks die het type document aangeeft (bijv. `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Betekenis**: Geeft aan of het veld deel uitmaakt van een sub-documenttype.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### profile
- **Betekenis**: Vertegenwoordigt het profiel of de context waarin de veldvalidatie wordt toegepast.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks zoals `DEFAULT`.

### field_name
- **Betekenis**: De naam van het veld waarvoor de validatieregel is gedefinieerd.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks die de veldnaam vertegenwoordigt (bijv. `Test`).

### field_length
- **Betekenis**: De maximaal toegestane lengte voor de inhoud van het veld.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een integer die de karakterlimiet specificeert.

### field_label
- **Betekenis**: Het label of de weergavenaam voor het veld in de gebruikersinterface.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal null in de voorbeeldgegevens.

### is_required
- **Betekenis**: Geeft aan of het veld verplicht is voor het document.
- **Rol**: Beperkingsindicator.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### is_readonly
- **Betekenis**: Specificeert of het veld bewerkbaar of alleen-lezen is.
- **Rol**: Beperkingsindicator.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### is_hidden
- **Betekenis**: Geeft aan of het veld verborgen moet blijven in de gebruikersinterface.
- **Rol**: Beperkingsindicator.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### force_validation
- **Betekenis**: Bepaalt of validatie moet worden afgedwongen, ongeacht andere omstandigheden.
- **Rol**: Beperkingsindicator.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### validation_pattern
- **Betekenis**: Een patroon (waarschijnlijk regex) waaraan de inhoud van het veld moet voldoen.
- **Rol**: Validatieregel.
- **Typische Inhoud**: Meestal null in de voorbeeldgegevens.

### confidence_threshold
- **Betekenis**: Het minimale betrouwbaarheidsniveau dat vereist is voor de validatie van het veld.
- **Rol**: Validatiebeperking.
- **Typische Inhoud**: Een integerwaarde die de betrouwbaarheidsdrempel vertegenwoordigt.

### match_score_threshold
- **Betekenis**: De minimale match-score die vereist is voor de validatie van de veldinhoud.
- **Rol**: Validatiebeperking.
- **Typische Inhoud**: Een integerwaarde die de match-scoredrempel vertegenwoordigt.

### created_by
- **Betekenis**: Identificatie voor de gebruiker die deze validatieregel heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een integer die de gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: Tijdstempel die aangeeft wanneer de validatieregel is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Een tijdstempel met tijdzone.

### last_modified_on
- **Betekenis**: Tijdstempel die de laatste wijziging van de validatieregel aangeeft.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Een tijdstempel met tijdzone, kan null zijn indien nooit gewijzigd.

### is_deleted
- **Betekenis**: Geeft aan of de validatieregel als verwijderd is gemarkeerd.
- **Rol**: Soft delete indicator.
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### additional_attributes
- **Betekenis**: Slaat extra attributen of metadata op die geassocieerd zijn met de veldvalidatieregel.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Tekst, vaak null in de voorbeeldgegevens.
```

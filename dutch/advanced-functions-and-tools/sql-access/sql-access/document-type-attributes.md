# Document type attributes

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type_key`: intern
* `sub_doc_type_key`: intern
* `attribute_key`: intern
* `attribute_value`: text
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `sub_org_id`: intern

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.document_type_attributes`

## Inleiding

De tabel `public.document_type_attributes` is ontworpen voor het beheren van attributen die gerelateerd zijn aan diverse documenttypen binnen een organisatorische context. Deze tabel ondersteunt waarschijnlijk configuratie- of metadatabeheer voor verschillende soorten documenten, zoals facturen of pakbonnen, door specifieke attributen te koppelen aan elk documenttype.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk record in de tabel.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een UUID-reeks die een rij in de tabel uniek identificeert.

### org_id
- **Betekenis**: Vertegenwoordigt de organisatie waartoe het documenttype-attribuut behoort.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die verwijst naar een organisatie.

### doc_type_key
- **Betekenis**: Het type document waarop het attribuut van toepassing is (bijv. INVOICE, DELIVERY_NOTE).
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks die een documenttype vertegenwoordigt.

### sub_doc_type_key
- **Betekenis**: Een specifiekere categorisering binnen het documenttype, indien van toepassing.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Meestal `None`, wat aangeeft dat het niet altijd wordt gebruikt.

### attribute_key
- **Betekenis**: De specifieke attribuut- of eigenschapssleutel gerelateerd aan het documenttype.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een reeks die een attribuutsleutel vertegenwoordigt, zoals `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Betekenis**: De waarde die geassocieerd is met de attribuutsleutel voor het documenttype.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een tekstuele of numerieke waarde die de waarde van het attribuut geeft, bijv. `true`, `123`.

### created_by
- **Betekenis**: De identificatie van de gebruiker die het record heeft aangemaakt.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Een integer die een gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: De tijdstempel van wanneer het record is aangemaakt.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Een tijdstempel met tijdzone die aangeeft wanneer het record is aangemaakt.

### last_modified_on
- **Betekenis**: De tijdstempel van de laatste wijziging aan het record.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Een tijdstempel met tijdzone die de laatste updatetijd aangeeft.

### is_deleted
- **Betekenis**: Geeft aan of het record als verwijderd is gemarkeerd.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Een boolean waarde, `false` impliceert dat het record actief is.

### sub_org_id
- **Betekenis**: Vertegenwoordigt een suborganisatie binnen de hoofdorganisatie, indien van toepassing.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Meestal `None`, wat aangeeft dat het niet altijd wordt gebruikt.
```

Deze documentatie biedt een gestructureerd overzicht van de tabel `public.document_type_attributes`, waardoor ontwikkelaars het doel en het gebruik van elke kolom kunnen begrijpen.

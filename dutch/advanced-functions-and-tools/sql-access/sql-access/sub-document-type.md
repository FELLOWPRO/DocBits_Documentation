# Documentsubtype

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type_key`: intern
* `sub_doc_type_key`: intern
* `name`: intern
* `title`: intern
* `translation_key`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean

## Analyse & Beschrijving

```markdown
# Tabel `public.sub_document_type`

## Inleiding

De tabel `sub_document_type` is bedoeld voor het opslaan van gedetailleerde informatie over diverse subdocumenttypen binnen een organisatie. Dit omvat unieke identificatoren, organisatiekoppelingen, beschrijvende namen en metadata over het aanmaken en wijzigen van deze subdocumenttypen. De tabel houdt ook de soft-delete-status van records bij.

## Kolombeschrijvingen

### id
- **Betekenis**: Deze kolom bevat de unieke identificatie van elk subdocumenttype.
- **Rol**: Primaire sleutel.
- **Typische inhoud**: Een UUID-reeks die een subdocumenttype-record uniek identificeert (bijv. `'c2cc2d62-e4be-491b-a43e-c4123dff5aa6'`).

### org_id
- **Betekenis**: Deze kolom geeft de organisatie aan waartoe het subdocumenttype behoort.
- **Rol**: Vreemde sleutel.
- **Typische inhoud**: Een UUID-reeks die naar een organisatie verwijst (bijv. `'23f3d697-7411-4c95-981d-faf089d266be'`).

### doc_type_key
- **Betekenis**: Geeft de documenttypesleutel weer die aan het subdocumenttype is gekoppeld.
- **Rol**: Vreemde sleutel (impliciet door de naamgevingsconventie).
- **Typische inhoud**: Een tekenreekssleutel die naar een breder documenttype verwijst (bijv. `'TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### sub_doc_type_key
- **Betekenis**: Duidt een specifieke sleutel aan voor het subdocumenttype binnen een documentcategorie.
- **Rol**: Unieke identificator voor het subdocumenttype binnen het bereik van een documenttype.
- **Typische inhoud**: Een tekenreekssleutel die een subdocumenttype uniek identificeert (bijv. `'TEST_SUB_TEST_23f3d697-7411-4c95-981d-faf089d266be'`).

### name
- **Betekenis**: Bevat een korte naam of code voor het subdocumenttype.
- **Rol**: Beschrijvend.
- **Typische inhoud**: Een beknopte identificator of code (bijv. `'TEST_SUB_TEST'`).

### title
- **Betekenis**: Bevat een voor mensen leesbare titel voor het subdocumenttype.
- **Rol**: Beschrijvend.
- **Typische inhoud**: Een beschrijvende titel voor gebruikersinterfaces of rapporten (bijv. `'Test Sub Test'`).

### translation_key
- **Betekenis**: Sleutel die voor internationalisering en lokalisatie wordt gebruikt om de naam van het subdocumenttype te vertalen.
- **Rol**: Technisch.
- **Typische inhoud**: Een tekenreeks die in vertaalbestanden wordt gebruikt (bijv. `'test_sub_test'`).

### created_by
- **Betekenis**: Identificeert de gebruiker die het subdocumenttype-item heeft aangemaakt.
- **Rol**: Technisch.
- **Typische inhoud**: Een integer die het gebruikers-ID vertegenwoordigt (bijv. `8`).

### created_on
- **Betekenis**: Tijdstempel die aangeeft wanneer het subdocumenttype is aangemaakt.
- **Rol**: Technisch.
- **Typische inhoud**: Een tijdstempel met tijdzone (bijv. `2022-12-13 08:34:13.932893+00:00`).

### last_modified_on
- **Betekenis**: Tijdstempel die aangeeft wanneer het subdocumenttype voor het laatst is gewijzigd.
- **Rol**: Technisch.
- **Typische inhoud**: Een tijdstempel met tijdzone, mogelijk `None` als het na aanmaak nooit is gewijzigd.

### is_deleted
- **Betekenis**: Boolean-vlag die aangeeft of het subdocumenttype via soft delete is verwijderd.
- **Rol**: Technisch.
- **Typische inhoud**: `True` of `False` als aanduiding van de verwijderstatus (bijv. `False`).
```

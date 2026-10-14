# Documents

## Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `batch_id`: intern
* `doc_path`: intern
* `doc_type`: DOC-type
* `status`: intern
* `message`: tekst
* `export_attempts`: integer
* `last_attempted_on`: tijdstempel met tijdzone
* `next_attempt_on`: tijdstempel met tijdzone
* `assigned_to`: integer
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `task_id`: intern
* `filename`: intern
* `assigned_on`: tijdstempel met tijdzone
* `pages`: integer
* `auto_processed`: boolean
* `exception_info`: tekst
* `doc_language`: Taal
* `is_trimmed`: boolean
* `doc_origin`: Documentoorsprong
* `doc_locale`: Documentlocale
* `is_doc2landing_doc`: boolean
* `extraction_time`: dubbele precisie
* `export_time`: dubbele precisie
* `po_all_matched`: boolean
* `restart_allowed`: boolean
* `table_version`: intern
* `force_ocr`: boolean
* `locked_by`: integer
* `locked_on`: tijdstempel met tijdzone
* `lock_renewed_on`: tijdstempel met tijdzone
* `lock_key`: intern
* `last_saved_by`: integer
* `last_saved_on`: tijdstempel met tijdzone
* `document_version`: integer
* `lock_session_key`: intern
* `sub_org_id`: intern
* `doc_source`: intern
* `sub_doc_type`: intern
* `assigned_to_group`: intern
* `status_changed_on`: tijdstempel met tijdzone
* `improve_quality`: boolean
* `priority`: integer
* `metadata_field`: json
* `doc_classification_label`: intern
* `doc_start_page`: integer
* `doc_classification_class`: intern
* `celery_task_token`: intern
* `celery_task_attempt`: integer
* `celery_task_priority`: integer
* `has_zugferd`: boolean
* `has_peppol`: boolean
* `timestamp_for_validation`: tijdstempel met tijdzone
* `exception_details`: tekst
* `has_annotated_version`: boolean
* `po_match_status`: intern
* `tr_ocr_extracted_data`: tekst
* `pending_workflow_execution`: boolean
* `extracted_document_id`: intern
* `extracted_supplier_id`: intern
* `classification_manually_corrected`: boolean
* `supplier_as_org_id`: intern
* `extracted_data_basic`: jsonb
* `celery_task_queue`: intern
* `extracted_data`: jsonb
* `extracted_data_jsonb`: jsonb
* `warnings`: jsonb

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.documents`

## Inleiding

De tabel `public.documents` is ontworpen voor het opslaan en beheren van metadata en verwerkingsinformatie met betrekking tot documentafhandeling binnen een organisatie. Dit omvat het bijhouden van de documentstatus, verwerkingspogingen, taal en andere administratieve details. De tabel is gestructureerd ter ondersteuning van documentclassificatie, verwerkingsworkflows en gebruikerstoewijzingen, waardoor deze integraal deel uitmaakt van het documentbeheersysteem.

## Kolombeschrijvingen

### id
- **Betekenis**: Unieke identificatie voor elk document.
- **Rol**: Primaire sleutel.
- **Typische Inhoud**: Een UUID-reeks die het document vertegenwoordigt.

### org_id
- **Betekenis**: Identificatie voor de organisatie die aan het document is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die de organisatie vertegenwoordigt.

### batch_id
- **Betekenis**: Identificatie voor de batch waarin het document is verwerkt.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die de batch vertegenwoordigt.

### doc_path
- **Betekenis**: Bestandspad waar het document is opgeslagen.
- **Rol**: Technisch veld.
- **Typische Inhoud**: Pad naar het documentbestand, bijv. `documents/{id}/{id}.pdf`.

### doc_type
- **Betekenis**: Type document dat wordt opgeslagen (bijv. factuur).
- **Rol**: Documentclassificatie.
- **Typische Inhoud**: Een reeks zoals `INVOICE`.

### status
- **Betekenis**: Huidige verwerkingsstatus van het document.
- **Rol**: Workflow-indicator.
- **Typische Inhoud**: Een reeks die de status aangeeft, bijv. `ready_for_validation`.

### message
- **Betekenis**: Informatie over de verwerkingsstatus of fouten van het document.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Tekst die fouten of berichten met betrekking tot documentverwerking beschrijft.

### export_attempts
- **Betekenis**: Aantal keren dat er een poging is gedaan om het document te exporteren.
- **Rol**: Verwerkingstracking.
- **Typische Inhoud**: Integer aantal exportpogingen.

### last_attempted_on
- **Betekenis**: Tijdstempel van de laatste poging om het document te verwerken of te exporteren.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### next_attempt_on
- **Betekenis**: Geplande tijdstempel voor de volgende poging om het document te verwerken of te exporteren.
- **Rol**: Planningsveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### assigned_to
- **Betekenis**: Identificatie voor de gebruiker die aan dit document is toegewezen.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### created_by
- **Betekenis**: Identificatie voor de gebruiker die het document heeft aangemaakt of geüpload.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: Tijdstempel van wanneer het document is aangemaakt of geüpload.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### last_modified_on
- **Betekenis**: Tijdstempel van de laatste wijziging aan het documentrecord.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### is_deleted
- **Betekenis**: Geeft aan of het document als verwijderd is gemarkeerd.
- **Rol**: Logische verwijderingsvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### task_id
- **Betekenis**: Identificatie voor de taak die aan de documentverwerking is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die de taak vertegenwoordigt.

### filename
- **Betekenis**: Oorspronkelijke bestandsnaam van het document.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Naam van het bestand, bijv. `document.pdf`.

### assigned_on
- **Betekenis**: Tijdstempel wanneer het document aan een gebruiker is toegewezen.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### pages
- **Betekenis**: Aantal pagina's in het document.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integer die het aantal pagina's aangeeft.

### auto_processed
- **Betekenis**: Geeft aan of het document automatisch is verwerkt.
- **Rol**: Verwerkingsstatusvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### exception_info
- **Betekenis**: Informatie over eventuele uitzonderingen (exceptions) tijdens de verwerking.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Tekst die verwerkingsuitzonderingen beschrijft.

### doc_language
- **Betekenis**: Taal van de inhoud van het document.
- **Rol**: Taalclassificatie.
- **Typische Inhoud**: ISO-taalcode, bijv. `en`, `nl`.

### is_trimmed
- **Betekenis**: Geeft aan of het document is bijgesneden of gecropt.
- **Rol**: Documentwijzigingsvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### doc_origin
- **Betekenis**: Oorsprong van het document, geeft mogelijk het land of het bronsysteem aan.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Landcode of oorsprongsidentificatie, bijv. `NL`.

### doc_locale
- **Betekenis**: Locale-instellingen van het document, geeft taal en regio aan.
- **Rol**: Locale-classificatie.
- **Typische Inhoud**: Locale-reeks, bijv. `nl_NL`.

### is_doc2landing_doc
- **Betekenis**: Geeft aan of het document gerelateerd is aan een specifieke verwerkingsworkflow (Doc2Landing).
- **Rol**: Workflow-vlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### extraction_time
- **Betekenis**: Tijd die nodig was om gegevens uit het document te extraheren.
- **Rol**: Prestatiemetriek.
- **Typische Inhoud**: Double precision waarde die de extractietijd vertegenwoordigt.

### export_time
- **Betekenis**: Tijd die nodig was om het document te exporteren.
- **Rol**: Prestatiemetriek.
- **Typische Inhoud**: Double precision waarde die de exporttijd vertegenwoordigt.

### po_all_matched
- **Betekenis**: Geeft aan of alle inkooporders die gerelateerd zijn aan het document zijn gematcht.
- **Rol**: Matching-statusvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### restart_allowed
- **Betekenis**: Geeft aan of de documentverwerking opnieuw kan worden gestart.
- **Rol**: Workflow-controlevlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### table_version
- **Betekenis**: Versie van de tabelstructuur die voor het document is gebruikt.
- **Rol**: Versiebeheer.
- **Typische Inhoud**: Reeks die de versie aangeeft, bijv. `v3`.

### force_ocr
- **Betekenis**: Geeft aan of OCR-verwerking voor het document is geforceerd.
- **Rol**: Verwerkingscontrolevlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### locked_by
- **Betekenis**: Identificatie voor de gebruiker die het document heeft vergrendeld voor bewerking.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### locked_on
- **Betekenis**: Tijdstempel wanneer het document is vergrendeld voor bewerking.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### lock_renewed_on
- **Betekenis**: Tijdstempel wanneer de documentvergrendeling voor het laatst is vernieuwd.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### lock_key
- **Betekenis**: Sleutel die aan de documentvergrendeling is gekoppeld.
- **Rol**: Vergrendelingscontrole.
- **Typische Inhoud**: Reeks die de vergrendelingssleutel vertegenwoordigt.

### last_saved_by
- **Betekenis**: Identificatie voor de gebruiker die het document als laatste heeft opgeslagen.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### last_saved_on
- **Betekenis**: Tijdstempel wanneer het document voor het laatst is opgeslagen.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### document_version
- **Betekenis**: Versienummer van het document.
- **Rol**: Versietracking.
- **Typische Inhoud**: Integer die de documentversie vertegenwoordigt.

### lock_session_key
- **Betekenis**: Sessiesleutel die aan de documentvergrendeling is gekoppeld.
- **Rol**: Vergrendelingscontrole.
- **Typische Inhoud**: Reeks die de sessiesleutel vertegenwoordigt.

### sub_org_id
- **Betekenis**: Identificatie voor een suborganisatie die aan het document is gekoppeld.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die de suborganisatie vertegenwoordigt.

### doc_source
- **Betekenis**: Bronsysteem of oorsprong van het document.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Reeks die de bron aangeeft, bijv. `doc2app`.

### sub_doc_type
- **Betekenis**: Subtype-classificatie van het document.
- **Rol**: Documentclassificatie.
- **Typische Inhoud**: Reeks die het subtype aangeeft.

### assigned_to_group
- **Betekenis**: Identificatie voor de groep waaraan het document is toegewezen.
- **Rol**: Toewijzingstracking.
- **Typische Inhoud**: Een UUID-reeks die de groep vertegenwoordigt.

### status_changed_on
- **Betekenis**: Tijdstempel wanneer de status van het document voor het laatst is gewijzigd.
- **Rol**: Tijdstempelveld.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### improve_quality
- **Betekenis**: Geeft aan of er kwaliteitsverbeteringsprocessen op het document worden toegepast.
- **Rol**: Kwaliteitscontrolevlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### priority
- **Betekenis**: Verwerkingsprioriteit van het document.
- **Rol**: Workflow-controle.
- **Typische Inhoud**: Integer die het prioriteitsniveau aangeeft.

### metadata_field
- **Betekenis**: JSON-veld met metadata gerelateerd aan het document.
- **Rol**: Metadata-opslag.
- **Typische Inhoud**: JSON-structuur met diverse metadata-velden.

### doc_classification_label
- **Betekenis**: Label dat de classificatie van het document aangeeft.
- **Rol**: Classificatielabel.
- **Typische Inhoud**: Reeks die de classificatie aangeeft, bijv. `INVOICE`.

### doc_start_page
- **Betekenis**: Paginanummer waar de documentinhoud begint.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Integer die de beginpagina aangeeft.

### doc_classification_class
- **Betekenis**: Klasse die de gedetailleerde classificatie van het document aangeeft.
- **Rol**: Classificatiedetail.
- **Typische Inhoud**: Reeks die de classificatieklasse aangeeft.

### celery_task_token
- **Betekenis**: Token voor het volgen van de Celery-taak die aan het document is gekoppeld.
- **Rol**: Taaktracking.
- **Typische Inhoud**: Reeks die het taaktoken vertegenwoordigt.

### celery_task_attempt
- **Betekenis**: Aantal pogingen gedaan voor de Celery-taak.
- **Rol**: Taaktracking.
- **Typische Inhoud**: Integer aantal taakpogingen.

### celery_task_priority
- **Betekenis**: Prioriteitsniveau van de Celery-taak.
- **Rol**: Taakcontrole.
- **Typische Inhoud**: Integer die de taakprioriteit aangeeft.

### has_zugferd
- **Betekenis**: Geeft aan of het document in ZUGFeRD-formaat is.
- **Rol**: Formaatindicator.
- **Typische Inhoud**: Boolean waarde (True of False).

### has_peppol
- **Betekenis**: Geeft aan of het document in PEPPOL-formaat is.
- **Rol**: Formaatindicator.
- **Typische Inhoud**: Boolean waarde (True of False).

### timestamp_for_validation
- **Betekenis**: Tijdstempel voor wanneer het document is gevalideerd.
- **Rol**: Validatietracking.
- **Typische Inhoud**: Datum en tijd met tijdzone.

### exception_details
- **Betekenis**: Gedetailleerde informatie over uitzonderingen tijdens de verwerking.
- **Rol**: Beschrijvend veld.
- **Typische Inhoud**: Tekst met details over de uitzondering.

### has_annotated_version
- **Betekenis**: Geeft aan of er een geannoteerde versie van het document bestaat.
- **Rol**: Versie-indicator.
- **Typische Inhoud**: Boolean waarde (True of False).

### po_match_status
- **Betekenis**: Status van de inkoopordermatching.
- **Rol**: Matching-statusindicator.
- **Typische Inhoud**: Reeks die de matchstatus aangeeft.

### tr_ocr_extracted_data
- **Betekenis**: Door OCR geëxtraheerde gegevens uit het document.
- **Rol**: Gegevensopslag.
- **Typische Inhoud**: Tekst met geëxtraheerde gegevens.

### pending_workflow_execution
- **Betekenis**: Geeft aan of er workflow-executies in afwachting zijn.
- **Rol**: Workflow-statusvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### extracted_document_id
- **Betekenis**: Identificatie voor het geëxtraheerde document.
- **Rol**: Extractietracking.
- **Typische Inhoud**: Een UUID-reeks die het geëxtraheerde document vertegenwoordigt.

### extracted_supplier_id
- **Betekenis**: Identificatie voor de geëxtraheerde leverancier.
- **Rol**: Extractietracking.
- **Typische Inhoud**: Een UUID-reeks die de geëxtraheerde leverancier vertegenwoordigt.

### classification_manually_corrected
- **Betekenis**: Geeft aan of de documentclassificatie handmatig is gecorrigeerd.
- **Rol**: Classificatiestatusvlag.
- **Typische Inhoud**: Boolean waarde (True of False).

### supplier_as_org_id
- **Betekenis**: Identificatie voor de leverancier behandeld als een organisatie.
- **Rol**: Vreemde sleutel.
- **Typische Inhoud**: Een UUID-reeks die de leveranciersorganisatie vertegenwoordigt.

### extracted_data_basic
- **Betekenis**: Basis geëxtraheerde gegevens in JSONB-formaat.
- **Rol**: Gegevensopslag.
- **Typische Inhoud**: JSONB-structuur met geëxtraheerde gegevensvelden.

### celery_task_queue
- **Betekenis**: Naam van de Celery-taakwachtrij.
- **Rol**: Taakbeheer.
- **Typische Inhoud**: Reeks die de wachtrijnaam aangeeft.

### extracted_data
- **Betekenis**: Geëxtraheerde gegevens uit het document in JSONB-formaat.
- **Rol**: Gegevensopslag.
- **Typische Inhoud**: JSONB-structuur met geëxtraheerde gegevensvelden.

### extracted_data_jsonb
- **Betekenis**: JSONB-veld met gedetailleerde geëxtraheerde gegevens.
- **Rol**: Gegevensopslag.
- **Typische Inhoud**: JSONB-structuur met geëxtraheerde gegevensvelden.

### warnings
- **Betekenis**: Waarschuwingen met betrekking tot documentverwerking opgeslagen in JSONB-formaat.
- **Rol**: Waarschuwingsopslag.
- **Typische Inhoud**: JSONB-structuur met waarschuwingsberichten.
```

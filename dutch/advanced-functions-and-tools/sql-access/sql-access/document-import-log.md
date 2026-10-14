# Document Import log

## Kolommen

* `id`: integer
* `org_id`: ID naar organisatie
* `sub_org_id`: intern
* `original_filename`: intern
* `filename`: intern
* `imported_on`: intern
* `source_type`: intern
* `source`: intern
* `success`: boolean
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `import_id`: text
* `extra_data`: text
* `doc_id`: intern
* `email_connection_id`: integer
* `subject`: intern
* `body`: text
* `sender`: intern
* `error_resp`: intern
* `source_received_on`: tijdstempel met tijdzone

## Analyse & Beschrijving

```markdown
# Technische Documentatie voor de Tabel `public.document_import_log`

## Inleiding

De tabel `public.document_import_log` is ontworpen om de details van documentimporten in het systeem te loggen. Het legt informatie vast over elk document, inclusief de herkomst, importstatus en gerelateerde metadata. Deze tabel is essentieel voor het volgen van documentimportactiviteiten en het diagnosticeren van eventuele problemen die zich tijdens het importproces kunnen voordoen.

## Kolombeschrijvingen

### id
- **Betekenis**: Een unieke identificatie voor elk importlogitem.
- **Rol**: Primaire Sleutel (Primary Key)
- **Typische Inhoud**: Opeenvolgende integerwaarden die elk record uniek identificeren.

### org_id
- **Betekenis**: De identificatie voor de organisatie die aan de import is gekoppeld.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: UUID of vergelijkbare unieke reeks die de organisatie vertegenwoordigt.

### sub_org_id
- **Betekenis**: De identificatie voor een suborganisatie of afdeling binnen de hoofdorganisatie.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: UUID of vergelijkbare unieke reeks; kan `None` zijn indien niet van toepassing.

### original_filename
- **Betekenis**: De oorspronkelijke naam van het documentbestand zoals het is geüpload.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks die de bestandsnaam vertegenwoordigt, bijv. `anton_factuur-1.pdf`.

### filename
- **Betekenis**: De naam van het documentbestand nadat het is verwerkt of opgeslagen in het systeem.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks die de bestandsnaam vertegenwoordigt, vaak identiek aan `original_filename`.

### imported_on
- **Betekenis**: De datum en tijd waarop het document is geïmporteerd.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: ISO 8601 geformatteerde tijdstempel.

### source_type
- **Betekenis**: Het type bron waaruit het document is geïmporteerd.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks, bijv. `EMAIL`, die het brontype aangeeft.

### source
- **Betekenis**: Gedetailleerde informatie over de bron van de import.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks die de bron specificeert, bijv. `Email:O365:demo@fellow-digital.de:Tini Test`.

### success
- **Betekenis**: Geeft aan of de import succesvol was.
- **Rol**: Statusveld
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### created_by
- **Betekenis**: De identificatie van de gebruiker die de import heeft geïnitieerd.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Integer die de gebruikers-ID vertegenwoordigt.

### created_on
- **Betekenis**: De datum en tijd waarop het importlogitem is aangemaakt.
- **Rol**: Technisch Veld
- **Typische Inhoud**: Tijdstempel met tijdzone.

### last_modified_on
- **Betekenis**: De datum en tijd waarop het importlogitem voor het laatst is gewijzigd.
- **Rol**: Technisch Veld
- **Typische Inhoud**: Tijdstempel met tijdzone; kan `None` zijn indien niet gewijzigd.

### is_deleted
- **Betekenis**: Geeft aan of het importlogitem als verwijderd is gemarkeerd.
- **Rol**: Statusveld
- **Typische Inhoud**: Boolean waarde (`True` of `False`).

### import_id
- **Betekenis**: Een unieke identificatie voor het importproces.
- **Rol**: Technisch Veld
- **Typische Inhoud**: Reeks of tekst die een unieke proces-ID vertegenwoordigt.

### extra_data
- **Betekenis**: Aanvullende metadata met betrekking tot de import.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: JSON-reeks met extra gegevens, zoals datum, afzender, onderwerp en aantal.

### doc_id
- **Betekenis**: De identificatie voor het document.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: UUID of vergelijkbare unieke reeks; kan `None` zijn.

### email_connection_id
- **Betekenis**: De identificatie voor de e-mailverbinding die bij de import is gebruikt.
- **Rol**: Vreemde Sleutel (Foreign Key)
- **Typische Inhoud**: Integer die de e-mailverbinding-ID vertegenwoordigt; kan `None` zijn.

### subject
- **Betekenis**: De onderwerpregel van de e-mail waaruit het document is geïmporteerd.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks die het e-mailonderwerp vertegenwoordigt.

### body
- **Betekenis**: De inhoud van de e-mail waaruit het document is geïmporteerd.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Tekst met de inhoud van de e-mail; kan `None` zijn.

### sender
- **Betekenis**: Het e-mailadres van de afzender van het document.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Reeks met het e-mailadres van de afzender.

### error_resp
- **Betekenis**: Foutrespons of bericht als de import is mislukt.
- **Rol**: Statusveld
- **Typische Inhoud**: Reeks met foutdetails; kan `None` zijn.

### source_received_on
- **Betekenis**: De datum en tijd waarop het document is ontvangen van de bron.
- **Rol**: Beschrijvend Veld
- **Typische Inhoud**: Tijdstempel met tijdzone.

Deze documentatie biedt een gedetailleerd overzicht van de tabel `public.document_import_log` en de kolommen ervan, die essentieel zijn voor het begrijpen en beheren van documentimporten binnen het systeem.
```

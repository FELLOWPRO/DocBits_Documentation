# Document Status alert

## Tabel `public.document_status_alert`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `doc_type_id`: intern
* `doc_type_key`: intern
* `doc_status`: intern
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `name`: intern
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: intern
* `email_template_id`: intern

### Analyse & Beschrijving

## Tabeldocumentatie: `public.document_status_alert`

### Inleiding

De tabel `public.document_status_alert` lijkt te zijn ontworpen voor het beheren van meldingen (alerts) met betrekking tot documentstatussen binnen een organisatie. Op basis van de kolomnamen slaat de tabel informatie op over diverse documenttypen en hun statussen, inclusief details over notificaties en timing voor meldingen. Deze tabel wordt waarschijnlijk gebruikt om meldingen te triggeren op basis van bepaalde documentstatussen en voorwaarden, mogelijk om gebruikers te informeren of processen te escaleren.

### Kolombeschrijvingen

#### `id`

* **Betekenis**: Unieke identificatie voor elk meldingsrecord.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Een UUID-reeks die elke rij in de tabel uniek identificeert.

#### `org_id`

* **Betekenis**: Identificatie voor de organisatie die aan de melding is gekoppeld.
* **Rol**: Vreemde sleutel.
* **Typische Inhoud**: Een UUID-reeks die linkt naar een organisatierecord.

#### `doc_type_id`

* **Betekenis**: Identificatie voor het documenttype.
* **Rol**: Vreemde sleutel (verondersteld).
* **Typische Inhoud**: Meestal een UUID, hoewel de voorbeeldgegevens `None` tonen, wat aangeeft dat dit veld optioneel kan zijn.

#### `doc_type_key`

* **Betekenis**: Sleutel die het type document vertegenwoordigt.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Een reeks zoals 'INVOICE' of 'XML\_INVOICE'.

#### `doc_status`

* **Betekenis**: Huidige status van het document.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Beschrijvende statusreeksen zoals 'validated\_pending\_approval' of 'error'.

#### `email_address`

* **Betekenis**: E-mailadres waarnaar meldingen worden verzonden.
* **Rol**: Notificatieveld.
* **Typische Inhoud**: Een e-mailadres; kan `None` zijn als er geen e-mail is opgegeven.

#### `send_to_assigned_user`

* **Betekenis**: Geeft aan of de melding moet worden verzonden naar de gebruiker die aan het document is toegewezen.
* **Rol**: Boolean veld.
* **Typische Inhoud**: `True` of `False`.

#### `delay_delta`

* **Betekenis**: Hoeveelheid tijd om de melding te vertragen.
* **Rol**: Timingveld.
* **Typische Inhoud**: Integer die de vertragingsduur vertegenwoordigt.

#### `delay_delta_type`

* **Betekenis**: Tijdseenheid voor `delay_delta`.
* **Rol**: Timingveld.
* **Typische Inhoud**: Meestal 'minutes'.

#### `created_by`

* **Betekenis**: Identificatie van de gebruiker die het meldingsrecord heeft aangemaakt.
* **Rol**: Vreemde sleutel (verondersteld).
* **Typische Inhoud**: Integer die een gebruikers-ID vertegenwoordigt.

#### `created_on`

* **Betekenis**: Tijdstempel van wanneer het meldingsrecord is aangemaakt.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd met tijdzone-informatie.

#### `last_modified_on`

* **Betekenis**: Tijdstempel van de laatste wijziging aan het meldingsrecord.
* **Rol**: Technisch veld.
* **Typische Inhoud**: Datum en tijd met tijdzone-informatie; kan `None` zijn indien niet gewijzigd.

#### `is_deleted`

* **Betekenis**: Geeft aan of het meldingsrecord als verwijderd is gemarkeerd.
* **Rol**: Boolean veld.
* **Typische Inhoud**: `True` of `False`.

#### `name`

* **Betekenis**: Naam of label voor de melding.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Een reeks die de naam van de melding vertegenwoordigt.

#### `is_recursive`

* **Betekenis**: Geeft aan of de melding met vaste intervallen moet worden herhaald.
* **Rol**: Boolean veld.
* **Typische Inhoud**: `True` of `False`.

#### `is_active`

* **Betekenis**: Geeft aan of de melding momenteel actief is.
* **Rol**: Boolean veld.
* **Typische Inhoud**: `True` of `False`.

#### `priority`

* **Betekenis**: Prioriteitsniveau van de melding.
* **Rol**: Beschrijvend veld.
* **Typische Inhoud**: Zouden reeksen kunnen zijn zoals 'High', 'Medium', 'Low'; voorbeeldgegevens tonen `None`.

#### `email_template_id`

* **Betekenis**: Identificatie voor de e-mailtemplate die voor de melding wordt gebruikt.
* **Rol**: Vreemde sleutel (verondersteld).
* **Typische Inhoud**: Meestal een UUID; voorbeeldgegevens tonen `None`, wat aangeeft dat dit veld optioneel kan zijn.

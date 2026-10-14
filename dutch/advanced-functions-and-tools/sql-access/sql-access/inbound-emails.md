# Inbound Emails

## Tabel `public.inbound_emails`

### Kolommen

* `id`: intern
* `org_id`: ID naar organisatie
* `is_active`: boolean
* `email_senders`: intern
* `email_receiver`: intern
* `token`: intern
* `created_by`: integer
* `created_on`: tijdstempel met tijdzone
* `last_modified_by`: intern
* `last_modified_on`: tijdstempel met tijdzone
* `is_deleted`: boolean
* `deleted_by`: intern
* `deleted_on`: tijdstempel met tijdzone

### Analyse & Beschrijving

## Technische Documentatie: Tabel `public.inbound_emails`

### Inleiding

De tabel `public.inbound_emails` is ontworpen om informatie op te slaan en te beheren over e-mails die door een organisatie worden ontvangen. Deze tabel houdt details van afzenders en ontvangers bij, de status van de e-mail en diverse metadata met betrekking tot het aanmaken, wijzigen en verwijderen van records. Het lijkt deel uit te maken van een e-mailbeheersysteem binnen een organisatie, mogelijk gebruikt voor het volgen van inkomende e-mailcommunicatie.

### Kolombeschrijvingen

#### id

* **Betekenis**: Unieke identificatie voor elk record in de tabel.
* **Rol**: Primaire sleutel.
* **Typische Inhoud**: Een unieke reeks, waarschijnlijk een UUID, zoals `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Betekenis**: Identificatie voor de organisatie die aan de inkomende e-mail is gekoppeld.
* **Rol**: Vreemde sleutel, linkend naar een andere tabel met organisatiedetails.
* **Typische Inhoud**: Een unieke reeks, waarschijnlijk een UUID, zoals `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Betekenis**: Geeft aan of het e-mailrecord momenteel actief is.
* **Rol**: Statusindicator.
* **Typische Inhoud**: Een boolean waarde, ofwel `True` of `False`.

#### email\_senders

* **Betekenis**: Slaat informatie op over de afzender(s) van de e-mail.
* **Rol**: Gegevensveld.
* **Typische Inhoud**: Een JSON-achtige reeks met details van afzenders, bijv. `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Betekenis**: E-mailadres van de primaire ontvanger.
* **Rol**: Gegevensveld.
* **Typische Inhoud**: Een reeks met een e-mailadres. In het voorbeeld is deze leeg, wat wijst op optioneel of wisselend gebruik.

#### token

* **Betekenis**: Een token gekoppeld aan de e-mail, mogelijk voor authenticatie of identificatie.
* **Rol**: Authenticatie- of trackingveld.
* **Typische Inhoud**: Een lange, willekeurig gegenereerde reeks.

#### created\_by

* **Betekenis**: Identificatie voor de gebruiker die het record heeft aangemaakt.
* **Rol**: Vreemde sleutel, linkend naar een gebruikers- of medewerkerstabel.
* **Typische Inhoud**: Een integer die een gebruikers-ID vertegenwoordigt, zoals `1`.

#### created\_on

* **Betekenis**: Tijdstempel van wanneer het record is aangemaakt.
* **Rol**: Metagegevensveld.
* **Typische Inhoud**: Een datetime-waarde met tijdzone-informatie, bijv. `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Betekenis**: Identificatie voor de gebruiker die het record voor het laatst heeft gewijzigd.
* **Rol**: Vreemde sleutel, linkend naar een gebruikers- of medewerkerstabel.
* **Typische Inhoud**: Kan een gebruikers-ID zijn of null indien er geen wijzigingen zijn aangebracht.

#### last\_modified\_on

* **Betekenis**: Tijdstempel van wanneer het record voor het laatst is gewijzigd.
* **Rol**: Metagegevensveld.
* **Typische Inhoud**: Een datetime-waarde die de laatste wijzigingstijd aangeeft, bijv. `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Betekenis**: Geeft aan of het e-mailrecord als verwijderd is gemarkeerd.
* **Rol**: Statusindicator.
* **Typische Inhoud**: Een boolean waarde, ofwel `True` of `False`.

#### deleted\_by

* **Betekenis**: Identificatie voor de gebruiker die het record als verwijderd heeft gemarkeerd.
* **Rol**: Vreemde sleutel, linkend naar een gebruikers- of medewerkerstabel.
* **Typische Inhoud**: Kan een gebruikers-ID zijn of null indien het record niet is verwijderd.

#### deleted\_on

* **Betekenis**: Tijdstempel van wanneer het record als verwijderd is gemarkeerd.
* **Rol**: Metagegevensveld.
* **Typische Inhoud**: Een datetime-waarde die de verwijderingstijd aangeeft, of een standaarddatum indien niet van toepassing, bijv. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.

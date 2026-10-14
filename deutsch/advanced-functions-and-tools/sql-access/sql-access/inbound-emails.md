# Inbound Emails

## Tabelle `public.inbound_emails`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `is_active`: boolean
* `email_senders`: internal
* `email_receiver`: internal
* `token`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: internal
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: internal
* `deleted_on`: timestamp with time zone

### Analyse & Beschreibung

## Technische Dokumentation: Tabelle `public.inbound_emails`

### Einführung

Die Tabelle `public.inbound_emails` speichert und verwaltet Informationen zu E-Mails, die eine Organisation empfängt. Sie erfasst Absender- und Empfängerdetails, den Status der E-Mail sowie verschiedene Metadaten zur Erstellung, Änderung und Löschung von Datensätzen. Sie scheint Teil eines E-Mail-Verwaltungssystems innerhalb einer Organisation zu sein und wird möglicherweise zur Nachverfolgung eingehender E-Mail-Kommunikation verwendet.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine eindeutige Zeichenfolge, vermutlich eine UUID, etwa `'42bf9383-73bf-4b46-9862-3c3a1d97ac80'`.

#### org\_id

* **Bedeutung**: Kennung der Organisation, der die eingehende E-Mail zugeordnet ist.
* **Rolle**: Fremdschlüssel, der auf eine andere Tabelle mit Organisationsdetails verweist.
* **Typischer Inhalt**: Eine eindeutige Zeichenfolge, vermutlich eine UUID, etwa `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### is\_active

* **Bedeutung**: Gibt an, ob der E-Mail-Datensatz derzeit aktiv ist.
* **Rolle**: Statusindikator.
* **Typischer Inhalt**: Ein boolescher Wert, entweder `True` oder `False`.

#### email\_senders

* **Bedeutung**: Speichert Informationen zu den Absendern der E-Mail.
* **Rolle**: Datenfeld.
* **Typischer Inhalt**: Eine JSON-ähnliche Zeichenfolge mit Details zu den Absendern, z. B. `"[{'email': '', 'sub_org': ''}]"`.

#### email\_receiver

* **Bedeutung**: E-Mail-Adresse des primären Empfängers.
* **Rolle**: Datenfeld.
* **Typischer Inhalt**: Eine Zeichenfolge mit einer E-Mail-Adresse. Im Beispiel ist sie leer, was auf eine optionale oder variierende Verwendung hindeutet.

#### token

* **Bedeutung**: Ein der E-Mail zugeordnetes Token, möglicherweise zur Authentifizierung oder Identifizierung.
* **Rolle**: Feld zur Authentifizierung oder Nachverfolgung.
* **Typischer Inhalt**: Eine lange, zufällig generierte Zeichenfolge.

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel, der auf eine Benutzer- oder Mitarbeitertabelle verweist.
* **Typischer Inhalt**: Eine Ganzzahl, die eine Benutzer-ID darstellt, etwa `1`.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Metadatenfeld.
* **Typischer Inhalt**: Ein Datum-Uhrzeit-Wert mit Zeitzoneninformation, z. B. `datetime.datetime(2024, 11, 25, 7, 43, 54, 266771, tzinfo=datetime.timezone.utc)`.

#### last\_modified\_by

* **Bedeutung**: Kennung des Benutzers, der den Datensatz zuletzt geändert hat.
* **Rolle**: Fremdschlüssel, der auf eine Benutzer- oder Mitarbeitertabelle verweist.
* **Typischer Inhalt**: Kann eine Benutzer-ID oder null sein, wenn keine Änderungen vorgenommen wurden.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung des Datensatzes.
* **Rolle**: Metadatenfeld.
* **Typischer Inhalt**: Ein Datum-Uhrzeit-Wert, der den Zeitpunkt der letzten Änderung angibt, z. B. `datetime.datetime(2024, 11, 25, 7, 44, 48, 505384, tzinfo=datetime.timezone.utc)`.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der E-Mail-Datensatz als gelöscht markiert wurde.
* **Rolle**: Statusindikator.
* **Typischer Inhalt**: Ein boolescher Wert, entweder `True` oder `False`.

#### deleted\_by

* **Bedeutung**: Kennung des Benutzers, der den Datensatz als gelöscht markiert hat.
* **Rolle**: Fremdschlüssel, der auf eine Benutzer- oder Mitarbeitertabelle verweist.
* **Typischer Inhalt**: Kann eine Benutzer-ID oder null sein, wenn der Datensatz nicht gelöscht ist.

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann der Datensatz als gelöscht markiert wurde.
* **Rolle**: Metadatenfeld.
* **Typischer Inhalt**: Ein Datum-Uhrzeit-Wert, der den Löschzeitpunkt angibt, oder ein Standarddatum, falls nicht zutreffend, z. B. `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`.

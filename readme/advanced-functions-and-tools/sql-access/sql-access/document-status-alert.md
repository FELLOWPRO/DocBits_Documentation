# Dokumentstatusbenachrichtigung

## Tabelle `public.document_status_alert`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_type_id`: intern
* `doc_type_key`: intern
* `doc_status`: intern
* `email_address`: text
* `send_to_assigned_user`: boolean
* `delay_delta`: integer
* `delay_delta_type`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `name`: intern
* `is_recursive`: boolean
* `is_active`: boolean
* `priority`: intern
* `email_template_id`: intern

### Analyse & Beschreibung

## Tabellendokumentation: `public.document_status_alert`

### Einführung

Die Tabelle `public.document_status_alert` dient offenbar der Verwaltung von Benachrichtigungen zu Dokumentstatus innerhalb einer Organisation. Anhand der Spaltennamen speichert die Tabelle Informationen zu verschiedenen Dokumenttypen und deren Status, einschließlich Details zu Benachrichtigungen und deren zeitlichem Ablauf. Die Tabelle wird vermutlich verwendet, um Benachrichtigungen auf Basis bestimmter Dokumentstatus und Bedingungen auszulösen, etwa um Benutzer zu informieren oder Prozesse zu eskalieren.

### Spaltenbeschreibungen

#### `id`

* **Bedeutung**: Eindeutiger Bezeichner für jeden Benachrichtigungsdatensatz.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jede Zeile der Tabelle eindeutig identifiziert.

#### `org_id`

* **Bedeutung**: Bezeichner der Organisation, die der Benachrichtigung zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf einen Organisationsdatensatz verweist.

#### `doc_type_id`

* **Bedeutung**: Bezeichner des Dokumenttyps.
* **Rolle**: Fremdschlüssel (angenommen).
* **Typischer Inhalt**: In der Regel eine UUID; die Beispieldaten zeigen jedoch `None`, was darauf hindeutet, dass dieses Feld optional sein könnte.

#### `doc_type_key`

* **Bedeutung**: Schlüssel, der den Dokumenttyp darstellt.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge wie 'INVOICE' oder 'XML\_INVOICE'.

#### `doc_status`

* **Bedeutung**: Aktueller Status des Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Beschreibende Statuszeichenfolgen wie 'validated\_pending\_approval' oder 'error'.

#### `email_address`

* **Bedeutung**: E-Mail-Adresse, an die Benachrichtigungen gesendet werden.
* **Rolle**: Benachrichtigungsfeld.
* **Typischer Inhalt**: Eine E-Mail-Adresse; kann `None` sein, wenn keine E-Mail-Adresse angegeben ist.

#### `send_to_assigned_user`

* **Bedeutung**: Gibt an, ob die Benachrichtigung an den dem Dokument zugewiesenen Benutzer gesendet werden soll.
* **Rolle**: Boolesches Feld.
* **Typischer Inhalt**: `True` oder `False`.

#### `delay_delta`

* **Bedeutung**: Zeitspanne, um die die Benachrichtigung verzögert wird.
* **Rolle**: Zeitsteuerungsfeld.
* **Typischer Inhalt**: Ganzzahl, die die Dauer der Verzögerung darstellt.

#### `delay_delta_type`

* **Bedeutung**: Zeiteinheit für `delay_delta`.
* **Rolle**: Zeitsteuerungsfeld.
* **Typischer Inhalt**: In der Regel 'minutes'.

#### `created_by`

* **Bedeutung**: Bezeichner des Benutzers, der den Benachrichtigungsdatensatz erstellt hat.
* **Rolle**: Fremdschlüssel (angenommen).
* **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.

#### `created_on`

* **Bedeutung**: Zeitstempel, zu dem der Benachrichtigungsdatensatz erstellt wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.

#### `last_modified_on`

* **Bedeutung**: Zeitstempel der letzten Änderung am Benachrichtigungsdatensatz.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation; kann `None` sein, wenn nicht geändert.

#### `is_deleted`

* **Bedeutung**: Gibt an, ob der Benachrichtigungsdatensatz als gelöscht markiert ist.
* **Rolle**: Boolesches Feld.
* **Typischer Inhalt**: `True` oder `False`.

#### `name`

* **Bedeutung**: Name oder Bezeichnung der Benachrichtigung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Namen der Benachrichtigung darstellt.

#### `is_recursive`

* **Bedeutung**: Gibt an, ob die Benachrichtigung in festgelegten Intervallen wiederholt werden soll.
* **Rolle**: Boolesches Feld.
* **Typischer Inhalt**: `True` oder `False`.

#### `is_active`

* **Bedeutung**: Gibt an, ob die Benachrichtigung derzeit aktiv ist.
* **Rolle**: Boolesches Feld.
* **Typischer Inhalt**: `True` oder `False`.

#### `priority`

* **Bedeutung**: Prioritätsstufe der Benachrichtigung.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Kann Zeichenfolgen wie 'High', 'Medium', 'Low' enthalten; die Beispieldaten zeigen `None`.

#### `email_template_id`

* **Bedeutung**: Bezeichner der E-Mail-Vorlage, die für die Benachrichtigung verwendet wird.
* **Rolle**: Fremdschlüssel (angenommen).
* **Typischer Inhalt**: In der Regel eine UUID; die Beispieldaten zeigen `None`, was darauf hindeutet, dass dieses Feld optional sein könnte.

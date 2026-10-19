# Document status trigger

## Tabelle `public.document_status_trigger`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `trigger_doc_type`: internal
* `trigger_doc_status`: internal
* `trigger_url`: internal
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.document_status_trigger`

### Einführung

Die Tabelle `public.document_status_trigger` dient der Verwaltung und Nachverfolgung des Status von Dokumenten innerhalb einer Organisation. Die Tabelle verwaltet offenbar Trigger im Zusammenhang mit der Dokumentverarbeitung, vermutlich in einem Workflow-System. Sie erfasst Informationen zu Dokumenttypen und deren Statuswechseln und kann über angegebene URLs Aktionen oder Workflows auslösen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Diese Spalte speichert einen eindeutigen Bezeichner für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, z. B. `8103b700-c03c-40cb-9322-e9e1ddbe0cb1`.

#### org\_id

* **Bedeutung**: Stellt den eindeutigen Bezeichner einer Organisation dar.
* **Rolle**: Fremdschlüssel, verknüpft mit einer Organisationsentität.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, z. B. `23f3d697-7411-4c95-981d-faf089d266be`.

#### trigger\_doc\_type

* **Bedeutung**: Gibt den Dokumenttyp an, der dem Trigger zugeordnet ist.
* **Rolle**: Beschreibendes Feld, das den Dokumenttyp angibt.
* **Typischer Inhalt**: Namen von Dokumenttypen, etwa `INVOICE`.

#### trigger\_doc\_status

* **Bedeutung**: Bezeichnet den konkreten Dokumentstatus, der den Trigger aktiviert.
* **Rolle**: Beschreibendes Feld, das den Dokumentstatus näher beschreibt.
* **Typischer Inhalt**: Statusbeschreibungen wie `approved_pending_second_approval`.

#### trigger\_url

* **Bedeutung**: URL, die aufgerufen wird, wenn der Dokumentstatus bestimmte Bedingungen erfüllt.
* **Rolle**: Technisches Feld für die Workflow-Automatisierung.
* **Typischer Inhalt**: URLs, z. B. `https://test-wf-stage.workflow.polydocs.io/webhook/3c3ab41b-a1d9-40a9-8e33-2968d33c989e/webhook`.

#### is\_active

* **Bedeutung**: Gibt an, ob der Trigger derzeit aktiv ist.
* **Rolle**: Technisches Feld zur Verwaltung von Trigger-Zuständen.
* **Typischer Inhalt**: Boolesche Werte, `True` oder `False`.

#### created\_by

* **Bedeutung**: Identifiziert den Benutzer, der den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel auf eine Benutzerentität.
* **Typischer Inhalt**: Ganzzahlige Benutzer-IDs, z. B. `1`.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Technisches Feld für Audit und Änderungsverfolgung.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone, z. B. `2022-09-16 07:26:55 UTC`.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung am Datensatz.
* **Rolle**: Technisches Feld für Audit und Änderungsverfolgung.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone; kann `None` sein, wenn nicht geändert.

#### is\_deleted

* **Bedeutung**: Kennzeichnet, ob der Datensatz als gelöscht oder inaktiv gilt.
* **Rolle**: Technisches Feld für das weiche Löschen.
* **Typischer Inhalt**: Boolesche Werte, `True` oder `False`.

Diese Tabelle bietet einen strukturierten Ansatz zur Verwaltung von Dokumentstatus und zugehörigen Triggern im Workflow-System einer Organisation und stellt sicher, dass Aktionen automatisch ausgeführt werden können, sobald Dokumente verschiedene Zustände durchlaufen.

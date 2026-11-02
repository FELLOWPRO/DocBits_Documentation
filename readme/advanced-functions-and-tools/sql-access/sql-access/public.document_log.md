# public.document\_log

## Tabelle `public.document_log`

### Spalten

* `id`: integer
* `org_id`: ID der Organisation
* `doc_id`: intern
* `action_type`: intern
* `action_description`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_hidden`: boolean
* `previous_status`: intern
* `current_status`: intern

### Analyse & Beschreibung

## Technische Dokumentation: Tabelle `public.document_log`

### Einführung

Die Tabelle `public.document_log` verfolgt den Verlauf und die Statusänderungen von Dokumenten innerhalb einer Organisation. Sie erfasst auf Dokumenten ausgeführte Aktionen, etwa Statusaktualisierungen, zusammen mit Details zum ausführenden Benutzer und Zeitstempeln, die angeben, wann diese Aktionen stattfanden. Diese Tabelle ist entscheidend für die Prüfung von Dokumentverarbeitungs-Workflows und für das Verständnis des Lebenszyklus jedes Dokuments.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Protokolleintrag.
* **Rolle**: Primärschlüssel. Diese Spalte dient als eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Typischer Inhalt**: Ganzzahlwerte, die mit jedem neuen Eintrag hochgezählt werden.

#### org\_id

* **Bedeutung**: Kennung der Organisation, die dem Dokument zugeordnet ist.
* **Rolle**: Fremdschlüssel. Verweist auf eine Organisationsentität, die in diesem Kontext jedoch nicht explizit definiert ist.
* **Typischer Inhalt**: Zeichenfolgen, vermutlich UUIDs, die Organisationskennungen darstellen.

#### doc\_id

* **Bedeutung**: Kennung des Dokuments, das dem Protokolleintrag zugeordnet ist.
* **Rolle**: Fremdschlüssel. Diese Spalte verweist auf ein bestimmtes Dokument im System.
* **Typischer Inhalt**: Zeichenfolgen, vermutlich UUIDs, die Dokumentkennungen darstellen.

#### action\_type

* **Bedeutung**: Typ der protokollierten Aktion.
* **Rolle**: Beschreibendes Feld. Gibt die Kategorie der ausgeführten Aktion an.
* **Typischer Inhalt**: Zeichenfolgen wie `STATUS_CHANGE`, die die Art der Aktion angeben.

#### action\_description

* **Bedeutung**: Detaillierte Beschreibung der ausgeführten Aktion.
* **Rolle**: Beschreibendes Feld. Liefert Kontext oder Details zur Aktion.
* **Typischer Inhalt**: Textbeschreibungen, z. B. "Data extraction started", "Error occurred processing document".

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der den Protokolleintrag erstellt hat.
* **Rolle**: Fremdschlüssel. Verweist auf eine Benutzerentität und zeigt, wer die Aktion ausgeführt hat.
* **Typischer Inhalt**: Ganzzahlwerte, die Benutzerkennungen darstellen.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Protokolleintrags.
* **Rolle**: Technisches Feld. Hält den genauen Zeitpunkt fest, zu dem eine Aktion protokolliert wurde.
* **Typischer Inhalt**: Zeitstempel mit Zeitzoneninformation, z. B. `2025-04-01 13:07:51.291193 UTC`.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung des Protokolleintrags.
* **Rolle**: Technisches Feld. Gibt den Zeitpunkt der letzten Aktualisierung des Protokolleintrags an.
* **Typischer Inhalt**: Zeitstempel, möglicherweise null, wenn nach der Erstellung nicht geändert.

#### is\_deleted

* **Bedeutung**: Kennzeichen, das angibt, ob der Protokolleintrag als gelöscht markiert ist.
* **Rolle**: Technisches Feld. Dient dem logischen Löschen von Einträgen.
* **Typischer Inhalt**: Boolesche Werte, `False` für aktive Einträge und `True` für gelöschte.

#### is\_hidden

* **Bedeutung**: Kennzeichen, das angibt, ob der Protokolleintrag in der normalen Ansicht ausgeblendet ist.
* **Rolle**: Technisches Feld. Dient der Steuerung der Sichtbarkeit von Protokolleinträgen.
* **Typischer Inhalt**: Boolesche Werte, `False` für sichtbare Einträge und `True` für ausgeblendete.

#### previous\_status

* **Bedeutung**: Status des Dokuments vor Ausführung der Aktion.
* **Rolle**: Beschreibendes Feld. Gibt den Zustand des Dokuments vor der protokollierten Aktion an.
* **Typischer Inhalt**: Zeichenfolgen wie `new`, `validating`, `running`, die Dokumentzustände darstellen.

#### current\_status

* **Bedeutung**: Status des Dokuments nach Ausführung der Aktion.
* **Rolle**: Beschreibendes Feld. Gibt den aktualisierten Zustand des Dokuments nach der Aktion an.
* **Typischer Inhalt**: Zeichenfolgen wie `running`, `ready_for_validation`, `error`, die Dokumentzustände darstellen.

Diese Dokumentation bietet einen Überblick über die Tabelle `public.document_log` und beschreibt Zweck und Struktur jeder Spalte, was für Entwickler, die Dokument-Workflows verwalten und Audit-Trails pflegen, von zentraler Bedeutung ist.

# Batch instance

## Tabelle `public.batch_instance`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Tabellendokumentation: `public.batch_instance`

### Einführung

Die Tabelle `public.batch_instance` dient der Speicherung von Informationen zu verschiedenen Batch-Instanzen innerhalb einer Organisation. Sie enthält wichtige Metadaten zu jeder Instanz, darunter ihre eindeutige Identifikation, die zugehörige Organisation sowie Angaben zu Erstellung und Änderung. Die Tabelle ist wesentlich, um den Lebenszyklus und die Verwaltung von Batch-Instanzen nachzuverfolgen, vermutlich in einer Softwareanwendung für die Stapelverarbeitung.

### Spalten

#### `id`

* **Bedeutung**: Diese Spalte speichert den eindeutigen Bezeichner jeder Batch-Instanz.
* **Rolle**: Primärschlüssel (`id`).
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jede Batch-Instanz eindeutig identifiziert, z. B. `'e9aa9ad7-6c36-4d7c-b31c-6e10bb8fbd87'`.

#### `org_id`

* **Bedeutung**: Diese Spalte speichert den Bezeichner der Organisation, die der Batch-Instanz zugeordnet ist.
* **Rolle**: Fremdschlüssel (`org_id`).
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Organisation darstellt, z. B. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### `created_by`

* **Bedeutung**: Diese Spalte gibt den Benutzer oder die Systementität an, der bzw. die die Batch-Instanz erstellt hat.
* **Rolle**: Möglicherweise ein Fremdschlüssel, der auf eine Benutzertabelle oder Ähnliches verweist.
* **Typischer Inhalt**: Eine Ganzzahl, die die ID des Erstellers darstellt, z. B. `1`.

#### `created_on`

* **Bedeutung**: Diese Spalte erfasst den Zeitstempel der Erstellung der Batch-Instanz.
* **Rolle**: Technisches Feld für Audit- und Nachverfolgungszwecke.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, z. B. `2021-09-22 10:55:59.755627+00`.

#### `last_modified_on`

* **Bedeutung**: Diese Spalte erfasst den Zeitstempel der letzten Änderung an der Batch-Instanz.
* **Rolle**: Technisches Feld zur Nachverfolgung von Änderungen.
* **Typischer Inhalt**: In der Regel null oder ein Zeitstempel mit Zeitzone, wenn Änderungen stattgefunden haben.

#### `is_deleted`

* **Bedeutung**: Diese Spalte gibt an, ob die Batch-Instanz als gelöscht markiert ist.
* **Rolle**: Technisches Feld für das weiche Löschen (Soft Delete).
* **Typischer Inhalt**: Ein boolescher Wert, in der Regel `False`, wenn die Instanz aktiv ist, z. B. `False`.

Diese Dokumentation bietet einen umfassenden Überblick über die Tabelle `public.batch_instance` und beschreibt Zweck und Struktur jeder Spalte, was für Entwickler, die mit diesem Datenmodell arbeiten, wichtig ist.

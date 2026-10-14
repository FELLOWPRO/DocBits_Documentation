# Custom\_classification\_document\_label

## Tabelle `public.custom_classification_document_label`

### Spalten

* `id`: integer
* `org_id`: ID to organisation
* `doc_id`: internal
* `label_id`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.custom_classification_document_label`

### Einführung

Die Tabelle `public.custom_classification_document_label` dient der Verwaltung und Speicherung von Zuordnungen zwischen Dokumenten und ihren jeweiligen Labels innerhalb einer Organisation. Sie erleichtert die Kategorisierung und das Auffinden von Dokumenten anhand benutzerdefinierter Labels und bietet eine strukturierte Möglichkeit, die Dokumentklassifizierung für unterschiedliche organisatorische Anforderungen zu verwalten.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Diese Spalte dient als eindeutiger Bezeichner für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel
* **Typischer Inhalt**: Eine Ganzzahl, die jede Zeile eindeutig identifiziert.
* **Hinweis**: Jeder Eintrag in der Tabelle hat eine eigene `id`, um die Datenintegrität sicherzustellen und effiziente Verweise zu ermöglichen.

#### org\_id

* **Bedeutung**: Stellt die Organisation dar, zu der die Dokument-Label-Zuordnung gehört.
* **Rolle**: Fremdschlüssel
* **Typischer Inhalt**: Eine Zeichenfolge, vermutlich eine UUID, die eine Organisation eindeutig identifiziert.
* **Hinweis**: Stellt sicher, dass die Zuordnung von Dokumenten und Labels auf den richtigen organisatorischen Kontext begrenzt ist.

#### doc\_id

* **Bedeutung**: Identifiziert das Dokument, das mit einem Label versehen wird.
* **Rolle**: Fremdschlüssel
* **Typischer Inhalt**: Eine Zeichenfolge, vermutlich eine UUID, die ein Dokument eindeutig identifiziert.
* **Hinweis**: Ermöglicht die Verknüpfung bestimmter Dokumente mit Labels und damit die Kategorisierung von Dokumenten.

#### label\_id

* **Bedeutung**: Verweist auf das Label, das auf das Dokument angewendet wird.
* **Rolle**: Fremdschlüssel
* **Typischer Inhalt**: Eine Ganzzahl, die auf ein Label in einer separaten Label-Tabelle verweist.
* **Hinweis**: Erleichtert die Zuordnung zwischen Dokumenten und ihren jeweiligen Labels.

#### created\_by

* **Bedeutung**: Identifiziert den Benutzer, der den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel (möglicherweise auf eine Benutzertabelle)
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.
* **Hinweis**: Verfolgt den Ursprung jeder Dokument-Label-Zuordnung für Audit und Nachvollziehbarkeit.

#### created\_on

* **Bedeutung**: Gibt an, wann der Datensatz erstellt wurde.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.
* **Hinweis**: Liefert den zeitlichen Kontext, wann die Dokument-Label-Beziehung hergestellt wurde.

#### last\_modified\_on

* **Bedeutung**: Erfasst den Zeitstempel der letzten Änderung des Datensatzes.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation, kann `None` sein, wenn nie geändert.
* **Hinweis**: Nützlich, um den Änderungsverlauf der Dokument-Label-Zuordnungen nachzuverfolgen.

#### is\_deleted

* **Bedeutung**: Kennzeichnet, ob der Datensatz als gelöscht markiert wurde.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`).
* **Hinweis**: Unterstützt das weiche Löschen (Soft Delete), also das logische Entfernen von Daten ohne physisches Löschen aus der Datenbank.

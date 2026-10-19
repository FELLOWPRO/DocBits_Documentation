# Electronic document extraction attributes

## Tabelle `public.electronic_document_extraction_attributes`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `doc_type_key`: internal
* `sub_doc_type_key`: internal
* `electronic_document_type`: internal
* `attribute_name`: internal
* `attribute_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.electronic_document_extraction_attributes`

### Einführung

Die Tabelle `public.electronic_document_extraction_attributes` verwaltet offenbar Attribute rund um die Extraktion elektronischer Dokumente. Sie speichert verschiedene Merkmale und Metadaten zu elektronischen Dokumenttypen, deren Verarbeitungsmethoden und den zugehörigen Organisationen. Die Tabelle scheint Funktionen wie die Identifizierung von Dokumenttypen, Transformationen, Vorschauen und Strukturbeschreibungen zu unterstützen, die für den effektiven Umgang mit elektronischen Dokumenten wichtig sind.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Eintrag eines Extraktionsattributs eindeutig identifiziert.
* **Hinweis**: Dient als eindeutige Referenz für jede Zeile.

#### org\_id

* **Bedeutung**: Kennung der Organisation, zu der die Dokumentattribute gehören.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf die zugehörige Organisation verweist.
* **Hinweis**: Verknüpft die Extraktionsattribute mit einer bestimmten Organisation.

#### doc\_type\_key

* **Bedeutung**: Ein Schlüssel, der den Dokumenttyp darstellt.
* **Rolle**: Kennung zur Kategorisierung von Dokumenten.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Dokumenttyp angibt, etwa 'INVOICE' oder 'ORDER\_CONFIRMATION'.
* **Hinweis**: Dient zur Bestimmung der Kategorie des Dokuments.

#### sub\_doc\_type\_key

* **Bedeutung**: Stellt eine Unterkategorie des Haupt-Dokumenttyps dar.
* **Rolle**: Kennung für eine weitere Klassifizierung.
* **Typischer Inhalt**: Null oder eine bestimmte Untertyp-Zeichenfolge.
* **Hinweis**: Nützlich für eine feinere Granularität bei der Dokumentklassifizierung.

#### electronic\_document\_type

* **Bedeutung**: Das Format oder der Standard des elektronischen Dokuments.
* **Rolle**: Beschreibendes Feld für das Dokumentformat.
* **Typischer Inhalt**: Zeichenfolgen wie 'EDI' oder 'FACTURX'.
* **Hinweis**: Gibt den Standard oder das Format des Dokuments an.

#### attribute\_name

* **Bedeutung**: Der Name des Attributs im Zusammenhang mit dem Dokumentextraktionsprozess.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Zeichenfolgen wie 'PREVIEW' oder 'TRANSFORMATION'.
* **Hinweis**: Beschreibt das konkrete Attribut, das für die Dokumentverarbeitung relevant ist.

#### attribute\_type

* **Bedeutung**: Der Typ des Attributs im Zusammenhang mit der Dokumentextraktion.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Zeichenfolgen wie 'XSLT' oder 'JSON'.
* **Hinweis**: Gibt das Datenformat oder die Methode an, die für das Attribut verwendet wird.

#### created\_by

* **Bedeutung**: ID des Benutzers, der den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.
* **Hinweis**: Verfolgt, wer den Datensatz ursprünglich erstellt hat.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit in UTC.
* **Hinweis**: Gibt den Erstellungszeitpunkt des Datensatzes an.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung des Datensatzes.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit in UTC, oder null, wenn nicht geändert.
* **Hinweis**: Verfolgt die letzte Aktualisierung des Datensatzes.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Datensatz als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert, `True` oder `False`.
* **Hinweis**: Unterstützt das logische Löschen (Soft Delete).

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann der Datensatz als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit in UTC, oder ein sehr altes Standarddatum, wenn nicht gelöscht.
* **Hinweis**: Dient zur Nachverfolgung, wann der Datensatz gelöscht wurde.

#### last\_modified\_by

* **Bedeutung**: ID des Benutzers, der den Datensatz zuletzt geändert hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolge, oder null, wenn nicht geändert.
* **Hinweis**: Identifiziert den Benutzer, der für die letzte Änderung verantwortlich ist.

#### deleted\_by

* **Bedeutung**: ID des Benutzers, der den Datensatz als gelöscht markiert hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolge, oder null, wenn nicht gelöscht.
* **Hinweis**: Verfolgt, wer die Löschung durchgeführt hat.

Diese Dokumentation bietet einen detaillierten Überblick über die Tabellenstruktur und ihre Spalten und erleichtert Entwicklern und Datenbankadministratoren das Verständnis und die Nutzung.

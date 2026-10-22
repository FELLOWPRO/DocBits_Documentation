# Organisationsdokumenttyp

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `document_type_id`: intern
* `document_type_key`: intern
* `document_locale`: intern
* `classification_method`: intern
* `is_active`: boolean
* `extraction_type`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: intern

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.organisation_document_type`

## Einführung

Die Tabelle `public.organisation_document_type` verwaltet und speichert Informationen zu verschiedenen Dokumenttypen, die Organisationen zugeordnet sind. Dazu gehören Details wie der Dokumenttyp-Schlüssel, das Gebietsschema, Klassifizierungsmethoden und der Status des Dokumenttyps (aktiv, gelöscht usw.). Sie dient offenbar als Zuordnung zwischen Organisationen und den Dokumenttypen, die sie verwenden oder verwalten, sowie als Ablage für Metadaten zu diesen Dokumenten.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die einen Dokumenttyp-Eintrag eindeutig identifiziert.
- **Hinweis**: Unerlässlich, um jeden Datensatz zu unterscheiden.

### org_id
- **Bedeutung**: Kennung der Organisation, die zum Dokumenttyp gehört.
- **Rolle**: Fremdschlüssel, der vermutlich auf eine Organisationstabelle verweist.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge.
- **Hinweis**: Verbindet den Dokumenttyp mit einer bestimmten Organisation.

### document_type_id
- **Bedeutung**: Kennung des Dokumenttyps.
- **Rolle**: Fremdschlüssel, der möglicherweise mit einer Referenztabelle für Dokumenttypen verknüpft ist.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge.
- **Hinweis**: Ermöglicht die Zuordnung zu bestimmten Dokumenttypen.

### document_type_key
- **Bedeutung**: Ein Schlüssel oder Code, der den Dokumenttyp darstellt.
- **Rolle**: Beschreibendes Feld zur Klassifizierung des Dokumenttyps.
- **Typischer Inhalt**: Eine Zeichenfolge, die als Kennung oder Bezeichnung des Dokumenttyps dient.
- **Hinweis**: Dient dazu, den Dokumenttyp in lesbarer Form zu identifizieren.

### document_locale
- **Bedeutung**: Gebietsschema- oder Spracheinstellung für den Dokumenttyp.
- **Rolle**: Beschreibendes Feld zur Festlegung des Gebietsschemas.
- **Typischer Inhalt**: Eine Zeichenfolge, häufig 'auto', was eine automatische Bestimmung des Gebietsschemas anzeigt.
- **Hinweis**: Nützlich für Internationalisierung und Lokalisierung.

### classification_method
- **Bedeutung**: Methode, mit der der Dokumenttyp klassifiziert wird.
- **Rolle**: Beschreibendes Feld, das angibt, wie das Dokument klassifiziert wird.
- **Typischer Inhalt**: Eine Zeichenfolge, häufig 'auto', was auf eine automatische Klassifizierung hindeutet.
- **Hinweis**: Wichtig, um den Klassifizierungsprozess zu verstehen.

### is_active
- **Bedeutung**: Status, der angibt, ob der Dokumenttyp aktiv ist.
- **Rolle**: Boolesches Statusfeld.
- **Typischer Inhalt**: `True` oder `False`.
- **Hinweis**: Bestimmt, ob der Dokumenttyp derzeit verwendet wird.

### extraction_type
- **Bedeutung**: Art der Extraktionsmethode, die für das Dokument verwendet wird.
- **Rolle**: Beschreibendes Feld für den Extraktionsprozess.
- **Typischer Inhalt**: Zeichenfolgen wie 'FIX_COORDINATES', 'FLEX_COORDINATES' oder `None`.
- **Hinweis**: Gibt Aufschluss darüber, wie Daten aus Dokumenten extrahiert werden.

### created_by
- **Bedeutung**: Kennung des Benutzers, der den Datensatz erstellt hat.
- **Rolle**: Technisches Feld für Audit-Zwecke.
- **Typischer Inhalt**: Eine Ganzzahl, die eine Benutzer-ID darstellt.
- **Hinweis**: Nützlich für die Nachverfolgung von Änderungen und die Nachvollziehbarkeit.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
- **Rolle**: Technisches Feld für Audit-Zwecke.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone.
- **Hinweis**: Wichtig, um Datum und Uhrzeit der Erstellung des Datensatzes nachzuvollziehen.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung des Datensatzes.
- **Rolle**: Technisches Feld für Audit-Zwecke.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone.
- **Hinweis**: Nützlich, um Aktualisierungen und Änderungen am Datensatz nachzuverfolgen.

### is_deleted
- **Bedeutung**: Status, der angibt, ob der Datensatz als gelöscht markiert wurde.
- **Rolle**: Boolesches Statusfeld.
- **Typischer Inhalt**: `True` oder `False`.
- **Hinweis**: Unterstützt die Umsetzung einer Funktion zum logischen Löschen (Soft Delete).

### sub_org_id
- **Bedeutung**: Kennung einer Unterorganisation, die zum Dokumenttyp gehört.
- **Rolle**: Möglicher Fremdschlüssel, der eine hierarchische Organisationsstruktur ergänzt.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge oder `None`.
- **Hinweis**: Liefert zusätzlichen Kontext zur Organisationsstruktur.

```

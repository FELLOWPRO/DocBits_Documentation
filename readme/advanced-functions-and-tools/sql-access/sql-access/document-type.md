# Dokumenttyp

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `document_key`: intern
* `document_name`: intern
* `title`: intern
* `translation_key`: intern
* `extraction_type`: intern
* `document_type_category`: intern
* `has_table`: boolean
* `sort_order`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

## Analyse & Beschreibung

```markdown
# Tabelle: public.document_type

## Einführung
Die Tabelle `public.document_type` speichert Informationen zu den verschiedenen Dokumenttypen innerhalb einer Organisation. Sie enthält Kennungen und Metadaten für die Kategorisierung, Verwaltung und Verarbeitung von Dokumenten, etwa Dokumentschlüssel, Namen, Titel, Übersetzungsschlüssel und weitere Attribute, die die Handhabung und das Auffinden von Dokumenten erleichtern. Außerdem protokolliert die Tabelle die Erstellung und Änderung dieser Einträge und unterstützt sowohl aktive als auch gelöschte Zustände.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jeden Dokumenttyp-Eintrag.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die einen Dokumenttyp-Eintrag eindeutig identifiziert.

### org_id
- **Bedeutung**: Kennung der Organisation, zu der der Dokumenttyp gehört.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Organisation verweist.

### document_key
- **Bedeutung**: Eindeutiger Schlüssel zur Identifizierung des Dokumenttyps, der möglicherweise in Dokumentenspeicher- oder Verarbeitungssystemen verwendet wird.
- **Rolle**: Kennung.
- **Typischer Inhalt**: Eine Zeichenfolge, die Informationen zum Dokumenttyp mit der Organisations-ID kombiniert.

### document_name
- **Bedeutung**: Der interne Name des Dokumenttyps.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge in Großbuchstaben, die den Namen des Dokumenttyps darstellt.

### title
- **Bedeutung**: Der Anzeigetitel des Dokumenttyps für Benutzeroberflächen.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine gut lesbare Zeichenfolge in Titelschreibweise, die den Dokumenttyp beschreibt.

### translation_key
- **Bedeutung**: Ein Schlüssel zur Lokalisierung des Dokumenttitels oder -namens in verschiedene Sprachen.
- **Rolle**: Unterstützung der Internationalisierung.
- **Typischer Inhalt**: Eine Zeichenfolge in Kleinbuchstaben, die als Referenz für Übersetzungssysteme dient.

### extraction_type
- **Bedeutung**: Gibt die Methode oder den Prozess an, mit dem Daten aus dem Dokument extrahiert werden.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: In den Beispieldaten derzeit nicht befüllt.

### document_type_category
- **Bedeutung**: Ordnet den Dokumenttyp übergeordneten Kategorien oder Klassifizierungen zu.
- **Rolle**: Kategorisierungsfeld.
- **Typischer Inhalt**: In den Beispieldaten derzeit nicht befüllt.

### has_table
- **Bedeutung**: Gibt an, ob der Dokumenttyp tabellarische Daten enthält.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`), der das Vorhandensein tabellarischer Daten anzeigt.

### sort_order
- **Bedeutung**: Legt die Reihenfolge fest, in der Dokumenttypen sortiert oder angezeigt werden.
- **Rolle**: Sortierfeld.
- **Typischer Inhalt**: Eine Ganzzahl, die die Position in der Sortierung angibt.

### created_by
- **Bedeutung**: Kennung des Benutzers, der den Dokumenttyp-Eintrag erstellt hat.
- **Rolle**: Metadatenfeld.
- **Typischer Inhalt**: Eine Ganzzahl, die auf eine Benutzer-ID verweist.

### created_on
- **Bedeutung**: Zeitstempel, der angibt, wann der Dokumenttyp-Eintrag erstellt wurde.
- **Rolle**: Audit-Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung des Dokumenttyp-Eintrags.
- **Rolle**: Audit-Feld.
- **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation, `None`, wenn nie geändert.

### is_deleted
- **Bedeutung**: Gibt an, ob der Dokumenttyp-Eintrag als gelöscht markiert ist.
- **Rolle**: Statusfeld.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`), der den Löschstatus anzeigt.
```

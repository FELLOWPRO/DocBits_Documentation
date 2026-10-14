# API credentials

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `sub_org_id`: internal
* `title`: internal
* `credentials_type`: internal
* `credentials_json`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `last_modified_by`: internal
* `deleted_by`: internal

## Analyse & Beschreibung

```markdown
# Tabellendokumentation: `public.api_credentials`

## Einführung

Die Tabelle `public.api_credentials` dient der Speicherung und Verwaltung von API-Zugangsdaten. Sie ist für Organisationen wichtig, um ihre API-Authentifizierungsdaten sicher zu verwalten, damit verschiedene Dienste mit den richtigen Zugangsdaten miteinander kommunizieren können. Sie enthält Angaben zur Art der Zugangsdaten, zur Organisation, zu der sie gehören, sowie Metadaten zu ihrer Erstellung und Änderung.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Ein eindeutiger Bezeichner für jeden Eintrag in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Ein universell eindeutiger Bezeichner (UUID), der einen bestimmten Satz von API-Zugangsdaten darstellt.

### org_id
- **Bedeutung**: Bezeichner der Organisation, der die Zugangsdaten gehören.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID, die auf den Datensatz der Organisation in einer anderen Tabelle verweist.

### sub_org_id
- **Bedeutung**: Bezeichner einer Unterorganisation innerhalb der Hauptorganisation.
- **Rolle**: Fremdschlüssel (optional).
- **Typischer Inhalt**: Kann eine UUID enthalten, die auf eine Unterorganisation verweist, oder `None`.

### title
- **Bedeutung**: Ein beschreibender Titel für die API-Zugangsdaten.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge wie "supplier_auth", die den Zweck oder die Verwendung der Zugangsdaten angibt.

### credentials_type
- **Bedeutung**: Gibt die Art der gespeicherten Zugangsdaten an.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge wie "ionapi", die das Format oder Protokoll der Zugangsdaten angibt.

### credentials_json
- **Bedeutung**: Ein JSON-Objekt mit detaillierten Zugangsdaten.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: JSON-Zeichenfolge mit verschiedenen Schlüssel-Wert-Paaren, die Authentifizierungsparameter beschreiben.

### created_by
- **Bedeutung**: Benutzer-ID der Person, die den Zugangsdaten-Datensatz erstellt hat.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Zeitstempel, der angibt, wann die Zugangsdaten erstellt wurden.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Datums-/Zeitwert mit Zeitzone, z. B. `2024-04-08 11:54:55 UTC`.

### last_modified_on
- **Bedeutung**: Zeitstempel, der den Zeitpunkt der letzten Änderung der Zugangsdaten angibt.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Datums-/Zeitwert mit Zeitzone oder `None`, wenn nie geändert.

### is_deleted
- **Bedeutung**: Kennzeichen, das angibt, ob die Zugangsdaten als gelöscht markiert sind.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein boolescher Wert, wobei `False` aktive Zugangsdaten kennzeichnet.

### deleted_on
- **Bedeutung**: Zeitstempel, der angibt, wann die Zugangsdaten als gelöscht markiert wurden.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Datums-/Zeitwert mit Zeitzone oder `None`, wenn nicht gelöscht.

### last_modified_by
- **Bedeutung**: Bezeichner des Benutzers, der die Zugangsdaten zuletzt geändert hat.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die die Benutzer-ID darstellt, oder `None`.

### deleted_by
- **Bedeutung**: Bezeichner des Benutzers, der die Zugangsdaten als gelöscht markiert hat.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die die Benutzer-ID darstellt, oder `None`.
```

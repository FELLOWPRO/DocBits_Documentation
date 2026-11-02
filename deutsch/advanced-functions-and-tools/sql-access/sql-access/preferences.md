# Präferenzen

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `pref_key`: intern
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `deleted_on`: timestamp with time zone
* `is_deleted`: boolean
* `user_id`: integer
* `sub_org_id`: intern

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.preferences`

## Einführung
Die Tabelle `public.preferences` speichert Konfigurationseinstellungen und Präferenzen für verschiedene Organisationseinheiten innerhalb eines Systems. Jeder Eintrag in der Tabelle stellt einen bestimmten Präferenzschlüssel und den zugehörigen Wert dar, der einer Organisation oder Unterorganisation zugeordnet ist. Diese Konfigurationsdaten können Einstellungen zu USt-IdNrn., Extraktionseinstellungen, Modulaktivierung und mehr umfassen.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Diese Spalte speichert die eindeutige Kennung für jeden Präferenzeintrag.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jede Zeile eindeutig identifiziert, etwa `23f3d697-7411-4c95-981d-faf089d266be`.

### org_id
- **Bedeutung**: Diese Spalte speichert die Kennung der Organisation, der die Präferenz zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die einer Organisation entspricht, ähnlich `23f3d697-7411-4c95-981d-faf089d266be`.

### pref_key
- **Bedeutung**: Diese Spalte stellt den Schlüssel oder Namen der Präferenzeinstellung dar.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Zeichenfolgen, die Konfigurationsschlüssel darstellen, etwa `VAT_NUMBERS`, `TABLE_EXTRACTION_SETTING`.

### pref_value
- **Bedeutung**: Diese Spalte enthält den Wert der Präferenz, der zu `pref_key` gehört.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Variiert je nach `pref_key`; Beispiele sind kommagetrennte USt-IdNrn. oder boolesche Werte wie `true` oder `false`.

### created_by
- **Bedeutung**: Diese Spalte gibt die Benutzer-ID der Person an, die den Präferenzeintrag erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die eine Benutzer-ID darstellt, z. B. `1`.

### created_on
- **Bedeutung**: Diese Spalte erfasst den Zeitstempel der Erstellung der Präferenz.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, z. B. `2021-11-09 11:04:18+00`.

### last_modified_on
- **Bedeutung**: Diese Spalte hält den Zeitstempel der letzten Änderung der Präferenz fest.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der den Zeitpunkt der letzten Aktualisierung angibt, etwa `2023-12-04 10:10:26+00`.

### deleted_on
- **Bedeutung**: Diese Spalte vermerkt den Zeitstempel, zu dem die Präferenz als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Üblicherweise `null`, sofern die Zeile nicht zum Löschen markiert ist.

### is_deleted
- **Bedeutung**: Diese Spalte gibt an, ob die Präferenz als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein boolescher Wert, üblicherweise `false`.

### user_id
- **Bedeutung**: Diese Spalte speichert die der Präferenz zugeordnete Benutzer-ID.
- **Rolle**: Beschreibendes Feld, möglicherweise ein Fremdschlüssel.
- **Typischer Inhalt**: Eine Ganzzahl oder `null`, falls nicht zutreffend.

### sub_org_id
- **Bedeutung**: Diese Spalte identifiziert die der Präferenz zugeordnete Unterorganisation.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge oder `null`, falls nicht zutreffend.

Die Tabelle `public.preferences` bietet eine flexible und umfassende Möglichkeit, Konfigurationseinstellungen über verschiedene Organisationseinheiten hinweg zu verwalten, sodass Präferenzen dynamisch angepasst und im Zeitverlauf nachverfolgt werden können.
```

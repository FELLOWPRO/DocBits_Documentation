# TF-IDF-Präferenzen

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `tfidf_id`: intern
* `pref_key`: intern
* `pref_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_by`: intern
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_by`: intern
* `deleted_on`: timestamp with time zone
* `supplier_id`: intern

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.tfidf_preferences`

## Einführung

Die Tabelle `public.tfidf_preferences` dient offenbar zur Speicherung von Einstellungen im Zusammenhang mit TF-IDF-Konfigurationen (Term Frequency-Inverse Document Frequency) bzw. -Modellen. Sie enthält Informationen zu bestimmten, von Organisationen festgelegten Einstellungen, einschließlich Einstellungsschlüsseln und den zugehörigen Werten, sowie Metadaten zu Erstellung, Änderung und Löschung.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die eindeutige ID eines Einstellungseintrags darstellt.

### org_id
- **Bedeutung**: Kennung der Organisation, die der Einstellung zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Einstellung mit einer bestimmten Organisation verknüpft.

### tfidf_id
- **Bedeutung**: Kennung der jeweiligen TF-IDF-Konfiguration bzw. des jeweiligen Modells.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die verknüpfte TF-IDF-Konfiguration darstellt.

### pref_key
- **Bedeutung**: Der Schlüssel bzw. Name der Einstellung.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die den Namen der Einstellung darstellt, etwa 'USE_ETEXT_IF_AVAILABLE' oder 'AI_MODEL'.

### pref_value
- **Bedeutung**: Der dem Einstellungsschlüssel zugeordnete Wert.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Ein Zeichenfolgen- oder Textwert, der zum Einstellungsschlüssel gehört, z. B. 'true', 'false' oder 'Full'.

### created_by
- **Bedeutung**: Kennung des Benutzers, der den Einstellungseintrag erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID des Erstellers darstellt.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung des Einstellungseintrags.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der Datum und Uhrzeit der Erstellung angibt.

### last_modified_by
- **Bedeutung**: Kennung des Benutzers, der den Einstellungseintrag zuletzt geändert hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine UUID, die die Benutzer-ID der Person darstellt, die den Eintrag zuletzt geändert hat, sofern zutreffend.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung des Einstellungseintrags.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der Datum und Uhrzeit der letzten Änderung zeigt.

### is_deleted
- **Bedeutung**: Kennzeichen, das angibt, ob der Einstellungseintrag als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein boolescher Wert; `True`, wenn der Eintrag gelöscht ist, andernfalls `False`.

### deleted_by
- **Bedeutung**: Kennung des Benutzers, der den Einstellungseintrag als gelöscht markiert hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine UUID, die die Benutzer-ID desjenigen darstellt, der den Eintrag gelöscht hat, sofern zutreffend.

### deleted_on
- **Bedeutung**: Zeitstempel, zu dem der Einstellungseintrag als gelöscht markiert wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der angibt, wann der Eintrag gelöscht wurde.

### supplier_id
- **Bedeutung**: Kennung des Lieferanten, der der Einstellung zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die den mit der Einstellung verknüpften Lieferanten darstellt.

Diese Dokumentation bietet einen detaillierten Überblick über Zweck und Aufbau der Tabelle `public.tfidf_preferences` und unterstützt Entwickler dabei, effektiv mit diesen Daten zu arbeiten.
```

# Field validation rules

## Spalten

* `id`: internal
* `org_id`: ID to organisation
* `field_id`: internal
* `doc_type`: DOC Type
* `is_sub_doc_type_field`: boolean
* `profile`: internal
* `field_name`: internal
* `field_length`: integer
* `field_label`: internal
* `is_required`: boolean
* `is_readonly`: boolean
* `is_hidden`: boolean
* `force_validation`: boolean
* `validation_pattern`: internal
* `confidence_threshold`: integer
* `match_score_threshold`: integer
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `additional_attributes`: text

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.field_validation_rules`

## Einführung

Die Tabelle `public.field_validation_rules` speichert offenbar Metadaten und Validierungsregeln für Felder, die verschiedenen Dokumenttypen innerhalb einer Organisation zugeordnet sind. Sie dient vermutlich dazu, Datenintegrität und Konsistenz in Formularen oder Dokumenten durchzusetzen, indem sie Anforderungen festlegt, etwa ob ein Feld erforderlich ist, wie lang es sein darf, ob es sichtbar ist und welche Validierungsmuster angewendet werden sollen.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Eindeutige Kennung für jede Feldvalidierungsregel.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die einen Datensatz eindeutig identifiziert.

### org_id
- **Bedeutung**: Kennung der Organisation, für die die Validierungsregel gilt.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine bestimmte Organisation verweist.

### field_id
- **Bedeutung**: Kennung des bestimmten Feldes, dem die Validierungsregel zugeordnet ist.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf ein bestimmtes Feld verweist.

### doc_type
- **Bedeutung**: Gibt den Dokumenttyp an, dem die Feldvalidierungsregel zugeordnet ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die den Dokumenttyp angibt (z. B. `PURCHASE_ORDER_FORM`).

### is_sub_doc_type_field
- **Bedeutung**: Gibt an, ob das Feld zu einem Dokumentuntertyp gehört.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### profile
- **Bedeutung**: Stellt das Profil oder den Kontext dar, in dem die Feldvalidierung angewendet wird.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge wie `DEFAULT`.

### field_name
- **Bedeutung**: Der Name des Feldes, für das die Validierungsregel definiert ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die den Feldnamen darstellt (z. B. `Test`).

### field_length
- **Bedeutung**: Die maximal zulässige Länge des Feldinhalts.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die das Zeichenlimit angibt.

### field_label
- **Bedeutung**: Die Beschriftung oder der Anzeigename des Feldes in der Benutzeroberfläche.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In den Beispieldaten üblicherweise null.

### is_required
- **Bedeutung**: Gibt an, ob das Feld für das Dokument obligatorisch ist.
- **Rolle**: Einschränkungsindikator.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### is_readonly
- **Bedeutung**: Gibt an, ob das Feld bearbeitbar oder schreibgeschützt ist.
- **Rolle**: Einschränkungsindikator.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### is_hidden
- **Bedeutung**: Gibt an, ob das Feld in der Benutzeroberfläche ausgeblendet werden soll.
- **Rolle**: Einschränkungsindikator.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### force_validation
- **Bedeutung**: Legt fest, ob die Validierung unabhängig von anderen Bedingungen erzwungen werden soll.
- **Rolle**: Einschränkungsindikator.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### validation_pattern
- **Bedeutung**: Ein Muster (vermutlich Regex), dem der Feldinhalt entsprechen muss.
- **Rolle**: Validierungsregel.
- **Typischer Inhalt**: In den Beispieldaten üblicherweise null.

### confidence_threshold
- **Bedeutung**: Das für die Validierung des Feldes erforderliche Mindestkonfidenzniveau.
- **Rolle**: Validierungseinschränkung.
- **Typischer Inhalt**: Ein Ganzzahlwert, der den Konfidenzschwellenwert darstellt.

### match_score_threshold
- **Bedeutung**: Der für die Validierung des Feldinhalts erforderliche Mindest-Abgleichswert.
- **Rolle**: Validierungseinschränkung.
- **Typischer Inhalt**: Ein Ganzzahlwert, der den Schwellenwert für den Abgleichswert darstellt.

### created_by
- **Bedeutung**: Kennung des Benutzers, der diese Validierungsregel erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Zeitstempel der Erstellung der Validierungsregel.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone.

### last_modified_on
- **Bedeutung**: Zeitstempel der letzten Änderung der Validierungsregel.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, kann null sein, wenn nie geändert.

### is_deleted
- **Bedeutung**: Gibt an, ob die Validierungsregel als gelöscht markiert wurde.
- **Rolle**: Indikator für logisches Löschen.
- **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

### additional_attributes
- **Bedeutung**: Speichert zusätzliche Attribute oder Metadaten, die der Feldvalidierungsregel zugeordnet sind.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Text, in den Beispieldaten häufig null.
```

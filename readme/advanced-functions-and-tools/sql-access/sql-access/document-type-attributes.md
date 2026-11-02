# Dokumenttypattribute

## Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_type_key`: intern
* `sub_doc_type_key`: intern
* `attribute_key`: intern
* `attribute_value`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: intern

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.document_type_attributes`

## Einführung

Die Tabelle `public.document_type_attributes` dient offenbar der Verwaltung von Attributen zu verschiedenen Dokumenttypen im organisatorischen Kontext. Die Tabelle unterstützt vermutlich die Konfigurations- oder Metadatenverwaltung für verschiedene Dokumenttypen wie Rechnungen oder Lieferscheine, indem sie jedem Dokumenttyp bestimmte Attribute zuordnet.

## Spaltenbeschreibungen

### id
- **Bedeutung**: Ein eindeutiger Bezeichner für jeden Datensatz in der Tabelle.
- **Rolle**: Primärschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die eine Zeile der Tabelle eindeutig identifiziert.

### org_id
- **Bedeutung**: Stellt die Organisation dar, zu der das Dokumenttyp-Attribut gehört.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Organisation verweist.

### doc_type_key
- **Bedeutung**: Der Dokumenttyp, für den das Attribut gilt (z. B. INVOICE, DELIVERY_NOTE).
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die einen Dokumenttyp darstellt.

### sub_doc_type_key
- **Bedeutung**: Eine genauere Kategorisierung innerhalb des Dokumenttyps, falls zutreffend.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: In der Regel `None`, d. h. das Feld wird nicht immer verwendet.

### attribute_key
- **Bedeutung**: Der konkrete Attribut- bzw. Eigenschaftsschlüssel, der zum Dokumenttyp gehört.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge, die einen Attributschlüssel darstellt, etwa `SECOND_APPROVAL_BEFORE_EXPORT`.

### attribute_value
- **Bedeutung**: Der Wert, der dem Attributschlüssel für den Dokumenttyp zugeordnet ist.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Zeichenfolge oder ein numerischer Wert, der den Wert des Attributs angibt, z. B. `true`, `123`.

### created_by
- **Bedeutung**: Der Bezeichner des Benutzers, der den Datensatz erstellt hat.
- **Rolle**: Beschreibendes Feld.
- **Typischer Inhalt**: Eine Ganzzahl, die eine Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Der Zeitstempel, zu dem der Datensatz erstellt wurde.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der angibt, wann der Datensatz erstellt wurde.

### last_modified_on
- **Bedeutung**: Der Zeitstempel der letzten Änderung am Datensatz.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der den Zeitpunkt der letzten Aktualisierung angibt.

### is_deleted
- **Bedeutung**: Gibt an, ob der Datensatz als gelöscht markiert ist.
- **Rolle**: Technisches Feld.
- **Typischer Inhalt**: Ein boolescher Wert, wobei `false` bedeutet, dass der Datensatz aktiv ist.

### sub_org_id
- **Bedeutung**: Stellt eine Unterorganisation innerhalb der Hauptorganisation dar, falls zutreffend.
- **Rolle**: Fremdschlüssel.
- **Typischer Inhalt**: In der Regel `None`, d. h. das Feld wird nicht immer verwendet.
```

Diese Dokumentation bietet einen strukturierten Überblick über die Tabelle `public.document_type_attributes` und hilft Entwicklern, Zweck und Verwendung jeder Spalte zu verstehen.

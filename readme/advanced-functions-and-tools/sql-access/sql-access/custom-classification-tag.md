# Custom classification tag

## Tabelle `public.custom_classification_tag`

### Spalten

* `id`: integer
* `org_id`: ID to organisation
* `name`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.custom_classification_tag`

### Einführung

Die Tabelle `public.custom_classification_tag` dient der Verwaltung benutzerdefinierter Klassifizierungs-Tags innerhalb einer Organisation. Sie erfasst wesentliche Informationen zu jedem Tag, darunter die Zuordnung zu einer Organisation, Angaben zu Erstellung und Änderung sowie den Lebenszyklusstatus.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Ein eindeutiger Bezeichner für jedes Klassifizierungs-Tag.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine Ganzzahl, die jeden Datensatz in der Tabelle eindeutig identifiziert.

#### org\_id

* **Bedeutung**: Der Bezeichner der Organisation, zu der das Klassifizierungs-Tag gehört.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Zeichenfolge, vermutlich eine UUID, die die eindeutige ID der Organisation darstellt.

#### name

* **Bedeutung**: Der Name oder die Bezeichnung des Klassifizierungs-Tags.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Namen oder die Beschreibung des Tags angibt. Sie kann ein leerer String sein, wenn kein Name angegeben wurde.

#### created\_by

* **Bedeutung**: Der Bezeichner des Benutzers, der das Klassifizierungs-Tag erstellt hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID des Erstellers darstellt.

#### created\_on

* **Bedeutung**: Der Zeitstempel, der angibt, wann das Klassifizierungs-Tag erstellt wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der Datum und Uhrzeit der Erstellung exakt erfasst.

#### last\_modified\_on

* **Bedeutung**: Der Zeitstempel der letzten Änderung am Klassifizierungs-Tag.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzone, der `None` sein kann, wenn seit der Erstellung keine Änderungen stattgefunden haben.

#### is\_deleted

* **Bedeutung**: Ein Kennzeichen, das angibt, ob das Klassifizierungs-Tag als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`), wobei `False` bedeutet, dass das Tag aktiv ist, und `True`, dass es gelöscht oder deaktiviert wurde.

# Lookup field configuration

## Tabelle `public.lookup_field_configuration`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `lookup_rec_id`: internal
* `field_id`: internal
* `lookup_field`: internal
* `is_searchable`: boolean
* `parent_field_id`: internal
* `auto_trigger`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `search_operator`: internal
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Tabellendokumentation: `public.lookup_field_configuration`

### Einführung

Die Tabelle `public.lookup_field_configuration` ist offenbar eine Konfigurationstabelle, mit der Lookup-Felder innerhalb einer Anwendung definiert und verwaltet werden. Sie enthält Metadaten zu jedem Feld, etwa Kennung, zugehörige Organisation, Durchsuchbarkeit und Audit-Informationen. Die Tabelle ist vermutlich Teil eines größeren Systems zur Verwaltung dynamischer oder benutzerdefinierter Felder und ermöglicht komplexe Abfragen und Konfigurationen.

### Spaltenbeschreibungen

#### `id`

* **Bedeutung**: Die eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Konfigurationseintrag eindeutig identifiziert.

#### `org_id`

* **Bedeutung**: Die Organisationskennung, der diese Konfiguration zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Organisation darstellt.

#### `lookup_rec_id`

* **Bedeutung**: Eine Kennung für den spezifischen Lookup-Datensatz, auf den sich diese Konfiguration bezieht.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf einen bestimmten Lookup-Datensatz verweist.

#### `field_id`

* **Bedeutung**: Die Kennung des Feldes, das konfiguriert wird.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf ein bestimmtes Feld verweist.

#### `lookup_field`

* **Bedeutung**: Der Name oder die Bezeichnung des Feldes, das konfiguriert wird.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die den Feldnamen darstellt, etwa "address\_1" oder "taxratefree".

#### `is_searchable`

* **Bedeutung**: Gibt an, ob das Feld in Suchvorgänge einbezogen werden kann.
* **Rolle**: Konfigurationskennzeichen.
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`).

#### `parent_field_id`

* **Bedeutung**: Kennung des übergeordneten Feldes, falls zutreffend.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge oder `None`, wenn kein übergeordnetes Feld existiert.

#### `auto_trigger`

* **Bedeutung**: Legt fest, ob die Feldkonfiguration bestimmte Aktionen automatisch auslösen soll.
* **Rolle**: Konfigurationskennzeichen.
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`).

#### `created_by`

* **Bedeutung**: Die Kennung des Benutzers, der den Konfigurationseintrag erstellt hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.

#### `created_on`

* **Bedeutung**: Der Zeitstempel der Erstellung des Konfigurationseintrags.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.

#### `last_modified_on`

* **Bedeutung**: Der Zeitstempel der letzten Änderung des Konfigurationseintrags.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation oder `None`, wenn nie geändert.

#### `is_deleted`

* **Bedeutung**: Gibt an, ob der Konfigurationseintrag als gelöscht markiert wurde.
* **Rolle**: Kennzeichen für logisches Löschen.
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`).

#### `deleted_on`

* **Bedeutung**: Der Zeitstempel, wann der Konfigurationseintrag als gelöscht markiert wurde.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation oder `None`, wenn nicht gelöscht.

#### `search_operator`

* **Bedeutung**: Definiert den Suchoperator, der für das Feld verwendet wird.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: Eine Zeichenfolge wie "contains", die die Art des Suchvorgangs angibt.

#### `last_modified_by`

* **Bedeutung**: Kennung des Benutzers, der den Konfigurationseintrag zuletzt geändert hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge oder `None`, wenn nie geändert.

#### `deleted_by`

* **Bedeutung**: Kennung des Benutzers, der den Eintrag als gelöscht markiert hat.
* **Rolle**: Audit-Feld.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge oder `None`, wenn nicht gelöscht.

Diese Dokumentation bietet einen detaillierten Einblick in Struktur und Zweck jeder Spalte der Tabelle `public.lookup_field_configuration` und vermittelt Entwicklern ein umfassendes Verständnis davon, wie Lookup-Felder im System konfiguriert und verwaltet werden.

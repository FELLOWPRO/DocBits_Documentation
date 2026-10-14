# Lookup table

## Tabelle `public.lookup_table`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `data_key`: internal
* `rec_id`: internal
* `prop_name`: internal
* `prop_value`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `prop_value_clean`: internal
* `version`: integer
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.lookup_table`

### Einführung

Die Tabelle `public.lookup_table` speichert Metadaten zu verschiedenen Eigenschaften, die Organisationsdaten zugeordnet sind. Sie dient vermutlich als Schlüssel-Wert-Speicher für unterschiedliche Attribute von Kunden oder anderen Entitäten innerhalb der Organisation. Die Tabelle erfasst Informationen wie Eigenschaftsnamen, Werte und den Kontext (z. B. die Organisation und Unterorganisation, zu der sie gehören) sowie Audit-Informationen wie Zeitstempel für Erstellung und Änderung.

### Spaltenbeschreibungen

#### `id`

* **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Eintrag eindeutig identifiziert.

#### `org_id`

* **Bedeutung**: Kennung der Organisation, zu der die Daten gehören.
* **Rolle**: Fremdschlüssel, der vermutlich auf eine Organisationstabelle verweist.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Organisation darstellt.

#### `data_key`

* **Bedeutung**: Ein Schlüssel, der einen bestimmten Datensatz oder Kontext innerhalb der Organisation darstellt.
* **Rolle**: Kontextkennung zur Gruppierung zusammengehöriger Eigenschaften.
* **Typischer Inhalt**: Alphanumerische Zeichenfolge, die eine Kategorie angibt, etwa `customer_amier`.

#### `rec_id`

* **Bedeutung**: Kennung eines bestimmten Datensatzes innerhalb des Datasets.
* **Rolle**: Kontextkennung, möglicherweise ein Fremdschlüssel auf eine andere Tabelle.
* **Typischer Inhalt**: Alphanumerische Zeichenfolge oder null für Datensätze ohne spezifische Kennung.

#### `prop_name`

* **Bedeutung**: Name der Eigenschaft oder des Attributs.
* **Rolle**: Beschreibendes Feld, das angibt, was der Eigenschaftswert darstellt.
* **Typischer Inhalt**: Zeichenfolgen wie 'Kundennummer', 'Versandanschrift', 'Kundenname' usw.

#### `prop_value`

* **Bedeutung**: Wert der durch `prop_name` beschriebenen Eigenschaft.
* **Rolle**: Beschreibendes Feld mit den eigentlichen Daten oder dem Wert.
* **Typischer Inhalt**: Zeichenfolgen oder Zahlen, die den Wert der Eigenschaft darstellen.

#### `created_by`

* **Bedeutung**: Kennung des Benutzers oder Systems, das den Datensatz erstellt hat.
* **Rolle**: Technisches Feld für Audit-Zwecke.
* **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.

#### `created_on`

* **Bedeutung**: Zeitstempel, der angibt, wann der Datensatz erstellt wurde.
* **Rolle**: Technisches Feld für Audit-Zwecke.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation.

#### `last_modified_on`

* **Bedeutung**: Zeitstempel, der angibt, wann der Datensatz zuletzt geändert wurde.
* **Rolle**: Technisches Feld für Audit-Zwecke.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation, möglicherweise null, wenn nicht geändert.

#### `is_deleted`

* **Bedeutung**: Kennzeichen, das angibt, ob der Datensatz gelöscht ist.
* **Rolle**: Technisches Feld für das logische Löschen.
* **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

#### `prop_value_clean`

* **Bedeutung**: Bereinigte oder aufbereitete Version von `prop_value`.
* **Rolle**: Beschreibendes Feld zur Speicherung eines normalisierten oder standardisierten Wertes.
* **Typischer Inhalt**: Ähnlich wie `prop_value`, möglicherweise null, falls nicht zutreffend.

#### `version`

* **Bedeutung**: Versionsnummer des Datensatzes.
* **Rolle**: Technisches Feld für die Versionsverwaltung.
* **Typischer Inhalt**: Ganzzahl, die die Version des Datensatzes darstellt.

#### `deleted_on`

* **Bedeutung**: Zeitstempel, der angibt, wann der Datensatz als gelöscht markiert wurde.
* **Rolle**: Technisches Feld für Audit-Zwecke.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzoneninformation, möglicherweise null, wenn nicht gelöscht.

#### `sub_org_id`

* **Bedeutung**: Kennung einer Unterorganisation innerhalb der Hauptorganisation.
* **Rolle**: Fremdschlüssel, der möglicherweise auf eine Tabelle für Unterorganisationen verweist.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die die Unterorganisation darstellt, möglicherweise null, falls nicht zutreffend.

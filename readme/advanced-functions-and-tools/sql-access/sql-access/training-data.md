# Trainingsdaten

## Tabelle `public.training_data`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_type`: Dokumenttyp
* `doc_origin`: Doc Origin
* `doc_locale`: Doc Locale
* `doc_language`: Language
* `first_page_content`: text
* `supplier_name`: Lieferantenname
* `supplier_vat`: intern
* `doc_created_on`: timestamp with time zone
* `is_training_sample`: boolean
* `sample_doc_id`: intern
* `sample_file_name`: intern
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_table_training_sample`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.training_data`

### Einführung

Die Tabelle `public.training_data` dient offenbar zur Speicherung verschiedener dokumentbezogener Daten, die vermutlich zum Training von Modellen oder Systemen verwendet werden, die Dokumentinhalte verarbeiten und analysieren. Die Tabelle enthält Informationen zu Dokumenttyp, Herkunft, Sprache, Lieferantendaten und Zeitstempeln für Erstellung und Änderung der Datensätze sowie weitere Attribute. Sie scheint besonders auf Rechnungen und medizinische Belege ausgerichtet zu sein, was auf einen Einsatz in der Verarbeitung von Finanz- oder Gesundheitsdaten hindeutet.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Ein universell eindeutiger Bezeichner (UUID) im Zeichenformat.
* **Hinweis**: Unerlässlich, um jeden Eintrag eindeutig zu identifizieren.

#### org\_id

* **Bedeutung**: Kennung der Organisation, die dem Dokument zugeordnet ist.
* **Rolle**: Fremdschlüssel, der auf einen Organisationsdatensatz verweist.
* **Typischer Inhalt**: UUID, die eine Organisation repräsentiert.
* **Hinweis**: Hilft dabei, Dokumente bestimmten Organisationen zuzuordnen.

#### doc\_type

* **Bedeutung**: Typ des im Datensatz gespeicherten Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Werte wie 'INVOICE' oder 'MEDICAL\_RECEIPT'.
* **Hinweis**: Nützlich zur Kategorisierung der Dokumente.

#### doc\_origin

* **Bedeutung**: Herkunft bzw. Ländercode der Quelle des Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ländercode wie 'DE' für Deutschland.
* **Hinweis**: Gibt die geografische Herkunft des Dokuments an.

#### doc\_locale

* **Bedeutung**: Gebietsschema-Information des Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Gebietsschema-Code wie 'en\_DE'.
* **Hinweis**: Kombiniert Sprache und Region für Lokalisierungszwecke.

#### doc\_language

* **Bedeutung**: Sprache, in der das Dokument verfasst ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Sprachcode wie 'en' oder 'de'.
* **Hinweis**: Gibt die im Dokument hauptsächlich verwendete Sprache an.

#### first\_page\_content

* **Bedeutung**: Inhalt der ersten Seite des Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Textdaten mit dem Inhalt der ersten Dokumentseite.
* **Hinweis**: Kann für Textanalyse oder -verarbeitung verwendet werden.

#### supplier\_name

* **Bedeutung**: Name des Lieferanten, der dem Dokument zugeordnet ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Name des Lieferanten im Textformat.
* **Hinweis**: Wichtig zur Identifikation der Quelle oder des Urhebers des Dokuments.

#### supplier\_vat

* **Bedeutung**: Umsatzsteuer-Identifikationsnummer des Lieferanten.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: USt-IdNr., z. B. 'DE 129375678'.
* **Hinweis**: Nützlich für steuerliche Prozesse.

#### doc\_created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Dokuments.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Datum und Uhrzeit im UTC-Format.
* **Hinweis**: Liefert den zeitlichen Kontext der Dokumenterstellung.

#### is\_training\_sample

* **Bedeutung**: Kennzeichen, ob der Datensatz als Trainingsbeispiel verwendet wird.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).
* **Hinweis**: Identifiziert Datensätze, die gezielt für Trainingszwecke markiert sind.

#### sample\_doc\_id

* **Bedeutung**: Kennung des Beispieldokuments.
* **Rolle**: Beschreibendes Feld oder möglicher Fremdschlüssel.
* **Typischer Inhalt**: UUID, die auf ein anderes Dokument verweist.
* **Hinweis**: Kann auf ein verwandtes oder ursprüngliches Dokument verweisen, das als Beispiel diente.

#### sample\_file\_name

* **Bedeutung**: Name der Datei, die dem Dokumentbeispiel zugeordnet ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Dateiname im Textformat.
* **Hinweis**: Nützlich für die Dateiverwaltung oder das Auffinden von Dateien.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit im UTC-Format.
* **Hinweis**: Gibt an, wann der Datensatz zur Datenbank hinzugefügt wurde.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung des Datensatzes.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit im UTC-Format.
* **Hinweis**: Verfolgt, wann der Datensatz zuletzt aktualisiert wurde.

#### is\_deleted

* **Bedeutung**: Kennzeichen, ob der Datensatz als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).
* **Hinweis**: Unterstützt die „Soft Delete“-Funktionalität.

#### is\_table\_training\_sample

* **Bedeutung**: Kennzeichen, ob der Datensatz ein tabellenspezifisches Trainingsbeispiel ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).
* **Hinweis**: Unterscheidet sich von allgemeinen Trainingsbeispielen, da der Fokus auf Tabellendaten liegt.

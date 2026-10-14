# Fellow kv table column rule

## Tabelle `public.fellow_kv_table_column_rule`

### Spalten

* `id`: internal
* `docType`: internal
* `tableName`: internal
* `dlfName`: internal
* `multi_line`: boolean
* `filterID1`: internal
* `filterID2`: internal
* `filterID3`: internal
* `tfidf_doc_id`: internal
* `tfidf_id`: internal
* `valuePattern`: internal
* `coordsY0`: integer
* `coordsY1`: integer
* `coordsX0`: integer
* `coordsX1`: integer
* `normalizedY0`: numeric
* `normalizedY1`: numeric
* `normalizedX0`: numeric
* `normalizedX1`: numeric
* `width`: integer
* `height`: integer
* `patternLeft`: internal
* `patternRight`: internal
* `patternAbove`: internal
* `patternBelow`: internal
* `wordLeft`: internal
* `wordAbove`: internal
* `ruleWeight`: integer
* `user_id`: integer
* `org_id`: ID to organisation
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `is_new`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.fellow_kv_table_column_rule`

### Einführung

Die Tabelle `public.fellow_kv_table_column_rule` dient offenbar dazu, Regeln und Muster für die Verarbeitung oder Extraktion von Daten aus Dokumenten zu speichern. Das lässt sich aus Feldern wie `docType`, `tableName`, `dlfName` sowie diversen muster- und koordinatenbezogenen Feldern ableiten. Die Tabelle scheint die Anwendung von Regeln auf verschiedene Dokumenttypen zu ermöglichen und damit Mustererkennung und Datenextraktion aus strukturierten Dokumenten wie Rechnungen oder Verträgen zu unterstützen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jede Regel.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolgen.
* **Hinweis**: Unerlässlich, um jede Zeile eindeutig zu identifizieren.

#### docType

* **Bedeutung**: Dokumenttyp, auf den die Regel angewendet wird.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Dokumenttypen wie 'INVOICE', 'CONTRACT'.
* **Hinweis**: Hilft, Regeln nach Dokumenttyp zu kategorisieren.

#### tableName

* **Bedeutung**: Name der Tabelle, auf die die Regel angewendet wird.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Tabellennamen wie 'INVOICE\_TABLE'.
* **Hinweis**: Gibt den Kontext an, in dem die Regel angewendet wird.

#### dlfName

* **Bedeutung**: Bestimmter Feld- oder Spaltenname im Dokument.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Feldnamen wie 'COUNTRY\_ORIGIN'.
* **Hinweis**: Legt das Zielfeld für die Datenextraktion fest.

#### multi\_line

* **Bedeutung**: Gibt an, ob die Regel auf mehrzeiligen Text angewendet wird.
* **Rolle**: Boolesches Kennzeichen.
* **Typischer Inhalt**: `True` oder `False`.
* **Hinweis**: Nützlich für den Umgang mit mehrzeiligen Textfeldern.

#### filterID1, filterID2, filterID3

* **Bedeutung**: Filter oder Bedingungen für die Anwendung der Regel.
* **Rolle**: Beschreibende oder bedingte Felder.
* **Typischer Inhalt**: Möglicherweise Zeichenfolgen, die Filterbedingungen darstellen.
* **Hinweis**: Dient dazu, die Anwendung der Regel anhand bestimmter Bedingungen einzugrenzen.

#### tfidf\_doc\_id, tfidf\_id

* **Bedeutung**: Kennungen im Zusammenhang mit der TF-IDF-Verarbeitung.
* **Rolle**: Fremdschlüsselähnliche Rollen oder Kennungen.
* **Typischer Inhalt**: UUID-Zeichenfolgen.
* **Hinweis**: Stehen vermutlich im Zusammenhang mit Textanalyse und Merkmalsextraktion.

#### valuePattern

* **Bedeutung**: Regex-Muster für die Wertextraktion.
* **Rolle**: Musterfeld.
* **Typischer Inhalt**: Reguläre Ausdrücke.
* **Hinweis**: Definiert das Muster, mit dem Werte erkannt und extrahiert werden.

#### coordsY0, coordsY1, coordsX0, coordsX1

* **Bedeutung**: Koordinaten, die den Begrenzungsrahmen für die Extraktion definieren.
* **Rolle**: Koordinatenfelder.
* **Typischer Inhalt**: Ganzzahlen, die Pixelpositionen darstellen.
* **Hinweis**: Definieren den relevanten Bereich in einem Dokument für die Datenextraktion.

#### normalizedY0, normalizedY1, normalizedX0, normalizedX1

* **Bedeutung**: Normalisierte Koordinaten für die Extraktion.
* **Rolle**: Koordinatenfelder.
* **Typischer Inhalt**: Numerische Werte, die proportionale Positionen darstellen.
* **Hinweis**: Werden für auflösungsunabhängige Bereichsdefinitionen verwendet.

#### width, height

* **Bedeutung**: Abmessungen des durch die Koordinaten definierten Bereichs.
* **Rolle**: Maßfelder.
* **Typischer Inhalt**: Ganzzahlwerte.
* **Hinweis**: Helfen bei der Festlegung der Größe des Extraktionsbereichs.

#### patternLeft, patternRight, patternAbove, patternBelow

* **Bedeutung**: Kontextmuster, die die Zieldaten umgeben.
* **Rolle**: Musterfelder.
* **Typischer Inhalt**: Reguläre Ausdrücke.
* **Hinweis**: Liefern Kontext dafür, wo sich Daten relativ zu anderem Text befinden.

#### wordLeft, wordAbove

* **Bedeutung**: Bestimmte Wörter in der Nähe der Zieldaten.
* **Rolle**: Kontextfelder.
* **Typischer Inhalt**: Bestimmte Wörter oder Phrasen.
* **Hinweis**: Helfen, die Suche nach den Zieldaten anhand benachbarter Wörter zu verfeinern.

#### ruleWeight

* **Bedeutung**: Bedeutung oder Priorität der Regel.
* **Rolle**: Gewichtungs- oder Prioritätsfeld.
* **Typischer Inhalt**: Ganzzahlwerte.
* **Hinweis**: Höhere Werte können eine höhere Priorität oder Wichtigkeit anzeigen.

#### user\_id

* **Bedeutung**: Kennung des Benutzers, der die Regel erstellt oder geändert hat.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Ganzzahlwerte.
* **Hinweis**: Verknüpft die Regel mit einem bestimmten Benutzer.

#### org\_id

* **Bedeutung**: Kennung der Organisation, die der Regel zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolgen.
* **Hinweis**: Ordnet die Regel einer Organisation zu.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung der Regel.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone.
* **Hinweis**: Nützlich, um den Erstellungsverlauf der Regel nachzuvollziehen.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung der Regel.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Zeitstempel mit Zeitzone oder `None`.
* **Hinweis**: Verfolgt Änderungen an der Regel im Zeitverlauf.

#### is\_deleted

* **Bedeutung**: Gibt an, ob die Regel als gelöscht markiert ist.
* **Rolle**: Boolesches Kennzeichen.
* **Typischer Inhalt**: `True` oder `False`.
* **Hinweis**: Wird für das logische Löschen (Soft Delete) von Regeln verwendet.

#### is\_new

* **Bedeutung**: Gibt an, ob die Regel neu erstellt wurde.
* **Rolle**: Boolesches Kennzeichen.
* **Typischer Inhalt**: `True` oder `False`.
* **Hinweis**: Hilft, kürzlich hinzugefügte Regeln zu erkennen.

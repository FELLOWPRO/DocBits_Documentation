# Abfragekonfiguration

## Tabelle `public.lookup_configuration`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `doc_type`: Dokumenttyp
* `lookup_dataset_name`: intern
* `lookup_name`: intern
* `conflict_handle`: intern
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `match_all`: boolean
* `last_modified_by`: intern
* `deleted_by`: intern
* `context`: intern
* `context_detail`: intern

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.lookup_configuration`

### Einführung

Die Tabelle `public.lookup_configuration` speichert Konfigurationseinstellungen für verschiedene Daten-Lookup-Vorgänge innerhalb einer Organisation. Sie enthält Informationen zur Organisation, zum Typ der betroffenen Dokumente sowie zu den für Lookups verwendeten Datensätzen und Namen. Die Tabelle verfolgt außerdem die Erstellung und Änderung dieser Konfigurationen sowie ihren aktuellen Status (aktiv oder gelöscht).

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Lookup-Konfigurationseintrag in der Tabelle.
* **Rolle**: Primärschlüssel, der jede Zeile eindeutig identifiziert.
* **Typischer Inhalt**: UUID-Werte, z. B. `'68454d10-e045-4d64-8dd3-774bcb5b6013'`.

#### org\_id

* **Bedeutung**: Stellt die Organisation dar, der die Lookup-Konfiguration zugeordnet ist.
* **Rolle**: Fremdschlüssel, der auf eine Organisation in einer anderen Tabelle verweist.
* **Typischer Inhalt**: UUID-Werte, die Organisationskennungen angeben, z. B. `'23f3d697-7411-4c95-981d-faf089d266be'`.

#### doc\_type

* **Bedeutung**: Gibt den Dokumenttyp an, auf den die Lookup-Konfiguration angewendet wird.
* **Rolle**: Beschreibendes Feld, das den Kontext der Konfiguration angibt.
* **Typischer Inhalt**: Zeichenfolgen wie `'MEDI_ORDER'`, `'INVOICE'` usw.

#### lookup\_dataset\_name

* **Bedeutung**: Der Name des Datensatzes, der für Lookups verwendet wird.
* **Rolle**: Beschreibendes Feld zur Identifizierung von Datensätzen.
* **Typischer Inhalt**: Beschreibende Zeichenfolgen wie `'customer_tini'`, `'supplier'`.

#### lookup\_name

* **Bedeutung**: Der spezifische Name oder Alias, der für den Lookup-Vorgang verwendet wird.
* **Rolle**: Beschreibendes Feld, das den operativen Namen angibt.
* **Typischer Inhalt**: Zeichenfolgen wie `'customer_tini'`, `'supplier (copy)'`.

#### conflict\_handle

* **Bedeutung**: Gibt die Strategie zur Behandlung von Konflikten bei Lookups an.
* **Rolle**: Beschreibendes Feld für die Konfliktlösungsstrategie.
* **Typischer Inhalt**: Werte wie `'BEST_SCORE'`, `'RETURN_NONE'`.

#### created\_by

* **Bedeutung**: Die ID des Benutzers, der die Lookup-Konfiguration erstellt hat.
* **Rolle**: Technisches Feld zur Nachverfolgung des Erstellers des Eintrags.
* **Typischer Inhalt**: Ganzzahlwerte, die Benutzer-IDs darstellen, z. B. `1`.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung der Lookup-Konfiguration.
* **Rolle**: Technisches Feld zur Nachverfolgung des Erstellungszeitpunkts.
* **Typischer Inhalt**: Zeitstempel, z. B. `2024-02-08 11:24:14 UTC`.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung der Lookup-Konfiguration.
* **Rolle**: Technisches Feld zur Nachverfolgung des Zeitpunkts der letzten Aktualisierung.
* **Typischer Inhalt**: Zeitstempel, üblicherweise `None`, wenn nicht geändert.

#### is\_deleted

* **Bedeutung**: Gibt an, ob die Lookup-Konfiguration als gelöscht markiert wurde.
* **Rolle**: Boolesches Feld zur Statusverfolgung.
* **Typischer Inhalt**: Boolesche Werte, `False` für aktive Einträge.

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann die Lookup-Konfiguration als gelöscht markiert wurde.
* **Rolle**: Technisches Feld zur Nachverfolgung des Löschzeitpunkts.
* **Typischer Inhalt**: Häufig ein Platzhalterdatum als Standardwert, z. B. `0002-01-01 11:00:00 UTC`.

#### match\_all

* **Bedeutung**: Legt fest, ob der Lookup alle Bedingungen erfüllen muss.
* **Rolle**: Boolesches Feld für Konfigurationseinstellungen.
* **Typischer Inhalt**: Boolesche Werte, üblicherweise `False`.

#### last\_modified\_by

* **Bedeutung**: Die ID des Benutzers, der die Lookup-Konfiguration zuletzt geändert hat.
* **Rolle**: Technisches Feld zur Nachverfolgung des Benutzers, der den Eintrag zuletzt aktualisiert hat.
* **Typischer Inhalt**: UUID oder Kennung des ändernden Benutzers, häufig `None`.

#### deleted\_by

* **Bedeutung**: Die ID des Benutzers, der die Lookup-Konfiguration als gelöscht markiert hat.
* **Rolle**: Technisches Feld zur Nachverfolgung des für die Löschung verantwortlichen Benutzers.
* **Typischer Inhalt**: UUID oder Kennung, häufig `None`.

#### context

* **Bedeutung**: Der Kontext, in dem der Lookup angewendet wird, etwa ein Abschnitt eines Dokuments.
* **Rolle**: Beschreibendes Feld für den operativen Kontext.
* **Typischer Inhalt**: Zeichenfolgen wie `'header'`.

#### context\_detail

* **Bedeutung**: Zusätzliche Details zum Kontext des Lookups.
* **Rolle**: Beschreibendes Feld für erweiterte Kontextinformationen.
* **Typischer Inhalt**: Häufig `None`, wird für eine zusätzliche Kontextbeschreibung verwendet.

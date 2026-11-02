# Konfiguration von REST-API-Abfragen

## Tabelle `public.rest_api_lookup_configurations`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `sub_org_id`: intern
* `data_key`: intern
* `url`: intern
* `method`: intern
* `params`: text
* `headers`: text
* `body`: text
* `body_type`: intern
* `authentication_type`: intern
* `authentication_json`: text
* `data_base_path`: intern
* `column_paths`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `is_template`: boolean
* `is_dynamic`: boolean

### Analyse & Beschreibung

## Technische Dokumentation: Tabelle `public.rest_api_lookup_configurations`

### Einführung

Die Tabelle `public.rest_api_lookup_configurations` speichert Konfigurationen für REST-API-Lookups innerhalb einer Organisation. Sie enthält die wesentlichen Informationen zum Ausführen von API-Anfragen, einschließlich Details zu den Endpunkten, Authentifizierungsmethoden und Anfrage-/Antwortkonfigurationen. Sie dient offenbar dazu, API-Aufrufe dynamisch aufzubauen und deren Ergebnisse auszuwerten.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Eindeutige Kennung für jeden Konfigurationseintrag.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolgen wie `5e9b3637-79a1-4535-99cf-9247dfa48960`.
* **Hinweis**: Dies ist der eindeutige Schlüssel zur Identifizierung einer bestimmten API-Lookup-Konfiguration.

#### org\_id

* **Bedeutung**: Kennung der Organisation, der die Konfiguration gehört.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolgen, die Organisations-IDs darstellen.
* **Hinweis**: Verknüpft die Konfiguration mit einer Organisation.

#### sub\_org\_id

* **Bedeutung**: Kennung einer Unterorganisation innerhalb der primären Organisation.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: UUID-Zeichenfolgen, die IDs von Unterorganisationen darstellen.
* **Hinweis**: Ermöglicht eine feinere Granularität innerhalb von Organisationen.

#### data\_key

* **Bedeutung**: Eine Bezeichnung oder ein Schlüssel zur Identifizierung der Daten oder des API-Endpunkts.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Beschreibender Text wie `bank_codes`.
* **Hinweis**: Dient zur Unterscheidung verschiedener Datentypen oder Endpunkte.

#### url

* **Bedeutung**: Die URL des aufzurufenden API-Endpunkts.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: URL-Zeichenfolgen wie `/M3/m3api-rest/v2/execute/CRS692MI/LstByID`.
* **Hinweis**: Stellt den Endpunkt dar, an den die HTTP-Anfrage gesendet wird.

#### method

* **Bedeutung**: HTTP-Methode für die API-Anfrage.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Gängige HTTP-Methoden wie `GET`.
* **Hinweis**: Bestimmt die Art der auszuführenden HTTP-Anfrage.

#### params

* **Bedeutung**: Parameter, die in die API-Anfrage aufgenommen werden.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON oder Schlüssel-Wert-Paare (häufig `None`, wenn nicht verwendet).
* **Hinweis**: Enthält dynamische Parameter für die Anfrage.

#### headers

* **Bedeutung**: HTTP-Header, die in die Anfrage aufgenommen werden.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON- oder Textdaten (häufig `None`, wenn nicht verwendet).
* **Hinweis**: Dient dazu, zusätzliche Metadaten in die Anfrage aufzunehmen.

#### body

* **Bedeutung**: Der Body der HTTP-Anfrage.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON-Daten oder andere serialisierte Daten (häufig `None`, wenn nicht verwendet).
* **Hinweis**: Enthält die Nutzdaten für POST-/PUT-Anfragen.

#### body\_type

* **Bedeutung**: Legt das Format des Anfrage-Bodys fest.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: MIME-Typen wie `application/json`.
* **Hinweis**: Gibt den Inhaltstyp des Bodys an.

#### authentication\_type

* **Bedeutung**: Art der Authentifizierung für die API-Anfrage.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Authentifizierungsmethoden wie `ionapi`.
* **Hinweis**: Bestimmt, wie die Anfrage authentifiziert wird.

#### authentication\_json

* **Bedeutung**: Details der Authentifizierungskonfiguration im JSON-Format.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON-Zeichenfolgen mit Authentifizierungsinformationen.
* **Hinweis**: Enthält Anmeldedaten und Endpunktdetails für die Authentifizierung.

#### data\_base\_path

* **Bedeutung**: Pfad innerhalb der API-Antwort, aus dem Daten extrahiert werden.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON-Pfadausdrücke wie `$[results][0][records]`.
* **Hinweis**: Dient dazu, die Daten der API-Antwort auszuwerten.

#### column\_paths

* **Bedeutung**: Ordnet Datenfelder Spalten für die Extraktion zu.
* **Rolle**: Konfigurationsfeld.
* **Typischer Inhalt**: JSON-Zeichenfolgen, die Felder der API-Antwort Spaltennamen zuordnen.
* **Hinweis**: Erleichtert die Datenextraktion aus der API-Antwort.

#### created\_by

* **Bedeutung**: Kennung des Benutzers, der die Konfiguration erstellt hat.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ganzzahl-IDs wie `1`.
* **Hinweis**: Verfolgt den Ersteller des Konfigurationseintrags.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung der Konfiguration.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Zeitstempel wie `2024-01-24T09:14:24.788788Z`.
* **Hinweis**: Gibt Datum und Uhrzeit der Erstellung an.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Zeitstempel (häufig `None`, wenn nicht geändert).
* **Hinweis**: Hält den Zeitpunkt der letzten Aktualisierung fest.

#### is\_deleted

* **Bedeutung**: Kennzeichen, das angibt, ob eine Konfiguration als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolesche Werte wie `False`.
* **Hinweis**: Wird für das logische Löschen (Soft Delete) von Konfigurationen verwendet.

#### deleted\_on

* **Bedeutung**: Zeitstempel, wann die Konfiguration als gelöscht markiert wurde.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Zeitstempel (häufig ein Platzhalter, wenn nicht gelöscht).
* **Hinweis**: Hält fest, wann die Konfiguration als gelöscht markiert wurde.

#### is\_template

* **Bedeutung**: Gibt an, ob die Konfiguration als Vorlage dient.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Boolesche Werte wie `True`.
* **Hinweis**: Kennzeichnet Vorlagen zur Wiederverwendung.

#### is\_dynamic

* **Bedeutung**: Legt fest, ob die Konfiguration dynamisch ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Boolesche Werte wie `False`.
* **Hinweis**: Bestimmt, ob sich die Konfiguration an veränderte Daten anpasst.

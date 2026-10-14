# Supplier address

## Spalten

* `org_id`: ID to organisation
* `customer_number`: internal
* `supplier_number`: internal
* `address_id`: internal
* `supplier_name`: Supplier Name
* `address_1`: internal
* `address_2`: internal
* `address_3`: internal
* `address_4`: internal
* `zip_code`: internal
* `town_city`: internal
* `country_code`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `sub_org_id`: internal
* `id`: internal

## Analyse & Beschreibung

```markdown
# Technische Dokumentation der Tabelle `public.supplier_address`

## Einführung

Die Tabelle `public.supplier_address` dient zur Speicherung von Informationen zu den Adressen von Lieferanten. Sie enthält verschiedene Felder, die Angaben wie Organisations-IDs, Kunden- und Lieferantennummern, mehrere Adresszeilen, Kontaktdaten, Metadaten zu Erstellung und Änderung sowie den Löschstatus erfassen. Die Tabelle wird vermutlich in einem System zur Verwaltung von Lieferantendaten und deren Adressen verwendet, die für Logistik, Abrechnung und Kontaktaufnahme von Bedeutung sein können.

## Spaltenbeschreibungen

### org_id
- **Bedeutung**: Diese Spalte speichert die eindeutige Kennung der Organisation.
- **Rolle**: Fremdschlüssel, der möglicherweise auf eine Organisationstabelle verweist.
- **Typischer Inhalt**: UUID, die eine Organisation repräsentiert.

### customer_number
- **Bedeutung**: Diese Spalte speichert möglicherweise eine eindeutige, Kunden zugewiesene Nummer.
- **Rolle**: Kennung für Kunden.
- **Typischer Inhalt**: Alphanumerische Zeichenfolge, die Kundennummern darstellt.

### supplier_number
- **Bedeutung**: Diese Spalte speichert eine eindeutige, Lieferanten zugewiesene Nummer.
- **Rolle**: Kennung für Lieferanten.
- **Typischer Inhalt**: Numerische Zeichenfolge, die Lieferantennummern darstellt.

### address_id
- **Bedeutung**: Diese Spalte speichert vermutlich den Adresstyp, etwa „Discrete“ oder „Text“.
- **Rolle**: Beschreibendes Feld zur Kategorisierung von Adressen.
- **Typischer Inhalt**: Werte wie 'Discrete', 'Text'.

### supplier_name
- **Bedeutung**: Diese Spalte speichert den Namen des Lieferanten.
- **Rolle**: Beschreibendes Feld zur Identifikation des Lieferanten.
- **Typischer Inhalt**: Name des Lieferanten, z. B. "Cake Corp. GmbH Qualitätsstrawberrys".

### address_1
- **Bedeutung**: Diese Spalte speichert die erste Zeile der Lieferantenadresse.
- **Rolle**: Beschreibendes Feld für Adressinformationen.
- **Typischer Inhalt**: Straßenadresse, z. B. "Irrweg. 42, D-12345 Blastadt".

### address_2
- **Bedeutung**: Diese Spalte speichert gegebenenfalls die zweite Zeile der Lieferantenadresse.
- **Rolle**: Ergänzendes Feld für Adressinformationen.
- **Typischer Inhalt**: Zusätzliche Adressangaben, häufig leer.

### address_3
- **Bedeutung**: Diese Spalte speichert gegebenenfalls die dritte Zeile der Lieferantenadresse.
- **Rolle**: Ergänzendes Feld für Adressinformationen.
- **Typischer Inhalt**: Zusätzliche Adressangaben, häufig leer.

### address_4
- **Bedeutung**: Diese Spalte speichert gegebenenfalls die vierte Zeile der Lieferantenadresse.
- **Rolle**: Ergänzendes Feld für Adressinformationen.
- **Typischer Inhalt**: Zusätzliche Adressangaben, häufig leer.

### zip_code
- **Bedeutung**: Diese Spalte speichert die Postleitzahl der Lieferantenadresse.
- **Rolle**: Beschreibendes Feld zur geografischen Zuordnung.
- **Typischer Inhalt**: Numerische Postleitzahl, z. B. "06449".

### town_city
- **Bedeutung**: Diese Spalte speichert den Orts- bzw. Städtenamen der Lieferantenadresse.
- **Rolle**: Beschreibendes Feld zur geografischen Zuordnung.
- **Typischer Inhalt**: Name des Ortes oder der Stadt, z. B. "Aschersleben".

### country_code
- **Bedeutung**: Diese Spalte speichert den ISO-Ländercode der Lieferantenadresse.
- **Rolle**: Beschreibendes Feld zur Identifikation des Landes.
- **Typischer Inhalt**: Zweistelliger Ländercode, z. B. "DE".

### created_by
- **Bedeutung**: Diese Spalte speichert die Kennung des Benutzers oder Systems, das den Datensatz erstellt hat.
- **Rolle**: Technisches Feld zur Nachverfolgung der Datensatzerstellung.
- **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt.

### created_on
- **Bedeutung**: Diese Spalte speichert den Zeitstempel der Datensatzerstellung.
- **Rolle**: Technisches Feld zur Nachverfolgung des Erstellungszeitpunkts.
- **Typischer Inhalt**: Zeitstempel mit Zeitzone, z. B. "2021-11-25 11:24:33 UTC".

### last_modified_on
- **Bedeutung**: Diese Spalte speichert den Zeitstempel der letzten Änderung des Datensatzes.
- **Rolle**: Technisches Feld zur Nachverfolgung des Zeitpunkts der letzten Aktualisierung.
- **Typischer Inhalt**: Zeitstempel mit Zeitzone, häufig `None`.

### is_deleted
- **Bedeutung**: Diese Spalte gibt an, ob der Datensatz als gelöscht markiert ist.
- **Rolle**: Technisches Feld für die „Soft Delete“-Funktionalität.
- **Typischer Inhalt**: Boolescher Wert, z. B. `False`.

### sub_org_id
- **Bedeutung**: Diese Spalte speichert gegebenenfalls die Kennung einer Unterorganisation.
- **Rolle**: Fremdschlüssel bzw. Kennung für Unterorganisationen.
- **Typischer Inhalt**: UUID, häufig leer.

### id
- **Bedeutung**: Diese Spalte speichert die eindeutige Kennung des Datensatzes.
- **Rolle**: Primärschlüssel der Tabelle.
- **Typischer Inhalt**: UUID, die den Datensatz repräsentiert.

```

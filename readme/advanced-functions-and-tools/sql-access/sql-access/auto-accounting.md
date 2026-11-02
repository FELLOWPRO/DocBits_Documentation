# Automatische Kontierung

## Tabelle `public.auto_accounting`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `supplier_name`: Lieferantenname
* `description`: intern
* `item_number`: intern
* `line_amount`: double precision
* `total_amount`: double precision
* `mapped_amount`: double precision
* `ledger_account`: intern
* `doc_id`: intern

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.auto_accounting`

### Einführung

Die Tabelle `public.auto_accounting` dient offenbar der Verwaltung und Speicherung von Buchhaltungsdaten zu verschiedenen Lieferanten und Organisationen. Die Tabelle erfasst Informationen zu Finanztransaktionen, einschließlich Beträgen und Hauptbuchkonten, die für Finanzberichte und Analysen unverzichtbar sind.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Ein eindeutiger Bezeichner für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die jeden Eintrag eindeutig darstellt.
* **Hinweis**: Stellt sicher, dass jeder Datensatz eindeutig identifiziert werden kann.

#### org\_id

* **Bedeutung**: Bezeichner der Organisation, die dem Buchungseintrag zugeordnet ist.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge, die auf eine Organisation in einer übergeordneten Tabelle verweist.
* **Hinweis**: Dient dazu, Buchungseinträge bestimmten Organisationen zuzuordnen.

#### supplier\_name

* **Bedeutung**: Der Name des an der Transaktion beteiligten Lieferanten.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Text, der den Namen des Lieferanten darstellt, etwa "Fellow Consulting AG".
* **Hinweis**: Liefert Informationen zum Lieferanten, der zur Transaktion gehört.

#### description

* **Bedeutung**: Eine kurze Beschreibung der Transaktion oder des Artikels.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Text, der die Transaktion beschreibt, etwa den Namen eines Artikels ("apple" oder "Peaches").
* **Hinweis**: Hilfreich, um die Art der Transaktion zu verstehen.

#### item\_number

* **Bedeutung**: Bezeichner für einen bestimmten Artikel, der an der Transaktion beteiligt ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Könnte eine Produkt- oder SKU-Kennung sein; Beispieldaten liegen nicht vor.
* **Hinweis**: Nützlich, um bestimmte Artikel zu verfolgen oder zu referenzieren.

#### line\_amount

* **Bedeutung**: Der Geldbetrag für eine bestimmte Position der Transaktion.
* **Rolle**: Finanzfeld.
* **Typischer Inhalt**: Ein Dezimalwert, der den Betrag einer einzelnen Position darstellt.
* **Hinweis**: Wichtig für detaillierte Finanzanalysen auf Positionsebene.

#### total\_amount

* **Bedeutung**: Der Gesamtbetrag der Transaktion.
* **Rolle**: Finanzfeld.
* **Typischer Inhalt**: Ein Dezimalwert, der den Gesamtbetrag der Transaktion darstellt.
* **Hinweis**: Entspricht der Summe aller Positionsbeträge einer Transaktion.

#### mapped\_amount

* **Bedeutung**: Der Betrag, der einem bestimmten Konto zugewiesen bzw. zugeordnet wurde.
* **Rolle**: Finanzfeld.
* **Typischer Inhalt**: Ein Dezimalwert, der angibt, wie viel der Transaktion zugeordnet wurde.
* **Hinweis**: Nützlich, um zu verstehen, wie die Mittel auf Konten verteilt werden.

#### ledger\_account

* **Bedeutung**: Die Kontonummer im Hauptbuch, auf der die Transaktion gebucht wird.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Text, der eine Kontonummer darstellt, etwa "2200" oder "2500".
* **Hinweis**: Für die Buchhaltung entscheidend, um nachzuvollziehen, wo Transaktionen gebucht werden.

#### doc\_id

* **Bedeutung**: Ein Bezeichner für ein zugehöriges Dokument oder einen zugehörigen Datensatz.
* **Rolle**: Fremdschlüssel oder Referenz.
* **Typischer Inhalt**: Eine UUID-Zeichenfolge oder ein anderer Bezeichner, der auf zugehörige Dokumente verweist.
* **Hinweis**: Hilft dabei, Transaktionen zur Nachvollziehbarkeit bestimmten Dokumenten oder Datensätzen zuzuordnen.

Diese Dokumentation bietet einen detaillierten Überblick über die Tabelle `public.auto_accounting` und beschreibt ihre Struktur sowie den Zweck jeder Spalte, damit Entwickler und Datenbankadministratoren die Daten effektiv verstehen und nutzen können.

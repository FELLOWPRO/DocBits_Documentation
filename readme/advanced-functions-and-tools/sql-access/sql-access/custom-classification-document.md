# Benutzerdefiniertes Klassifizierungsdokument

## Tabelle `public.custom_classification_document`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `first_page_content`: text
* `content`: text
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean

### Analyse & Beschreibung

## Technische Dokumentation der Tabelle `public.custom_classification_document`

### Einführung

Die Tabelle `public.custom_classification_document` dient der Speicherung detaillierter Informationen zu Dokumentklassifizierungen innerhalb einer Organisation. Dazu gehören Metadaten zum Dokument, etwa Inhalt, Angaben zur Erstellung und der organisatorische Kontext. Die Struktur der Tabelle deutet darauf hin, dass sie für die Verwaltung von Dokumenten zu Organisationsprozessen verwendet wird, möglicherweise Rechnungen oder Bestellformulare, wie aus den Beispieldaten hervorgeht.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Diese Spalte speichert vermutlich einen eindeutigen Bezeichner für jeden Dokumenteintrag.
* **Rolle**: Primärschlüssel
* **Typischer Inhalt**: Eine UUID, die einen eindeutigen Dokumentbezeichner darstellt.

#### org\_id

* **Bedeutung**: Diese Spalte speichert den Bezeichner der Organisation, die dem Dokument zugeordnet ist.
* **Rolle**: Fremdschlüssel
* **Typischer Inhalt**: Eine UUID, die das Dokument mit einer bestimmten Organisation verknüpft.

#### first\_page\_content

* **Bedeutung**: Diese Spalte enthält den Textinhalt der ersten Seite des Dokuments.
* **Rolle**: Datenfeld
* **Typischer Inhalt**: Textdarstellung des Dokuments einer Organisation, möglicherweise mit Kopfzeilen, Adressen und ersten Angaben einer Rechnung oder Bestellung.

#### content

* **Bedeutung**: Diese Spalte speichert den vollständigen Textinhalt des Dokuments.
* **Rolle**: Datenfeld
* **Typischer Inhalt**: Vollständiger Textinhalt des Dokuments, einschließlich aller Angaben der ersten Seite und der folgenden Seiten.

#### created\_by

* **Bedeutung**: Diese Spalte gibt den Benutzer an, der den Dokumenteintrag erstellt hat.
* **Rolle**: Datenfeld
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID des Erstellers darstellt.

#### created\_on

* **Bedeutung**: Diese Spalte erfasst Datum und Uhrzeit der Erstellung des Dokumenteintrags.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation, der Erstellungsdatum und -uhrzeit angibt.

#### last\_modified\_on

* **Bedeutung**: Diese Spalte speichert Datum und Uhrzeit der letzten Änderung des Dokumenteintrags.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation, der Datum und Uhrzeit der letzten Änderung angibt. Er ist teilweise `None`, wenn nach der Erstellung keine Änderungen stattgefunden haben.

#### is\_deleted

* **Bedeutung**: Diese Spalte gibt an, ob der Dokumenteintrag als gelöscht markiert wurde.
* **Rolle**: Technisches Feld
* **Typischer Inhalt**: Ein boolescher Wert (`True` oder `False`), der den Löschstatus des Dokumenteintrags zeigt.

Diese Tabelle bietet eine robuste Struktur für die Verwaltung von Dokumentdaten. Sie stellt sicher, dass jedes Dokument eindeutig identifiziert, einer Organisation zugeordnet und über seinen Lebenszyklus von Erstellung und Änderung hinweg nachverfolgt werden kann.

# Additional charge costing element

## Tabelle `public.additional_charge_costing_element`

### Spalten

* `id`: internal
* `org_id`: ID to organisation
* `costing_element`: internal
* `description`: internal
* `charge_type`: internal
* `distribution_method`: internal
* `distribution_type`: internal
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `deleted_on`: timestamp with time zone
* `sub_org_id`: internal
* `charge_count`: integer
* `charge_icon`: internal
* `charge_category`: internal
* `charge_sequence_number`: integer
* `charge_operator`: integer
* `last_modified_by`: internal
* `deleted_by`: internal

### Analyse & Beschreibung

## Tabellendokumentation: `public.additional_charge_costing_element`

### Einführung

Die Tabelle `public.additional_charge_costing_element` dient der Verwaltung und Speicherung von Informationen zu verschiedenen Kostenelementen für Zusatzkosten innerhalb einer Organisation. Sie enthält Daten zur Art der Kosten, zu deren Verteilung sowie administrative Metadaten wie Angaben zur Erstellung und Änderung. Die Tabelle wird vermutlich für das Finanz- und Betriebsmanagement einer Organisation verwendet und konzentriert sich auf Zusatzkosten, die erfasst und analysiert werden müssen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Diese Spalte speichert einen eindeutigen Bezeichner für jeden Datensatz in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Eine eindeutige alphanumerische Zeichenfolge, die jeden Kostenelement-Datensatz identifiziert.

#### org\_id

* **Bedeutung**: Der Bezeichner der Organisation, zu der dieses Kostenelement gehört.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID, die die Organisation darstellt.

#### costing\_element

* **Bedeutung**: Ein Bezeichner oder Code für das Kostenelement.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine alphanumerische Zeichenfolge, die das konkrete Kostenelement darstellt.

#### description

* **Bedeutung**: Eine Textbeschreibung des Kostenelements.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine kurze Erläuterung des Kostenelements.

#### charge\_type

* **Bedeutung**: Die Art der Kosten, die diesem Kostenelement zugeordnet ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Code oder kurzer Text, der die Kostenart angibt.

#### distribution\_method

* **Bedeutung**: Methode, mit der die Kosten verteilt werden.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Code oder kurzer Text, der die Verteilungsmethode angibt.

#### distribution\_type

* **Bedeutung**: Art der Verteilung der Kosten.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Ein Code oder kurzer Text, der die Verteilungsart angibt.

#### created\_by

* **Bedeutung**: Bezeichner des Benutzers, der den Datensatz erstellt hat.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Eine Ganzzahl, die die Benutzer-ID darstellt.

#### created\_on

* **Bedeutung**: Zeitstempel, der angibt, wann der Datensatz erstellt wurde.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung am Datensatz.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Datensatz als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolescher Wert (`True` oder `False`).

#### deleted\_on

* **Bedeutung**: Zeitstempel, zu dem der Datensatz als gelöscht markiert wurde.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Ein Zeitstempel mit Zeitzoneninformation oder `None`, wenn nicht gelöscht.

#### sub\_org\_id

* **Bedeutung**: Bezeichner einer Unterorganisation, die zum Kostenelement gehört.
* **Rolle**: Fremdschlüssel.
* **Typischer Inhalt**: Eine UUID, die die Unterorganisation darstellt.

#### charge\_count

* **Bedeutung**: Die Anzahl der Kosten, die dem Kostenelement zugeordnet sind.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Ganzzahl, die die Anzahl der Kosten darstellt.

#### charge\_icon

* **Bedeutung**: Symbol oder Icon, das den Kosten zugeordnet ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die das Symbol darstellt, vermutlich ein Pfad oder Bezeichner.

#### charge\_category

* **Bedeutung**: Die Kategorie, in die die Kosten fallen.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Kostenkategorie darstellt.

#### charge\_sequence\_number

* **Bedeutung**: Reihenfolgenummer zur Sortierung der Kosten.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Ganzzahl, mit der die Kosten in eine Reihenfolge gebracht werden.

#### charge\_operator

* **Bedeutung**: Bezeichner des Operators, der für die Kosten verantwortlich ist.
* **Rolle**: Beschreibendes Feld.
* **Typischer Inhalt**: Eine Ganzzahl, die die Operator-ID darstellt.

#### last\_modified\_by

* **Bedeutung**: Bezeichner des Benutzers, der den Datensatz zuletzt geändert hat.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Benutzer-ID darstellt, gegebenenfalls `None`, wenn nie geändert.

#### deleted\_by

* **Bedeutung**: Bezeichner des Benutzers, der den Datensatz als gelöscht markiert hat.
* **Rolle**: Administratives Feld.
* **Typischer Inhalt**: Eine Zeichenfolge, die die Benutzer-ID darstellt, gegebenenfalls `None`, wenn nicht gelöscht.

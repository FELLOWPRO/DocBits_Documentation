# Aktivierungsstatus von Dokumentskripten

## Tabelle `public.document_script_activation_status`

### Spalten

* `id`: intern
* `org_id`: ID der Organisation
* `sort_order`: integer
* `is_active`: boolean
* `created_by`: integer
* `created_on`: timestamp with time zone
* `last_modified_on`: timestamp with time zone
* `is_deleted`: boolean
* `script_id`: intern

### Analyse & Beschreibung

## Tabellendokumentation: `public.document_script_activation_status`

### Einführung

Die Tabelle `public.document_script_activation_status` dient der Verwaltung des Aktivierungsstatus von Skripten, die Dokumenten innerhalb einer Organisation zugeordnet sind. Jeder Eintrag in der Tabelle entspricht einem bestimmten Skript und dessen aktuellem Aktivierungsstatus. So können Organisationen die Ausführung von Skripten im Zusammenhang mit ihren Dokumenten steuern und ordnen.

### Spaltenbeschreibungen

#### id

* **Bedeutung**: Diese Spalte speichert einen eindeutigen Bezeichner für jeden Eintrag in der Tabelle.
* **Rolle**: Primärschlüssel.
* **Typischer Inhalt**: Universell eindeutiger Bezeichner (UUID), etwa `c599a3fa-a784-446a-a48e-cf37b95d93cd`.
* **Hinweis**: Stellt sicher, dass jeder Datensatz eindeutig identifizierbar ist.

#### org\_id

* **Bedeutung**: Stellt den Bezeichner einer Organisation dar.
* **Rolle**: Fremdschlüssel, verweist vermutlich auf eine Organisationstabelle.
* **Typischer Inhalt**: UUID, die die Organisation identifiziert, z. B. `23f3d697-7411-4c95-981d-faf089d266be`.
* **Hinweis**: Verknüpft den Skript-Aktivierungsstatus mit einer bestimmten Organisation.

#### sort\_order

* **Bedeutung**: Gibt die Reihenfolge an, in der Skripte ausgeführt oder angezeigt werden sollen.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Ganzzahlen, die die Reihenfolge darstellen, etwa `0`.
* **Hinweis**: Kann verwendet werden, um Skripte zu priorisieren oder zu ordnen.

#### is\_active

* **Bedeutung**: Gibt an, ob ein Skript derzeit aktiv ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolesche Werte, `True` oder `False`.
* **Hinweis**: Bestimmt, ob das zugehörige Skript ausgeführt werden soll.

#### created\_by

* **Bedeutung**: Bezeichner des Benutzers, der den Datensatz erstellt hat.
* **Rolle**: Fremdschlüssel, verweist vermutlich auf eine Benutzertabelle.
* **Typischer Inhalt**: Ganzzahl, die eine Benutzer-ID darstellt, etwa `1`.
* **Hinweis**: Verfolgt den Ersteller des Datensatzes für Audit-Zwecke.

#### created\_on

* **Bedeutung**: Zeitstempel der Erstellung des Datensatzes.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone, z. B. `2023-11-20 10:44:14.685170+00:00`.
* **Hinweis**: Liefert einen Erstellungszeitstempel für die Datenhaltung.

#### last\_modified\_on

* **Bedeutung**: Zeitstempel der letzten Änderung am Datensatz.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Datum und Uhrzeit mit Zeitzone oder `None`, wenn nie geändert.
* **Hinweis**: Nützlich, um Änderungen im Zeitverlauf nachzuverfolgen.

#### is\_deleted

* **Bedeutung**: Gibt an, ob der Datensatz als gelöscht markiert ist.
* **Rolle**: Technisches Feld.
* **Typischer Inhalt**: Boolesche Werte, `True` oder `False`.
* **Hinweis**: Ermöglicht das weiche Löschen von Datensätzen, ohne sie physisch aus der Datenbank zu entfernen.

#### script\_id

* **Bedeutung**: Bezeichner des Skripts, das dem Datensatz zugeordnet ist.
* **Rolle**: Fremdschlüssel, verweist vermutlich auf eine Skripttabelle.
* **Typischer Inhalt**: UUID, die das Skript identifiziert, z. B. `4edc8cd7-e1bc-443a-9a23-dc490a09e80b`.
* **Hinweis**: Verknüpft den Aktivierungsstatus mit einem bestimmten Skript.

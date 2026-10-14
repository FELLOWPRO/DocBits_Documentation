# Transformationsregeln

## Überblick

Transformationsregeln bereinigen oder schreiben extrahierte Daten **automatisch** um — ein Feld im Header, eine Spalte in einer Tabelle, ganze Tabellenzeilen oder ein Attribut des Dokuments — jedes Mal, wenn ein Dokument verarbeitet und jedes Mal, wenn es gespeichert wird. Sie ersetzen die kleinen Skripte, die viele Organisationen früher schrieben für „immer dieses Feld trimmen“, „diese Spalte standardmäßig auf 1 setzen“, „die Einheitencodes dieses Lieferanten abbilden“ oder „die Positionen dieses Lieferanten zu einer Gesamtzeile zusammenfassen“.

Eine Regel wird pro **Dokumenttyp** definiert und läuft bei jedem Dokument dieses Typs. Regeln laufen **vor** Validierung, Skripten und Bestellabgleich, sodass alles nachgelagerte bereits die transformierten Werte sieht.

## Zugriff

1. Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumenttypen**.
2. Öffnen Sie den Dokumenttyp und wählen Sie **Transformationsregeln**. Die Liste zeigt jede Regel des Typs mit ihrem Umfang, Ziel, Priorität und ob sie aktiv ist.
3. Klicken Sie auf **Neue Regel**, um den Regel-Editor zu öffnen, oder öffnen Sie eine bestehende Regel, um sie zu ändern.

## Aufbau einer Regel

| Teil                          | Was es ist                                                                                                                                                                                                                                                     |
| ----------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Name / Schlüssel**          | Der Anzeigename, der in Listen, Nachrichten und der Matching-Historie angezeigt wird, und ein technischer Schlüssel, der stabil bleibt, wenn Sie die Regel umbenennen.                                                                                         |
| **Umfang**                    | Wo die Regel schreibt: ein **Header-Feld**, eine **Tabellenspalte**, eine **Tabelle** (ganze Zeilen) oder ein **Dokumentenattribut**. Siehe unten.                                                                                                             |
| **Ziel**                      | Das Feld, die Spalte (mit ihrer Tabelle) oder die Tabelle, in die die Regel schreibt.                                                                                                                                                                          |
| **Quelle**                    | Optional. Woher die Regel ihre Eingabe liest, statt vom Ziel selbst: `header.<field>` für ein Header-Feld, `doc.<attribute>` für ein Dokumentattribut, `row.<column>` für eine andere Spalte derselben Zeile (nur Spaltenumfang).                              |
| **Wann**                      | **Immer** oder **nur wenn** eine Bedingung wahr ist (siehe Bedingungen).                                                                                                                                                                                       |
| **Aktionen**                  | Die Liste der Transformationen, die der Reihenfolge nach angewendet werden; die Ausgabe einer Aktion ist die Eingabe der nächsten.                                                                                                                             |
| **Priorität**                 | Regeln mit demselben Umfang laufen in aufsteigender Priorität (dann nach Schlüssel). Verwenden Sie sie, wenn eine Regel das Ergebnis einer anderen sehen muss.                                                                                                 |
| **Einmal ausführen**          | Die Regel wird auf ein Dokument **höchstens einmal** angewendet. Nötig für Aktionen, die den Wert bei jedem Speichern erneut ändern würden (Substring, Regex-Ersetzen, Regex-Extrahieren) und für Tabellenregeln, die die Zeilen nicht erneut aufbauen sollen. |
| **Ausführung protokollieren** | Schreibt pro Anwendung eine Protokollzeile — nützlich beim Feinjustieren einer neuen Regel.                                                                                                                                                                    |

### Umfänge

| Umfang                 | Schreibt in                                                       | Typische Regel                                                                                                      |
| ---------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| **Header-Feld**        | ein extrahiertes Header-Feld (Rechnungsnummer, Währung, …)        | trimmen und Großschreibung der Rechnungsnummer; „EUR€“ auf „EUR“ abbilden                                           |
| **Tabellenspalte**     | eine Spalte in jeder Zeile einer Tabelle                          | `UNIT_PRICE_PER` standardmäßig auf 1 setzen; das Präfix „Art.-Nr.“ aus der Artikelnummer entfernen                  |
| **Tabelle**            | die Zeilen einer Tabelle                                          | die Zeilen löschen und eine Gesamtzeile für einen Lieferanten hinzufügen, der auf den Gesamtbetrag abgeglichen wird |
| **Dokumentenattribut** | ein Attribut des Dokuments selbst (derzeit die Unterorganisation) | Dokumente eines Lieferanten an eine Unterorganisation weiterleiten                                                  |

Regeln laufen Umfang für Umfang in dieser Reihenfolge: Header → Dokument → Tabelle → Spalte. Eine Spaltenregel sieht daher bereits Zeilen, die eine Tabellenregel hinzugefügt hat.

### Bedingungen („nur wenn“)

Eine Bedingung vergleicht einen Wert des Dokuments mit einer Konstante. Der Wert stammt aus einem Header-Feld (`header.<field>`), einem Dokumentattribut (`doc.<attribute>`) oder bei Spaltenregeln aus einer Spalte der aktuellen Zeile (`row.<column>`).

| Operator                                       | Bedeutung             |
| ---------------------------------------------- | --------------------- |
| ist / ist nicht                                | exakter Vergleich     |
| ist eines von / ist keines von                 | Wert in einer Liste   |
| enthält, beginnt mit, endet mit                | Textvergleich         |
| ist leer / ist nicht leer                      | kein Wert benötigt    |
| größer als, kleiner als, mindestens, höchstens | numerischer Vergleich |
| entspricht                                     | regulärer Ausdruck    |

Bedingungen können mit **alle von** (und) und **eine von** (oder) gruppiert und mit **nicht** negiert werden. Beispiel: _nur wenn `header.supplier_id`_ _`20723` ist_ — die Regel läuft nur für einen Lieferanten.

### Aktionen

Aktionen für Header-Felder und Tabellenspalten (sie bilden eine Pipeline; der Wert geht oben rein und unten raus):

| Aktion          | Wirkung                                                                                                                                |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `trim`          | entfernt Leerzeichen (oder angegebene Zeichen) links, rechts oder beidseitig                                                           |
| `case`          | Groß-, Klein-, Titel- oder Kapitalisierung                                                                                             |
| `pad`           | füllt auf eine Länge mit einem Zeichen, links oder rechts                                                                              |
| `truncate`      | kürzt auf eine maximale Länge                                                                                                          |
| `affix`         | fügt ein Präfix oder Suffix hinzu oder entfernt eines                                                                                  |
| `sanitize`      | behält nur eine Zeichengruppe (alphanumerisch, alphabetisch, numerisch, alphanumerisch + Leerzeichen) oder entfernt eine Zeichengruppe |
| `substring`     | nimmt einen Teil des Werts anhand von Start und Länge oder Ende                                                                        |
| `regex_replace` | ersetzt, was ein regulärer Ausdruck findet                                                                                             |
| `regex_extract` | behält, was ein regulärer Ausdruck erfasst                                                                                             |
| `value_map`     | ordnet Werte anderen Werten zu (optional ohne Beachtung der Groß-/Kleinschreibung, mit Standardwert)                                   |
| `date_format`   | formatiert ein Datum neu (die Eingabe muss das ISO-Datum sein, das DocBits in `value` speichert)                                       |
| `number_format` | formatiert eine Zahl neu                                                                                                               |
| `default`       | setzt einen Wert nur, wenn das Feld leer ist                                                                                           |
| `set_value`     | setzt einen festen Wert, egal was im Feld stand                                                                                        |
| `clear`         | leert das Feld                                                                                                                         |

Aktionen für den **Tabellen**-Umfang (sie wirken auf Zeilen, nicht auf Werte, und können nicht mit den obigen Aktionen gemischt werden):

| Aktion       | Wirkung                                                                                                                                                                          |
| ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | löscht jede Zeile der Tabelle                                                                                                                                                    |
| `add_row`    | fügt eine Zeile am Ende oder Anfang hinzu; jede Spalte erhält entweder einen festen Wert oder einen Wert aus dem Header (`header.<field>`) oder dem Dokument (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` und `regex_extract` ändern einen Wert erneut, wenn sie auf einen bereits transformierten Wert angewendet werden. Kombinieren Sie sie mit **Einmal ausführen** oder schreiben Sie den regulären Ausdruck so, dass ein zweiter Lauf nichts mehr ändert.
{% endhint %}

## Wann Regeln laufen

* Während der Verarbeitung, nach der Extraktion und vor Validierung, Skripten und Bestellabgleich.
* Bei **jedem Speichern** des Dokuments, in dem sich die extrahierten Daten geändert haben. Regeln ohne **Einmal ausführen** werden bei jedem Speichern erneut angewendet; da jede Aktion außer den drei oben genannten idempotent ist, bleibt ein Wert, der bereits in der Zielform vorliegt, unverändert.

## Transformationsregeln und Bestellabgleich

Tabellen- und Spaltenregeln ändern, was der PO-Matcher sieht:

* Eine Tabellenregel, die Zeilen **neu aufbaut** (z. B. alle Zeilen löscht und eine Gesamtzeile hinzufügt), behält eine bestehende Bestellübereinstimmung, solange sie **die gleichen Zeilen wieder erzeugt** — Werte werden inhaltlich verglichen, sodass `1.0` und `1.00` dieselbe Zeile sind. Die Zeilen behalten ihre Identität und die Übereinstimmung überlebt jedes Speichern.
* Wenn eine Regel **Zeilen ersetzt oder entfernt, die abgeglichen wurden**, kann die Übereinstimmung nicht beibehalten werden. Das Dokument vermerkt dann, welche Regel sie entfernt hat, der Bestellabgleich-Bildschirm zeigt dies als Grund an („_Die PO-Übereinstimmung konnte nicht gespeichert werden: die Transformationsregel „…“ hat die Tabelle neu aufgebaut_“) und Administratoren erhalten einen Link zur Regel. Die **Matching-Historie** des Dokuments zeigt einen _Transformationsregeln_-Schritt vor der ersten Matching-Stufe mit den ausgeführten Regeln.
* Die Anzahl der Zeilen nach den Regeln ist das, was die [Aktivierungsbedingungen](https://github.com/Fellow-Consulting-AG/docbits/tree/de/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) der Matching-Regeln zählen. Eine Regel, die eine Rechnung auf **eine** Zeile zusammenfasst, macht nur in Kombination mit einer Match-on-Total-Regel Sinn, die für Ein-Zeilen-Dokumente aktiv ist (`[[count(table_lines)]] >= 1`).

## Beispiele

**Rechnungsnummer bereinigen** — Header-Feld `invoice_id`, immer: `trim` → `case` upper.

**Preisgrundlage standardisieren** — Tabellenspalte `UNIT_PRICE_PER` der Positions-Tabelle, immer: `default` `1`.

**Einheitencodes eines Lieferanten abbilden** — Tabellenspalte `UNIT` der Positions-Tabelle, nur wenn `header.supplier_id` `10040` ist: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Eine Gesamtzeile für einen Lieferanten, der auf den Gesamtbetrag abgeglichen wird** — Tabellenumfang auf der Positions-Tabelle, nur wenn `header.supplier_id` `20723` ist: `clear_rows`, dann `add_row` mit `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Kombinieren Sie dies mit einer Match-on-Total-Regel, deren Aktivierungsbedingung ein Dokument mit einer Zeile akzeptiert.

**Lieferanten an eine Unterorganisation weiterleiten** — Dokumentenattribut `sub_org_id`, nur wenn `header.supplier_id` eines von `[…]` ist: `set_value` `<Unterorganisations-ID>`.

## Fehlerbehebung

| Symptom                                                     | Was zu prüfen                                                                                                                                                                                                    |
| ----------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Die Regel hat nichts geändert                               | Ist sie aktiv? Passt der Dokumenttyp? Ist die Bedingung für dieses Dokument wahr (exakten Wert inklusive Leerzeichen vergleichen)? Wurde eine **Einmal ausführen**-Regel bereits auf das Dokument angewendet?    |
| Der Wert ändert sich bei jedem Speichern erneut             | Die Pipeline enthält `substring`, `regex_replace` oder `regex_extract`. Schalten Sie **Einmal ausführen** ein oder machen Sie den Ausdruck idempotent.                                                           |
| Die Bestellübereinstimmung geht nach dem Speichern verloren | Eine Tabellenregel hat die abgeglichenen Zeilen ersetzt. Der Grund im Dokument nennt die Regel; sorgen Sie dafür, dass die Regel die gleichen Zeilen reproduziert, oder setzen Sie sie auf **Einmal ausführen**. |
| Eine Matching-Regel läuft nach der Transformation nie       | Die Regel hat die Anzahl der Zeilen geändert; passen Sie die Aktivierungsbedingung der Matching-Regel an.                                                                                                        |

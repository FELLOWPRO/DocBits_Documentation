# Transformationsregeln

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/de.mp4" %}

## Überblick

Transformationsregeln bereinigen oder schreiben extrahierte Daten **automatisch** um, jedes Mal, wenn ein Dokument verarbeitet und jedes Mal, wenn es gespeichert wird. Eine Regel kann Folgendes ändern:

* ein **Kopffeld** (Rechnungsnummer, Währung, Steuernummer des Lieferanten …),
* eine **Spalte** in jeder Zeile einer Tabelle (Einheit, Artikelnummer, Preisbasis …),
* die **Zeilen** einer Tabelle (löschen, eine Zeile hinzufügen),
* ein **Attribut des Dokuments** — derzeit die Unterorganisation, zu der es gehört (**Routing**).

Jede Regel **liest** einen Wert, schickt ihn durch eine kurze **Pipeline** aus Schritten und **schreibt** das Ergebnis zurück. Regeln laufen **vor** Validierung, Skripten und Bestellabgleich, sodass alles Nachgelagerte bereits die korrigierten Werte sieht.

Transformationsregeln ersetzen die meisten der kleinen Skripte, die Organisationen früher für „dieses Feld immer trimmen“, „die Einheitencodes dieses Lieferanten abbilden“, „das Präfix hinzufügen, das unser ERP erwartet“ oder „die Positionen dieses Lieferanten zu einer Gesamtzeile zusammenfassen“ geschrieben haben — mit einem Formular, einer Live-Vorschau und ohne Code.

### Welche Probleme sie lösen

| Anforderung | Regel |
| --- | --- |
| Ein Lieferant druckt die Rechnungsnummer ohne das Präfix `INV-`, das unser ERP erwartet | Kopffeld *Invoice Number*, nur für diesen Lieferanten: Trimmen → UPPERCASE → Affix: Präfix `INV-` hinzufügen |
| Lieferanten senden deutsche Einheitencodes (`STK`, `Std`), das ERP erwartet UN/ECE-Codes (`PCE`, `HUR`) | Tabellenspalte *UNIT*: Map values `STK → PCE`, `KG → KGM`, `Std → HUR` |
| Artikelnummern kommen mit einem Präfix wie `Art.-Nr. 4711` | Tabellenspalte *ITEM_NUMBER*: Affix: Präfix `Art.-Nr. ` entfernen |
| Steuernummern enthalten Leerzeichen und Punkte | Kopffeld *Supplier Tax ID*: Desinfektionsmittel (Sanitise), nur alphanumerische Zeichen behalten |
| Ein Lieferant wird auf den Gesamtbetrag abgeglichen, nicht auf Zeilen | Tabellenzeilen: Clear all rows → Add a row mit dem Nettobetrag |
| Alle Dokumente bestimmter Lieferanten gehören zu einer Unterorganisation | Routing: Unterorganisation setzen, wenn *Supplier ID is one of …* |
| Datumsangaben müssen in einem festen Format in ein Freitextfeld geschrieben werden | Kopffeld: Reformat date `%d.%m.%Y` |
| Die Bestellnummer steht im falschen Feld (zum Beispiel in *Invoice Number*) | Kopffeld *Purchase Order*: aus *Invoice Number* lesen, nur wenn *Purchase Order is empty* |
| Die Bestellnummer hat führende Nullen oder ein Präfix, das die Bestellung nicht hat | Kopffeld *Purchase Order*: Trimmen von `0` auf der linken Seite oder Affix: Präfix entfernen |
| Artikelnummern unterscheiden sich von den Bestellzeilen in Groß-/Kleinschreibung, Leerzeichen oder Präfixen | Tabellenspalte *ITEM_NUMBER*: Affix: Präfix entfernen → Desinfektionsmittel (Sanitise) → UPPERCASE |

{% hint style="info" %}
Solange sich die Funktion in der Beta befindet, erscheinen die unten beschriebenen Einstellungen nur, wenn die Einstellungsseite **Document Types** mit angehängtem `?beta=true` an die Adresse geöffnet wird.
{% endhint %}

## Transformationsregeln aktivieren

Transformationsregeln werden **pro Dokumenttyp** von einem **Organisationsadministrator** eingeschaltet.

1. Navigieren Sie zu **Einstellungen → Globale Einstellungen → Dokumenttypen**.
2. Klicken Sie auf das **Einstellungen**-Symbol (Zahnrad) auf der Karte des Dokumenttyps.
3. Öffnen Sie **Transformation Rules** und schalten Sie den Schalter ein. Klicken Sie auf **Manage transformation rules**, um die Liste zu öffnen.

<figure><img src="../../../../.gitbook/assets/doc-type-settings-rule-toggles.png" alt="Der Schalter Transformation Rules"><figcaption><p>Der Schalter Transformation Rules in den zusätzlichen Einstellungen eines Dokumenttyps</p></figcaption></figure>

Die Karte des Dokumenttyps zeigt nun einen Link **Transformation Rules** und einen Link **Logs** für die Ausführungsprotokolle.

## Die Regelliste

Die Liste zeigt alle Regeln des Dokumenttyps in der Reihenfolge, in der sie laufen, jeweils mit einer einzeiligen Zusammenfassung („When invoice_id is abcd, take invoice_id, make it UPPERCASE, and save it back.“), ihrem Umfang (**Kopffeld**, **Tabellenzeilen**, **Tabellenspalte**, **Routing**), der Anzahl der Schritte, ihrer Quelle und ob **Ausführung protokollieren** eingeschaltet ist. Filtern Sie nach Umfang und nach **Active / Inactive**, durchsuchen Sie die Liste und verwenden Sie das Menü **⋮**, um eine Regel zu duplizieren oder zu löschen.

Regeln stammen wie bei den Validierungsregeln aus drei Quellen: **System default**-Regeln, die mit DocBits ausgeliefert werden (klicken Sie auf **Customize**, um eine bearbeitbare Kopie zu erhalten), **Customized** Systemregeln (**Reset to Default** stellt das Original wieder her) und **Custom**-Regeln, die Sie selbst erstellt haben.

## Eine Regel erstellen

Klicken Sie auf **New rule**. Der Builder hat links drei Schritte und rechts eine **Live-Vorschau**. Oben fasst er die Regel in einem Satz zusammen, während Sie sie aufbauen.

<figure><img src="../../../../.gitbook/assets/transformation-rule-scope.png" alt="Schritt 1 des Transformationsregel-Builders"><figcaption><p>Schritt 1: Was die Regel ändert. Der Satz oben beschreibt die Regel in einfacher Sprache</p></figcaption></figure>

### Schritt 1 — Was und wo

**Was ändert diese Regel?** — der Umfang:

| Umfang | Ändert | Ziel | Läuft |
| --- | --- | --- | --- |
| **Kopffeld** | einen Wert pro Dokument | ein Kopffeld, z. B. *Invoice Number* | einmal pro Dokument |
| **Tabellenzeilen** | ganze Positionszeilen — löschen oder Zeilen hinzufügen | eine Tabelle, z. B. `INVOICE_TABLE` | einmal pro Dokument |
| **Tabellenspalte** | einen Wert in jeder Positionszeile | eine Tabelle und eine Spalte, z. B. `INVOICE_TABLE` / `UNIT` | einmal pro Zeile |
| **Routing** | ein Attribut des Dokuments — derzeit die Unterorganisation | *Unterorganisation* | einmal pro Dokument |

Geben Sie anschließend den **Regelnamen** ein (der **Regelschlüssel** wird daraus erzeugt), wählen Sie **Zielfeld** / **Name der Tabelle** / **Zielspalte** und optional eine **Beschreibung**. **Ausführung protokollieren** schreibt pro Anwendung einen Protokolleintrag — nützlich, solange Sie eine Regel feinjustieren.

### Schritt 2 — Wann sie läuft

* **Stets** — die Regel läuft bei jedem Dokument des Typs.
* **Nur wenn…** — die Regel läuft nur, wenn eine Bedingung wahr ist, zum Beispiel *Supplier ID is HP0000278*. Bei Regeln mit dem Umfang **Tabellenspalte** kann die Bedingung die Spalten der aktuellen Zeile verwenden und wird Zeile für Zeile geprüft. Alle Felder, Operatoren und Beispiele finden Sie unter [Regelbedingungen (Applies when)](rule-conditions-applies-when.md).

Zwei Optionen unter **Verarbeitungsoptionen** steuern, wie oft die Regel angewendet wird:

| Option | Wirkung |
| --- | --- |
| **Nur einmal pro Dokument ausführen** | Normalerweise laufen Regeln bei jedem Speichern erneut. Ist die Option eingeschaltet, wird die Regel **höchstens einmal** auf ein Dokument angewendet und ist damit für dieses Dokument abgeschlossen. Ein Durchlauf, bei dem die Bedingungen nicht zutreffen, zählt nicht, sodass die Regel bei einem späteren Speichern noch angewendet werden kann. Erforderlich für Schritte, die den Wert bei jedem Speichern erneut ändern würden (siehe [Idempotenz](#einmal-ausfuhren-und-idempotenz)) und für Tabellenregeln, die die Zeilen nicht erneut aufbauen sollen. |
| **Run after lookup population (before PO match)** | *(neuere Versionen)* Führt die Regel in einem zusätzlichen Durchlauf aus, nachdem die Lookup-Daten (zum Beispiel Lieferantenstammdaten) befüllt wurden und bevor der Bestellabgleich stattfindet. Verwenden Sie die Option, wenn die Regel einen Wert benötigt, den ein Lookup liefert. Die Regel läuft weiterhin auch in den üblichen Phasen; eine Regel mit „Nur einmal pro Dokument ausführen“ und dieser Option wartet auf diesen Durchlauf, statt direkt nach der Extraktion zu laufen. |

### Schritt 3 — Die Pipeline

<figure><img src="../../../../.gitbook/assets/transformation-rule-pipeline.png" alt="Die Pipeline mit drei Schritten und die Live-Vorschau"><figcaption><p>Read → Trim → Change case → Affix → Write, mit dem Wert nach jedem Schritt in der Live-Vorschau</p></figcaption></figure>

* **Read from** — **das Feld (oder die Spalte) selbst** oder **ein anderes Feld**. Wenn Sie aus einem anderen Feld lesen, können Sie ein Feld aus einem anderen befüllen, zum Beispiel die Bestellnummer aus einem Freitextfeld kopieren.
* **Steps** — der Wert durchläuft die Schritte **von oben nach unten**; die Ausgabe eines Schritts ist die Eingabe des nächsten. Fügen Sie Schritte mit **+ Add a step** hinzu, ordnen Sie sie mit den Pfeilen neu an und entfernen Sie sie mit **✕**. Jeder Schritt zeigt rechts den Zwischenwert des Beispiels an.
* **Write to** — das Ziel aus Schritt 1. DocBits schreibt den gespeicherten Wert und aktualisiert danach automatisch den Anzeigewert.

### Die Schritte

<figure><img src="../../../../.gitbook/assets/transformation-step-menu.png" alt="Das Schrittmenü"><figcaption><p>Alle Schritte, nach Zweck gruppiert</p></figcaption></figure>

| Schritt | Einstellungen | Beispiel Eingabe → Ausgabe |
| --- | --- | --- |
| **Fall ändern** (Change case) | UPPERCASE, lowercase, Title Case, Capitalise first | `inv-4711` → `INV-4711` |
| **Trimmen** (Trim) | Seite (beide, links, rechts); Zeichen (leer = Leerraum) | `  4711 ` → `4711`; mit Zeichen `0` und Seite links: `004711` → `4711` |
| **Pad** | Länge, Füllzeichen, Seite | Länge 10, `0`, links: `4711` → `0000004711` |
| **Truncate** | maximale Länge | 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` |
| **Affix** | Präfix hinzufügen, Suffix hinzufügen, Präfix entfernen, Suffix entfernen; Text | Präfix `INV-` hinzufügen: `4711` → `INV-4711`; Präfix `Art.-Nr. ` entfernen: `Art.-Nr. 4711` → `4711` |
| **Desinfektionsmittel** (Sanitise) | nur behalten (alphanumerisch, Buchstaben, Ziffern, alphanumerisch + Leerzeichen) oder angegebene Zeichen entfernen | alphanumerisch behalten: `DE 123.456.789` → `DE123456789` |
| **Take a slice** | Start, Länge oder Ende | Start 0, Länge 4: `2026-09-29` → `2026` |
| **Extract** | Muster, Erfassungsgruppe | Muster `PO[- ]?(\d+)`, Gruppe 1: `Order PO-45001234` → `45001234` |
| **Find & replace** | Muster, Ersetzen durch, Anzahl (0 = alle) | Muster `\s+`, ersetzen durch ` `: `ACME    GmbH` → `ACME GmbH` |
| **Map values** | Zuordnungen (von → nach), Wert ohne Treffer (leer = Eingabe behalten), Groß-/Kleinschreibung ignorieren | `STK → PCE`: `stk` → `PCE` |
| **Reformat date** | Ausgabemuster (`%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y`) | `%d.%m.%Y`: `2026-09-29` → `29.09.2026` |
| **Format number** | Locale (de_DE, en_US, en_GB, fr_FR), min. und max. Nachkommastellen | de_DE, 2 Nachkommastellen: `1234.5` → `1.234,50` |
| **Fix value** | der Wert | schreibt immer den Wert, egal was das Feld enthielt |
| **Clear** | – | leert das Feld |

Regeln mit dem Umfang **Tabellenzeilen** verwenden zwei andere Schritte, die auf Zeilen statt auf Werten arbeiten:

| Schritt | Wirkung |
| --- | --- |
| **Clear all rows** | löscht jede extrahierte Zeile. Zeilen, die ein späterer Schritt hinzufügt, bleiben erhalten. |
| **Add a row** | fügt eine Zeile **nach der letzten Zeile** oder **vor der ersten Zeile** hinzu. Wählen Sie für jede Spalte **Value** (ein fester Wert) oder **Field** (der Wert eines Kopffelds). Spalten, die Sie weglassen, bleiben leer. |

{% hint style="info" %}
**Reformat date** erwartet das Datum so, wie DocBits es intern speichert (`YYYY-MM-DD`). Wenden Sie es auf das Feld selbst an, nicht auf einen Text, der bereits ein formatiertes Datum enthält.
{% endhint %}

### Live-Vorschau

Die Live-Vorschau führt die Regel an einem Beispiel aus, während Sie sie aufbauen:

* **Beispieleingabe** — geben Sie einen Wert so ein, wie er aus dem Dokument käme. Bei Tabellenregeln geben Sie die Anzahl der extrahierten Zeilen (**Sample table**) und Werte für die Felder ein, die neue Zeilen lesen (**Row source values**).
* **Bedingungswerte** — geben Sie bei Regeln mit Bedingung die Werte der Bedingungsfelder ein. Die Vorschau zeigt **Bedingungen treffen zu — Regel wird ausgeführt** oder **Conditions do not match — rule is skipped**.
* Darunter sehen Sie den Wert nach **jedem Schritt** und das Endergebnis, das geschrieben würde („invoice_id → INV-230620-03A“ oder „unchanged“).

Während Sie die Vorschau verwenden, wird nichts gespeichert. Klicken Sie auf **Speichern**, um die Regel zu speichern.

## Beispiele

### Die Rechnungsnummer eines Lieferanten bereinigen

Kopffeld **Invoice Number** · nur wenn *Supplier ID is HP0000278* · Trimmen → Fall ändern UPPERCASE → Affix Präfix `INV-` hinzufügen.
Beispiel `  230620-03a ` → `INV-230620-03A`. Siehe den Screenshot der Pipeline oben.

### Einheitencodes abbilden

Tabellenspalte **INVOICE_TABLE / UNIT** · stets · Trimmen → Map values `STK → PCE`, `KG → KGM`, `Std → HUR`, **Ignore case when matching** eingeschaltet, Wert ohne Treffer leer (Eingabe behalten).

<figure><img src="../../../../.gitbook/assets/transformation-column-value-map.png" alt="Eine Tabellenspaltenregel mit Map values"><figcaption><p>Map values auf der Spalte UNIT: <code>stk</code> wird zu <code>PCE</code></p></figcaption></figure>

### Eine Gesamtzeile für einen Lieferanten, der auf den Gesamtbetrag abgeglichen wird

Tabellenzeilen **INVOICE_TABLE** · nur wenn *Supplier ID is HP0000278* · Clear all rows → Add a row mit `POSITION` = Wert `001`, `QUANTITY` = Wert `1`, `NET_AMOUNT` = Feld *Total Net Amount*.

<figure><img src="../../../../.gitbook/assets/transformation-add-row-columns.png" alt="Eine Regel für Tabellenzeilen: alle Zeilen löschen, dann eine Zeile hinzufügen"><figcaption><p>Drei extrahierte Zeilen werden durch eine Zeile mit dem Nettobetrag ersetzt</p></figcaption></figure>

Die Reihenfolge ist wichtig: **Clear all rows** muss **vor** **Add a row** stehen. Der Builder warnt Sie, wenn das nicht der Fall ist („Clear all rows runs after Add a row …“), und er warnt auch, wenn einem Schritt **Add a row** kein **Clear all rows** vorausgeht, weil die Regel dann bei jedem Speichern eine weitere Kopie der Zeile anhängen würde. Kombinieren Sie diese Regel mit einer Bestellabgleich-Regel „Match on total“, die für Ein-Zeilen-Dokumente aktiv ist.

### Die Bestellnummer aus dem Feld Rechnungsnummer befüllen

Kopffeld **Purchase Order** · nur wenn *Purchase Order is empty* · **Read from** *Invoice Number* → Trimmen → Fall ändern UPPERCASE.

<figure><img src="../../../../.gitbook/assets/transformation-po-from-invoice-number-de.png" alt="Der Regel-Builder für die Regel, die Purchase Order aus Invoice Number befüllt, mit der Live-Vorschau"><figcaption><p>Die Regel und ihre Live-Vorschau: <code>po-4711</code> wird in <code>purchase_order</code> zu <code>PO-4711</code>. Beispielregel auf einem Test-Dokumenttyp.</p></figcaption></figure>

Manche Lieferanten drucken die Bestellnummer dorthin, wo die Extraktion die Rechnungsnummer erwartet. Dann enthält **Invoice Number** die Bestellnummer und **Purchase Order** ist leer, sodass der Bestellabgleich nichts zum Abgleichen findet. Diese Regel kopiert den Wert hinüber, bevor der Abgleich beginnt. In einem Test auf einem Entwicklungssystem wechselte ein Dokument mit genau diesem Problem von *nicht abgeglichen* zu *vollständig abgeglichen* (2 von 2 Zeilen), als es mit der Regel gespeichert wurde. Die Regel läuft nur, solange **Purchase Order** leer ist, und überschreibt daher nie eine Nummer, die korrekt extrahiert wurde.

### Artikelnummern für den Bestellabgleich vergleichbar machen

Tabellenspalte **INVOICE_TABLE / ITEM_NUMBER** · stets · Affix: Präfix `Art.-Nr. ` entfernen → Desinfektionsmittel (Sanitise): alphanumerisch behalten → Fall ändern UPPERCASE.

<figure><img src="../../../../.gitbook/assets/transformation-item-number-compare-de.png" alt="Der Regel-Builder für die Artikelnummern-Regel mit der Live-Vorschau"><figcaption><p>Die Live-Vorschau zeigt jeden Schritt: <code>Art.-Nr. ab-12/3</code> wird zu <code>AB123</code></p></figcaption></figure>

Schreibt die Rechnung `Art.-Nr. ab-12/3` und die Bestellung hat `AB123`, stimmen die Zeilen nicht überein. Die Regel bringt den Rechnungswert in die Form der Bestellung. Prüfen Sie, welche Form Ihre Bestellungen verwenden, und passen Sie die Schritte an.

### Weitere Beispiele

| Ziel | Umfang | Bedingung | Schritte |
| --- | --- | --- | --- |
| Leerzeichen und Punkte aus der Steuernummer entfernen | Kopffeld *Supplier Tax ID* | stets | Desinfektionsmittel (Sanitise): alphanumerisch behalten |
| Das Artikelpräfix entfernen | Spalte *ITEM_NUMBER* | stets | Affix: Präfix `Art.-Nr. ` entfernen |
| 10-stellige Lieferantennummern | Kopffeld *Supplier ID* | stets | Trimmen → Pad Länge 10 mit `0`, links |
| Die Bestellnummer aus einem Referenztext herausziehen | Kopffeld *Purchase Order*, aus einem anderen Feld lesen | nur wenn *Purchase Order is empty* | Extract `PO[- ]?(\d+)`, Gruppe 1 |
| Für einen Lieferanten immer eine Währung verwenden | Kopffeld *Currency* | nur wenn *Supplier ID is 10040* | Fix value `CHF` |
| Einen falsch extrahierten Wert entfernen | Kopffeld *Discount Term* | nur wenn *Supplier ID is 20723* | Clear |
| Preisbasis pro Einheit | Spalte *UNIT_PRICE_PER* | nur wenn *row.UNIT_PRICE_PER is empty* | Fix value `1` |
| Lieferanten an eine Unterorganisation weiterleiten | Routing | *Supplier ID is one of* `10040, 10041` | eine feste Unterorganisation zuweisen |
| Führende Nullen aus der Bestellnummer entfernen | Kopffeld *Purchase Order* | stets | Trimmen: Zeichen `0`, Seite links |
| Nur die Ziffern der Bestellnummer behalten | Kopffeld *Purchase Order* | stets | Desinfektionsmittel (Sanitise): nur Ziffern behalten (`PO-45001234` → `45001234`) |
| Eine zu lange Bestellreferenz kürzen | Kopffeld *Purchase Order* | nur wenn *Supplier ID is 20723* | Truncate auf 10 Zeichen |
| Der Bestellnummer das Präfix hinzufügen, das Ihr ERP erwartet | Kopffeld *Purchase Order* | nur wenn *Supplier ID is 10040* | Affix: Präfix `4500` hinzufügen |
| Beträge so schreiben, wie Ihr ERP sie liest | Kopffeld *Total Amount* | stets | Format number, Locale `de_DE`, 2 Nachkommastellen |
| Leerzeichen in Artikelnummern entfernen | Spalte *ITEM_NUMBER* | stets | Desinfektionsmittel (Sanitise): die Zeichen ` ` (Leerzeichen) entfernen |
| Artikelnummern in Großbuchstaben schreiben | Spalte *ITEM_NUMBER* | stets | Fall ändern UPPERCASE |
| Bestellungen eines Werks an eine Unterorganisation senden | Routing | *Purchase Order starts with* `4500` | eine feste Unterorganisation zuweisen |

## Routing-Regeln (Unterorganisation)

Eine **Routing**-Regel ändert kein Feld. Sie setzt ein Attribut am Dokument, wenn ihre Bedingungen zutreffen — derzeit die **Unterorganisation**. Wählen Sie **Assign a fixed sub-organisation** und wählen Sie die Unterorganisation aus der Liste aus, oder wählen Sie **Map from a field**, um Werte eines extrahierten Felds Unterorganisationen zuzuordnen. Das Dokument gehört dann zu dieser Unterorganisation, mit ihren Benutzern, Berechtigungen und Einstellungen. Ein Wert, der keine gültige Unterorganisation ist, wird nie geschrieben.

## Wann Regeln laufen

* **Während der Verarbeitung**, nach der Extraktion und vor Stammdaten-Lookup, Validierung, Skripten und Bestellabgleich.
* Bei **jedem Speichern** des Dokuments, bei dem sich die extrahierten Daten geändert haben. Regeln ohne **Nur einmal pro Dokument ausführen** werden jedes Mal erneut angewendet.
* Innerhalb eines Durchlaufs laufen Regeln Umfang für Umfang in dieser Reihenfolge: **Kopffeld → Routing → Tabellenzeilen → Tabellenspalte**. Eine Spaltenregel gilt daher auch für Zeilen, die eine Tabellenregel gerade hinzugefügt hat. Innerhalb eines Umfangs laufen die Regeln nach Priorität, dann nach Schlüssel.

### Einmal ausführen und Idempotenz

Die meisten Schritte liefern dasselbe Ergebnis, wenn sie auf ihre eigene Ausgabe angewendet werden — einen getrimmten Wert erneut trimmen, `PCE` erneut abbilden, ein Präfix hinzufügen, das schon vorhanden ist. Diese Regeln können bei jedem Speichern gefahrlos laufen.

**Take a slice**, **Extract** und **Find & replace** sind anders: Auf ihr eigenes Ergebnis erneut angewendet, ändern sie es weiter (ein Ausschnitt nimmt die ersten vier Zeichen der ersten vier Zeichen …). DocBits lässt Sie daher keine Regel speichern, die diese Schritte auf ihr eigenes Zielfeld anwendet. Entweder:

* schalten Sie **Nur einmal pro Dokument ausführen** ein, oder
* lesen Sie aus einem anderen Feld (**Read from** → ein anderes Feld), damit die Eingabe unverändert bleibt.

## Transformationsregeln und Bestellabgleich

Regeln laufen **vor** dem Bestellabgleich, sodass sie genau das vorbereiten können, was der Matcher liest:

| Der Matcher liest | Eine Regel kann | Beispiel |
| --- | --- | --- |
| Die Bestellnummer im Kopf | sie aus einem anderen Feld kopieren, aus einem Text extrahieren, Präfixe und führende Nullen entfernen | [Die Bestellnummer aus dem Feld Rechnungsnummer befüllen](#die-bestellnummer-aus-dem-feld-rechnungsnummer-befullen) |
| Die Artikelnummern der Zeilen | Präfixe entfernen, Sonderzeichen entfernen, die Schreibweise vereinheitlichen | [Artikelnummern vergleichbar machen](#artikelnummern-fur-den-bestellabgleich-vergleichbar-machen) |
| Die Einheitencodes | die Codes des Lieferanten auf Ihre abbilden | [Einheitencodes abbilden](#einheitencodes-abbilden) |
| Die Anzahl der Zeilen | die Zeilen zu einer Gesamtzeile zusammenfassen | [Eine Gesamtzeile](#eine-gesamtzeile-fur-einen-lieferanten-der-auf-den-gesamtbetrag-abgeglichen-wird) |

Tabellen- und Spaltenregeln ändern, was der PO-Matcher sieht:

* Eine Tabellenregel, die Zeilen **neu aufbaut** (zum Beispiel alle Zeilen löscht und eine Gesamtzeile hinzufügt), behält eine bestehende Bestellübereinstimmung, solange sie **dieselben Zeilen wieder erzeugt** — Werte werden inhaltlich verglichen, sodass `1.0` und `1.00` dieselbe Zeile sind. Die Zeilen behalten ihre Identität und die Übereinstimmung übersteht jedes Speichern.
* Wenn eine Regel **Zeilen ersetzt oder entfernt, die abgeglichen waren**, kann die Übereinstimmung nicht beibehalten werden. Das Dokument vermerkt dann, welche Regel sie verworfen hat, der Bildschirm Bestellabgleich zeigt dies als Grund an („_The PO match could not be saved: the transformation rule "…" rebuilt the table_“) und Administratoren erhalten einen Link zur Regel. Die **Matching-Historie** des Dokuments zeigt vor der ersten Matching-Stufe einen Schritt _Transformation rules_ mit den ausgeführten Regeln.
* Die Anzahl der Zeilen nach den Regeln ist das, was die [Aktivierungsbedingungen](more-settings/purchase-order/purchase-order-matching-rules.md#aktivierungsbedingungen) der Matching-Regeln zählen. Eine Regel, die eine Rechnung auf **eine** Zeile zusammenfasst, ergibt nur zusammen mit einer Match-on-Total-Regel Sinn, die für Ein-Zeilen-Dokumente aktiv ist (`[[count(table_lines)]] >= 1`).

## Protokolle

Ist **Ausführung protokollieren** eingeschaltet, wird jede Anwendung der Regel unter **Document Types → (Dokumenttyp) → Logs** protokolliert, mit dem Ergebnis (angewendet, keine Änderung, übersprungen), dem Dokument und — bei übersprungenen Regeln — der Bedingungsspur, die erklärt, warum. Siehe [Die Bedingungsspur in den Protokollen lesen](rule-conditions-applies-when.md#die-bedingungsspur-in-den-protokollen-lesen).

## Best Practices

* **Ein Zweck pro Regel.** „Rechnungsnummer bereinigen“ und „Einheitencodes abbilden“ sind zwei Regeln, nicht eine.
* **Bauen Sie mit der Live-Vorschau**, mit echten Werten aus Dokumenten, auch mit ungewöhnlichen (Leerzeichen, Kleinschreibung, Präfixe).
* **Begrenzen Sie lieferantenspezifische Regeln mit einer Bedingung**, statt sie auf alles laufen zu lassen.
* **Bevorzugen Sie idempotente Schritte.** Verwenden Sie „Nur einmal pro Dokument ausführen“ nur dort, wo Sie es brauchen.
* **Beobachten Sie die Bestellübereinstimmung**, nachdem Sie Tabellenregeln hinzugefügt haben; prüfen Sie die Matching-Historie einiger Dokumente.
* **Schalten Sie „Ausführung protokollieren“ aus**, sobald die Regel funktioniert.

## Fehlerbehebung

| Symptom | Was zu prüfen ist |
| --- | --- |
| Die Regel hat nichts geändert | Ist sie aktiv, und ist die Funktion für den Dokumenttyp aktiviert? Ist die Bedingung für dieses Dokument wahr (exakter Wert, einschließlich Leerzeichen und Groß-/Kleinschreibung)? Wurde eine Regel mit **Nur einmal pro Dokument ausführen** bereits auf das Dokument angewendet? Prüfen Sie die Spur im Protokoll. |
| Der Wert ändert sich bei jedem Speichern erneut | Die Pipeline enthält Take a slice, Extract oder Find & replace. Schalten Sie **Nur einmal pro Dokument ausführen** ein oder lesen Sie aus einem anderen Feld. |
| Eine Tabelle erhält bei jedem Speichern eine weitere Zeile | Ein Schritt **Add a row** ohne vorheriges **Clear all rows**. Fügen Sie zuerst den Clear-Schritt hinzu oder schalten Sie „Nur einmal pro Dokument ausführen“ ein. |
| Die Bestellübereinstimmung geht nach dem Speichern verloren | Eine Tabellenregel hat die abgeglichenen Zeilen ersetzt. Der Grund im Dokument nennt die Regel; sorgen Sie dafür, dass die Regel dieselben Zeilen reproduziert, oder stellen Sie sie auf „Nur einmal pro Dokument ausführen“. |
| Eine Matching-Regel läuft nach der Transformation nie | Die Regel hat die Anzahl der Zeilen geändert; passen Sie die Aktivierungsbedingung der Matching-Regel an. |
| Die Regel braucht einen Wert aus den Lieferantenstammdaten, der aber noch leer ist | Schalten Sie **Run after lookup population (before PO match)** ein. |
| Ein Datum wird nicht neu formatiert | Reformat date erwartet `YYYY-MM-DD` als Eingabe. |

## Verwandte Themen

* [Regelbedingungen (Applies when)](rule-conditions-applies-when.md) — Bedingungen im Detail
* [Custom Validation Rules](custom-validation-rules.md) — die transformierten Werte prüfen
* [Layout Selection Rules](layout-manager/layout-selection-rules.md) — das Layout wählen, das ein Dokument verwendet
* [Regeln für die Übereinstimmung von Bestellungen](more-settings/purchase-order/purchase-order-matching-rules.md)

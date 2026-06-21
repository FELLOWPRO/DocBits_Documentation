# Schnellsuche

Die **Schnellsuche** ist der schnellste Weg, um Dokumente im Dashboard zu finden. Sie
geben ein, wonach Sie suchen — einen Namen, einen Status, einen Betrag, ein Datum — und die
Dokumentliste wird sofort gefiltert.

Dieser Leitfaden ist so aufgebaut, wie die Suche schrittweise zusammengesetzt wird:

1. **Standardfelder** — die Spalten, die jedes Dokument besitzt (Dokumentname, Status,
   Daten). Immer verfügbar.
2. **Volltextfelder** — extrahierte Inhalte (Lieferant, Bestellung, Rechnungs-
   nummer, Beträge, Positionen). Verfügbar, wenn die Volltextsuche aktiviert ist.
3. **Operatoren, Kurzformen & Rezepte** — die vollständige Referenz, sobald Sie
   sich sicher fühlen.

> Sie müssen sich nichts merken: Klicken Sie in die Suchleiste und wählen Sie ein Feld und
> einen Wert aus der Liste aus — die Schnellsuche erstellt die Abfrage für Sie. Die Beispiele unten
> zeigen außerdem die getippte Form, sodass Sie sie direkt kopieren können.

<figure><img src="../../../.gitbook/assets/quick_search_01_entry.png" alt="The Quick Search bar at the top of the Dashboard"><figcaption><p>Die Schnellsuchleiste oben im Dashboard.</p></figcaption></figure>

---

## So funktioniert die Suchleiste — Chips, Symbolleiste & Rohansicht

Bevor wir uns den Feldern selbst zuwenden, ist es hilfreich zu wissen, wie die Leiste aufgebaut ist.

### Bedingungen werden zu Chips

Sobald Sie eine Bedingung vervollständigt haben (ein Feld, einen Operator und einen Wert), verwandelt die Schnellsuche
sie in einen **Chip** — eine farbige Pille innerhalb der Leiste — und beginnt mit einem neuen. Ein
Chip zeigt das **Feld**, den **Operator** und den **Wert** sowie ein **×** zum
Entfernen an. Chips sind je nach Speicherort der Daten farblich gekennzeichnet:

| Chip-Farbe | Feldtyp |
|-------------|------------|
| **Blau** | Standardspalte (Dokumentname, Status, Daten) |
| **Orange** | Volltext-/extrahiertes Feld (Lieferant, Betrag, Rechnungsnummer) |
| **Lila** | Vektorsuche (semantisch) |
| **Grün** | OCR-Textsuche |

Klicken Sie auf einen Chip, um ihn zu bearbeiten (er klappt wieder zu Text auf); klicken Sie auf **×**, um ihn zu löschen.
Mehrere kombinierte Chips werden standardmäßig als **UND** gelesen.

### Die Symbolleiste

Am rechten Ende der Leiste:

- **ⓘ Hilfe** — öffnet die in der App integrierte Referenz **Dashboard-Suche — Felder & Syntax**,
  die jedes Feld, jeden Operator und jede Kurzform auflistet, die in Ihrem Workspace verfügbar sind.
- **Filter (Regler)** — ein Schnellbereich für die gängigen Filter Status / Benutzer / Neustart,
  mit **Filter zurücksetzen** und **Anwenden**.
- **Index-Ring** — ein kleiner Fortschrittsring, der anzeigt, wie viel Ihres Volltext-Index
  bereits aufgebaut ist (wird nur angezeigt, wenn die Volltextsuche aktiviert ist).

### Standard- vs. Rohansicht

Die Leiste zeigt Ihre Abfrage normalerweise als Chips an (**Standardansicht**). Wechseln Sie zur **Roh-
ansicht**, um die Abfrage als reinen Text anzuzeigen und zu bearbeiten (z. B.
`status=ready_for_validation AND supplier_name=Test`) — nützlich zum Kopieren,
Teilen oder direkten Eingeben einer langen Abfrage. Ihre Abfrage bleibt beim Wechsel erhalten und wird
gespeichert, wenn Sie das Dashboard neu laden.

---

## Teil 1 — Standardfelder

Standardfelder sind die eigenen Spalten des Dokuments. Sie sind **immer verfügbar**,
unabhängig davon, ob die Volltextsuche aktiviert ist oder nicht.

### Dokumente anhand des Namens finden

Die Suche nach dem Dokumentnamen ist die häufigste. Es gibt drei Möglichkeiten, ihn abzugleichen —
alle **ohne Berücksichtigung der Groß-/Kleinschreibung**:

#### `=` → beginnt mit

```
filename=invoice
```

Findet Dokumente, deren Name **mit** „invoice“ **beginnt**. Beim Abgleich wird die Groß-/Kleinschreibung ignoriert, sodass
all diese mit `filename=invoice` übereinstimmen:

```
Invoice.pdf   iNVoice.pdf   iNvoiCE.pdf   INVOICE.pdf
Invoice.xml   iNVoice.xml   iNvoiCE.edi   …
```

Es stimmt **nicht** mit `XYZ_Invoice.pdf` überein (dort steht „invoice“ in der Mitte — verwenden Sie
dafür `:`).

<figure><img src="../../../.gitbook/assets/quick_search_02_filename_starts.png" alt="filename=invoice matches only names that start with invoice, any case"><figcaption><p><code>filename=invoice</code> — nur Namen, die mit „invoice“ <strong>beginnen</strong>, in beliebiger Groß-/Kleinschreibung (<code>Invoice.pdf</code>, <code>iNVoice.pdf</code>, <code>INVOICE_2026.pdf</code> … alle stimmen überein). Vergleichen Sie mit <code>:</code> unten.</p></figcaption></figure>

#### `:` → enthält (an beliebiger Stelle)

```
filename:invoice
```

Verwenden Sie `:`, um das Wort **an beliebiger Stelle** im Namen abzugleichen — `2026_Invoice.pdf`,
`vietnam_einvoice_sample.xml`, `scan_invoice_copy.pdf`.

<figure><img src="../../../.gitbook/assets/quick_search_03_filename_contains.png" alt="filename:invoice matches the word anywhere in the name"><figcaption><p><code>filename:invoice</code> — gleicht das Wort an beliebiger Stelle im Dokumentnamen ab.</p></figcaption></figure>

#### `="…"` → beginnt *oder* endet mit

```
filename="invoice"
```

Anführungszeichen sorgen dafür, dass `=` Namen abgleicht, die mit dem Wert **beginnen oder enden** — praktisch für einen
vorangestellten Code oder eine Dateiendung.

> **Die drei in einer Zeile:** `=` → beginnt mit · `:` → enthält · `="…"` →
> beginnt oder endet mit. Alle ignorieren Groß-/Kleinschreibung. Sie können dies jederzeit über das
> **Hilfesymbol** in der Suchleiste zusammengefasst sehen (nächster Abschnitt).

### Dokumente anhand des Status finden

```
status=ready_for_validation
```

Der Status ist eine feste Liste, daher ist `=` ein **exakter** Abgleich, und die Leiste bietet eine Wert-
auswahl an, wenn Sie `status=` eingeben.

<figure><img src="../../../.gitbook/assets/quick_search_05_status.png" alt="Filtering by document status"><figcaption><p><code>status=ready_for_validation</code> — exakter Abgleich bei einem Feld mit fester Liste.</p></figcaption></figure>

### Dokumente anhand des Datums finden

```
created_on>2026-05-25
```

Verwenden Sie `>`, `<`, `>=`, `<=` für Datumsbereiche. Sie können auch **relative** Daten verwenden:
`today()`, `today()-7` (letzte 7 Tage), `today()+30` (nächste 30 Tage).

<figure><img src="../../../.gitbook/assets/quick_search_06_date.png" alt="Filtering by creation date"><figcaption><p><code>created_on&#62;2026-05-25</code> — Dokumente, die nach einem Datum erstellt wurden.</p></figcaption></figure>

### Dokumente anhand des Rechnungs-Untertyps finden

```
invoice_sub_type="Cost Invoice"
```

Der Rechnungs-Untertyp ist eine feste Liste (zum Beispiel **Cost Invoice** oder **Purchase
Invoice**), daher ist `=` ein **exakter** Abgleich, und die Leiste bietet eine Wertauswahl an, wenn
Sie `invoice_sub_type=` eingeben. Verwenden Sie `invoice_sub_type!="Cost Invoice"` für
alles außer diesem Untertyp.

---

## Teil 2 — Volltextfelder

Volltextfelder durchsuchen den **extrahierten Inhalt** Ihrer Dokumente — Lieferant,
Bestellung, Rechnungsnummer, Beträge, Positionen. Sie erscheinen in **Orange**
und sind verfügbar, wenn die **Volltextsuche** für Ihre Organisation aktiviert ist. Die
Abgleichsregeln sind genau dieselben wie für Standardtextfelder
(`=` beginnt mit, `:` enthält, `="…"` beginnt oder endet mit).

### Dokumente eines Lieferanten finden

```
supplier_name=Test
```

Beginnt-mit auf dem extrahierten Lieferantennamen. Verwenden Sie `supplier_name:fuji`, um an beliebiger Stelle
abzugleichen, oder `supplier_name:"Ruiz Foods"`, um einen Wert mit Leerzeichen in Anführungszeichen zu setzen.

<figure><img src="../../../.gitbook/assets/quick_search_09_supplier.png" alt="Searching by supplier name"><figcaption><p><code>supplier_name=Test</code> — der Lieferant jedes Ergebnisses beginnt mit „Test“.</p></figcaption></figure>

### Dokumente anhand der Bestellung finden

```
purchase_order=PO
```

Beginnt-mit auf der extrahierten Bestellnummer — ideal für ein Bestell-Präfix.

<figure><img src="../../../.gitbook/assets/quick_search_10_purchase_order.png" alt="Searching by purchase order"><figcaption><p><code>purchase_order=PO</code> — Dokumente, deren Bestellnummer mit „PO“ beginnt.</p></figcaption></figure>

### Dokumente anhand des Betrags finden

```
total_amount>5000
```

Verwenden Sie `>`, `<`, `>=`, `<=` oder `between 100 and 500` für eine Spanne.

<figure><img src="../../../.gitbook/assets/quick_search_07_amount.png" alt="Filtering by total amount"><figcaption><p><code>total_amount&#62;5000</code> — Rechnungen über 5.000.</p></figcaption></figure>

Für ein Fenster verwenden Sie `between`:

```
total_amount between 1000 and 5000
```

Dies ist die Kurzform für `total_amount>=1000 AND total_amount<=5000`.

<figure><img src="../../../.gitbook/assets/quick_search_14_between.png" alt="Amount window with between"><figcaption><p><code>total_amount between 1000 and 5000</code> — jedes Ergebnis liegt innerhalb des Fensters.</p></figcaption></figure>

### Finden, was fehlt

```
supplier_name=""
```

`=""` bedeutet „dieses Feld ist **nicht gesetzt**“; `supplier_name!=""` bedeutet „hat einen beliebigen
Lieferanten“.

<figure><img src="../../../.gitbook/assets/quick_search_12_empty.png" alt="Finding documents with no supplier"><figcaption><p><code>supplier_name=""</code> — Dokumente, die noch keinen Lieferanten haben.</p></figcaption></figure>

Dieselbe Prüfung auf Vorhandensein funktioniert bei jedem Feld — zum Beispiel bei Dokumenten, denen noch
ein AP-Zuordnungscode fehlt:

```
ap_assignment_code=""
```

<figure><img src="../../../.gitbook/assets/quick_search_15_ap_empty.png" alt="Documents missing an AP assignment code"><figcaption><p><code>ap_assignment_code=""</code> — Dokumente, die keinen AP-Zuordnungscode haben. Verwenden Sie <code>ap_assignment_code!=""</code> für diejenigen, die einen haben.</p></figcaption></figure>

---

## Smart-Filter — ein Klick

Oben im Dropdown-Menü der Schnellsuche (klicken Sie in die Suchleiste) finden Sie
**Smart-Filter**: fertige Suchen, die Sie mit einem einzigen Klick anwenden. Jeder davon
ist lediglich eine Kurzform für eine Abfrage, die Sie auch selbst eingeben könnten:

| Smart-Filter | Findet | Entspricht der Eingabe |
|--------------|-------|----------------|
| ⚠️ **Überfällig** | Über das Fälligkeitsdatum hinaus | `invoice_due_date<today()` |
| 🕐 **Bald fällig** | Innerhalb der nächsten 7 Tage | `invoice_due_date<=today()+7` |
| 👤 **Mir zugewiesen** | Elemente, die auf Ihre Aktion warten | `assigned_to=<you>` |
| 📅 **Heutiger Posteingang** | Heute importiert | `imported_on>=today()` |
| 📋 **Ausstehende Validierung** | Bereit zur Validierung | `status=ready_for_validation` |
| 🧾 **Elektronische Dokumente** | E-Rechnungen (XML, ZUGFeRD, EDI) | `is_edoc=true` |
| ✅ **Vollständiger Bestellabgleich** | Vollständig mit einer Bestellung abgeglichen | `po_match_status=full_matched` |
| ➗ **Teilweiser Bestellabgleich** | Teilweise mit einer Bestellung abgeglichen | `po_match_status=partial_matched` |
| 📉 **Unter-Bestellabgleich** | Menge oder Stückpreis unter der Bestellung | `po_match_status=under_matched` |

Die drei **Bestellabgleich**-Filter und die Volltextfelder erfordern, dass die Volltextsuche
für Ihre Organisation aktiviert ist.

<figure><img src="../../../.gitbook/assets/quick_search_11_smart_filters.png" alt="The Smart Filters dropdown panel"><figcaption><p>Die Smart-Filter oben im Dropdown-Menü der Schnellsuche — ein Klick wendet den Filter an (Überfällig, Bald fällig, Mir zugewiesen, Heutiger Posteingang, Ausstehende Validierung, Elektronische Dokumente, Vollständiger / Teilweiser / Unter-Bestellabgleich).</p></figcaption></figure>

---

## Ergebnisse gruppieren

Anstatt einer flachen Liste können Sie die Ergebnisse nach einem beliebigen Feld **gruppieren** — Lieferant,
Status, Dokumenttyp, Unterorganisation oder einem Datumsbereich. Fügen Sie eine Gruppierung über
die Suchleiste hinzu:

```
group by supplier_name
```

Die Liste zeigt dann einklappbare **Gruppenüberschriften**, jede mit dem Namen der Gruppe und
einer **Anzahl** (z. B. *Ruiz Foods (12)*). Klicken Sie auf eine Überschrift, um diese Gruppe ein- oder
auszuklappen. Bei Datumsfeldern können Sie nach **Tag, Woche oder Monat** gruppieren.

<figure><img src="../../../.gitbook/assets/quick_search_16_grouping.png" alt="Results grouped by supplier with collapsible headers"><figcaption><p><code>group by supplier_name</code> — die Ergebnisse werden zu einer einklappbaren Überschrift pro Lieferant zusammengefasst.</p></figcaption></figure>

Die Gruppierung lässt sich mit jedem Filter kombinieren — `status=ready_for_validation group by
supplier_name` gruppiert nur die übereinstimmenden Dokumente. Das Klicken in eine Gruppe
**zoomt hinein**: Es wendet den Wert dieser Gruppe als Filter an und führt Sie zurück zur
flachen Liste für diese Auswahl.

---

## Teil 3 — Operatoren, Verknüpfungen, Kurzformen

### Die integrierte Hilfe

Das **Hilfesymbol** in der Suchleiste öffnet eine vollständige Referenz aller Felder,
Operatoren und Kurzformen, die in Ihrem Workspace verfügbar sind — einschließlich der Angabe, welche Felder
Standard- bzw. Volltextfelder sind.

<figure><img src="../../../.gitbook/assets/quick_search_08_help_modal.png" alt="The in-app Dashboard Search help with all operators"><figcaption><p>Die integrierte Hilfe <strong>Dashboard-Suche — Felder &#38; Syntax</strong>, die jeden Operator und die Art des Wertabgleichs auflistet.</p></figcaption></figure>

### Wie `=` je nach Feldtyp abgleicht

Bei jedem Textabgleich wird die Groß-/Kleinschreibung ignoriert.

| Feldtyp | Beispiel | `=` bedeutet |
|------------|---------|-----------|
| Text (Name, Lieferant, Bestellung) | `filename=invoice` | **beginnt mit** |
| Text, an beliebiger Stelle | `filename:invoice` | **enthält** |
| Text, Beginn *oder* Ende | `filename="invoice"` | **beginnt oder endet mit** |
| Status / Typ / Bestellabgleich (feste Listen) | `status=finished` | **exakt** |
| Bezeichner (Rechnungsnummer, Lieferanten-ID) | `invoice_number=INV-100` | **exakt** |
| Zahl | `total_amount>5000` | Bereich (`> < >= <= between`) |
| Datum | `created_on>2026-01-01` | Bereich + `today()±N` |

### Operatoren

| Operator | Bedeutung |
|----------|---------|
| `=` | beginnt-mit (Text) / exakt (Liste, Zahl, Datum) |
| `:` | enthält (Text, an beliebiger Stelle) |
| `="…"` | beginnt-mit oder endet-mit (Text) |
| `!=` | das Gegenteil von `=` |
| `>` `<` `>=` `<=` | größer / kleiner als |
| `between … and …` | inklusiver Bereich |
| `field=""` / `field!=""` | ist leer / ist gesetzt |
| `today()`, `today()-7`, `today()+30` | relative Daten |

### Verknüpfungen

Kombinieren Sie Bedingungen mit **AND** (beide wahr), **OR** (eine von beiden), **NOT** und
Klammern `( … )` zur Gruppierung:

```
status=ready_for_validation AND supplier_name=Test
(status=error OR status=failed) AND created_on>today()-1
```

<figure><img src="../../../.gitbook/assets/quick_search_13_combined.png" alt="Combining conditions with AND"><figcaption><p><code>status=ready_for_validation AND supplier_name=Test</code> — zwei kombinierte Bedingungen.</p></figcaption></figure>

### Kurzformen

Kürzere Formulierungen für dieselben Abfragen — verwenden Sie, was sich besser liest:

| Kurzform | Entspricht | Beschreibung |
|----------|---------|-------------|
| `total_amount gt 5000` | `total_amount>5000` | Wort-Aliase für Vergleichsoperatoren (`gt`/`gte`/`lt`/`lte`/`eq`/`ne`) |
| `due_date > today` | `due_date>today()` | Bloßes `today` / `yesterday` / `tomorrow` |
| `imported_on this_week` | `imported_on>=today()-7 AND imported_on<=today()` | Relative Zeiträume (`this_week`, `last_week`, `this_month`, …) |
| `ap_assignment_code is empty` | `ap_assignment_code=""` | Ob ein Feld einen beliebigen Wert hat |
| `status:open` | `status=ready_for_validation` | Benutzerfreundliche Statusbezeichnung (`open`/`closed`/`failed`/`done`) |
| `total_amount not between 100, 200` | `total_amount<100 OR total_amount>200` | Wert außerhalb eines Fensters |
| `status in (finished, error)` | `status=finished OR status=error` | Beliebigen Wert aus einer Liste abgleichen |
| `not status=finished` | `status!=finished` | Beliebiges Prädikat negieren |
| `filename contains rechnung` | `filename:rechnung` | Zeichenketten-Abgleich (`contains`/`starts_with`/`ends_with`) |
| `total_amount > 5k` | `total_amount>5000` | Währungssuffix `k` (×1.000), `M` (×1.000.000) |
| `overdue` | `invoice_due_date<today() AND status!=finished` | Unbezahlte überfällige Rechnungen |
| `#INV-1234` | `invoice_id:INV-1234` | Präfix im Twitter-Stil für die Rechnungs-ID |
| `@User` | `assigned_to:User` | Präfix im Twitter-Stil für den Zugewiesenen |
| `$5000+` | `total_amount>=5000` | `$`-Präfix für Betragsschwellen |

---

## Teil 4 — Erweiterte Suchmodi

Über die Feldsuche hinaus durchsuchen drei Präfixmodi den Dokumentinhalt selbst.

### Vektorsuche (semantisch) — `vector:`

Gleicht nach **Bedeutung** ab, nicht nach exaktem Text — nützlich für „Dokumente über XYZ finden“.
Erfordert das Vektor-Modul; bezieht sich auf den Dokumentinhalt.

```
vector: invoices about office supplies
vector: shipping delays with Hamburg port
```

<figure><img src="../../../.gitbook/assets/quick_search_17_vector.png" alt="Semantic vector search results"><figcaption><p><code>vector: supplier invoice</code> — semantisch verwandte Dokumente, auch ohne diese exakten Wörter.</p></figcaption></figure>

### OCR-Textsuche — `ocr:`

Durchsucht den **Seitentext**, den die OCR-Engine extrahiert hat — nicht nur die
strukturierten Spalten. Nützlich, wenn der Wert, an den Sie sich erinnern, im Dokumenttext steht.

```
ocr: Versandkosten
ocr: "purchase order PO-12345"
ocr: Hamburg AND doc_type=INVOICE
ocr: IBAN
```

<figure><img src="../../../.gitbook/assets/quick_search_18_ocr.png" alt="OCR text search results"><figcaption><p><code>ocr: demo invoice</code> — gleicht Text ab, der irgendwo auf den Dokumentseiten gefunden wird.</p></figcaption></figure>

### Natürlichsprachliche (KI-)Suche — `ai:`

Beschreiben Sie in einfacher Sprache, was Sie suchen; die KI liest Ihre Formulierung und extrahiert
Filter (Lieferant, Daten, Beträge) in eine strukturierte Abfrage. Anders als die Vektorsuche
**erstellt sie eine Abfrage**, anstatt ähnliche Dokumente zu finden.

```
ai: invoices from Ruiz over 1000 last quarter
ai: overdue invoices waiting on approval
ai: shipping documents from Hamburg last month
```

<figure><img src="../../../.gitbook/assets/quick_search_19_ai.png" alt="Natural-language AI search results"><figcaption><p><code>ai: invoices over 1000 from this year</code> — die KI wandelt den Satz automatisch in Filter um.</p></figcaption></figure>

---

### Rezepte

| Sie möchten … | Geben Sie dies ein |
|-----------|-----------|
| Bereit zur Validierung, vollständig abgeglichen | `status=ready_for_validation AND po_match_status=full_matched` |
| Dieser Lieferant, diese Woche | `supplier_name=Test AND created_on>today()-7` |
| Überfällige Rechnungen mit hohem Wert | `total_amount>5000 AND invoice_due_date<today()` |
| Zwei Lieferanten gleichzeitig | `supplier_name=fuji OR supplier_name=acme` |
| Fehlerhafte Dokumente von heute | `(status=error OR status=failed) AND created_on>today()-1` |
| Elektronische Gutschriften | `is_edoc=true AND sub_doc_type=CREDIT_NOTE` |
| Nach Bestell-Präfix | `purchase_order=PO-2026` |

> Orangefarbene (Volltext-)Felder erfordern, dass die **Volltextsuche** für Ihre
> Organisation aktiviert ist. Ein wörtliches `%` oder `_` in einem Wert wird als normales Zeichen behandelt.

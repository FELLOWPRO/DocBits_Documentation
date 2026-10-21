# Bedingungskarten – Vollständiger Leitfaden

## Bedingungskarten – Vollständiger Leitfaden

Die Bedingungskarten auf dieser Seite gehören in die **Wenn**- und **Und**-Gruppe des Workflow-Builders – sie entscheiden, ob die Then-Aktionen ausgeführt werden:

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-de.png" alt="Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus."><figcaption><p>Nicht gespeichertes Beispiel mit Wenn-, Und- und Dann-Karten. Füllen Sie alle Platzhalter vor der Ausführung aus.</p></figcaption></figure>

**Umfasst:** 31 verbleibende Bedingungskarten

***

### 📌 Versionsinformationen

**Status:** Die meisten Bedingungskarten sind stabil mit Strukturen mit einer oder zwei Versionen. **Versionsmuster:** Die meisten folgen dem Muster v1 → v2 (mit i18n-Unterstützung). **Beispiel für mehrere Versionen:** CONDITION\_DECISION\_TREE\_DATA (v2-v3)

**Hinweis:** Einige Bedingungskarten für den PO-Vergleich haben mehrere Versionen. Verwenden Sie diese Anleitung für das aktuelle Verhalten und die untenstehenden Release-Notizen für veröffentlichte Änderungen.

📖 [Release-Notizen](../../../overview-and-basics/release-notes) | [PO-Matching-Anleitung](compare-with-purchase-order/po-matching-complete-guide.md)

***

## Dokumentstatus- und Statusbedingungen

### Karte: CONDITION\_DOC\_STATUS\_IS\_ISNOT / Dokumentenstatusprüfung

#### Zweck

Prüft, ob das Dokument einen bestimmten Status hat

#### Wann zu verwenden

* Vor der Genehmigung
* In einer bestimmten Workflow-Phase
* Statusbasiertes Routing

#### Dokumentstatustypen

```
- Upload: Being uploaded
- OCR: Being scanned
- Classification: Type detection
- Ready for Validation: Waiting for review
- Workflow: In process
- Pending Approval: Needs approval
- Pending Second Approval: Needs secondary approval
- Auto Accounting: Auto-booking
- Export: Being exported
- Error: Problem occurred
```

#### Wie es funktioniert

```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

#### Beispiel

```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

#### Parameter

```
Operator: IS / IS NOT
Status: [Select status]
```

***

### Karte: CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST

#### Zweck

Überprüft, ob der Status mit einem in einer Liste übereinstimmt

#### Wann zu verwenden

* Mehrere gültige Status
* ODER-Logik für Status

#### Beispiel

```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

***

### Karte: CONDITION\_DOC\_TYPE\_IS\_ISNOT / Dokumententypprüfung

#### Zweck

Überprüft, ob das Dokument einen bestimmten Typ hat

#### Dokumenttypen

```
- Invoice
- Credit Note
- Purchase Order
- Delivery Note
- ASN (Advanced Ship Notice)
- Receipt
- Return
- Custom Types
```

#### Wie es funktioniert

```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

#### Beispiel

```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

***

### Karte: CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST

#### Zweck

Überprüft, ob der Typ mit einem in der Liste übereinstimmt

#### Beispiel

```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

***

### Karte: CONDITION\_SUB\_ORG\_IS\_ISNOT / Unterorganisationsprüfung

#### Zweck

Überprüft, welche Organisation/Abteilung das Dokument besitzt

#### Organisationen

```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

#### Beispiel

```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

***

### Karte: CONDITION\_PURCHASE\_ORDER\_IMPORT / PO-Importprüfung

#### Zweck

Überprüft, ob die Bestellung neu importiert wurde oder vorhanden ist

#### Wie es funktioniert

```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

#### Wann zu verwenden

* Unterschiedliche Handhabung für neue Bestellungen
* Überspringen Sie die Validierung für bekannte Bestellungen
* Verfolgen Sie den ersten Besuch beim Lieferanten

***

## Bedingungen für den Zessionar

### Karte: CONDITION\_USER\_IS\_ISNOT / Benutzerprüfung

#### Zweck

Überprüft, ob das Dokument einem bestimmten Benutzer zugewiesen ist

#### Wie es funktioniert

```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

#### Beispiel

```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

***

### Karte: CONDITION\_USER\_IS\_ISNOT\_IN\_LIST

#### Zweck

Überprüft, ob es einem Benutzer in der Liste zugewiesen ist

#### Beispiel

```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

***

### Karte: CONDITION\_GROUP\_IS\_ISNOT / Gruppencheck

#### Zweck

Überprüft, ob es einer bestimmten Gruppe zugeordnet ist

#### Beispiel

```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

***

### Karte: CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST

#### Zweck

Überprüft, ob einer Gruppe in der Liste zugewiesen ist

#### Beispiel

```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

***

## Datums- und Uhrzeitbedingungen

### Karte: CONDITION\_TIME\_IS\_ISNOT\_BETWEEN / Datumsbereichsprüfung

#### Zweck

Prüft, ob das Datum zwischen zwei Datumsangaben liegt

#### Wie es funktioniert

```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

#### Berechnung

```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

#### Wann zu verwenden

* Prüfen Sie, ob im Geschäftsjahr
* Prüfen Sie, ob innerhalb der Frist
* Prüfen Sie, ob sich das Angebot im Aktionszeitraum befindet

#### Beispiel

```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

#### Parameter

```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

***

### Karte: CONDITION\_TODAY\_IS\_ISNOT / Today Check

#### Zweck

Überprüft, ob das heutige Datum den Kriterien entspricht

#### Wie es funktioniert

```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

#### Anwendungsfälle

```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

#### Beispiel

```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

***

### Karte: CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

#### Zweck

Überprüft, ob das Lieferdatum mit den genehmigten Lieferdaten im Kalender übereinstimmt

#### Wie es funktioniert

```
Delivery Date from Invoice: 2025-10-25
    ↓
Check Master Calendar: Is 2025-10-25 acceptable?
    ↓
(Master calendar has list of acceptable dates)
    ↓
YES: Date is acceptable
NO: Date not in approved list
```

#### Wann zu verwenden

* Überprüfen Sie, ob die Lieferung mit den vereinbarten Terminen übereinstimmt
* Prüfen Sie anhand des Feiertagskalenders
* Validieren Sie anhand der vertraglich vereinbarten Termine

#### Beispiel

```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

***

## Logische Bedingungen

### Karte: CONDITION\_DECISION\_TREE\_DATA / Entscheidungstabellenrückgaben

#### Zweck

Prüft, ob die Entscheidungstabelle Rückgabewerte hat

#### Wie es funktioniert

```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

#### Wann zu verwenden

* Bevor Sie die Ergebnisse der Entscheidungstabelle verwenden
* Als Torzustand
* Um zu prüfen, ob Routing verfügbar ist

#### Beispiel

```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

***

### Karte: CONDITION\_CONTINUE\_CHANCE / Zufallswahrscheinlichkeit

#### Zweck

Wird mit der angegebenen Wahrscheinlichkeit fortgesetzt

#### Wie es funktioniert

```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

#### Wann zu verwenden

* A/B-Test-Workflows
* Bemusterungsunterlagen
* Stichprobenartige Qualitätsprüfungen

#### Beispiel

```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

#### Berechnung

```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

***

### Karte: CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE / Funktionsprüfung

#### Zweck

Überprüft, ob ein bestimmtes Modul/eine bestimmte Funktion aktiviert ist

#### Module

```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

#### Wie es funktioniert

```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

#### Wann zu verwenden

* Funktionsabhängige Arbeitsabläufe
* Optionale Verarbeitung
* Überprüfen Sie, ob die lizenzierte Funktion aktiv ist

***

### Karte: CONDITION\_HTTPS\_REQUEST\_STATUS / Ergebnisprüfung anfordern

#### Zweck

Prüft, ob die HTTPS-Anfrage erfolgreich war

#### Statuscodes

```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

#### Wie es funktioniert

```
Send HTTPS request
    ↓
Receive response code
    ↓
Check: Was request successful (200)?
    ↓
YES: Continue with response data
NO: Error handling
```

#### Beispiel

```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

***

### Karte: CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT / Lieferantenstatusprüfung

#### Zweck

Überprüft den Status des Lieferanten im System

#### Lieferantenstatus

```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

#### Wie es funktioniert

```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

#### Beispiel

```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

***

### Karte: CONDITION\_SPECIFY\_SUPPLIER\_TYPE

#### Zweck

Gibt den Lieferantentyp an bzw. prüft ihn

#### Lieferantentypen

```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

#### Wie es funktioniert

```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

***

## Beispielhafte Entscheidungsabläufe

### Ablauf 1: Statusbasierte Verarbeitung

```
Document Arrives
    ↓
Check: Status = "Ready for Validation"?
    ↓
YES: Validate document
    ↓
Check: Status = "Pending Approval"?
    ↓
YES: Create approval task
    ↓
Check: Status = "Error"?
    ↓
YES: Escalate to manager
```

### Ablauf 2: Lieferantenbasierte Verarbeitung

```
Invoice Arrives
    ↓
Check: Supplier status ACTIVE?
    ↓
NO: Block and escalate
    ↓
YES: Check: Supplier is preferred?
    ↓
YES: Fast track approval
NO: Standard approval
```

### Ablauf 3: Betragsbasiert mit Datumsprüfung

```
Invoice Arrives
    ↓
Check: Amount > €10,000?
    ↓
YES: Check: Date within Oct (fiscal period)?
    ↓
YES: Assign to Finance Director
NO: Assign to Finance Manager
```

***

## Vergleich der Bedingungskarten

| Karte                                        | Prüfungen          | Operator      | Verwendung               |
| ------------------------------------------- | --------------- | ------------- | ----------------- |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT           | Document status | IST / IST NICHT   | Stage check       |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST | Status in list  | IN / NICHT IN   | Mehrere Status |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT             | Document type   | IST / IST NICHT   | Type filtering    |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST       | Type in list    | IN / NICHT IN   | Multiple types    |
| CONDITION\_SUB\_ORG\_IS\_ISNOT              | Organisation    | IST / IST NICHT   | Abteilungskontrolle  |
| CONDITION\_USER\_IS\_ISNOT                  | Zugewiesener Benutzer   | IST / IST NICHT   | User check        |
| CONDITION\_USER\_IS\_ISNOT\_IN\_LIST        | User in list    | IN / NICHT IN   | Mehrere Benutzer    |
| CONDITION\_GROUP\_IS\_ISNOT                 | Zugewiesene Gruppe  | IST / IST NICHT   | Group check       |
| CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST       | Group in list   | IN / NICHT IN   | Mehrere Gruppen   |
| CONDITION\_TIME\_IS\_ISNOT\_BETWEEN         | Date range      | ZWISCHEN       | Datumsfenster       |
| CONDITION\_TODAY\_IS\_ISNOT                 | Das heutige Datum    | IST / IST NICHT   | Heute überprüfen       |
| CONDITION\_DECISION\_TREE\_DATA             | DT kehrt zurück      | HAT/HAT NICHT | DT result check   |
| CONDITION\_CONTINUE\_CHANCE                 | Wahrscheinlichkeit     | CHANCE        | Random gate       |
| CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE        | Funktion aktiviert | IST / IST NICHT   | Funktionsprüfung     |
| CONDITION\_HTTPS\_REQUEST\_STATUS           | Request result  | STATUS        | Response check    |
| CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT      | Supplier status | IST / IST NICHT   | Supplier check    |

***

## Best Practices für Bedingungen

✅ **Do:**

* Verwenden Sie bestimmte Bedingungen
* Testlogik mit Beispielen
* Konditionen logisch bestellen
* Haben Sie einen Fallback für alle Pfade
* Komplexe Logik dokumentieren

❌ **Nicht:**

* Erstellen Sie zirkuläre Bedingungen (A wenn B, B wenn A)
* Machen Sie die Bedingungen zu komplex
* Vergessen Sie Randfälle
* Angenommen, das Feld hat immer einen Wert
* Schaffen Sie unmögliche Bedingungen

***

## Mehrere Bedingungen kombinieren

```
Condition 1: Type = Invoice?
    AND
Condition 2: Amount > €5000?
    AND
Condition 3: Supplier status = Active?
    ↓
ALL TRUE → Process
SOME FALSE → Stop
```

***

## Verwandte Karten

* **CONDITION\_DOC\_FIELD\_CONTAINS** – Prüfung des Feldinhalts
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - Feldvergleich
* **CONDITION\_CHECKBOX\_IS** – Kontrollkästchenprüfung

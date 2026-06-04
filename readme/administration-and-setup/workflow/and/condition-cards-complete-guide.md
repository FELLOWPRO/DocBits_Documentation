# Uslovne kartice - Kompletan vodič

**Pokriva:** 31 preostalu uslovnu karticu

---

Uslovne kartice na ovoj stranici idu u grupe **When** i **And** u Workflow Builder-u — one odlučuju da li će se Then akcije pokrenuti:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Uslovne kartice se dodaju u grupe <strong>When</strong> i <strong>And</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Status:** Većina uslovnih kartica je stabilna sa jednoverzijskim ili dvoverzijskim strukturama
**Obrazac verzija:** Većina prati obrazac v1 → v2 (dodavanje i18n podrške)
**Primer sa više verzija:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Napomena:** Neke uslovne kartice za poređenje PO imaju 4-5 verzija (videti PO Matching Guide za detalje)

📖 [Kompletna istorija verzija](../../../changelog/release.md) | [Baza podataka verzija kartica](../../../../DocFlow/docs/card_version.md) | [PO Matching Guide](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Uslovi stanja i statusa dokumenta

## Kartica: CONDITION_DOC_STATUS_IS_ISNOT / Provera statusa dokumenta

### Svrha
Proverava da li dokument ima određeni status

### Kada koristiti
- Pre odobravanja
- U određenoj fazi toka rada
- Rutiranje zasnovano na statusu

### Tipovi statusa dokumenta
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

### Kako funkcioniše
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Primer
```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

### Parametri
```
Operator: IS / IS NOT
Status: [Select status]
```

---

## Kartica: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Svrha
Proverava da li se status poklapa sa bilo kojim u listi

### Kada koristiti
- Više važećih statusa
- OR logika za status

### Primer
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Kartica: CONDITION_DOC_TYPE_IS_ISNOT / Provera tipa dokumenta

### Svrha
Proverava da li je dokument određenog tipa

### Tipovi dokumenata
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

### Kako funkcioniše
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Primer
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Kartica: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Svrha
Proverava da li se tip poklapa sa bilo kojim u listi

### Primer
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Kartica: CONDITION_SUB_ORG_IS_ISNOT / Provera pod-organizacije

### Svrha
Proverava koja organizacija/odeljenje poseduje dokument

### Organizacije
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Primer
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Kartica: CONDITION_PURCHASE_ORDER_IMPORT / Provera uvoza PO

### Svrha
Proverava da li je PO novouvezen ili postojeći

### Kako funkcioniše
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Kada koristiti
- Različito rukovanje za nove PO
- Preskakanje validacije za poznate PO
- Praćenje prvog viđenja dobavljača

---

# Uslovi osobe za dodeljivanje

## Kartica: CONDITION_USER_IS_ISNOT / Provera korisnika

### Svrha
Proverava da li je dokument dodeljen određenom korisniku

### Kako funkcioniše
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Primer
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Kartica: CONDITION_USER_IS_ISNOT_IN_LIST

### Svrha
Proverava da li je dodeljen bilo kom korisniku u listi

### Primer
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Kartica: CONDITION_GROUP_IS_ISNOT / Provera grupe

### Svrha
Proverava da li je dodeljen određenoj grupi

### Primer
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Kartica: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Svrha
Proverava da li je dodeljen bilo kojoj grupi u listi

### Primer
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Uslovi datuma i vremena

## Kartica: CONDITION_TIME_IS_ISNOT_BETWEEN / Provera opsega datuma

### Svrha
Proverava da li datum spada između dva datuma

### Kako funkcioniše
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Izračunavanje
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Kada koristiti
- Provera da li je u fiskalnom periodu
- Provera da li je unutar roka
- Provera da li je u promotivnom periodu

### Primer
```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

### Parametri
```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

---

## Kartica: CONDITION_TODAY_IS_ISNOT / Provera današnjeg dana

### Svrha
Proverava da li današnji datum ispunjava kriterijume

### Kako funkcioniše
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Slučajevi upotrebe
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Primer
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Kartica: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Svrha
Proverava da li se datum isporuke poklapa sa odobrenim datumima isporuke u kalendaru

### Kako funkcioniše
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

### Kada koristiti
- Verifikacija da se isporuka poklapa sa dogovorenim datumima
- Provera u odnosu na kalendar praznika
- Validacija u odnosu na ugovorene datume

### Primer
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Logički uslovi

## Kartica: CONDITION_DECISION_TREE_DATA / Povratne vrednosti tabele odlučivanja

### Svrha
Proverava da li tabela odlučivanja ima povratne vrednosti

### Kako funkcioniše
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Kada koristiti
- Pre korišćenja rezultata tabele odlučivanja
- Kao uslov kapije
- Za proveru da li je rutiranje dostupno

### Primer
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Kartica: CONDITION_CONTINUE_CHANCE / Slučajna verovatnoća

### Svrha
Nastavlja sa navedenom verovatnoćom

### Kako funkcioniše
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Kada koristiti
- A/B testiranje tokova rada
- Uzorkovanje dokumenata
- Slučajne provere kvaliteta

### Primer
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Izračunavanje
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Kartica: CONDITION_MODULE_IS_ISNOT_ACTIVE / Provera funkcije

### Svrha
Proverava da li je određeni modul/funkcija omogućen

### Moduli
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Kako funkcioniše
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Kada koristiti
- Tokovi rada zavisni od funkcije
- Opciona obrada
- Provera da li je licencirana funkcija aktivna

---

## Kartica: CONDITION_HTTPS_REQUEST_STATUS / Provera rezultata zahteva

### Svrha
Proverava da li je HTTPS zahtev bio uspešan

### Statusni kodovi
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Kako funkcioniše
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

### Primer
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Kartica: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Provera statusa dobavljača

### Svrha
Proverava status dobavljača u sistemu

### Statusi dobavljača
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Kako funkcioniše
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Primer
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Kartica: CONDITION_SPECIFY_SUPPLIER_TYPE

### Svrha
Navodi/proverava tip dobavljača

### Tipovi dobavljača
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Kako funkcioniše
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Primeri tokova odlučivanja

## Tok 1: Obrada zasnovana na statusu
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

## Tok 2: Obrada zasnovana na dobavljaču
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

## Tok 3: Zasnovano na iznosu sa proverom datuma
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

---

# Poređenje uslovnih kartica

| Kartica | Proverava | Operator | Upotreba |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Status dokumenta | IS / IS NOT | Provera faze |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Status u listi | IN / NOT IN | Više statusa |
| CONDITION_DOC_TYPE_IS_ISNOT | Tip dokumenta | IS / IS NOT | Filtriranje po tipu |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Tip u listi | IN / NOT IN | Više tipova |
| CONDITION_SUB_ORG_IS_ISNOT | Organizacija | IS / IS NOT | Provera odeljenja |
| CONDITION_USER_IS_ISNOT | Dodeljeni korisnik | IS / IS NOT | Provera korisnika |
| CONDITION_USER_IS_ISNOT_IN_LIST | Korisnik u listi | IN / NOT IN | Više korisnika |
| CONDITION_GROUP_IS_ISNOT | Dodeljena grupa | IS / IS NOT | Provera grupe |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Grupa u listi | IN / NOT IN | Više grupa |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Opseg datuma | BETWEEN | Vremenski prozor |
| CONDITION_TODAY_IS_ISNOT | Današnji datum | IS / IS NOT | Provera današnjeg dana |
| CONDITION_DECISION_TREE_DATA | Povratne vrednosti DT | HAS / HAS NOT | Provera rezultata DT |
| CONDITION_CONTINUE_CHANCE | Verovatnoća | CHANCE | Slučajna kapija |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Funkcija omogućena | IS / IS NOT | Provera funkcije |
| CONDITION_HTTPS_REQUEST_STATUS | Rezultat zahteva | STATUS | Provera odgovora |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Status dobavljača | IS / IS NOT | Provera dobavljača |

---

# Najbolje prakse za uslove

✅ **Radite:**
- Koristite specifične uslove
- Testirajte logiku sa uzorcima
- Logički poređajte uslove
- Imajte rezervnu opciju za sve putanje
- Dokumentujte složenu logiku

❌ **Ne radite:**
- Ne kreirajte kružne uslove (A ako B, B ako A)
- Ne pravite uslove previše složenim
- Ne zaboravljajte granične slučajeve
- Ne pretpostavljajte da polje uvek ima vrednost
- Ne kreirajte nemoguće uslove

---

# Kombinovanje više uslova

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

---

# Povezane kartice

- **CONDITION_DOC_FIELD_CONTAINS** - Provera sadržaja polja
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Poređenje polja
- **CONDITION_CHECKBOX_IS** - Provera polja za potvrdu

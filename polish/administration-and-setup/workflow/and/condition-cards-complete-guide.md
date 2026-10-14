# Condition Cards - Complete Guide

Karty warunków na tej stronie trafiają do grup **When** i **And** w Kreatorze przepływów — decydują, czy akcje Then zostaną wykonane:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Karty warunków dodaje się do grup <strong>When</strong> i <strong>And</strong> za pomocą <strong>Add Card</strong>.</p></figcaption></figure>

**Obejmuje:** 31 pozostałych kart warunków

---

## 📌 Informacje o wersji

**Status:** Większość kart warunków jest stabilna ze strukturami jedno- lub dwuwersyjnymi
**Wzorzec wersji:** Większość podąża za wzorcem v1 → v2 (dodanie obsługi i18n)
**Przykład wielowersyjny:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Uwaga:** Niektóre karty warunków porównania PO mają 4-5 wersji (szczegóły w przewodniku PO Matching)

📖 [Pełna historia wersji](../../../changelog/release.md) | [Baza danych wersji kart](../../../../DocFlow/docs/card_version.md) | [Przewodnik PO Matching](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Warunki stanu i statusu dokumentu

## Karta: CONDITION_DOC_STATUS_IS_ISNOT / Document Status Check

### Cel
Sprawdza, czy dokument ma określony status

### Kiedy używać
- Przed zatwierdzeniem
- Na określonym etapie przepływu pracy
- Routing oparty na statusie

### Typy statusu dokumentu
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

### Jak to działa
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Przykład
```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

### Parametry
```
Operator: IS / IS NOT
Status: [Select status]
```

---

## Karta: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Cel
Sprawdza, czy status pasuje do dowolnego z listy

### Kiedy używać
- Wiele prawidłowych statusów
- Logika OR dla statusu

### Przykład
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Karta: CONDITION_DOC_TYPE_IS_ISNOT / Document Type Check

### Cel
Sprawdza, czy dokument jest określonego typu

### Typy dokumentów
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

### Jak to działa
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Przykład
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Karta: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Cel
Sprawdza, czy typ pasuje do dowolnego z listy

### Przykład
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Karta: CONDITION_SUB_ORG_IS_ISNOT / Sub-Organization Check

### Cel
Sprawdza, która organizacja/dział jest właścicielem dokumentu

### Organizacje
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Przykład
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Karta: CONDITION_PURCHASE_ORDER_IMPORT / PO Import Check

### Cel
Sprawdza, czy PO jest nowo zaimportowane czy istniejące

### Jak to działa
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Kiedy używać
- Inna obsługa dla nowych PO
- Pomijanie walidacji dla znanych PO
- Śledzenie pierwszego kontaktu z dostawcą

---

# Warunki osoby przypisanej

## Karta: CONDITION_USER_IS_ISNOT / User Check

### Cel
Sprawdza, czy dokument jest przypisany do określonego użytkownika

### Jak to działa
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Przykład
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Karta: CONDITION_USER_IS_ISNOT_IN_LIST

### Cel
Sprawdza, czy przypisano do dowolnego użytkownika z listy

### Przykład
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Karta: CONDITION_GROUP_IS_ISNOT / Group Check

### Cel
Sprawdza, czy przypisano do określonej grupy

### Przykład
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Karta: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Cel
Sprawdza, czy przypisano do dowolnej grupy z listy

### Przykład
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Warunki daty i godziny

## Karta: CONDITION_TIME_IS_ISNOT_BETWEEN / Date Range Check

### Cel
Sprawdza, czy data mieści się między dwiema datami

### Jak to działa
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Obliczenie
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Kiedy używać
- Sprawdzenie, czy w okresie obrachunkowym
- Sprawdzenie, czy w terminie
- Sprawdzenie, czy w okresie promocyjnym

### Przykład
```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

### Parametry
```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

---

## Karta: CONDITION_TODAY_IS_ISNOT / Today Check

### Cel
Sprawdza, czy dzisiejsza data spełnia kryteria

### Jak to działa
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Przypadki użycia
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Przykład
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Karta: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Cel
Sprawdza, czy data dostawy odpowiada zatwierdzonym datom dostawy w kalendarzu

### Jak to działa
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

### Kiedy używać
- Weryfikacja, czy dostawa odpowiada uzgodnionym datom
- Sprawdzenie względem kalendarza świąt
- Walidacja względem dat zakontraktowanych

### Przykład
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Warunki logiczne

## Karta: CONDITION_DECISION_TREE_DATA / Decision Table Returns

### Cel
Sprawdza, czy tabela decyzyjna ma wartości zwracane

### Jak to działa
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Kiedy używać
- Przed użyciem wyników tabeli decyzyjnej
- Jako warunek bramkowy
- Aby sprawdzić, czy routing jest dostępny

### Przykład
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Karta: CONDITION_CONTINUE_CHANCE / Random Probability

### Cel
Kontynuuje z określonym prawdopodobieństwem

### Jak to działa
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Kiedy używać
- Przepływy pracy testów A/B
- Próbkowanie dokumentów
- Losowe kontrole jakości

### Przykład
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Obliczenie
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Karta: CONDITION_MODULE_IS_ISNOT_ACTIVE / Feature Check

### Cel
Sprawdza, czy określony moduł/funkcja jest włączona

### Moduły
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Jak to działa
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Kiedy używać
- Przepływy pracy zależne od funkcji
- Opcjonalne przetwarzanie
- Sprawdzenie, czy licencjonowana funkcja jest aktywna

---

## Karta: CONDITION_HTTPS_REQUEST_STATUS / Request Result Check

### Cel
Sprawdza, czy żądanie HTTPS powiodło się

### Kody statusu
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Jak to działa
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

### Przykład
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Karta: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Supplier Status Check

### Cel
Sprawdza status dostawcy w systemie

### Statusy dostawcy
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Jak to działa
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Przykład
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Karta: CONDITION_SPECIFY_SUPPLIER_TYPE

### Cel
Określa/sprawdza typ dostawcy

### Typy dostawcy
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Jak to działa
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Przykładowe przepływy decyzyjne

## Przepływ 1: Przetwarzanie oparte na statusie
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

## Przepływ 2: Przetwarzanie oparte na dostawcy
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

## Przepływ 3: Oparty na kwocie ze sprawdzeniem daty
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

# Porównanie kart warunków

| Karta | Sprawdza | Operator | Zastosowanie |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Status dokumentu | IS / IS NOT | Sprawdzenie etapu |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Status na liście | IN / NOT IN | Wiele statusów |
| CONDITION_DOC_TYPE_IS_ISNOT | Typ dokumentu | IS / IS NOT | Filtrowanie typu |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Typ na liście | IN / NOT IN | Wiele typów |
| CONDITION_SUB_ORG_IS_ISNOT | Organizacja | IS / IS NOT | Sprawdzenie działu |
| CONDITION_USER_IS_ISNOT | Przypisany użytkownik | IS / IS NOT | Sprawdzenie użytkownika |
| CONDITION_USER_IS_ISNOT_IN_LIST | Użytkownik na liście | IN / NOT IN | Wielu użytkowników |
| CONDITION_GROUP_IS_ISNOT | Przypisana grupa | IS / IS NOT | Sprawdzenie grupy |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Grupa na liście | IN / NOT IN | Wiele grup |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Zakres dat | BETWEEN | Okno czasowe |
| CONDITION_TODAY_IS_ISNOT | Dzisiejsza data | IS / IS NOT | Sprawdzenie dzisiaj |
| CONDITION_DECISION_TREE_DATA | Zwroty DT | HAS / HAS NOT | Sprawdzenie wyniku DT |
| CONDITION_CONTINUE_CHANCE | Prawdopodobieństwo | CHANCE | Bramka losowa |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Funkcja włączona | IS / IS NOT | Sprawdzenie funkcji |
| CONDITION_HTTPS_REQUEST_STATUS | Wynik żądania | STATUS | Sprawdzenie odpowiedzi |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Status dostawcy | IS / IS NOT | Sprawdzenie dostawcy |

---

# Najlepsze praktyki dla warunków

✅ **Rób:**
- Używaj konkretnych warunków
- Testuj logikę z próbkami
- Porządkuj warunki logicznie
- Miej rozwiązanie zapasowe dla wszystkich ścieżek
- Dokumentuj złożoną logikę

❌ **Nie rób:**
- Nie twórz warunków cyklicznych (A if B, B if A)
- Nie czyń warunków zbyt złożonymi
- Nie zapominaj o przypadkach brzegowych
- Nie zakładaj, że pole zawsze ma wartość
- Nie twórz niemożliwych warunków

---

# Łączenie wielu warunków

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

# Powiązane karty

- **CONDITION_DOC_FIELD_CONTAINS** - Sprawdzenie zawartości pola
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Porównanie pól
- **CONDITION_CHECKBOX_IS** - Sprawdzenie pola wyboru

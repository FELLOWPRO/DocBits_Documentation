# Kartice za dodeljivanje dokumenata i korisnike - Kompletan vodič

**Pokriva:** 13 kartica povezanih sa dodeljivanjem i korisnicima

---

Kartice na ovoj stranici idu u grupu **Then** u Workflow Builder-u — akcije koje se pokreću kada se When/And uslovi poklope:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder platno sa grupama kartica When, And i Then"><figcaption><p>Kartice za dodeljivanje i korisnike se dodaju u grupu <strong>Then</strong> preko <strong>Add Card</strong>.</p></figcaption></figure>

---

## 📌 Version Information

**Kartice sa više verzija:** DOC_USER_ASSIGN (v2 najnovija, v3 zastarela), DOC_GROUP_ASSIGN (v2 najnovija, v3 zastarela), OC_ASSIGN_DOC (v2)

**Važno:** v3 verzije su dodale podršku za stablo odlučivanja ali su sada zastarele
**Preporuka:** Koristite v2 i za DOC_USER_ASSIGN i za DOC_GROUP_ASSIGN

📖 [Kompletna istorija verzija](../../../changelog/release.md#-assignment--routing-cards) | [Baza podataka verzija kartica](../../../../DocFlow/docs/card_version.md)

---

# Osnovno dodeljivanje dokumenata

## Kartica: DOC_USER_ASSIGN / Dodeli dokument korisniku

### Svrha
Dodeljuje dokument određenoj osobi za njenu akciju

### Kada koristiti
- Dokument zahteva pregled određene osobe
- Predaja pojedinačnom članu tima
- Praćenje odgovornosti
- Dodeljivanje posla imenovanoj osobi

### Kako funkcioniše
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Primer
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parametri
```
User: [Select which person]
```

### Napomena
Dodeljivanje znači:
- Dokument se prikazuje kao „assigned to me" za tu osobu
- Ta osoba je odgovorna
- Drugi i dalje mogu videti dokument (ali ne kao dodeljen njima)
- Jedno dodeljivanje po dokumentu istovremeno

---

## Kartica: DOC_GROUP_ASSIGN / Dodeli dokument grupi

### Svrha
Dodeljuje dokument grupi (svi članovi ga vide kao dodeljen njima)

### Kada koristiti
- Dokument za tim, ne za pojedinca
- Više ljudi može da rukuje
- Deljena odgovornost
- Raspodela radnog opterećenja tima

### Kako funkcioniše
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Primer
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parametri
```
Group: [Select which group]
```

### Razlika
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Kartica: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Svrha
Dodeljuje dokument na osnovu logike tabele odlučivanja

### Kada koristiti
- Različiti dobavljači zahtevaju različite obrađivače
- Dodeljivanje na osnovu iznosa
- Složena logika rutiranja
- Više uslova za dodeljivanje

### Kako funkcioniše
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Primer: Dodeljivanje na osnovu iznosa
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Primer: Dodeljivanje na osnovu dobavljača
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parametri
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Kartica: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Svrha
Dodeljuje dokument sekvencijalno na osnovu tabele odlučivanja sa prioritetima

### Kada koristiti
- Više sekvencijalnih odobravanja
- Različite osobe na različitim nivoima
- Lanac odobravanja na osnovu iznosa
- Putanja eskalacije

### Kako funkcioniše
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Sistem prioriteta
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Primer: Višenivovsko odobravanje
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parametri
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Svrha
Dodeljuje dokument korisniku sa sekvencijalnim prioritetom

### Kada koristiti
- Dokument zahteva određenu osobu
- Jasna sekvencijalna obrada
- Jedno dodeljivanje sa redosledom

### Kako funkcioniše
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Primer
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Svrha
Dodeljuje dokument sekvencijalno grupama

### Kada koristiti
- Više odobravanja grupa
- Različita odeljenja u svakoj fazi
- Sekvencijalna obrada zasnovana na timu

### Kako funkcioniše
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Primer
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Svrha
Dodeljuje dokument određenoj grupi objekta

### Kada koristiti
- Dokument za određeno skladište/objekat
- Operacije zasnovane na objektu
- Obrada specifična za lokaciju

### Primer
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Svrha
Dodeljuje sekvencijalno kroz objekte

### Kada koristiti
- Obrada na više lokacija
- Pošiljka prolazi kroz objekte
- Tok rada zasnovan na lokaciji

### Primer
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Svrha
Dodeljuje dokument odeljenju nabavke

### Kada koristiti
- Rukovanje od strane tima za nabavku
- Posao povezan sa dobavljačem
- Povezano sa narudžbenicom

### Primer
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Kartica: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Svrha
Sekvencijalno dodeljivanje unutar nabavke

### Kada koristiti
- Višekoračni proces nabavke
- Lanac odobravanja u nabavci

### Primer
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Kartica: ACTION_CHANGE_DOC_SUBORG / Promeni pod-organizaciju dokumenta

### Svrha
Dodeljuje dokument drugoj pod-organizaciji

### Kada koristiti
- Izabrana pogrešna organizacija
- Potrebno premeštanje u ispravno odeljenje
- Reorganizacija

### Kako funkcioniše
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Primer
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Kartica: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Svrha
Menja pod-organizaciju na osnovu vrednosti polja dokumenta

### Kada koristiti
- Pod-organizacija sačuvana u polju
- Poklapanje lokacije dokumenta sa poljem
- Automatsko dodeljivanje organizacije

### Kako funkcioniše
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Primer
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Kartica: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Svrha
Dodeljuje dokument korisniku iz polja, sa rezervnom opcijom ako korisnik nije pronađen

### Kada koristiti
- Ime korisnika sačuvano u polju dokumenta
- Možda ne postoji u sistemu
- Potrebna rezerva ako korisnik nije dostupan

### Kako funkcioniše
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parametri
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Primer
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Kartica: ACTION_ASSIGN_USER_TO_SUPPLIER

### Svrha
Dodeljuje dokument korisniku koji upravlja tim dobavljačem

### Kada koristiti
- Korisnik povezan sa dobavljačem
- Menadžer naloga dobavljača
- Vlasnik odnosa sa dobavljačem

### Kako funkcioniše
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Stabla odlučivanja za dodeljivanje

## Primer tabele odlučivanja 1: Zasnovano na iznosu
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Primer tabele odlučivanja 2: Zasnovano na dobavljaču
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Primer tabele odlučivanja 3: Zasnovano na tipu dokumenta
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Primeri tokova rada za dodeljivanje

## Primer 1: Jednostavno rutiranje
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Primer 2: Sekvencijalno odobravanje
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Primer 3: Rutiranje zasnovano na iznosu
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Primer 4: Zasnovano na objektu
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Najbolje prakse za dodeljivanje

✅ **Radite:**
- Održavajte tabele odlučivanja jednostavnim
- Testirajte logiku rutiranja sa uzorcima
- Obezbedite da sve putanje vode nekuda
- Imajte rezervu za nedostajuće korisnike
- Dokumentujte odluke o rutiranju

❌ **Ne radite:**
- Ne kreirajte kružna dodeljivanja (A→B→A)
- Ne dodeljujte nepostojećim korisnicima (bez rezerve)
- Ne pravite rutiranje previše složenim
- Ne zaboravljajte da testirate rutiranje
- Ne dodeljujte nedostupnim osobama

---

# Rešavanje problema sa dodeljivanjem

## „Document not assigned"
**Uzrok:** Uslov nije ispunjen ili korisnik ne postoji

**Rešenje:**
- Proverite da li je uslov istinit
- Verifikujte da korisnik postoji u sistemu
- Proverite podešavanja rezerve
- Pregledajte logiku tabele odlučivanja

## „Wrong person assigned"
**Uzrok:** Tabela odlučivanja ili logika rutiranja nije ispravna

**Rešenje:**
- Testirajte tabelu odlučivanja
- Proverite uslove
- Verifikujte mapiranje korisnika
- Pregledajte vrednosti polja

## „Assignment seems to skip someone"
**Uzrok:** Sekvencijalni redosled nije ispravan

**Rešenje:**
- Proverite brojeve prioriteta
- Verifikujte da je redosled ispravan
- Testirajte sa uzorkom
- Pregledajte redosled tabele odlučivanja

---

# Poređenje kartica za dodeljivanje

| Kartica | Dodeljuje | Tip rutiranja | Slučaj upotrebe |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Pojedincu | Direktno | Jednostavno dodeljivanje |
| DOC_GROUP_ASSIGN | Grupi | Direktno | Dodeljivanje timu |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Rezultatu odluke | Uslovno | Složeno rutiranje |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Više (sekvencijalno) | Uslovno | Lanac odobravanja |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Korisniku (sekvencijalno) | Poređano | Sekvencijalni koraci korisnika |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Grupama (sekvencijalno) | Poređano | Sekvencijalni koraci grupa |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Grupi objekta | Direktno | Specifično za objekat |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Objektima (sekvencijalno) | Poređano | Više objekata |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Nabavci | Direktno | Tok rada nabavke |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Nabavci (sekvencijalno) | Poređano | Lanac odobravanja nabavke |
| ACTION_CHANGE_DOC_SUBORG | Pod-organizaciji | Direktno | Promena odeljenja |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Pod-organizaciji po polju | Uslovno | Dodeljivanje zasnovano na polju |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Polje/Rezerva | Uslovno | Dinamičko dodeljivanje korisnika |

---

# Povezane kartice

- **ACTION_CREATE_TASK_FOR_USER** - Dodeli zadatak istoj osobi
- **ACTION_SEND_EMAIL** - Obavesti dodeljenu osobu
- **CONDITION_USER_IS_ISNOT** - Proveri da li je dodeljena ispravna osoba
- **CONDITION_GROUP_IS_ISNOT** - Proveri da li je dodeljena ispravna grupa

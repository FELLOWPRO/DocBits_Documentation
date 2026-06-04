---
hidden: true
---

# Workflow Card Release & Version History

## Principi kontrole verzija

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 13.41.53.png" alt=""><figcaption>Workflow Version Control System</figcaption></figure>

### Version 8.5.2024 - Osnovne funkcije verzionisanja

DocBits Workflow Engine implementira robusnu kontrolu verzija za sve kartice radnog toka:

1. **Version Control**: Svaka kartica može imati više verzija, od kojih svaka predstavlja različit skup uslova ili akcija. Ovo vam omogućava da eksperimentišete ili dorađujete pravila bez uticaja na trenutno aktivni radni tok.
2. **Seamless Upgrades**: Kada treba da ažurirate pravilo ili uslov zbog promena u zahtevima za obradu dokumenata, možete kreirati novu verziju kartice. Ovaj pristup obezbeđuje da su sve izmene namerne i testirane pre nego što zamene trenutnu verziju. Smanjuje greške i potencijalne prekide u obradi dokumenata.
3. **Maintaining Consistency**: Zadržavanje originalne verzije kartice nepromenjene dok ne odlučite da je nadogradite obezbeđuje da tekući procesi ne budu pogođeni. Možete pokretati testove i validacije na novoj verziji bez uticaja na žive podatke ili radne tokove.
4. **Flexibility and Testing**: Više verzija omogućava testiranje različitih scenarija u kontrolisanom okruženju. Možete videti efekte novih pravila ili promena na vašem radnom toku za obradu dokumenata bez trajnih izmena. Kada budete zadovoljni rezultatima, možete izabrati da primenite novu verziju.

---

## Pregled verzionisanja kartica

### Statistika

| Metric | Value |
|--------|-------|
| **Cards with Multiple Versions** | 30+ |
| **Total Version Records** | 90+ |
| **Current Active Versions** | 81+ |
| **Deprecated Versions** | 9 |
| **Fully Disabled Cards** | 2 |
| **Latest Version (Max)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Opseg verzija
- **Minimum:** v1
- **Maximum:** v5
- **Average Versions per Card:** 3

---

## Detaljne promene verzija kartica

### 🔧 ACTION CARDS - Eksterna integracija i izvršavanje

#### 1. CALL_API
**Versions:** v1, v2 (Current: v2)

📖 **Vodič:** [Call External API Guide](../then/action/call-api-guide.md)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v1 | No | Active | Osnovni API poziv bez ključeva za prevod |
| v2 | Yes | ✅ Current | Dodat `trnsl_%call_api` za višejezičku podršku |

**Šta je promenjeno:** Dodata podrška za internacionalizaciju (i18n) sa ključevima za prevod. Funkcionalnost ostaje identična.

**Pre (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Posle (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Preporuka:** Koristite v2 za sve nove radne tokove (uključuje jezičku podršku)
**Backward Compatibility:** ✅ v1 i dalje radi

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versions:** v1, v2 (Current: v2)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v1 | No | Active | Jednostavan HTTP zahtev |
| v2 | Yes | ✅ Current | Dodati `trnsl_%send_https_request` ključevi za prevod |

**Šta je promenjeno:** Dodata podrška za prevod. Osnovna funkcionalnost webhook-a/zahteva nepromenjena.
**Preporuka:** Koristite v2 (višejezička podrška)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versions:** v2 (Current), v3, v4 (Deprecated & Disabled)

| Version | Translation | Status | Key Changes |
|---------|-------------|--------|-------------|
| v2 | Yes | Active | Originalna DocOperator implementacija |
| v3 | Yes | Active | Dodat parametar „Execute the prompt“ za dodatnu kontrolu |
| v4 | Yes | ❌ DEPRECATED & DISABLED | Uklonjen parametar „Execute“ (vraćeno) |

**Putanja evolucije:** v2 → v3 (dodat parametar) → v4 (vraćeno - ne preporučuje se)

**Šta je promenjeno:**
- v2 → v3: Dodat opcioni parametar za kontrolu izvršavanja radi veće fleksibilnosti
- v3 → v4: Uklonjen parametar nakon dalje analize (zastarelo)

**Preporuka:** Koristite v3 za nove radne tokove (najnovija aktivna verzija sa svim funkcijama)
**Migracija:** Ako koristite v4, pređite na v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versions:** v2, v3 (Deprecated), v4 (Current)

📖 **Vodič:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

| Version | Changes | Status | Type Parameter |
|---------|---------|--------|-----------------|
| v2 | Originalna implementacija | Active | "Task" (fiksno) |
| v3 | + Podrška za stablo odlučivanja | ❌ DEPRECATED | "Task" (fiksno) |
| v4 | - Stablo odlučivanja, + Generički tip | ✅ Current | Generički tip (fleksibilan) |

**Evolucija:** v2 → v3 (eksperiment sa stablom odlučivanja) → v4 (generički tipovi, stablo odlučivanja uklonjeno)

**v2 → v3 promena (eksperiment sa stablom odlučivanja):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 promena (generički tipovi + uklanjanje stabla odlučivanja):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Šta je promenjeno:**
- v2 → v3: Dodat parametar `decision tree, if available: [param]`
- v3 → v4:
  - ❌ Uklonjen parametar stabla odlučivanja
  - ✅ Promenjeno "Task" → generičko `[param]` (podržava Task, Ticket, Issue, itd.)
  - Dodat ključ za prevod `trnsl_%task_for_group_v4`

**Zašto:** Pristup sa stablom odlučivanja u v3 bio je eksperimentalan. v4 pruža bolju fleksibilnost sa generičkim tipovima radnih stavki.
**Preporuka:** Koristite v4 (trenutna, najfleksibilnija)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versions:** v2, v3 (Current)

| Version | Task Type | Status | Key Difference |
|---------|-----------|--------|-----------------|
| v2 | "task" (fiksno) | Active | Originalna verzija |
| v3 | Generički tip | ✅ Current | Promenjeno u fleksibilno `[param]` |

**Šta je promenjeno:** v2 → v3: "Create a new task" → "Create a new [param]" (podržava bilo koji tip radne stavke)
**Preporuka:** Koristite v3

---

#### 6. RUN_WORKFLOW
**Versions:** v1, v2 (Current)

**Šta je promenjeno:** v1 → v2: Dodati `trnsl_%run_workflow` ključevi za prevod
**Preporuka:** Koristite v2

---

### 📊 PO COMPARISON & VALIDATION CARDS

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (Najrazvijenija - 5 verzija)
**Versions:** v2, v3, v4, v5 (Current)

📖 **Vodič:** [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Version | Changes | Status | Tolerance | Comparison |
|---------|---------|--------|-----------|------------|
| v2 | Osnovno poređenje cena | Active | ❌ No | Osnovno |
| v3 | Isto kao v2 | Active | ❌ No | Osnovno |
| v4 | + Parametar režima poređenja | Active | ❌ No | ✅ Yes |
| v5 | + Parametri tolerancije | ✅ Current | ✅ Yes (iznos + jedinica) | ✅ Yes |

**Putanja evolucije:** v2 → v3 (bez promene) → v4 (režimi poređenja) → v5 (pragovi tolerancije)

**v2 → v3:** Bez funkcionalne promene (isti ključ za prevod)

**v3 → v4 promena (dodat režim poređenja):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**v4 → v5 promena (dodati parametri tolerancije):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Šta je promenjeno:**
- **v2 → v3:** Bez funkcionalne promene
- **v3 → v4:** Dodat `Compare as [param]` - Podrška za različite operatore poređenja
- **v4 → v5:** Dodati parametri tolerancije:
  - `with tolerance of [amount] [unit]`
  - Primer: "with tolerance of 2 %" ili "with tolerance of 100 EUR"
  - Podržava: %, EUR, $ i druge valute

**Slučajevi upotrebe:**
- v2/v3: Strogo podudaranje (samo tačne cene)
- v4: Različite metode poređenja
- v5: Fleksibilno prihvatanje odstupanja (npr. prihvatanje razlika u ceni od 2%) ✅ PREPORUČENO

**Preporuka:** Koristite v5 za savremene radne tokove PO podudaranja

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versions:** v1 (Deprecated), v2, v3, v4 (Current)

| Version | Changes | Status | Compare Feature |
|---------|---------|--------|-----------------|
| v1 | Bez prevoda, bez metode | ❌ DEPRECATED | Osnovno |
| v2 | + Ključevi za prevod, + metoda | Active | Osnovna metoda |
| v3 | Isto kao v2 | Active | Osnovna metoda |
| v4 | + Parametri režima poređenja | ✅ Current | ✅ Fleksibilno |

**Šta je promenjeno:**
- **v1 → v2:** Dodat `trnsl_%in_order_confirmations_matches_purchase_order` + parametar metode poređenja
- **v2 → v3:** Bez promene
- **v3 → v4:** Dodat `Compare as [param1] [param2]` za fleksibilne režime poređenja

**Preporuka:** Koristite v4 (izbegavajte v1 koji je zastareo)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versions:** v2, v3 (Current)

| Version | Tolerance Days | Accepted Tolerance Days | Status |
|---------|-----------------|------------------------|--------|
| v2 | ❌ No | ❌ No | Active |
| v3 | ✅ Yes | ✅ Yes | ✅ Current |

**Šta je promenjeno:** v2 → v3: Dodati parametri tolerancije:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Primer:** Prihvatanje datuma isporuke u roku od 5 dana od obećanog datuma
**Preporuka:** Koristite v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versions:** v2, v3, v4 (Current)

| Version | Comparison Mode | Status |
|---------|-----------------|--------|
| v2 | Osnovno | Active |
| v3 | Osnovno (bez promene) | Active |
| v4 | ✅ Fleksibilan izbor režima | ✅ Current |

**Šta je promenjeno:** v3 → v4: Dodat `compare [param]` za različite pristupe poređenju
**Preporuka:** Koristite v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versions:** v2, v3, v4 (Current)

| Version | Comparison Mode | Status |
|---------|-----------------|--------|
| v2 | Standardno | Active |
| v3 | Standardno (bez promene) | Active |
| v4 | ✅ Fleksibilno | ✅ Current |

**Šta je promenjeno:** v3 → v4: Dodat parametar `compare [param]`
**Preporuka:** Koristite v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versions:** v2, v3 (Current)

| Version | Delivery Type | Master Data Table | Status |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (fiksno) | Fiksna referenca | Active |
| v3 | [Konfigurabilan param] | Dinamičko [param] | ✅ Current |

**Šta je promenjeno:** v2 → v3:
- Promenjeno "Confirmed delivery" → `[param] delivery` (fleksibilan tip isporuke)
- Promenjena fiksna referenca tabele → `stored in [param]` (dinamički izbor tabele)

**Fleksibilnost:** v3 dozvoljava različite tipove datuma isporuke i tabele dobavljača
**Preporuka:** Koristite v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versions:** v2, v3 (Current)

| Version | Supplier Table Reference | Status |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (fiksno) | Active |
| v3 | [Dinamički param] | ✅ Current |

**Šta je promenjeno:** v2 → v3: Fiksna referenca tabele → `stored in [param]` (dozvoljava dinamički izbor tabele)
**Preporuka:** Koristite v3

---

### 👥 ASSIGNMENT & ROUTING CARDS

#### 1. DOC_USER_ASSIGN
**Versions:** v1, v2, v3 (Deprecated)

| Version | Translation | Decision Tree | Status |
|---------|-------------|---------------|--------|
| v1 | No | ❌ No | Active |
| v2 | Yes | ❌ No | ✅ Current |
| v3 | Yes | ✅ Yes | ❌ DEPRECATED |

**Evolucija:** v1 (bez i18n) → v2 (sa i18n) → v3 (+ eksperiment sa stablom odlučivanja, sada zastarelo)

**Šta je promenjeno:**
- v1 → v2: Dodati ključevi za prevod
- v2 → v3: Dodata podrška za stablo odlučivanja (eksperimentalno, zastarelo)

**Preporuka:** Koristite v2 (stabilno sa i18n podrškom)

---

#### 2. DOC_GROUP_ASSIGN
**Versions:** v2, v3 (Deprecated)

| Version | Decision Tree | Status |
|---------|---------------|--------|
| v2 | ❌ No | ✅ Current |
| v3 | ✅ Yes | ❌ DEPRECATED |

**Šta je promenjeno:** v2 → v3: Dodat `Use decision tree, if available [param]` (kasnije zastarelo)
**Preporuka:** Koristite v2

---

#### 3. OC_ASSIGN_DOC
**Versions:** v1, v2 (Current)

**Šta je promenjeno:** v1 → v2: Dodati `trnsl_%oc_assign_doc` ključevi za prevod
**Preporuka:** Koristite v2

---

### 📋 TASK MANAGEMENT CARDS

#### 1. tasks_create ⭐ (Najrazvijenija kartica zadataka - 4 verzije)
**Versions:** v1 (Deprecated), v2 (Deprecated), v3 (Deprecated), v4 (Current)

📖 **Vodič:** [Task Assignment Guide](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Version | Translation | Decision Tree | Work Item Type | Status |
|---------|-------------|---------------|-----------------|--------|
| v1 | No | No | "Task" (fiksno) | ❌ DEPRECATED |
| v2 | Yes | No | "Task" (fiksno) | ❌ DEPRECATED |
| v3 | Yes | Yes | "Task" (fiksno) | ❌ DEPRECATED |
| v4 | Yes | No | [Generički param] | ✅ Current |

**Vremenska linija evolucije:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**v1 → v2 promena (dodati ključevi za prevod):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**v2 → v3 promena (eksperiment sa stablom odlučivanja):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 promena (generički tipovi + uklanjanje stabla odlučivanja):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Šta je promenjeno:**
- **v1 → v2:** Dodati `trnsl_%tasks_create` ključevi za prevod
- **v2 → v3:**
  - Dodata podrška za stablo odlučivanja: `Use decision tree, if available: [param]`
  - Promenjeno "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Uklonjen parametar stabla odlučivanja
  - ✅ Promenjeno "Task" → generičko `[param]` (podržava Task, Ticket, Issue, itd.)
  - Ažuriran ključ za prevod na `trnsl_%tasks_create_v4`

**Napomena o stablu odlučivanja:** v3 je koristila stabla odlučivanja za dinamičko dodeljivanje zadataka. Ovaj pristup je bio eksperimentalan i zastareo u v4 u korist direktnog izbora tipa radne stavke zasnovanog na parametrima.

**Preporuka:** Koristite isključivo v4 za nove radne tokove
**Migracija:** Ako koristite v1, v2 ili v3, nadogradite na v4 ✅

---

#### 2. OC_TASK
**Versions:** v1, v2 (Current)

**Šta je promenjeno:** v1 → v2: Dodati `trnsl_%oc_task` ključevi za prevod
**Preporuka:** Koristite v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versions:** v1, v3 (Current - v2 Skipped)

| Version | Work Item Type | Status |
|---------|-----------------|--------|
| v1 | "Task" (fiksno) | Active |
| v3 | [Generički param] | ✅ Current |

**Šta je promenjeno:** v1 → v3: Evolucija generičkog tipa (v2 je preskočena u produkciji)
**Preporuka:** Koristite v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versions:** v2, v3 (Current)

| Version | Assignment Text | Status |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Active |
| v3 | "Assign [generic] with title" | ✅ Current |

**Šta je promenjeno:** v2 → v3:
- Promenjeno "Assign task" → "Assign [generic param]"
- Promenjeno "return of decision" → "return of decision table" (jasnija terminologija)

**Preporuka:** Koristite v3

---

### 🔄 DOCUMENT CONTROL CARDS

#### APPROVE
**Versions:** v1, v2 (Current)
**Promena:** Dodati `trnsl_%approve_doc` ključevi za prevod
**Preporuka:** Koristite v2

---

#### REJECT
**Versions:** v1, v2 (Current)
**Promena:** Dodati `trnsl_%reject_doc` ključevi za prevod
**Preporuka:** Koristite v2

---

#### STAUS_CHANGE (Status Change)
**Versions:** v1, v2, v3 (Current)

| Version | Workflow Trigger | Status |
|---------|-----------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Yes | ✅ Current |

**Šta je promenjeno:** v2 → v3: Dodat `trigger Workflows [param]` - Automatsko pokretanje radnih tokova pri promeni statusa
**Preporuka:** Koristite v3

---

#### EXPORT
**Versions:** v1, v2, v3 (Current)

| Version | Validation | Status |
|---------|------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Yes | ✅ Current |

**Šta je promenjeno:** v2 → v3: Dodat `Start Export with Validation: [param]`
**Preporuka:** Koristite v3

---

### 🧮 DATA MANIPULATION CARDS

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Obrazac:** v1 → v2 (dodati ključevi za prevod)
**Preporuka:** Koristite v2 za sve

---

#### CONDITION_DECISION_TREE_DATA
**Versions:** v2, v3 (Current)

| Version | Data Usage | Status |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Active |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Current |

**Šta je promenjeno:** v2 → v3: Eksplicitnija kontrola nad ekstrakcijom podataka iz stabla odlučivanja
**Preporuka:** Koristite v3

---

### ❌ DISABLED CARDS (Ne koristiti)

#### DOC_SUBORG_CHANGE
**Versions:** v1, v2 (obe onemogućene)
**Status:** Više nije podržano
**Alternativa:** Koristite funkcije dodeljivanja dokumenata

---

#### RUN_SCRIPT
**Versions:** v2, v3 (obe onemogućene)
**Status:** Zamenjeno sa ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternativa:** Koristite ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Uobičajeni obrasci verzija

### Obrazac 1: Usvajanje ključeva za prevod (v1 → v2)
**Pogođeno:** 15+ kartica

**Promena:** Dodati `trnsl_%[card_name]` ključevi za prevod
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Kartice:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS i druge
**Uticaj:** Omogućava višejezičku podršku

---

### Obrazac 2: Integracija stabla odlučivanja (v2 → v3) - ZASTARELO
**Pogođeno:** 5 kartica (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Promena:** Dodat opcioni parametar stabla odlučivanja
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Status:** ❌ Uglavnom zastarelo (osim ACTION_DECISION_TREE_CREATE_TASKS)
**Razlog:** Prednost se daje jednostavnijem pristupu sa direktnim parametrom

---

### Obrazac 3: Evolucija generičkog tipa (v3 → v4)
**Pogođeno:** 4 kartice (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Promena:** "Task" → parametar generičkog tipa
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Uticaj:** Podržava Task, Ticket, Issue i druge tipove radnih stavki
**Korist:** Veća fleksibilnost i mogućnost ponovne upotrebe

---

### Obrazac 4: Parametri tolerancije (PO kartice)
**Pogođeno:** 6 kartica (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, itd.)

**Promena:** Dodata podrška za toleranciju/odstupanje
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Primeri:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Uticaj:** Realistični kriterijumi podudaranja (ne moraju se sve vrednosti tačno podudarati)

---

### Obrazac 5: Parametri režima poređenja
**Pogođeno:** 3 kartice (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Promena:** Dodat fleksibilan izbor metode poređenja
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Uticaj:** Podrška za različite algoritme poređenja

---

## ✅ Preporuke za verzije

### Za nove radne tokove
**Pravilo:** Uvek koristite najviši omogućeni broj verzije
- Pruža najnovije funkcije
- Najbolju podršku
- Najviše testirano
- Preporučeni pristup

### Za postojeće radne tokove
**Bezbedan pristup:**
- Nastavite da koristite trenutnu verziju ako radi
- Planirajte postepenu migraciju na novije verzije
- Prvo testirajte nadogradnje u sandbox-u

### Prioritet migracije

| Priority | Cards | Action |
|----------|-------|--------|
| **High** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Nadogradite na trenutnu verziju |
| **Medium** | Ostale v1/v2 nadogradnje prevoda, PO kartice v2/v3 | Razmotrite nadogradnju |
| **Low** | Kartice bez funkcionalnih promena | Opciono |

---

## ⚠️ Zastarele verzije - Ne koristiti

| Card | Version | Reason | Use Instead |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Veoma staro ili stablo odlučivanja zastarelo | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Pristup sa stablom odlučivanja zastareo | v4 |
| DOC_USER_ASSIGN | v3 | Pristup sa stablom odlučivanja zastareo | v2 |
| DOC_GROUP_ASSIGN | v3 | Pristup sa stablom odlučivanja zastareo | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Veoma staro | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Veoma staro | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funkcije vraćene | v3 |

---

## 🔄 Potpuno onemogućene kartice - Ne mogu se koristiti

| Card | Versions | Reason | Alternative |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Više nije podržano | Kartice za dodeljivanje dokumenata |
| RUN_SCRIPT | v2, v3 | Zamenjeno DocOperator-om | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Povezana dokumentacija

- 📖 [Card Versioning Reference](../changelog/card-versioning.md) - Detaljne informacije o verzijama
- 📚 [Workflow Guides](../) - Korak-po-korak upotreba kartica
- 🔄 [Card Version Database](../docs/card_version.md) - Kompletna istorija verzija
- 📋 [Workflow Logs](../workflow-logs/) - Izvršavanje i otklanjanje grešaka

---

**Last Updated:** October 23, 2025
**Status:** Complete Version History
**Database Source:** postgres-dev-docflow

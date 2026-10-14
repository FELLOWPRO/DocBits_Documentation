---
hidden: true
---

# Workflowkaart Release & Versiegeschiedenis

## Principes van versiebeheer

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>Versiebeheersysteem voor workflows</figcaption></figure>

### Versie 8.5.2024 - Kernfuncties voor versiebeheer

De DocBits Workflow Engine implementeert robuust versiebeheer voor alle workflowkaarten:

1. **Versiebeheer**: Elke kaart kan meerdere versies hebben, die elk een andere set voorwaarden of acties vertegenwoordigen. Hiermee kunt u experimenteren met of de regels aanpassen zonder de momenteel actieve workflow te beïnvloeden.
2. **Naadloze upgrades**: Wanneer u een regel of voorwaarde moet bijwerken vanwege wijzigingen in uw documentverwerkingsvereisten, kunt u een nieuwe versie van de kaart aanmaken. Deze aanpak zorgt ervoor dat eventuele wijzigingen weloverwogen en getest zijn voordat ze de huidige versie vervangen. Het minimaliseert fouten en mogelijke verstoringen in uw documentverwerking.
3. **Consistentie behouden**: Door de oorspronkelijke kaartversie ongewijzigd te houden totdat u besluit te upgraden, zorgt u ervoor dat lopende processen niet worden beïnvloed. U kunt tests en validaties op de nieuwe versie uitvoeren zonder live gegevens of workflows te beïnvloeden.
4. **Flexibiliteit en testen**: Meerdere versies maken het mogelijk om verschillende scenario's in een gecontroleerde omgeving te testen. U kunt de effecten van nieuwe regels of wijzigingen op uw documentverwerkingsworkflow zien zonder permanente wijzigingen aan te brengen. Zodra u tevreden bent met de resultaten, kunt u ervoor kiezen de nieuwe versie toe te passen.

---

## Overzicht van kaartversiebeheer

### Statistieken

| Metric | Waarde |
|--------|-------|
| **Kaarten met meerdere versies** | 30+ |
| **Totaal aantal versierecords** | 90+ |
| **Huidige actieve versies** | 81+ |
| **Verouderde versies** | 9 |
| **Volledig uitgeschakelde kaarten** | 2 |
| **Hoogste versie (Max)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Versiebereik
- **Minimum:** v1
- **Maximum:** v5
- **Gemiddeld aantal versies per kaart:** 3

---

## Gedetailleerde wijzigingen per kaartversie

### 🔧 ACTION CARDS - Externe integratie & uitvoering

#### 1. CALL_API
**Versies:** v1, v2 (Huidig: v2)

📖 **Gids:** [Externe API aanroepen-gids](../then/action/call-api-guide.md)

| Versie | Vertaling | Status | Belangrijkste wijzigingen |
|---------|-------------|--------|-------------|
| v1 | Nee | Actief | Basis-API-aanroep zonder vertaalsleutels |
| v2 | Ja | ✅ Huidig | `trnsl_%call_api` toegevoegd voor meertalige ondersteuning |

**Wat is gewijzigd:** Internationalisatie (i18n)-ondersteuning toegevoegd met vertaalsleutels. De functionaliteit blijft identiek.

**Voor (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Na (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Aanbeveling:** Gebruik v2 voor alle nieuwe workflows (inclusief taalondersteuning)
**Achterwaartse compatibiliteit:** ✅ v1 werkt nog steeds

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versies:** v1, v2 (Huidig: v2)

| Versie | Vertaling | Status | Belangrijkste wijzigingen |
|---------|-------------|--------|-------------|
| v1 | Nee | Actief | Eenvoudig HTTP-verzoek |
| v2 | Ja | ✅ Huidig | `trnsl_%send_https_request` vertaalsleutels toegevoegd |

**Wat is gewijzigd:** Vertaalondersteuning toegevoegd. De kernfunctionaliteit voor webhook/verzoek is ongewijzigd.
**Aanbeveling:** Gebruik v2 (meertalige ondersteuning)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versies:** v2 (Huidig), v3, v4 (Verouderd & uitgeschakeld)

| Versie | Vertaling | Status | Belangrijkste wijzigingen |
|---------|-------------|--------|-------------|
| v2 | Ja | Actief | Oorspronkelijke DocOperator-implementatie |
| v3 | Ja | Actief | Parameter "Execute the prompt" toegevoegd voor extra controle |
| v4 | Ja | ❌ VEROUDERD & UITGESCHAKELD | Parameter "Execute" verwijderd (teruggedraaid) |

**Evolutiepad:** v2 → v3 (parameter toegevoegd) → v4 (teruggedraaid - niet aanbevolen)

**Wat is gewijzigd:**
- v2 → v3: Optionele uitvoeringscontroleparameter toegevoegd voor meer flexibiliteit
- v3 → v4: De parameter verwijderd na verdere analyse (verouderd)

**Aanbeveling:** Gebruik v3 voor nieuwe workflows (nieuwste actieve versie met alle functies)
**Migratie:** Als u v4 gebruikt, schakel over naar v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versies:** v2, v3 (Verouderd), v4 (Huidig)

📖 **Gids:** [Taaktoewijzing-gids](../then/task/task-assignment-guide.md)

| Versie | Wijzigingen | Status | Type-parameter |
|---------|---------|--------|-----------------|
| v2 | Oorspronkelijke implementatie | Actief | "Task" (vast) |
| v3 | + Ondersteuning voor beslisboom | ❌ VEROUDERD | "Task" (vast) |
| v4 | - Beslisboom, + Generiek type | ✅ Huidig | Generiek type (flexibel) |

**Evolutie:** v2 → v3 (beslisboomexperiment) → v4 (generieke types, beslisboom verwijderd)

**Wijziging v2 → v3 (Beslisboomexperiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Wijziging v3 → v4 (Generieke types + verwijdering beslisboom):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Wat is gewijzigd:**
- v2 → v3: Parameter `decision tree, if available: [param]` toegevoegd
- v3 → v4:
  - ❌ Beslisboomparameter verwijderd
  - ✅ "Task" → generiek `[param]` (ondersteunt Task, Ticket, Issue, enz.)
  - Vertaalsleutel `trnsl_%task_for_group_v4` toegevoegd

**Waarom:** De beslisboomaanpak van v3 was experimenteel. v4 biedt betere flexibiliteit met generieke werkitemtypes.
**Aanbeveling:** Gebruik v4 (huidig, meest flexibel)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versies:** v2, v3 (Huidig)

| Versie | Taaktype | Status | Belangrijkste verschil |
|---------|-----------|--------|-----------------|
| v2 | "task" (vast) | Actief | Oorspronkelijke versie |
| v3 | Generiek type | ✅ Huidig | Gewijzigd naar flexibele `[param]` |

**Wat is gewijzigd:** v2 → v3: "Create a new task" → "Create a new [param]" (ondersteunt elk werkitemtype)
**Aanbeveling:** Gebruik v3

---

#### 6. RUN_WORKFLOW
**Versies:** v1, v2 (Huidig)

**Wat is gewijzigd:** v1 → v2: `trnsl_%run_workflow` vertaalsleutels toegevoegd
**Aanbeveling:** Gebruik v2

---

### 📊 PO-VERGELIJKINGS- & VALIDATIEKAARTEN

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (Meest geëvolueerd - 5 versies)
**Versies:** v2, v3, v4, v5 (Huidig)

📖 **Gids:** [Volledige gids voor PO-matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Versie | Wijzigingen | Status | Tolerantie | Vergelijking |
|---------|---------|--------|-----------|------------|
| v2 | Basis-prijsvergelijking | Actief | ❌ Nee | Basis |
| v3 | Gelijk aan v2 | Actief | ❌ Nee | Basis |
| v4 | + Vergelijkingsmodusparameter | Actief | ❌ Nee | ✅ Ja |
| v5 | + Tolerantieparameters | ✅ Huidig | ✅ Ja (bedrag + eenheid) | ✅ Ja |

**Evolutiepad:** v2 → v3 (geen wijziging) → v4 (vergelijkingsmodi) → v5 (tolerantiedrempels)

**v2 → v3:** Geen functionele wijziging (dezelfde vertaalsleutel)

**Wijziging v3 → v4 (Vergelijkingsmodus toegevoegd):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Wijziging v4 → v5 (Tolerantieparameters toegevoegd):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Wat is gewijzigd:**
- **v2 → v3:** Geen functionele wijziging
- **v3 → v4:** `Compare as [param]` toegevoegd - Ondersteuning voor verschillende vergelijkingsoperatoren
- **v4 → v5:** Tolerantieparameters toegevoegd:
  - `with tolerance of [amount] [unit]`
  - Voorbeeld: "with tolerance of 2 %" of "with tolerance of 100 EUR"
  - Ondersteunt: %, EUR, $ en andere valuta's

**Gebruiksscenario's:**
- v2/v3: Strikte matching (alleen exacte prijzen)
- v4: Verschillende vergelijkingsmethoden
- v5: Flexibele acceptatie van afwijkingen (bijv. accepteer prijsverschillen van 2%) ✅ AANBEVOLEN

**Aanbeveling:** Gebruik v5 voor moderne PO-matchingworkflows

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versies:** v1 (Verouderd), v2, v3, v4 (Huidig)

| Versie | Wijzigingen | Status | Vergelijkingsfunctie |
|---------|---------|--------|-----------------|
| v1 | Geen vertaling, geen methode | ❌ VEROUDERD | Basis |
| v2 | + Vertaalsleutels, + methode | Actief | Basismethode |
| v3 | Gelijk aan v2 | Actief | Basismethode |
| v4 | + Vergelijkingsmodusparameters | ✅ Huidig | ✅ Flexibel |

**Wat is gewijzigd:**
- **v1 → v2:** `trnsl_%in_order_confirmations_matches_purchase_order` + vergelijkingsmethodeparameter toegevoegd
- **v2 → v3:** Geen wijziging
- **v3 → v4:** `Compare as [param1] [param2]` toegevoegd voor flexibele vergelijkingsmodi

**Aanbeveling:** Gebruik v4 (vermijd v1, die verouderd is)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versies:** v2, v3 (Huidig)

| Versie | Tolerantiedagen | Geaccepteerde tolerantiedagen | Status |
|---------|-----------------|------------------------|--------|
| v2 | ❌ Nee | ❌ Nee | Actief |
| v3 | ✅ Ja | ✅ Ja | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3: Tolerantieparameters toegevoegd:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Voorbeeld:** Accepteer leverdata binnen 5 dagen van de beloofde datum
**Aanbeveling:** Gebruik v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versies:** v2, v3, v4 (Huidig)

| Versie | Vergelijkingsmodus | Status |
|---------|-----------------|--------|
| v2 | Basis | Actief |
| v3 | Basis (geen wijziging) | Actief |
| v4 | ✅ Flexibele moduskeuze | ✅ Huidig |

**Wat is gewijzigd:** v3 → v4: `compare [param]` toegevoegd voor verschillende vergelijkingsbenaderingen
**Aanbeveling:** Gebruik v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versies:** v2, v3, v4 (Huidig)

| Versie | Vergelijkingsmodus | Status |
|---------|-----------------|--------|
| v2 | Standaard | Actief |
| v3 | Standaard (geen wijziging) | Actief |
| v4 | ✅ Flexibel | ✅ Huidig |

**Wat is gewijzigd:** v3 → v4: Parameter `compare [param]` toegevoegd
**Aanbeveling:** Gebruik v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versies:** v2, v3 (Huidig)

| Versie | Levertype | Stamgegevenstabel | Status |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (vast) | Vaste referentie | Actief |
| v3 | [Configureerbare param] | Dynamische [param] | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3:
- "Confirmed delivery" → `[param] delivery` (flexibel levertype)
- Vaste tabelreferentie → `stored in [param]` (dynamische tabelselectie)

**Flexibiliteit:** v3 maakt verschillende leverdatumtypes en leverancierstabellen mogelijk
**Aanbeveling:** Gebruik v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versies:** v2, v3 (Huidig)

| Versie | Leverancierstabelreferentie | Status |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (vast) | Actief |
| v3 | [Dynamische param] | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3: Vaste tabelreferentie → `stored in [param]` (maakt dynamische tabelselectie mogelijk)
**Aanbeveling:** Gebruik v3

---

### 👥 TOEWIJZINGS- & ROUTERINGSKAARTEN

#### 1. DOC_USER_ASSIGN
**Versies:** v1, v2, v3 (Verouderd)

| Versie | Vertaling | Beslisboom | Status |
|---------|-------------|---------------|--------|
| v1 | Nee | ❌ Nee | Actief |
| v2 | Ja | ❌ Nee | ✅ Huidig |
| v3 | Ja | ✅ Ja | ❌ VEROUDERD |

**Evolutie:** v1 (geen i18n) → v2 (met i18n) → v3 (+ beslisboomexperiment, nu verouderd)

**Wat is gewijzigd:**
- v1 → v2: Vertaalsleutels toegevoegd
- v2 → v3: Ondersteuning voor beslisboom toegevoegd (experimenteel, verouderd)

**Aanbeveling:** Gebruik v2 (stabiel met i18n-ondersteuning)

---

#### 2. DOC_GROUP_ASSIGN
**Versies:** v2, v3 (Verouderd)

| Versie | Beslisboom | Status |
|---------|---------------|--------|
| v2 | ❌ Nee | ✅ Huidig |
| v3 | ✅ Ja | ❌ VEROUDERD |

**Wat is gewijzigd:** v2 → v3: `Use decision tree, if available [param]` toegevoegd (later verouderd)
**Aanbeveling:** Gebruik v2

---

#### 3. OC_ASSIGN_DOC
**Versies:** v1, v2 (Huidig)

**Wat is gewijzigd:** v1 → v2: `trnsl_%oc_assign_doc` vertaalsleutels toegevoegd
**Aanbeveling:** Gebruik v2

---

### 📋 TAAKBEHEERKAARTEN

#### 1. tasks_create ⭐ (Meest geëvolueerde taakkaart - 4 versies)
**Versies:** v1 (Verouderd), v2 (Verouderd), v3 (Verouderd), v4 (Huidig)

📖 **Gids:** [Taaktoewijzing-gids](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Versie | Vertaling | Beslisboom | Werkitemtype | Status |
|---------|-------------|---------------|-----------------|--------|
| v1 | Nee | Nee | "Task" (vast) | ❌ VEROUDERD |
| v2 | Ja | Nee | "Task" (vast) | ❌ VEROUDERD |
| v3 | Ja | Ja | "Task" (vast) | ❌ VEROUDERD |
| v4 | Ja | Nee | [Generieke param] | ✅ Huidig |

**Evolutietijdlijn:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Wijziging v1 → v2 (Vertaalsleutels toegevoegd):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Wijziging v2 → v3 (Beslisboomexperiment):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Wijziging v3 → v4 (Generieke types + verwijdering beslisboom):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Wat is gewijzigd:**
- **v1 → v2:** `trnsl_%tasks_create` vertaalsleutels toegevoegd
- **v2 → v3:**
  - Ondersteuning voor beslisboom toegevoegd: `Use decision tree, if available: [param]`
  - "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Beslisboomparameter verwijderd
  - ✅ "Task" → generiek `[param]` (ondersteunt Task, Ticket, Issue, enz.)
  - Vertaalsleutel bijgewerkt naar `trnsl_%tasks_create_v4`

**Opmerking over beslisboom:** v3 gebruikte beslisbomen om taken dynamisch toe te wijzen. Deze aanpak was experimenteel en is in v4 verouderd ten gunste van directe, op parameters gebaseerde selectie van het werkitemtype.

**Aanbeveling:** Gebruik uitsluitend v4 voor nieuwe workflows
**Migratie:** Als u v1, v2 of v3 gebruikt, upgrade naar v4 ✅

---

#### 2. OC_TASK
**Versies:** v1, v2 (Huidig)

**Wat is gewijzigd:** v1 → v2: `trnsl_%oc_task` vertaalsleutels toegevoegd
**Aanbeveling:** Gebruik v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versies:** v1, v3 (Huidig - v2 overgeslagen)

| Versie | Werkitemtype | Status |
|---------|-----------------|--------|
| v1 | "Task" (vast) | Actief |
| v3 | [Generieke param] | ✅ Huidig |

**Wat is gewijzigd:** v1 → v3: Generieke type-evolutie (v2 werd overgeslagen in productie)
**Aanbeveling:** Gebruik v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versies:** v2, v3 (Huidig)

| Versie | Toewijzingstekst | Status |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Actief |
| v3 | "Assign [generic] with title" | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3:
- "Assign task" → "Assign [generic param]"
- "return of decision" → "return of decision table" (duidelijkere terminologie)

**Aanbeveling:** Gebruik v3

---

### 🔄 DOCUMENTBEHEERKAARTEN

#### APPROVE
**Versies:** v1, v2 (Huidig)
**Wijziging:** `trnsl_%approve_doc` vertaalsleutels toegevoegd
**Aanbeveling:** Gebruik v2

---

#### REJECT
**Versies:** v1, v2 (Huidig)
**Wijziging:** `trnsl_%reject_doc` vertaalsleutels toegevoegd
**Aanbeveling:** Gebruik v2

---

#### STAUS_CHANGE (Status Change)
**Versies:** v1, v2, v3 (Huidig)

| Versie | Workflowtrigger | Status |
|---------|-----------------|--------|
| v1 | ❌ Nee | Actief |
| v2 | ❌ Nee | Actief |
| v3 | ✅ Ja | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3: `trigger Workflows [param]` toegevoegd - Workflows automatisch activeren bij statuswijziging
**Aanbeveling:** Gebruik v3

---

#### EXPORT
**Versies:** v1, v2, v3 (Huidig)

| Versie | Validatie | Status |
|---------|------------|--------|
| v1 | ❌ Nee | Actief |
| v2 | ❌ Nee | Actief |
| v3 | ✅ Ja | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3: `Start Export with Validation: [param]` toegevoegd
**Aanbeveling:** Gebruik v3

---

### 🧮 GEGEVENSMANIPULATIEKAARTEN

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Patroon:** v1 → v2 (vertaalsleutels toegevoegd)
**Aanbeveling:** Gebruik v2 voor alle

---

#### CONDITION_DECISION_TREE_DATA
**Versies:** v2, v3 (Huidig)

| Versie | Gegevensgebruik | Status |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Actief |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Huidig |

**Wat is gewijzigd:** v2 → v3: Meer expliciete controle over de gegevensextractie uit de beslisboom
**Aanbeveling:** Gebruik v3

---

### ❌ UITGESCHAKELDE KAARTEN (Niet gebruiken)

#### DOC_SUBORG_CHANGE
**Versies:** v1, v2 (beide uitgeschakeld)
**Status:** Niet langer ondersteund
**Alternatief:** Gebruik de functies voor documenttoewijzing

---

#### RUN_SCRIPT
**Versies:** v2, v3 (beide uitgeschakeld)
**Status:** Vervangen door ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternatief:** Gebruik ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Veelvoorkomende versiepatronen

### Patroon 1: Adoptie van vertaalsleutels (v1 → v2)
**Betreft:** 15+ kaarten

**Wijziging:** `trnsl_%[card_name]` vertaalsleutels toegevoegd
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Kaarten:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS, en meer
**Impact:** Maakt meertalige ondersteuning mogelijk

---

### Patroon 2: Beslisboomintegratie (v2 → v3) - VEROUDERD
**Betreft:** 5 kaarten (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Wijziging:** Optionele beslisboomparameter toegevoegd
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Status:** ❌ Grotendeels verouderd (behalve ACTION_DECISION_TREE_CREATE_TASKS)
**Reden:** Eenvoudigere directe-parameteraanpak heeft de voorkeur

---

### Patroon 3: Generieke type-evolutie (v3 → v4)
**Betreft:** 4 kaarten (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Wijziging:** "Task" → generieke type-parameter
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Impact:** Ondersteunt Task, Ticket, Issue en andere werkitemtypes
**Voordeel:** Grotere flexibiliteit en herbruikbaarheid

---

### Patroon 4: Tolerantieparameters (PO-kaarten)
**Betreft:** 6 kaarten (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, enz.)

**Wijziging:** Ondersteuning voor tolerantie/afwijking toegevoegd
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Voorbeelden:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Impact:** Realistische matchingcriteria (niet alle waarden hoeven exact overeen te komen)

---

### Patroon 5: Vergelijkingsmodusparameters
**Betreft:** 3 kaarten (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Wijziging:** Flexibele selectie van vergelijkingsmethode toegevoegd
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Impact:** Ondersteunt verschillende vergelijkingsalgoritmen

---

## ✅ Versieaanbevelingen

### Voor nieuwe workflows
**Regel:** Gebruik altijd het hoogste ingeschakelde versienummer
- Biedt de nieuwste functies
- Beste ondersteuning
- Meest getest
- Aanbevolen aanpak

### Voor bestaande workflows
**Veilige aanpak:**
- Blijf de huidige versie gebruiken als deze werkt
- Plan een geleidelijke migratie naar nieuwere versies
- Test upgrades eerst in sandbox

### Migratieprioriteit

| Prioriteit | Kaarten | Actie |
|----------|-------|--------|
| **Hoog** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Upgrade naar huidige versie |
| **Gemiddeld** | Overige v1/v2 vertaalupgrades, PO-kaarten v2/v3 | Overweeg upgraden |
| **Laag** | Kaarten zonder functionele wijzigingen | Optioneel |

---

## ⚠️ Verouderde versies - Niet gebruiken

| Kaart | Versie | Reden | Gebruik in plaats daarvan |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Zeer oud, of beslisboom verouderd | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Beslisboomaanpak verouderd | v4 |
| DOC_USER_ASSIGN | v3 | Beslisboomaanpak verouderd | v2 |
| DOC_GROUP_ASSIGN | v3 | Beslisboomaanpak verouderd | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Zeer oud | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Zeer oud | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Functies teruggedraaid | v3 |

---

## 🔄 Volledig uitgeschakelde kaarten - Kunnen niet worden gebruikt

| Kaart | Versies | Reden | Alternatief |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Niet langer ondersteund | Documenttoewijzingskaarten |
| RUN_SCRIPT | v2, v3 | Vervangen door DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Gerelateerde documentatie

- 📖 [Referentie voor kaartversiebeheer](../changelog/card-versioning.md) - Gedetailleerde versie-informatie
- 📚 [Workflowgidsen](../) - Stapsgewijs kaartgebruik
- 🔄 [Kaartversiedatabase](../docs/card_version.md) - Volledige versiegeschiedenis
- 📋 [Workflowlogs](../workflow-logs/) - Uitvoering en foutopsporing

---

**Laatst bijgewerkt:** 23 oktober 2025
**Status:** Volledige versiegeschiedenis
**Databasebron:** postgres-dev-docflow

---
hidden: true
---

# Cronologia di Rilascio e Versioni delle Card del Workflow

## Principi di Controllo delle Versioni

<figure><img src="../../.gitbook/assets/docbits_workflow_version_control.png" alt="Docbits Workflow Version Control"><figcaption>Sistema di Controllo delle Versioni del Workflow</figcaption></figure>

### Version 8.5.2024 - Funzionalità di Versioning di Base

Il Motore di Workflow DocBits implementa un solido controllo delle versioni per tutte le card del workflow:

1. **Version Control**: ogni card può avere più versioni, ognuna rappresentante un diverso insieme di condizioni o azioni. Questo ti consente di sperimentare o modificare le regole senza influire sul workflow attualmente attivo.
2. **Seamless Upgrades**: quando devi aggiornare una regola o una condizione a causa di modifiche ai requisiti di elaborazione dei documenti, puoi creare una nuova versione della card. Questo approccio garantisce che eventuali modifiche siano intenzionali e testate prima di sostituire la versione corrente. Riduce al minimo gli errori e le potenziali interruzioni nell'elaborazione dei documenti.
3. **Maintaining Consistency**: mantenere invariata la versione originale della card finché non decidi di aggiornarla garantisce che i processi in corso non vengano influenzati. Puoi eseguire test e convalide sulla nuova versione senza incidere su dati o workflow in produzione.
4. **Flexibility and Testing**: più versioni consentono di testare scenari diversi in un ambiente controllato. Puoi vedere gli effetti di nuove regole o modifiche sul tuo workflow di elaborazione dei documenti senza apportare modifiche permanenti. Una volta soddisfatto dei risultati, puoi scegliere di applicare la nuova versione.

---

## Panoramica del Versioning delle Card

### Statistiche

| Metrica | Valore |
|--------|-------|
| **Card con Più Versioni** | 30+ |
| **Record di Versione Totali** | 90+ |
| **Versioni Attive Correnti** | 81+ |
| **Versioni Deprecate** | 9 |
| **Card Completamente Disabilitate** | 2 |
| **Versione Più Recente (Max)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Intervallo di Versioni
- **Minima:** v1
- **Massima:** v5
- **Media di Versioni per Card:** 3

---

## Modifiche Dettagliate delle Versioni delle Card

### 🔧 ACTION CARDS - Integrazione ed Esecuzione Esterna

#### 1. CALL_API
**Versioni:** v1, v2 (Corrente: v2)

📖 **Guida:** [Guida alla Chiamata di API Esterne](../then/action/call-api-guide.md)

| Versione | Traduzione | Stato | Modifiche Principali |
|---------|-------------|--------|-------------|
| v1 | No | Active | Chiamata API di base senza chiavi di traduzione |
| v2 | Sì | ✅ Corrente | Aggiunta `trnsl_%call_api` per il supporto multilingua |

**Cosa è cambiato:** aggiunto il supporto all'internazionalizzazione (i18n) con chiavi di traduzione. La funzionalità rimane identica.

**Prima (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Dopo (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Raccomandazione:** usa v2 per tutti i nuovi workflow (include il supporto linguistico)
**Compatibilità all'indietro:** ✅ v1 funziona ancora

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Versioni:** v1, v2 (Corrente: v2)

| Versione | Traduzione | Stato | Modifiche Principali |
|---------|-------------|--------|-------------|
| v1 | No | Active | Richiesta HTTP semplice |
| v2 | Sì | ✅ Corrente | Aggiunte le chiavi di traduzione `trnsl_%send_https_request` |

**Cosa è cambiato:** aggiunto il supporto alla traduzione. La funzionalità principale di webhook/richiesta è invariata.
**Raccomandazione:** usa v2 (supporto multilingua)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Versioni:** v2 (Corrente), v3, v4 (Deprecate e Disabilitate)

| Versione | Traduzione | Stato | Modifiche Principali |
|---------|-------------|--------|-------------|
| v2 | Sì | Active | Implementazione originale di DocOperator |
| v3 | Sì | Active | Aggiunto il parametro "Execute the prompt" per un controllo aggiuntivo |
| v4 | Sì | ❌ DEPRECATED & DISABLED | Rimosso il parametro "Execute" (ripristino) |

**Percorso di Evoluzione:** v2 → v3 (parametro aggiunto) → v4 (ripristinato - non consigliato)

**Cosa è cambiato:**
- v2 → v3: aggiunto un parametro opzionale di controllo dell'esecuzione per maggiore flessibilità
- v3 → v4: rimosso il parametro dopo ulteriore analisi (deprecato)

**Raccomandazione:** usa v3 per i nuovi workflow (ultima versione attiva con tutte le funzionalità)
**Migrazione:** se usi v4, passa a v3 ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Versioni:** v2, v3 (Deprecata), v4 (Corrente)

📖 **Guida:** [Guida all'Assegnazione delle Attività](../then/task/task-assignment-guide.md)

| Versione | Modifiche | Stato | Parametro Type |
|---------|---------|--------|-----------------|
| v2 | Implementazione originale | Active | "Task" (fisso) |
| v3 | + Supporto al decision tree | ❌ DEPRECATED | "Task" (fisso) |
| v4 | - Decision tree, + Tipo generico | ✅ Corrente | Tipo generico (flessibile) |

**Evoluzione:** v2 → v3 (esperimento con decision tree) → v4 (tipi generici, decision tree rimosso)

**Modifica v2 → v3 (Esperimento Decision Tree):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**Modifica v3 → v4 (Tipi Generici + Rimozione Decision Tree):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Cosa è cambiato:**
- v2 → v3: aggiunto il parametro `decision tree, if available: [param]`
- v3 → v4:
  - ❌ Rimosso il parametro decision tree
  - ✅ Cambiato "Task" → `[param]` generico (supporta Task, Ticket, Issue, ecc.)
  - Aggiunta la chiave di traduzione `trnsl_%task_for_group_v4`

**Perché:** l'approccio con decision tree di v3 era sperimentale. v4 offre maggiore flessibilità con tipi di elemento di lavoro generici.
**Raccomandazione:** usa v4 (corrente, più flessibile)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Versioni:** v2, v3 (Corrente)

| Versione | Tipo Task | Stato | Differenza Principale |
|---------|-----------|--------|-----------------|
| v2 | "task" (fisso) | Active | Versione originale |
| v3 | Tipo generico | ✅ Corrente | Cambiato in `[param]` flessibile |

**Cosa è cambiato:** v2 → v3: "Create a new task" → "Create a new [param]" (supporta qualsiasi tipo di elemento di lavoro)
**Raccomandazione:** usa v3

---

#### 6. RUN_WORKFLOW
**Versioni:** v1, v2 (Corrente)

**Cosa è cambiato:** v1 → v2: aggiunte le chiavi di traduzione `trnsl_%run_workflow`
**Raccomandazione:** usa v2

---

### 📊 CARD DI CONFRONTO E CONVALIDA PO

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (La Più Evoluta - 5 Versioni)
**Versioni:** v2, v3, v4, v5 (Corrente)

📖 **Guida:** [Guida Completa al PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Versione | Modifiche | Stato | Tolleranza | Confronto |
|---------|---------|--------|-----------|------------|
| v2 | Confronto prezzo di base | Active | ❌ No | Base |
| v3 | Come v2 | Active | ❌ No | Base |
| v4 | + Parametro modalità di confronto | Active | ❌ No | ✅ Sì |
| v5 | + Parametri di tolleranza | ✅ Corrente | ✅ Sì (importo + unità) | ✅ Sì |

**Percorso di Evoluzione:** v2 → v3 (nessuna modifica) → v4 (modalità di confronto) → v5 (soglie di tolleranza)

**v2 → v3:** nessuna modifica funzionale (stessa chiave di traduzione)

**Modifica v3 → v4 (Aggiunta Modalità di Confronto):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**Modifica v4 → v5 (Aggiunta Parametri di Tolleranza):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Cosa è cambiato:**
- **v2 → v3:** nessuna modifica funzionale
- **v3 → v4:** aggiunto `Compare as [param]` - Supporta diversi operatori di confronto
- **v4 → v5:** aggiunti i parametri di tolleranza:
  - `with tolerance of [amount] [unit]`
  - Esempio: "with tolerance of 2 %" oppure "with tolerance of 100 EUR"
  - Supporta: %, EUR, $ e altre valute

**Casi d'Uso:**
- v2/v3: corrispondenza rigorosa (solo prezzi esatti)
- v4: diversi metodi di confronto
- v5: accettazione flessibile della varianza (es. accettare differenze di prezzo del 2%) ✅ CONSIGLIATA

**Raccomandazione:** usa v5 per i moderni workflow di PO matching

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Versioni:** v1 (Deprecata), v2, v3, v4 (Corrente)

| Versione | Modifiche | Stato | Funzione di Confronto |
|---------|---------|--------|-----------------|
| v1 | Nessuna traduzione, nessun metodo | ❌ DEPRECATED | Base |
| v2 | + Chiavi di traduzione, + metodo | Active | Metodo di base |
| v3 | Come v2 | Active | Metodo di base |
| v4 | + Parametri modalità di confronto | ✅ Corrente | ✅ Flessibile |

**Cosa è cambiato:**
- **v1 → v2:** aggiunte `trnsl_%in_order_confirmations_matches_purchase_order` + parametro del metodo di confronto
- **v2 → v3:** nessuna modifica
- **v3 → v4:** aggiunto `Compare as [param1] [param2]` per modalità di confronto flessibili

**Raccomandazione:** usa v4 (evita v1 che è deprecata)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Versioni:** v2, v3 (Corrente)

| Versione | Giorni di Tolleranza | Giorni di Tolleranza Accettati | Stato |
|---------|-----------------|------------------------|--------|
| v2 | ❌ No | ❌ No | Active |
| v3 | ✅ Sì | ✅ Sì | ✅ Corrente |

**Cosa è cambiato:** v2 → v3: aggiunti i parametri di tolleranza:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Esempio:** accettare date di consegna entro 5 giorni dalla data promessa
**Raccomandazione:** usa v3

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Versioni:** v2, v3, v4 (Corrente)

| Versione | Modalità di Confronto | Stato |
|---------|-----------------|--------|
| v2 | Base | Active |
| v3 | Base (nessuna modifica) | Active |
| v4 | ✅ Selezione modalità flessibile | ✅ Corrente |

**Cosa è cambiato:** v3 → v4: aggiunto `compare [param]` per diversi approcci di confronto
**Raccomandazione:** usa v4

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Versioni:** v2, v3, v4 (Corrente)

| Versione | Modalità di Confronto | Stato |
|---------|-----------------|--------|
| v2 | Standard | Active |
| v3 | Standard (nessuna modifica) | Active |
| v4 | ✅ Flessibile | ✅ Corrente |

**Cosa è cambiato:** v3 → v4: aggiunto il parametro `compare [param]`
**Raccomandazione:** usa v4

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Versioni:** v2, v3 (Corrente)

| Versione | Tipo di Consegna | Tabella Dati Anagrafici | Stato |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (fisso) | Riferimento fisso | Active |
| v3 | [Parametro configurabile] | [param] dinamico | ✅ Corrente |

**Cosa è cambiato:** v2 → v3:
- Cambiato "Confirmed delivery" → `[param] delivery` (tipo di consegna flessibile)
- Cambiato il riferimento fisso alla tabella → `stored in [param]` (selezione dinamica della tabella)

**Flessibilità:** v3 consente diversi tipi di data di consegna e tabelle fornitori
**Raccomandazione:** usa v3

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Versioni:** v2, v3 (Corrente)

| Versione | Riferimento Tabella Fornitori | Stato |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (fisso) | Active |
| v3 | [param dinamico] | ✅ Corrente |

**Cosa è cambiato:** v2 → v3: riferimento fisso alla tabella → `stored in [param]` (consente la selezione dinamica della tabella)
**Raccomandazione:** usa v3

---

### 👥 CARD DI ASSEGNAZIONE E INSTRADAMENTO

#### 1. DOC_USER_ASSIGN
**Versioni:** v1, v2, v3 (Deprecata)

| Versione | Traduzione | Decision Tree | Stato |
|---------|-------------|---------------|--------|
| v1 | No | ❌ No | Active |
| v2 | Sì | ❌ No | ✅ Corrente |
| v3 | Sì | ✅ Sì | ❌ DEPRECATED |

**Evoluzione:** v1 (senza i18n) → v2 (con i18n) → v3 (+ esperimento decision tree, ora deprecata)

**Cosa è cambiato:**
- v1 → v2: aggiunte le chiavi di traduzione
- v2 → v3: aggiunto il supporto al decision tree (sperimentale, deprecato)

**Raccomandazione:** usa v2 (stabile con supporto i18n)

---

#### 2. DOC_GROUP_ASSIGN
**Versioni:** v2, v3 (Deprecata)

| Versione | Decision Tree | Stato |
|---------|---------------|--------|
| v2 | ❌ No | ✅ Corrente |
| v3 | ✅ Sì | ❌ DEPRECATED |

**Cosa è cambiato:** v2 → v3: aggiunto `Use decision tree, if available [param]` (poi deprecato)
**Raccomandazione:** usa v2

---

#### 3. OC_ASSIGN_DOC
**Versioni:** v1, v2 (Corrente)

**Cosa è cambiato:** v1 → v2: aggiunte le chiavi di traduzione `trnsl_%oc_assign_doc`
**Raccomandazione:** usa v2

---

### 📋 CARD DI GESTIONE DELLE ATTIVITÀ

#### 1. tasks_create ⭐ (La Card Attività Più Evoluta - 4 Versioni)
**Versioni:** v1 (Deprecata), v2 (Deprecata), v3 (Deprecata), v4 (Corrente)

📖 **Guida:** [Guida all'Assegnazione delle Attività](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Versione | Traduzione | Decision Tree | Tipo Elemento di Lavoro | Stato |
|---------|-------------|---------------|-----------------|--------|
| v1 | No | No | "Task" (fisso) | ❌ DEPRECATED |
| v2 | Sì | No | "Task" (fisso) | ❌ DEPRECATED |
| v3 | Sì | Sì | "Task" (fisso) | ❌ DEPRECATED |
| v4 | Sì | No | [param generico] | ✅ Corrente |

**Cronologia di Evoluzione:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**Modifica v1 → v2 (Aggiunta Chiavi di Traduzione):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**Modifica v2 → v3 (Esperimento Decision Tree):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**Modifica v3 → v4 (Tipi Generici + Rimozione Decision Tree):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Cosa è cambiato:**
- **v1 → v2:** aggiunte le chiavi di traduzione `trnsl_%tasks_create`
- **v2 → v3:**
  - Aggiunto il supporto al decision tree: `Use decision tree, if available: [param]`
  - Cambiato "assign to user" → "assign it to the user"
- **v3 → v4:**
  - ❌ Rimosso il parametro decision tree
  - ✅ Cambiato "Task" → `[param]` generico (supporta Task, Ticket, Issue, ecc.)
  - Aggiornata la chiave di traduzione a `trnsl_%tasks_create_v4`

**Nota sul Decision Tree:** v3 utilizzava i decision tree per assegnare dinamicamente le attività. Questo approccio era sperimentale ed è stato deprecato in v4 a favore della selezione del tipo di elemento di lavoro basata direttamente sui parametri.

**Raccomandazione:** usa esclusivamente v4 per i nuovi workflow
**Migrazione:** se usi v1, v2 o v3, aggiorna a v4 ✅

---

#### 2. OC_TASK
**Versioni:** v1, v2 (Corrente)

**Cosa è cambiato:** v1 → v2: aggiunte le chiavi di traduzione `trnsl_%oc_task`
**Raccomandazione:** usa v2

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Versioni:** v1, v3 (Corrente - v2 Saltata)

| Versione | Tipo Elemento di Lavoro | Stato |
|---------|-----------------|--------|
| v1 | "Task" (fisso) | Active |
| v3 | [param generico] | ✅ Corrente |

**Cosa è cambiato:** v1 → v3: evoluzione del tipo generico (v2 è stata saltata in produzione)
**Raccomandazione:** usa v3

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Versioni:** v2, v3 (Corrente)

| Versione | Testo di Assegnazione | Stato |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Active |
| v3 | "Assign [generic] with title" | ✅ Corrente |

**Cosa è cambiato:** v2 → v3:
- Cambiato "Assign task" → "Assign [generic param]"
- Cambiato "return of decision" → "return of decision table" (terminologia più chiara)

**Raccomandazione:** usa v3

---

### 🔄 CARD DI CONTROLLO DEL DOCUMENTO

#### APPROVE
**Versioni:** v1, v2 (Corrente)
**Modifica:** aggiunte le chiavi di traduzione `trnsl_%approve_doc`
**Raccomandazione:** usa v2

---

#### REJECT
**Versioni:** v1, v2 (Corrente)
**Modifica:** aggiunte le chiavi di traduzione `trnsl_%reject_doc`
**Raccomandazione:** usa v2

---

#### STAUS_CHANGE (Status Change)
**Versioni:** v1, v2, v3 (Corrente)

| Versione | Trigger del Workflow | Stato |
|---------|-----------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Sì | ✅ Corrente |

**Cosa è cambiato:** v2 → v3: aggiunto `trigger Workflows [param]` - Attiva automaticamente i workflow al cambio di stato
**Raccomandazione:** usa v3

---

#### EXPORT
**Versioni:** v1, v2, v3 (Corrente)

| Versione | Convalida | Stato |
|---------|------------|--------|
| v1 | ❌ No | Active |
| v2 | ❌ No | Active |
| v3 | ✅ Sì | ✅ Corrente |

**Cosa è cambiato:** v2 → v3: aggiunto `Start Export with Validation: [param]`
**Raccomandazione:** usa v3

---

### 🧮 CARD DI MANIPOLAZIONE DEI DATI

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Schema:** v1 → v2 (aggiunte le chiavi di traduzione)
**Raccomandazione:** usa v2 per tutte

---

#### CONDITION_DECISION_TREE_DATA
**Versioni:** v2, v3 (Corrente)

| Versione | Utilizzo dei Dati | Stato |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Active |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Corrente |

**Cosa è cambiato:** v2 → v3: controllo più esplicito sull'estrazione dei dati del decision tree
**Raccomandazione:** usa v3

---

### ❌ CARD DISABILITATE (Da Non Usare)

#### DOC_SUBORG_CHANGE
**Versioni:** v1, v2 (entrambe disabilitate)
**Stato:** non più supportata
**Alternativa:** usa le funzionalità di assegnazione dei documenti

---

#### RUN_SCRIPT
**Versioni:** v2, v3 (entrambe disabilitate)
**Stato:** sostituita da ACTION_RUN_DOCOPERATOR_SCRIPT
**Alternativa:** usa ACTION_RUN_DOCOPERATOR_SCRIPT v3

---

## 🎯 Schemi Comuni di Versione

### Schema 1: Adozione delle Chiavi di Traduzione (v1 → v2)
**Interessate:** 15+ card

**Modifica:** aggiunte le chiavi di traduzione `trnsl_%[card_name]`
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Card:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS e altre
**Impatto:** abilita il supporto multilingua

---

### Schema 2: Integrazione Decision Tree (v2 → v3) - DEPRECATA
**Interessate:** 5 card (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Modifica:** aggiunto un parametro decision tree opzionale
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Stato:** ❌ Per lo più deprecata (eccetto ACTION_DECISION_TREE_CREATE_TASKS)
**Motivo:** preferito un approccio più semplice basato direttamente sui parametri

---

### Schema 3: Evoluzione del Tipo Generico (v3 → v4)
**Interessate:** 4 card (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Modifica:** "Task" → parametro di tipo generico
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Impatto:** supporta Task, Ticket, Issue e altri tipi di elemento di lavoro
**Vantaggio:** maggiore flessibilità e riutilizzabilità

---

### Schema 4: Parametri di Tolleranza (Card PO)
**Interessate:** 6 card (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY, ecc.)

**Modifica:** aggiunto il supporto a tolleranza/varianza
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Esempi:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Impatto:** criteri di corrispondenza realistici (non tutti i valori devono corrispondere esattamente)

---

### Schema 5: Parametri di Modalità di Confronto
**Interessate:** 3 card (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Modifica:** aggiunta la selezione flessibile del metodo di confronto
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Impatto:** supporta diversi algoritmi di confronto

---

## ✅ Raccomandazioni sulle Versioni

### Per i Nuovi Workflow
**Regola:** usa sempre il numero di versione abilitato più alto
- Fornisce le funzionalità più recenti
- Miglior supporto
- Più testata
- Approccio consigliato

### Per i Workflow Esistenti
**Approccio Sicuro:**
- Continua a usare la versione corrente se funziona
- Pianifica una migrazione graduale verso versioni più recenti
- Testa prima gli aggiornamenti in sandbox

### Priorità di Migrazione

| Priorità | Card | Azione |
|----------|-------|--------|
| **Alta** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Aggiorna alla versione corrente |
| **Media** | Altri aggiornamenti di traduzione v1/v2, card PO v2/v3 | Valuta l'aggiornamento |
| **Bassa** | Card senza modifiche funzionali | Facoltativo |

---

## ⚠️ Versioni Deprecate - Da Non Usare

| Card | Versione | Motivo | Usa Invece |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Molto vecchia, o decision tree deprecato | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Approccio decision tree deprecato | v4 |
| DOC_USER_ASSIGN | v3 | Approccio decision tree deprecato | v2 |
| DOC_GROUP_ASSIGN | v3 | Approccio decision tree deprecato | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Molto vecchia | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Molto vecchia | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funzionalità ripristinate | v3 |

---

## 🔄 Card Completamente Disabilitate - Non Utilizzabili

| Card | Versioni | Motivo | Alternativa |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Non più supportata | Card di assegnazione documenti |
| RUN_SCRIPT | v2, v3 | Sostituita da DocOperator | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## Documentazione Correlata

- 📖 [Riferimento al Versioning delle Card](../changelog/card-versioning.md) - Informazioni dettagliate sulle versioni
- 📚 [Guide ai Workflow](../) - Utilizzo delle card passo dopo passo
- 🔄 [Database delle Versioni delle Card](../docs/card_version.md) - Cronologia completa delle versioni
- 📋 [Log del Workflow](../workflow-logs/) - Esecuzione e debug

---

**Ultimo Aggiornamento:** 23 ottobre 2025
**Stato:** Cronologia Completa delle Versioni
**Origine Database:** postgres-dev-docflow

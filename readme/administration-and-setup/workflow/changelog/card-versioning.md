# Sistema di Versioning delle Card - Aggiornamento di Ottobre 2025

**Documento:** Panoramica del Versioning delle Card del Workflow
**Ultimo Aggiornamento:** 23 ottobre 2025
**Stato:** Completo

---

## Panoramica

Il Motore di Workflow DocBits utilizza un **versioning basato su numeri interi** per gestire l'evoluzione delle card mantenendo la compatibilità all'indietro. Questo documento fornisce una panoramica del sistema di versioning.

---

## Cos'è il Versioning delle Card?

### Concetto
Ogni card del workflow può avere più versioni, consentendo al sistema di:
- Aggiungere nuove funzionalità senza interrompere i workflow esistenti
- Supportare funzionalità deprecate durante la loro dismissione graduale
- Far evolvere le capacità delle card nel tempo
- Mantenere la compatibilità all'indietro

### Struttura della Versione
- **Formato:** valori interi (1, 2, 3, 4, 5...)
- **Identificazione:** chiave composita di (card_type, card_version)
- **Stato:** ogni versione ha flag deprecated/enabled

### Esempio
La card `tasks_create` si è evoluta attraverso 4 versioni:
- **v1:** creazione di attività originale (deprecata)
- **v2:** aggiunto il supporto alla traduzione (deprecata)
- **v3:** supporto sperimentale al decision tree (deprecata)
- **v4:** supporto al tipo di elemento di lavoro generico (attiva corrente)

---

## Statistiche Chiave

### Panoramica del Versioning
| Metrica | Valore |
|--------|-------|
| **Card con Più Versioni** | 30+ |
| **Record di Versione Totali** | 90+ |
| **Versioni per Card (media)** | 3 |
| **Versioni Massime** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Versioni Deprecate** | 9 |
| **Card Completamente Disabilitate** | 2 |

### Distribuzione delle Versioni
- **2 Versioni:** 14 card (evoluzione più semplice)
- **3 Versioni:** 11 card (evoluzione moderata)
- **4 Versioni:** 4 card (evoluzione significativa)
- **5 Versioni:** 1 card (la più evoluta: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Schemi Comuni di Versione

### Schema 1: Adozione delle Chiavi di Traduzione (v1 → v2)

**Interessate:** 15+ card

**Modifica:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Scopo:** abilitare il supporto multilingua

**Card:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS e altre

**Migrazione:** sicura - nessuna modifica funzionale

---

### Schema 2: Integrazione Decision Tree (v2 → v3)

**Interessate:** 5 card

**Modifica:** aggiunta del parametro decision tree

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Scopo:** supportare i risultati delle decision table

**Card:**
- tasks_create (v3 deprecata)
- ACTION_TASK_FOR_GROUP (v3 deprecata)
- DOC_USER_ASSIGN (v3 deprecata)
- DOC_GROUP_ASSIGN (v3 deprecata)
- ACTION_DECISION_TREE_CREATE_TASKS

**Stato:** deprecato - l'approccio con decision tree era sperimentale

---

### Schema 3: Evoluzione del Tipo Generico (v3 → v4)

**Interessate:** 4 card

**Modifica:** "Task" diventa un tipo di elemento di lavoro flessibile

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Scopo:** supportare Task, Ticket, Issue e altri tipi di elemento di lavoro

**Card:**
- tasks_create (v4 corrente)
- ACTION_TASK_FOR_GROUP (v4 corrente)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 corrente)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 corrente)

**Stato Corrente:** attivo e consigliato

---

### Schema 4: Parametri di Tolleranza (Card PO)

**Interessate:** 6 card di confronto PO

**Modifica:** aggiunta del supporto a tolleranza/varianza

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Scopo:** consentire una varianza accettabile nell'abbinamento (es. una differenza di prezzo del 2% è accettabile)

**Card Principali:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (evoluta a v5 con tolleranza)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Vantaggio:** criteri di abbinamento più realistici

---

### Schema 5: Parametri di Modalità di Confronto

**Interessate:** 3 card di confronto PO

**Modifica:** supporto a diversi algoritmi di confronto

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Scopo:** metodi di confronto flessibili

**Card:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Schema 6: Trigger dei Workflow

**Interessate:** solo STAUS_CHANGE

**Modifica:** attivazione automatica dei workflow al cambio di stato

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Scopo:** propagare i cambiamenti di stato tra i workflow

---

## Card Più Evolute

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versioni)

**Percorso di Evoluzione:** v2 → v3 → v4 → v5

- **v2:** confronto di base del prezzo unitario
- **v3:** stessa chiave di traduzione (v2)
- **v4:** aggiunto il parametro modalità di confronto
- **v5:** aggiunto il parametro di soglia di tolleranza

**Corrente:** v5 (con supporto alla tolleranza)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versioni)

**Percorso di Evoluzione:** v1 → v2 → v3 → v4

- **v1:** abbinamento di base degli articoli (deprecata)
- **v2:** aggiunto il parametro del metodo di confronto
- **v3:** potenziata con le chiavi di traduzione
- **v4:** aggiunto il parametro modalità di confronto

**Corrente:** v4

**Evita:** v1 (deprecata)

---

### 3. tasks_create (4 versioni)

**Percorso di Evoluzione:** v1 → v2 → v3 → v4

- **v1:** implementazione originale (deprecata)
- **v2:** aggiunto il supporto alla traduzione (deprecata)
- **v3:** aggiunto il decision tree (deprecata)
- **v4:** tipi di elemento di lavoro generici (corrente)

**Corrente:** v4 (consigliata)

**Cronologia:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Stato di Deprecazione

### Versioni Completamente Deprecate (Da Non Usare)

| Card | Versione | Motivo | Alternativa |
|------|---------|--------|-------------|
| tasks_create | v1 | Molto vecchia | Usa v4 |
| tasks_create | v3 | Decision tree deprecato | Usa v4 |
| ACTION_TASK_FOR_GROUP | v3 | Decision tree deprecato | Usa v4 |
| DOC_USER_ASSIGN | v3 | Decision tree deprecato | Usa v2 |
| DOC_GROUP_ASSIGN | v3 | Decision tree deprecato | Usa v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Molto vecchia | Usa v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Molto vecchia | Usa v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funzionalità ripristinate | Usa v3 |

### Card Completamente Disabilitate (Non Utilizzabili)

| Card | Versioni | Note |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Funzionalità non supportata |
| RUN_SCRIPT | v2, v3 | Sostituita da ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Raccomandazioni sulle Versioni

### Per Caso d'Uso

**Creazione di Nuovi Workflow:**
- Usa sempre il **numero di versione abilitato più alto**
- Fornisce le funzionalità e i miglioramenti più recenti
- Supportato e documentato

**Manutenzione dei Workflow Esistenti:**
- Continua a usare la versione corrente se funziona
- Pianifica la migrazione quando è fattibile
- Nessuna necessità urgente di aggiornare

**Migrazione di Workflow Legacy:**
- Identifica la versione attualmente in uso
- Pianifica il percorso di aggiornamento
- Testa accuratamente prima di distribuire

---

## Come Funzionano le Versioni

### Selezione della Versione
Quando crei un workflow, selezioni quale versione di una card utilizzare. Esempio:
- Usa `tasks_create v4` per la creazione di nuove attività (consigliato)
- Usa `tasks_create v2` se i sistemi legacy lo richiedono (più vecchia ma funzionante)
- NON usare `tasks_create v1` (deprecata)

### Compatibilità all'Indietro
- Le versioni più recenti non interrompono i workflow più vecchi
- I vecchi workflow continuano a funzionare con la loro versione originale
- È possibile aggiornare i workflow gradualmente

### Implementazione Tecnica
Le versioni sono gestite a livello di database:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## A Scopo Documentale

### Comprendere le Informazioni sulla Versione
Quando vedi "Card v3" nella documentazione:
- Si riferisce alla versione 3 di quella specifica card
- Consulta il [Riferimento Completo al Versioning](../../docs/card_version.md) per i dettagli
- Verifica quale versione è consigliata

### Verificare la Tua Versione
Per sapere quale versione stai utilizzando:
1. Apri la card nel tuo workflow
2. Controlla il numero di versione visualizzato
3. Confronta con le raccomandazioni nelle guide

### Cronologia di Evoluzione delle Versioni
- **2024-2025:** evoluzione in corso
- **Ottobre 2025:** documentazione completa del versioning
- **Futuro:** miglioramenti continui

---

## Documentazione Correlata

### Riferimento Completo
→ [Riferimento Completo al Versioning delle Card](../../docs/card_version.md)

Include:
- Tutte le 30+ card con versioni
- Evoluzione dettagliata del testo per ciascuna
- Modifiche specifiche dei parametri
- Query SQL per la ricerca delle versioni

### Guide Specifiche per Card
→ [Guide ai Workflow](../)

Documentazione per ciascuna card con raccomandazioni sulle versioni

### Dettagli della Cronologia delle Versioni
Ogni guida include informazioni sulla versione e note di migrazione

---

## Riferimento Rapido

### Card con Più Versioni
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versioni
2. CONDITION_OC_TO_PO_ITEMS - 4 versioni
3. tasks_create - 4 versioni
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versioni
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versioni

### Schema di Evoluzione Più Comune
**Adozione delle Chiavi di Traduzione (v1 → v2)** - 15+ card

### Modifica Più Significativa
**Evoluzione del Tipo Generico (v3 → v4)** - cambiato da "Task" a un tipo di elemento di lavoro flessibile

### Completamente Disabilitate
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Domande Frequenti

### D: Quale versione dovrei usare?
R: usa la **versione abilitata più alta** a meno che tu non abbia un motivo specifico per usare una versione più vecchia.

### D: Posso aggiornare il mio workflow a una versione più recente?
R: sì, ma testa accuratamente. Alcune versioni hanno requisiti di parametri diversi.

### D: Cosa succede se uso una versione deprecata?
R: continua a funzionare, ma non otterrai nuove funzionalità. Migrazione consigliata.

### D: Posso usare una card disabilitata?
R: no, le card disabilitate non possono essere usate. Usa invece l'alternativa consigliata.

### D: Come faccio a sapere se la mia card deve essere aggiornata?
R: consulta il [Riferimento Completo al Versioning](../../docs/card_version.md) per il tuo tipo di card e segui le raccomandazioni.

---

## Best Practice

1. **Nuovi Workflow:** usa l'ultima versione stabile
2. **Aggiornamenti:** controlla periodicamente le nuove versioni
3. **Test:** testa prima gli aggiornamenti di versione in sandbox
4. **Documentazione:** fai riferimento alle guide specifiche per card per i dettagli sulle versioni
5. **Migrazione:** pianifica gli aggiornamenti in modo incrementale
6. **Supporto:** contatta il supporto in caso di domande sulla compatibilità delle versioni

---

## Tabella di Riepilogo

| Tipo di Card | Versione Corrente | Versioni Totali | Stato | Note |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Active | La più evoluta; v3 deprecata |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Active | Conteggio versioni più alto |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Active | v1 deprecata |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Active | v3 deprecata |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Active | v4 deprecata/disabilitata |
| La maggior parte delle card | 2 | 2 | Active | Schema v1 → v2 |

---

## Vedi Anche

- 📖 [Riferimento Completo al Versioning delle Card](../../docs/card_version.md)
- 🔗 [Guide ai Workflow](../)
- 📋 [Note di Rilascio di Ottobre 2025](./2025-10-october.md)
- 🔄 [Analisi del Collegamento dei Workflow](../../WORKFLOW_LINKING_MAP.md)

---

**Ultimo Aggiornamento:** 23 ottobre 2025
**Origine:** database postgres-dev-docflow
**Stato:** Riferimento Completo

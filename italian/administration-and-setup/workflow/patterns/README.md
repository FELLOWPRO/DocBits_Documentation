# Guide ai pattern di workflow

**Versione:** 1.0
**Ultimo aggiornamento:** 23 ottobre 2025

---

## Panoramica

Questa directory contiene guide complete ai pattern di workflow che mostrano come combinare più card di workflow per risolvere scenari aziendali comuni. Ogni pattern fornisce istruzioni di implementazione passo passo, esempi completi e best practice.

**Cosa sono i pattern di workflow?**

I pattern di workflow sono soluzioni comprovate e riutilizzabili per le sfide comuni di elaborazione dei documenti. Invece di partire da zero, puoi usare questi pattern come modelli e adattarli alle tue esigenze specifiche.

---

## Il Workflow Builder in breve

Ogni pattern di questa pagina viene assemblato nel **Workflow Builder**. Lo raggiungi da **Workflow Dashboard → Workflow List → Add Workflow** (oppure aprendo un workflow esistente). La dashboard ti mostra la cronologia delle esecuzioni e i tassi di successo/fallimento di tutti i tuoi workflow:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard che mostra i totali delle esecuzioni, i tassi di successo e fallimento, il grafico delle esecuzioni del workflow e l'attività recente"><figcaption><p>La Workflow Dashboard — totali delle esecuzioni, tassi di successo/fallimento e attività recente per ogni workflow.</p></figcaption></figure>

La scheda **Workflow List** elenca ogni workflow con il suo tipo, l'ordine di esecuzione e il trigger. Usa **Add Workflow** per crearne uno nuovo, oppure clicca su un workflow per aprirlo nel builder:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="Scheda Workflow List che elenca i workflow con tipo, ordine di esecuzione e trigger"><figcaption><p>La Workflow List — ogni riga è un workflow che puoi aprire, attivare/disattivare o modificare.</p></figcaption></figure>

Un workflow è costruito da tre gruppi di card — **When** (il trigger), **And** (condizioni aggiuntive) e **Then** (le azioni da eseguire). L'esempio qui sotto si attiva sulle fatture appartenenti a una sotto-organizzazione e le assegna a un utente:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Canvas del Workflow Builder con card When, And e Then"><figcaption><p>Il canvas del Workflow Builder. Ogni pattern qui sotto è semplicemente una diversa combinazione di card When / And / Then.</p></figcaption></figure>

Clicca **Add Card** in qualsiasi gruppo per aprire la libreria delle card. Le card sono organizzate per categoria (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …) così puoi trovare il blocco costitutivo richiesto da ciascun pattern:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Finestra di dialogo Add Card che mostra le categorie di card e le card disponibili"><figcaption><p>La libreria <strong>Add Card</strong> — ogni card a cui si fa riferimento nei pattern qui sotto viene scelta da qui.</p></figcaption></figure>

---

## Pattern disponibili

### 1. [API Integration Pattern](api-integration-pattern.md)

**Complessità:** Media | **Tempo di configurazione:** 45-60 minuti

Scopri come integrare DocBits con API esterne per recuperare, validare e memorizzare dati da sistemi esterni.

**Casi d'uso:**
- Recuperare prezzi in tempo reale da sistemi esterni
- Validare le informazioni dei fornitori rispetto a database master
- Cercare i dettagli dei prodotti dai sistemi di catalogo
- Ottenere i tassi di cambio dai servizi valutari
- Verificare gli indirizzi con servizi di geocodifica

**Card utilizzate:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Visualizza il pattern completo →](api-integration-pattern.md)**

---

### 2. [Task Management Pattern](task-management-pattern.md)

**Complessità:** Bassa-Media | **Tempo di configurazione:** 30-45 minuti

Padroneggia l'arte di creare, assegnare, monitorare e gestire i task all'interno dei workflow di DocBits per i processi di approvazione e revisione.

**Casi d'uso:**
- Creare workflow di approvazione
- Assegnare task di revisione agli utenti
- Gestire le eccezioni che richiedono intervento umano
- Inoltrare i problemi ai manager
- Creare catene di approvazione multi-livello
- Monitorare il completamento dei task e le scadenze

**Card utilizzate:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Visualizza il pattern completo →](task-management-pattern.md)**

---

### 3. [PO Matching Pattern](po-matching-pattern.md)

**Complessità:** Media-Alta | **Tempo di configurazione:** 60-90 minuti

Implementa workflow completi di matching degli ordini di acquisto per validare le fatture rispetto ai PO con instradamento basato sulla tolleranza.

**Casi d'uso:**
- Validare le fatture rispetto agli ordini di acquisto
- Rilevare errori di prezzo prima del pagamento
- Identificare discrepanze nelle quantità
- Applicare controlli sugli approvvigionamenti
- Prevenire pagamenti duplicati
- Automatizzare il matching a tre vie

**Card utilizzate:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Visualizza il pattern completo →](po-matching-pattern.md)**

---

### 4. [Decision Logic Pattern](decision-logic-pattern.md)

**Complessità:** Media | **Tempo di configurazione:** 30-45 minuti

Implementa alberi decisionali complessi e logica di instradamento condizionale per elaborare i documenti attraverso percorsi diversi in base alle regole aziendali.

**Casi d'uso:**
- Instradare i documenti per soglie di importo
- Applicare regole diverse per tipi di documento diversi
- Implementare logica di approvazione multi-livello
- Gestire policy aziendali complesse
- Creare instradamento dinamico basato su più criteri
- Implementare matrici di approvazione

**Card utilizzate:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Visualizza il pattern completo →](decision-logic-pattern.md)**

---

### 5. [Data Transformation Pattern](data-transformation-pattern.md)

**Complessità:** Media | **Tempo di configurazione:** 30-45 minuti

Trasforma, calcola, formatta e arricchisci i dati dei documenti per prepararli all'esportazione, eseguire calcoli e standardizzare i formati.

**Casi d'uso:**
- Calcolare totali, subtotali, imposte
- Convertire valute o unità di misura
- Formattare date, numeri, testo
- Derivare valori da campi esistenti
- Arricchire i dati da fonti esterne
- Standardizzare i formati dei dati
- Validare i calcoli

**Card utilizzate:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Visualizza il pattern completo →](data-transformation-pattern.md)**

---

## Guida alla scelta del pattern

### Per complessità

| Complessità | Pattern | Ideale per |
|------------|----------|----------|
| **Bassa-Media** | [Task Management](task-management-pattern.md) | Principianti, workflow semplici |
| **Media** | [API Integration](api-integration-pattern.md)<br>[Decision Logic](decision-logic-pattern.md)<br>[Data Transformation](data-transformation-pattern.md) | Utenti intermedi, workflow standard |
| **Media-Alta** | [PO Matching](po-matching-pattern.md) | Utenti avanzati, validazione complessa |

---

### Per caso d'uso

| Ho bisogno di... | Usa questo pattern |
|--------------|------------------|
| Integrare con sistemi esterni | [API Integration Pattern](api-integration-pattern.md) |
| Creare workflow di approvazione | [Task Management Pattern](task-management-pattern.md) |
| Validare rispetto agli ordini di acquisto | [PO Matching Pattern](po-matching-pattern.md) |
| Instradare in base alle condizioni | [Decision Logic Pattern](decision-logic-pattern.md) |
| Calcolare e trasformare i dati | [Data Transformation Pattern](data-transformation-pattern.md) |

---

### Per settore/reparto

| Settore/Reparto | Pattern consigliati |
|---------------------|---------------------|
| **Finanza/Contabilità** | [PO Matching](po-matching-pattern.md), [Task Management](task-management-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Approvvigionamenti** | [PO Matching](po-matching-pattern.md), [Decision Logic](decision-logic-pattern.md), [API Integration](api-integration-pattern.md) |
| **Operations** | [Task Management](task-management-pattern.md), [Decision Logic](decision-logic-pattern.md) |
| **IT/Integrazione** | [API Integration](api-integration-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Tutti i reparti** | [Decision Logic](decision-logic-pattern.md), [Task Management](task-management-pattern.md) |

---

## Come usare questi pattern

### Passo 1: Scegli un pattern

1. Esamina le descrizioni dei pattern qui sopra
2. Identifica quale pattern corrisponde al tuo caso d'uso
3. Verifica la complessità e il tempo di configurazione stimato
4. Esamina la sezione "Quando usarlo" nella guida del pattern

### Passo 2: Esamina i prerequisiti

Ogni guida al pattern elenca:
- Conoscenze richieste
- Guide correlate da leggere prima
- Card che verranno utilizzate
- Requisiti di configurazione

### Passo 3: Segui le istruzioni passo passo

Ogni pattern fornisce:
- Esempio completo di workflow
- Guida all'implementazione passo passo
- Modelli di configurazione
- Esempi reali
- Suggerimenti per la risoluzione dei problemi

### Passo 4: Personalizza in base alle tue esigenze

- Adatta l'esempio alle tue regole aziendali
- Regola soglie e tolleranze
- Modifica la logica di instradamento
- Aggiungi/rimuovi passaggi secondo necessità
- Esegui test approfonditi prima dell'uso in produzione

### Passo 5: Monitora e ottimizza

- Monitora le prestazioni del workflow
- Monitora i tassi di successo
- Raccogli il feedback degli utenti
- Affina la configurazione
- Documenta le personalizzazioni

---

## Combinazioni di pattern

Molti scenari reali richiedono la combinazione di più pattern:

### Esempio 1: Elaborazione completa della fattura

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Esempio 2: Approvazione di fatture di valore elevato

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Esempio 3: Gestione delle eccezioni

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

---

## Modelli di pattern

Ogni pattern include queste sezioni standardizzate:

1. **Panoramica** - Cosa fa il pattern
2. **Quando usarlo** - Casi d'uso appropriati
3. **Esempio completo** - Scenario reale
4. **Passo passo** - Istruzioni di implementazione
5. **Configurazione** - Modelli di configurazione delle card
6. **Diagramma del workflow** - Rappresentazione visiva
7. **Varianti avanzate** - Implementazioni alternative
8. **Gestione degli errori** - Problemi comuni e soluzioni
9. **Checklist di test** - Passaggi di validazione
10. **Pattern correlati** - Pattern complementari
11. **Guide correlate** - Documentazione di riferimento

---

## Ottenere aiuto

### Risorse di supporto per i pattern

**Documentazione:**
- [Indice completo delle guide ai workflow](../README.md)
- [Guide alle singole card](../then/action/)
- [Riferimento alle card di condizione](../and/condition-cards-complete-guide.md)
- [Mappa di collegamento dei workflow](../../../../WORKFLOW_LINKING_MAP.md)

**Risorse aggiuntive:**
- [Guida di riferimento rapido](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- [Note di rilascio ottobre 2025](../changelog/2025-10-october.md)
- [Riferimento al versionamento delle card](../../../docs/card_version.md)

**Contatti:**
- Feedback sui pattern: docs@docbits.com
- Supporto tecnico: support@docbits.com
- Aiuto all'implementazione: consulting@docbits.com

---

## Statistiche dei pattern

| Metrica | Valore |
|--------|-------|
| **Totale pattern** | 5 |
| **Totale card coperte** | 30+ |
| **Documentazione combinata** | ~1.200 righe |
| **Scenari di esempio** | 25+ |
| **Modelli di configurazione** | 15+ |
| **Diagrammi di workflow** | 5 diagrammi completi |
| **Riferimenti incrociati** | 87+ link interni |

---

## Contribuire ai pattern

Hai un pattern di workflow che potrebbe essere utile ad altri?

**Linee guida per contribuire ai pattern:**

1. **Documenta il tuo workflow**
   - Scenario aziendale chiaro
   - Implementazione passo passo
   - Esempi di configurazione funzionanti
   - Risultati di test reali

2. **Segui il modello di pattern**
   - Usa la struttura standard delle sezioni
   - Includi tutti gli elementi richiesti
   - Fornisci diagrammi/esempi
   - Aggiungi una guida alla risoluzione dei problemi

3. **Invia per la revisione**
   - Email a: docs@docbits.com
   - Includi: descrizione del pattern, casi d'uso, guida all'implementazione
   - Lo esamineremo e potenzialmente lo aggiungeremo alla documentazione ufficiale

**Vantaggi:**
- Aiutare altri utenti DocBits
- Essere riconosciuti nella documentazione
- Migliorare la base di conoscenza complessiva del prodotto
- Ricevere feedback sulla tua implementazione

---

## Changelog

### Versione 1.0 (23 ottobre 2025)
- Rilascio iniziale di 5 pattern di workflow completi
- Aggiunto API Integration Pattern
- Aggiunto Task Management Pattern
- Aggiunto PO Matching Pattern
- Aggiunto Decision Logic Pattern
- Aggiunto Data Transformation Pattern
- Implementato il collegamento con riferimenti incrociati (87 link)
- Creata la guida alla scelta del pattern

---

## Prossimi passi

**Nuovo ai pattern di workflow?**
1. Inizia con il [Task Management Pattern](task-management-pattern.md) - il più facile da comprendere
2. Esamina il [Decision Logic Pattern](decision-logic-pattern.md) - fondamentale per tutti i workflow
3. Esplora l'[API Integration Pattern](api-integration-pattern.md) - esigenza di integrazione comune

**Pronto a implementare?**
1. Scegli il tuo pattern dall'elenco qui sopra
2. Leggi la guida completa al pattern
3. Esamina i prerequisiti e le guide correlate
4. Segui le istruzioni passo passo
5. Esegui test con documenti di esempio
6. Distribuisci in produzione
7. Monitora e ottimizza

**Hai bisogno di altro aiuto?**
- Esamina la [Panoramica della documentazione dei workflow](../README.md)
- Consulta la [Guida di riferimento rapido](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- Contatta il team di supporto

---

**Ultimo aggiornamento:** 23 ottobre 2025
**Gestito da:** Team di documentazione
**Versione:** 1.0

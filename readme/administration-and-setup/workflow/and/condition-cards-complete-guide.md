# Carte Condizioni - Guida Completa

## Carte Condizioni - Guida Completa

Le schede di condizione di questa pagina vanno nei gruppi **Quando** e **E** del Generatore di workflow — decidono se eseguire le azioni Then. Per usare il canvas — **Aggiungi scheda**, **Salva modello**, **Salva flusso di lavoro** — consulta la [guida Standard Workflow](../README.md):

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-it.png" alt="Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale."><figcaption><p>Esempio non salvato con schede Quando, E e Allora. Configurare tutti i campi prima dell’esecuzione. Alcune etichette dell’interfaccia di questa versione sono ancora in inglese o tradotte in modo non corretto. Le spiegazioni di questa pagina sono tradotte; l’immagine mostra l’interfaccia reale.</p></figcaption></figure>

**Copre:** le 31 condition card rimanenti

***

### 📌 Informazioni sulla Versione

**Stato:** la maggior parte delle condition card è stabile con strutture a versione singola o doppia **Schema delle Versioni:** la maggior parte segue lo schema v1 → v2 (aggiunta del supporto i18n) **Esempio Multi-Versione:** CONDITION\_DECISION\_TREE\_DATA (v2-v3)

**Nota:** alcune condition card di confronto PO hanno diverse versioni. Usa questa guida per il comportamento attuale e le note della versione qui sotto per le modifiche pubblicate.

📖 [Note della versione del prodotto](../../../overview-and-basics/release-notes) | [Guida al PO Matching](compare-with-purchase-order/po-matching-complete-guide.md)

***

## Condizioni su Stato del Documento

### Carta: CONDITION\_DOC\_STATUS\_IS\_ISNOT / Controllo stato documento

#### Scopo

Verifica se il documento ha uno stato specifico

#### Quando Usarla

* Prima dell'approvazione
* In una fase specifica del flusso di lavoro
* Instradamento basato sullo stato

#### Tipi di Stato del Documento

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

#### Come Funziona

```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

#### Esempio

```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

#### Parametri

```
Operator: IS / IS NOT
Status: [Select status]
```

***

### Carta: CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST

#### Scopo

Verifica se lo stato corrisponde a uno qualsiasi di un elenco

#### Quando Usarla

* Più stati validi
* Logica OR per lo stato

#### Esempio

```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

***

### Carta: CONDITION\_DOC\_TYPE\_IS\_ISNOT / Verifica tipo documento

#### Scopo

Verifica se il documento è di un tipo specifico

#### Tipi di Documento

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

#### Come Funziona

```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

#### Esempio

```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

***

### Carta: CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST

#### Scopo

Verifica se il tipo corrisponde a uno qualsiasi di un elenco

#### Esempio

```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

***

### Carta: CONDITION\_SUB\_ORG\_IS\_ISNOT / Controllo Sotto-Organizzazione

#### Scopo

Verifica quale organizzazione/reparto è proprietario del documento

#### Organizzazioni

```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

#### Esempio

```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

***

### Carta: CONDITION\_PURCHASE\_ORDER\_IMPORT / Controllo importazione PO

#### Scopo

Verifica se il PO è appena importato o già esistente

#### Come Funziona

```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

#### Quando Usarla

* Gestione diversa per i nuovi PO
* Saltare la convalida per i PO noti
* Tracciare la prima volta che si vede un fornitore

***

## Condizioni sull'Assegnatario

### Carta: CONDITION\_USER\_IS\_ISNOT / Controllo Utente

#### Scopo

Verifica se il documento è assegnato a un utente specifico

#### Come Funziona

```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

#### Esempio

```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

***

### Carta: CONDITION\_USER\_IS\_ISNOT\_IN\_LIST

#### Scopo

Verifica se è assegnato a uno qualsiasi degli utenti di un elenco

#### Esempio

```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

***

### Carta: CONDITION\_GROUP\_IS\_ISNOT / Controllo di gruppo

#### Scopo

Verifica se è assegnato a un gruppo specifico

#### Esempio

```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

***

### Carta: CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST

#### Scopo

Verifica se è assegnato a uno qualsiasi dei gruppi di un elenco

#### Esempio

```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

***

## Condizioni su Data e Ora

### Carta: CONDITION\_TIME\_IS\_ISNOT\_BETWEEN / Controllo intervallo date

#### Scopo

Verifica se una data è compresa tra due date

#### Come Funziona

```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

#### Calcolo

```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

#### Quando Usarla

* Verificare se si è in un periodo fiscale
* Verificare se si è entro una scadenza
* Verificare se si è in un periodo promozionale

#### Esempio

```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

#### Parametri

```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

***

### Carta: CONDITION\_TODAY\_IS\_ISNOT / Controllo oggi

#### Scopo

Verifica se la data odierna corrisponde ai criteri

#### Come Funziona

```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

#### Casi d'Uso

```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

#### Esempio

```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

***

### Carta: CONDITION\_CONFIRMED\_DELIVERY\_ACCEPTED\_DATE\_IN\_CALENDAR\_MASTER\_DATA

#### Scopo

Verifica se la data di consegna corrisponde alle date di consegna approvate nel calendario

#### Come Funziona

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

#### Quando Usarla

* Verificare che la consegna corrisponda alle date concordate
* Confrontare con il calendario delle festività
* Convalidare rispetto alle date contrattuali

#### Esempio

```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

***

## Condizioni Logiche

### Carta: CONDITION\_DECISION\_TREE\_DATA / Ritorni della tabella decisionale

#### Scopo

Verifica se la decision table ha valori restituiti

#### Come Funziona

```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

#### Quando Usarla

* Prima di utilizzare i risultati della decision table
* Come condizione di filtro
* Per verificare se l'instradamento è disponibile

#### Esempio

```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

***

### Carta: CONDITION\_CONTINUE\_CHANCE / Probabilità casuale

#### Scopo

Prosegue con una probabilità specificata

#### Come Funziona

```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

#### Quando Usarla

* Flusso di lavoro di A/B testing
* Campionamento dei documenti
* Controlli qualità casuali

#### Esempio

```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

#### Calcolo

```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

***

### Scheda: CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE / Controllo funzionalità

#### Scopo

Verifica se un modulo/funzionalità specifica è abilitato

#### Moduli

```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

#### Come Funziona

```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

#### Quando Usarla

* Workflow dipendenti da funzionalità
* Elaborazione opzionale
* Verificare se una funzionalità in licenza è attiva

***

### Scheda: CONDITION\_HTTPS\_REQUEST\_STATUS / Richiedi controllo esito

#### Scopo

Verifica se la richiesta HTTPS è andata a buon fine

#### Codici di Stato

```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

#### Come Funziona

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

#### Esempio

```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

***

### Scheda: CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT / Verifica Stato Fornitore

#### Scopo

Verifica lo stato del fornitore nel sistema

#### Stati del Fornitore

```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

#### Come Funziona

```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

#### Esempio

```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

***

### Carta: CONDITION\_SPECIFY\_SUPPLIER\_TYPE

#### Scopo

Specifica/verifica il tipo di fornitore

#### Tipi di Fornitore

```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

#### Come Funziona

```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

***

## Esempi di Flussi Decisionali

### Flusso 1: Elaborazione Basata sullo Stato

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

### Flusso 2: Elaborazione Basata sul Fornitore

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

### Flusso 3: Basato sull'Importo con Verifica della Data

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

## Confronto tra le Condition Card

| Carta                                        | Verifica        | Operatore     | Uso               |
| ------------------------------------------- | --------------- | ------------- | ----------------- |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT           | Document status | È/NON È   | Stage check       |
| CONDITION\_DOC\_STATUS\_IS\_ISNOT\_IN\_LIST | Status in list  | DENTRO/NON DENTRO   | Stati multipli |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT             | Document type   | È/NON È   | Type filtering    |
| CONDITION\_DOC\_TYPE\_IS\_ISNOT\_LIST       | Type in list    | DENTRO/NON DENTRO   | Multiple types    |
| CONDITION\_SUB\_ORG\_IS\_ISNOT              | Organizzazione    | È/NON È   | Controllo del dipartimento  |
| CONDITION\_USER\_IS\_ISNOT                  | Utente assegnato   | È/NON È   | User check        |
| CONDITION\_USER\_IS\_ISNOT\_IN\_LIST        | User in list    | DENTRO/NON DENTRO   | Utenti multipli    |
| CONDITION\_GROUP\_IS\_ISNOT                 | Gruppo assegnato  | È/NON È   | Group check       |
| CONDITION\_GROUP\_IS\_ISNOT\_IN\_LIST       | Group in list   | DENTRO/NON DENTRO   | Gruppi multipli   |
| CONDITION\_TIME\_IS\_ISNOT\_BETWEEN         | Date range      | TRA       | Finestra della data       |
| CONDITION\_TODAY\_IS\_ISNOT                 | La data di oggi    | È/NON È   | Oggi controlla       |
| CONDITION\_DECISION\_TREE\_DATA             | Ritorna il DT      | HA/NON HA | DT result check   |
| CONDITION\_CONTINUE\_CHANCE                 | Probabilità     | CHANCE        | Random gate       |
| CONDITION\_MODULE\_IS\_ISNOT\_ACTIVE        | Funzionalità abilitata | È/NON È   | Controllo delle funzionalità     |
| CONDITION\_HTTPS\_REQUEST\_STATUS           | Request result  | STATUS        | Response check    |
| CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT      | Supplier status | È/NON È   | Supplier check    |

***

## Best Practice per le Condizioni

✅ **Fai:**

* Usa condizioni specifiche
* Testa la logica con dati di esempio
* Ordina le condizioni in modo logico
* Predisponi un piano di riserva per tutti i percorsi
* Documenta la logica complessa

❌ **Non Fare:**

* Creare condizioni circolari (A se B, B se A)
* Rendere le condizioni troppo complesse
* Dimenticare i casi limite
* Presumere che un campo abbia sempre un valore
* Creare condizioni impossibili

***

## Combinare Più Condizioni

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

## Card Correlate

* **CONDITION\_DOC\_FIELD\_CONTAINS** - Verifica del contenuto del campo
* **CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES** - Confronto tra campi
* **CONDITION\_CHECKBOX\_IS** - Verifica della checkbox

<!-- workflow-card-complete-example-20261021 condition_purchase_order_import -->

### Esempio di trigger di importazione di ordini di acquisto

**Configurazione:** In Quando selezionare l'evento di importazione del nuovo ordine di acquisto (`wf_new_purchase_order`) e lasciare deselezionato l'evento di aggiornamento (`wf_updated_purchase_order`). Configura le azioni successive per questo contesto di flusso di lavoro indipendente dal documento.

**Risultato atteso e controesempio:** Un'esecuzione avviata da un ordine di acquisto appena importato soddisfa questa condizione. Una corsa avviata solo da un aggiornamento non lo fa. La selezione di entrambi gli eventi consente l'esecuzione di entrambi gli eventi. Ciò controlla le informazioni sull'attivazione del flusso di lavoro, non se una fattura contiene attualmente un numero di ordine di acquisto.

Questa è una configurazione di test illustrativa e il risultato atteso; non è stato eseguito. Utilizza dati e destinatari configurati nella tua organizzazione di test.

<!-- workflow-card-complete-example-20261021 condition_supplier_status_is_isnot -->

### Esempio di trigger di modifica dello stato del fornitore

**Configurazione:** In Quando scegli l'operatore `is` e uno stato target effettivamente offerto nella tua organizzazione. Chiama lo stato selezionato A in questo esempio. Lasciare deselezionato un altro stato disponibile B.

**Risultato atteso e controesempio:** La condizione è vera per un evento di cambiamento di stato del fornitore il cui nuovo stato è A; è falso per un evento il cui nuovo stato è B. Con l'operatore `is not`, questi risultati si invertono. Si tratta di un trigger di evento basato sulle informazioni di esecuzione del flusso di lavoro, non di un controllo generale dello stato del fornitore su una fattura. Conferma l'evento effettivo e lo stato selezionato nel registro.

Questa è una configurazione di test illustrativa e il risultato atteso; non è stato eseguito. Utilizza dati e destinatari configurati nella tua organizzazione di test.

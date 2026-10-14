# Condition Cards - Complete Guide

Le schede di condizione di questa pagina vanno nei gruppi **When** e **And** del Generatore di workflow — decidono se eseguire le azioni Then:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Le schede di condizione vengono aggiunte ai gruppi <strong>When</strong> e <strong>And</strong> tramite <strong>Add Card</strong>.</p></figcaption></figure>

**Copre:** le 31 condition card rimanenti

---

## 📌 Informazioni sulla Versione

**Stato:** la maggior parte delle condition card è stabile con strutture a versione singola o doppia
**Schema delle Versioni:** la maggior parte segue lo schema v1 → v2 (aggiunta del supporto i18n)
**Esempio Multi-Versione:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Nota:** alcune condition card di confronto PO hanno 4-5 versioni (vedi la Guida al PO Matching per i dettagli)

📖 [Cronologia Completa delle Versioni](../../../changelog/release.md) | [Database delle Versioni delle Card](../../../../DocFlow/docs/card_version.md) | [Guida al PO Matching](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Condizioni su Stato del Documento

## Card: CONDITION_DOC_STATUS_IS_ISNOT / Document Status Check

### Scopo
Verifica se il documento ha uno stato specifico

### Quando Usarla
- Prima dell'approvazione
- In una fase specifica del workflow
- Instradamento basato sullo stato

### Tipi di Stato del Documento
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

### Come Funziona
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Esempio
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

## Card: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Scopo
Verifica se lo stato corrisponde a uno qualsiasi di un elenco

### Quando Usarla
- Più stati validi
- Logica OR per lo stato

### Esempio
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Card: CONDITION_DOC_TYPE_IS_ISNOT / Document Type Check

### Scopo
Verifica se il documento è di un tipo specifico

### Tipi di Documento
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

### Come Funziona
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Esempio
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Card: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Scopo
Verifica se il tipo corrisponde a uno qualsiasi di un elenco

### Esempio
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Card: CONDITION_SUB_ORG_IS_ISNOT / Sub-Organization Check

### Scopo
Verifica quale organizzazione/reparto è proprietario del documento

### Organizzazioni
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Esempio
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Card: CONDITION_PURCHASE_ORDER_IMPORT / PO Import Check

### Scopo
Verifica se il PO è appena importato o già esistente

### Come Funziona
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Quando Usarla
- Gestione diversa per i nuovi PO
- Saltare la convalida per i PO noti
- Tracciare la prima volta che si vede un fornitore

---

# Condizioni sull'Assegnatario

## Card: CONDITION_USER_IS_ISNOT / User Check

### Scopo
Verifica se il documento è assegnato a un utente specifico

### Come Funziona
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Esempio
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Card: CONDITION_USER_IS_ISNOT_IN_LIST

### Scopo
Verifica se è assegnato a uno qualsiasi degli utenti di un elenco

### Esempio
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Card: CONDITION_GROUP_IS_ISNOT / Group Check

### Scopo
Verifica se è assegnato a un gruppo specifico

### Esempio
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Card: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Scopo
Verifica se è assegnato a uno qualsiasi dei gruppi di un elenco

### Esempio
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Condizioni su Data e Ora

## Card: CONDITION_TIME_IS_ISNOT_BETWEEN / Date Range Check

### Scopo
Verifica se una data è compresa tra due date

### Come Funziona
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Calcolo
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Quando Usarla
- Verificare se si è in un periodo fiscale
- Verificare se si è entro una scadenza
- Verificare se si è in un periodo promozionale

### Esempio
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

## Card: CONDITION_TODAY_IS_ISNOT / Today Check

### Scopo
Verifica se la data odierna corrisponde ai criteri

### Come Funziona
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Casi d'Uso
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Esempio
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Card: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Scopo
Verifica se la data di consegna corrisponde alle date di consegna approvate nel calendario

### Come Funziona
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

### Quando Usarla
- Verificare che la consegna corrisponda alle date concordate
- Confrontare con il calendario delle festività
- Convalidare rispetto alle date contrattuali

### Esempio
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Condizioni Logiche

## Card: CONDITION_DECISION_TREE_DATA / Decision Table Returns

### Scopo
Verifica se la decision table ha valori restituiti

### Come Funziona
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Quando Usarla
- Prima di utilizzare i risultati della decision table
- Come condizione di filtro
- Per verificare se l'instradamento è disponibile

### Esempio
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Card: CONDITION_CONTINUE_CHANCE / Random Probability

### Scopo
Prosegue con una probabilità specificata

### Come Funziona
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Quando Usarla
- Workflow di A/B testing
- Campionamento dei documenti
- Controlli qualità casuali

### Esempio
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Calcolo
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Card: CONDITION_MODULE_IS_ISNOT_ACTIVE / Feature Check

### Scopo
Verifica se un modulo/funzionalità specifica è abilitato

### Moduli
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Come Funziona
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Quando Usarla
- Workflow dipendenti da funzionalità
- Elaborazione opzionale
- Verificare se una funzionalità in licenza è attiva

---

## Card: CONDITION_HTTPS_REQUEST_STATUS / Request Result Check

### Scopo
Verifica se la richiesta HTTPS è andata a buon fine

### Codici di Stato
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Come Funziona
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

### Esempio
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Supplier Status Check

### Scopo
Verifica lo stato del fornitore nel sistema

### Stati del Fornitore
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Come Funziona
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Esempio
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Card: CONDITION_SPECIFY_SUPPLIER_TYPE

### Scopo
Specifica/verifica il tipo di fornitore

### Tipi di Fornitore
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Come Funziona
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Esempi di Flussi Decisionali

## Flusso 1: Elaborazione Basata sullo Stato
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

## Flusso 2: Elaborazione Basata sul Fornitore
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

## Flusso 3: Basato sull'Importo con Verifica della Data
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

# Confronto tra le Condition Card

| Card | Verifica | Operatore | Uso |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Document status | IS / IS NOT | Stage check |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Status in list | IN / NOT IN | Multiple statuses |
| CONDITION_DOC_TYPE_IS_ISNOT | Document type | IS / IS NOT | Type filtering |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Type in list | IN / NOT IN | Multiple types |
| CONDITION_SUB_ORG_IS_ISNOT | Organization | IS / IS NOT | Department check |
| CONDITION_USER_IS_ISNOT | Assigned user | IS / IS NOT | User check |
| CONDITION_USER_IS_ISNOT_IN_LIST | User in list | IN / NOT IN | Multiple users |
| CONDITION_GROUP_IS_ISNOT | Assigned group | IS / IS NOT | Group check |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Group in list | IN / NOT IN | Multiple groups |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Date range | BETWEEN | Date window |
| CONDITION_TODAY_IS_ISNOT | Today's date | IS / IS NOT | Today check |
| CONDITION_DECISION_TREE_DATA | DT returns | HAS / HAS NOT | DT result check |
| CONDITION_CONTINUE_CHANCE | Probability | CHANCE | Random gate |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Feature enabled | IS / IS NOT | Feature check |
| CONDITION_HTTPS_REQUEST_STATUS | Request result | STATUS | Response check |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Supplier status | IS / IS NOT | Supplier check |

---

# Best Practice per le Condizioni

✅ **Fai:**
- Usa condizioni specifiche
- Testa la logica con dati di esempio
- Ordina le condizioni in modo logico
- Predisponi un piano di riserva per tutti i percorsi
- Documenta la logica complessa

❌ **Non Fare:**
- Creare condizioni circolari (A se B, B se A)
- Rendere le condizioni troppo complesse
- Dimenticare i casi limite
- Presumere che un campo abbia sempre un valore
- Creare condizioni impossibili

---

# Combinare Più Condizioni

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

# Card Correlate

- **CONDITION_DOC_FIELD_CONTAINS** - Verifica del contenuto del campo
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Confronto tra campi
- **CONDITION_CHECKBOX_IS** - Verifica della checkbox

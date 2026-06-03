# Padrão de Correspondência de Encomendas (PO Matching)

**Tipo de padrão:** Validação e comparação
**Complexidade:** Média-Alta
**Configuração estimada:** 60–90 minutos
**Casos de uso comuns:** Correspondência de três vias, validação de faturas, verificação de desvios, gestão de tolerâncias

---

Este padrão é construído no **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clique em **Add Card** e abra a categoria **Compare with Purchase Order** — contém todas as cartas de correspondência utilizadas por este padrão (cartas de comparação de preço, quantidade, tolerância e posições):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card com as cartas Compare with Purchase Order"><figcaption><p>A categoria <strong>Compare with Purchase Order</strong> — cartas de correspondência de preço, quantidade, tolerância e posições utilizadas ao longo de todo este padrão.</p></figcaption></figure>

---

## Visão geral do padrão

Este padrão demonstra como implementar workflows abrangentes de correspondência de encomendas (PO Matching) no DocBits. A correspondência de encomendas é um processo de controlo crítico que compara os dados da fatura com os dados da encomenda para detetar discrepâncias antes da aprovação do pagamento.

**O que este padrão faz:**
1. Obtém os dados da encomenda com base no número de PO da fatura
2. Compara as posições da fatura com as posições da encomenda
3. Calcula os desvios (preço, quantidade, totais)
4. Aplica regras de tolerância
5. Encaminha para aprovação ou escalonamento com base nos resultados da correspondência
6. Acompanha o histórico de correspondências e as exceções

---

## Quando utilizar este padrão

Utilize este padrão quando precisar de:
- ✅ Validar faturas contra encomendas
- ✅ Detetar erros de preços antes do pagamento
- ✅ Identificar discrepâncias de quantidade
- ✅ Aplicar controlos de aprovisionamento
- ✅ Evitar pagamentos em duplicado
- ✅ Automatizar a correspondência de três vias
- ✅ Reduzir o esforço de revisão manual de faturas

**Não utilize este padrão quando:**
- ❌ não existir encomenda para a fatura (faturas sem PO)
- ❌ os dados da encomenda não estiverem disponíveis no DocBits
- ❌ se preferir a revisão manual à automatização
- ❌ a correspondência de encomendas não for exigida pela política de negócio

---

## Compreender a correspondência de encomendas

### A correspondência de três vias

**Controlo de aprovisionamento clássico:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**Implementação no DocBits (correspondência de duas vias):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Fórmulas de cálculo de desvios

### Desvio do preço unitário

**Fórmula:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Exemplo:**
```
PO Unit Price:       €100.00
Invoice Unit Price:  €103.00

Variance = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerance: 5%
Result: 3% ≤ 5% → PASS ✅
```

---

### Desvio da quantidade

**Fórmula:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Exemplo:**
```
PO Quantity:        100 units
Invoice Quantity:   98 units

Variance = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerance: 10%
Result: 2% ≤ 10% → PASS ✅
```

---

### Desvio do montante total

**Fórmula:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Exemplo:**
```
PO Total:       €10,000.00
Invoice Total:  €10,450.00

Variance = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4.5%

Tolerance: 5%
Result: 4.5% ≤ 5% → PASS ✅
```

---

## Exemplo completo de workflow

### Cenário: Validação de faturas com encaminhamento baseado em tolerâncias

**Requisito de negócio:**
- Todas as faturas com referência de PO têm de ser validadas
- Tolerância do desvio de preço: 5 %
- Tolerância do desvio de quantidade: 10 %
- Tolerância do desvio do montante total: 3 %
- Dentro da tolerância: Aprovação automática
- Fora da tolerância: Criar tarefa de revisão
- Encomenda em falta: Escalar para as Compras

**Cartas de workflow utilizadas:**
1. CONDITION_DOC_FIELD_EXISTS – Verificar se o número de PO está presente
2. PURCHASE_ORDER_FULL_MATCH – Tentar correspondência total
3. CONDITION_DOC_TO_PO_UNIT_PRICE – Verificar o desvio de preço
4. CONDITION_DOC_TO_PO_QUANTITY – Verificar o desvio de quantidade
5. CONDITION_DOC_TO_PO_TAX_LINES – Verificar o alinhamento fiscal
6. ACTION_SET_FIELD_TO_TEXT – Armazenar os resultados da correspondência
7. tasks_create – Criar tarefas de revisão
8. ACTION_SEND_EMAIL_TO_GROUPS – Enviar notificações

---

## Implementação passo a passo

### Passo 1: Verificar a referência de PO

**Carta:** CONDITION_DOC_FIELD_EXISTS ou CONDITION_DOC_FIELD_CONTAINS

**Configuração:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Lógica:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Referência de guia:** [Guia de cartas de condição](../and/condition-cards-complete-guide.md)

---

### Passo 2: Obter os dados da encomenda

**Automático no DocBits:**
- O sistema consulta a encomenda através do campo PO_Number
- Obtém as posições da encomenda
- Disponibiliza os dados para comparação

**Configuração manual (se necessário):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Passo 3: Verificar a correspondência total

**Carta:** PURCHASE_ORDER_FULL_MATCH

**Objetivo:** Verificação rápida de que tudo corresponde na perfeição

**Configuração:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Lógica:**
```
IF Full Match = TRUE:
  → Set "PO_Match_Status" = "FULL MATCH"
  → Auto-approve document
  → Skip detailed checks
  → END ✅

IF Full Match = FALSE:
  → Continue to detailed variance checks
  → Identify specific variances
```

**Resultado:**
- **TRUE**: Correspondência perfeita, aprovação automática
- **FALSE**: Avançar para as verificações detalhadas

---

### Passo 4: Verificar o desvio do preço unitário

**Carta:** CONDITION_DOC_TO_PO_UNIT_PRICE (recomenda-se a v5)

**Configuração:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Passo a passo:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Exemplo de cálculo:**
```
Line Item 1:
  Product: ABC123
  Invoice Price: €52.00
  PO Price: €50.00
  Variance = |52-50|/50 × 100 = 4%
  Tolerance: 5%
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Price: €120.00
  PO Price: €100.00
  Variance = |120-100|/100 × 100 = 20%
  Tolerance: 5%
  Result: FAIL ❌

Overall Result: FAIL (one or more items failed)
```

**Referência de guia:** [Guia completo de PO Matching – Preço unitário](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Passo 5: Verificar o desvio da quantidade

**Carta:** CONDITION_DOC_TO_PO_QUANTITY

**Configuração:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Lógica:**
```
For each line item:
  1. Get Invoice Quantity
  2. Get PO Quantity
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 10%?
  5. Special rules:
     - Under-delivery: Allow within tolerance
     - Over-delivery: Reject (or apply stricter tolerance)
```

**Exemplo:**
```
Line Item 1:
  Product: ABC123
  Invoice Qty: 98 units
  PO Qty: 100 units
  Variance = |98-100|/100 × 100 = 2%
  Under-delivery: 2% (within 10% tolerance)
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Qty: 115 units
  PO Qty: 100 units
  Variance = |115-100|/100 × 100 = 15%
  Over-delivery: 15% (exceeds 10% tolerance)
  Result: FAIL ❌ (Escalate)
```

**Referência de guia:** [Guia completo de PO Matching – Quantidade](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Passo 6: Verificar o alinhamento das linhas de imposto

**Carta:** CONDITION_DOC_TO_PO_TAX_LINES

**Configuração:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Validação:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Exemplo:**
```
Invoice:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

PO:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

Result: Tax alignment PASS ✅
```

---

### Passo 7: Armazenar os resultados da correspondência

**Carta:** ACTION_SET_FIELD_TO_TEXT (várias instâncias)

**Configuração:**

**Campo 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Campo 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Campo 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Campo 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Referência de guia:** [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md)

---

### Passo 8: Encaminhar com base nos resultados da correspondência

**Cenário A: Correspondência perfeita (correspondência total)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Cenário B: Dentro da tolerância**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Cenário C: Fora da tolerância (ligeira)**
```
IF Variance < 15% (minor exceptions):
  1. Set Match_Status = "REVIEW REQUIRED"
  2. Create Task: "Review PO Variance"
     - Assign to: Accounts Payable Officer
     - Priority: Medium
     - Deadline: 3 days
  3. Send email with variance details
  4. Wait for task completion
  5. IF Approved: Continue processing
     IF Rejected: Return to supplier
```

**Cenário D: Fora da tolerância (significativa)**
```
IF Variance ≥ 15% (major exceptions):
  1. Set Match_Status = "ESCALATION REQUIRED"
  2. Create Task: "URGENT: Major PO Variance"
     - Assign to: Procurement Manager
     - Priority: High
     - Deadline: 1 day
  3. Send urgent email to:
     - Procurement Manager
     - Finance Manager
     - Supplier contact
  4. Block document from processing
  5. Wait for resolution
```

**Cenário E: Encomenda em falta ou sem correspondência**
```
IF PO not found OR no items match:
  1. Set Match_Status = "NO MATCH"
  2. Create Task: "PO Not Found"
     - Assign to: Procurement Team
     - Priority: High
  3. Send email to procurement
  4. Block document
  5. Request PO creation or correction
```

---

## Diagrama completo de workflow

```
INVOICE ARRIVES
│
├─ CHECK: Does invoice have PO number?
│  │
│  ├─ NO PO NUMBER ❌
│  │  │
│  │  ├─ Set Match_Status = "NO PO"
│  │  ├─ Route to Non-PO workflow
│  │  └─ Create manual review task
│  │     → END (Non-PO Invoice)
│  │
│  └─ PO NUMBER EXISTS ✅
│     │
│     ├─ RETRIEVE PO DATA
│     │  - Lookup PO by PO_Number
│     │  - Get PO line items
│     │  - Get PO totals
│     │  │
│     │  ├─ PO FOUND ✅
│     │  │  │
│     │  │  ├─ STEP 1: Check Full Match
│     │  │  │  Card: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ FULL MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Set Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Approve
│     │  │  │  │  └─ Export to ERP
│     │  │  │  │     → END (Perfect Match)
│     │  │  │  │
│     │  │  │  └─ NO FULL MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STEP 2: Check Unit Price Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerance: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRICE VARIANCE ≤ 5% ✅
│     │  │  │     │  │  Store variance: 3.2% (example)
│     │  │  │     │  │  Price Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRICE VARIANCE > 5% ❌
│     │  │  │     │     Store variance: 12.5% (example)
│     │  │  │     │     Price Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 3: Check Quantity Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerance: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ QUANTITY VARIANCE ≤ 10% ✅
│     │  │  │     │  │  Store variance: 2.0% (example)
│     │  │  │     │  │  Quantity Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ QUANTITY VARIANCE > 10% ❌
│     │  │  │     │     Store variance: 15.0% (example)
│     │  │  │     │     Quantity Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 4: Check Tax Lines
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ TAX ALIGNED ✅
│     │  │  │     │  │  Tax Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ TAX MISMATCH ❌
│     │  │  │     │     Tax Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ EVALUATE RESULTS
│     │  │  │     │  │
│     │  │  │     │  ├─ ALL CHECKS PASS ✅
│     │  │  │     │  │  (Within tolerance)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variance details
│     │  │  │     │  │  ├─ Auto-Approve
│     │  │  │     │  │  └─ Export to ERP
│     │  │  │     │  │     → END (Approved with Variance)
│     │  │  │     │  │
│     │  │  │     │  ├─ MINOR FAILURES (Variance < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Create Review Task
│     │  │  │     │  │  │  - Assign to: AP Officer
│     │  │  │     │  │  │  - Priority: Medium
│     │  │  │     │  │  │  - Deadline: 3 days
│     │  │  │     │  │  ├─ Send email with details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WAIT FOR TASK COMPLETION
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TASK APPROVED ✅
│     │  │  │     │  │     │  Approve & Export
│     │  │  │     │  │     │  → END (Manual Approval)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TASK REJECTED ❌
│     │  │  │     │  │        Reject & Return to Supplier
│     │  │  │     │  │        → END (Rejected)
│     │  │  │     │  │
│     │  │  │     │  └─ MAJOR FAILURES (Variance ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Set Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Create Urgent Task
│     │  │  │     │     │  - Assign to: Procurement Manager
│     │  │  │     │     │  - Priority: High
│     │  │  │     │     │  - Deadline: 1 day
│     │  │  │     │     ├─ Send urgent emails to:
│     │  │  │     │     │  * Procurement Manager
│     │  │  │     │     │  * Finance Manager
│     │  │  │     │     │  * Supplier
│     │  │  │     │     ├─ Block document processing
│     │  │  │     │     │
│     │  │  │     │     └─ WAIT FOR RESOLUTION
│     │  │  │     │        → END (Pending Escalation)
│     │  │  │     │
│     │  │  │     └─ [Variance checks complete]
│     │  │  │
│     │  │  └─ [Full match check complete]
│     │  │
│     │  └─ PO NOT FOUND ❌
│     │     │
│     │     ├─ Set Match_Status = "PO NOT FOUND"
│     │     ├─ Create Task: "Missing PO"
│     │     │  - Assign to: Procurement Team
│     │     │  - Priority: High
│     │     ├─ Send email to procurement
│     │     └─ Block document
│     │        → END (Missing PO)
│     │
│     └─ [PO retrieval complete]
│
└─ [PO check complete]
```

---

## Modelos de configuração

### Modelo 1: Correspondência de encomendas padrão (conservadora)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**Utilização:** Ambiente de controlo rigoroso, baixa tolerância a desvios

---

### Modelo 2: Correspondência de encomendas flexível (tolerante)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**Utilização:** Ambiente flexível, fornecedores de confiança, tolerância mais elevada

---

### Modelo 3: Correspondência apenas de preço

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**Utilização:** Quando só o preço importa e se esperam desvios de quantidade

---

## Cenários avançados

### Cenário 1: Tratamento de entregas parciais

**Desafio:** Fatura de uma entrega parcial de uma encomenda

**Solução:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Implementação:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Cenário 2: Correspondência de encomendas com várias moedas

**Desafio:** A moeda da fatura difere da moeda da encomenda

**Solução:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Implementação:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Cenário 3: Encomenda-quadro / Acordo-quadro

**Desafio:** Várias faturas contra uma única encomenda

**Solução:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Implementação:**
```
IF PO_Type = "Blanket":
  Calculate: Total_Invoiced_To_Date
  Check: Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF Within limit:
    Approve invoice
    Update: Remaining_PO_Value
  ELSE:
    Escalate: "Blanket PO limit exceeded"
```

---

## Tratamento de erros e casos especiais

### Caso especial 1: Posição em falta na fatura

**Problema:** A fatura contém uma posição que não está na encomenda

**Solução:**
```
1. Identify unmatched line items
2. Calculate: Unmatched_Amount
3. IF Unmatched_Amount < €100 (threshold):
     Create review task (minor issue)
   ELSE:
     Escalate immediately (major issue)
4. Store unmatched item details
5. Flag: "Additional_Items_Present"
```

---

### Caso especial 2: Encomenda fechada, mas chega uma fatura

**Problema:** Encomenda já fechada, fatura recebida em atraso

**Solução:**
```
1. Check: PO_Status = "CLOSED"
2. Check: Invoice_Date vs PO_Close_Date
3. IF Invoice within 30 days of close:
     Reopen PO temporarily
     Process invoice
     Close PO again
   ELSE:
     Create task: "Late Invoice for Closed PO"
     Assign to procurement
     Manual decision required
```

---

### Caso especial 3: Várias encomendas numa fatura

**Problema:** A fatura faz referência a várias encomendas

**Solução:**
```
1. Parse invoice for multiple PO numbers
2. For each PO:
     Retrieve PO data
     Match respective line items
3. Aggregate match results
4. Overall match = ALL individual POs must match
5. Report on each PO separately
```

---

## Sugestões de desempenho

✅ **Boas práticas:**
- Fazer caching dos dados das encomendas para reduzir consultas
- Definir tolerâncias adequadas (nem demasiado rigorosas, nem demasiado tolerantes)
- Verificar primeiro a correspondência total (mais rápido)
- Registar todos os cálculos de desvios
- Rever as definições de tolerância trimestralmente
- Monitorizar as taxas de aprovação automática
- Acompanhar os motivos de desvio mais frequentes

❌ **Evitar:**
- Tolerância zero (demasiado rigorosa, demasiadas revisões manuais)
- Tolerância extremamente elevada (subverte o objetivo)
- Ignorar desvios sistemáticas
- Não acompanhar as tendências de desvios
- Processar sem encomenda (quando exigido)

---

## Monitorização e relatórios

### Indicadores-chave a acompanhar

1. **Taxa de correspondência:**
   - Correspondência total: X %
   - Dentro da tolerância: Y %
   - Fora da tolerância: Z %

2. **Análise de desvios:**
   - Desvio média de preço
   - Desvio média de quantidade
   - Motivos de desvio mais frequentes

3. **Eficiência do processamento:**
   - Taxa de aprovação automática
   - Taxa de revisão manual
   - Tempo médio de revisão

4. **Desempenho dos fornecedores:**
   - Desvioen por fornecedor
   - Taxa de correspondência por fornecedor
   - Fornecedores problemáticos

---

## Lista de verificação de testes

- [ ] Cenário de correspondência perfeita (correspondência total)
- [ ] Cenário dentro da tolerância (desvio ligeiro)
- [ ] Cenário fora da tolerância (desvio significativo)
- [ ] Cenário de encomenda em falta
- [ ] Cenário de número de PO incorreto
- [ ] Cenário de entrega parcial
- [ ] Cenário de entrega em excesso
- [ ] Cenário de desvio de moeda
- [ ] Cenário de várias encomendas
- [ ] Cenário de encomenda fechada
- [ ] Cenário de desvio de imposto
- [ ] Workflow de escalonamento
- [ ] Criação de tarefas
- [ ] Notificações por e-mail
- [ ] Atualizações de campos
- [ ] Exportação após aprovação

---

## Padrões relacionados

### Padrões que combinam bem:

- **[Padrão de Gestão de Tarefas](task-management-pattern.md)** – Criar tarefas de revisão para desvios
- **[Padrão de Lógica de Decisão](decision-logic-pattern.md)** – Encaminhamento complexo com base na magnitude do desvio
- **[Padrão de Integração de API](api-integration-pattern.md)** – Obter preços atuais para comparação
- **[Padrão de Transformação de Dados](data-transformation-pattern.md)** – Conversão de moeda e de unidades

---

## Guias relacionados

### Pré-requisitos
- [Guia completo de PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md) – Todas as cartas de correspondência de PO
- [Guia de cartas de condição](../and/condition-cards-complete-guide.md) – Lógica de condições
- [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md) – Operações de campos

### Cartas relacionadas
- **PURCHASE_ORDER_FULL_MATCH** – [Guia de PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** – [Guia de PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** – [Guia de PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** – [Guia de PO Matching](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** – [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md)

### Próximos passos
- Criar tarefas de revisão: [Padrão de Gestão de Tarefas](task-management-pattern.md)
- Adicionar notificações por e-mail: [Guia de e-mail](../then/action/send-email-groups-guide.md)
- Implementar encaminhamento complexo: [Padrão de Lógica de Decisão](decision-logic-pattern.md)

---

**Versão do padrão:** 1.0
**Última atualização:** 23 de outubro de 2025
**Dificuldade:** Média-Alta
**Tempo estimado:** 60–90 minutos
**Taxa de êxito:** Alta (com configuração correta)

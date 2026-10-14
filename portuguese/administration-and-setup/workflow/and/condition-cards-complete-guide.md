# Condition Cards - Complete Guide

Os cartões de condição desta página ficam nos grupos **When** e **And** do Construtor de fluxos de trabalho — decidem se as ações Then são executadas:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões de condição são adicionados aos grupos <strong>When</strong> e <strong>And</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

**Abrange:** 31 cartões de condição restantes

---

## 📌 Informações de versão

**Estado:** A maioria dos cartões de condição é estável, com estruturas de versão única ou dupla
**Padrão de versão:** A maioria segue o padrão v1 → v2 (adição de suporte de i18n)
**Exemplo multiversão:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Nota:** Alguns cartões de condição de comparação de PO têm 4-5 versões (consulte o PO Matching Guide para mais detalhes)

📖 [Complete Version History](../../../changelog/release.md) | [Card Version Database](../../../../DocFlow/docs/card_version.md) | [PO Matching Guide](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Condições de estado do documento

## Cartão: CONDITION_DOC_STATUS_IS_ISNOT / Document Status Check

### Objetivo
Verifica se o documento tem um estado específico

### Quando utilizar
- Antes de aprovar
- Numa fase específica do fluxo de trabalho
- Encaminhamento baseado no estado

### Tipos de estado do documento
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

### Como funciona
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Exemplo
```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

### Parâmetros
```
Operator: IS / IS NOT
Status: [Select status]
```

---

## Cartão: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Objetivo
Verifica se o estado corresponde a algum de uma lista

### Quando utilizar
- Vários estados válidos
- Lógica OR para o estado

### Exemplo
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Cartão: CONDITION_DOC_TYPE_IS_ISNOT / Document Type Check

### Objetivo
Verifica se o documento é de um tipo específico

### Tipos de documento
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

### Como funciona
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Exemplo
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Cartão: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Objetivo
Verifica se o tipo corresponde a algum de uma lista

### Exemplo
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Cartão: CONDITION_SUB_ORG_IS_ISNOT / Sub-Organization Check

### Objetivo
Verifica que organização/departamento é proprietário do documento

### Organizações
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Exemplo
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Cartão: CONDITION_PURCHASE_ORDER_IMPORT / PO Import Check

### Objetivo
Verifica se a PO foi recém-importada ou já existe

### Como funciona
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Quando utilizar
- Tratamento diferente para novas POs
- Ignorar a validação para POs conhecidas
- Acompanhar a primeira vez que se vê um fornecedor

---

# Condições de responsável (Assignee)

## Cartão: CONDITION_USER_IS_ISNOT / User Check

### Objetivo
Verifica se o documento está atribuído a um utilizador específico

### Como funciona
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Exemplo
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Cartão: CONDITION_USER_IS_ISNOT_IN_LIST

### Objetivo
Verifica se está atribuído a algum utilizador de uma lista

### Exemplo
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Cartão: CONDITION_GROUP_IS_ISNOT / Group Check

### Objetivo
Verifica se está atribuído a um grupo específico

### Exemplo
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Cartão: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Objetivo
Verifica se está atribuído a algum grupo de uma lista

### Exemplo
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Condições de data e hora

## Cartão: CONDITION_TIME_IS_ISNOT_BETWEEN / Date Range Check

### Objetivo
Verifica se uma data se situa entre duas datas

### Como funciona
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Cálculo
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Quando utilizar
- Verificar se está num período fiscal
- Verificar se está dentro de um prazo
- Verificar se está num período promocional

### Exemplo
```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

### Parâmetros
```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

---

## Cartão: CONDITION_TODAY_IS_ISNOT / Today Check

### Objetivo
Verifica se a data de hoje cumpre determinados critérios

### Como funciona
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Casos de utilização
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Exemplo
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Cartão: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Objetivo
Verifica se a data de entrega corresponde às datas de entrega aprovadas no calendário

### Como funciona
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

### Quando utilizar
- Verificar se a entrega corresponde às datas acordadas
- Confrontar com o calendário de feriados
- Validar com base nas datas contratadas

### Exemplo
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Condições de lógica

## Cartão: CONDITION_DECISION_TREE_DATA / Decision Table Returns

### Objetivo
Verifica se a tabela de decisão tem valores de retorno

### Como funciona
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Quando utilizar
- Antes de utilizar os resultados da tabela de decisão
- Como condição de barreira
- Para verificar se o encaminhamento está disponível

### Exemplo
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Cartão: CONDITION_CONTINUE_CHANCE / Random Probability

### Objetivo
Continua com uma probabilidade especificada

### Como funciona
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Quando utilizar
- Fluxos de trabalho de testes A/B
- Amostragem de documentos
- Verificações de qualidade aleatórias

### Exemplo
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Cálculo
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Cartão: CONDITION_MODULE_IS_ISNOT_ACTIVE / Feature Check

### Objetivo
Verifica se um módulo/funcionalidade específico está ativado

### Módulos
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Como funciona
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Quando utilizar
- Fluxos de trabalho dependentes de funcionalidades
- Processamento opcional
- Verificar se uma funcionalidade licenciada está ativa

---

## Cartão: CONDITION_HTTPS_REQUEST_STATUS / Request Result Check

### Objetivo
Verifica se um pedido HTTPS foi bem-sucedido

### Códigos de estado
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Como funciona
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

### Exemplo
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Cartão: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Supplier Status Check

### Objetivo
Verifica o estado do fornecedor no sistema

### Estados de fornecedor
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Como funciona
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Exemplo
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Cartão: CONDITION_SPECIFY_SUPPLIER_TYPE

### Objetivo
Especifica/verifica o tipo de fornecedor

### Tipos de fornecedor
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Como funciona
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Exemplos de fluxos de decisão

## Fluxo 1: Processamento baseado no estado
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

## Fluxo 2: Processamento baseado no fornecedor
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

## Fluxo 3: Baseado no montante com verificação de data
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

# Comparação de cartões de condição

| Cartão | Verifica | Operador | Utilização |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Estado do documento | IS / IS NOT | Verificação de fase |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Estado numa lista | IN / NOT IN | Vários estados |
| CONDITION_DOC_TYPE_IS_ISNOT | Tipo de documento | IS / IS NOT | Filtragem por tipo |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Tipo numa lista | IN / NOT IN | Vários tipos |
| CONDITION_SUB_ORG_IS_ISNOT | Organização | IS / IS NOT | Verificação de departamento |
| CONDITION_USER_IS_ISNOT | Utilizador atribuído | IS / IS NOT | Verificação de utilizador |
| CONDITION_USER_IS_ISNOT_IN_LIST | Utilizador numa lista | IN / NOT IN | Vários utilizadores |
| CONDITION_GROUP_IS_ISNOT | Grupo atribuído | IS / IS NOT | Verificação de grupo |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Grupo numa lista | IN / NOT IN | Vários grupos |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Intervalo de datas | BETWEEN | Janela de datas |
| CONDITION_TODAY_IS_ISNOT | Data de hoje | IS / IS NOT | Verificação de hoje |
| CONDITION_DECISION_TREE_DATA | Retornos da DT | HAS / HAS NOT | Verificação de resultado da DT |
| CONDITION_CONTINUE_CHANCE | Probabilidade | CHANCE | Barreira aleatória |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Funcionalidade ativada | IS / IS NOT | Verificação de funcionalidade |
| CONDITION_HTTPS_REQUEST_STATUS | Resultado do pedido | STATUS | Verificação de resposta |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Estado do fornecedor | IS / IS NOT | Verificação de fornecedor |

---

# Boas práticas para condições

✅ **Faça:**
- Utilize condições específicas
- Teste a lógica com amostras
- Ordene as condições de forma lógica
- Tenha uma alternativa para todos os caminhos
- Documente a lógica complexa

❌ **Não faça:**
- Criar condições circulares (A se B, B se A)
- Tornar as condições demasiado complexas
- Esquecer os casos extremos
- Assumir que um campo tem sempre um valor
- Criar condições impossíveis

---

# Combinar várias condições

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

# Cartões relacionados

- **CONDITION_DOC_FIELD_CONTAINS** - Verificação do conteúdo de um campo
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Comparação de campos
- **CONDITION_CHECKBOX_IS** - Verificação de caixa de verificação

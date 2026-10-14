# Padrão de Lógica de Decisão

**Tipo de padrão:** Encaminhamento condicional e lógica
**Complexidade:** Média
**Configuração estimada:** 30–45 minutos
**Casos de uso comuns:** Encaminhamento de múltiplos caminhos, processamento condicional, árvores de decisão, implementação de regras de negócio

---

Este padrão é construído no **Workflow Builder** (Workflow Dashboard → Workflow List → Add Workflow). Clique em **Add Card** e abra a categoria **Logic** — contém as cartas de condição e de ramificação que controlam a árvore de decisão e que combina com o grupo **And** para avaliar várias condições:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Biblioteca Add Card no Workflow Builder, agrupada por categoria"><figcaption><p>A biblioteca <strong>Add Card</strong> — as cartas de condição e de ramificação encontram-se na categoria <strong>Logic</strong>.</p></figcaption></figure>

---

## Visão geral do padrão

Este padrão demonstra como implementar lógica de decisão complexa em workflows do DocBits. Com cartas de condição, encaminha documentos com base em atributos do documento, valores de campo e regras de negócio através de diferentes caminhos de processamento.

**O que este padrão faz:**
1. Avalia várias condições em sequência ou em paralelo
2. Encaminha documentos por diferentes caminhos com base em condições
3. Implementa regras de negócio e políticas
4. Trata árvores de decisão complexas
5. Combina vários critérios para decisões de encaminhamento

---

## Quando utilizar este padrão

Utilize este padrão quando precisar de:
- ✅ Encaminhar documentos por limiares de valor
- ✅ Aplicar regras diferentes a tipos de documento diferentes
- ✅ Implementar lógica de aprovação em vários níveis
- ✅ Tratar políticas de negócio complexas
- ✅ Criar encaminhamento dinâmico com base em múltiplos critérios
- ✅ Implementar lógica de tratamento de exceções
- ✅ Criar matrizes de aprovação

**Não utilize este padrão quando:**
- ❌ um workflow linear simples for suficiente
- ❌ todos os documentos seguirem o mesmo caminho
- ❌ não for necessário processamento condicional

---

## Tipos de lógica de decisão

### 1. Lógica IF-THEN simples

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Exemplo:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Vários critérios (lógica E)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Exemplo:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Critérios alternativos (lógica OU)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Exemplo:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. Árvore de decisão aninhada

```
IF condition1:
  IF condition2:
    → Action A
  ELSE:
    → Action B
ELSE:
  IF condition3:
    → Action C
  ELSE:
    → Action D
```

**Exemplo:**
```
IF Document_Type = "Invoice":
  IF Amount > €10,000:
    → High-value invoice workflow
  ELSE:
    → Standard invoice workflow
ELSE IF Document_Type = "Credit Note":
  IF Amount > €5,000:
    → High-value credit workflow
  ELSE:
    → Standard credit workflow
```

---

## Exemplo completo de workflow

### Cenário: Matriz de aprovação de faturas

**Regras de negócio:**
1. Montante < 1.000 €: Aprovação automática
2. Montante 1.000–10.000 €: Aprovação pela Direção
3. Montante > 10.000 € E novo fornecedor: Aprovação por Diretor + CFO
4. Montante > 10.000 € E fornecedor existente: Apenas aprovação pelo Diretor
5. Qualquer montante com discrepância de PO: Primeiro aprovação pelas Compras
6. Faturas urgentes (assinaladas): Workflow acelerado

**Implementação:**

```
STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = HIGH
    → 1-day deadline

STEP 3: Amount-Based Routing (if not urgent)
  IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount ≥ €10,000:
    CHECK Supplier Status:
      IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → After approval, create task for CFO (Task 2)
        → Priority: High
        → Deadline: 2 days each

      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days
```

---

## Implementação passo a passo

### Passo 1: Definir as cartas de condição

**Condição 1: Limiar de valor**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Condição 2: Verificação do tipo de documento**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Condição 3: Estado do fornecedor**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Condição 4: Verificação de novo fornecedor**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Referência de guia:** [Guia completo de cartas de condição](../and/condition-cards-complete-guide.md)

---

### Passo 2: Construir a árvore de decisão

**Nível 1: Tipo de documento**
```
Workflow: "Invoice Processing"

IF Document_Type = "Invoice":
  → Continue to Level 2

ELSE IF Document_Type = "Credit Note":
  → Branch to "Credit Note Processing"

ELSE IF Document_Type = "Receipt":
  → Branch to "Receipt Processing"

ELSE:
  → Route to "Unknown Document Type" handling
```

**Nível 2: Limiares de valor (para faturas)**
```
IF Amount < €1,000:
  → Branch to "Auto-Approve Path"

ELSE IF Amount < €10,000:
  → Branch to "Manager Approval Path"

ELSE IF Amount < €50,000:
  → Branch to "Director Approval Path"
  → Check Level 3 conditions

ELSE (Amount ≥ €50,000):
  → Branch to "Executive Approval Path"
  → Dual or triple approval required
```

**Nível 3: Análise do fornecedor (para faturas de valor elevado)**
```
IF Supplier_Status = "BLOCKED":
  → STOP processing
  → Create urgent escalation task
  → Notify procurement and finance

ELSE IF Supplier_Age < 180 days (New):
  → Additional approval required
  → Add CFO to approval chain
  → Enhanced verification

ELSE IF Supplier_Risk_Rating = "HIGH":
  → Additional checks required
  → Fraud detection review
  → Manager pre-approval

ELSE:
  → Standard high-value workflow
```

---

### Passo 3: Criar as ações de encaminhamento

**Caminho A: Aprovação automática (montante < 1.000 €)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Caminho B: Aprovação pela Direção (1.000–10.000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "1"
3. tasks_create:
   - Title: "Approve Invoice {{DOCUMENT_NUMBER}}"
   - Assign to: Department_Manager
   - Priority: Medium
   - Deadline: 3 days
4. Send email notification to manager
5. Wait for task completion
6. If approved: Export to ERP
7. If rejected: Return to supplier
```

**Caminho C: Aprovação pelo Diretor (10.000–50.000 €)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - After Task 1: Create Task 2: CFO approval
     - Dual approval required
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

**Caminho D: Aprovação pela administração (≥ 50.000 €)**
```
Actions:
1. Set field "Approval_Type" = "EXECUTIVE"
2. Set field "Approval_Level" = "3"
3. Sequential approvals:
   - Task 1: Finance Director
   - Task 2: CFO
   - Task 3: CEO (if > €100,000)
4. Priority: Urgent
5. Deadline: 1 day each
6. Send urgent notifications
7. Executive dashboard update
8. Wait for all approvals
9. If all approved: Export
10. If any rejected: Executive review meeting
```

---

## Padrões avançados de lógica de decisão

### Padrão 1: Encaminhamento baseado em pontuação

**Calcular uma pontuação de risco e encaminhar em conformidade:**

```
Risk Score Calculation:
  Score = 0

  IF Amount > €50,000: Score += 30
  IF Supplier_Age < 180 days: Score += 25
  IF PO_Variance > 10%: Score += 20
  IF Supplier_Country = "High Risk Country": Score += 15
  IF Payment_Terms < 30 days: Score += 10

  Total Score Range: 0-100

Routing:
  IF Score < 20: Auto-approve
  IF Score 20-50: Manager approval
  IF Score 51-75: Director approval
  IF Score > 75: Executive approval + fraud check
```

**Implementação:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Padrão 2: Matriz baseada no departamento

**Regras de aprovação diferentes por departamento:**

```
Department Matrix:

  IT Department:
    Amount < €5,000: IT Manager
    Amount ≥ €5,000: IT Director + CIO

  Finance Department:
    Amount < €10,000: Finance Manager
    Amount ≥ €10,000: CFO

  Operations Department:
    Amount < €3,000: Operations Manager
    Amount ≥ €3,000: COO

  General:
    Amount < €2,000: Department Manager
    Amount ≥ €2,000: Department Director
```

**Implementação:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Padrão 3: Lógica baseada no tempo

**Regras diferentes consoante o momento:**

```
Month-End Processing (Last 3 days of month):
  IF Today in last 3 days of month:
    - Priority: URGENT
    - Deadline: 1 day
    - Approver: On-duty finance manager
    - Expedited workflow
  ELSE:
    - Standard priority
    - Standard deadline
    - Standard workflow

Business Hours vs After Hours:
  IF Time between 9 AM - 5 PM:
    - Assign to current shift
  ELSE:
    - Queue for next business day
    - OR route to on-call approver

Fiscal Period:
  IF Document_Date in Current_Fiscal_Period:
    - Standard processing
  ELSE:
    - Flag as "Prior Period"
    - Require accounting approval
    - Additional checks
```

---

### Padrão 4: Encaminhamento baseado em exceções

**Encaminhar as exceções separadamente:**

```
Exception Detection:

  No Exception:
    → Standard workflow

  Minor Exception (Auto-fixable):
    → Auto-correct
    → Log correction
    → Continue standard workflow

  Medium Exception (Needs review):
    → Create review task
    → Flag document
    → After fix: Continue workflow

  Major Exception (Requires escalation):
    → Stop processing
    → Create urgent task
    → Notify multiple levels
    → Manual intervention required

Exception Types:
  - Missing required field
  - Invalid field value
  - PO mismatch
  - Duplicate invoice
  - Supplier mismatch
  - Amount discrepancy
```

---

## Diagrama completo de lógica de decisão

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Has Critical Exception? (Missing PO, Duplicate, etc.)
│  │  │
│  │  ├─ YES → Stop & Escalate
│  │  │        Create urgent task
│  │  │        Notify admin
│  │  │        → END (Exception Handling)
│  │  │
│  │  └─ NO → Continue to Level 2
│
├─ LEVEL 2: DOCUMENT TYPE
│  │
│  ├─ Type = Invoice?
│  │  └─ YES → Continue to Level 3
│  │
│  ├─ Type = Credit Note?
│  │  └─ YES → Branch to Credit Note workflow
│  │           → END (Credit Note Path)
│  │
│  └─ Other Type?
│     └─ YES → Branch to appropriate workflow
│              → END (Other Type Path)
│
├─ LEVEL 3: URGENCY CHECK (for Invoices)
│  │
│  ├─ Urgent Flag = TRUE?
│  │  │
│  │  ├─ YES → Expedited Workflow
│  │  │        Priority: URGENT
│  │  │        Deadline: 1 day
│  │  │        Assign to: Senior Approver
│  │  │        → END (Expedited Path)
│  │  │
│  │  └─ NO → Continue to Level 4
│
├─ LEVEL 4: AMOUNT THRESHOLDS
│  │
│  ├─ Amount < €1,000?
│  │  │
│  │  ├─ YES → AUTO-APPROVE PATH
│  │  │        Set Approval_Type = "AUTO"
│  │  │        Approve immediately
│  │  │        Export to ERP
│  │  │        → END (Auto-Approved)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €10,000?
│  │  │
│  │  ├─ YES → MANAGER APPROVAL PATH
│  │  │        Create task for Manager
│  │  │        Priority: Medium
│  │  │        Deadline: 3 days
│  │  │        → WAIT for approval
│  │  │           → END (Manager Path)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €50,000?
│  │  │
│  │  ├─ YES → DIRECTOR APPROVAL PATH
│  │  │        Continue to Level 5 (Supplier Check)
│  │  │
│  │  └─ NO → Continue
│  │
│  └─ Amount ≥ €50,000?
│     │
│     └─ YES → EXECUTIVE APPROVAL PATH
│              Create sequential tasks:
│              - Finance Director
│              - CFO
│              - CEO (if > €100,000)
│              Priority: URGENT
│              Deadline: 1 day each
│              → WAIT for all approvals
│                 → END (Executive Path)
│
├─ LEVEL 5: SUPPLIER ANALYSIS (for €10k-€50k range)
│  │
│  ├─ Supplier Status = "BLOCKED"?
│  │  │
│  │  ├─ YES → BLOCK & ESCALATE
│  │  │        Stop processing
│  │  │        Create urgent task
│  │  │        Notify procurement & finance
│  │  │        → END (Blocked Supplier)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Age < 180 days (New)?
│  │  │
│  │  ├─ YES → DUAL APPROVAL REQUIRED
│  │  │        Task 1: Director (2 days)
│  │  │        → WAIT for Task 1
│  │  │           IF Task 1 Approved:
│  │  │             Task 2: CFO (2 days)
│  │  │             → WAIT for Task 2
│  │  │                → END (Dual Approved)
│  │  │           IF Task 1 Rejected:
│  │  │             → END (Rejected at Level 1)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Risk Rating = "HIGH"?
│  │  │
│  │  ├─ YES → ENHANCED APPROVAL
│  │  │        Additional fraud checks
│  │  │        Director approval required
│  │  │        Extended deadline
│  │  │        → END (Enhanced Path)
│  │  │
│  │  └─ NO → STANDARD DIRECTOR APPROVAL
│  │           Create task for Director
│  │           Priority: High
│  │           Deadline: 2 days
│  │           → WAIT for approval
│  │              → END (Standard High-Value)
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

---

## Boas práticas de configuração

### 1. Manter a lógica clara e fácil de manter

✅ **Bom:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Mau (demasiado complexo):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Melhor: dividir em passos:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Documentar a lógica de decisão

**Incluir sempre:**
- Objetivo de cada ponto de decisão
- Regra de negócio implementada
- Resultados esperados
- Tratamento de exceções

**Exemplo de documentação:**
```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000-€10,000: Manager approval (Delegation matrix)
  > €10,000: Director approval (Signature authority)
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

---

### 3. Testar todos os caminhos

**Matriz de testes:**

| Caso de teste | Montante | Tipo | Fornecedor | Caminho esperado | Estado |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Existing | Auto-approve | ✅ |
| TC2 | €5,000 | Invoice | Existing | Manager | ✅ |
| TC3 | €15,000 | Invoice | New | Director+CFO | ✅ |
| TC4 | €60,000 | Invoice | Existing | Executive | ✅ |
| TC5 | €2,000 | Credit Note | Existing | Credit workflow | ✅ |
| TC6 | €100,000 | Invoice | Blocked | Stop & Escalate | ✅ |

---

### 4. Monitorizar as métricas de decisão

**Acompanhar:**
- Distribuição pelos caminhos de decisão
- Taxa de aprovação automática
- Taxa de revisão manual
- Tempo médio de processamento por caminho
- Taxas de exceção
- Utilização dos caminhos

**Exemplo de métricas:**
```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k-€10k): 420 (34%)
- Director path (€10k-€50k): 120 (10%)
- Executive path (> €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

---

## Padrões relacionados

### Padrões que combinam bem:

- **[Padrão de Gestão de Tarefas](task-management-pattern.md)** – Criar tarefas com base em decisões
- **[Padrão de Integração de API](api-integration-pattern.md)** – Obter dados para a tomada de decisão
- **[Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md)** – Utilizar os resultados do PO nas decisões
- **[Padrão de Transformação de Dados](data-transformation-pattern.md)** – Transformar dados antes das decisões

---

## Guias relacionados

### Pré-requisitos
- [Guia completo de cartas de condição](../and/condition-cards-complete-guide.md) – Todas as cartas de condição
- [Guia de manipulação de campos](../then/document-field/field-manipulation-guide.md) – Operações de campos
- [Guia de atribuição](../then/assignee/assignment-user-guide.md) – Lógica de encaminhamento

### Cartas relacionadas
- **CONDITION_DOC_FIELD_AMOUNT** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** – [Guia de atribuição](../then/assignee/assignment-user-guide.md)
- **tasks_create** – [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md)

### Próximos passos
- Criar tarefas: [Padrão de Gestão de Tarefas](task-management-pattern.md)
- Adicionar correspondência complexa: [Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md)
- Integrar APIs: [Padrão de Integração de API](api-integration-pattern.md)

---

**Versão do padrão:** 1.0
**Última atualização:** 23 de outubro de 2025
**Dificuldade:** Média
**Tempo estimado:** 30–45 minutos
**Taxa de êxito:** Alta

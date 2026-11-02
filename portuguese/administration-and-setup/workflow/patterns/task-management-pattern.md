# Padrão de gerenciamento de tarefas

**Tipo de padrão:** Gestão de Workflow **Complexidade:** Baixa-Média **Configuração estimada:** 30–45 minutos **Casos de uso comuns:** Workflows de aprovação, tarefas de revisão, tratamento de exceções, escalonamento

***

<!-- workflow-card-task-pattern-scope-20261022 -->

**Âmbito verificado:** Este é um modelo conceptual de coordenação, não uma configuração de fluxo de trabalho pronta para importar. Na biblioteca verificada, `tasks_create` pertence a **Tarefa**, `doc_user_assign` a **Responsável** e `action_send_email_to_groups` a **E-mail**.

Os nomes anteriores `ACTION_ASSIGN_TO_USER` e `CONDITION_TASK_STATUS` são designações ilustrativas, não cartões registados que possam ser selecionados nesta biblioteca. O JSON abaixo é esquemático. Criar uma tarefa, por si só, não pausa um fluxo de trabalho nem configura a sua retoma automática. O encaminhamento após a conclusão, a espera e a escalada exigem configuração e verificação separadas.

[Cartões de tarefas atuais](../then/task/README.md) · [Proteções de exportação e tarefas pendentes](../cards-overview/export-cards-guide.md).

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-9a74b1360332-pt.png" alt="Ilustração da biblioteca de cartões. A criação de tarefas, a atribuição de documentos e o envio de e-mail a grupos utilizam categorias distintas; escolha a versão disponível na sua organização. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Ilustração da biblioteca de cartões. A criação de tarefas, a atribuição de documentos e o envio de e-mail a grupos utilizam categorias distintas; escolha a versão disponível na sua organização. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

## Visão geral do padrão

Este modelo ilustra a criação e atribuição de tarefas e as notificações aos destinatários. Os passos após a conclusão descrevem uma arquitetura proposta; criar a tarefa não constitui uma operação de espera.

**O que este padrão faz:**

1. Cria tarefas com base em condições do workflow
2. Atribui tarefas aos utilizadores ou grupos adequados
3. Define as propriedades das tarefas (prioridade, prazo, descrição)
4. Envia notificações quando as tarefas são criadas
5. Acompanha o estado e a conclusão das tarefas
6. Encaminha os documentos com base nos resultados das tarefas

***

## Quando utilizar este padrão

Utilize este padrão quando precisar de:

* ✅ Criar workflows de aprovação
* ✅ Atribuir tarefas de revisão a utilizadores
* ✅ Tratar exceções que exigem intervenção humana
* ✅ Escalar problemas para responsáveis
* ✅ Criar cadeias de aprovação em vários níveis
* ✅ Acompanhar quem tem de fazer o quê
* ✅ Definir prazos para ações

**Não utilize este padrão quando:**

* ❌ não for necessária qualquer ação humana (utilize antes o processamento automático)
* ❌ apenas pretender notificar (utilize antes o e-mail)
* ❌ bastar um encaminhamento simples de documentos (utilize antes a atribuição)

***

## Exemplo completo de fluxo de trabalho

### Cenário: Aprovação de faturas com encaminhamento baseado no valor

**Requisito de negócio:**

* Faturas < 1.000 €: Aprovação automática (não é necessária tarefa)
* Faturas 1.000–10.000 €: Tarefa de aprovação para a Direção
* Faturas > 10.000 €: Dupla aprovação (Direção + Diretor)
* Todos os aprovadores recebem uma notificação por e-mail
* As tarefas têm um prazo de 3 dias

**Cartas de workflow utilizadas:**

1. CONDITION\_DOC\_FIELD\_AMOUNT – Verificar o montante da fatura
2. tasks\_create – Criar a tarefa de aprovação
3. ACTION\_ASSIGN\_TO\_USER – Atribuir a tarefa ao aprovador
4. ACTION\_SEND\_EMAIL\_TO\_GROUPS – Enviar a notificação
5. CONDITION\_TASK\_STATUS – Verificar se a tarefa foi concluída
6. ACTION\_APPROVE\_DOCUMENT – Aprovar após a conclusão da tarefa

***

## Implementação passo a passo

### Passo 1: Verificar o limiar de valor

**Carta:** CONDITION\_DOC\_FIELD\_AMOUNT ou uma condição de campo semelhante

**Configuração para o caminho 1 (< 1.000 €):**

```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Configuração para o caminho 2 (1.000–10.000 €):**

```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Configuração para o caminho 3 (> 10.000 €):**

```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Referência de guia:** [Guia de cartas de condição](../and/condition-cards-complete-guide.md)

***

### Passo 2A: Aprovar automaticamente faturas pequenas (< 1.000 €)

**Para montantes pequenos não é necessária tarefa**

**Cartas:**

* ACTION\_SET\_FIELD\_TO\_TEXT
  * Definir «Approval\_Type» = «AUTO»
  * Definir «Approval\_Reason» = «Valor abaixo do limite»
* ACTION\_APPROVE\_DOCUMENT

**Resultado:** Documento aprovado automaticamente, sem criação de tarefa

***

### Passo 2B: Criar a tarefa de aprovação para a Direção (1.000–10.000 €)

**Carta:** tasks\_create (recomendado para v4)

**Configuração:**

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "task_type": "Approval",
  "task_title": "Approve Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "Please approve invoice from {{Supplier_Name}}\n\nAmount: €{{Total_Amount}}\nInvoice Number: {{Invoice_Number}}\nInvoice Date: {{Invoice_Date}}\n\nReview and approve within 3 business days.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Mapeamento de campos:**

* `{{DOCUMENT_NUMBER}}` – ID automático do documento
* `{{Total_Amount}}` – Campo: Total\_Amount
* `{{Supplier_Name}}` – Campo: Supplier\_Name
* `{{Invoice_Number}}` – Campo: Invoice\_Number
* `{{Invoice_Date}}` – Campo: Invoice\_Date
* `{{Approving_Manager}}` – Campo ou utilizador fixo

**Referência de guia:** [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md)

***

### Passo 2C: Criar tarefas de dupla aprovação (> 10.000 €)

**Duas tarefas sequenciais para faturas de valor elevado**

**Tarefa 1: Aprovação pela Direção**

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Approve High-Value Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "HIGH VALUE INVOICE REQUIRES APPROVAL\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nThis invoice exceeds €10,000 and requires dual approval.\nYour approval is required before Director review.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Tarefa 2: Aprovação pelo Diretor (criada após a conclusão da Tarefa 1)**

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "task_type": "Second Approval",
  "task_title": "Final Approval: Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "FINAL APPROVAL REQUIRED\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nFirst approval: Completed by {{Task1_Approver}} on {{Task1_Date}}\n\nYour final approval required.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

***

### Passo 3: Atribuir a tarefa a um utilizador/grupo

**Carta:** ACTION\_ASSIGN\_TO\_USER ou ACTION\_ASSIGN\_TO\_GROUP

**Opção 1: Atribuir a um utilizador específico**

```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Opção 2: Atribuir a um grupo**

```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Opção 3: Atribuição sequencial**

```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Referência de guia:** [Guia de atribuição](../then/assignee/assignment-user-guide.md)

***

### Passo 4: Enviar a notificação por e-mail

**Carta:** ACTION\_SEND\_EMAIL\_TO\_GROUPS

**Configuração:**

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "New Task Assigned: Approve Invoice {{DOCUMENT_NUMBER}}",
  "body": "Dear {{TASK_ASSIGNEE_NAME}},\n\nA new approval task has been assigned to you:\n\nTask: Approve Invoice {{DOCUMENT_NUMBER}}\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPriority: {{TASK_PRIORITY}}\n\nPlease log in to DocBits to review and approve:\n{{DOCUMENT_LINK}}\n\nBest regards,\nDocBits Automation"
}
```

**Variáveis de e-mail:**

* `{{TASK_ASSIGNEE_EMAIL}}` – E-mail do destinatário da tarefa
* `{{TASK_ASSIGNEE_NAME}}` – Nome do destinatário da tarefa
* `{{DOCUMENT_NUMBER}}` – ID do documento
* `{{TASK_DEADLINE}}` – Data de vencimento da tarefa
* `{{TASK_PRIORITY}}` – Nível de prioridade da tarefa
* `{{DOCUMENT_LINK}}` – Ligação direta para o documento

**Referência de guia:** [Guia de envio de e-mail a grupos](../then/action/send-email-groups-guide.md)

***

### Passo 5: Acompanhar o estado da tarefa

**Carta:** CONDITION\_TASK\_STATUS ou um verificador de estado de tarefa semelhante

**Configuração:**

```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Opções de estado:**

* CREATED – Tarefa acabada de criar
* ASSIGNED – Tarefa atribuída a um utilizador
* IN\_PROGRESS – O utilizador iniciou a tarefa
* COMPLETED – Tarefa concluída
* APPROVED – Tarefa aprovada
* REJECTED – Tarefa rejeitada
* CANCELADA – Tarefa cancelada
* OVERDUE – Tarefa em atraso

**Lógica:**

```
IF TASK_STATUS = COMPLETED AND TASK_RESULT = APPROVED:
  → Continue to next step (or next approval level)
  → Update document status
  → Log approval

IF TASK_STATUS = COMPLETED AND TASK_RESULT = REJECTED:
  → Stop workflow
  → Send rejection notification
  → Create review task for corrections

IF TASK_STATUS = OVERDUE:
  → Escalate to manager
  → Send reminder email
  → Create escalation task
```

***

### Passo 6: Concluir o workflow com base no resultado da tarefa

**Após a conclusão da tarefa:**

**Cenário A: Tarefa aprovada**

```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Cenário B: Tarefa rejeitada**

```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Cenário C: Tarefa em atraso**

```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

***

## Diagrama completo de fluxo de trabalho

```
INVOICE ARRIVES
│
├─ CHECK AMOUNT
│  │
│  ├─ Amount < €1,000 ✅
│  │  │
│  │  ├─ Set Approval_Type = "AUTO"
│  │  └─ Auto-Approve Document
│  │     → END (Approved)
│  │
│  ├─ Amount €1,000-€10,000 ⚠️
│  │  │
│  │  ├─ CREATE TASK: Manager Approval
│  │  │  - Title: "Approve Invoice"
│  │  │  - Priority: Medium
│  │  │  - Deadline: 3 days
│  │  │  │
│  │  │  ├─ ASSIGN TO: Finance Manager
│  │  │  │
│  │  │  ├─ SEND EMAIL: Notification
│  │  │  │
│  │  │  ├─ WAIT FOR TASK COMPLETION
│  │  │  │  │
│  │  │  │  ├─ TASK APPROVED ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "APPROVED"
│  │  │  │  │  └─ Approve Document
│  │  │  │  │     → END (Approved)
│  │  │  │  │
│  │  │  │  ├─ TASK REJECTED ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Reject Document
│  │  │  │  │  └─ Create Correction Task
│  │  │  │  │     → END (Rejected)
│  │  │  │  │
│  │  │  │  └─ TASK OVERDUE ⏰
│  │  │  │     │
│  │  │  │     ├─ Send Reminder Email
│  │  │  │     ├─ Escalate to Director
│  │  │  │     └─ Create Escalation Task
│  │  │  │        → WAIT (Escalated)
│  │  │  │
│  │  │  └─ [Task tracking active]
│  │  │
│  │  └─ [Manager approval path]
│  │
│  └─ Amount > €10,000 🚨
│     │
│     ├─ CREATE TASK 1: Manager First Approval
│     │  - Title: "URGENT: First Approval"
│     │  - Priority: High
│     │  - Deadline: 2 days
│     │  │
│     │  ├─ ASSIGN TO: Finance Manager
│     │  ├─ SEND EMAIL: High Priority Notification
│     │  │
│     │  ├─ WAIT FOR TASK 1 COMPLETION
│     │  │  │
│     │  │  ├─ TASK 1 APPROVED ✅
│     │  │  │  │
│     │  │  │  ├─ CREATE TASK 2: Director Final Approval
│     │  │  │  │  - Title: "Final Approval Required"
│     │  │  │  │  - Priority: High
│     │  │  │  │  - Deadline: 1 day
│     │  │  │  │  │
│     │  │  │  │  ├─ ASSIGN TO: Finance Director
│     │  │  │  │  ├─ SEND EMAIL: Final Approval Notification
│     │  │  │  │  │
│     │  │  │  │  ├─ WAIT FOR TASK 2 COMPLETION
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TASK 2 APPROVED ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Set Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Approve Document
│     │  │  │  │  │  │     → END (Dual Approved)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TASK 2 REJECTED ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Reject Document
│     │  │  │  │  │     └─ Notify All Parties
│     │  │  │  │  │        → END (Final Rejected)
│     │  │  │  │  │
│     │  │  │  │  └─ [Task 2 tracking]
│     │  │  │  │
│     │  │  │  └─ [Task 2 created]
│     │  │  │
│     │  │  └─ TASK 1 REJECTED ❌
│     │  │     │
│     │  │     ├─ Reject Document (No Task 2 created)
│     │  │     └─ Notify Supplier
│     │  │        → END (First Rejected)
│     │  │
│     │  └─ [Task 1 tracking]
│     │
│     └─ [Dual approval path]
│
└─ [Amount check complete]
```

***

## Modelos de configuração

### Modelo 1: Tarefa de aprovação simples

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "card": "tasks_create",
  "task_title": "Approve {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}}",
  "task_description": "Please review and approve this document.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

***

### Modelo 2: Tarefa de revisão com detalhes

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "card": "tasks_create",
  "task_title": "Review Exception: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nException: {{EXCEPTION_REASON}}\n\nDetails:\n- Supplier: {{Supplier_Name}}\n- Amount: €{{Total_Amount}}\n- Date: {{Document_Date}}\n\nAction Required: Review and resolve exception",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

***

### Modelo 3: Tarefa de escalonamento

**JSON esquemático:** Apenas ilustra a estrutura; não o importe como um fluxo de trabalho executável.

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATION: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "ESCALATED TASK\n\nOriginal Task: {{ORIGINAL_TASK_ID}}\nOriginal Assignee: {{ORIGINAL_ASSIGNEE}}\nDeadline Passed: {{ORIGINAL_DEADLINE}}\nDays Overdue: {{DAYS_OVERDUE}}\n\nPlease review and take immediate action.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

***

## Padrões avançados

### Padrão 1: Aprovação sequencial em vários níveis

**Utilização:** As faturas têm de passar por vários aprovadores em sequência

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Implementação:**

```
1. Create Task 1 for Clerk
2. Wait for Task 1 completion
3. IF Task 1 = APPROVED:
     Create Task 2 for Manager
4. Wait for Task 2 completion
5. IF Task 2 = APPROVED:
     Create Task 3 for Director
6. Wait for Task 3 completion
7. IF Task 3 = APPROVED:
     Approve Document
```

***

### Padrão 2: Aprovação paralela por vários aprovadores

**Utilização:** Várias pessoas têm de aprovar em simultâneo

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Implementação:**

```
1. Create 3 tasks simultaneously
2. Track all 3 task statuses
3. WAIT until ALL tasks completed
4. IF ALL = APPROVED:
     Approve Document
   ELSE:
     Reject Document
```

***

### Padrão 3: Criação condicional de tarefas

**Utilização:** Criar tarefas diferentes com base em condições

```
IF Supplier = "New":
  → Create "New Supplier Review" task
ELSE IF Amount > €50,000:
  → Create "High Value Approval" task
ELSE IF Document has errors:
  → Create "Error Correction" task
ELSE:
  → Create "Standard Approval" task
```

***

### Padrão 4: Escalonamento baseado em prazos

**Utilização:** Escalar automaticamente se a tarefa não for concluída a tempo

```
Day 0: Create task for User A (3-day deadline)
Day 3: IF not completed:
         → Send reminder to User A
Day 4: IF still not completed:
         → Create escalation task for Manager B
         → Notify both User A and Manager B
Day 5: IF still not completed:
         → Create urgent task for Director C
         → High priority notification
```

***

## Tratamento de erros

### Cenário 1: Destinatário não encontrado

**Problema:** O utilizador não existe ou está inativo

**Solução:**

```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

***

### Cenário 2: Falha na criação da tarefa

**Problema:** Erro de sistema ao criar a tarefa

**Solução:**

```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

***

### Cenário 3: Sem resposta à tarefa

**Problema:** O utilizador não conclui a tarefa dentro do prazo

**Solução:**

```
1. Monitor task deadline
2. Day before deadline:
     → Send reminder email
3. On deadline day:
     → Send urgent reminder
4. After deadline:
     → Create escalation task
     → Notify manager
     → Log overdue event
```

***

## Lista de verificação de testes

* [ ] Tarefa criada com êxito
* [ ] Tarefa atribuída ao utilizador/grupo correto
* [ ] Notificação por e-mail enviada
* [ ] A tarefa aparece na lista de tarefas do utilizador
* [ ] Propriedades da tarefa corretas (título, descrição, prioridade, prazo)
* [ ] O utilizador consegue concluir a tarefa
* [ ] O workflow continua após a conclusão da tarefa
* [ ] O workflow de aprovação funciona corretamente
* [ ] O workflow de rejeição funciona corretamente
* [ ] O escalonamento é acionado no momento certo
* [ ] O tratamento de tarefas em atraso funciona
* [ ] Todas as notificações por e-mail foram enviadas
* [ ] As atualizações de campos funcionam corretamente

***

## Exemplos do mundo real

### Exemplo 1: Exceção na correspondência de três vias (PO)

**Cenário:** A fatura não corresponde à encomenda, é necessária revisão

```
1. PO Matching fails (price variance > 5%)
2. Create Task: "Review PO Mismatch"
   - Assign to: Procurement Officer
   - Priority: High
   - Description: Include variance details
3. Send email with comparison table
4. Wait for task completion
5. IF Approved: Continue processing
   IF Rejected: Return to supplier
```

***

### Exemplo 2: Aprovação de fatura de fornecedor

**Cenário:** A fatura de um novo fornecedor requer uma aprovação especial

```
1. Check if supplier is new (< 6 months old)
2. IF New:
     Create Task: "New Supplier Invoice Review"
     - Assign to: Procurement Manager
     - Include supplier details
     - Require supplier verification
3. After approval:
     Add to approved supplier list
     Continue normal workflow
```

***

### Exemplo 3: Processamento de fim de mês

**Cenário:** As faturas de fim de mês requerem processamento urgente

```
1. Check if document date in last 3 days of month
2. IF Yes:
     Create Task: "URGENT: Month-End Invoice"
     - Priority: Urgent
     - Deadline: 1 day
     - Assign to: Finance Team (all members)
     - Flag for expedited processing
3. Send urgent email notification
4. Track completion
```

***

## Sugestões de desempenho

✅ **Boas práticas:**

* Definir prazos realistas
* Utilizar títulos e descrições de tarefas claros
* Incluir na tarefa todas as informações necessárias
* Notificar atempadamente
* Monitorizar as taxas de conclusão das tarefas
* Escalar automaticamente as tarefas em atraso
* Registar todas as atividades das tarefas
* Rever os padrões de tarefas mensalmente

❌ **Evitar:**

* Criar tarefas para tudo
* Descrições de tarefas vagas
* Prazos irrealistas
* Demasiados e-mails de notificação
* Não ter um caminho de escalonamento
* Ignorar tarefas em atraso
* Não acompanhar as métricas das tarefas

***

## Padrões relacionados

### Padrões que combinam bem:

* [**Padrão de Integração de API**](api-integration-pattern.md) – Criar tarefas para erros de API
* [**Padrão de Correspondência de Encomendas (PO Matching)**](po-matching-pattern.md) – Criar tarefas em caso de discrepâncias de PO
* [**Padrão de Lógica de Decisão**](decision-logic-pattern.md) – Encaminhar para o tipo de tarefa adequado
* [**Padrão de Transformação de Dados**](data-transformation-pattern.md) – Transformar dados antes de criar a tarefa

***

## Guias relacionados

### Pré-requisitos

* [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md) – Documentação da carta de tarefa
* [Guia de atribuição](../then/assignee/assignment-user-guide.md) – Atribuição de utilizadores
* [Guia de envio de e-mail a grupos](../then/action/send-email-groups-guide.md) – Notificações por e-mail

### Cartas relacionadas

* **tasks\_create** – [Guia de atribuição de tarefas](../then/task/task-assignment-guide.md)
* **ACTION\_ASSIGN\_TO\_USER** – [Guia de atribuição](../then/assignee/assignment-user-guide.md)
* **ACTION\_SEND\_EMAIL\_TO\_GROUPS** – [Guia de e-mail](../then/action/send-email-groups-guide.md)
* **CONDITION\_TASK\_STATUS** – [Guia de cartas de condição](../and/condition-cards-complete-guide.md)

### Próximos passos

* Adicionar notificações por e-mail: [Guia de e-mail](../then/action/send-email-groups-guide.md)
* Implementar encaminhamento complexo: [Padrão de Lógica de Decisão](decision-logic-pattern.md)
* Resolver erros de tarefas: [Tratamento de erros](task-management-pattern.md#tratamento-de-erros) acima

***

**Versão do padrão:** 1.0 **Última atualização:** 23 de outubro de 2025 **Dificuldade:** Baixa-Média **Tempo estimado:** 30–45 minutos **Taxa de êxito:** Muito alta

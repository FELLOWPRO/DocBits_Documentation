# Task Assignment Guide

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

{% embed url="https://youtu.be/MZoDMibM-7E" %}
DocBits Tasks & Notifications Tutorial: Assign Work, Track Status & Handle Workflow Tasks
{% endembed %}

Neste vídeo, vai aprender como funcionam as Tasks & Notifications no DocBits e como ajudam as equipas a manter-se a par de seguimentos, atribuições e atualizações importantes de documentos.

**O que vai aprender:**
*   Para que servem as Tasks & Notifications (seguimentos, atribuições, atualizações)
*   O que muda quando a funcionalidade é ativada (vista dedicada de gestão de tarefas)
*   Como as tarefas podem ser atribuídas a utilizadores ou grupos de utilizadores
*   Como gerir tarefas: atualizar o estado, adicionar descrições, reatribuir e fechar tarefas
*   Como as tarefas geradas pelo fluxo de trabalho são criadas automaticamente e aparecem no dashboard com base nas regras de tratamento padrão

## Visão geral
As tarefas são a forma principal de atribuir trabalho aos utilizadores no DocFlow. Uma tarefa representa uma unidade de trabalho que tem de ser concluída, como "Approve Invoice", "Review Discrepancy" ou "Contact Supplier".

---

# Criação básica de tarefas

## Cartão: tasks_create / Create Task and Assign to User

### Objetivo
Cria uma tarefa e atribui-a a uma pessoa específica

### Quando utilizar
- A fatura necessita da revisão de uma pessoa específica
- É necessária a aprovação de uma pessoa nomeada
- Transferência para um membro específico da equipa

### Parâmetros

**Title**
O nome/assunto da tarefa
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Description**
Detalhes sobre a tarefa
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Priority**
- 🔴 **High**: Urgente, fazer de imediato
- 🟡 **Medium**: Prioridade normal
- 🟢 **Low**: Pode ser feito mais tarde

**Assigned User**
Quem recebe a tarefa
```
Example: John Smith (Finance Manager)
```

**Email Notification**
Enviar um alerta por e-mail à pessoa atribuída?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Exemplo
```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

---

## Cartão: ACTION_TASK_FOR_GROUP / Create Task for Group

### Objetivo
Cria uma tarefa e atribui-a a um grupo (todos os membros a podem ver)

### Quando utilizar
- Várias pessoas podem realizar a tarefa
- Tarefa para uma equipa, não para um indivíduo
- A primeira pessoa disponível deve tratá-la

### Diferença em relação à tarefa individual
```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

### Exemplo de fluxo de trabalho
```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

---

## Cartão: ACTION_DECISION_TREE_CREATE_TASKS

### Objetivo
Cria tarefas com base na lógica de uma tabela de decisão

### Como funciona
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Quando utilizar
- Diferentes fornecedores necessitam de aprovações diferentes
- Encaminhamento complexo com base em vários fatores
- Equipa diferente consoante o tipo de documento

### Exemplo
```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

---

## Cartão: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Objetivo
Cria tarefas sequencialmente com base numa tabela de decisão
As tarefas são atribuídas uma de cada vez, por ordem de prioridade

### Quando utilizar
- São necessárias várias aprovações em sequência
- Cadeia de aprovação do fluxo de trabalho
- Cada pessoa revê e depois passa para a seguinte

### Como funciona
```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

### Sistema de prioridades
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Exemplo de configuração
```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

---

## Cartão: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Objetivo
Atribui o documento a um utilizador E cria uma tarefa sequencial

### Quando utilizar
- Atribuir o documento E criar a tarefa ao mesmo tempo
- O documento precisa de ser revisto por uma pessoa específica
- Acompanhar tanto a atribuição como a criação da tarefa

### Como funciona
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Exemplo
```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

---

## Cartão: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Objetivo
Atribui o documento a um grupo E cria uma tarefa

### Quando utilizar
- O documento necessita da atenção de um grupo
- Pretende acompanhar a criação da tarefa
- Criar uma tarefa inicial e depois a atribuição do documento

### Exemplo
```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

---

# Criação avançada de tarefas

## Cartão: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Objetivo
Cria uma tarefa para um grupo de instalação específico

### Quando utilizar
- Tarefa para a equipa de um armazém/instalação
- Operações específicas por instalação
- A localização física é relevante

### Exemplo
```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

---

## Cartão: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Objetivo
Atribuição sequencial de tarefas entre instalações

### Quando utilizar
- Operações em várias instalações
- As tarefas passam de instalação em instalação
- Processamento sequencial por instalação

### Como funciona
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Exemplo
```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

---

## Cartão: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Objetivo
Cria uma tarefa para o departamento de aquisições

### Quando utilizar
- Tarefa para a equipa de aquisições
- Tarefas de gestão de fornecedores
- Trabalho relacionado com compras

### Exemplo
```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

---

## Cartão: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Objetivo
Encaminhamento sequencial de tarefas dentro das aquisições

### Quando utilizar
- Processos de aquisição em várias etapas
- Cadeia de aprovação nas aquisições
- Caminho de escalonamento

### Exemplo
```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

---

## Cartão: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Objetivo
Obter o utilizador a partir de um campo do documento e atribuir a tarefa
Se o utilizador não for encontrado, utilizar um utilizador alternativo

### Quando utilizar
- Utilizador armazenado num campo do documento
- O documento especifica quem deve fazer a revisão
- Ter uma pessoa de reserva caso o utilizador especificado não esteja disponível

### Como funciona
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Exemplo
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parâmetros
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Parâmetros comuns das tarefas

Todos os cartões de tarefa utilizam estes parâmetros:

### Title
```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

### Description
```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

### Níveis de prioridade
```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

### Data de vencimento (se disponível)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Cenários de fluxo de trabalho de tarefas

## Cenário 1: Aprovação simples
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Cenário 2: Aprovação multinível
```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

## Cenário 3: Tarefas paralelas
```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

## Cenário 4: Encaminhamento condicional
```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

---

# Boas práticas de atribuição de tarefas

✅ **Faça:**
- Inclua detalhes específicos no título da tarefa
- Defina níveis de prioridade adequados
- Defina prazos realistas
- Notifique as pessoas atribuídas
- Inclua uma ligação para o documento
- Utilize descrições claras e acionáveis

❌ **Não faça:**
- Criar títulos de tarefa vagos ("Review this")
- Definir tudo como prioridade High
- Esquecer-se de notificar a pessoa atribuída
- Criar várias tarefas para o mesmo trabalho
- Atribuir a pessoas indisponíveis

---

# Resolução de problemas de tarefas

## "Tarefa não atribuída a ninguém"
**Causa:** O utilizador não existe ou o grupo está vazio

**Solução:**
- Verifique a escrita do nome do utilizador
- Verifique se o utilizador está ativo no sistema
- Verifique se o grupo tem membros
- Utilize uma alternativa, se necessário

## "A pessoa diz que não recebeu a notificação"
**Causa:** Notificação por e-mail desativada ou e-mail incorreto

**Solução:**
- Verifique se a caixa "Send Email" está ativada
- Verifique o endereço de e-mail do destinatário
- Verifique a pasta de spam
- Reenvie a notificação manualmente

## "A tarefa foi para a pessoa errada"
**Causa:** Lógica de encaminhamento incorreta

**Solução:**
- Verifique as condições da tabela de decisão
- Verifique as definições de alternativa
- Teste com um documento de amostra
- Verifique se há erros de escrita nos nomes dos utilizadores

## "Foram criadas demasiadas tarefas"
**Causa:** O cartão é acionado várias vezes

**Solução:**
- Verifique se as condições são suficientemente específicas
- Verifique se o cartão só é executado uma vez por documento
- Reveja as condições "And"
- Adicione filtragem adicional

---

# Tabela de comparação dos cartões de tarefa

| Cartão | Cria tarefa | Atribui a | Quando |
|------|-------------|-----------|------|
| tasks_create | Sim | Individual | Sempre |
| ACTION_TASK_FOR_GROUP | Sim | Grupo | Sempre |
| ACTION_DECISION_TREE_CREATE_TASKS | Sim | Resultado da tabela de decisão | Condicional |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Sim | Vários (sequencial) | Condicional |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Sim | Utilizador + Documento | Condicional |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Sim | Grupo + Documento | Condicional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Sim | Grupo de instalação | Condicional |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Sim | Várias instalações | Condicional |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Sim | Equipa de aquisições | Condicional |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Sim | Vários (sequencial) | Condicional |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Sim | Campo/Alternativa | Condicional |

---

# Cartões relacionados

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Atribuir o documento sem criar uma tarefa
- **ACTION_SEND_EMAIL** - Notificar as pessoas diretamente
- **STAUS_CHANGE** - Alterar o estado em vez de criar uma tarefa
- **RUN_WORKFLOW** - Acionar um fluxo de trabalho diferente em alternativa

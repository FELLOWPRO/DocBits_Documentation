# Cartões de atribuição e criação de tarefas

## Cartões de atribuição e criação de tarefas - guia completo

**Capas:** 12 cartões relacionados a tarefas

***

Os cartões de tarefas nesta página vão para o grupo **Então** do Workflow Builder — as ações que são executadas quando as condições Quando/E correspondem:

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-canvas-e5e45b3054fa-pt.png" alt="Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Exemplo não guardado com cartões Quando, E e Então. Configure todos os campos antes da execução. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

***

### 📌 Informações da versão

**Cartão mais evoluído:** tasks\_create (4 versões, v4 mais recente) **Outros cartões multi-versão:** ACTION\_TASK\_FOR\_GROUP (v4), ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP (v3), ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK (v3), ACTION\_DECISION\_TREE\_CREATE\_TASKS (v3)

**Alterações principais:**

* **v3 → v4 Evolução:** Removida abordagem de árvore de decisão, adicionados tipos de itens de trabalho genéricos (Tarefa, Ticket, Problema)
* **v2 → migração v3:** Adicionado suporte à árvore de decisão (agora praticamente obsoleto)

📖 [Histórico completo da versão](../../release.md) | [Versões e comportamento das cartas](../../cards-overview/card-versions-guide.md)

***

### Visão geral

Os cartões de tarefas criam atribuições de trabalho para os membros da equipe. Quando uma fatura precisa de aprovação, você pode criar automaticamente uma tarefa e atribuí-la à pessoa certa.

***

## Criação de Tarefa Básica

### Cartão: tasks\_create / Criar tarefa e atribuir ao usuário

#### Objetivo

Cria uma tarefa e a atribui a uma pessoa específica

#### Quando usar

* A fatura precisa da revisão de uma pessoa específica
* Aprovação necessária do indivíduo nomeado
* Transferência para membro específico da equipe

#### Parâmetros

**Título** O nome/assunto da tarefa

```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Descrição** Detalhes sobre a tarefa

```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Prioridade**

* 🔴 **High**: Urgente, faça imediatamente
* 🟡 **Médio**: Prioridade normal
* 🟢 **Baixo**: Pode ser feito mais tarde

**Usuário atribuído** Quem recebe a tarefa

```
Example: John Smith (Finance Manager)
```

**Notificação por e-mail** Enviar alerta por e-mail para a pessoa designada?

```
✅ Yes: Person gets email
❌ No: Task only in system
```

#### Exemplo

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

***

### Cartão: ACTION\_TASK\_FOR\_GROUP / Criar tarefa para grupo

#### Objetivo

Cria uma tarefa e a atribui a um grupo (todos os membros podem vê-la)

#### Quando usar

* Várias pessoas podem fazer a tarefa
* Tarefa para equipe, não individual
* A primeira pessoa disponível deve cuidar

#### Diferença da tarefa individual

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

#### Exemplo de fluxo de trabalho

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

***

### Cartão: ACTION\_DECISION\_TREE\_CREATE\_TASKS

#### Objetivo

Cria tarefas com base na lógica da tabela de decisão

#### Como funciona

```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

#### Quando usar

* Fornecedores diferentes precisam de aprovações diferentes
* Roteamento complexo baseado em múltiplos fatores
* Equipe diferente com base no tipo de documento

#### Exemplo

```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

***

### Cartão: ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL

#### Objetivo

Cria tarefas sequencialmente com base na tabela de decisão As tarefas são atribuídas uma de cada vez com ordem de prioridade

#### Quando usar

* Múltiplas aprovações necessárias em sequência
* Cadeia de aprovação de fluxo de trabalho
* Cada pessoa analisa e depois passa para a próxima

#### Como funciona

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

#### Sistema Prioritário

```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

#### Exemplo de configuração

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

***

### Cartão: ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL

#### Objetivo

Atribui documento a um usuário E cria tarefas sequenciais

#### Quando usar

* Atribuir documento E criar tarefa ao mesmo tempo
* O documento precisa ser revisado por pessoa específica
* Acompanhe a atribuição e a criação de tarefas

#### Como funciona

```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

#### Exemplo

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

***

### Cartão: ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL

#### Objetivo

Atribui documento ao grupo E cria tarefa

#### Quando usar

* Documento precisa de atenção do grupo
* Quer acompanhar a criação de tarefas
* Crie a tarefa inicial e depois documente a atribuição

#### Exemplo

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

***

## Criação avançada de tarefas

### Cartão: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP

#### Objetivo

Cria tarefa para grupo de instalações específico

#### Quando usar

* Tarefa para a equipe do armazém/instalação
* Operações específicas da instalação
* A localização física é importante

#### Exemplo

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

***

### Cartão: ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL

#### Objetivo

Atribuição sequencial de tarefas entre instalações

#### Quando usar

* Operações multi-instalações
* As tarefas passam de instalação em instalação
* Processamento sequencial de instalações

#### Como funciona

```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

#### Exemplo

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

***

### Cartão: ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP

#### Objetivo

Cria tarefa para o departamento de compras

#### Quando usar

* Tarefa para a equipe de compras
* Tarefas de gerenciamento de fornecedores
* Trabalho relacionado à compra

#### Exemplo

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

***

### Cartão: ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL

#### Objetivo

Roteamento sequencial de tarefas dentro de compras

#### Quando usar

* Processos de aquisição em várias etapas
* Cadeia de aprovação em compras
* Caminho de escalonamento

#### Exemplo

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

***

### Cartão: ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK

#### Objetivo

Obtenha o usuário do campo do documento, atribua a tarefa Se o usuário não for encontrado, use o usuário substituto

#### Quando usar

* Usuário armazenado no campo do documento
* Documento especifica quem deve revisar
* Tenha uma pessoa de apoio se o usuário especificado não estiver disponível

#### Como funciona

```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

#### Exemplo

```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

#### Parâmetros

```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

***

## Parâmetros de tarefas comuns

Todos os cartões de tarefas usam estes parâmetros:

#### Título

```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

#### Descrição

```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

#### Níveis de prioridade

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

#### Data de vencimento (se disponível)

```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

***

## Cenários de fluxo de trabalho de tarefas

### Cenário 1: Aprovação Simples

```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

### Cenário 2: Aprovação Multinível

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

### Cenário 3: Tarefas Paralelas

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

### Cenário 4: Roteamento Condicional

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

***

## Práticas recomendadas para atribuição de tarefas

✅ **Fazer:**

* Incluir detalhes específicos no título da tarefa
* Defina níveis de prioridade apropriados
* Estabeleça prazos realistas
* Notificar os responsáveis
* Incluir link para documento
* Use descrições claras e acionáveis

❌ **Não:**

* Crie títulos de tarefas vagos ("Revise isto")
* Defina tudo como alta prioridade
* Esqueci de notificar a pessoa designada
* Crie várias tarefas para o mesmo trabalho
* Atribuir a pessoas indisponíveis

***

## Tarefas de solução de problemas

### "Tarefa não atribuída a ninguém"

**Causa:** O usuário não existe ou o grupo está vazio

**Solução:**

* Verifique a ortografia do nome de usuário
* Verifique se o usuário está ativo no sistema
* Verifique se o grupo tem membros
* Use substituto se necessário

### "Pessoa diz que não recebeu notificação"

**Causa:** Notificação por e-mail desativada ou e-mail errado

**Solução:**

* Marque a caixa de seleção "Enviar e-mail" ativada
* Verifique o endereço de e-mail do destinatário
* Verifique a pasta de spam
* Reenviar notificação manualmente

### "Pessoa errada recebeu tarefa"

**Causa:** Lógica de roteamento incorreta

**Solução:**

* Verifique as condições da tabela de decisão
* Verifique as configurações de substituto
* Teste com documento de amostra
* Verifique se há erros de digitação nos nomes de usuário

### "Muitas tarefas criadas"

**Causa:** Cartão disparando diversas vezes

**Solução:**

* Verifique se as condições são específicas o suficiente
* O cartão de verificação é executado apenas uma vez por documento
* Revise as condições "E"
* Adicionar filtragem adicional

***

## Tabela de comparação de cartões de tarefas

| Cartão                                                        | Cria tarefa | Atribuir a            | When        |
| ----------------------------------------------------------- | ------------ | --------------------- | ----------- |
| tasks\_create                                               | Sim          | Individual            | Sempre      |
| ACTION\_TASK\_FOR\_GROUP                                    | Sim          | Grupo                 | Sempre      |
| ACTION\_DECISION\_TREE\_CREATE\_TASKS                       | Sim          | Resultado da Tabela de Decisão | Condicional |
| ACTION\_DECISION\_TREE\_TASKS\_SEQUENTIAL                   | Sim          | Múltiplo (Sequencial) | Condicional |
| ACTION\_CREATE\_TASK\_FOR\_USER\_SEQUENTIAL                 | Sim          | Usuário + Documento       | Condicional |
| ACTION\_CREATE\_TASK\_FOR\_GROUP\_SEQUENTIAL                | Sim          | Grupo + Documento      | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP                   | Sim          | Grupo de instalações        | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_FACILITY\_GROUP\_SEQUENTIAL       | Sim          | Várias instalações   | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_PROCUREMENT\_GROUP                | Sim          | Equipe de compras      | Condicional |
| ACTION\_ASSIGN\_TASK\_PROCUREMENT\_GROUP\_SEQUENTIAL        | Sim          | Múltiplo (Sequencial) | Condicional |
| ACTION\_ASSIGN\_TASK\_TO\_USER\_FROM\_FIELD\_WITH\_FALLBACK | Sim          | Campo/substituto        | Condicional |

***

## Cartões Relacionados

* **ACTION\_ASSIGN\_DOCUMENT\_TO\_USER** - Atribuir documento sem criar tarefa
* **ACTION\_SEND\_EMAIL** - Notificar as pessoas diretamente
* **STAUS\_CHANGE** - Alterar status em vez de criar tarefa
* **RUN\_WORKFLOW** - Aciona um fluxo de trabalho diferente

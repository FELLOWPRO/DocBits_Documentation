# Document Assignment & User Cards - Complete Guide

Estes cartões ficam no grupo **Then** do Construtor de fluxos de trabalho — as ações executadas assim que as condições When/And são atendidas:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="Workflow Builder"><figcaption><p>Os cartões são adicionados ao grupo <strong>Then</strong> através de <strong>Add Card</strong>.</p></figcaption></figure>

**Abrange:** 13 cartões de atribuição e relacionados com utilizadores

---

## 📌 Informações de versão

**Cartões multiversão:** DOC_USER_ASSIGN (v2 a mais recente, v3 descontinuada), DOC_GROUP_ASSIGN (v2 a mais recente, v3 descontinuada), OC_ASSIGN_DOC (v2)

**Importante:** As versões v3 adicionaram suporte de árvore de decisão, mas estão agora descontinuadas
**Recomendação:** Utilize a v2 tanto para DOC_USER_ASSIGN como para DOC_GROUP_ASSIGN

📖 [Complete Version History](../../../changelog/release.md#-assignment--routing-cards) | [Card Version Database](../../../../DocFlow/docs/card_version.md)

---

# Atribuição básica de documentos

## Cartão: DOC_USER_ASSIGN / Assign Document to User

### Objetivo
Atribui o documento a uma pessoa específica para a sua ação

### Quando utilizar
- O documento necessita da revisão de uma pessoa específica
- Transferência para um membro individual da equipa
- Acompanhamento da responsabilização
- Atribuir trabalho a uma pessoa nomeada

### Como funciona
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Exemplo
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parâmetros
```
User: [Select which person]
```

### Nota
Atribuir significa:
- O documento aparece como "assigned to me" para essa pessoa
- Essa pessoa é a responsável
- Os outros ainda podem ver o documento (mas não como atribuído a si)
- Uma atribuição de cada vez por documento

---

## Cartão: DOC_GROUP_ASSIGN / Assign Document to Group

### Objetivo
Atribui o documento a um grupo (todos os membros o veem como atribuído a si)

### Quando utilizar
- Documento para uma equipa, não para um indivíduo
- Várias pessoas podem tratá-lo
- Responsabilidade partilhada
- Distribuição da carga de trabalho da equipa

### Como funciona
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Exemplo
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parâmetros
```
Group: [Select which group]
```

### Diferença
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Cartão: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Objetivo
Atribui o documento com base na lógica de uma tabela de decisão

### Quando utilizar
- Diferentes fornecedores necessitam de diferentes responsáveis
- Atribuição com base no montante
- Lógica de encaminhamento complexa
- Várias condições para a atribuição

### Como funciona
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Exemplo: Atribuição baseada no montante
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Exemplo: Atribuição baseada no fornecedor
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parâmetros
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Cartão: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Objetivo
Atribui o documento sequencialmente com base numa tabela de decisão com prioridades

### Quando utilizar
- Várias aprovações sequenciais
- Pessoas diferentes em níveis diferentes
- Cadeia de aprovação baseada no montante
- Caminho de escalonamento

### Como funciona
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Sistema de prioridades
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Exemplo: Aprovação multinível
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parâmetros
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Objetivo
Atribui o documento a um utilizador com prioridade sequencial

### Quando utilizar
- O documento necessita de uma pessoa específica
- Processamento sequencial claro
- Atribuição única com ordem

### Como funciona
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Exemplo
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Objetivo
Atribui o documento sequencialmente a grupos

### Quando utilizar
- Várias aprovações de grupo
- Departamentos diferentes em cada fase
- Processamento sequencial baseado em equipas

### Como funciona
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Exemplo
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Objetivo
Atribui o documento a um grupo de instalação específico

### Quando utilizar
- Documento para um armazém/instalação específico
- Operações baseadas em instalações
- Processamento específico por localização

### Exemplo
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Objetivo
Atribui sequencialmente entre instalações

### Quando utilizar
- Processamento em várias localizações
- A expedição passa por várias instalações
- Fluxo de trabalho baseado na localização

### Exemplo
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Objetivo
Atribui o documento ao departamento de aquisições

### Quando utilizar
- Tratamento pela equipa de aquisições
- Trabalho relacionado com fornecedores
- Relacionado com ordens de compra

### Exemplo
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Cartão: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Objetivo
Atribuição sequencial dentro das aquisições

### Quando utilizar
- Processo de aquisição em várias etapas
- Cadeia de aprovação nas aquisições

### Exemplo
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Cartão: ACTION_CHANGE_DOC_SUBORG / Change Document Sub-Organization

### Objetivo
Atribui o documento a uma suborganização diferente

### Quando utilizar
- Organização errada selecionada
- Necessidade de mover para o departamento correto
- Reestruturação organizacional

### Como funciona
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Exemplo
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Cartão: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Objetivo
Altera a suborganização com base no valor de um campo do documento

### Quando utilizar
- Suborganização armazenada num campo
- Fazer corresponder a localização do documento ao campo
- Atribuição automática de organização

### Como funciona
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Exemplo
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Cartão: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Objetivo
Atribui o documento a um utilizador a partir de um campo, com uma alternativa caso o utilizador não seja encontrado

### Quando utilizar
- Nome de utilizador armazenado num campo do documento
- Pode não existir no sistema
- Necessidade de uma reserva caso o utilizador esteja indisponível

### Como funciona
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parâmetros
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Exemplo
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Cartão: ACTION_ASSIGN_USER_TO_SUPPLIER

### Objetivo
Atribui o documento ao utilizador que gere esse fornecedor

### Quando utilizar
- Utilizador associado a um fornecedor
- Gestor de conta do fornecedor
- Responsável pela relação com o fornecedor

### Como funciona
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Árvores de decisão de atribuição

## Exemplo de tabela de decisão 1: Baseada no montante
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Exemplo de tabela de decisão 2: Baseada no fornecedor
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Exemplo de tabela de decisão 3: Baseada no tipo de documento
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Exemplos de fluxos de trabalho de atribuição

## Exemplo 1: Encaminhamento simples
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Exemplo 2: Aprovação sequencial
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Exemplo 3: Encaminhamento baseado no montante
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Exemplo 4: Baseado na instalação
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Boas práticas de atribuição

✅ **Faça:**
- Mantenha as tabelas de decisão simples
- Teste a lógica de encaminhamento com amostras
- Garanta que todos os caminhos conduzem a algum lugar
- Tenha uma alternativa para utilizadores em falta
- Documente as decisões de encaminhamento

❌ **Não faça:**
- Criar atribuições circulares (A→B→A)
- Atribuir a utilizadores inexistentes (sem alternativa)
- Tornar o encaminhamento demasiado complexo
- Esquecer-se de testar o encaminhamento
- Atribuir a pessoas indisponíveis

---

# Resolução de problemas de atribuição

## "Documento não atribuído"
**Causa:** Condição não cumprida ou o utilizador não existe

**Solução:**
- Verifique se a condição é verdadeira
- Verifique se o utilizador existe no sistema
- Verifique as definições de alternativa
- Reveja a lógica da tabela de decisão

## "Pessoa errada atribuída"
**Causa:** Tabela de decisão ou lógica de encaminhamento incorreta

**Solução:**
- Teste a tabela de decisão
- Verifique as condições
- Verifique o mapeamento de utilizadores
- Reveja os valores dos campos

## "A atribuição parece ignorar alguém"
**Causa:** Ordem sequencial incorreta

**Solução:**
- Verifique os números de prioridade
- Verifique se a sequência está correta
- Teste com uma amostra
- Reveja a ordenação da tabela de decisão

---

# Comparação dos cartões de atribuição

| Cartão | Atribui a | Tipo de encaminhamento | Caso de utilização |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Individual | Direto | Atribuição simples |
| DOC_GROUP_ASSIGN | Grupo | Direto | Atribuição a equipa |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Resultado de decisão | Condicional | Encaminhamento complexo |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Vários (sequencial) | Condicional | Cadeia de aprovação |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Utilizador (sequencial) | Ordenado | Etapas sequenciais de utilizador |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Grupos (sequencial) | Ordenado | Etapas sequenciais de grupo |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Grupo de instalação | Direto | Específico por instalação |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Instalações (sequencial) | Ordenado | Várias instalações |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Aquisições | Direto | Fluxo de trabalho de aquisições |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Aquisições (sequencial) | Ordenado | Cadeia de aprovação de aquisições |
| ACTION_CHANGE_DOC_SUBORG | Suborganização | Direto | Mudança de departamento |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Suborg. por campo | Condicional | Atribuição baseada em campo |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Campo/Alternativa | Condicional | Atribuição dinâmica de utilizador |

---

# Cartões relacionados

- **ACTION_CREATE_TASK_FOR_USER** - Atribuir uma tarefa à mesma pessoa
- **ACTION_SEND_EMAIL** - Notificar a pessoa atribuída
- **CONDITION_USER_IS_ISNOT** - Verificar se a pessoa correta foi atribuída
- **CONDITION_GROUP_IS_ISNOT** - Verificar se o grupo correto foi atribuído

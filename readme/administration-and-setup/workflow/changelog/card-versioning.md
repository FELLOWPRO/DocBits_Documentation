# Card Versioning System - October 2025 Update

**Documento:** Visão geral do versionamento dos cartões de fluxo de trabalho
**Última atualização:** 23 de outubro de 2025
**Estado:** Completo

---

## Visão geral

O Motor de Fluxo de Trabalho DocBits utiliza **versionamento baseado em números inteiros** para gerir a evolução dos cartões, mantendo a compatibilidade com versões anteriores. Este documento fornece uma visão geral do sistema de versionamento.

---

## O que é o versionamento de cartões?

### Conceito
Cada cartão de fluxo de trabalho pode ter várias versões, permitindo que o sistema:
- Adicione novas funcionalidades sem quebrar os fluxos de trabalho existentes
- Suporte funcionalidades descontinuadas enquanto as elimina gradualmente
- Faça evoluir as capacidades dos cartões ao longo do tempo
- Mantenha a compatibilidade com versões anteriores

### Estrutura das versões
- **Formato:** Valores inteiros (1, 2, 3, 4, 5...)
- **Identificação:** Chave composta de (card_type, card_version)
- **Estado:** Cada versão tem indicadores de descontinuada/ativada

### Exemplo
O cartão `tasks_create` evoluiu ao longo de 4 versões:
- **v1:** Criação de tarefas original (descontinuada)
- **v2:** Adicionado suporte de tradução (descontinuada)
- **v3:** Suporte experimental de árvore de decisão (descontinuada)
- **v4:** Suporte de tipo genérico de item de trabalho (ativa atual)

---

## Principais estatísticas

### Visão geral do versionamento
| Métrica | Valor |
|--------|-------|
| **Cartões com várias versões** | 30+ |
| **Total de registos de versões** | 90+ |
| **Versões por cartão (média)** | 3 |
| **Número máximo de versões** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Versões descontinuadas** | 9 |
| **Cartões totalmente desativados** | 2 |

### Distribuição das versões
- **2 versões:** 14 cartões (evolução mais simples)
- **3 versões:** 11 cartões (evolução moderada)
- **4 versões:** 4 cartões (evolução significativa)
- **5 versões:** 1 cartão (mais evoluído: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Padrões comuns de versões

### Padrão 1: Adoção de chaves de tradução (v1 → v2)

**Afetados:** 15+ cartões

**Alteração:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Objetivo:** Permitir o suporte multilíngue

**Cartões:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS e outros

**Migração:** Segura - sem alterações funcionais

---

### Padrão 2: Integração de árvore de decisão (v2 → v3)

**Afetados:** 5 cartões

**Alteração:** Adição do parâmetro de árvore de decisão

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Objetivo:** Suportar os resultados da tabela de decisão

**Cartões:**
- tasks_create (v3 descontinuada)
- ACTION_TASK_FOR_GROUP (v3 descontinuada)
- DOC_USER_ASSIGN (v3 descontinuada)
- DOC_GROUP_ASSIGN (v3 descontinuada)
- ACTION_DECISION_TREE_CREATE_TASKS

**Estado:** Descontinuado - a abordagem de árvore de decisão era experimental

---

### Padrão 3: Evolução para tipo genérico (v3 → v4)

**Afetados:** 4 cartões

**Alteração:** "Task" passa a ser um tipo flexível de item de trabalho

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Objetivo:** Suportar Tasks, Tickets, Issues e outros tipos de item de trabalho

**Cartões:**
- tasks_create (v4 atual)
- ACTION_TASK_FOR_GROUP (v4 atual)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 atual)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 atual)

**Estado atual:** Ativo e recomendado

---

### Padrão 4: Parâmetros de tolerância (Cartões de PO)

**Afetados:** 6 cartões de comparação de PO

**Alteração:** Adição de suporte de tolerância/variação

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Objetivo:** Permitir variações aceitáveis na correspondência (por exemplo, uma diferença de preço de 2% é aceitável)

**Cartões principais:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (evoluiu para v5 com tolerância)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Benefício:** Critérios de correspondência mais realistas

---

### Padrão 5: Parâmetros de modo de comparação

**Afetados:** 3 cartões de comparação de PO

**Alteração:** Suporte para diferentes algoritmos de comparação

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Objetivo:** Métodos de comparação flexíveis

**Cartões:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Padrão 6: Acionadores de fluxo de trabalho

**Afetados:** Apenas STAUS_CHANGE

**Alteração:** Acionar automaticamente fluxos de trabalho na mudança de estado

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Objetivo:** Propagar as mudanças de estado entre fluxos de trabalho

---

## Cartões mais evoluídos

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 versões)

**Trajetória de evolução:** v2 → v3 → v4 → v5

- **v2:** Comparação básica de preço unitário
- **v3:** Mesma chave de tradução (v2)
- **v4:** Adicionado o parâmetro de modo de comparação
- **v5:** Adicionado o parâmetro de limiar de tolerância

**Atual:** v5 (com suporte de tolerância)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 versões)

**Trajetória de evolução:** v1 → v2 → v3 → v4

- **v1:** Correspondência básica de artigos (descontinuada)
- **v2:** Adicionado o parâmetro de método de comparação
- **v3:** Melhorado com chaves de tradução
- **v4:** Adicionado o parâmetro de modo de comparação

**Atual:** v4

**Evitar:** v1 (descontinuada)

---

### 3. tasks_create (4 versões)

**Trajetória de evolução:** v1 → v2 → v3 → v4

- **v1:** Implementação original (descontinuada)
- **v2:** Adicionado suporte de tradução (descontinuada)
- **v3:** Adicionada árvore de decisão (descontinuada)
- **v4:** Tipos genéricos de item de trabalho (atual)

**Atual:** v4 (recomendada)

**Cronologia:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Estado de descontinuação

### Versões totalmente descontinuadas (Não utilizar)

| Cartão | Versão | Motivo | Alternativa |
|------|---------|--------|-------------|
| tasks_create | v1 | Muito antiga | Utilizar v4 |
| tasks_create | v3 | Árvore de decisão descontinuada | Utilizar v4 |
| ACTION_TASK_FOR_GROUP | v3 | Árvore de decisão descontinuada | Utilizar v4 |
| DOC_USER_ASSIGN | v3 | Árvore de decisão descontinuada | Utilizar v2 |
| DOC_GROUP_ASSIGN | v3 | Árvore de decisão descontinuada | Utilizar v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Muito antiga | Utilizar v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Muito antiga | Utilizar v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Funcionalidades revertidas | Utilizar v3 |

### Cartões totalmente desativados (Não podem ser utilizados)

| Cartão | Versões | Notas |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Funcionalidade não suportada |
| RUN_SCRIPT | v2, v3 | Substituído por ACTION_RUN_DOCOPERATOR_SCRIPT |

---

## Recomendações de versão

### Por caso de utilização

**Criação de novos fluxos de trabalho:**
- Utilize sempre o **número de versão ativada mais elevado**
- Disponibiliza as funcionalidades e melhorias mais recentes
- Suportada e documentada

**Manutenção de fluxos de trabalho existentes:**
- Continue a utilizar a versão atual se funcionar
- Planeie a migração quando for viável
- Não há necessidade urgente de atualizar

**Migração de fluxos de trabalho antigos:**
- Identifique a versão atualmente em utilização
- Planeie a trajetória de atualização
- Teste exaustivamente antes de implementar

---

## Como funcionam as versões

### Seleção de versão
Ao criar um fluxo de trabalho, seleciona a versão de um cartão a utilizar. Exemplo:
- Utilize `tasks_create v4` para a criação de novas tarefas (recomendado)
- Utilize `tasks_create v2` se os sistemas antigos o exigirem (mais antiga, mas funciona)
- NÃO utilize `tasks_create v1` (descontinuada)

### Compatibilidade com versões anteriores
- As versões mais recentes não quebram os fluxos de trabalho mais antigos
- Os fluxos de trabalho antigos continuam a funcionar com a sua versão original
- Os fluxos de trabalho podem ser atualizados gradualmente

### Implementação técnica
As versões são geridas ao nível da base de dados:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## Para efeitos de documentação

### Compreender as informações de versão
Quando vê "Card v3" na documentação:
- Refere-se à versão 3 desse cartão específico
- Consulte a [Full Versioning Reference](../../docs/card_version.md) para mais detalhes
- Verifique qual a versão recomendada

### Verificar a sua versão
Para saber qual a versão que está a utilizar:
1. Abra o cartão no seu fluxo de trabalho
2. Verifique o número de versão apresentado
3. Compare com as recomendações dos guias

### Cronologia de evolução das versões
- **2024-2025:** Evolução em curso
- **Outubro de 2025:** Documentação completa do versionamento
- **Futuro:** Melhorias contínuas

---

## Documentação relacionada

### Referência abrangente
→ [Full Card Versioning Reference](../../docs/card_version.md)

Inclui:
- Todos os mais de 30 cartões com versões
- Evolução detalhada do texto de cada um
- Alterações específicas de parâmetros
- Consultas SQL para a procura de versões

### Guias específicos de cartões
→ [Workflow Guides](../)

Documentação de cada cartão com recomendações de versão

### Detalhes do histórico de versões
Cada guia inclui informações de versão e notas de migração

---

## Referência rápida

### Cartões com mais versões
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 versões
2. CONDITION_OC_TO_PO_ITEMS - 4 versões
3. tasks_create - 4 versões
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 versões
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 versões

### Padrão de evolução mais comum
**Adoção de chaves de tradução (v1 → v2)** - 15+ cartões

### Alteração mais significativa
**Evolução para tipo genérico (v3 → v4)** - Alterou de "Task" para um tipo flexível de item de trabalho

### Totalmente desativados
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Perguntas frequentes

### P: Que versão devo utilizar?
R: Utilize a **versão ativada mais elevada**, a menos que tenha um motivo específico para utilizar uma versão mais antiga.

### P: Posso atualizar o meu fluxo de trabalho para uma versão mais recente?
R: Sim, mas teste exaustivamente. Algumas versões têm requisitos de parâmetros diferentes.

### P: O que acontece se utilizar uma versão descontinuada?
R: Continua a funcionar, mas não obterá novas funcionalidades. Recomenda-se a migração.

### P: Posso utilizar um cartão desativado?
R: Não, os cartões desativados não podem ser utilizados. Utilize a alternativa recomendada.

### P: Como sei se o meu cartão precisa de ser atualizado?
R: Consulte a [Full Versioning Reference](../../docs/card_version.md) para o seu tipo de cartão e siga as recomendações.

---

## Boas práticas

1. **Novos fluxos de trabalho:** Utilize a versão estável mais recente
2. **Atualizações:** Verifique periodicamente se existem novas versões
3. **Testes:** Teste primeiro as atualizações de versão em sandbox
4. **Documentação:** Consulte os guias específicos dos cartões para detalhes de versão
5. **Migração:** Planeie as atualizações de forma incremental
6. **Suporte:** Contacte o suporte se surgirem questões de compatibilidade de versões

---

## Tabela de resumo

| Tipo de cartão | Versão atual | Total de versões | Estado | Notas |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Active | Mais evoluído; v3 descontinuada |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Active | Maior número de versões |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Active | v1 descontinuada |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Active | v3 descontinuada |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Active | v4 descontinuada/desativada |
| Maioria dos cartões | 2 | 2 | Active | Padrão v1 → v2 |

---

## Consulte também

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Última atualização:** 23 de outubro de 2025
**Fonte:** base de dados postgres-dev-docflow
**Estado:** Referência completa

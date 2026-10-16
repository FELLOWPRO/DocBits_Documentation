# Workflow Pattern Guides

**Versão:** 1.0 **Última atualização:** 23 de outubro de 2025

***

## Visão geral

Este diretório contém guias abrangentes de padrões de workflow que mostram como combinar vários cartões de workflow para resolver cenários de negócio comuns. Cada padrão traz instruções de implementação passo a passo, exemplos completos e boas práticas.

**O que são padrões de workflow?**

Padrões de workflow são soluções comprovadas e reutilizáveis para desafios comuns do processamento de documentos. Em vez de começar do zero, você pode usar estes padrões como modelos e adaptá-los às suas necessidades específicas.

***

## O Workflow Builder em resumo

Todos os padrões desta página são montados no **Workflow Builder**. Você chega a ele por **Workflow Dashboard → Workflow List → Add Workflow** (ou abrindo um workflow existente). O dashboard mostra o histórico de execuções e as taxas de sucesso/falha de todos os seus workflows:

<figure><img src="../../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard com totais de execuções, taxas de sucesso e falha, o gráfico de execuções de workflow e a atividade recente"><figcaption><p>O Workflow Dashboard — totais de execuções, taxas de sucesso/falha e atividade recente de cada workflow.</p></figcaption></figure>

A aba **Workflow List** lista todos os workflows com tipo, ordem de execução e gatilho. Use **Add Workflow** para criar um novo ou clique em um workflow para abri-lo no builder:

<figure><img src="../../../../.gitbook/assets/workflow_list.png" alt="Aba Workflow List com os workflows, seu tipo, ordem de execução e gatilho"><figcaption><p>A Workflow List — cada linha é um workflow que você pode abrir, ativar/desativar ou editar.</p></figcaption></figure>

Um workflow é construído a partir de três grupos de cartões — **When** (o gatilho), **And** (condições adicionais) e **Then** (as ações a executar). O exemplo abaixo é disparado por faturas pertencentes a uma suborganização e as atribui a um usuário:

<figure><img src="../../../../.gitbook/assets/workflow_add_button.png" alt="Canvas do Workflow Builder com os cartões When, And e Then"><figcaption><p>O canvas do Workflow Builder. Cada padrão abaixo é apenas uma combinação diferente de cartões When / And / Then.</p></figcaption></figure>

Clique em **Add Card** em qualquer grupo para abrir a biblioteca de cartões. Os cartões são organizados por categoria (Compare with Purchase Order, Partner Cards, Document Field, Date & Time, Document, Logic, Status, Table, Assignee, …), para que você encontre o bloco de construção que cada padrão pede:

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Caixa de diálogo Add Card mostrando as categorias de cartões e os cartões disponíveis"><figcaption><p>A biblioteca <strong>Add Card</strong> — todos os cartões citados nos padrões abaixo são escolhidos aqui.</p></figcaption></figure>

***

## Padrões disponíveis

### 1. [Padrão de integração de API](api-integration-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 45-60 minutos

Aprenda a integrar o DocBits com APIs externas para buscar, validar e armazenar dados de sistemas externos.

**Casos de uso:**

* Buscar preços em tempo real de sistemas externos
* Validar informações de fornecedores em bases de dados mestres
* Consultar detalhes de produtos em sistemas de catálogo
* Obter taxas de câmbio de serviços de moeda
* Verificar endereços com serviços de geocodificação

**Cartões usados:** CALL\_API, CONDITION\_HTTPS\_REQUEST\_STATUS, ACTION\_SET\_FIELD\_TO\_TEXT, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Ver o padrão completo →**](api-integration-pattern.md)

***

### 2. [Padrão de gerenciamento de tarefas](task-management-pattern.md)

**Complexidade:** Baixa a média | **Tempo de configuração:** 30-45 minutos

Domine a criação, a atribuição, o acompanhamento e o gerenciamento de tarefas em workflows do DocBits para processos de aprovação e revisão.

**Casos de uso:**

* Criar workflows de aprovação
* Atribuir tarefas de revisão a usuários
* Tratar exceções que exigem intervenção humana
* Escalar problemas para gestores
* Criar cadeias de aprovação em vários níveis
* Acompanhar a conclusão e os prazos das tarefas

**Cartões usados:** tasks\_create, ACTION\_ASSIGN\_TO\_USER, ACTION\_SEND\_EMAIL\_TO\_GROUPS, CONDITION\_TASK\_STATUS

[**Ver o padrão completo →**](task-management-pattern.md)

***

### 3. [Padrão de PO Matching](po-matching-pattern.md)

**Complexidade:** Média a alta | **Tempo de configuração:** 60-90 minutos

Implemente workflows completos de PO Matching para validar faturas em relação aos pedidos de compra, com roteamento baseado em tolerâncias.

**Casos de uso:**

* Validar faturas em relação aos pedidos de compra
* Detectar erros de preço antes do pagamento
* Identificar divergências de quantidade
* Aplicar controles de compras
* Evitar pagamentos duplicados
* Automatizar o three-way matching

**Cartões usados:** PURCHASE\_ORDER\_FULL\_MATCH, CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE, CONDITION\_DOC\_TO\_PO\_QUANTITY, CONDITION\_DOC\_TO\_PO\_TAX\_LINES

[**Ver o padrão completo →**](po-matching-pattern.md)

***

### 4. [Padrão de lógica de decisão](decision-logic-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 30-45 minutos

Implemente árvores de decisão complexas e lógica de roteamento condicional para processar documentos por caminhos diferentes com base em regras de negócio.

**Casos de uso:**

* Rotear documentos por limites de valor
* Aplicar regras diferentes a tipos de documento diferentes
* Implementar lógica de aprovação em vários níveis
* Tratar políticas de negócio complexas
* Criar roteamento dinâmico com base em vários critérios
* Implementar matrizes de aprovação

**Cartões usados:** CONDITION\_DOC\_FIELD\_AMOUNT, CONDITION\_DOC\_TYPE\_IS\_ISNOT, CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT, ACTION\_ASSIGN\_TO\_USER

[**Ver o padrão completo →**](decision-logic-pattern.md)

***

### 5. [Padrão de transformação de dados](data-transformation-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 30-45 minutos

Transforme, calcule, formate e enriqueça dados de documentos para preparar a exportação, fazer cálculos e padronizar formatos.

**Casos de uso:**

* Calcular totais, subtotais e impostos
* Converter moedas ou unidades
* Formatar datas, números e texto
* Derivar valores de campos existentes
* Enriquecer dados com fontes externas
* Padronizar formatos de dados
* Validar cálculos

**Cartões usados:** ACTION\_CALCULATE\_FIELD, ACTION\_SET\_FIELD\_TO\_TEXT, ACTION\_COPY\_FIELD\_VALUE, CALL\_API, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Ver o padrão completo →**](data-transformation-pattern.md)

***

## Guia de seleção de padrões

### Por complexidade

| Complexidade      | Padrões                                                                                                                                                                                               | Ideal para                                |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------- |
| **Baixa a média** | [Gerenciamento de tarefas](task-management-pattern.md)                                                                                                                                                | Iniciantes, workflows simples             |
| **Média**         | <p><a href="api-integration-pattern.md">Integração de API</a><br><a href="decision-logic-pattern.md">Lógica de decisão</a><br><a href="data-transformation-pattern.md">Transformação de dados</a></p> | Usuários intermediários, workflows padrão |
| **Média a alta**  | [PO Matching](po-matching-pattern.md)                                                                                                                                                                 | Usuários avançados, validação complexa    |

***

### Por caso de uso

| Preciso...                             | Use este padrão                                                    |
| -------------------------------------- | ------------------------------------------------------------------ |
| Integrar com sistemas externos         | [Padrão de integração de API](api-integration-pattern.md)          |
| Criar workflows de aprovação           | [Padrão de gerenciamento de tarefas](task-management-pattern.md)   |
| Validar em relação a pedidos de compra | [Padrão de PO Matching](po-matching-pattern.md)                    |
| Rotear com base em condições           | [Padrão de lógica de decisão](decision-logic-pattern.md)           |
| Calcular e transformar dados           | [Padrão de transformação de dados](data-transformation-pattern.md) |

***

### Por setor/departamento

| Setor/Departamento         | Padrões recomendados                                                                                                                                    |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Finanças/Contabilidade** | [PO Matching](po-matching-pattern.md), [Gerenciamento de tarefas](task-management-pattern.md), [Transformação de dados](data-transformation-pattern.md) |
| **Compras**                | [PO Matching](po-matching-pattern.md), [Lógica de decisão](decision-logic-pattern.md), [Integração de API](api-integration-pattern.md)                  |
| **Operações**              | [Gerenciamento de tarefas](task-management-pattern.md), [Lógica de decisão](decision-logic-pattern.md)                                                  |
| **TI/Integração**          | [Integração de API](api-integration-pattern.md), [Transformação de dados](data-transformation-pattern.md)                                               |
| **Todos os departamentos** | [Lógica de decisão](decision-logic-pattern.md), [Gerenciamento de tarefas](task-management-pattern.md)                                                  |

***

## Como usar estes padrões

### Passo 1: Escolha um padrão

1. Leia as descrições dos padrões acima
2. Identifique qual padrão corresponde ao seu caso de uso
3. Confira a complexidade e o tempo de configuração estimado
4. Leia a seção "When to Use" no guia do padrão

### Passo 2: Revise os pré-requisitos

Cada guia de padrão lista:

* Conhecimentos necessários
* Guias relacionados para ler antes
* Cartões que serão usados
* Requisitos de configuração

### Passo 3: Siga as instruções passo a passo

Cada padrão traz:

* Exemplo completo de workflow
* Guia de implementação passo a passo
* Modelos de configuração
* Exemplos reais
* Dicas de solução de problemas

### Passo 4: Personalize conforme suas necessidades

* Adapte o exemplo às suas regras de negócio
* Ajuste limites e tolerâncias
* Modifique a lógica de roteamento
* Adicione ou remova etapas conforme necessário
* Teste bem antes de usar em produção

### Passo 5: Monitore e otimize

* Acompanhe o desempenho do workflow
* Monitore as taxas de sucesso
* Colete o feedback dos usuários
* Refine a configuração
* Documente as personalizações

***

## Combinações de padrões

Muitos cenários reais exigem a combinação de vários padrões:

### Exemplo 1: Processamento completo de faturas

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Exemplo 2: Aprovação de faturas de alto valor

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Exemplo 3: Tratamento de exceções

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

***

## Modelos de padrões

Cada padrão inclui estas seções padronizadas:

1. **Overview** - O que o padrão faz
2. **When to Use** - Casos de uso adequados
3. **Complete Example** - Cenário real
4. **Step-by-Step** - Instruções de implementação
5. **Configuration** - Modelos de configuração dos cartões
6. **Workflow Diagram** - Representação visual
7. **Advanced Variations** - Implementações alternativas
8. **Error Handling** - Problemas comuns e soluções
9. **Testing Checklist** - Etapas de validação
10. **Related Patterns** - Padrões complementares
11. **Related Guides** - Documentação de referência

***

## Obtendo ajuda

### Recursos de suporte para padrões

**Documentação:**

* [Índice completo do guia de workflows](../../)
* [Guias de cartões individuais](../then/action/)
* [Referência dos cartões de condição](../condition-cards-complete-guide.md)
* [Mapa de vínculos de workflows](../../../../../WORKFLOW_LINKING_MAP.md)

**Recursos adicionais:**

* [Guia de referência rápida](../../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
* [Notas de versão de outubro de 2025](../../changelog/2025-10-october.md)
* [Referência de versionamento de cartões](../../../../docs/card_version.md)

**Contato:**

* Feedback sobre padrões: docs@docbits.com
* Suporte técnico: support@docbits.com
* Ajuda com a implementação: consulting@docbits.com

***

## Estatísticas dos padrões

| Métrica                       | Valor                 |
| ----------------------------- | --------------------- |
| **Total de padrões**          | 5                     |
| **Total de cartões cobertos** | 30+                   |
| **Documentação combinada**    | \~1.200 linhas        |
| **Cenários de exemplo**       | 25+                   |
| **Modelos de configuração**   | 15+                   |
| **Diagramas de workflow**     | 5 diagramas completos |
| **Referências cruzadas**      | 87+ links internos    |

***

## Contribuindo com padrões

Você tem um padrão de workflow que pode ajudar outras pessoas?

**Diretrizes para contribuir com padrões:**

1. **Documente seu workflow**
   * Cenário de negócio claro
   * Implementação passo a passo
   * Exemplos de configuração funcionais
   * Resultados de testes reais
2. **Siga o modelo de padrão**
   * Use a estrutura de seções padrão
   * Inclua todos os elementos obrigatórios
   * Forneça diagramas/exemplos
   * Adicione um guia de solução de problemas
3. **Envie para revisão**
   * Envie um e-mail para: docs@docbits.com
   * Inclua: descrição do padrão, casos de uso, guia de implementação
   * Vamos revisar e, possivelmente, adicioná-lo à documentação oficial

**Benefícios:**

* Ajude outros usuários do DocBits
* Seja reconhecido na documentação
* Melhore a base de conhecimento do produto
* Receba feedback sobre a sua implementação

***

## Histórico de alterações

### Versão 1.0 (23 de outubro de 2025)

* Lançamento inicial de 5 padrões de workflow completos
* Padrão de integração de API adicionado
* Padrão de gerenciamento de tarefas adicionado
* Padrão de PO Matching adicionado
* Padrão de lógica de decisão adicionado
* Padrão de transformação de dados adicionado
* Vínculos de referência cruzada implementados (87 links)
* Guia de seleção de padrões criado

***

## Próximos passos

**Novo em padrões de workflow?**

1. Comece pelo [Padrão de gerenciamento de tarefas](task-management-pattern.md) - o mais fácil de entender
2. Veja o [Padrão de lógica de decisão](decision-logic-pattern.md) - fundamental para todos os workflows
3. Explore o [Padrão de integração de API](api-integration-pattern.md) - uma necessidade comum de integração

**Pronto para implementar?**

1. Escolha seu padrão na lista acima
2. Leia o guia completo do padrão
3. Revise os pré-requisitos e os guias relacionados
4. Siga as instruções passo a passo
5. Teste com documentos de exemplo
6. Publique em produção
7. Monitore e otimize

**Precisa de mais ajuda?**

* Consulte a [Visão geral da documentação de workflows](../../)
* Confira o [Guia de referência rápida](../../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
* Entre em contato com a equipe de suporte

***

**Última atualização:** 23 de outubro de 2025 **Mantido por:** Equipe de Documentação **Versão:** 1.0

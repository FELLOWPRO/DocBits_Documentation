# Workflow Pattern Guides

**Versão:** 1.0 **Última atualização:** 23 de outubro de 2025

***

## Visão geral

Esta secção contém guias abrangentes de padrões de workflow que demonstram como combinar várias cartas de workflow para resolver cenários de negócio comuns. Cada padrão fornece instruções de implementação passo a passo, exemplos completos e boas práticas.

**O que são padrões de workflow?**

Os padrões de workflow são soluções comprovadas e reutilizáveis para desafios comuns no processamento de documentos. Em vez de começar do zero, pode utilizar estes padrões como modelos e adaptá-los às suas necessidades específicas.

***

## O Workflow Builder num relance

Cada padrão desta página é montado no **Workflow Builder**. Acede-lhe através de **Workflow Dashboard → Workflow List → Add Workflow** (ou abrindo um workflow existente). O dashboard mostra o histórico de execuções e as taxas de êxito/falha de todos os seus workflows:

<figure><img src="../../../../.gitbook/assets/workflow_dashboard.png" alt="Workflow Dashboard com totais de execuções, taxas de êxito e falha, o gráfico de execuções de workflow e a atividade recente"><figcaption><p>O Workflow Dashboard — totais de execuções, taxas de êxito/falha e atividade recente de cada workflow.</p></figcaption></figure>

O separador **Workflow List** lista todos os workflows com o respetivo tipo, ordem de execução e acionador. Utilize **Add Workflow** para criar um novo ou clique num workflow para o abrir no builder:

<figure><img src="../../../../.gitbook/assets/workflow_list.png" alt="Separador Workflow List com os workflows por tipo, ordem de execução e acionador"><figcaption><p>A Workflow List — cada linha é um workflow que pode abrir, ativar/desativar ou editar.</p></figcaption></figure>

Um workflow é construído a partir de três grupos de cartas — **When** (o acionador), **And** (condições adicionais) e **Then** (as ações a executar). O exemplo abaixo é acionado em faturas pertencentes a uma sub-organização e atribui-as a um utilizador:

<figure><img src="../../../../.gitbook/assets/workflow_add_button.png" alt="Canvas do Workflow Builder com cartas When, And e Then"><figcaption><p>O canvas do Workflow Builder. Cada padrão abaixo é apenas uma combinação diferente de cartas When / And / Then.</p></figcaption></figure>

Clique em **Add Card** em qualquer grupo para abrir a biblioteca de cartas. As cartas estão organizadas por categoria (Compare with Purchase Order, Partner Cards, Document Field, Date & Time, Document, Logic, Status, Table, Assignee, …), para que encontre o bloco de construção que cada padrão exige:

<figure><img src="../../../../.gitbook/assets/workflow_add_card_picker.png" alt="Diálogo Add Card com as categorias de cartas e as cartas disponíveis"><figcaption><p>A biblioteca <strong>Add Card</strong> — cada carta referida nos padrões abaixo é escolhida a partir daqui.</p></figcaption></figure>

***

## Padrões disponíveis

### 1. [Padrão de Integração de API](api-integration-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 45–60 minutos

Aprenda a integrar o DocBits com APIs externas para obter, validar e armazenar dados de sistemas externos.

**Casos de uso:**

* Obter preços em tempo real de sistemas externos
* Validar informações de fornecedores em bases de dados de referência
* Consultar detalhes de produtos em sistemas de catálogo
* Obter taxas de câmbio de serviços de moeda
* Verificar endereços com serviços de geocodificação

**Cartas utilizadas:** CALL\_API, CONDITION\_HTTPS\_REQUEST\_STATUS, ACTION\_SET\_FIELD\_TO\_TEXT, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Ver padrão completo →**](api-integration-pattern.md)

***

### 2. [Padrão de Gestão de Tarefas](task-management-pattern.md)

**Complexidade:** Baixa-Média | **Tempo de configuração:** 30–45 minutos

Domine a arte de criar, atribuir, acompanhar e gerir tarefas em workflows do DocBits para processos de aprovação e revisão.

**Casos de uso:**

* Criar workflows de aprovação
* Atribuir tarefas de revisão a utilizadores
* Tratar exceções que exigem intervenção humana
* Escalar problemas para responsáveis
* Criar cadeias de aprovação em vários níveis
* Acompanhar a conclusão e os prazos das tarefas

**Cartas utilizadas:** tasks\_create, ACTION\_ASSIGN\_TO\_USER, ACTION\_SEND\_EMAIL\_TO\_GROUPS, CONDITION\_TASK\_STATUS

[**Ver padrão completo →**](task-management-pattern.md)

***

### 3. [Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md)

**Complexidade:** Média-Alta | **Tempo de configuração:** 60–90 minutos

Implemente workflows abrangentes de correspondência de encomendas para validar faturas contra encomendas com encaminhamento baseado em tolerâncias.

**Casos de uso:**

* Validar faturas contra encomendas
* Detetar erros de preços antes do pagamento
* Identificar discrepâncias de quantidade
* Aplicar controlos de aprovisionamento
* Evitar pagamentos em duplicado
* Automatizar a correspondência de três vias

**Cartas utilizadas:** PURCHASE\_ORDER\_FULL\_MATCH, CONDITION\_DOC\_TO\_PO\_UNIT\_PRICE, CONDITION\_DOC\_TO\_PO\_QUANTITY, CONDITION\_DOC\_TO\_PO\_TAX\_LINES

[**Ver padrão completo →**](po-matching-pattern.md)

***

### 4. [Padrão de Lógica de Decisão](decision-logic-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 30–45 minutos

Implemente árvores de decisão complexas e lógica de encaminhamento condicional para processar documentos através de diferentes caminhos com base em regras de negócio.

**Casos de uso:**

* Encaminhar documentos por limiares de valor
* Aplicar regras diferentes a tipos de documento diferentes
* Implementar lógica de aprovação em vários níveis
* Tratar políticas de negócio complexas
* Criar encaminhamento dinâmico com base em múltiplos critérios
* Implementar matrizes de aprovação

**Cartas utilizadas:** CONDITION\_DOC\_FIELD\_AMOUNT, CONDITION\_DOC\_TYPE\_IS\_ISNOT, CONDITION\_SUPPLIER\_STATUS\_IS\_ISNOT, ACTION\_ASSIGN\_TO\_USER

[**Ver padrão completo →**](decision-logic-pattern.md)

***

### 5. [Padrão de Transformação de Dados](data-transformation-pattern.md)

**Complexidade:** Média | **Tempo de configuração:** 30–45 minutos

Transforme, calcule, formate e enriqueça dados de documentos para preparar a exportação, efetuar cálculos e normalizar formatos.

**Casos de uso:**

* Calcular totais, subtotais, impostos
* Converter moedas ou unidades
* Formatar datas, números, texto
* Derivar valores de campos existentes
* Enriquecer dados a partir de fontes externas
* Normalizar formatos de dados
* Validar cálculos

**Cartas utilizadas:** ACTION\_CALCULATE\_FIELD, ACTION\_SET\_FIELD\_TO\_TEXT, ACTION\_COPY\_FIELD\_VALUE, CALL\_API, CONDITION\_COMPARE\_TWO\_DOCFIELD\_VALUES

[**Ver padrão completo →**](data-transformation-pattern.md)

***

## Guia de seleção de padrões

### Por complexidade

| Complexidade    | Padrões                                                                                                                                                                                               | Melhor para                                |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------ |
| **Baixa-Média** | [Gestão de Tarefas](task-management-pattern.md)                                                                                                                                                       | Iniciantes, workflows simples              |
| **Média**       | <p><a href="api-integration-pattern.md">Integração de API</a><br><a href="decision-logic-pattern.md">Lógica de Decisão</a><br><a href="data-transformation-pattern.md">Transformação de Dados</a></p> | Utilizadores intermédios, workflows padrão |
| **Média-Alta**  | [PO Matching](po-matching-pattern.md)                                                                                                                                                                 | Utilizadores avançados, validação complexa |

***

### Por caso de uso

| Preciso de…                      | Utilizar este padrão                                                            |
| -------------------------------- | ------------------------------------------------------------------------------- |
| Integrar com sistemas externos   | [Padrão de Integração de API](api-integration-pattern.md)                       |
| Criar workflows de aprovação     | [Padrão de Gestão de Tarefas](task-management-pattern.md)                       |
| Validar contra encomendas        | [Padrão de Correspondência de Encomendas (PO Matching)](po-matching-pattern.md) |
| Encaminhar com base em condições | [Padrão de Lógica de Decisão](decision-logic-pattern.md)                        |
| Calcular e transformar dados     | [Padrão de Transformação de Dados](data-transformation-pattern.md)              |

***

### Por setor/departamento

| Setor/Departamento         | Padrões recomendados                                                                                                                             |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Finanças/Contabilidade** | [PO Matching](po-matching-pattern.md), [Gestão de Tarefas](task-management-pattern.md), [Transformação de Dados](data-transformation-pattern.md) |
| **Compras**                | [PO Matching](po-matching-pattern.md), [Lógica de Decisão](decision-logic-pattern.md), [Integração de API](api-integration-pattern.md)           |
| **Operações**              | [Gestão de Tarefas](task-management-pattern.md), [Lógica de Decisão](decision-logic-pattern.md)                                                  |
| **TI/Integração**          | [Integração de API](api-integration-pattern.md), [Transformação de Dados](data-transformation-pattern.md)                                        |
| **Todos os departamentos** | [Lógica de Decisão](decision-logic-pattern.md), [Gestão de Tarefas](task-management-pattern.md)                                                  |

***

## Como utilizar estes padrões

### Passo 1: Escolher um padrão

1. Reveja as descrições dos padrões acima
2. Identifique qual o padrão que corresponde ao seu caso de uso
3. Verifique a complexidade e o tempo de configuração estimado
4. Reveja a secção «Quando utilizar» no guia do padrão

### Passo 2: Rever os pré-requisitos

Cada guia de padrão lista:

* Conhecimentos necessários
* Guias relacionados a ler primeiro
* Cartas que serão utilizadas
* Requisitos de configuração

### Passo 3: Seguir as instruções passo a passo

Cada padrão fornece:

* Exemplo completo de workflow
* Guia de implementação passo a passo
* Modelos de configuração
* Exemplos do mundo real
* Sugestões de resolução de problemas

### Passo 4: Personalizar conforme as suas necessidades

* Adapte o exemplo às suas regras de negócio
* Ajuste limiares e tolerâncias
* Modifique a lógica de encaminhamento
* Acrescente/remova passos conforme necessário
* Teste exaustivamente antes da utilização em produção

### Passo 5: Monitorizar e otimizar

* Acompanhe o desempenho do workflow
* Monitorize as taxas de êxito
* Recolha feedback dos utilizadores
* Refine a configuração
* Documente as personalizações

***

## Combinações de padrões

Muitos cenários do mundo real exigem a combinação de vários padrões:

### Exemplo 1: Processamento completo de faturas

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Exemplo 2: Aprovação de faturas de valor elevado

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

Cada padrão inclui estas secções normalizadas:

1. **Visão geral** – O que o padrão faz
2. **Quando utilizar** – Casos de uso adequados
3. **Exemplo completo** – Cenário do mundo real
4. **Passo a passo** – Instruções de implementação
5. **Configuração** – Modelos de configuração de cartas
6. **Diagrama de workflow** – Representação visual
7. **Variantes avançadas** – Implementações alternativas
8. **Tratamento de erros** – Problemas comuns e soluções
9. **Lista de verificação de testes** – Passos de validação
10. **Padrões relacionados** – Padrões complementares
11. **Guias relacionados** – Documentação de referência

***

## Obter ajuda

### Recursos de apoio para padrões

**Documentação:**

* [Índice completo do guia de workflows](../../)
* [Guias de cartas individuais](../then/action/)
* [Referência de cartas de condição](../condition-cards-complete-guide.md)

**Contacto:**

* Feedback sobre padrões: docs@docbits.com
* Suporte técnico: support@docbits.com
* Ajuda na implementação: consulting@docbits.com

***

## Próximos passos

**Novo nos padrões de workflow?**

1. Comece com o [Padrão de Gestão de Tarefas](task-management-pattern.md) – o mais fácil de entender
2. Reveja o [Padrão de Lógica de Decisão](decision-logic-pattern.md) – fundamental para todos os workflows
3. Explore o [Padrão de Integração de API](api-integration-pattern.md) – necessidade de integração frequente

**Pronto para implementar?**

1. Escolha o seu padrão da lista acima
2. Leia o guia completo do padrão
3. Verifique os pré-requisitos e os guias relacionados
4. Siga as instruções passo a passo
5. Teste com documentos de exemplo
6. Avance para produção
7. Monitorize e otimize

***

**Última atualização:** 23 de outubro de 2025 **Mantido por:** Equipa de Documentação **Versão:** 1.0

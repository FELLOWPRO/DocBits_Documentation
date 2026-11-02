# Contabilização automática

## Tabela `public.auto_accounting`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `supplier_name`: nome do fornecedor
* `description`: interno
* `item_number`: interno
* `line_amount`: precisão dupla
* `total_amount`: precisão dupla
* `mapped_amount`: precisão dupla
* `ledger_account`: interno
* `doc_id`: interno

### Análise e descrição

## Documentação técnica da tabela `public.auto_accounting`

### Introdução

A tabela `public.auto_accounting` parece ter sido projetada para gerenciar e armazenar dados contábeis relacionados a diversos fornecedores e organizações. A tabela registra informações sobre transações financeiras, incluindo valores e contas contábeis, que são essenciais para relatórios e análises financeiras.

### Descrição das colunas

#### id

* **Significado**: um identificador único para cada registro da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que representa cada entrada de forma única.
* **Observação**: garante que cada registro possa ser identificado de forma distinta.

#### org\_id

* **Significado**: identificador da organização associada ao lançamento contábil.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que faz referência a uma organização em uma tabela pai.
* **Observação**: usado para associar os lançamentos contábeis a organizações específicas.

#### supplier\_name

* **Significado**: o nome do fornecedor envolvido na transação.
* **Função**: campo descritivo.
* **Conteúdo típico**: texto que representa o nome do fornecedor, como "Fellow Consulting AG".
* **Observação**: fornece informações sobre o fornecedor relacionado à transação.

#### description

* **Significado**: uma breve descrição da transação ou do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: texto que descreve a transação, como o nome de um item ("apple" ou "Peaches").
* **Observação**: útil para entender a natureza da transação.

#### item\_number

* **Significado**: identificador de um item específico envolvido na transação.
* **Função**: campo descritivo.
* **Conteúdo típico**: pode ser um identificador de produto ou SKU, embora não haja dados de exemplo.
* **Observação**: útil para acompanhar ou referenciar itens específicos.

#### line\_amount

* **Significado**: o valor monetário de uma linha específica da transação.
* **Função**: campo financeiro.
* **Conteúdo típico**: um valor decimal que representa o valor de uma linha individual.
* **Observação**: importante para análises financeiras detalhadas no nível da linha.

#### total\_amount

* **Significado**: o valor monetário total da transação.
* **Função**: campo financeiro.
* **Conteúdo típico**: um valor decimal que representa o valor total da transação.
* **Observação**: representa a soma de todos os valores de linha de uma transação.

#### mapped\_amount

* **Significado**: o valor que foi alocado ou mapeado para uma conta específica.
* **Função**: campo financeiro.
* **Conteúdo típico**: um valor decimal que indica quanto da transação foi alocado.
* **Observação**: útil para entender como os recursos são distribuídos entre as contas.

#### ledger\_account

* **Significado**: o número da conta no razão em que a transação é registrada.
* **Função**: campo descritivo.
* **Conteúdo típico**: texto que representa um número de conta, como "2200" ou "2500".
* **Observação**: essencial para fins contábeis, para acompanhar onde as transações são lançadas.

#### doc\_id

* **Significado**: um identificador de um documento ou registro relacionado.
* **Função**: chave estrangeira ou referência.
* **Conteúdo típico**: uma string UUID ou outro identificador que faz referência a documentos relacionados.
* **Observação**: ajuda a associar transações a documentos ou registros específicos para fins de rastreabilidade.

Esta documentação oferece uma visão geral detalhada da tabela `public.auto_accounting`, descrevendo sua estrutura e a finalidade de cada coluna para ajudar desenvolvedores e administradores de banco de dados a entender e utilizar os dados de forma eficaz.

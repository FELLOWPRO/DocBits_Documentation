# Tolerância de correspondência de pedidos de compra

## Tabela `public.po_match_tolerance`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `item_number`: interno
* `supplier_item_number`: interno
* `description`: interno
* `unit_price_tolerance`: precisão dupla
* `quantity_tolerance`: precisão dupla
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `unit_price_tolerance_type`: interno
* `quantity_tolerance_type`: interno

### Análise e descrição

## Documentação técnica da tabela `public.po_match_tolerance`

### Introdução

A tabela `public.po_match_tolerance` foi projetada para gerenciar e armazenar os níveis de tolerância associados aos processos de correspondência de pedidos de compra (PO). Isso normalmente envolve as discrepâncias permitidas nos preços unitários e nas quantidades entre as mercadorias pedidas e as recebidas. Cada entrada da tabela representa as configurações de tolerância de itens específicos, o que pode ajudar as organizações a garantir consistência e precisão nos processos de compras.

### Descrição das colunas

#### id

* **Significado**: um identificador único de cada entrada da tabela.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que identifica de forma única cada registro de configuração de tolerância.

#### org\_id

* **Significado**: identificador da organização associada às configurações de tolerância.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que se vincula à organização dentro do sistema.

#### item\_number

* **Significado**: o número do item específico para o qual as configurações de tolerância são definidas.
* **Função**: identificador de negócio.
* **Conteúdo típico**: uma string que representa o código ou o número do item no estoque da organização.

#### supplier\_item\_number

* **Significado**: o número do item conforme informado pelo fornecedor.
* **Função**: identificador de negócio.
* **Conteúdo típico**: uma string que pode ser `None` se não for informada e que representa o código ou o número do item para o fornecedor.

#### description

* **Significado**: uma descrição textual do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string com detalhes sobre o item, que pode ser `None`.

#### unit\_price\_tolerance

* **Significado**: a variação permitida no preço unitário do item.
* **Função**: regra de negócio.
* **Conteúdo típico**: um valor numérico que indica a tolerância percentual ou em valor absoluto no preço unitário.

#### quantity\_tolerance

* **Significado**: a variação permitida na quantidade do item.
* **Função**: regra de negócio.
* **Conteúdo típico**: um valor numérico que indica a tolerância percentual ou em valor absoluto na quantidade.

#### created\_by

* **Significado**: identificador do usuário que criou a entrada.
* **Função**: campo de auditoria/registro.
* **Conteúdo típico**: um número inteiro que normalmente referencia um ID de usuário no sistema.

#### created\_on

* **Significado**: o timestamp de quando a entrada foi criada.
* **Função**: campo de auditoria/registro.
* **Conteúdo típico**: um valor de data e hora com fuso horário que indica a data e a hora de criação.

#### last\_modified\_on

* **Significado**: o timestamp da última modificação da entrada.
* **Função**: campo de auditoria/registro.
* **Conteúdo típico**: um valor de data e hora com fuso horário que indica quando o registro foi atualizado pela última vez, podendo ser `None` se não foi modificado.

#### is\_deleted

* **Significado**: indica se a entrada foi excluída logicamente.
* **Função**: campo técnico/indicador de exclusão lógica.
* **Conteúdo típico**: um valor booleano em que `False` significa ativa e `True` significa excluída logicamente.

#### unit\_price\_tolerance\_type

* **Significado**: define o tipo da tolerância do preço unitário (por exemplo, percentual ou valor absoluto).
* **Função**: regra de negócio.
* **Conteúdo típico**: uma string, frequentemente 'value', que indica o tipo de medida da tolerância.

#### quantity\_tolerance\_type

* **Significado**: define o tipo da tolerância da quantidade (por exemplo, percentual ou valor absoluto).
* **Função**: regra de negócio.
* **Conteúdo típico**: uma string, frequentemente 'value', que indica o tipo de medida da tolerância.

Esta documentação oferece uma visão geral detalhada de cada campo da tabela `public.po_match_tolerance`, com informações sobre seu possível conteúdo e sua função no contexto da gestão de pedidos de compra.

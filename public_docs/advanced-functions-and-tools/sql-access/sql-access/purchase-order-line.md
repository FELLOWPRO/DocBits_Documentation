# Linha de pedido de compra

## Tabela `public.purchase_order_line`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `purchase_order_id`: interno
* `purchase_order_number`: interno
* `line_number`: interno
* `item_id`: interno
* `supplier_item_id`: interno
* `description`: interno
* `quantity`: precisão dupla
* `unit_code`: interno
* `unit_price`: precisão dupla
* `total_amount`: precisão dupla
* `currency`: interno
* `status`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `deleted_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `open_quantity`: precisão dupla
* `received_quantity`: precisão dupla
* `confirmed_quantity`: precisão dupla
* `note`: texto
* `sub_org_id`: interno
* `sub_line_number`: interno
* `unit_price_per`: precisão dupla
* `buyer_id`: interno
* `buyer_name`: interno
* `unit_code_price`: interno
* `geo_code`: interno
* `promised_delivery_date`: timestamp com fuso horário
* `delivery_method`: interno
* `requested_ship_date`: data
* `received_base_mou_quantity`: precisão dupla
* `extended_amount`: precisão dupla

### Análise e descrição

## Documentação técnica da tabela `public.purchase_order_line`

### Introdução

A tabela `public.purchase_order_line` foi projetada para armazenar informações detalhadas sobre cada item de linha de um pedido de compra. Ela registra vários atributos de uma linha de pedido de compra, como detalhes do item, quantidades, preços e status. Essa tabela é fundamental para gerenciar e acompanhar os pedidos de compra e seu status de atendimento em um contexto organizacional.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada item de linha do pedido de compra.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID que identifica de forma única a linha do pedido de compra.

#### org\_id

* **Significado**: identificador da organização associada ao pedido de compra.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que referencia uma organização.

#### purchase\_order\_id

* **Significado**: identificador do pedido de compra ao qual o item de linha pertence.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que referencia um pedido de compra.

#### purchase\_order\_number

* **Significado**: o número atribuído ao pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o número do pedido de compra.

#### line\_number

* **Significado**: o número de linha do item dentro do pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que indica a sequência da linha no pedido de compra.

#### item\_id

* **Significado**: identificador do item que está sendo pedido.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string que representa o código do item.

#### supplier\_item\_id

* **Significado**: identificador do item específico do fornecedor.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string, que pode ser nula se não for informada pelo fornecedor.

#### description

* **Significado**: descrição do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma descrição textual do item.

#### quantity

* **Significado**: o número de unidades pedidas.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que indica a quantidade pedida.

#### unit\_code

* **Significado**: código que representa a unidade de medida do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa unidades, por exemplo 'EA' para unidade.

#### unit\_price

* **Significado**: preço por unidade do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que representa o preço por unidade.

#### total\_amount

* **Significado**: valor total do item de linha (quantidade \* preço unitário).
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que representa o valor total.

#### currency

* **Significado**: moeda em que a compra é feita.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o código da moeda, por exemplo 'USD'.

#### status

* **Significado**: status atual da linha do pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que indica o status, por exemplo 'Received' e 'Invoiced'.

#### created\_by

* **Significado**: identificador do usuário que criou a entrada.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um número inteiro que representa o ID do usuário.

#### created\_on

* **Significado**: timestamp de quando a entrada foi criada.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp com informações de fuso horário.

#### last\_modified\_on

* **Significado**: timestamp da última modificação.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp com informações de fuso horário, que pode ser nulo se nunca foi modificada.

#### deleted\_on

* **Significado**: timestamp de quando a entrada foi marcada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp com informações de fuso horário, que pode ser nulo se não foi excluída.

#### is\_deleted

* **Significado**: indica se a entrada foi marcada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano (true/false).

#### open\_quantity

* **Significado**: quantidade ainda não recebida ou faturada.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico, normalmente zero se foi totalmente recebida.

#### received\_quantity

* **Significado**: quantidade que foi recebida.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que indica a quantidade recebida.

#### confirmed\_quantity

* **Significado**: quantidade confirmada pelo fornecedor.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico, que pode ser nulo se não foi confirmada.

#### note

* **Significado**: observações adicionais sobre a linha do pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: texto, que pode incluir instruções especiais ou comentários.

#### sub\_org\_id

* **Significado**: identificador da suborganização associada à linha do pedido de compra.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string, possivelmente nula se não for aplicável.

#### sub\_line\_number

* **Significado**: número da sublinha dentro do pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa a sequência da sublinha.

#### unit\_price\_per

* **Significado**: preço unitário base do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que representa o preço unitário base.

#### buyer\_id

* **Significado**: identificador do comprador responsável pela compra.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string que representa o ID do comprador.

#### buyer\_name

* **Significado**: nome do comprador responsável.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o nome do comprador.

#### unit\_code\_price

* **Significado**: código da unidade relacionado ao preço.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string, semelhante a unit\_code.

#### geo\_code

* **Significado**: código geográfico da entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa um local geográfico.

#### promised\_delivery\_date

* **Significado**: data prometida para a entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: um timestamp com informações de fuso horário.

#### delivery\_method

* **Significado**: método de entrega da linha do pedido de compra.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa o método de entrega.

#### requested\_ship\_date

* **Significado**: data solicitada para o envio.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor de data.

#### received\_base\_mou\_quantity

* **Significado**: quantidade recebida em unidades de medida base.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que indica a quantidade recebida na unidade de medida base (MOU).

#### extended\_amount

* **Significado**: valor estendido do item de linha.
* **Função**: campo descritivo.
* **Conteúdo típico**: um valor numérico que representa o valor estendido, que pode ser igual a total\_amount se não houver descontos ou encargos adicionais.

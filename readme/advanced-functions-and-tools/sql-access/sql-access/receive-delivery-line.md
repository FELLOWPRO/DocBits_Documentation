# Linha de recebimento de entrega

## Tabela `public.receive_delivery_line`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `receive_delivery_id`: interno
* `delivery_number`: interno
* `line_number`: interno
* `item_id`: interno
* `description`: interno
* `shipped_quantity`: precisão dupla
* `status`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `deleted_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `purchase_order`: interno
* `sequence_number`: interno
* `sub_org_id`: interno
* `shipped_quantity_unit_code`: interno
* `packing_slip_quantity`: precisão dupla
* `packing_slip_quantity_unit_code`: interno
* `received_quantity`: precisão dupla
* `received_quantity_unit_code`: interno
* `purchase_order_line_number`: interno
* `status_effective_from`: timestamp com fuso horário
* `purchase_order_sub_line_number`: interno
* `invoiced_quantity`: precisão dupla
* `invoice_matching_status`: interno
* `open_quantity`: precisão dupla
* `last_modified_by`: interno
* `deleted_by`: interno

### Análise e descrição

## Documentação da tabela `public.receive_delivery_line`

### Introdução

A tabela `public.receive_delivery_line` parece ser um registro detalhado das linhas de entrega e recebimento associadas às operações de logística e de cadeia de suprimentos de uma organização. Cada linha da tabela representa um item de linha específico de uma entrega e registra detalhes como a descrição do item, as quantidades enviadas e recebidas e vários campos de status. A tabela é um componente essencial para acompanhar a movimentação das mercadorias, do envio ao recebimento, incluindo o faturamento e o gerenciamento de pedidos.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada item de linha de entrega.
* **Função**: chave primária.
* **Conteúdo típico**: um identificador universalmente único (UUID).

#### org\_id

* **Significado**: identificador da organização associada à entrega.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um UUID que representa a organização.

#### receive\_delivery\_id

* **Significado**: identificador que se vincula à transação de entrega como um todo.
* **Função**: chave estrangeira.
* **Conteúdo típico**: um UUID associado a uma transação de entrega específica.

#### delivery\_number

* **Significado**: número único atribuído à entrega.
* **Função**: campo de referência.
* **Conteúdo típico**: uma string que representa o número da entrega.

#### line\_number

* **Significado**: número de linha específico dentro de uma entrega.
* **Função**: campo de referência.
* **Conteúdo típico**: string numérica que indica a sequência da linha.

#### item\_id

* **Significado**: identificador do item que está sendo enviado.
* **Função**: campo de referência.
* **Conteúdo típico**: uma string numérica correspondente a um item.

#### description

* **Significado**: descrição do item.
* **Função**: campo descritivo.
* **Conteúdo típico**: descrição textual do item, por exemplo "FLOUR, WHEAT, UN-BLEACHED ENRICHED, BULK".

#### shipped\_quantity

* **Significado**: quantidade do item que foi enviada.
* **Função**: campo quantitativo.
* **Conteúdo típico**: um número decimal que indica a quantidade enviada.

#### status

* **Significado**: status atual do item de linha da entrega.
* **Função**: campo de status.
* **Conteúdo típico**: texto como "Received".

#### created\_by

* **Significado**: identificador do usuário ou do sistema que criou o registro.
* **Função**: campo de auditoria.
* **Conteúdo típico**: número inteiro que representa o ID de um usuário.

#### created\_on

* **Significado**: timestamp de quando o registro foi criado.
* **Função**: campo de auditoria.
* **Conteúdo típico**: data e hora com fuso horário.

#### last\_modified\_on

* **Significado**: timestamp da última modificação.
* **Função**: campo de auditoria.
* **Conteúdo típico**: data e hora com fuso horário.

#### deleted\_on

* **Significado**: timestamp de quando o registro foi marcado como excluído.
* **Função**: campo de auditoria.
* **Conteúdo típico**: data e hora com fuso horário, frequentemente nulo, a menos que tenha sido excluído.

#### is\_deleted

* **Significado**: indica se o registro está marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: valor booleano, true ou false.

#### purchase\_order

* **Significado**: referência ao pedido de compra associado.
* **Função**: campo de referência.
* **Conteúdo típico**: string alfanumérica que representa o número de um pedido de compra.

#### sequence\_number

* **Significado**: número de sequência da linha de entrega.
* **Função**: campo de referência.
* **Conteúdo típico**: string numérica, frequentemente nula.

#### sub\_org\_id

* **Significado**: identificador de uma suborganização envolvida.
* **Função**: chave estrangeira.
* **Conteúdo típico**: UUID, frequentemente nulo.

#### shipped\_quantity\_unit\_code

* **Significado**: unidade de medida da quantidade enviada.
* **Função**: campo de referência.
* **Conteúdo típico**: código que representa unidades, por exemplo "LBP".

#### packing\_slip\_quantity

* **Significado**: quantidade conforme a guia de remessa.
* **Função**: campo quantitativo.
* **Conteúdo típico**: número decimal, frequentemente nulo.

#### packing\_slip\_quantity\_unit\_code

* **Significado**: código da unidade da quantidade da guia de remessa.
* **Função**: campo de referência.
* **Conteúdo típico**: código que representa unidades, frequentemente nulo.

#### received\_quantity

* **Significado**: quantidade de itens efetivamente recebida.
* **Função**: campo quantitativo.
* **Conteúdo típico**: número decimal que indica a quantidade recebida.

#### received\_quantity\_unit\_code

* **Significado**: código da unidade da quantidade recebida.
* **Função**: campo de referência.
* **Conteúdo típico**: código que representa unidades, por exemplo "LBP".

#### purchase\_order\_line\_number

* **Significado**: número da linha dentro do pedido de compra.
* **Função**: campo de referência.
* **Conteúdo típico**: string numérica.

#### status\_effective\_from

* **Significado**: a data e a hora a partir das quais o status entra em vigor.
* **Função**: campo de status.
* **Conteúdo típico**: data e hora com fuso horário, frequentemente nulo.

#### purchase\_order\_sub\_line\_number

* **Significado**: número da sublinha dentro do pedido de compra.
* **Função**: campo de referência.
* **Conteúdo típico**: string numérica, frequentemente "000".

#### invoiced\_quantity

* **Significado**: quantidade que já foi faturada.
* **Função**: campo quantitativo.
* **Conteúdo típico**: número decimal.

#### invoice\_matching\_status

* **Significado**: status do processo de correspondência de faturas.
* **Função**: campo de status.
* **Conteúdo típico**: código de status em texto, por exemplo "9.0".

#### open\_quantity

* **Significado**: quantidade que permanece em aberto ou ainda não foi processada.
* **Função**: campo quantitativo.
* **Conteúdo típico**: número decimal.

#### last\_modified\_by

* **Significado**: identificador do usuário que modificou o registro pela última vez.
* **Função**: campo de auditoria.
* **Conteúdo típico**: UUID do usuário, frequentemente nulo.

#### deleted\_by

* **Significado**: identificador do usuário que marcou o registro como excluído.
* **Função**: campo de auditoria.
* **Conteúdo típico**: UUID do usuário, frequentemente nulo.

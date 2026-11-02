# Pedido de venda

## Tabela `public.sales_order`

### Colunas

* `id`: interno
* `org_id`: ID da organização
* `sub_org_id`: interno
* `location_id`: interno
* `order_number`: interno
* `customer_purchase_order`: interno
* `customer_id`: interno
* `customer_name`: interno
* `warehouse_id`: interno
* `warehouse_name`: interno
* `transportation_method`: interno
* `requested_delivery_date`: timestamp com fuso horário
* `order_date`: timestamp com fuso horário
* `sales_person_id`: interno
* `sales_person_name`: interno
* `ship_to_party_id`: interno
* `ship_to_party_name`: interno
* `ship_to_party_city`: interno
* `ship_to_party_state`: interno
* `ship_to_party_country`: interno
* `ship_to_party_zip`: interno
* `status`: interno
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `deleted_on`: timestamp com fuso horário
* `preview_path`: interno
* `last_modified_by`: interno
* `deleted_by`: interno

### Análise e descrição

## Documentação técnica da tabela `public.sales_order`

### Introdução

A tabela `public.sales_order` foi projetada para capturar e armazenar informações relacionadas a pedidos de venda em um contexto empresarial. Isso inclui detalhes sobre o pedido, o cliente, a logística e vários metadados associados ao ciclo de vida do pedido. A tabela serve como repositório central para acompanhar o status e o histórico das transações de venda.

### Descrição das colunas

#### id

* **Significado**: identificador único de cada pedido de venda.
* **Função**: chave primária.
* **Conteúdo típico**: uma string UUID (por exemplo, `'6ffe4673-7563-44dc-8e71-855e8f25534a'`).

#### org\_id

* **Significado**: identificador da organização que criou o pedido de venda.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string UUID que representa a organização (por exemplo, `'23f3d697-7411-4c95-981d-faf089d266be'`).

#### sub\_org\_id

* **Significado**: identificador de uma suborganização, se aplicável.
* **Função**: chave estrangeira.
* **Conteúdo típico**: pode ser `NULL` se não for aplicável.

#### location\_id

* **Significado**: identificador do local associado ao pedido de venda.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string de código que representa um local (por exemplo, `'028'`).

#### order\_number

* **Significado**: número único atribuído ao pedido de venda.
* **Função**: campo técnico para o acompanhamento do pedido.
* **Conteúdo típico**: uma string (por exemplo, `'0010174175'`).

#### customer\_purchase\_order

* **Significado**: número de referência do pedido de compra do cliente.
* **Função**: campo técnico para referência cruzada.
* **Conteúdo típico**: uma string (por exemplo, `'1YFNC3'`).

#### customer\_id

* **Significado**: identificador do cliente que faz o pedido.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string de código (por exemplo, `'35623000'`).

#### customer\_name

* **Significado**: nome do cliente.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'DOLLAR GENERAL'`).

#### warehouse\_id

* **Significado**: identificador do depósito responsável pelo atendimento do pedido.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string de código (por exemplo, `'028'`).

#### warehouse\_name

* **Significado**: nome do depósito.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'USCS - DENTON, TX'`).

#### transportation\_method

* **Significado**: método de transporte para a entrega do pedido.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string de código (por exemplo, `'001'`).

#### requested\_delivery\_date

* **Significado**: data de entrega solicitada pelo cliente.
* **Função**: campo descritivo.
* **Conteúdo típico**: um timestamp (por exemplo, `None`).

#### order\_date

* **Significado**: data em que o pedido foi feito.
* **Função**: campo descritivo.
* **Conteúdo típico**: um timestamp (por exemplo, `datetime.datetime(2024, 1, 29, 0, 0, tzinfo=datetime.timezone.utc)`).

#### sales\_person\_id

* **Significado**: identificador do vendedor responsável pelo pedido.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string (por exemplo, `'ROBERTDOCK'`).

#### sales\_person\_name

* **Significado**: nome do vendedor.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'ROBERT DOCKINS'`).

#### ship\_to\_party\_id

* **Significado**: identificador da parte para a qual o pedido é enviado.
* **Função**: chave estrangeira.
* **Conteúdo típico**: uma string (por exemplo, `'35623000 009'`).

#### ship\_to\_party\_name

* **Significado**: nome da parte para a qual o pedido é enviado.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'DOLLAR GENERAL DC 98061/96460'`).

#### ship\_to\_party\_city

* **Significado**: cidade do endereço de entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'SAN ANTONIO'`).

#### ship\_to\_party\_state

* **Significado**: estado do endereço de entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: pode ser `NULL`.

#### ship\_to\_party\_country

* **Significado**: país do endereço de entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'US'`).

#### ship\_to\_party\_zip

* **Significado**: CEP/código postal do endereço de entrega.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'78218'`).

#### status

* **Significado**: status atual do pedido de venda.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string (por exemplo, `'Allocated'`).

#### created\_by

* **Significado**: identificador do usuário que criou a entrada.
* **Função**: campo técnico.
* **Conteúdo típico**: um número inteiro (por exemplo, `1`).

#### created\_on

* **Significado**: timestamp de quando a entrada foi criada.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp (por exemplo, `datetime.datetime(2024, 3, 6, 11, 48, 43, 237208, tzinfo=datetime.timezone.utc)`).

#### last\_modified\_on

* **Significado**: timestamp da última modificação.
* **Função**: campo técnico.
* **Conteúdo típico**: um timestamp (por exemplo, `datetime.datetime(2024, 9, 4, 8, 42, 32, 912247, tzinfo=datetime.timezone.utc)`).

#### is\_deleted

* **Significado**: indicador que informa se o pedido está marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: um booleano (por exemplo, `False`).

#### deleted\_on

* **Significado**: timestamp de quando o pedido foi marcado como excluído.
* **Função**: campo técnico.
* **Conteúdo típico**: data padrão se não foi excluído (por exemplo, `datetime.datetime(2, 1, 1, 11, 0, tzinfo=datetime.timezone.utc)`).

#### preview\_path

* **Significado**: caminho para um documento de pré-visualização do pedido de venda.
* **Função**: campo descritivo.
* **Conteúdo típico**: uma string que representa um caminho de arquivo (por exemplo, `'previews/sales_order/23f3d697-7411-4c95-981d-faf089d266be/0010174175/0010174175_preview.pdf'`).

#### last\_modified\_by

* **Significado**: identificador do usuário que modificou a entrada pela última vez.
* **Função**: campo técnico.
* **Conteúdo típico**: pode ser `NULL`.

#### deleted\_by

* **Significado**: identificador do usuário que marcou a entrada como excluída.
* **Função**: campo técnico.
* **Conteúdo típico**: pode ser `NULL`.

# Campo

## Colunas

* `id`: interno
* `org_id`: ID da organização
* `doc_type`: tipo de documento
* `is_sub_doc_type_field`: booleano
* `profile`: interno
* `field_name`: interno
* `field_type`: interno
* `title`: interno
* `translation_key`: interno
* `hide_label`: booleano
* `input_type`: interno
* `input_size`: interno
* `icon_left`: interno
* `icon_right`: interno
* `icon_above`: interno
* `group_id`: interno
* `row_order`: inteiro
* `sort_order`: inteiro
* `fuzzy_name`: interno
* `fuzzy_field`: interno
* `fuzzy_primary_field`: booleano
* `label_align`: interno
* `calculation_formula`: texto
* `clean_field`: booleano
* `alphanumeric_field`: booleano
* `placeholder`: interno
* `coordinates`: interno
* `normalized_coordinates`: interno
* `threshold`: interno
* `reference_point`: interno
* `checkbox_group`: interno
* `list_of_values`: interno
* `enforce_list_of_values`: booleano
* `created_by`: inteiro
* `created_on`: timestamp com fuso horário
* `last_modified_on`: timestamp com fuso horário
* `is_deleted`: booleano
* `costing_element`: interno
* `erp_field_name`: interno

## Análise e descrição

```markdown
# Documentação técnica da tabela `public.field`

## Introdução

A tabela `public.field` parece ter sido projetada para gerenciar metadados e configurações de diferentes campos associados a documentos, provavelmente no setor de seguros. Cada linha da tabela parece representar a configuração de um campo específico, incluindo seu tipo, rótulo, configurações de visibilidade e outras propriedades que determinam como o campo deve ser apresentado e processado.

## Colunas

### id
- **Significado**: identificador único de cada configuração de campo.
- **Função**: chave primária.
- **Conteúdo típico**: uma string UUID que identifica de forma única cada entrada da tabela.

### org_id
- **Significado**: identificador da organização associada à configuração do campo.
- **Função**: chave estrangeira.
- **Conteúdo típico**: um UUID que referencia uma organização.

### doc_type
- **Significado**: especifica o tipo de documento ao qual o campo está associado.
- **Função**: possivelmente uma chave estrangeira ou um identificador categórico.
- **Conteúdo típico**: uma string no formato `INSURANCE_DOCUMENTS_<UUID>` que indica o tipo de documento.

### is_sub_doc_type_field
- **Significado**: indica se o campo é um subtipo do tipo de documento.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### profile
- **Significado**: possivelmente define o perfil ou o escopo do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: frequentemente vazio ou uma breve descrição em texto.

### field_name
- **Significado**: o nome interno do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: uma string que representa o nome do campo em um contexto técnico (por exemplo, `Schadennummer`).

### field_type
- **Significado**: define o tipo de dado que o campo contém.
- **Função**: campo descritivo.
- **Conteúdo típico**: strings descritivas como `STRING` e `AMOUNT`.

### title
- **Significado**: o título de exibição do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: string em maiúsculas usada para exibir o rótulo do campo.

### translation_key
- **Significado**: chave para a tradução em diferentes idiomas.
- **Função**: campo técnico.
- **Conteúdo típico**: string em minúsculas que representa a chave de tradução.

### hide_label
- **Significado**: indica se o rótulo do campo deve ser ocultado na interface.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### input_type
- **Significado**: especifica o método de entrada do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: pode estar vazio ou conter strings que definem o tipo de entrada.

### input_size
- **Significado**: determina o tamanho do campo de entrada.
- **Função**: campo descritivo.
- **Conteúdo típico**: pode estar vazio ou conter strings que definem o tamanho da entrada.

### icon_left
- **Significado**: ícone a ser exibido no lado esquerdo do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém identificadores de ícones.

### icon_right
- **Significado**: ícone a ser exibido no lado direito do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém identificadores de ícones.

### icon_above
- **Significado**: ícone a ser exibido acima do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém identificadores de ícones.

### group_id
- **Significado**: identificador do grupo de campos ao qual este campo pertence.
- **Função**: chave estrangeira.
- **Conteúdo típico**: um UUID que referencia um grupo de campos.

### row_order
- **Significado**: determina a ordem do campo em uma lista ou formulário.
- **Função**: campo técnico.
- **Conteúdo típico**: número inteiro que indica a posição.

### sort_order
- **Significado**: especifica a ordem de classificação do campo.
- **Função**: campo técnico.
- **Conteúdo típico**: número inteiro que define a precedência de classificação.

### fuzzy_name
- **Significado**: um nome alternativo para a correspondência aproximada (fuzzy).
- **Função**: campo descritivo.
- **Conteúdo típico**: frequentemente vazio ou contém uma string usada para fins de correspondência.

### fuzzy_field
- **Significado**: especifica se o campo é usado na correspondência aproximada (fuzzy).
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém uma string.

### fuzzy_primary_field
- **Significado**: indica se este é o campo principal para a correspondência aproximada (fuzzy).
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### label_align
- **Significado**: configuração de alinhamento do rótulo do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: frequentemente vazio ou contém informações de alinhamento (por exemplo, esquerda, direita, centro).

### calculation_formula
- **Significado**: fórmula usada em cálculos que envolvem o campo.
- **Função**: campo técnico.
- **Conteúdo típico**: texto contendo uma fórmula ou lógica de cálculo.

### clean_field
- **Significado**: indica se o campo deve passar por limpeza de dados.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### alphanumeric_field
- **Significado**: especifica se o campo deve aceitar apenas caracteres alfanuméricos.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### placeholder
- **Significado**: texto de espaço reservado do campo de entrada.
- **Função**: campo descritivo.
- **Conteúdo típico**: frequentemente vazio ou contém um texto de orientação.

### coordinates
- **Significado**: dados de coordenadas associados ao campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém informações de coordenadas.

### normalized_coordinates
- **Significado**: versão normalizada das coordenadas, para garantir consistência.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém dados de coordenadas normalizadas.

### threshold
- **Significado**: valor limite relacionado à validação ou ao processamento do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém valores limite.

### reference_point
- **Significado**: ponto de referência usado em cálculos ou no posicionamento.
- **Função**: campo descritivo.
- **Conteúdo típico**: frequentemente vazio ou contém dados do ponto de referência.

### checkbox_group
- **Significado**: identificador de agrupamento para campos de caixa de seleção.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém identificadores de grupo.

### list_of_values
- **Significado**: especifica uma lista de valores permitidos para o campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém uma lista de valores.

### enforce_list_of_values
- **Significado**: indica se a lista de valores deve ser aplicada de forma estrita.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### created_by
- **Significado**: identificador do usuário que criou a entrada do campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: número inteiro que referencia um ID de usuário.

### created_on
- **Significado**: timestamp de quando o campo foi criado.
- **Função**: campo técnico.
- **Conteúdo típico**: data e hora em UTC.

### last_modified_on
- **Significado**: timestamp da última modificação do campo.
- **Função**: campo técnico.
- **Conteúdo típico**: data e hora em UTC.

### is_deleted
- **Significado**: indica se o campo foi marcado como excluído.
- **Função**: campo técnico.
- **Conteúdo típico**: valor booleano (True ou False).

### costing_element
- **Significado**: elemento de custeio associado ao campo.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém identificadores de elementos de custeio.

### erp_field_name
- **Significado**: nome do campo conforme usado em sistemas ERP.
- **Função**: campo descritivo.
- **Conteúdo típico**: geralmente vazio ou contém nomes de campos específicos do ERP.

Esta documentação oferece uma visão geral detalhada da estrutura e da finalidade de cada coluna da tabela `public.field`. Serve como guia para que os desenvolvedores entendam o modelo de dados e sua aplicação no sistema.
```

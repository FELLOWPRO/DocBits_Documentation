# Exportação de Configuração para o Portal do Fornecedor

### Visão Geral

O arquivo de configuração de exportação é um componente crucial no portal do fornecedor, definindo como os dados são mapeados entre o portal do fornecedor e o sistema ERP. Essa configuração garante que os dados sejam transferidos e sincronizados com precisão entre os sistemas, permitindo operações suaves e eficientes.

### Estrutura do Arquivo de Configuração

O arquivo de configuração de exportação é estruturado como um objeto JSON que contém múltiplos mapeamentos. Cada mapeamento está associado a um programa específico no sistema ERP e define as ações a serem realizadas, os campos a serem mapeados e quaisquer condições a serem aplicadas.

### Componentes Principais

#### 1. Programa

* **Definição**: Especifica o programa ERP ao qual o mapeamento se aplica.
* **Exemplo**: `"program": "CRS620MI"`

#### 2. Ações

* **Definição**: Define as ações que podem ser realizadas, como adicionar ou atualizar registros.
*   **Exemplo**:

    ```json
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    }
    ```

#### 3. Mapeamento

• Definição: Especifica o mapeamento entre campos no sistema ERP e campos no portal do fornecedor.

• Componentes:

• erp\_field\_name: O nome do campo no sistema ERP.

• value\_field\_name: O nome do campo correspondente no portal do fornecedor.

• value: Um valor estático a ser usado se nenhum campo correspondente existir no portal do fornecedor.

• if\_conditions: Condições opcionais que determinam o valor com base em certos critérios.

• Exemplo:

```json
{
    "erp_field_name": "SUNO",
    "value_field_name": "supplier_number"
}
```

#### 4. Lógica Condicional (if\_conditions)

• Definição: Especifica condições que devem ser atendidas para que um valor específico seja utilizado.

• Componentes:

• field\_name: O nome do campo no portal do fornecedor que é avaliado.

• field\_value: O valor que aciona a condição.

• then\_value: O valor a ser usado se a condição for atendida.

• Exemplo:

```json
{
    "erp_field_name": "SUTY",
    "value": "0",
    "if_conditions": [{
        "field_name": "supplier_group",
        "field_value": "FRT",
        "then_value": "5"
    }]
}
```

#### 5. Laços (loop\_on)

• Definição: Define as seções onde a configuração deve iterar sobre uma lista de itens, como detalhes de endereço ou referência.

• Exemplo:

```json
"loop_on": "address_details"
```

#### 6. Campos Calculados (value\_field\_calculated)

• Definição: Especifica campos que devem ser calculados em tempo de execução, como gerar a data atual.

• Exemplo:

```json
{
    "erp_field_name": "STDT",
    "value_field_calculated": "now()"
}
```

#### 7. Mapeamentos de Campo com Listas (mapping\_field\_name e mapping\_list)

• Definição: Mapeia valores específicos do portal do fornecedor para valores correspondentes no sistema ERP com base em uma lista pré-definida.

• Componentes:

• mapping\_field\_name: O campo que determina o mapeamento.

• mapping\_list: Um dicionário que traduz valores do portal do fornecedor para o sistema ERP.

• Exemplo:

```json
{
    "erp_field_name": "RFID",
    "mapping_field_name": "reference_type",
    "mapping_list": {
        "10": "PURCHASING",
        "15": "DLVRY PHN#",
        "20": "COA",
        "25": "QA",
        "30": "FINANCE",
        "35": "SALES"
    }
}
```

### Exemplo de Quebra de Configuração

#### Adição e Atualização de Fornecedor (CRS620MI)

• Programa: CRS620MI

• Ações:

• Adicionar Fornecedor: AddSupplier

• Atualizar Fornecedor: UpdSupplier

• Campos de Mapeamento:

• SUNO → supplier\_number

• SUNM → name

• CSCD → supplier\_country

• TINO → tax\_id

• Campos adicionais incluem valores estáticos e mapeamentos condicionais.

#### Detalhes de Endereço (CRS620MI)

• Loop Em: _**address\_details**_

• Ações:

• Adicionar Endereço: AddAddress

• Atualizar Endereço: AddAddress

• Campos de Mapeamento:

• SUNO → supplier\_number

• ADR1 → address

• TOWN → city

• Campos adicionais incluem campos calculados como now() para a data atual.

#### Detalhes de Referência (CRS620MI)

• Loop Em: _**reference\_details**_

• Ações:

• Adicionar Referência de Fornecedor: AddSupplierRef

• Atualizar Referência de Fornecedor: AddSupplierRef

• Campos de Mapeamento:

• SUNO → supplier\_number

• RFTY → reference\_type

• RFID é mapeado usando uma lista para traduzir tipos como “PURCHASING”, “QA” e “FINANCE”.

### Usando a Configuração de Exportação

#### 1. Carregando o Arquivo de Configuração

**1. Navegue até a Configuração de Exportação:**

• Vá para a seção de Configuração de Exportação no menu principal.

**2. Carregue o Arquivo de Configuração:**

• Clique nas seções ION-Mapping File ou IDM Mapping File para carregar o respectivo arquivo de configuração.

**3. Salve a Configuração:**

• Após o upload, clique no botão Salvar para aplicar a configuração.

#### 2. Usando Modelos Padrão

• Clique no botão Usar Modelo Padrão se desejar reverter para o modelo de configuração padrão fornecido pelo sistema.

#### 3. Formatando o JSON

• Use o botão Formatar para formatar automaticamente o código JSON para melhor legibilidade.

### Conclusão

Este arquivo de configuração é essencial para garantir que os dados entre o portal do fornecedor e o sistema ERP sejam corretamente mapeados e sincronizados. Ao entender a estrutura e os componentes principais, os administradores podem gerenciar e personalizar efetivamente o processo de exportação para atender a seus requisitos de negócios específicos.

### Exemplo Completo

```json
[{
    "program": "CRS620MI",
    "actions": {
        "add": "AddSupplier",
        "update": "UpdSupplier"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "value_field_name": "supplier_number"
    }, {
        "erp_field_name": "SUNM",
        "value_field_name": "name"
    }, {
        "erp_field_name": "SUTY",
        "value": "0",
        "if_conditions": [{
            "field_name": "supplier_group",
            "field_value": "FRT",
            "then_value": "5"
        }]
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }, {
        "erp_field_name": "DTFM",
        "value_field_name": "date_format"
    }, {
        "erp_field_name": "ORTY",
        "value": "F20"
    }, {
        "erp_field_name": "DT4T",
        "value": "1"
    }, {
        "erp_field_name": "DTCD",
        "value": "2"
    }, {
        "erp_field_name": "CUCD",
        "value_field_name": "currency"
    }, {
        "erp_field_name": "TINO",
        "value_field_name": "tax_id"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "supplier_phone"
    }, {
        "erp_field_name": "CRTP",
        "value": "1"
    }, {
        "erp_field_name": "ATPR",
        "value": "1"
    }, {
        "erp_field_name": "SUCL",
        "value_field_name": "supplier_group"
    }, {
        "erp_field_name": "LNCD",
        "value_field_name": "language"
    }, {
        "erp_field_name": "CONO",
        "value": "781_DDD"
    }, {
        "erp_field_name": "TEDL",
        "value": "FOB"
    }, {
        "erp_field_name": "TEPY",
        "value_field_name": "payment_term"
    }, {
        "erp_field_name": "TEPA",
        "value": "001"
    }, {
        "erp_field_name": "PYME",
        "value": "CRP"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "address_details",
    "actions": {
        "add": "AddAddress",
        "update": "AddAddress"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "ADTE",
        "value_field_name": "address_type"
    }, {
        "erp_field_name": "ADID",
        "value_field_name": "address_type",
        "if_conditions": [{
            "field_name": "address_type",
            "field_value": "10",
            "then_value": ""
        }]
    }, {
        "erp_field_name": "STDT",
        "value_field_calculated": "now()"
    }, {
        "erp_field_name": "ADR1",
        "value_field_name": "address"
    }, {
        "erp_field_name": "TOWN",
        "value_field_name": "city"
    }, {
        "erp_field_name": "ECAR",
        "value_field_name": "state"
    }, {
        "erp_field_name": "PONO",
        "value_field_name": "postal_code"
    }, {
        "erp_field_name": "CSCD",
        "value_field_name": "supplier_country"
    }]
}, {
    "program": "CRS620MI",
    "loop_on": "reference_details",
    "actions": {
        "add": "AddSupplierRef",
        "update": "AddSupplierRef"
    },
    "mapping": [{
        "erp_field_name": "SUNO",
        "main_value_field": "supplier_number"
    }, {
        "erp_field_name": "RFTY",
        "value_field_name": "reference_type"
    }, {
        "erp_field_name": "RFID",
        "mapping_field_name": "reference_type",
        "mapping_list": {
            "10": "PURCHASING",
            "15": "DLVRY PHN#",
            "20": "COA",
            "25": "QA",
            "30": "FINANCE",
            "35": "SALES"
        }
    }, {
        "erp_field_name": "YRE1",
        "value_field_name": "reference_name"
    }, {
        "erp_field_name": "PHNO",
        "value_field_name": "telephone_no"
    }, {
        "erp_field_name": "EMAL",
        "value_field_name": "email_address"
    }]
}]
```

# Scripting no DocBits

## Guia de Scripting do Docbits

Bem-vindo ao guia de scripting do Docbits! Aqui, você aprenderá como usar scripts para automatizar e aprimorar o processamento de documentos dentro do Docbits. Os scripts permitem a manipulação de campos personalizados, transformação de dados e implementação de lógica em vários tipos de documentos.

### Começando

Os scripts no Docbits são escritos em Python. Eles interagem com os campos e metadados do documento para realizar uma ampla gama de operações, desde formatação simples de dados até lógica complexa.

#### Funções Principais

* `get_field_value(fields_dict, field_name, default=None)`: Recupera o valor de um campo especificado.
* `set_field_value(fields_dict, field_name, value)`: Define o valor de um campo especificado.
* `create_new_field(field_name, value)`: Cria um novo campo com um nome e valor especificados.
* `format_decimal_to_locale(value, locale)`: Formata um valor decimal de acordo com um local especificado.

### Scripts de Exemplo

Abaixo estão vários exemplos que demonstram tarefas comuns de scripting.

#### Exemplo 1: Mapeamento de Moeda para Faturas

Padronize símbolos ou texto de moeda para códigos de moeda ISO.
```python
currency_map = {
"€": "EUR",
"EURO": "EUR",
"$": "USD",
"£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
currency_value = currency_value.upper()
if currency_value in currency_map:
currency_value = currency_map[currency_value]
set_field_value(fields_dict, "currency", currency_value)
```


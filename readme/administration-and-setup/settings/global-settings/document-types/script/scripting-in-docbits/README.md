# Scripting no DocBits

## Guia de Scripting do DocBits

Bem-vindo ao guia de scripting do DocBits! Aqui, aprenderá a utilizar scripts para automatizar e melhorar o processamento de documentos no DocBits. Os scripts permitem a manipulação personalizada de campos, transformação de dados e implementação de lógica em vários tipos de documentos.

### Primeiros Passos

Os scripts no DocBits são escritos em Python. Eles interagem com os campos e metadados dos documentos para realizar uma ampla gama de operações, desde a formatação simples de dados até lógica complexa.

#### Funções Principais

* `get_field_value(fields_dict, field_name, default=None)`: Obtém o valor de um campo especificado.
* `set_field_value(fields_dict, field_name, value)`: Define o valor de um campo especificado.
* `create_new_field(field_name, value)`: Cria um novo campo com um nome e valor especificados.
* `format_decimal_to_locale(value, locale)`: Formata um valor decimal de acordo com uma localidade especificada.

### Scripts de Exemplo

Abaixo estão vários exemplos que demonstram tarefas comuns de scripting.

#### Exemplo 1: Mapeamento de Moeda para Faturas

Padronizar símbolos ou texto de moeda para códigos de moeda ISO.

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



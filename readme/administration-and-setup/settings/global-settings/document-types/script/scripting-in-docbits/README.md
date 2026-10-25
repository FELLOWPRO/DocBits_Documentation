# Scripting no DocBits

## Guia de Scripting do DocBits

Bem-vindo ao guia de scripting do DocBits! Aqui, aprenderá a utilizar scripts para automatizar e melhorar o processamento de documentos no DocBits. Os scripts permitem a manipulação personalizada de campos, transformação de dados e implementação de lógica em vários tipos de documentos.

### Primeiros Passos

Os scripts no DocBits são escritos em Python. Eles interagem com os campos e metadados dos documentos para realizar uma ampla gama de operações, desde a formatação simples de dados até lógica complexa.

#### Funções Principais

Cada script recebe o documento com o nome `document_data`. Passe-o como primeiro argumento às funções de campo. A referência completa encontra-se na página [Funções de Campo](field-functions.md).

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`: Lê o valor de um campo.
* `set_field_value(document_data, field_name, value)`: Escreve um valor num campo e cria o campo se ele não existir.
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`: Escreve uma data, opcionalmente com dias adicionados e sem fins de semana.
* `set_amount_value(document_data, field_name, value)`: Escreve um montante no formato da localidade do documento.
* `set_field_as_invalid(document_data, field_name, message, code=None)`: Marca um campo como inválido e mostra a mensagem ao utilizador.
* `set_is_required(document_data, field_name, value)`: Torna um campo obrigatório ou remove essa obrigatoriedade.

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```



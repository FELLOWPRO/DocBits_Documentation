---
description: "P1: escolher Field is, Docfield is ou Compare two Fields"
---

# P1: escolher Field is, Docfield is ou Compare two Fields

Use **Field is** para verificar vazio, **Docfield is** para comparar com um valor configurado e **Compare two Fields** para dois valores do documento atual. Uma verificação de vazio não prova que o campo exista no layout nem que seja válido para o negócio.

Em Field is v2, campo ausente, `null`, texto vazio, apenas espaços e booleano `false` são vazios. O número `0`, o texto `"0"` e o texto `"false"` não são vazios. Estes oito casos foram testados em Dev com dados documentais completos. Use uma condição explícita de caixa de seleção quando a decisão for verdadeiro/falso.

`"1000.01"` num campo AMOUNT difere dos mesmos caracteres num campo de texto. O pacote v2 usa AMOUNT e pontos decimais no JSON. Verifique conjuntamente chave técnica, layout e tipo. Uma etiqueta traduzida não é uma chave técnica, nem um símbolo monetário um valor numérico.

Em Compare two Fields, defina campo esquerdo, operador e campo direito. Confirme tipos compatíveis e ambas as entradas; dados ausentes ou não comparáveis são erro de dados, não desigualdade demonstrada. Repita caso positivo, negativo, entrada ausente e limite exato. Registe valor, tipo e saída escolhida.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `condition_docfield_status` · v2

Identidade: `6f346541-faa0-42bd-b1a5-b23282157da1`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_status` | `field_empty / field_not_empty` | `"field_empty"` |

### `condition_docfield_operator_value` · v2

Identidade: `1c35a5a0-1592-446c-9a61-6abb14d27450`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `operator` | `eq / neq / gt / ge / lt / le` | `"gt"` |
| `field_name` | `field_name:str` | `"total_amount"` |
| `field_value` | `field_value:str` | `"1000"` |

### `condition_compare_two_docfield_values` · v2

Identidade: `3b3cdc55-6afe-4797-ae8b-9480ec3a8a30`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| FIELD-01 | missing / null / "" / "   " / false | field_empty=success |
| FIELD-02 | 0 / "0" / "false" | field_empty=failed_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Provas e limites

Resultados selecionados de cartões e nós foram verificados com dados sintéticos em Advanced Test. As respostas estão no pacote. As ações documentais são simuladas e não provam execução persistida nem entrega externa.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)

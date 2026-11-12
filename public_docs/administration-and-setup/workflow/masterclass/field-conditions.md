---
description: "Escolher Field is, Docfield is ou Compare two Fields"
---

# P1: Escolher Field is, Docfield is ou Compare two Fields

Três cartões de condição parecem iguais no designer, e a diferença entre eles decide o que uma regra consegue realmente detetar. Esta página ajuda a escolher o cartão certo e depois dá três exercícios curtos que mostram o que cada cartão devolve. No fim, vai distinguir «vazio» de «zero», «falso» de «ausente» e uma condição não cumprida de um erro.

Faça os exercícios no Advanced Test, na sua própria organização de testes, com um documento sintético. Aqui não se toca em nenhum documento de cliente.

## De que cartão precisa?

| Se quer verificar... | Use | Cartão e versão |
| --- | --- | --- |
| se um campo tem algum valor | **Field is** | `condition_docfield_status` v2 |
| um campo face a um valor que introduz | **Docfield is** | `condition_docfield_operator_value` v2 |
| dois campos do mesmo documento entre si | **Compare two Fields** | `condition_compare_two_docfield_values` v2 |

Os três são condições: devolvem um resultado e não alteram nada no documento. Uma verificação de estado vazio não prova que um campo exista no layout nem que o seu conteúdo seja válido para o negócio. As páginas de cada cartão detalham todas as definições: [Field is](../and/document-field/field-is.md), [Docfield is](../and/document-field/docfield-is.md) e [Compare two Fields](../and/document-field/compare-two-fields.md).

## Exercício 1: descobrir o que significa «vazio»

**Objetivo:** saber que valores o Field is versão 2 trata como vazios.

1. Adicione **Field is** versão 2 a uma regra na sua organização de testes e escolha um campo de texto do seu layout.
2. Coloque o estado do campo em `field_empty` (Empty or missing).
3. Execute oito casos de Advanced Test com dados de documento completos: campo ausente, `null`, texto vazio `""`, apenas espaços `" "`, booleano `false`, número `0`, texto `"0"` e texto `"false"`.

**Concluído quando:** os primeiros cinco casos devolverem `field_empty=success` e os últimos três `field_empty=failed_condition`. Estes oito casos foram testados em Dev com dados de documento completos.

O número `0`, o texto `"0"` e o texto `"false"` são valores, não ausências. Se a sua decisão de negócio é verdadeiro ou falso, use uma condição de caixa de verificação explícita em vez de testar o campo como vazio.

## Exercício 2: comparar um campo com um valor

**Objetivo:** ver como o operador e o tipo de campo alteram a resposta.

1. Escolha um campo numérico como `total_amount`, o operador `gt` e o valor `1000`.
2. Teste `1000`, `1000.01`, um campo ausente e um valor inválido.

**Concluído quando:** `1000` devolver `failed_condition`, porque `gt` significa estritamente maior, `1000.01` devolver `success` e uma entrada ausente ou inválida devolver `error`.

## Exercício 3: comparar dois campos

**Objetivo:** saber quando dois valores são comparados e quando o cartão não os consegue comparar de todo.

1. Defina o campo esquerdo, o operador e o campo direito. Use dois campos com tipos compatíveis.
2. Teste valores iguais, valores diferentes e uma entrada ausente.

**Concluído quando:** valores iguais cumprirem `eq`, valores diferentes devolverem `failed_condition` e uma entrada ausente devolver `error` em vez de uma desigualdade provada.

## O que significam os três resultados

| Resultado | O que lhe diz |
| --- | --- |
| `success` | O cartão comparou os valores e a condição foi cumprida. |
| `failed_condition` | O cartão comparou os valores e a condição não foi cumprida. `0` e `"0"` ficam aqui numa verificação de estado vazio. |
| `error` | O cartão não conseguiu comparar, por exemplo porque falta um valor ou não é válido. Um erro não é a mesma resposta que «diferente». |

## O tipo faz parte da comparação

Um valor `"1000.01"` num campo AMOUNT não é o mesmo que os mesmos caracteres num campo de texto. O pacote de exercícios v2 usa AMOUNT e pontos decimais no JSON. Verifique em conjunto a chave técnica do campo, o layout e o tipo. Uma etiqueta traduzida não é uma chave técnica, e um símbolo de moeda não é um valor numérico.

## Cartões e parâmetros de exemplo

Estes valores descrevem parâmetros de cartões individuais, não um workflow completo importável. Substitua YOUR\_\* pelas suas próprias escolhas de teste. O ID oculto do chamador é gerido pelo designer. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; verifique as versões disponíveis e as permissões na sua própria organização.

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
| FIELD-01 | missing / null / "" / " " / false | field\_empty=success |
| FIELD-02 | 0 / "0" / "false" | field\_empty=failed\_condition |
| FIELD-03 | AMOUNT 1000; gt 1000 | failed\_condition |
| FIELD-04 | AMOUNT 1000.01; gt 1000 | success |
| FIELD-05 | AMOUNT missing / invalid; gt 1000 | error |

## Evidência e limites

Alguns resultados de cartão e de nó foram verificados com dados sintéticos no Advanced Test. As respostas estão no pacote de exercícios. As ações de documento são simuladas; estes testes não provam uma execução de documento guardada nem uma entrega externa.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)

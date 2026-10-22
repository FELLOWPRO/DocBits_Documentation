---
description: "P1: calcular colunas e verificar dependências regex"
---

# P1: calcular colunas e verificar dependências regex

**Calculate Columns** calcula duas colunas da mesma linha e escreve o resultado. **Calculate in / CALC_COLUMNS_REGEX** acrescenta uma condição regex numa terceira coluna. Aqui a regex decide se há cálculo; não extrai nem substitui texto. A antiga explicação de substituição não descreve este cartão.

Exemplo: `QTY=2`, `PRICE=10`, operação `*`, resultado `TOTAL=20.0`. Na variante regex, use `TYPE` e padrão `^A$`. Uma linha A é calculada. Numa linha B sem correspondência, o código escreve um resultado vazio; um TOTAL existente não é preservado automaticamente.

A função aritmética arredonda resultados numéricos a quatro casas decimais. Um operando vazio pode tornar-se 0; dois textos vazios devolvem vazio. `+` pode concatenar texto não numérico. Na função analisada, `10/0` produz erro. Valide números e células necessárias antes de calcular e defina um percurso de erro.

Guarde uma tabela completa antes/depois: duas linhas correspondentes, uma sem correspondência, entrada vazia, texto inválido e divisão por zero. Em cálculos dependentes A→B, ligue os cartões explicitamente e verifique o valor atualizado que B lê. Compare cada linha e as outras colunas existentes, além do estado documental.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

### `calc_columns` · v2

Identidade: `92d7a634-736a-4e1f-80b3-2b521efcd81c`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |

### `calc_columns_regex` · v2

Identidade: `dbf035c8-927b-444a-9e5a-18555f5deacf`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `table_name` | `table_name:str` | `"LINE_ITEMS"` |
| `result_column_name` | `result_column_name:str` | `"TOTAL"` |
| `regex_pattern` | `regex_pattern:str` | `"^A$"` |
| `column_name_dependency` | `column_name_dependency:str` | `"TYPE"` |
| `table_column_name_right` | `table_column_name_right:str` | `"PRICE"` |
| `math_operator` | `+ / - / / / *` | `"*"` |
| `table_column_name_left` | `table_column_name_left:str` | `"QTY"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| CALC-01 | QTY=2; PRICE=10; TYPE=A; ^A$ | TOTAL=20.0 |
| CALC-02 | QTY=2; PRICE=10; TYPE=B; ^A$; TOTAL=99 | TOTAL="" |
| CALC-03 | 10 / 3 | 3.3333 |
| CALC-04 | 10 / 0 | error |
| CALC-05 | "" + 2 | 2.0 |
| CALC-06 | x + y | "x y" |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)

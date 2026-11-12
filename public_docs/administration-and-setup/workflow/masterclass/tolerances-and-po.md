---
description: "Definir a referência de tolerâncias e comparação PO"
---

# P1: Definir a referência de tolerâncias e comparação PO

Uma tolerância de 2 por cento não é um valor fixo. É 2 por cento do lado com que compara, por isso a mesma linha de fatura pode falhar numa direção e passar na outra. Esta página mostra-o num par de valores, dá três exercícios para o reproduzir e depois lista as seis direções de comparação e os parâmetros de cartão que pode copiar para o seu próprio teste.

Faça os exercícios no Advanced Test, na sua própria organização de testes, com um documento sintético e uma encomenda associada.

## O lado de referência é a base

No cartão PO versão 5 analisado, `document_po` compara o valor do documento com o valor da encomenda, pelo que a encomenda é a base de uma tolerância percentual. `po_document` inverte tanto a comparação como a base. As seis direções permitidas incluem também o lado recebido. Defina direção, operador e Any/All de forma explícita, em vez de confiar no que um cartão guardado ainda contém.

## Exercício 1: os mesmos valores, duas direções

**Objetivo:** ver como das mesmas cifras saem dois resultados diferentes.

1. Crie uma encomenda associada de `100` e um preço unitário no documento de `102.02`.
2. Compare com o operador `eq` e uma tolerância de `2` por cento, primeiro com `document_po`. Espere `false`: 2 por cento de 100 são 2, logo o intervalo fechado vai de 98 a 102, e 102.02 fica 0.02 acima.
3. Repita o mesmo caso com `po_document`. Espere `true`: 2 por cento de 102.02 são 2.0404, o intervalo vai de 99.9796 a 104.0604, e o valor da encomenda 100 cai dentro.

**Concluído quando:** ambos os resultados e ambos os intervalos estiverem registados, e souber dizer de que valor foi calculada a percentagem em cada direção.

Uma tolerância absoluta de `2` comporta-se de outra forma: usa a unidade do valor comparado e não se desloca com a referência.

## Exercício 2: encontrar a fronteira exata

**Objetivo:** saber se o limite do intervalo conta.

1. Mantenha `document_po`, `eq` e a tolerância de 2 por cento, e mude o valor do documento para `102`.
2. Execute o caso e depois repita-o com `102.01`.

**Concluído quando:** `102` devolver `true` e `102.01` devolver `false`. O limite é inclusive: 102 fica exatamente na fronteira superior do intervalo 98 a 102.

## Exercício 3: Any, All e as linhas comparadas

**Objetivo:** saber o que o cartão faz com várias linhas e o que acontece quando não há nada para comparar.

1. Construa um documento com duas linhas contra a mesma encomenda associada: uma dentro da tolerância e uma fora.
2. Execute o cartão com `match_any` e depois com `match_all`.
3. Execute um documento que não tenha nenhuma linha comparável.

**Concluído quando:** `match_any` passar na única linha correspondente, `match_all` falhar assim que uma comparação falhar, e o documento sem linha comparável devolver um erro de dados. Na versão 5 isso é um erro e não um All satisfeito automaticamente.

## Que lado é a base?

| Opção guardada | Lado comparado | Lado de referência (base percentual) |
| --- | --- | --- |
| `po_document` | Encomenda | Documento |
| `received_document` | Dados recebidos | Documento |
| `po_received` | Encomenda | Dados recebidos |
| `document_po` | Documento | Encomenda |
| `document_received` | Documento | Dados recebidos |
| `received_po` | Dados recebidos | Encomenda |

## Verifique antes de confiar num workflow existente

O cartão normaliza preços por unidade de preço e usa dados de encomenda ou de receção conforme a direção, por isso verifique primeiro a associação, as quantidades e as unidades. Any precisa de uma comparação correspondente; All, de todas as comparações realmente efetuadas. As linhas não associadas registam-se à parte.

Em workflows existentes, releia a versão guardada, a direção e o operador: as migrações alteraram definições de comparação, pelo que as etiquetas históricas não bastam como prova de aceitação. Registe os valores e a referência, a fronteira exata, o menor excesso, a precisão de arredondamento, a encomenda ausente e a linha não associada. Este cálculo não substitui uma aceitação com os seus próprios dados mestres de PO.

## Cartões e parâmetros de exemplo

Estes valores descrevem parâmetros de cartões individuais, não um workflow completo importável. Substitua YOUR\_\* pelas suas próprias escolhas de teste. O ID oculto do chamador é gerido pelo designer. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; verifique as versões disponíveis e as permissões na sua própria organização.

### `condition_docfield_operator_docfield_tolerances` · v2

Identidade: `d0472648-d1a2-499d-83e3-b47306ae130a`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `field_name_left` | `field_name_left:str` | `"total_amount"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `field_name_right` | `field_name_right:str` | `"expected_amount"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |

### `condition_doc_to_po_unit_price` · v5

Identidade: `ed2cd0fe-ac87-4bae-9a86-0b0576159b28`

| Parâmetro | Tipo / opções | Exemplo |
| --- | --- | --- |
| `operator_any_all` | `match_any / match_all` | `"match_all"` |
| `operator` | `eq / neq / gt / ge / lt / le` | `"eq"` |
| `tolerance_amount` | `tolerance_amount` | `"2"` |
| `tolerance_type` | `percent / value` | `"percent"` |
| `comparison_data` | `po_document / received_document / po_received / document_po / document_received / received_po` | `"document_po"` |

## Casos de teste de negócio

| Caso | Entrada / configuração | Resultado esperado |
| --- | --- | --- |
| PO-01 | document\_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document\_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po\_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared\_rows=0 | erro de dados |
| PO-05 | unmatched\_rows>0 | verificar cobertura separadamente |

## Evidência e limites

Os parâmetros e o comportamento foram verificados contra o catálogo de Dev e a revisão de código analisada. Os casos de teste de negócio são um procedimento de aceitação. Neste capítulo não foram efetuadas aprovações pessoais, alterações a dados reais nem entregas.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)

---
description: "P1: definir a referência de tolerâncias e comparação PO"
---

# P1: definir a referência de tolerâncias e comparação PO

A tolerância percentual depende do **lado de referência**. No cartão PO v5 analisado, `document_po` compara documento com encomenda; a encomenda é a base percentual. `po_document` inverte comparação e base. As seis direções permitidas também incluem o valor recebido. Defina direção, operador e Any/All explicitamente.

Exemplo: encomenda 100, documento 102.02, igualdade a 2 %. Com referência à encomenda, o intervalo é 98–102: fora. Com referência ao documento, é 99.9796–104.0604: a encomenda 100 está dentro. Documento 102 coincide com o limite superior incluído da primeira direção. Uma tolerância absoluta de 2 usa a unidade do valor comparado.

O cartão normaliza preços por unidade de preço e usa dados de encomenda ou receção conforme a direção. Verifique correspondências, quantidades e unidades. Any exige uma comparação correspondente; All todas as comparações efetuadas. **Nenhuma linha comparável** é erro de dados em v5, não um All automaticamente satisfeito. Conte separadamente linhas sem correspondência.

Nos workflows existentes, releia versão, direção e operador guardados: as migrações alteraram configurações. Etiquetas antigas não bastam para aceitar. Registe valores, referência, limite, menor excesso, precisão, encomenda ausente e linha sem correspondência. Este cálculo não substitui a aceitação com os seus dados mestre PO.

## Cartões e parâmetros de exemplo

Os valores descrevem parâmetros de cartões, não um workflow completo importável. Substitua YOUR_* por seleções próprias de teste. O designer gere o ID oculto do chamador. Catálogo: Dev, DocFlow 2.10.38, 21 de outubro de 2026; confirme versões e permissões da organização.

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
| PO-01 | document_po; PO=100; DOC=102; eq; 2 percent | true |
| PO-02 | document_po; PO=100; DOC=102.02; eq; 2 percent | false |
| PO-03 | po_document; PO=100; DOC=102.02; eq; 2 percent | true |
| PO-04 | compared_rows=0 | erro de dados |
| PO-05 | unmatched_rows>0 | verificar cobertura separadamente |

## Provas e limites

Parâmetros e comportamento foram comparados com o catálogo Dev e o código analisado. Os casos de negócio são uma orientação de aceitação. Não foram feitas aprovações pessoais, alterações reais nem entregas neste capítulo.

[Continuar a aprender](../workflow-learning-path.md) · [Pacote de formação](../workflow-training-kit.md)

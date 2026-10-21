# Comparações de PO: direção, tolerância e versões de cartão

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-72e8f3204ac8-pt.png" alt="Cartões disponíveis na categoria selecionada. Configure os campos antes de utilizar. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Cartões disponíveis na categoria selecionada. Configure os campos antes de utilizar. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

Os cartões de comparação PO comparam um lado escolhido com um lado de referência. A referência determina a base para uma tolerância percentual. Primeiro complete a correspondência do pedido de compra, depois selecione a comparação, a operadora, Qualquer/Todos e a tolerância solicitada pelo cartão específico.

## Direções de comparação

| Opção armazenada | Lado comparado | Lado de referência |
| --- | --- | --- |
| `po_document` | Pedido de compra | Documento |
| `received_document` | Dados recebidos | Documento |
| `po_received` | Pedido de compra | Dados recebidos |
| `document_po` | Documento | Pedido de compra |
| `document_received` | Documento | Dados recebidos |
| `received_po` | Dados recebidos | Pedido de compra |

O lado recebido é derivado dos dados do pedido de compra conciliados. Uma comparação recebida no cartão de preço unitário pode usar quantidades para derivar um valor comparável; não é uma comparação direta de uma quantidade com o preço de uma moeda. Utilize os valores registrados por esse cartão no log ao verificar o cálculo.

## Por que a direção é importante

Para uma referência de `100` e um valor comparado de `110`, uma tolerância percentual de `5` corresponde a `5` em torno da referência. Se o documento for a referência e seu valor for editável, a alteração do documento também altera essa base de tolerância. Escolha a referência deliberadamente, especialmente para aprovação automática.

Inverter os lados inverte os operadores de ordem: `>` torna-se `<`, `>=` torna-se `<=` e vice-versa. A igualdade e a desigualdade mantêm o seu significado. Não inverta um operador sem inspecionar também os lados escolhidos.

Versões contendo o movimento de migração de comparação afetaram os cartões salvos de `po_document` para `document_po` e de `received_document` para `document_received`, enquanto revertia o operador de ordenação. As versões afetadas são tolerância de quantidade v4, confirmação de pedido para pedido de compra v4 e preço unitário v4/v5. O preço combinado da diferença de quantidade está excluído dessa migração de cartão salvo. Inspecione a configuração salva e teste seu resultado comercial após um lançamento; não reverta manualmente uma segunda vez.

## Versões de cartão com preço unitário

| Versão | Configuração |
| --- | --- |
| v3 | Usa o comportamento de comparação anterior. Não presuma que isso expõe os campos de direção e tolerância mais recentes. |
| v4 | Adiciona a seleção do lado da comparação. |
| v5 | Inclui Qualquer/Todos, operador, quantidade de tolerância, tipo de tolerância e seleção do lado de comparação. |

Escolha uma tolerância absoluta para um valor fixo e uma tolerância percentual para uma variação relativa à referência selecionada. Utilize a operadora oferecida pelo cartão; igualdade exata e estar dentro de uma tolerância são decisões diferentes. Não existe uma tolerância comercial universal adequada para cada fornecedor ou tipo de documento.

## Exemplo de verificação

1. Use uma referência de PO correspondente de `100` e valor do documento `110`.
2. Selecione Documento para Pedido de Compra, uma comparação dentro da tolerância quando oferecida e `5` por cento. Espere uma comparação fora da banda.
3. Teste o limite de tolerância exato, os valores em ambos os lados e um PO correspondente ausente.
4. Com várias linhas, verifique Qualquer versus Todos usando uma linha de aprovação e uma de falha.
5. Inspecione os valores comparados do log, os lados selecionados, o operador e a tolerância e, em seguida, verifique a ramificação do fluxo de trabalho resultante.

Um pedido de compra sem correspondência, um valor não numérico e uma condição comercial falsa são resultados diferentes. Não trate os dados ausentes como uma correspondência bem-sucedida. Para cobranças, use [Any / All Charges](../and/compare-with-purchase-order/any-all-charges.md), que explica separadamente o comportamento de cobrança ausente e v2/v3.

Continue com o [Guia de correspondência de PO](../and/compare-with-purchase-order/po-matching-complete-guide.md) e a referência do cartão individual para os campos restantes.

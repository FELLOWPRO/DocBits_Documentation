# Regras de Transformação: visão geral prática completa

> Limitação conhecida da pré-visualização (verificada em 29 de outubro de 2026, versão 11.15.2): ao adicionar o prefixo `INV-`, a pré-visualização altera incorretamente `INV-4711` para `INV-INV-4711`. O teste independente do servidor mantém `INV-4711`. Verifique também a execução repetida com um teste do servidor; um resultado correto na pré-visualização, por si só, não comprova a execução completa ao guardar.

Data da verificação: 28 de outubro de 2026. Os exemplos foram verificados com valores sintéticos de formação no Dev NOVA. Uma pré-visualização não é prova de uma alteração de documento guardada, de uma reconciliação de encomenda ou de uma exportação ERP.


## Etiquetas visíveis no editor

Algumas etiquetas da interface atual apresentam traduções imprecisas. A tabela indica o texto realmente apresentado para encontrar o passo correto; a explicação funcional utiliza terminologia técnica. As capturas mostram a interface sem alterações.

| Operação | Etiqueta visível |
| --- | --- |
| case | Alterar maiúsculas/minúsculas |
| trim | Aparar |
| pad | Almofada |
| truncate | Truncar |
| affix | Afixo |
| sanitize | Limpar |
| substring | Pegue uma fatia |
| regex_extract | Extrair |
| regex_replace | Localizar e substituir |
| value_map | Mapear valores |
| date_format | Data de reformatação |
| number_format | Número de formato |
| fix_value | Valor fixo |
| clear | Limpar |
| clear_rows | Limpar todas as linhas |
| add_row | Adicionar linha |


## Quatro Âmbitos de Aplicação

| Âmbito | Entrada e Destino | Tarefa Típica |
| --- | --- | --- |
| Campo de cabeçalho | Um campo por documento; a fonte pode ser outro campo de cabeçalho | Limpar número de fatura, assumir número de encomenda |
| Coluna de tabela | A coluna selecionada por linha da tabela selecionada | Uniformizar números de artigo ou códigos de unidade |
| Linhas de tabela | Tabela completa | Remover linhas ou adicionar posições definidas |
| Routing | Atributo de documento `sub_org_id` | Atribuir suborganização existente |

Os âmbitos executam-se **Cabeçalho → Routing → Linhas de tabela → Coluna de tabela**. Dentro de um âmbito, a prioridade e a chave de regra determinam a ordem. Os passos de uma regra executam-se de cima para baixo. Uma regra posterior pode, portanto, ler valores já alterados. A ordem dos âmbitos não é invertida pela prioridade de uma única regra.

## Todos os Passos do Editor

O editor verificado oferece 14 passos de valor para cabeçalho/coluna, dois passos para tabelas completas e uma atribuição fixa no routing. `fix_value` e a atribuição fixa de routing utilizam ambos, do lado do servidor, `set_value`. Adicionalmente, a interface conhece `default`; este passo não é oferecido no menu normal de passos verificado.

| Passo | Variantes e Parâmetros | Exemplo | Limite e Prova de Contrário |
| --- | --- | --- | --- |
| Alterar maiúsculas/minúsculas (`case`) | upper, lower, title, capitalize | `inv-4711` → `INV-4711` | Title: `acme gmbh` → `Acme Gmbh`; capitalize: `aCME GMBH` → `Acme gmbh`. Nomes próprios/abreviaturas podem alterar-se de forma tecnicamente indesejável. Em `capitalize`, a pré-visualização do navegador verificada deixa o resto inalterado, enquanto o servidor o escreve em minúsculas; verificar o valor do servidor separadamente. |
| Aparar (`trim`) | ambos / esquerda / direita; carateres vazio = espaço em branco | `  4711  ` → `4711` | `47 11` permanece preservado. Carateres à esquerda `0`: `004711` → `4711`, mas `000` → vazio. Os carateres são um conjunto, não um texto de prefixo completo. |
| Preencher (`pad`) | comprimento mínimo, um caráter de preenchimento, esquerda/direita | Comprimento 10, esquerda `0`: `4711` → `0000004711` | Já com 11 carateres permanecem 11 carateres. Direita `_`, comprimento 6: `ABC` → `ABC___`. |
| Truncar (`truncate`) | comprimento máximo | Comprimento 10: `ABCDEFGHIJKL` → `ABCDEFGHIJ` | `ABC` permanece `ABC`. O corte perde informação e pode fazer com que números coincidam. |
| Afixo (`affix`) | adicionar/remover prefixo/sufixo | `INV-` + `4711` → `INV-4711` | Um afixo exato existente não é adicionado duplicado. A remoção só atua na extremidade adequada e respeita a capitalização. |
| Limpar carateres (`sanitize`) | manter alfanumérico / letras / dígitos / alfanumérico + espaço; alternativamente remover classe de carateres | `DE 123.456.789` → `DE123456789` | Os símbolos podem ser semanticamente relevantes. Na remoção, a entrada é uma classe de carateres de expressão regular; proteger corretamente o hífen, por exemplo `.\-/`. |
| Fragmento (`substring`) | início + comprimento **ou** início + fim; índices negativos possíveis | Início 3, fim 7: `DE-4711-X` → `4711` | O início conta a partir de 0, o fim é exclusivo. Início −4: últimos quatro carateres. Fonte original separada necessária. |
| Extrair (`regex_extract`) | expressão regular, grupo de captura | `PO[- ]?(\d+)`, grupo 1: `Order PO-45001234` → `45001234` | Primeira correspondência; grupo 0 = correspondência completa. Sem correspondência: vazio. Fonte separada necessária. |
| Procurar e Substituir (`regex_replace`) | padrão, substituto, quantidade | `\s+` → espaço: `ACME    GmbH` → `ACME GmbH` | Quantidade 0 = todas, 1 = primeira correspondência. Fonte separada necessária. Verificar expressões regulares de navegador/servidor separadamente para padrões complexos. |
| Mapear valores (`value_map`) | pares completos de→para; ignorar capitalização; substituto sem correspondência | `stk` → `PCE` com `STK→PCE` e capitalização ignorada | Substituto vazio significa **manter entrada**. `BOX` permanece `BOX`; um substituto fixo `C62` sobrescreveria `BOX`. O aparar não ocorre automaticamente. |
| Formatar data (`date_format`) | padrão de saída, por exemplo `%d.%m.%Y`, `%m/%d/%Y`, `%Y-%m-%d`, `%d %b %Y` | `2026-10-28` → `28.10.2026` no destino de texto | Em campos de cabeçalho DATE, o valor guardado pode permanecer ISO e apenas a representação alterar-se. Texto ilegível permanece inalterado; o teste do servidor indica o motivo. |
| Formatar número (`number_format`) | de_DE / en_US / en_GB / fr_FR; min./máx. casas decimais | `1234.5` → `1234,50` ou `1234.50` no resultado do servidor verificado | Sem separador de milhares no resultado do servidor verificado. Sem conversão de moeda ou de unidade. Verificar arredondamento e reprocessamento separadamente. |
| Valor fixo (`fix_value` no editor, `set_value` na API) | um valor fixo | `USD` → `EUR` | Também sobrescreve valores existentes. Não confundir com um valor por omissão. |
| Esvaziar (`clear`) | sem parâmetros | `Altwert` → `""` | Esvazia o valor; não elimina a definição de campo nem o documento. |
| Eliminar todas as linhas (`clear_rows`) | apenas linhas de tabela | 2 posições → 0 | Pode invalidar referências de linhas e a reconciliação de PO existente. |
| Adicionar linha (`add_row`) | início/fim; por coluna valor fixo ou fonte de cabeçalho | Quantidade `1`, valor líquido de `header.total_net_amount` | Sem eliminação prévia apenas com execução única adequada. Sem agregação automática de posições existentes. |
| Suborganização fixa (`set_value`, Routing) | destino existente da seleção de suborganizações | Fornecedor A → Suborganização Norte | Não é um atributo de estado/utilizador/permissão arbitrário. Alternativamente, atribuição via `value_map` e fonte. |

### Valor por Omissão via Interface

`default` complementa o seu valor apenas em caso de entrada ausente/vazia. Com omissão `1`, `null` e `""` resultam no valor `1`; `0` permanece `0`, `100` permanece `100`. Isto é verificado do lado do servidor. O editor normal não tem, no estado verificado, um passo próprio para isto. O caso simples funcionalmente correspondente pode frequentemente ser representado com **Destino está vazio → Valor fixo**. Isto é uma condição de regra com atribuição, não um item de menu oculto.

## Nove Sequências Práticas Detalhadas

- [01 · Fundamentos, âmbitos de aplicação e testes seguros](01-foundations.md)
- [02 · Limpar texto: escrita, aparar e carateres](02-text-cleaning.md)
- [03 · Moldar números: preencher, truncar, prefixo e sufixo](03-numbers-and-affixes.md)
- [04 · Fragmentos e padrões: recortar, extrair, substituir](04-substrings-and-patterns.md)
- [05 · Mapeamentos de valor e regras por linha de tabela](05-value-mapping.md)
- [06 · Formatar datas e números corretamente](06-dates-and-numbers.md)
- [07 · Assumir campos, valores fixos, esvaziar e valores por omissão](07-field-copy-and-defaults.md)
- [08 · Reconstruir linhas de tabela](08-table-rows.md)
- [09 · Routing, ordem, dados mestre e repetições](09-routing-and-execution.md)

| Sequência | Conteúdo | Ponto de Verificação Concreto |
| --- | --- | --- |
| 01 Fundamentos | Destino, fonte, quatro âmbitos, pipeline, condições, pré-visualização, armazenamento | Caso adequado, caso de contrário, regra guardada reaberta |
| 02 Limpeza de texto | Todas as quatro formas de escrita, aparar, todos os modos de limpeza | Espaços internos, sequência pura de zeros, carateres semanticamente relevantes |
| 03 Números | Preencher, truncar, todas as quatro variantes de afixo | Número demasiado longo, prefixo já existente, prefixos duplicados |
| 04 Padrões | Fragmento, índices negativos, extração/grupos, substituir/quantidade | Fonte separada, sem correspondência, várias correspondências |
| 05 Mapeamento | Pares, capitalização, substituto, aplicação por linha | `STK→PCE`, `BOX` desconhecido, reaplicação em `PCE` |
| 06 Formatos | Data, DATE vs. texto, data ilegível, formatos numéricos | Valor real do servidor em vez de representação assumida do navegador |
| 07 Assunção de campo | Outra fonte, destino vazio, valor fixo, esvaziar, valor por omissão da API | Proteger número de encomenda correto existente; zero permanece zero |
| 08 Tabelas | Eliminar, adicionar, valores de coluna estáticos e dinâmicos | Ordem, repetição, número de linhas e referências de PO |
| 09 Interação | Routing, fases, lookup, execução única, registos | Fonte de cabeçalho limpa, condição ignorada, segundo armazenamento |

## Condições e Fontes

Com "Sempre", a regra aplica-se sem restrição funcional para o tipo de documento. "Apenas se…" limita-a por condições. Os valores de cabeçalho estão no contexto `header.*`, as caraterísticas de documento em `doc.*`; `row.*` está disponível apenas no contexto de linha de uma regra de coluna. Grupos aninhados de E/Ou permitem critérios combinados. Para os operadores individuais, aplica-se a documentação separada das condições de regra.

**Exemplo de assunção de campo:** Destino `purchase_order`, fonte `header.invoice_id`, condição `header.purchase_order` está vazio, passos Aparar → Maiúsculas. `  po-4711  ` resulta em `PO-4711`. Um número de encomenda já corretamente preenchido deve permanecer inalterado. Não esvaziar a fonte errada: copiar com processamento não move a fonte.

**Exemplo de número de artigo:** Tabela `INVOICE_TABLE`, coluna `ITEM_NUMBER`, remover prefixo `Art.-Nr. ` → manter alfanumérico → maiúsculas. `Art.-Nr. ab-12/3` resulta em `AB123`. Adequado apenas se o sistema de destino esperar exatamente esta forma.

**Exemplo de linha total:** Para um fornecedor claramente delimitado, primeiro `clear_rows`, depois `add_row`; `POSITION=001`, `QUANTITY=1`, `NET_AMOUNT` do valor líquido do cabeçalho. Se a reconciliação de encomenda sobre o total está funcionalmente correta, é decidido pela configuração adicional de PO e por um teste de reconciliação separado.

## Repetição e Execução Única

As regras podem executar-se em vários ciclos de processamento e ao guardar novamente. Verifique sempre **toda a pipeline**, não apenas a estabilidade de um único passo.

* `substring`, `regex_extract` e `regex_replace` não podem, no contrato de servidor verificado, ler o seu próprio valor de destino. Uma fonte separada é necessária; `run_once` não levanta esta exigência.
* Complementar um afixo exato já existente é estável. Remover um prefixo múltiplo presente pode, pelo contrário, remover mais a cada ciclo.
* `A→B` e `B→C` no mesmo mapeamento de valor podem, em dois ciclos, fazer com que `A` finalmente se torne `C`. Teste saídas novamente como entradas.
* `clear_rows → add_row` reconstrói uma tabela de forma limitada. `add_row` sem eliminação prévia necessita de uma execução única adequada, senão a tabela cresce a cada armazenamento.
* "Apenas uma vez por documento" marca uma regra efetivamente aplicada. Condições não cumpridas não consomem a aplicação. Sem prova de documento/aplicação fiavelmente legível, a execução de uma regra de uma só vez é adiada.

## Após o Lookup e Antes da Reconciliação de Encomenda

"Também executar após a pesquisa de dados mestre" acrescenta uma fase após o preenchimento do lookup e antes da reconciliação de PO. Apenas regras assim marcadas executam nesta fase adicional. Os restantes ciclos permanecem. Combinado com execução única, a regra aguarda na primeira extração a fase posterior; se a fase de lookup falhar, um ciclo regular posterior entra em consideração. A visualização de fases do editor atual mostra estas diferenças.

## Um Teste de Aceitação Robusto

1. Definir objetivo funcional, formato do sistema de destino e âmbito de aplicação.
2. Preparar um valor bruto adequado, um caso de contrário, um valor vazio e um resultado já processado.
3. Verificar condições e todos os valores intermédios na pré-visualização.
4. Executar teste do lado do servidor com o mesmo exemplo; comparar particularmente padrões complexos e formatos de número/data.
5. Guardar e reabrir a regra. Utilizar uma regra ativa apenas no âmbito de teste previsto.
6. Num documento isolado, guardar, recarregar novo e verificar valor e exibição; em tabelas, também número de linhas e valores de coluna.
7. Guardar novamente. O resultado não deve ser alterado ou multiplicado inadvertidamente.
8. Se funcionalmente necessário, verificar também a reconciliação de PO e a receção real no sistema de destino. Um registo de transformação por si só não prova estes resultados.

## O que uma Transformação Não Faz Automaticamente

Nenhum novo reconhecimento OCR, nenhuma conversão matemática de unidade ou moeda, nenhuma agregação arbitrária de tabelas e nenhuma contabilização ERP completa. O routing está limitado ao atributo de documento oferecido. A disponibilidade e a exibição exata dependem da versão implementada, do tipo de documento e da configuração da organização.

## Documento de Exercício Contínuo

{% file src="../../../../../.gitbook/assets/transformation-training-invoice-pt-20261028.pdf" %}
Transferir fatura de formação
{% endfile %}

O documento fictício contém duas posições, diferentes formas de escrita da unidade e uma referência de encomenda no texto livre. Para testes de regra reproduzíveis, os valores de partida são preparados propositadamente; isto não é prova de uma extração OCR automaticamente isenta de erros.

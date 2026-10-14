# Regras de Transformação

## Visão Geral

As regras de transformação limpam ou reescrevem dados extraídos **automaticamente** — um campo no cabeçalho, uma coluna em uma tabela, linhas inteiras da tabela ou um atributo do documento — toda vez que um documento é processado e toda vez que é salvo. Elas substituem os pequenos scripts que muitas organizações costumavam escrever para "sempre aparar este campo", "definir esta coluna como 1 por padrão", "mapear os códigos de unidade deste fornecedor" ou "agrupar os itens desta linha de um fornecedor em uma linha total".

Uma regra é definida por **tipo de documento** e é executada em todo documento desse tipo. As regras são executadas **antes** da validação, scripts e correspondência de pedidos de compra, para que tudo a jusante já veja os valores transformados.

## Como acessar

1. Navegue até **Configurações → Configurações Globais → Tipos de Documento**.
2. Abra o tipo de documento e escolha **Regras de Transformação**. A lista mostra todas as regras do tipo com seu escopo, alvo, prioridade e se está ativa.
3. Clique em **Nova regra** para abrir o construtor de regras, ou abra uma regra existente para alterá-la.

## Anatomia de uma regra

| Parte                  | O que é                                                                                                                                                                                                                                           |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nome / chave**       | O nome exibido mostrado em listas, mensagens e no histórico de correspondência, e uma chave técnica que permanece estável quando você renomeia a regra.                                                                                           |
| **Escopo**             | Onde a regra escreve: um **campo de cabeçalho**, uma **coluna de tabela**, uma **tabela** (linhas inteiras) ou um **atributo do documento**. Veja abaixo.                                                                                         |
| **Alvo**               | O campo, coluna (com sua tabela) ou tabela para o qual a regra escreve.                                                                                                                                                                           |
| **Fonte**              | Opcional. De onde a regra lê sua entrada em vez do próprio alvo: `header.<field>` para um campo de cabeçalho, `doc.<attribute>` para um atributo do documento, `row.<column>` para outra coluna da mesma linha (apenas escopo coluna).            |
| **Quando**             | **Sempre**, ou **somente quando** uma condição for verdadeira (veja Condições).                                                                                                                                                                   |
| **Ações**              | A lista de transformações, aplicadas em ordem; a saída de uma ação é a entrada da próxima.                                                                                                                                                        |
| **Prioridade**         | Regras do mesmo escopo são executadas em ordem crescente de prioridade (depois pela chave). Use quando uma regra precisa ver o resultado de outra.                                                                                                |
| **Executar uma vez**   | A regra se aplica a um documento **no máximo uma vez**. Necessário para ações que mudariam o valor novamente a cada salvamento (substring, regex\_replace, regex\_extract) e para regras de tabela que não devem reconstruir as linhas novamente. |
| **Registrar execução** | Escreve uma linha de log por aplicação — útil enquanto você ajusta uma nova regra.                                                                                                                                                                |

### Escopos

| Escopo                    | Escreve em                                                      | Regra típica                                                                                 |
| ------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| **Campo de cabeçalho**    | um campo extraído do cabeçalho (número da fatura, moeda, …)     | aparar e colocar em maiúsculas o número da fatura; mapear "EUR€" para "EUR"                  |
| **Coluna de tabela**      | uma coluna em cada linha de uma tabela                          | definir `UNIT_PRICE_PER` como 1 por padrão; remover o prefixo "Art.-Nr." do número do item   |
| **Tabela**                | as linhas de uma tabela                                         | limpar as linhas e adicionar uma linha total para um fornecedor que é correspondido no total |
| **Atributo do documento** | um atributo do próprio documento (atualmente a sub-organização) | direcionar documentos de um fornecedor para uma sub-organização                              |

As regras são executadas escopo por escopo nesta ordem: cabeçalho → documento → tabela → coluna. Uma regra de coluna, portanto, já vê linhas que uma regra de tabela adicionou.

### Condições ("somente quando")

Uma condição compara um valor do documento com uma constante. O valor vem de um campo de cabeçalho (`header.<field>`), um atributo do documento (`doc.<attribute>`) ou, para regras de coluna, uma coluna da linha atual (`row.<column>`).

| Operador                                    | Significado          |
| ------------------------------------------- | -------------------- |
| é / não é                                   | comparação exata     |
| é um dos / não é um dos                     | valor em uma lista   |
| contém, começa com, termina com             | comparação de texto  |
| está vazio / não está vazio                 | não precisa de valor |
| maior que, menor que, pelo menos, no máximo | comparação numérica  |
| corresponde                                 | expressão regular    |

Condições podem ser agrupadas com **todas as** (e) e **qualquer das** (ou) e negadas com **não**. Exemplo: _somente quando `header.supplier_id` é `20723`_ — a regra roda para um fornecedor apenas.

### Ações

Ações para campos de cabeçalho e colunas de tabela (formam um pipeline; o valor entra no topo e sai na base):

| Ação            | Efeito                                                                                                                           |
| --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `trim`          | remove espaços em branco (ou caracteres dados) à esquerda, direita ou ambos os lados                                             |
| `case`          | maiúsculas, minúsculas, título ou capitalizar                                                                                    |
| `pad`           | preenche até um comprimento com um caractere, à esquerda ou direita                                                              |
| `truncate`      | corta até um comprimento máximo                                                                                                  |
| `affix`         | adiciona um prefixo ou sufixo, ou remove um deles                                                                                |
| `sanitize`      | mantém apenas uma classe de caracteres (alfanumérico, alfa, numérico, alfanumérico + espaço) ou remove um conjunto de caracteres |
| `substring`     | pega uma parte do valor por início e comprimento ou fim                                                                          |
| `regex_replace` | substitui o que uma expressão regular corresponde                                                                                |
| `regex_extract` | mantém o que uma expressão regular captura                                                                                       |
| `value_map`     | mapeia valores para outros valores (opcionalmente sem diferenciar maiúsculas/minúsculas, com um padrão)                          |
| `date_format`   | reformata uma data (a entrada deve ser a data ISO que o DocBits armazena em `value`)                                             |
| `number_format` | reformata um número                                                                                                              |
| `default`       | define um valor somente quando o campo está vazio                                                                                |
| `set_value`     | define um valor fixo, qualquer que fosse o conteúdo do campo                                                                     |
| `clear`         | esvazia o campo                                                                                                                  |

Ações para escopo **tabela** (funcionam em linhas, não em valores, e não podem ser misturadas com as ações acima):

| Ação         | Efeito                                                                                                                                                          |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `clear_rows` | deleta todas as linhas da tabela                                                                                                                                |
| `add_row`    | adiciona uma linha no final ou no início; cada coluna recebe um valor fixo ou um valor lido do cabeçalho (`header.<field>`) ou do documento (`doc.<attribute>`) |

{% hint style="info" %}
`substring`, `regex_replace` e `regex_extract` mudam um valor novamente quando são executados em um valor já transformado. Combine-os com **Executar uma vez**, ou escreva a expressão regular para que uma segunda execução não tenha mais nada a alterar.
{% endhint %}

## Quando as regras são executadas

* Durante o processamento, após a extração e antes da validação, scripts e correspondência de pedidos de compra.
* Em **cada salvamento** do documento em que os dados extraídos mudaram. Regras sem **Executar uma vez** são aplicadas novamente a cada salvamento; porque toda ação exceto as três acima é idempotente, um valor que já está na forma alvo permanece como está.

## Regras de transformação e correspondência de pedidos de compra

Regras de tabela e regras de coluna mudam o que o sistema de correspondência de pedidos de compra vê:

* Uma regra de tabela que **reconstrói** linhas (por exemplo, limpa todas as linhas e adiciona uma linha total) mantém uma correspondência de pedido de compra existente desde que produza **as mesmas linhas novamente** — os valores são comparados pelo significado, então `1.0` e `1.00` são a mesma linha. As linhas mantêm sua identidade e a correspondência sobrevive a cada salvamento.
* Se uma regra **substitui ou remove linhas que foram correspondidas**, a correspondência não pode ser mantida. O documento então registra qual regra a descartou, a tela de Correspondência de Pedidos de Compra mostra isso como motivo ("_A correspondência do pedido de compra não pôde ser salva: a regra de transformação "…" reconstruiu a tabela_") e os administradores recebem um link para a regra. O **histórico de correspondência** do documento mostra uma etapa _Regras de transformação_ antes da primeira etapa de correspondência com as regras que foram executadas.
* O número de linhas após as regras é o que as [condições de ativação](https://github.com/Fellow-Consulting-AG/docbits/tree/pt/readme/administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md#activation-conditions) das regras de correspondência contam. Uma regra que colapsa uma fatura em **uma** linha só faz sentido junto com uma regra de correspondência por total que está ativa para documentos de uma linha (`[[count(table_lines)]] >= 1`).

## Exemplos

**Limpar o número da fatura** — campo de cabeçalho `invoice_id`, sempre: `trim` → `case` maiúsculas.

**Definir o preço base por padrão** — coluna de tabela `UNIT_PRICE_PER` da tabela de itens da linha, sempre: `default` `1`.

**Mapear os códigos de unidade de um fornecedor** — coluna de tabela `UNIT` da tabela de itens da linha, somente quando `header.supplier_id` é `10040`: `value_map` `{ "STK": "PCE", "KG": "KGM" }`.

**Uma linha total para um fornecedor que é correspondido no total** — escopo tabela na tabela de itens da linha, somente quando `header.supplier_id` é `20723`: `clear_rows`, depois `add_row` com `POSITION` = `001`, `UNIT_PRICE` = `1.0`, `QUANTITY` = `header.total_net_amount`, `NET_AMOUNT` = `header.total_net_amount`. Combine com uma regra de correspondência por total cuja condição de ativação aceita um documento de uma linha.

**Direcionar um fornecedor para uma sub-organização** — atributo do documento `sub_org_id`, somente quando `header.supplier_id` é um dos `[…]`: `set_value` `<id da sub-organização>`.

## Solução de Problemas

| Sintoma                                                             | O que verificar                                                                                                                                                                                       |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A regra não mudou nada                                              | Está ativa? O tipo de documento corresponde? A condição é verdadeira para este documento (compare o valor exato, incluindo espaços)? Uma regra com **Executar uma vez** já foi aplicada ao documento? |
| O valor muda novamente a cada salvamento                            | O pipeline contém `substring`, `regex_replace` ou `regex_extract`. Ative **Executar uma vez** ou torne a expressão idempotente.                                                                       |
| A correspondência do pedido de compra é perdida após salvar         | Uma regra de tabela substituiu as linhas correspondidas. O motivo no documento nomeia a regra; faça a regra reproduzir as mesmas linhas, ou defina para **Executar uma vez**.                         |
| Uma regra de correspondência nunca é executada após a transformação | A regra mudou o número de linhas; ajuste a condição de ativação da regra de correspondência.                                                                                                          |

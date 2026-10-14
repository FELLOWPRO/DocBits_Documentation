# Regras de Correspondência de Pedido de Compra

## Introdução: Pedidos de Compra e Gestão de Regras de PO

A Correspondência de Pedido de Compra (PO) é um processo crítico para garantir a consistência entre os Pedidos de Compra (POs) e as faturas ou recibos de mercadorias correspondentes. Um conjunto robusto de regras é essencial para alcançar uma alta taxa de correspondência automática, prevenir fraudes e garantir pagamentos corretos.

Esta página de configuração é usada para definir e gerenciar as regras que determinam _como_ os itens das linhas do PO são correspondidos ao documento de entrada correspondente (Fatura, Confirmação de Pedido).

{% hint style="info" %}
**Pré-requisito:** as regras de correspondência são usadas apenas quando o **PO match server side** está ativado para o tipo de documento (Configurações → Tipos de Documento → Mais Configurações → Pedido de Compra). Com o interruptor desligado, o DocBits faz a correspondência com seu mecanismo interno (quantidade, preço unitário, número do item, número do pedido de compra) e ignora o conjunto de regras.
{% endhint %}

***

## Como Acessar

1.  Navegue até **Configurações --> Configurações Globais --> Tipos de Documento**

    <figure><img src="../../../../../../.gitbook/assets/image (31).png" alt=""><figcaption></figcaption></figure>


2.  Selecione o tipo de documento desejado e clique em **Mais Configurações**.

    <figure><img src="../../../../../../.gitbook/assets/image (40).png" alt=""><figcaption></figcaption></figure>


3.  Depois vá para a Seção Pedido de Compra e clique no botão (PO match server side) e em seguida clique em Configurar Regras de Correspondência de PO

    <figure><img src="../../../../../../.gitbook/assets/image (168).png" alt=""><figcaption></figcaption></figure>

***

<figure><img src="../../../../../../.gitbook/assets/Bildschirmfoto 2025-12-09 um 07.43.15.png" alt=""><figcaption></figcaption></figure>

## Configurações Globais (Regras Base)

Estas configurações estabelecem a estrutura que se aplica a todas as regras de correspondência:

* **Configuração:** Quantidade para Correspondência
  * **Objetivo:** Define qual quantidade da linha do pedido de compra é comparada com a linha do documento — por exemplo, a quantidade pedida ou a **quantidade aberta da fatura** (pedido menos já faturado), que é a escolha usual para faturas.
  * **Valores Válidos:** Quantidade ou outros campos de quantidade disponíveis no sistema, dependendo da estrutura dos dados (por exemplo, um campo alternativo de quantidade normalizada).
  * **Dependência:** Determina a base para todas as regras de correspondência que incluem quantidade em seus critérios de comparação.
* **Configuração:** Tolerância Padrão (Tolerância Default)
  * **Objetivo:** Define o quanto um valor numérico no documento pode se desviar do valor do pedido de compra e ainda ser considerado uma correspondência. Compensa diferenças de arredondamento. Aplica-se a **todas as colunas numéricas** com "Permitir Tolerância" ativado — quantidade e preço unitário.
  * **Valor Válido:** Um número decimal. Se é interpretado como um **valor absoluto** (0.005 = uma variação de até 0.005 na quantidade ou preço comparado) ou como uma **percentagem** (0.5 = 0,5 % do valor comparado) é definido pelo **tipo de tolerância** do conjunto de regras (`value` ou `percent`; novos conjuntos usam `value`). Tolerâncias por item (veja [Configurações de Tolerância](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)) substituem a tolerância padrão para aquele item.
  * **Dependência:** Aplica-se a regras que usam campos numéricos para correspondência e têm a opção "Permitir Tolerância" ativada.

***

## Lista de Regras

A Lista de Regras exibe todas as regras de correspondência disponíveis e gerencia sua ordem de execução.

#### Estrutura e Execução

* **Prioridade:** Este campo numérico (ex.: 1, 2, 3) dita a sequência de execução das regras. Regras com número de prioridade menor são tentadas primeiro. Isso permite que os administradores estruturem uma hierarquia, normalmente começando pelas regras mais específicas e rigorosas (ex.: correspondência por número de linha e número da peça) e recuando para regras mais amplas ou menos restritivas.
* **Nome & Descrição:** Fornece identificação clara e contexto para a regra, explicando os critérios principais usados (ex.: "Regra Padrão Nº 1: Correspondência baseada em Número da Linha, ID do Item e Quantidade").
* **Ativa:** Um simples interruptor que permite ativar ou desativar instantaneamente a regra sem precisar excluir sua configuração.

**Fluxo de Execução:** O sistema realiza a correspondência em sequência cascata. Se uma regra (ex.: Prioridade 1) corresponder com sucesso a um item da linha, o processo para aquele item é interrompido. Se nenhuma correspondência for encontrada, o sistema passa para a próxima regra na sequência de prioridade (ex.: Prioridade 2). Cada execução é registrada no documento; o **histórico de correspondência** na tela de Correspondência de Pedido de Compra mostra qual regra foi tentada, qual correspondeu e quais foram puladas e por quê.

***

## Configuração da Regra (Configurações Detalhadas)

Esta área detalhada de configuração define a lógica e os critérios específicos para uma regra individual.

#### Parâmetros Base

* **Tipo de Regra:** Especifica a cardinalidade da correspondência.

| Tipo de regra       | O que faz                                                                                                                                                                                               | Uso típico                                                                    |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Correspondência única** | Uma linha do pedido de compra para uma linha do documento. Todas as colunas configuradas devem concordar (dentro da tolerância onde permitida).                                                         | O caso padrão.                                                                |
| **Correspondência múltipla** | Várias linhas do pedido de compra para uma linha do documento, ou várias linhas do documento para uma linha do pedido de compra. Quantidades são **somadas**, o preço unitário é comparado como uma **média**, as outras colunas devem concordar. | Entregas fracionadas, uma linha de fatura que cobre várias linhas do pedido. |
| **Correspondência no total** | Compara um **valor** — geralmente o valor líquido da linha do documento contra o **total** do pedido de compra — e corresponde ao pedido inteiro de uma vez.                                         | Fornecedores que faturam um valor global, faturas de serviço, faturas de uma linha. |

* **Correspondência Automática:** Se ativado, o sistema tentará aplicar esta regra totalmente de forma automática. É necessária alta confiança nos critérios para o processamento automático.
* **Correspondência Manual:** Se ativado, esta regra pode ser apresentada ou aplicada por um usuário durante a etapa de reconciliação manual, oferecendo um conjunto pré-definido de critérios de comparação para resolver exceções.
* **Fallback:** Uma regra marcada como fallback é executada em uma fase posterior, apenas para os pares de linhas que ainda não foram correspondidos após todas as regras regulares terem sido executadas. Use para a regra "mais flexível" que deve capturar o que as regras rigorosas perderam.

#### Condições de Ativação

Uma regra pode conter **condições de ativação** — expressões que devem ser verdadeiras antes que a regra seja executada. Se uma condição for falsa, a regra é **ignoradas para este documento** (o histórico de correspondência mostra como "não executada" com o motivo). As expressões usam as contagens das linhas que estão sendo correspondidas:

| Expressão               | Significado                                                         |
| ----------------------- | ------------------------------------------------------------------ |
| `[[count(po_lines)]]`    | número de linhas do pedido de compra disponíveis para correspondência |
| `[[count(table_lines)]]` | número de itens da linha no documento que estão mapeados para correspondência |

Compare-os com `==`, `!=`, `>`, `>=`, `<`, `<=` e combine várias condições com `&` (e). Exemplos:

* `([[count(po_lines)]] > 1) & ([[count(table_lines)]] > 1)` — apenas para documentos com várias linhas em ambos os lados (típico para uma regra de correspondência múltipla).
* `([[count(po_lines)]] == 1) & ([[count(table_lines)]] == 1)` — apenas para documentos de uma linha contra um pedido de uma linha.
* `([[count(po_lines)]] >= 1) & ([[count(table_lines)]] >= 1)` — sempre que houver algo para corresponder.

{% hint style="warning" %}
Condições de ativação são a razão mais comum pela qual uma regra "não faz nada". Uma regra de correspondência no total com a condição `[[count(table_lines)]] > 1` nunca é executada para uma fatura de uma linha — e uma [regra de transformação](../../transformation-rules.md) que colapsa a fatura em uma linha total produz exatamente esse tipo de documento. Verifique as contagens no histórico de correspondência antes de alterar a regra em si.
{% endhint %}

#### Comparação de Colunas (Critérios de Correspondência)

Esta é a definição central da lógica da regra, especificando quais campos devem estar alinhados entre os documentos.

1. Definindo as Colunas a Comparar:
   * **Colunas do PO:** O campo extraído dos dados do Pedido de Compra (ex.: número da linha).
   * **Colunas da Tabela Extraídas:** O campo correspondente extraído ou analisado do documento de entrada (Fatura/Confirmação de Pedido) (ex.: `POSITION`).
2. **Tipo de Comparação:** Define a natureza da correspondência requerida (ex.: Tt para comparação de Texto/String, exigindo correspondência exata caractere por caractere; # para comparação Numérica).
3. **Permitir Tolerância:** Para campos numéricos (quantidade, preço), ativar esta opção instrui o sistema a aplicar a Tolerância Padrão Global definida anteriormente. Se _não_ estiver ativado para um campo numérico, os valores devem corresponder exatamente.
4. **Ignorar na Correspondência Manual:** Se marcado, este critério é relaxado durante a intervenção manual. Isso é útil para campos como descrições ou referências internas que podem variar ligeiramente, permitindo que o usuário ignore pequenas discrepâncias não críticas.

**Quais colunas podem ser comparadas**

| Coluna                          | Lado do documento                         | Lado do pedido de compra                 | Nota                                                                                                                                                                                                                              |
| ------------------------------- | ---------------------------------------- | ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Número da linha                 | `POSITION`                               | `line_number`                            | Texto, exato. Útil apenas quando o fornecedor imprime os números das linhas do pedido no documento.                                                                                                                               |
| Identificador do item           | `ITEM_IDENTIFIER`                        | `item_identifier`                        | Texto, exato. Número do item ou número do item do fornecedor, também via o [Mapa de Número de Item do Fornecedor](supplier-item-number-map-admin-documentation.md).                                                                |
| Quantidade normalizada efetiva  | `QUANTITY_EFFECTIVE_NORMALIZED`          | `quantity_effective_normalized`          | Numérico. A quantidade selecionada por **Quantidade para Correspondência**, convertida para a mesma unidade em ambos os lados (conversão de código de unidade, quantidades "por").                                                   |
| Preço unitário normalizado efetivo | `UNIT_PRICE_EFFECTIVE_NORMALIZED`        | `unit_price_effective_normalized`        | Numérico. O preço unitário por unidade após descontos e após **Preço Unitário Por** — e, se [Calcular preço unitário do PO](calculate-po-unit-price.md) estiver ativado, o preço calculado a partir do valor e quantidade da linha do pedido. |
| Valor líquido                  | `NET_AMOUNT`                             | `total_amount`                           | Numérico. Usado por regras de correspondência no total.                                                                                                                                                                          |

**Exemplo: Regra Rigorosa de Correspondência de PO (`DefaultRule#1`)**

Uma regra rigorosa típica combina verificações obrigatórias de identidade com verificações de valor:

* **Identidade Obrigatória:** Número da Linha e Identificador do Item devem corresponder exatamente (Comparação de Texto, sem tolerância).
* **Verificações de Valor:** Quantidade Normalizada Efetiva e Preço Unitário Normalizado Efetivo devem corresponder (Comparação Numérica, Tolerância Permitida). Somente se todos os quatro critérios forem atendidos (com tolerância para valores) é executada uma correspondência automática.

***

## O conjunto de regras padrão

Toda organização começa com o mesmo conjunto de regras padrão. É uma boa referência quando você constrói o seu próprio:

| Regra                      | Tipo / prioridade               | Colunas comparadas                                                       | Condição de ativação                                  |
| -------------------------- | ------------------------------ | ----------------------------------------------------------------------- | ---------------------------------------------------- |
| `DefaultRule#1`            | correspondência única, prioridade 1 | número da linha, identificador do item, quantidade (tol.), preço unitário (tol.) | sempre                                               |
| `DefaultMultiMatchRules#1` | correspondência múltipla, prioridade 1, fallback | identificador do item, quantidade (tol.), preço unitário (tol.)         | `count(po_lines) > 1` e `count(table_lines) > 1`     |
| `DefaultTotalMatchRules#1` | correspondência no total, prioridade 1 | valor líquido ↔ total do pedido de compra (sem tolerância)              | `count(po_lines) >= 1` e `count(table_lines) > 1`    |
| `DefaultRule#2`            | correspondência única, prioridade 2, fallback | identificador do item, quantidade (tol.), preço unitário (tol.)         | sempre                                               |
| `DefaultRule#3`            | correspondência única, prioridade 2, fallback | quantidade (tol.), preço unitário (tol.)                                | `count(po_lines) == 1` e `count(table_lines) == 1`   |

Lendo de cima para baixo: primeiro a regra rigorosa (número da linha e item devem estar impressos no documento), depois os fallbacks sem o número da linha, depois um último recurso para documentos de uma linha que compara apenas quantidade e preço.

***

## Impacto no Processo de Correspondência de PO

O conjunto de regras definido governa diretamente a eficiência e integridade do fluxo de trabalho de correspondência de PO:

* **Priorização e Fallbacks:** A Prioridade definida garante que o sistema tente primeiro o método de correspondência mais confiável. Se as regras rigorosas e de alta prioridade falharem, o sistema recua para regras mais amplas, visando minimizar o número de exceções encaminhadas aos usuários.
* **Controle da Qualidade da Correspondência:** Regras mais rigorosas (exigindo correspondências mais exatas e menos tolerância) resultam em menos, mas altamente confiáveis, correspondências automáticas. Regras mais flexíveis aumentam a taxa de correspondência automática, mas elevam o risco de falsos positivos.
* **Tratamento de Exceções (Correspondência Manual):** Ao ativar regras para Correspondência Manual, o sistema oferece opções estruturadas para os usuários. Se uma transação falhar nos critérios de correspondência automática, ela se torna uma exceção. O usuário pode então tentar resolver a exceção aplicando uma regra manual pré-definida, que pode ter critérios relaxados (ex.: ignorar uma pequena discrepância de texto conforme a configuração "Ignorar na Correspondência Manual").

## O que mais influencia o resultado

* **Quando a correspondência é executada:** durante o processamento do documento, quando um usuário clica em **Auto PO Match**, e **a cada salvamento** em que o número do pedido de compra mudou ou nunca foi consultado antes (por exemplo, quando os dados mestres o preencheram após o processamento). Um salvamento nunca sobrescreve uma correspondência que já existe.
* **[Regras de transformação](../../transformation-rules.md)** são executadas antes da correspondência e podem alterar os itens da linha — e com eles as contagens de linhas que as condições de ativação observam. Uma regra de tabela que reconstrói as linhas mantém uma correspondência existente enquanto as linhas permanecerem as mesmas; se substituir linhas correspondidas, a correspondência é descartada e o nome da regra é mostrado como motivo.
* **[Calcular preço unitário do PO](calculate-po-unit-price.md)** altera qual preço unitário as regras comparam no lado do pedido de compra.
* **[Configurações de tolerância](purchase-order-tolerance-settings-additional-purchase-order-tolerance.md)** e **[status desativados](purchase-order-disable-statuses.md)** decidem quão rigorosa é a comparação e quais linhas do pedido de compra são oferecidas.

## Solução de Problemas

| Sintoma                                                        | O que verificar                                                                                                                                                                                   |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| "Sem correspondência" embora todos os valores concordem        | Abra o histórico de correspondência: qual regra foi executada, em qual coluna falhou (a variação é mostrada por coluna), a regra foi ignorada por uma condição de ativação?                        |
| Preço unitário subestimado exatamente pela taxa de imposto      | O total do pedido de compra inclui imposto; ative [Calcular preço unitário do PO](calculate-po-unit-price.md) (valor líquido primeiro) ou compare o valor líquido da linha.                         |
| Uma regra de correspondência no total nunca é executada         | Sua condição de ativação requer mais de uma linha no documento. Defina `[[count(table_lines)]] >= 1` ou não colapse as linhas com uma regra de transformação.                                      |
| O conjunto de regras não tem efeito algum                      | **PO match server side** está desligado para o tipo de documento, ou o conjunto de regras alterado ainda está em rascunho — ative a versão.                                                      |

***

## Personalizar as Regras de Correspondência de PO

Para editar as regras de Correspondência de PO, a versão padrão pode ser clonada clicando em **"Configurar Versionamento"** e usando a opção **"Clonar como Rascunho"** nas opções disponíveis do cartão

<figure><img src="../../../../../../.gitbook/assets/image (197).png" alt=""><figcaption></figcaption></figure>
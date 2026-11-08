# Diagnóstico de PO Matching

<!-- touchless-admin-video-v2-20261104:start -->
**Capítulo do vídeo (versão de revisão):** [Seguir um documento](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence-preview-admin/v2/pt.html#chapter=07).
<!-- touchless-admin-video-v2-20261104:end -->

## Visão geral

Muitas faturas param no pedido de compra. A fatura diz uma coisa, o pedido de compra (PO) diz outra e as verificações configuradas não conseguem resolver a diferença automaticamente. **Uma extração correta pode ainda assim levar a um PO match bloqueado quando os dados do sistema de origem divergem.** Uma paragem temporária ainda não é um resultado final: um processamento automático posterior pode ter sucesso, enquanto uma correção ou um reinício manual registado impede que um documento com sucesso seja touchless.

O Touchless Intelligence mostra-lhe **por que** um PO match falhou e **como** o DocBits tentou fazer o match. Esta página explica as duas etapas do pipeline envolvidas, os motivos que verá e o **fluxo de decisão do PO Matching**, um diagrama que mostra os passos do match um após o outro.

### Onde vê o PO Matching no Touchless Intelligence

| Onde                                                                                       | O que vê                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Where touchless is lost first** (separador de visão geral)                                | Uma barra como _PO line match: PO item mismatch_. Indica quantos documentos pararam ali                                                                                          |
| **Supplier opportunities**                                                                  | Um fornecedor com a causa raiz **PO matching**                                                                                                                                  |
| **Supplier Diagnosis**, secção **How this organisation matches** e o **cluster de problemas** | O fluxo de decisão com o conjunto de regras da sua organização                                                                                                                  |
| **Document Trace**                                                                          | A etapa **PO Line Match** com o estado **blocked** e o motivo                                                                                                                    |
| **Settings → Document Types → More Settings → Purchase Order**                              | As próprias regras de matching. Ver [Regras de matching de pedidos de compra](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) |

## As duas etapas de PO

| Etapa                  | Pergunta                                    | Para com                                                                                                              |
| ---------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| **9 · PO Lookup**      | Existe um pedido de compra para esta fatura? | _Purchase order not found_                                                                                           |
| **10 · PO Line Match** | Cada linha da fatura corresponde a uma linha do PO? | _PO item mismatch_, _PO line identifier mismatch_, _Unit price outside PO tolerance_, _Quantity outside PO tolerance_ |

Um documento que para na etapa 9 ou 10 aparece na fila de fornecedores com o primeiro bloqueio **PO matching**.

## Motivos pelos quais um PO match falha

| Motivo que vê                        | O que significa                                                                                             | Causa típica                                                                                              | O que alterar                                                                                                                                                        |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Purchase order not found**         | O DocBits não encontrou nenhum pedido de compra para o número de PO da fatura                               | O número de PO é lido errado ou está em falta; o PO ainda não foi importado; o PO pertence a outro fornecedor | Verifique a extração do número de PO deste fornecedor, a importação dos dados mestres de PO e a ligação ao fornecedor                                              |
| **PO item mismatch**                 | As linhas da fatura não corresponderam às linhas do PO                                                      | O fornecedor usa os seus próprios números de artigo; a descrição difere; linhas foram agregadas ou divididas | Verifique o mapeamento de números de artigo e as **rule priorities** nas regras de matching; acrescente uma regra para a forma como o fornecedor identifica as linhas |
| **PO line identifier mismatch**      | O número ou identificador da linha na fatura não corresponde ao PO                                          | O fornecedor renumera as linhas                                                                           | Faça o match por artigo e quantidade em vez de por número de linha                                                                                                    |
| **Unit price outside PO tolerance**  | O preço difere mais do que a tolerância permitida                                                           | Uma alteração de preço real, uma diferença de arredondamento ou uma unidade de preço diferente             | Verifique a **Unit price tolerance** no conjunto de regras; corrija o PO ou fale com o fornecedor                                                                     |
| **Quantity outside PO tolerance**    | A quantidade difere mais do que a tolerância permitida                                                      | Entrega parcial, entrega em excesso                                                                        | Verifique **Match quantity on** e a **Quantity tolerance**                                                                                                            |
| **PO matching service error**        | O serviço de matching não conseguiu responder                                                               | Um problema técnico temporário                                                                             | Reinicie os documentos; contacte o suporte se se repetir                                                                                                              |
| **Automatic PO export disabled**     | A configuração **Auto export if PO matched 100%** está desligada, por isso os documentos com match não são exportados automaticamente | A configuração está desligada                                                          | Ligue a configuração se pretender a exportação automática. Ver [Auto Export if PO Matched 100%](../../settings/document-processing/module/auto-export-if-po-matched-100.md) |

{% hint style="info" %}
Nem todos os motivos de PO matching podem ser corrigidos no DocBits. Se o fornecedor envia um número de PO errado, o cartão indica **Supplier action only**: o fornecedor tem de corrigir o documento e enviá-lo novamente.
{% endhint %}

Os casos separados de preço e quantidade e as respetivas evidências estão em [Exemplos resolvidos](touchless-examples.md).

## O fluxo de decisão do PO Matching

O fluxo de decisão mostra como o DocBits tenta fazer corresponder uma linha da fatura a uma linha do PO. Tem **cinco etapas** e o primeiro match vence:

1. **Single match validation**: aplica as regras por ordem de prioridade. É o caso normal, uma linha da fatura e uma linha do PO
2. **Multi match validation**: depois de um match único, quando estão envolvidas várias linhas de um dos lados
3. **Total match validation**: apenas quando nada correspondeu. O total da linha do PO é comparado com a soma das suas linhas de tabela
4. **Single mismatch validation**: o preço unitário é ignorado, de modo que uma linha pode ser correspondida por artigo e quantidade mesmo que o preço difira
5. **Fallback logic**: resta uma linha do PO e uma linha de tabela, por isso são emparelhadas

Dentro das etapas o DocBits tenta, por esta ordem:

* **Exact match for all rules**: todos os valores comparados são idênticos
* **Tolerance-based match**: os valores numéricos podem desviar-se dentro da tolerância
* **Package criteria**: a última passagem, com base nos critérios de embalagem do conjunto de regras

Cada passo pergunta **Match found?** A resposta **Yes** (verde) leva a **Match found** e o documento continua. A resposta **No match** (vermelho) passa ao passo seguinte e, depois do último passo, o resultado é **No match found**: o documento para e precisa de uma pessoa.

<figure><img src="https://raw.githubusercontent.com/FELLOWPRO/DocBits_Documentation/refs/heads/main/public_docs/.gitbook/assets/touchless-po-matching-flow.png" alt="O fluxo de decisão do PO matching: cabeçalho do conjunto de regras, cinco etapas de matching numeradas com as suas passagens e os pontos finais Match found e No match found"><figcaption><p>O fluxo de decisão do PO matching, aberto a partir de <strong>How this organisation matches</strong> na página Supplier Diagnosis. O cabeçalho mostra o conjunto de regras (versão 7, propriedade desta organização) e as tolerâncias. Abaixo, as cinco etapas com as suas passagens correm de cima para baixo. O verde leva a <strong>Match found</strong>, o vermelho passa ao passo seguinte e termina em <strong>No match found</strong>. Organização de exemplo com dados de demonstração.</p></figcaption></figure>

### O que o cabeçalho do diagrama lhe diz

| Campo                                             | Significado                                                                                            |
| ------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Document type**                                 | O tipo de documento a que o conjunto de regras pertence, por exemplo INVOICE                            |
| **Rule set version**                              | A versão das regras de matching, por exemplo v3                                                        |
| **Rule set owner**                                | **This organisation** (as suas próprias regras) ou **Shipped default rule set** (as regras padrão do DocBits) |
| **Published**                                     | Quando a versão foi publicada                                                                          |
| **Match quantity on**                             | Que quantidade é comparada (quantidade encomendada, quantidade em aberto)                              |
| **Tolerance amount**                              | Se as tolerâncias vêm dos atributos do tipo de documento ou do conjunto de regras                      |
| **Unit price tolerance** / **Quantity tolerance** | Quanto um preço ou uma quantidade pode desviar-se                                                      |
| **Default tolerance**                             | A tolerância para todos os outros valores numéricos                                                    |

No exemplo acima, as tolerâncias mostram **not configured** e **not in force: attribute decides**. Isso significa: o conjunto de regras não tem tolerância própria e a linha **Tolerance amount** indica que as tolerâncias vêm dos **document type attributes**. Uma tolerância só decide quando está em vigor. Leia esta linha primeiro quando uma diferença de preço ou quantidade bloqueia documentos: ela diz-lhe **onde** alterar a tolerância.

O estado do conjunto de regras é mostrado como nota: **Active version** (estas regras decidem), **Approved, not active**, **Draft, not yet in force** ou **Version state unknown**. Apenas a versão ativa decide.

Se as regras de transformação alteraram um documento antes do matching, o diagrama indica-o, por exemplo _2 aplicadas: (nomes)_ ou _"(regra)" reconstruiu (tabela): o PO match perdeu-se aqui_. É uma causa oculta frequente: uma regra que reformata uma tabela pode quebrar um match que antes funcionava.

## Exemplos

Os números dos exemplos são ilustrativos.

### Exemplo 1: Preço dentro da tolerância

Uma linha da fatura tem um preço unitário de **10.40**. A linha do PO indica **10.00**. A tolerância de preço unitário é **5 %**.

* O **Exact match** falha (10.40 não é 10.00).
* O **Tolerance-based match** tem sucesso: a diferença é **4 %**, dentro dos 5 %.
* A linha é correspondida. **Match found.**

Com uma tolerância de **3 %** o tolerance-based match também falha. Depois de todas as etapas o documento para com **Unit price outside PO tolerance**. O diagrama mostra exatamente este caminho e a correção é ou a tolerância (se 4 % for aceitável para o seu negócio) ou uma correção no fornecedor.

### Exemplo 2: Os números de artigo do fornecedor diferem dos seus

Um fornecedor fatura o artigo **"A-4711-X"**, o seu PO indica **"4711"**. Nenhuma regra compara os dois, por isso não é encontrado nenhum match e o Touchless Intelligence agrupa todas as faturas deste fornecedor num só cluster: **PO line match, PO item mismatch**, 27 documentos.

* No cluster lê _27 afetados, 27 recuperáveis_, com uma subida esperada de, por exemplo, **+8.7 pp**.
* A correção é do seu lado: acrescente ou reordene uma regra que faça o match pelo número de artigo do fornecedor ou pela descrição, ou mantenha os números de artigo do fornecedor nos dados mestres.
* Depois de alterar a regra, aplique a alteração com uma [change proposal](touchless-change-proposals.md) e leia o **Change history** duas semanas depois: taxa AP touchless antes e depois.

### Exemplo 3: O pedido de compra ainda não está lá

As faturas chegam antes de o PO ser importado. Param no **PO Lookup** com **Purchase order not found**. O cluster mostra um pico curto. A correção é a ordem dos seus processos, ou o agendamento da importação de PO, e não as regras de matching. Verifique **Where touchless is lost first**: uma barra _PO lookup: Purchase order not found_ que cresce depois de cada falha de importação aponta para esta causa.

### Exemplo 4: Uma regra reconstruiu a tabela

Depois de entrar em produção uma regra de transformação para a tabela de um fornecedor, a taxa de matching desse fornecedor caiu acentuadamente. O diagrama de um documento afetado indica _"(regra)" reconstruiu (tabela): o PO match perdeu-se aqui_. A correção é ajustar ou desfazer a regra de transformação, não as regras de matching.

## Uma rotina para problemas de PO matching

1. Abra **Where touchless is lost first**. Está alguma etapa de PO matching nos três primeiros lugares?
2. Abra **Supplier opportunities** e ordene por **Expected lift**. Pegue no fornecedor com a causa raiz **PO matching** e o estado **RECOVERABLE**.
3. Abra o **Supplier Diagnosis** e leia o cluster: motivo, documentos afetados, **What to change**, **Missing evidence**.
4. Abra **How this organisation matches** e verifique o conjunto de regras: versão, proprietário e tolerâncias.
5. Abra um **documento de exemplo** e o respetivo [Document Trace](touchless-document-trace.md): que etapa, que motivo?
6. Altere **uma** coisa (ordem das regras, tolerância, mapeamento de artigos) com pré-visualização, para que o **Change history** a possa medir.

## Páginas relacionadas

* [Touchless Intelligence](./)
* [Supplier Diagnosis e clusters de problemas](touchless-supplier-diagnosis.md)
* [Document Trace](touchless-document-trace.md)
* [Change Proposals e relatórios](touchless-change-proposals.md)
* [Regras de matching de pedidos de compra](../../settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md)
* [Cartões de PO Matching: guia completo](../../workflow/cards-overview/po-matching-complete-guide.md)

<!-- Documentation review 2026-11-04: extraction quality vs process outcomes; KPI and terminal-outcome definitions checked against DocBits_API c51f350c728acb8ac964098d15f7b006bce273f4, module/automation_intelligence/kpi.py and bucket.py. Existing native screenshots retained and checked separately from illustrative examples. -->

<!-- Completion review 2026-11-04: owned synthetic PO examples, MCP schema/read evidence, human-action classification, KPI labels and screenshot proof limits. -->

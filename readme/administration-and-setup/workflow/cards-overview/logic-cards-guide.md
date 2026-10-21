# Cartões lógicos: variáveis, conversões, JSON e gatilhos

<figure><img src="../../../.gitbook/assets/workflow-card-qa-20261021-category-e019409102f9-pt.png" alt="Cartões de conversão e JSON na biblioteca. Os cartões de variáveis da organização requerem Advanced Builder; os modelos visíveis também dependem da versão. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real."><figcaption><p>Cartões de conversão e JSON na biblioteca. Os cartões de variáveis da organização requerem Advanced Builder; os modelos visíveis também dependem da versão. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

Use esses cartões no Advanced Workflow Builder, onde o cartão selecionado está disponível. A visibilidade do cartão depende da sua versão e dos modelos habilitados. As referências abaixo descrevem a versão 2. Lembre-se da versão armazenada em um fluxo de trabalho existente ao comparar seus campos com este guia.

## Escolha a reserva de valor certa

Uma variável de fluxo de trabalho da organização selecionada no painel Variáveis é compartilhada entre fluxos de trabalho e salva independentemente da tela. Uma tag nomeada usada por cartões de conversão, JSON e comparação de tags pertence ao contexto de execução atual. Criar uma tag não cria uma variável de organização. Insira o nome da tag sem um prefixo de armazenamento interno. Um campo de documento é uma terceira fonte de dados separada.

Uma variável de organização e uma tag de execução permanecem separadas mesmo quando seus nomes correspondem. Selecione um campo variável compatível ou forneça explicitamente o valor que o cartão receptor espera. Consulte [Variáveis](../advanced-workflow/variables.md) para escopo da organização e persistência imediata.

## Ações variáveis da organização

Crie primeiro a variável com o tipo correto e selecione-a no cartão. Uma referência de variável ausente relata `MISSING_VARIABLE`. Os cartões que definem variáveis ​​registram o valor anterior e o novo no registro do cartão. Evite dados pessoais ou confidenciais reais em valores de teste e registros compartilhados.

| Cartão | Entrada obrigatória | Resultado e exemplo | Falha ou caso limite |
| --- | --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Variável de texto e `value` | Armazena texto; por exemplo, defina um rótulo de roteamento como `review`. | Um valor ausente é diferente de um valor de texto intencionalmente vazio. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Variável do tipo Número e numérico `value` | Armazena um número finito; por exemplo, defina um limite para `1000.50`. | Texto numérico inválido, infinito e NaN são rejeitados. Use um ponto decimal, sem símbolo de moeda. |
| `ACTION_LOGIC_CALC_NUMBER` | Variável numérica e `expression` | Armazena o resultado aritmético; `(100 + 20) / 2` dá `60`. | Suporta literais numéricos, parênteses, `+`, `-`, `*`, `/`, `%` e `**`. Nomes, chamadas de função e referências de campos de documentos não são aceitos na expressão. Expressões inválidas ou divisão por zero falham. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Variável Sim/Não e `value` | Define o sinalizador como Sim ou Não. | Use o valor booleano oferecido pelo cartão em vez de um sinônimo de texto livre traduzido. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Sim/Não variável | Reverte seu valor atual; Sim se torna Não. | Inicialize a variável antes de confiar em um primeiro resultado específico. |

### Ação de referência de documento

`ACTION_LOGIC_SET_DOCUMENT_VAR` armazena o ID do documento atual em uma variável de documento selecionada. Precisa de um documento atualizado; sem um, ele relata `NO_DOCUMENT`. Um fluxo de trabalho acionado recebe o ID do documento, não um objeto de documento serializado. A implementação verificada não possui modelo de cartão de UI propagado para esta ação, portanto, não espere que ele apareça em todos os seletores de cartão. Use-o somente se o seu administrador confirmar que um modelo correspondente está disponível; inserir um ID de documento no formulário de criação de variável não é um substituto.

## Tags e conversões de tipo

Essas ações usam nomes de tags no contexto de execução atual. Produza a tag de entrada antes de lê-la. Uma tag de entrada ausente ou um nome ausente relata `MISSING_VARIABLE`; uma conversão numérica inválida informa um erro de configuração. A saída é uma tag nova ou substituída, não um campo de documento extraído.

| Cartão | Entradas | Saída e exemplo |
| --- | --- | --- |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | `tag_name`, `value` | Cria uma tag de texto; `raw_amount` com valor `125.50`. Um valor de texto vazio é permitido. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | `input_tag`, `output_tag` | Converte `125.50` no número `125.5`. Um booleano torna-se `1` ou `0`. Texto como `EUR 125,50` não é uma entrada numérica válida. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | `input_tag`, `output_tag` | Converte o valor armazenado em texto. Ele não formata uma moeda nem localiza separadores decimais. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | `input_tag`, `output_tag` | Converte um booleano existente diretamente; um número diferente de zero torna-se verdadeiro e zero torna-se falso. Use `true` ou `false` para entrada de texto previsível e teste outras representações aceitas. |

### Exemplo de conversão

1. Crie a tag de texto `raw_amount` com valor `125.50`.
2. Converta `raw_amount` em número, escrevendo em `amount_number`.
3. Use um número maior que com `tag_name` definido como `amount_number` e `value` definido como `100`.
4. Verifique se a condição foi bem-sucedida para `125.50`, falhou para `100` e relatou um erro de conversão para `EUR 125,50` na etapa 2.

## Ler valores do JSON

Todos os três cartões lidos levam `json_text`, `json_path` e `output_tag`. Apesar do nome, `json_text` é o nome de uma tag contendo JSON, não uma caixa para colar um documento JSON literal. Produza essa tag primeiro, por exemplo, com Criar tag de texto.

Os caminhos são chaves separadas por pontos e índices de lista baseados em zero: `invoice.lines.0.amount`. Não use sintaxe JSONPath como `$.invoice.lines[0].amount`. Se uma chave estiver faltando, um índice for inválido ou JSON for inválido, o resultado será `ERROR_CARD_SETUP`; uma tag de origem ausente relata `MISSING_VARIABLE`.

| Cartão | Saída |
| --- | --- |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Valor numérico; o texto numérico é convertido e um booleano se torna `1` ou `0`. O texto numérico inválido falha. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Representação de texto do valor selecionado. Esta não é uma promessa de serialização JSON para objetos aninhados. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Um booleano; o texto `true`, `1` ou `yes` é verdadeiro após letras minúsculas, enquanto outro texto é falso. Os números seguem seu valor zero/diferente de zero. |

Para uma tag `payload` contendo o seguinte JSON, ler `invoice.lines.0.amount` em `amount` com JSON para numerar produz `125.5`:

```json
{"invoice":{"lines":[{"amount":"125.50"}],"approved":false}}
```

Teste também um caminho inexistente, um índice fora do intervalo e JSON malformado. Uma leitura com falha não deve ser tratada como um zero válido ou uma aprovação bem-sucedida.

## Atualizar JSON

Os quatro cartões de gravação recebem `json_tag`, `json_path` e `value`. `json_tag` nomeia uma tag existente contendo JSON. Eles atualizam essa tag com JSON serializado. A mesma sintaxe de caminho separado por pontos se aplica; chaves de objetos intermediários ausentes podem ser criadas, mas os índices de lista devem identificar os elementos existentes. Eles não estendem uma lista nem suportam caminhos curinga.

| Cartão | Valor e efeito |
| --- | --- |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Um valor numérico, como `125.5`; armazena um número JSON. O texto numérico inválido falha. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Texto, como `review`; armazena uma string JSON. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | O texto `true`, `1` ou `yes` é definido como verdadeiro após letras minúsculas; outro texto define falso. Prefira `true` e `false`. |
| `ACTION_LOGIC_JSON_SET_JSON` | JSON válido, como `{"status":"review"}`; insere esse valor analisado, não o texto citado. JSON inválido falha. |

Por exemplo, defina o caminho `invoice.approved` para `true` em `payload` com JSON definido como booleano. Em seguida, leia o mesmo caminho com JSON para Boolean e verifique se é verdade. Uma tag de origem ausente, JSON inválido ou caminho inválido devem ser diagnosticados no log do cartão antes de continuar.

## Condições

Todas as seis condições abaixo são da versão 2. Uma condição falsa é um resultado comercial, não uma ação bem-sucedida ou um erro de execução. Em uma sequência de condições de estilo padrão, evita as seguintes ações; em um fluxo de trabalho avançado, conecte o resultado à ramificação pretendida.

| Cartão | Campos | Avaliação e limite importante |
| --- | --- | --- |
| `CONDITION_LOGIC_VALUE_EQUALS` | `tag_name`, `value` | Compara exatamente as representações de texto, incluindo maiúsculas e minúsculas. Não use isso como uma verificação de presença: uma tag ausente não é automaticamente relatada como um erro. |
| `CONDITION_LOGIC_BOOLEAN_IS` | `tag_name` | Verifica se a tag é verdadeira. Uma tag ausente é avaliada como falsa. Use um booleano real para obter resultados confiáveis. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | `tag_name`, `value` | Pesquisa de substring com distinção entre maiúsculas e minúsculas. Uma tag ausente é tratada como texto vazio. Uma string de pesquisa vazia corresponde; sempre defina o valor de pesquisa deliberadamente. |
| `CONDITION_LOGIC_NUMBER_LESS` | `tag_name`, numérico `value` | Estritamente menos que. Uma tag ausente ou um valor de comparação omitido é padronizado como zero; dados numéricos inválidos são um erro de configuração. |
| `CONDITION_LOGIC_NUMBER_GREATER` | `tag_name`, numérico `value` | Estritamente maior que. Um valor igual ao limite não satisfaz esta condição. Os mesmos padrões de zero e comportamento de erro numérico se aplicam. |
| `CONDITION_LOGIC_EXPRESSION` | `value1`, `operator`, `value2` | Suporta `==`, `!=`, `<`, `<=`, `>`, `>=`, `contains`, `not_contains`. Ele primeiro tenta a comparação numérica e, caso contrário, compara o texto. Não é um campo arbitrário de expressão Python. |

Para Número maior que `100`, teste `99`, `100` e `101`. Para Texto contém `ABC`, teste `ABC`, `abc` e uma pesquisa vazia. Verifique a ramificação e o log; um nó cinza foi ignorado e não prova nenhuma comparação bem-sucedida.

## Gatilhos

| Cartão | Configuração | Quando combina |
| --- | --- | --- |
| `CONDITION_LOGIC_VAR_CHANGED` | Selecione uma variável de organização. A referência armazenada usa seu ID, portanto, renomear a variável não altera intencionalmente o destino. | Os valores das variáveis atuais e anteriores fornecidos são diferentes. Repetir o mesmo valor não é uma mudança. Uma referência de variável ausente relata `MISSING_VARIABLE`. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Opcional `event_name`. | Uma carga de webhook está presente no contexto de execução do fluxo de trabalho. Com um nome, o valor `event` da carga útil deve corresponder exatamente; sem um nome, qualquer evento de webhook fornecido corresponde. Nenhum evento significa falso. |

Selecionar o evento Webhook não cria um endpoint público de webhook ou sua autenticação. Sua integração deve fornecer o evento através de um ponto de entrada configurado. Teste o evento correspondente, outro evento e nenhum evento. Para um gatilho de variável, teste uma mudança de valor real e um valor inalterado e evite uma cadeia que reescreva repetidamente a mesma variável compartilhada.

## Testar e diagnosticar

Valide o gráfico, teste cada ramificação com entrada representativa e inspecione [Logs de fluxo de trabalho](../workflow-logs.md). Inclui tags ausentes, JSON inválido, tipos de variáveis ​​errados, limites numéricos e condições falsas. Um teste sem documento não pode provar uma ação dependente de documento. Verifique novamente a versão salva do cartão e o estado ativado antes de confiar na execução automática.

<!-- workflow-card-logic-examples-20261021 -->

## Exemplos resolvidos para cada placa lógica

Estas são entradas ilustrativas e resultados esperados para a versão 2. Use cartões de variáveis de organização apenas onde o Advanced Builder expõe seus modelos.

| Cartão | Configuração de exemplo | Resultado esperado e contra-exemplo |
| --- | --- | --- |
| `ACTION_LOGIC_SET_TEXT_VAR` | Defina a variável de texto da organização `routing_label` como `review`. | A variável compartilhada contém `review`. Um fluxo de trabalho posterior pode ler a mesma variável de organização. |
| `ACTION_LOGIC_SET_NUMBER_VAR` | Defina a variável numérica `approval_limit` como `1000.50`. | Ele armazena o número `1000.5`. O texto `EUR 1000,50` não é uma entrada numérica válida. |
| `ACTION_LOGIC_CALC_NUMBER` | Armazene a expressão `(100 + 20) / 2` na variável numérica `calculated_limit`. | O resultado é `60`. Um nome de campo de documento ou divisão por zero não é um substituto válido. |
| `ACTION_LOGIC_SET_BOOLEAN_VAR` | Defina a variável Sim/Não `review_required` para o booleano `true` oferecido. | A bandeira da organização é verdadeira. Use o booleano `false` em um caso separado para limpá-lo. |
| `ACTION_LOGIC_INVERT_BOOLEAN` | Comece com a variável de organização `demo_flag` igual a `true`. | Uma execução torna `false`. Executar novamente torna `true`, portanto a execução repetida não é idempotente. |
| `ACTION_LOGIC_CREATE_TEXT_TAG` | Crie a tag de execução `raw_amount` com o texto `125.50`. | A tag contém esse texto nesta execução; não é uma nova variável de organização ou campo de documento. |
| `ACTION_LOGIC_CONVERT_TO_NUMBER` | Converta a tag de entrada `raw_amount`, contendo `125.50`, na tag de saída `amount_number`. | A saída é numérica `125.5`. `EUR 125,50` produz um erro de conversão. |
| `ACTION_LOGIC_CONVERT_TO_TEXT` | Converta a tag numérica `amount_number` contendo `125.5` em `amount_text`. | A saída é o texto `125.5`; não está localizado como um valor monetário. |
| `ACTION_LOGIC_CONVERT_TO_BOOLEAN` | Converta uma tag de entrada numérica contendo `1` na tag de saída `has_value`. | A saída é verdadeira. O numérico `0` produz falso. |
| `ACTION_LOGIC_JSON_TO_NUMBER` | Crie a tag de origem `payload` com `{"invoice":{"amount":"125.50"}}`; leia o caminho `invoice.amount` para `amount_number`. | A saída é numérica `125.5`. Um caminho ausente é um erro, não um zero válido. |
| `ACTION_LOGIC_JSON_TO_TEXT` | Use a tag de origem `payload` contendo `{"invoice":{"status":"review"}}` e caminho `invoice.status`. | A tag de saída contém o texto `review`. |
| `ACTION_LOGIC_JSON_TO_BOOLEAN` | Use a tag de origem `payload` contendo `{"invoice":{"approved":false}}` e caminho `invoice.approved`. | A saída é booleana falsa. Um caminho ausente não é o mesmo que um falso armazenado. |
| `ACTION_LOGIC_JSON_SET_NUMBER` | Use a tag JSON existente `payload` contendo `{"invoice":{}}`; defina `invoice.total` para `125.5`. | A tag contém um total numérico JSON, não uma string numérica entre aspas. |
| `ACTION_LOGIC_JSON_SET_TEXT` | Use a tag JSON existente `payload` contendo `{"invoice":{}}`; defina `invoice.status` para `review`. | O valor JSON armazenado é uma string: `{"invoice":{"status":"review"}}`. |
| `ACTION_LOGIC_JSON_SET_BOOLEAN` | Use a tag JSON existente `payload` contendo `{"invoice":{}}`; defina `invoice.approved` com o texto `true`. | O valor JSON armazenado é booleano verdadeiro. Use `false` para limpá-lo. |
| `ACTION_LOGIC_JSON_SET_JSON` | Use a tag JSON existente `payload` contendo `{"invoice":{}}`; defina `invoice.metadata` como JSON válido `{"source":"demo"}`. | O valor inserido é um objeto. JSON inválido deve ser relatado e não armazenado como uma atualização de objeto bem-sucedida. |
| `CONDITION_LOGIC_VALUE_EQUALS` | Crie a tag `route` com o texto `review` e compare-a com `review`. | Isso passa. A comparação com `Review` falha porque a comparação diferencia maiúsculas de minúsculas. |
| `CONDITION_LOGIC_BOOLEAN_IS` | Use a tag `review_required` contendo o booleano real `true`. | Isso passa; false ou uma tag ausente não estabelece um resultado verdadeiro. |
| `CONDITION_LOGIC_TEXT_CONTAINS` | Use a tag `note` com o texto `manual review` e pesquise `review`. | Isso passa. A pesquisa por `REVIEW` maiúsculo falha. Uma string de pesquisa vazia corresponde e deve ser evitada, a menos que seja intencional. |
| `CONDITION_LOGIC_NUMBER_LESS` | Use tag numérica `amount` igual a `50` e valor de comparação `100`. | Isso passa. Um valor de `100` falha na comparação estrita de menor que. |
| `CONDITION_LOGIC_NUMBER_GREATER` | Use tag numérica `amount` igual a `125` e valor de comparação `100`. | Isso passa. `100` falha na comparação estrita maior que. |
| `CONDITION_LOGIC_EXPRESSION` | Selecione valor1 `120`, operador `>` e valor2 `100`. | A comparação numérica é aprovada. Use `80` como valor1 para uma ramificação falsa; esta não é uma expressão Python de formato livre. |
| `CONDITION_LOGIC_VAR_CHANGED` | Selecione uma variável de organização cujo valor anterior seja `new` e o valor atual fornecido seja `review`. | O evento de valor alterado corresponde. Repetir `review` porque o valor anterior e o atual não correspondem. |
| `CONDITION_LOGIC_WEBHOOK_EVENT` | Selecione o nome do evento `invoice.ready` e forneça um evento de integração configurado com carga útil `{"event":"invoice.ready"}`. | Combina. `{"event":"invoice.updated"}` e nenhum evento não correspondem. O cartão não cria um endpoint de webhook. |

A ação opcional de referência de documento `ACTION_LOGIC_SET_DOCUMENT_VAR` não possui modelo propagado na fonte verificada. Se o seu administrador fornecer um modelo compatível, selecione uma variável Document e execute com um documento de demonstração atual: ele armazena esse ID do documento. Sem documento reporta `NO_DOCUMENT`. Não o trate como um cartão disponível apenas porque a implementação existe.

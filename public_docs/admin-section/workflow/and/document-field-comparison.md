# Comparação de Campos de Documentos

<figure><img src="../../../.gitbook/assets/userlmn_7d5c06ce63181faee30b7bc6903e4d7b.png" alt=""><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho é projetado para comparar automaticamente os valores de dois campos especificados dentro de um documento com base em um operador definido. É usado para garantir a integridade dos dados e garantir que os dados do documento estejam em conformidade com regras ou condições comerciais.

**Componentes do Cartão**

1. **Nomes dos Campos**
* **Descrição**: Especifica os nomes dos dois campos dentro do documento que serão comparados.
* **Detalhe**: Os usuários devem inserir os nomes exatos dos campos conforme aparecem no sistema. Esses campos podem ser de qualquer tipo de dados que suporta comparação, como campos numéricos, de data ou de texto.
2. **Operador**
* **Descrição**: O operador de comparação usado para avaliar a relação entre os valores dos dois campos.
* **Opções**:
* **Igual (==)**: Verifica se o valor do primeiro campo é igual ao valor do segundo campo.
* **Diferente (!=)**: Verifica se o valor do primeiro campo não é igual ao valor do segundo campo.
* **Maior Que (>)**: Verifica se o valor do primeiro campo é maior que o valor do segundo campo.
* **Maior Que ou Igual (>=)**: Verifica se o valor do primeiro campo é maior ou igual ao valor do segundo campo.
* **Menor Que (<)**: Verifica se o valor do primeiro campo é menor que o valor do segundo campo.
* **Menor Que ou Igual (<=)**: Verifica se o valor do primeiro campo é menor ou igual ao valor do segundo campo.

**Funcionalidade**

* **Seleção de Campo**: Os usuários inserem ou selecionam os nomes dos dois campos a serem comparados. Isso é geralmente feito por meio de um formulário ou de um menu suspenso na configuração do cartão.
* **Seleção de Operador**: Os usuários escolhem um operador em uma lista de opções disponíveis que definem como os campos devem ser comparados.
* **Execução da Comparação**:
* O sistema lê os valores dos campos especificados e aplica o operador selecionado para avaliar a relação entre eles.
* Com base no resultado da comparação (verdadeiro ou falso), ações subsequentes podem ser acionadas. Por exemplo, se uma comparação falhar, o sistema pode sinalizar o documento para revisão, bloquear o processamento adicional ou notificar as partes responsáveis.

**Interações do Usuário**

* **Configuração e Configuração**: Os usuários configuram a comparação inserindo os nomes dos campos e selecionando um operador. Essa configuração deve ser direta e orientada, possivelmente com texto de ajuda ou exemplos.
* **Monitoramento e Relatórios**: O sistema pode fornecer feedback sobre os resultados das comparações, como registrar todas as comparações feitas, seus resultados e quaisquer ações tomadas em resposta aos resultados da comparação.
* **Tratamento de Erros e Notificações**: Os usuários recebem alertas se a comparação não puder ser executada (por exemplo, se um dos campos não for encontrado no documento ou não estiver em um formato comparável).

#### Conclusão

O cartão de fluxo de trabalho "Comparação de Campos de Documentos" é vital para manter a precisão e consistência dos dados em documentos em um sistema ERP. Ele ajuda a automatizar verificações que, de outra forma, seriam manuais, propensas a erros e demoradas, melhorando a eficiência e confiabilidade no processamento de documentos. Documentar claramente este cartão no manual do seu sistema ERP ajudará os usuários a empregar efetivamente esse recurso, garantindo que os dados em documentos permaneçam consistentes e em conformidade com as regras comerciais.

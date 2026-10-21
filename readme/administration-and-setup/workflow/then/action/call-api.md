# Chamar API

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-6a1c780ee588-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados.</p></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"Call API"** permite aos utilizadores fazer pedidos HTTP a endpoints de API especificados diretamente a partir do fluxo de trabalho. Este cartão suporta vários métodos HTTP e possibilita uma interação dinâmica com sistemas externos através do envio de parâmetros e dados. Simplifica a integração com serviços de terceiros e APIs personalizadas, assegurando uma comunicação transparente.

## Componentes do cartão:

1. **Ponto final da API**
   * **Descrição:** O endpoint de destino da **DocBits API** com o qual este cartão irá interagir.
   * **Detalhe:** Um campo de texto onde os utilizadores especificam o endpoint para o pedido de API.
2. **Método HTTP**
   * **Descrição:** O tipo de pedido HTTP a efetuar.
   * **Opções:**
     1. **GET:** Obtém dados do endpoint especificado.
     2. **POST:** Envia dados para o endpoint.
     3. **PUT:** Atualiza dados existentes no endpoint.
     4. **DELETE:** Remove dados no endpoint.
3. **Parâmetros**
   * **Descrição:** Parâmetros de consulta a incluir no pedido de API.
   * **Detalhe:** Um campo de texto ou lista para introduzir pares chave-valor para o URL do pedido.
4. **Dados**
   1. **Descrição:** O payload a enviar no corpo do pedido de API (aplicável aos métodos POST e PUT).
   2. **Detalhe:** Um campo para introduzir os dados em JSON.

## Funcionalidade:

**Avaliação da condição:** O sistema avalia as condições definidas nas secções "Where" e "And Sections":

* Se ambas as condições forem **verdadeiras**, o pedido de API é executado conforme configurado.
* Se alguma das condições for **falsa**, o cartão não é executado e não é feita qualquer chamada de API.

**Execução do pedido de API:**

* O cartão envia o pedido HTTP ao endpoint especificado utilizando o método selecionado.
* Quaisquer parâmetros fornecidos são acrescentados ao URL e os dados são incluídos no corpo do pedido (se aplicável).

## Configuração:

1. **Defina o endpoint da API:**\
   Introduza o URL da API que pretende chamar.
2. **Selecionar o HTTP Method:**\
   Escolha um dos métodos suportados (GET, POST, PUT, DELETE) consoante os requisitos da sua API.
3. **Fornecer parâmetros:**\
   Adicione quaisquer parâmetros de consulta necessários como pares chave-valor.
4. **Incluir dados (se aplicável):**\
   Para os métodos POST ou PUT, especifique os dados a enviar no corpo do pedido.
5. **Configuração das condições:**\
   Configure as secções "Where" e "And Sections" para definir quando a chamada de API deve ocorrer.

## Conclusão:

O cartão de fluxo de trabalho **"Call API"** melhora a automação do fluxo de trabalho ao permitir a interação direta com sistemas externos. Ao oferecer configurações flexíveis para endpoints, métodos e dados, assegura que os fluxos de trabalho se podem integrar de forma transparente com APIs de terceiros ou backends personalizados. A capacidade de executar chamadas de API de forma condicional assegura precisão e eficiência na automação das comunicações externas.

***

<!-- workflow-card-practical-example-20261021 -->

## Exemplo prático

**Quando usar:** Solicite validação complementar a um serviço externo configurado.

**Configuração:** Selecione o endpoint da API de demonstração configurado e o método HTTP. Forneça os parâmetros e o corpo JSON exigidos por esse endpoint.

**Resultado esperado e contra-exemplo:** Para uma resposta simulada `200`, verifique o tratamento da resposta esperado pelos seguintes cartões. Teste também `500`; iniciar a chamada não estabelece que a verificação comercial foi bem-sucedida.

Esta é uma configuração ilustrativa e resultado esperado. Utilize campos, usuários e grupos configurados em sua organização de teste; não é uma afirmação de que este exemplo foi executado.

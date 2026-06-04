# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"Call API"** permite aos utilizadores fazer pedidos HTTP a endpoints de API especificados diretamente a partir do fluxo de trabalho. Este cartão suporta vários métodos HTTP e possibilita uma interação dinâmica com sistemas externos através do envio de parâmetros e dados. Simplifica a integração com serviços de terceiros e APIs personalizadas, assegurando uma comunicação transparente.

## Componentes do cartão:

1. **API Endpoint**
   * **Descrição:** O endpoint de destino da **DocBits API** com o qual este cartão irá interagir.
   * **Detalhe:** Um campo de texto onde os utilizadores especificam o endpoint para o pedido de API.
2. **HTTP Method**
   * **Descrição:** O tipo de pedido HTTP a efetuar.
   * **Opções:**
     1. **GET:** Obtém dados do endpoint especificado.
     2. **POST:** Envia dados para o endpoint.
     3. **PUT:** Atualiza dados existentes no endpoint.
     4. **DELETE:** Remove dados no endpoint.
3. **Parameters**
   * **Descrição:** Parâmetros de consulta a incluir no pedido de API.
   * **Detalhe:** Um campo de texto ou lista para introduzir pares chave-valor para o URL do pedido.
4. **Data**
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

1. **Definir o API Endpoint:**\
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

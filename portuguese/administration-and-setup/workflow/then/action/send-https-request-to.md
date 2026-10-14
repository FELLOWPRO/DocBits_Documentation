# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

O cartão de fluxo de trabalho **"Send HTTPS Request"** permite aos utilizadores enviar pedidos HTTPS para um URL especificado com cabeçalhos, parâmetros e payload de dados personalizáveis. Este cartão é ideal para integrar APIs externas ou serviços web diretamente no fluxo de trabalho.

## Componentes do cartão:

1. **URL**
   * **Descrição:** Especifica o endpoint para onde o pedido HTTPS será enviado.
   * **Detalhe:** Introduza o URL completo da API ou serviço web a que se pretende ligar.
2. **Headers**
   * **Descrição:** Define os cabeçalhos a incluir no pedido HTTPS.
   * **Detalhe:** Forneça **pares chave-valor** num **formato JSON válido** para especificar cabeçalhos como tokens de autenticação ou tipos de conteúdo. Exemplo: {"Authorization": "Bearer example\_value"}
3. **Method**
   * **Descrição:** Especifica o método HTTP a utilizar no pedido.
   * **Opções:**
     * **GET:** Obtém dados do endpoint.
     * **POST:** Envia dados ao endpoint para criar ou atualizar recursos.
     * **PUT:** Atualiza recursos existentes no endpoint.
     * **DELETE:** Remove recursos do endpoint.
4. **Parameters**
   * **Descrição:** Pares chave-valor a incluir no URL como parâmetros de consulta.
   * **Detalhe:** Utilize isto para enviar filtros ou dados adicionais exigidos pelo endpoint num formato JSON válido. Veja o exemplo dos Headers.
5. **Data**
   * **Descrição:** O corpo do pedido HTTPS.
   * **Detalhe:** Forneça o payload num formato JSON válido. Veja o exemplo dos Headers.

## Funcionalidade:

* **Avaliação da condição:** O cartão só envia o pedido HTTPS se as secções **"Where"** e **"And Sections"** forem avaliadas como verdadeiras.&#x20;
  * Se alguma das condições for falsa, o pedido não é enviado.
* **Execução do pedido:**
  * Quando as condições são cumpridas, o sistema envia o pedido HTTPS com as configurações especificadas.

## Configuração:

1. **Definir o URL:** Introduza o endpoint para onde o pedido HTTPS deve ser enviado.
2. **Definir os Headers:** Forneça os cabeçalhos necessários como pares chave-valor.
3. **Selecionar o HTTP Method:** Escolha o método adequado (**GET**, **POST**, **PUT** ou **DELETE**) consoante a ação a realizar.
4. **Adicionar parâmetros:** Especifique quaisquer parâmetros de consulta exigidos pelo endpoint.
5. **Fornecer o payload de dados:** Introduza o corpo do pedido no formato exigido (por exemplo, JSON) se necessário.
6. **Configurar condições:** Defina as secções **"Where"** e **"And Sections"** para assegurar que o pedido só é enviado quando determinadas condições são cumpridas.

## Exemplo de cartão:

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Conclusão:

O cartão de fluxo de trabalho **"Send HTTPS Request"** simplifica a integração de APIs ao permitir aos utilizadores fazer pedidos personalizados a serviços externos diretamente a partir dos seus fluxos de trabalho. Ao automatizar o processo de envio de pedidos HTTPS e a gestão de respostas, este cartão melhora a flexibilidade e a funcionalidade do fluxo de trabalho.

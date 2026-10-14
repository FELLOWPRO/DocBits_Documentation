# Send HTTPS Request

<figure><img src="../../../../.gitbook/assets/image (4) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão DocBits foi concebido para facilitar a interação com sistemas externos ao enviar pedidos HTTPS para URLs especificados. Permite que os fluxos de trabalho realizem ações como obtenção, atualização ou eliminação de dados através de chamadas de API, assegurando uma integração transparente com serviços externos.

## **Funcionalidade:**

* **Execução de pedidos HTTPS:** O cartão envia um pedido a um URL especificado utilizando o método HTTP configurado (por exemplo, GET, POST, PUT, DELETE).
* **Cabeçalhos e parâmetros:** Os utilizadores podem incluir cabeçalhos personalizados e parâmetros de consulta para assegurar que o pedido cumpre os requisitos da API externa.
* **Dados do pedido:** Permite aos utilizadores definir o payload de dados (se aplicável) a enviar com o pedido, como dados JSON ou codificados em formulário.
* **Avaliação da resposta:** O fluxo de trabalho verifica se o código de estado recebido corresponde ao valor esperado, assegurando uma comunicação bem-sucedida antes de prosseguir.
* **Métodos HTTP suportados:**
  * GET: Obtém dados do URL especificado.
  * POST: Submete dados ao URL especificado para criar recursos.
  * PUT: Atualiza recursos existentes no URL especificado.
  * DELETE: Remove recursos do URL especificado.

## **Utilização:**

Este cartão é particularmente útil em cenários onde os fluxos de trabalho precisam de interagir com APIs externas para troca de dados, como enviar atualizações para um CRM, obter estados de encomendas ou publicar novas entradas numa base de dados.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para enviar um pedido POST a um sistema externo de gestão de encomendas com um payload que contém os detalhes de uma nova encomenda. São adicionados cabeçalhos personalizados para incluir tokens de autenticação da API. O cartão está configurado para continuar apenas se o código de estado da resposta for 201 (Created). Se o código de estado for diferente, o fluxo de trabalho aciona uma notificação de erro para intervenção manual.

Ao utilizar o cartão "Send HTTPS Request", as organizações podem automatizar integrações externas, melhorar a comunicação entre sistemas e simplificar fluxos de trabalho complexos.

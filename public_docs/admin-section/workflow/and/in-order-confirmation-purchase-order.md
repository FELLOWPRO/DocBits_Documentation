# Confirmação do Pedido de Compra em Ordem

### Comparar com Pedido de Compra:&#x20;

**Confirmação do Pedido de Compra em Ordem**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Cartão Lógico: Quantidade ou Preço Unitário ou Correspondência de Desconto

Este cartão lógico é projetado para verificar automaticamente se a quantidade, preço unitário ou desconto detalhados em uma confirmação de pedido correspondem às cifras correspondentes no pedido de compra. Essa verificação garante consistência e precisão entre o que foi pedido e o que o fornecedor confirma em entregar.

#### Condição de Acionamento

A lógica é ativada quando qualquer uma das seguintes condições é atendida em uma confirmação de pedido em relação ao pedido de compra original:

* **Quantidade**: A quantidade de itens pedidos corresponde à quantidade confirmada pelo fornecedor.
* **Preço Unitário**: O preço por item acordado corresponde à confirmação do fornecedor.
* **Desconto**: Quaisquer descontos aplicados são consistentes entre o pedido de compra e a confirmação do pedido.

#### Resultados

* **Igual**: Se a quantidade, preço unitário ou desconto da confirmação do pedido corresponder exatamente ao pedido de compra, o sistema considera a confirmação como válida e prossegue com as próximas etapas no processo de aquisição.
* **Não Igual**: Se houver uma discrepância na quantidade, preço unitário ou desconto, o sistema sinaliza a confirmação do pedido para revisão manual. Isso garante que quaisquer divergências sejam resolvidas antes de avançar.

#### Benefícios

* **Precisão e Consistência**: Mantém a precisão no processo de aquisição, garantindo que os pagamentos e entregas sejam feitos com base em cifras corretas.
* **Eficiência**: Automatiza o processo de verificação, reduzindo a necessidade de verificações manuais e acelerando o processamento de pedidos.
* **Controle de Custos**: Ajuda a evitar pagamentos em excesso ou entregas incorretas ao detectar discrepâncias no início do processo.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definir Parâmetros de Comparação**: Configure os campos específicos (quantidade, preço unitário, desconto) que o cartão lógico verificará para uma correspondência.
2. **Automatizar Verificação**: Configure o sistema para comparar automaticamente esses detalhes ao receber uma confirmação de pedido.
3. **Personalizar Alertas**: Decida sobre o fluxo de trabalho para lidar com discrepâncias, incluindo a personalização de alertas para revisão manual.

Este cartão lógico é vital para garantir que os detalhes de uma confirmação de pedido estejam alinhados com o pedido de compra original, protegendo a integridade do ciclo de aquisição. \`\`

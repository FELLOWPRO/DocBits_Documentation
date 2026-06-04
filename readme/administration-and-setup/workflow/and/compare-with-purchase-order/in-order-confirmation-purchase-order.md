---
hidden: true
---

# In Order Confirmation Purchase Order

### Compare with Purchase Order:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Cartão Logic: Correspondência de Quantidade, Preço Unitário ou Desconto

Este cartão de lógica foi concebido para verificar automaticamente que a quantidade, o preço unitário ou o desconto detalhados numa confirmação de encomenda correspondem aos valores correspondentes na ordem de compra. Esta verificação assegura consistência e precisão entre o que foi encomendado e o que o fornecedor confirma entregar.

#### Condição de acionamento

A lógica é ativada quando alguma das seguintes condições é cumprida numa confirmação de encomenda relativamente à ordem de compra original:

* **Quantity**: A quantidade de itens encomendados corresponde à quantidade confirmada pelo fornecedor.
* **Unit Price**: O preço por item acordado corresponde à confirmação do fornecedor.
* **Discount**: Quaisquer descontos aplicados são consistentes entre a ordem de compra e a confirmação de encomenda.

#### Resultados

* **Equals**: Se a quantidade, o preço unitário ou o desconto da confirmação de encomenda corresponderem exatamente à ordem de compra, o sistema considera a confirmação válida e prossegue com os passos seguintes do processo de compras.
* **Not Equal**: Se houver uma discrepância na quantidade, no preço unitário ou no desconto, o sistema assinala a confirmação de encomenda para revisão manual. Isto garante que quaisquer divergências são resolvidas antes de prosseguir.

#### Benefícios

* **Precisão e consistência**: Mantém a precisão no processo de compras, assegurando que os pagamentos e as entregas são feitos com base em valores corretos.
* **Eficiência**: Automatiza o processo de verificação, reduzindo a necessidade de verificações manuais e acelerando o processamento de encomendas.
* **Controlo de custos**: Ajuda a prevenir pagamentos em excesso ou entregas incorretas ao detetar discrepâncias no início do processo.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Definir parâmetros de comparação**: Configure os campos específicos (quantidade, preço unitário, desconto) que o cartão de lógica irá verificar quanto a correspondência.
2. **Automatizar a verificação**: Configure o sistema para comparar automaticamente estes detalhes aquando da receção de uma confirmação de encomenda.
3. **Personalizar alertas**: Decida o fluxo de trabalho para o tratamento de discrepâncias, incluindo a personalização de alertas para revisão manual.

Este cartão de lógica é vital para garantir que os detalhes de uma confirmação de encomenda estão alinhados com a ordem de compra original, salvaguardando a integridade do ciclo de compras. \`\`

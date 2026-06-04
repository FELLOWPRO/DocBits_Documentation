# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Propósito:

Este cartão DocBits foi concebido para comparar um campo específico de dados de encomenda — como quantidade, desconto ou preço unitário — entre uma confirmação de encomenda e uma ordem de compra. Ao permitir uma comparação focada de um campo de cada vez, assegura precisão na validação de pontos de dados essenciais, mantendo a exatidão da encomenda. A **Versão 4** amplia esta funcionalidade ao permitir comparações entre diferentes entidades, como a ordem de compra, as quantidades recebidas e o próprio documento, acrescentando mais flexibilidade e controlo ao fluxo de trabalho.

## Componentes do cartão:

1. **Any/All**&#x20;
   * **Descrição:** Determina se a condição se aplica a alguma ou a todas as linhas da confirmação de encomenda.\
     **Opções:**
     * **Any**: A comparação será acionada se o valor do campo selecionado em alguma linha da confirmação de encomenda corresponder ao valor correspondente na ordem de compra.
     * **All**: A comparação só será acionada se o valor do campo selecionado em todas as linhas da confirmação de encomenda corresponder ao valor correspondente na ordem de compra.
2. **Order Data Field**
   * **Descrição**: Especifica o campo de dados a comparar entre a confirmação de encomenda e a ordem de compra.
   * **Detalhe**: Os utilizadores podem selecionar um dos seguintes campos para comparação:
     * **Quantity**: Compara a quantidade encomendada com a quantidade confirmada.
     * **Discount**: Valida que o desconto na confirmação corresponde ao da ordem de compra.
     * **Unit Price**: Garante que o preço unitário na confirmação está alinhado com a ordem de compra.
3. **Operador**
   * **Descrição**: Define a condição aplicada à comparação do campo de dados selecionado.
   * **Opções**:
     * **Equals (=)**: Confirma que o valor corresponde ao da ordem de compra.
     * **Not Equals (≠)**: Garante que o valor é diferente do da ordem de compra.
     * **Greater Than (>)**: Verifica que o valor excede o valor da ordem de compra.
     * **Greater or Equals (≥)**: Confirma que o valor é igual ou superior ao valor da ordem de compra.
     * **Less Than (<)**: Verifica que o valor é inferior ao valor da ordem de compra.
     * **Less or Equals (≤)**: Confirma que o valor é inferior ou igual ao valor da ordem de compra.

## **Componentes adicionais na Versão 4**:

* **Comparison Type**: Seleciona as entidades a comparar. As opções incluem:
  * **Purchase Order to Document**: Compara os dados da ordem de compra com o documento relacionado.
  * **Received to Document**: Compara os dados recebidos (por exemplo, quantidades recebidas) com o documento.
  * **Purchase Order to Received**: Compara os dados da ordem de compra com as quantidades recebidas.

## Funcionalidade:

* **Comparação de campos**: O sistema compara o campo de dados de encomenda selecionado (Unit Price, Discount ou Quantity) da confirmação de encomenda com o valor correspondente na ordem de compra.
* **Execução da ação**: Com base no resultado da comparação e na condição do operador, o cartão pode acionar ações de seguimento, como notificações ou alertas.

## Exemplo de cenário:

* Uma confirmação de encomenda especifica um **preço unitário** de 50 $, enquanto a ordem de compra indica 45 $. Utilizando o operador "Greater Than", o cartão assinala a discrepância, permitindo que a equipa de compras a resolva antes do processamento.

## Conclusão:

Este cartão simplifica a validação de campos individuais de dados de encomenda, assegurando a conformidade com os termos da ordem de compra. Ao isolar um campo de cada vez para comparação, apoia revisões direcionadas e a prevenção de erros no processamento de encomendas.

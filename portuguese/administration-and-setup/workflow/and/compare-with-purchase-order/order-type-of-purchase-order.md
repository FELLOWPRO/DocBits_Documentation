# Order Type of Purchase Order

<figure><img src="../../../../.gitbook/assets/image (277).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar o tipo de encomenda de uma ordem de compra com um valor especificado. O cartão verifica se o tipo de encomenda da ordem de compra cumpre a condição especificada (por exemplo, se é igual, diferente, superior ou cumpre outra condição) de modo a garantir que a ordem de compra está classificada corretamente. Esta comparação pode acionar ações com base em condições específicas, como encaminhar a encomenda para revisão ou aprovação adicional caso sejam encontradas discrepâncias.

## **Componentes do cartão:**

1. **Any/All:**
   * **Descrição**: Define se a condição se aplica a alguma ou a todas as ordens de compra avaliadas no fluxo de trabalho.
   * **Opções**:
     * **Any**: A condição é cumprida se alguma das ordens de compra corresponder à condição especificada.
     * **All**: A condição é cumprida apenas se todas as ordens de compra cumprirem a condição especificada.
2. **Operador:**
   * **Descrição**: Define a condição que será aplicada para comparar o tipo de encomenda com um valor especificado.
   * **Opções**:
     * **Equals (=)**: Verifica se o tipo de encomenda corresponde ao valor especificado.
     * **Not Equals (≠)**: Garante que o tipo de encomenda é diferente do valor especificado.
3. **Order Type:**
   * **Descrição**: Especifica o valor com o qual o tipo de encomenda da ordem de compra será comparado.
   * **Detalhe**: O valor tem de corresponder ao tipo de encomenda ou classificação no sistema.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia o tipo de encomenda da ordem de compra face à condição especificada utilizando o operador selecionado. Se o tipo de encomenda corresponder (ou não corresponder) ao valor especificado, o fluxo de trabalho prossegue em conformidade.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a condição for avaliada como verdadeira (por exemplo, o tipo de encomenda corresponde ao valor especificado), o fluxo de trabalho continuará, podendo acionar ações ou passos de processamento adicionais.
  * **Condição Falsa**: Se a condição for avaliada como falsa (por exemplo, o tipo de encomenda não corresponde ao valor especificado), o fluxo de trabalho não continuará.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o campo de tipo de encomenda da ordem de compra e escolhendo o operador que define como o tipo de encomenda será comparado. De seguida, definem o valor especificado e decidem se aplicam a condição a alguma ou a todas as linhas da ordem de compra.

## **Exemplo de cenário:**

* Uma ordem de compra tem o tipo de encomenda "Standard". O fluxo de trabalho está configurado para verificar se o tipo de encomenda é "Urgent". Utilizando o operador "Equals", o cartão compara o tipo de encomenda e verifica que não corresponde ao valor especificado, acionando o fluxo de trabalho para enviar a encomenda para revisão devido à divergência.

## **Conclusão:**

O cartão de fluxo de trabalho "Order Type of Purchase Order" assegura que as ordens de compra são classificadas corretamente de acordo com o seu tipo de encomenda especificado. Ao automatizar a comparação dos tipos de encomenda, as organizações podem garantir que as ordens de compra são processadas de acordo com as classificações esperadas, ajudando a impor conformidade e a simplificar os fluxos de compras.

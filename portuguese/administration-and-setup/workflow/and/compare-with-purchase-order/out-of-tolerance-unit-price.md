# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para avaliar se o valor combinado dos preços unitários e de um campo especificado excede ou fica aquém de um limiar definido. Ajuda a identificar quaisquer discrepâncias em que os preços unitários, quando combinados com outros campos, estejam fora de tolerância, assegurando que as condições de preços cumprem as expectativas e assinalando quaisquer problemas para revisão ou ação adicional.

## **Componentes do cartão:**

1. **Field Name:**
   * **Descrição**: Especifica o campo do documento que contém o valor a combinar com o preço unitário.
   * **Detalhe**: O valor neste campo será combinado com o preço unitário para criar o valor combinado total para comparação.
2. **Operador:**
   * **Descrição**: Define a condição para comparar o valor combinado do preço unitário e do valor do campo com o valor especificado.
   * **Opções**:
     * **Equals (=)**: Verifica se o valor combinado do preço unitário e do campo corresponde ao valor especificado.
     * **Not Equals (≠)**: Garante que o valor combinado do preço unitário e do campo é diferente do valor especificado.
     * **Greater Than (>)**: Verifica se o valor combinado do preço unitário e do campo excede o valor especificado.
     * **Greater or Equals (≥)**: Verifica se o valor combinado do preço unitário e do campo é superior ou igual ao valor especificado.
     * **Lesser Than (<)**: Verifica se o valor combinado do preço unitário e do campo é inferior ao valor especificado.
     * **Lesser or Equals (≤)**: Verifica se o valor combinado do preço unitário e do campo é inferior ou igual ao valor especificado.
3. **Value:**
   * **Descrição**: Especifica o valor com o qual o valor combinado do preço unitário e do campo será comparado.
   * **Detalhe**: Este valor numérico representa o limiar de comparação. Se o valor combinado do preço unitário e do campo exceder ou ficar aquém deste valor (com base no operador selecionado), a condição acionará as ações especificadas.

## **Funcionalidade:**

* &#x20;**Avaliação da condição:** O sistema calcula o valor combinado multiplicando ou somando o preço unitário com o valor do campo, consoante a configuração. O resultado é depois comparado com o valor especificado utilizando o operador selecionado. Se a condição for cumprida (ou seja, o valor combinado está fora de tolerância), o fluxo de trabalho prossegue com o passo seguinte, seja ele aprovação, rejeição ou revisão adicional.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a comparação resultar em verdadeiro (ou seja, o valor combinado cumpre a condição), o fluxo de trabalho aciona a ação associada à condição verdadeira (por exemplo, aprovação ou notificação).
  * **Condição Falsa**: Se a comparação resultar em falso (ou seja, o valor combinado não cumpre a condição), o fluxo de trabalho não prosseguirá.

## **Configuração:**

* Os utilizadores selecionam o campo que contém o valor a combinar com o preço unitário. De seguida, escolhem o operador adequado para determinar como o valor combinado será comparado com o valor especificado. Por fim, o utilizador define o valor com o qual o preço combinado será comparado.

## **Exemplo de cenário:**

* Uma fatura indica 50 unidades de um produto a 30 $ cada, totalizando 1500 $. O documento relacionado tem um campo de quantidade com um valor de 10. O preço combinado é calculado multiplicando o preço unitário (30 $) pela quantidade (10), resultando em 300 $. O cartão compara depois este valor combinado com um limiar de 250 $. Utilizando o operador "Greater Than", o cartão identifica que 300 $ é superior a 250 $, acionando um processo de aprovação para o documento.

## **Conclusão:**

O cartão de fluxo de trabalho "Out of Tolerance Unit Prices Combined with Fields" ajuda a garantir que os valores de preços e de campos estão alinhados com as regras de negócio. Ao automatizar esta verificação, as organizações podem identificar discrepâncias no início do processo, assegurando que quaisquer preços unitários fora de tolerância são assinalados para revisão ou ação necessária.

# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para avaliar se o preço unitário, quando combinado com um valor de campo especificado (como quantidade, desconto ou encargos adicionais), cumpre uma condição definida. O cartão compara o preço unitário e o valor do campo com um limiar especificado para ajudar a garantir que os preços estão alinhados com as expectativas. Esta comparação pode acionar ações com base em condições específicas, como assinalar discrepâncias ou automatizar processos de aprovação em fluxos de compras ou de receção.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição:** Especifica o campo do documento que contém o valor a combinar com o preço unitário.
   * **Detalhe:** Tem de corresponder ao identificador exato do primeiro campo dentro do documento.
2. **Operador**
   * **Descrição:** Define a condição que será aplicada à comparação entre o valor combinado e o valor especificado.
   * **Opções:**
     * **Equals (=):** Verifica se o valor combinado do preço unitário e do campo corresponde ao valor especificado.
     * **Not Equals (≠):** Garante que o valor combinado do preço unitário e do campo é diferente do valor especificado.
     * **Greater Than (>):** Verifica se o valor combinado é superior ao valor especificado.
     * **Greater or Equals (≥):** Verifica se o valor combinado é superior ou igual ao valor especificado.
     * **Lesser Than (<):** Verifica se o valor combinado é inferior ao valor especificado.
     * **Lesser or Equals (≤):** Verifica se o valor combinado é inferior ou igual ao valor especificado.
3. **Value**
   * **Descrição:** Especifica o valor com o qual o valor combinado do preço unitário e do campo será comparado.
   * **Detalhe:** O valor tem de ser um valor numérico.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia o valor combinado do preço unitário e do campo com base no operador selecionado e compara-o com o valor especificado. O resultado desta avaliação determina se a condição é verdadeira ou falsa.
* **Execução da ação:**
  * **Condição Verdadeira:** Se a comparação resultar em verdadeiro (por exemplo, o valor combinado excede o valor especificado), o fluxo de trabalho prossegue com a condição verdadeira. Isto pode acionar ações como aprovação, encaminhamento de documentos ou aplicação de regras de processamento.
  * **Condição Falsa:** Se a comparação resultar em falso (por exemplo, o valor combinado não cumpre a condição), o fluxo de trabalho prossegue com a condição falsa. Isto pode acionar uma notificação, enviar o documento para revisão manual ou interromper o fluxo de trabalho.

## **Configuração:**

* Os utilizadores começam por selecionar o(s) campo(s) do documento que contém(êm) o(s) valor(es) a combinar com o preço unitário. Após selecionar o campo, escolhem o operador adequado para definir como o valor combinado será comparado com o valor especificado. Depois, podem definir o valor.

## **Exemplo de cenário:**

* Uma fatura indica 50 unidades de um produto a 20 $ cada, totalizando 1000 $. O documento relacionado tem um campo de quantidade com um valor de 10. Utilizando o operador "Greater Than", o cartão compara o valor combinado do preço unitário (20 $) e da quantidade (10), que é igual a 200 $. O cartão verifica se o valor combinado é superior a 150 $ (o valor especificado). Como o valor combinado de 200 $ é superior ao limiar de 150 $, o fluxo de trabalho prossegue para acionar uma aprovação para o documento.

## **Conclusão:**

O cartão de fluxo de trabalho "Unit Price Combined with Fields" assegura que as condições de preços são cumpridas ao avaliar o valor combinado do preço unitário e de um campo especificado. Ao automatizar esta comparação, as organizações podem assegurar consistência e assinalar discrepâncias nos preços ou nas quantidades antes de avançar com a aprovação, ajudando a simplificar os processos de compras e financeiros.

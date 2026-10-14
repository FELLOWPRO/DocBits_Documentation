# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar IDs de itens entre uma ordem de compra e um documento relacionado, de modo a garantir que os itens corretos estão incluídos. O cartão avalia se o ID de item na ordem de compra corresponde ao ID de item no documento. Esta comparação pode acionar ações caso sejam encontradas discrepâncias, assegurando que os itens no documento estão alinhados com a ordem de compra.

## **Componentes do cartão:**

1. **Any / All:**
   * **Descrição**: Define se a condição se aplica a alguma ou a todas as instâncias de comparação de IDs de itens.
   * **Opções**:
     * **Any**: A condição é cumprida se algum ID de item na ordem de compra corresponder ao ID de item no documento.
     * **All**: A condição é cumprida apenas se todos os IDs de itens na ordem de compra corresponderem aos IDs de itens no documento.
2. **Operador:**
   * **Descrição**: Define a condição para comparar o ID de item na ordem de compra com o ID de item no documento.
   * **Opções**:
     * **Equals (=)**: Verifica se o ID de item na ordem de compra corresponde exatamente ao ID de item no documento.
     * **Not Equals (≠)**: Garante que o ID de item na ordem de compra não corresponde ao ID de item no documento.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema compara o ID de item na ordem de compra com o ID de item no documento com base no operador selecionado. Se a condição de comparação for verdadeira (por exemplo, os IDs de itens correspondem ou não correspondem), o fluxo de trabalho prossegue em conformidade.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a condição for avaliada como verdadeira (por exemplo, o ID de item na ordem de compra é igual ao ID de item no documento), o fluxo de trabalho prosseguirá com a ação verdadeira (por exemplo, aprovação ou processamento adicional).
  * **Condição Falsa**: Se a condição for avaliada como falsa (por exemplo, o ID de item na ordem de compra não corresponde ao ID de item no documento), o fluxo de trabalho não prosseguirá.

## **Configuração:**

* Os utilizadores configuram o cartão selecionando o ID de item tanto na ordem de compra como no documento. De seguida, escolhem o operador adequado (Equals ou Not Equals) para definir como os IDs de itens serão comparados. Por fim, os utilizadores selecionam se a condição se aplica a alguma ou a todas as instâncias dos IDs de itens na comparação.

## **Exemplo de cenário:**

* Uma fatura indica um item com o ID "ABC123" e a ordem de compra relacionada também inclui um item com o ID "ABC123". Utilizando o operador "Equals", o cartão compara o ID de item no documento com o ID de item na ordem de compra. Como os IDs de itens correspondem, o fluxo de trabalho continua sem problemas.

## **Conclusão:**

O cartão de fluxo de trabalho "Item ID Comparison" assegura que os IDs de itens nos documentos estão alinhados com os das ordens de compra. Isto ajuda a prevenir discrepâncias nas listagens de itens e garante que os itens corretos são processados de acordo com a ordem de compra. A capacidade de comparar com base em algumas ou em todas as instâncias proporciona flexibilidade para diferentes casos de utilização, melhorando a precisão e a eficiência dos fluxos de compras.

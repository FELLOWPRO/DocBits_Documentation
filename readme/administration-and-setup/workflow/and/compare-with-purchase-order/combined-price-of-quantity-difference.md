# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**:

Este cartão de fluxo de trabalho avalia o preço combinado de uma diferença de quantidade, comparando-o com um valor especificado. Ajuda a automatizar ações com base em discrepâncias de preço e quantidade entre documentos relacionados, melhorando os fluxos de compras e de receção. A **Versão 4** amplia esta funcionalidade ao permitir comparações entre diferentes entidades, como a ordem de compra, as quantidades recebidas e o próprio documento, acrescentando mais flexibilidade e controlo ao fluxo de trabalho.

## **Componentes do cartão**:

1. **Operador**:&#x20;
   * **Descrição:** A condição para comparar o preço combinado com um valor especificado.
   * **Opções:**
     * **Equals (=)**: Verifica se o preço combinado corresponde ao valor especificado.
     * **Not Equals (≠)**: Garante que o preço combinado é diferente do valor especificado.
     * **Greater Than (>)**: Verifica se o preço combinado é superior ao valor especificado.
     * **Greater or Equals (≥)**: Verifica se o preço combinado é superior ou igual ao valor especificado.
     * **Lesser Than (<)**: Verifica se o preço combinado é inferior ao valor especificado.
     * **Lesser or Equals (≤)**: Verifica se o preço combinado é inferior ou igual ao valor especificado.
2. **Value**:&#x20;
   * **Descrição:** Especifica o valor com o qual o preço combinado da diferença de quantidade será comparado.
   * **Detalhe:** O valor tem de ser um valor numérico.

## **Componentes adicionais na Versão 4**:

* **Comparison Type**: Seleciona as entidades a comparar. As opções incluem:
  * **Purchase Order to Document**: Compara as quantidades e os preços entre a ordem de compra e o documento relacionado.
  * **Received to Document**: Compara as quantidades recebidas com as quantidades no documento.
  * **Purchase Order to Received**: Compara as quantidades da ordem de compra com as quantidades recebidas.

## **Funcionalidade**:

* **Avaliação da condição**: Calcula o preço combinado multiplicando a diferença de quantidade pelo preço por unidade e compara-o com o valor especificado utilizando o operador selecionado.\
  A **Versão 4** acrescenta a opção de comparar entidades adicionais com base na configuração do utilizador, como ordem de compra com recebida ou ordem de compra com documento.
* **Execução da ação**: Consoante o preço combinado cumprir ou não a condição especificada, o fluxo de trabalho continuará com condições verdadeiras ou falsas para acionar ações ou interromper o fluxo de trabalho. A **Versão 4** também permite uma execução de ações mais dinâmica, em que o tipo de condição (por exemplo, ordem de compra com recebida) influencia o passo seguinte.

## **Configuração**:

* **Versão 3**: Os utilizadores configuram o cartão selecionando os campos do documento para a diferença de quantidade e o preço por unidade. O operador é depois escolhido para definir como o preço combinado será comparado com o valor especificado. Por fim, os utilizadores definem a condição de continuação (verdadeira ou falsa), que determina o passo seguinte no fluxo de trabalho.
* **Versão 4**: Para além da configuração da **Versão 3**, os utilizadores têm a opção adicional de configurar o **Comparison Type**. Isto define que entidades serão comparadas, tais como **Purchase Order to Document**, **Received to Document** ou **Purchase Order to Received**.

## **Exemplo de cenário**:

* Uma fatura apresenta 50 unidades de um produto a 100 $ cada, totalizando 5000 $. A ordem de compra relacionada autorizou uma compra de 4500 $ por 45 unidades. A diferença de quantidade é de 5 unidades e o preço combinado da diferença é de 500 $. O cartão compara a quantidade da ordem de compra (45 unidades) com a quantidade recebida (50 unidades) e verifica se o preço combinado é superior a 400 $ (o valor especificado). Utilizando o operador **Greater Than (>)**, o cartão identifica a discrepância e assinala-a para revisão pela equipa financeira.

## **Conclusão**:

A **Versão 3** do cartão de fluxo de trabalho "Combined Price of Quantity Difference" oferece uma abordagem direta para comparar discrepâncias de quantidade e acionar ações com base em limiares de preço.\
A **Versão 4** amplia esta funcionalidade ao permitir comparações entre diferentes entidades (ordem de compra, recebida, documento), proporcionando mais flexibilidade e controlo sobre o fluxo de trabalho. As organizações podem agora automatizar cenários mais complexos e impor um controlo mais rigoroso sobre os seus processos de compras e de receção.

# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho é utilizado para comparar o preço unitário num documento com o preço unitário numa ordem de compra, assegurando que os preços estão alinhados dentro dos níveis de tolerância definidos. A comparação pode acionar ações caso o preço unitário não corresponda às expectativas. A **Versão 4** acrescenta mais flexibilidade ao permitir aos utilizadores escolher diferentes entidades para comparação, proporcionando um nível mais profundo de controlo sobre os processos de preços e de compras.

## **Componentes do cartão:**

1. **Any / All:**
   * **Descrição**: Define se a condição se aplica a alguma ou a todas as instâncias em que o preço unitário é comparado.
   * **Opções**:
     * **Any**: A condição é cumprida se algum preço unitário satisfizer a condição de comparação especificada.
     * **All**: A condição é cumprida apenas se todos os preços unitários satisfizerem a condição de comparação especificada.
2. **Operador:**
   * **Descrição**: Define a condição para comparar o preço unitário com o valor especificado.
   * **Opções**:
     * **Equals (=)**: Verifica se o preço unitário corresponde ao valor especificado.
     * **Not Equals (≠)**: Garante que o preço unitário é diferente do valor especificado.
     * **Greater Than (>)**: Verifica se o preço unitário é superior ao valor especificado.
     * **Greater or Equals (≥)**: Verifica se o preço unitário é superior ou igual ao valor especificado.
     * **Lesser Than (<)**: Verifica se o preço unitário é inferior ao valor especificado.
     * **Lesser or Equals (≤)**: Verifica se o preço unitário é inferior ou igual ao valor especificado.

## **Componentes adicionais na Versão 4:**

**Comparison Type:**

* **Descrição**: Permite aos utilizadores escolher que entidades serão comparadas para além do preço unitário.
* **Opções**:
  * **Purchase Order to Document**: Compara o preço unitário na ordem de compra com o preço unitário no documento.
  * **Received to Document**: Compara a quantidade recebida com o preço unitário no documento.
  * **Purchase Order to Received**: Compara o preço unitário na ordem de compra com a quantidade recebida.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema compara o preço unitário no documento com o preço unitário na ordem de compra (ou outra entidade selecionada, na Versão 4) com base no operador selecionado. Se a comparação for verdadeira, o fluxo de trabalho prossegue de acordo com os próximos passos, acionando a aprovação ou interrompendo o processo.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a condição for avaliada como verdadeira (por exemplo, o preço unitário no documento é superior ao valor especificado), o fluxo de trabalho prosseguirá com a ação verdadeira (por exemplo, aprovação, processamento do documento).
  * **Condição Falsa**: Se a condição for avaliada como falsa (por exemplo, o preço unitário no documento não cumpre a comparação), o fluxo de trabalho não prosseguirá.

## **Configuração:**

* **Configuração da Versão 3:** Os utilizadores configuram o cartão selecionando o preço unitário no documento, escolhendo o operador adequado para definir como o preço unitário será comparado com o valor especificado e definindo o valor a comparar. Adicionalmente, os utilizadores selecionam se a condição se aplica a alguma ou a todas as instâncias da comparação do preço unitário.
* **Configuração da Versão 4:** Na Versão 4, os utilizadores têm a opção adicional de selecionar o Comparison Type. Isto permite-lhes definir as entidades a comparar, tais como Purchase Order to Document, Received to Document ou Purchase Order to Received. Isto aumenta a flexibilidade do cartão para comparar preços unitários em cenários mais complexos.

## **Exemplo de cenário:**

*   **Exemplo da Versão 3:**&#x20;

    Uma fatura apresenta um preço unitário de 50 $. A ordem de compra relacionada tem um preço unitário de 45 $. O cartão compara os dois preços unitários utilizando o operador "Greater Than". Como o preço unitário no documento (50 $) é superior ao preço unitário na ordem de compra (45 $), o fluxo de trabalho acionará a condição verdadeira (por exemplo, enviar o documento para revisão).
* **Exemplo da Versão 4:**\
  Uma fatura apresenta um preço unitário de 50 $ e a ordem de compra relacionada autorizou um preço unitário de 45 $. Adicionalmente, a quantidade recebida é de 60 unidades. O cartão compara a quantidade recebida com o preço unitário do documento utilizando o operador "Greater Than". Como a quantidade recebida (60) é superior ao preço unitário (50 $), o fluxo de trabalho aciona a condição verdadeira e o documento é assinalado para revisão adicional.

## **Conclusão:**

A Versão 3 do cartão de fluxo de trabalho "Unit Price Comparison" foi concebida para garantir que os preços unitários nos documentos estão alinhados com os das ordens de compra, acionando ações com base em condições definidas. A Versão 4 amplia esta funcionalidade ao introduzir opções de comparação mais complexas, como comparar ordens de compra com documentos, quantidades recebidas com documentos e ordens de compra com quantidades recebidas. Esta flexibilidade adicional permite às organizações tratar cenários de preços e de compras mais sofisticados, melhorando o controlo e a precisão dos seus fluxos de trabalho.

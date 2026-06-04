# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar a quantidade num documento com a tolerância definida na ordem de compra. Permite aos utilizadores avaliar se a quantidade cumpre determinadas condições, como igualdade ou ultrapassagem da tolerância especificada. Na Versão 4, o cartão amplia a funcionalidade ao acrescentar a capacidade de comparar várias entidades, incluindo a ordem de compra, as quantidades recebidas e as quantidades do documento, oferecendo maior flexibilidade no tratamento de diferentes cenários.

## **Componentes do cartão:**

1. **Any / All:**
   * **Descrição**: Especifica como a comparação deve ser aplicada a vários itens ou condições.
   * **Opções**:
     * **Any**: Pelo menos uma das condições tem de ser verdadeira para que a ação seja acionada.
     * **All**: Todas as condições têm de ser verdadeiras para que a ação prossiga.
2. **Operador:**
   * **Descrição**: Define a condição que será aplicada para comparar a quantidade do documento com a tolerância especificada.
   * **Opções**:
     * **Equals (=)**: Verifica se a quantidade corresponde ao valor de tolerância especificado.
     * **Not Equals (≠)**: Garante que a quantidade é diferente do valor de tolerância especificado.
     * **Greater Than (>)**: Verifica se a quantidade é superior à tolerância especificada.
     * **Greater or Equals (≥)**: Verifica se a quantidade é superior ou igual à tolerância especificada.
     * **Lesser Than (<)**: Verifica se a quantidade é inferior à tolerância especificada.
     * **Lesser or Equals (≤)**: Verifica se a quantidade é inferior ou igual à tolerância especificada.
3. **Tolerance Amount:**
   * **Descrição**: Especifica o valor de tolerância com o qual a quantidade do documento será comparada.
   * **Detalhe**: Este valor é numérico e representa o limiar de variação permitida na quantidade.
4. **Tolerance Type:**
   * **Descrição**: Define o tipo de tolerância que será aplicado.
   * **Opções**:
     * **Percentage**: A tolerância é calculada como uma percentagem da quantidade da ordem de compra.
     * **Value**: A tolerância é especificada como um valor numérico fixo.

## **Componentes adicionais na Versão 4:**

* **Comparison Type**: Seleciona as entidades a comparar, oferecendo mais flexibilidade na forma como as quantidades são avaliadas na Versão 4.
  * **Purchase Order to Document**: Compara a quantidade na ordem de compra com a quantidade no documento relacionado.
  * **Received to Document**: Compara a quantidade recebida com a quantidade no documento.
  * **Purchase Order to Received**: Compara a quantidade da ordem de compra com a quantidade recebida.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema compara a quantidade no documento com a tolerância na ordem de compra com base no operador e no valor/tipo de tolerância selecionados. Na Versão 4, o **Comparison Type** permite comparar diferentes quantidades, como ordem de compra com recebida, ou ordem de compra com documento, proporcionando uma comparação mais dinâmica.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a comparação resultar em verdadeiro (por exemplo, a quantidade do documento está dentro do intervalo de tolerância aceitável), o fluxo de trabalho prossegue.
  * **Condição Falsa**: Se a comparação resultar em falso (por exemplo, a quantidade não cumpre a tolerância), o fluxo de trabalho não prosseguirá.

## **Configuração:**

**Versão 3:**

* Os utilizadores configuram o cartão selecionando a quantidade do documento, definindo o valor e o tipo de tolerância e escolhendo o operador adequado para comparar a quantidade com a tolerância. O cartão avalia se a quantidade está dentro do limiar de tolerância e prossegue com a ação "True" ou "False" consoante o resultado.

**Versão 4:**

* Para além da configuração da Versão 3, os utilizadores podem selecionar o **Comparison Type**, permitindo comparações entre diferentes entidades, tais como:
  * **Purchase Order to Document**
  * **Received to Document**
  * **Purchase Order to Received**

## **Exemplo de cenário:**

Uma fatura indica que foram entregues 100 unidades, mas a ordem de compra apenas autorizou 90 unidades. O valor de tolerância está definido em 10 unidades e o tipo de tolerância é absoluto.

* **Versão 3**: O cartão compara as 100 unidades do documento com a tolerância de 90 unidades da ordem de compra. Se a quantidade exceder a tolerância, o cartão assinala a discrepância para revisão adicional.
* **Versão 4**: O cartão pode comparar a **quantidade da ordem de compra** (90 unidades) com a **quantidade recebida** (100 unidades) ou a **quantidade do documento** (100 unidades). Dependendo do **Comparison Type** selecionado, verifica se a diferença entre as duas entidades excede a tolerância e aciona a ação correspondente.

## **Conclusão:**

* **Versão 3**: Este cartão de fluxo de trabalho compara a quantidade do documento com a tolerância da ordem de compra, ajudando a garantir que as discrepâncias de quantidade são assinaladas e tratadas adequadamente.
* **Versão 4**: Amplia esta funcionalidade ao permitir aos utilizadores comparar diferentes entidades, como ordem de compra com recebida ou ordem de compra com documento, proporcionando maior flexibilidade no tratamento de cenários mais complexos. A Versão 4 assegura um controlo mais rigoroso dos fluxos de compras e receção, oferecendo comparações e ações mais dinâmicas com base no tipo de comparação escolhido.

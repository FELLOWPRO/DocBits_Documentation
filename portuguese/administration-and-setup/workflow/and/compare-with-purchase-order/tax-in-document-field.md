# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para avaliar se o valor de imposto num campo de documento corresponde ao valor de imposto numa ordem de compra, considerando tolerâncias baseadas no charge ID. O cartão compara estes dois valores de imposto (um do campo do documento e outro da ordem de compra) e verifica se cumprem uma condição especificada (por exemplo, igual, superior, inferior, etc.). Isto ajuda a garantir que os valores de imposto são consistentes e a assinalar discrepâncias para revisão ou aprovação adicional nos fluxos de compras.

## **Componentes do cartão:**

1. **Field Name**
   * **Descrição**: Especifica o campo do documento que contém o valor de imposto a comparar com o valor de imposto na ordem de compra.
   * **Detalhe**: Este campo tem de corresponder ao identificador exato do valor de imposto no documento.
2. **Operador**
   * **Descrição**: Define a condição a aplicar à comparação entre o valor de imposto do documento e o valor de imposto da ordem de compra.
   * **Opções**:
     * **Equals (=)**: Verifica se o imposto no campo do documento corresponde ao imposto na ordem de compra.
     * **Not Equals (≠)**: Garante que o imposto no campo do documento não corresponde ao imposto na ordem de compra.
     * **Greater Than (>)**: Verifica se o imposto no campo do documento é superior ao imposto na ordem de compra.
     * **Greater or Equals (≥)**: Verifica se o imposto no campo do documento é superior ou igual ao imposto na ordem de compra.
     * **Lesser Than (<)**: Verifica se o imposto no campo do documento é inferior ao imposto na ordem de compra.
     * **Lesser or Equals (≤)**: Verifica se o imposto no campo do documento é inferior ou igual ao imposto na ordem de compra.
3. **Master Data Table**
   * **Descrição**: A tabela que contém os detalhes da ordem de compra, incluindo o charge ID e os valores de imposto.
   * **Detalhe**: Esta tabela tem de ter uma referência ao charge ID associado ao valor de imposto da ordem de compra.
4. **Tolerance Amount**
   * **Descrição**: O valor-limiar dentro do qual os valores de imposto podem variar. É utilizado para acomodar pequenas discrepâncias nos cálculos de imposto.
   * **Detalhe**: O valor de tolerância deve ser um valor numérico, definindo a diferença máxima permitida entre os valores de imposto.
5. **Tolerance Type**
   * **Descrição**: Especifica o tipo de tolerância aplicado, absoluto ou baseado em percentagem.
   * **Opções**:
     * **Value**: A tolerância é um valor numérico fixo.
     * **Percentage**: A tolerância é calculada como uma percentagem do valor de imposto.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema avalia se o valor de imposto no campo do documento cumpre a condição especificada quando comparado com o valor de imposto na ordem de compra (com a referência ao charge ID a partir da tabela de dados-mestre). O valor e o tipo de tolerância são considerados nesta avaliação para permitir pequenas diferenças nos cálculos de imposto.
* **Execução da ação:**
  * **Condição Verdadeira**: Se o imposto no campo do documento cumprir a condição quando comparado com o imposto da ordem de compra (dentro do valor e tipo de tolerância), o fluxo de trabalho continua.
  * **Condição Falsa**: Se o imposto no campo do documento não cumprir a condição (não estar dentro do intervalo de tolerância ou a comparação falhar), o fluxo de trabalho será interrompido.

## **Configuração:**

* Os utilizadores têm de selecionar o campo do documento que contém o valor de imposto a comparar. De seguida, escolhem o operador para definir como a comparação deve ser feita (por exemplo, equals, greater than). Depois disto, os utilizadores precisam de especificar a referência da tabela de dados-mestre e definir o valor e o tipo de tolerância para acomodar pequenas discrepâncias de imposto.

## **Exemplo de cenário:**

* Uma fatura indica um valor de imposto de 100 $. A ordem de compra correspondente, encontrada na tabela de dados-mestre, especifica um valor de imposto de 95 $. Utilizando o operador "Greater Than", o sistema compara o valor de imposto do documento (100 $) com o valor de imposto da ordem de compra (95 $) com uma tolerância de 10 $ (tipo de tolerância absoluto). Como a diferença de 5 $ está dentro do intervalo de tolerância, o fluxo de trabalho prossegue sem acionar quaisquer alertas.

## **Conclusão:**

O cartão de fluxo de trabalho "Tax in Document Field Comparison" assegura que os valores de imposto nos documentos estão alinhados com os detalhes da ordem de compra, permitindo pequenas discrepâncias com base nas tolerâncias especificadas. Ao automatizar esta verificação, as organizações podem minimizar erros nos cálculos de imposto e simplificar os processos de compras, reduzindo a necessidade de intervenção ou aprovações manuais.

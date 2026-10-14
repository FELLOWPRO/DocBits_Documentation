# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho compara os encargos totais num campo de documento com os encargos correspondentes numa ordem de compra. O cartão ajuda a garantir que os encargos no documento estão alinhados com os da ordem de compra, considerando os níveis de tolerância especificados. A comparação pode acionar ações caso sejam encontradas discrepâncias, como assinalar discrepâncias para revisão ou ajustar os encargos em conformidade.

## **Componentes do cartão:**

1. **Field Name:**
   * **Descrição**: Especifica o campo do documento que contém os valores dos encargos totais a comparar com os encargos na ordem de compra.
   * **Detalhe**: O valor neste campo representa os encargos totais aplicados no documento (por exemplo, fatura) e será comparado com o encargo da ordem de compra.
2. **Operador:**
   * **Descrição**: Define a condição que será aplicada à comparação entre o encargo total no documento e o encargo na ordem de compra.
   * **Opções**:
     * **Equals (=)**: Verifica se o encargo total no documento corresponde ao encargo na ordem de compra.
     * **Not Equals (≠)**: Garante que o encargo total no documento é diferente do encargo na ordem de compra.
     * **Greater Than (>)**: Verifica se o encargo total no documento é superior ao encargo na ordem de compra.
     * **Greater or Equals (≥)**: Verifica se o encargo total no documento é superior ou igual ao encargo na ordem de compra.
     * **Lesser Than (<)**: Verifica se o encargo total no documento é inferior ao encargo na ordem de compra.
     * **Lesser or Equals (≤)**: Verifica se o encargo total no documento é inferior ou igual ao encargo na ordem de compra.
3. **Tolerance Amount**
   * **Descrição**: Especifica o limiar de tolerância para comparar os encargos totais.
   * **Detalhe**: Este valor numérico representa a variação permitida nos encargos entre o documento e a ordem de compra.
4. **Tolerance Type:**
   * **Descrição**: Especifica o tipo de tolerância que será aplicado.
   * **Opções**:
     * **Percentage**: A tolerância é aplicada como uma percentagem do encargo da ordem de compra.
     * **Value**: A tolerância é aplicada como um valor numérico fixo.
5. **Separator:**
   * **Descrição**: Especifica o separador utilizado para distinguir o Charge ID no fim do nome do campo.
   * **Detalhe**: O separador separa o campo de encargo do Charge ID único que será utilizado para associar o encargo do documento ao encargo correspondente na ordem de compra.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema compara o encargo total no campo do documento com o encargo correspondente na ordem de compra com base no operador e na tolerância. A tolerância é aplicada para determinar se a diferença entre os dois encargos está dentro de um intervalo aceitável.
* **Execução da ação:**
  * **Condição Verdadeira**: Se os encargos corresponderem (considerando a tolerância) e a condição for verdadeira, o fluxo de trabalho continuará com a ação definida, como a aprovação do documento ou o processamento adicional.
  * **Condição Falsa**: Se a condição for falsa (ou seja, os encargos não correspondem dentro da tolerância), o fluxo de trabalho não continuará.

## **Configuração:**

* Os utilizadores começam por selecionar o campo do documento que contém o valor do encargo total. De seguida, selecionam o operador para definir como o encargo será comparado com o encargo da ordem de compra. Depois, definem o valor e o tipo de tolerância (percentagem ou absoluto). Por fim, especificam o separador e o Charge ID que serão utilizados na comparação.

## **Exemplo de cenário:**

Uma fatura indica um encargo de 500 $ no campo "total charges". O encargo correspondente da ordem de compra é de 480 $ e a tolerância está definida em 20 $ (tolerância absoluta). O cartão compara o encargo do documento com o encargo da ordem de compra:

* O encargo total no documento está dentro da tolerância de 20 $ da ordem de compra e o fluxo de trabalho continua sem problemas.
* Se o encargo exceder a tolerância, o fluxo de trabalho assinala a discrepância para revisão.

## **Conclusão:**

O cartão de fluxo de trabalho "Compare Total Charges" assegura que os encargos nos documentos estão alinhados com os das ordens de compra, considerando os níveis de tolerância especificados. Isto ajuda as organizações a automatizar o processo de verificação, a identificar discrepâncias antecipadamente e a manter um melhor controlo sobre os processos relacionados com encargos.

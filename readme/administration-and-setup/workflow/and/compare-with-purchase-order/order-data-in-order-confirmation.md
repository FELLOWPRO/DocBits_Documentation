# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

Este cartão de fluxo de trabalho foi concebido para comparar campos específicos — **Unit Price**, **Discount** ou **Quantity** — entre uma confirmação de encomenda e uma ordem de compra. Assegura consistência e conformidade com os termos acordados. Com base no resultado da comparação, o cartão permite aos utilizadores escrever texto especificado num campo escolhido quando a condição é avaliada como **verdadeira** ou **falsa**, simplificando o processamento de documentos e reduzindo a intervenção manual.

## **Componentes do cartão**

1. **Order Data**
   * **Descrição:** Especifica o campo a comparar entre a confirmação de encomenda e a ordem de compra.
   * **Opções:**
     * **Unit Price**: Compara o preço unitário em ambos os documentos.
     * **Discount**: Compara a percentagem ou o valor do desconto.
     * **Quantity**: Compara a quantidade encomendada.
2. **Operador**
   * **Descrição:** Define a condição aplicada durante a comparação.
   * **Opções:**
     * **Equals (=):** Verifica se o valor no campo selecionado corresponde entre a confirmação de encomenda e a ordem de compra.
     * **Not Equals (≠):** Garante que o valor no campo selecionado difere entre os dois documentos.
3. **Text**
   * **Descrição:** Especifica o texto a escrever no campo de destino aquando da avaliação da condição.
   * **Detalhe:** Este texto pode incluir notas personalizadas, atualizações de estado ou valores predefinidos.
4. **Field Name**
   * **Descrição:** Especifica o campo onde o texto será escrito.
   * **Detalhe:** O campo de destino é selecionado de entre os campos editáveis disponíveis no sistema.
5. **Condition Result**
   * **Descrição:** Determina quando o texto deve ser escrito, com base no resultado da comparação.
   * **Opções:**
     * **True:** Escreve o texto se a condição de comparação for cumprida.
     * **False:** Escreve o texto se a condição de comparação não for cumprida.

## **Funcionalidade**

* **Avaliação da comparação:** O sistema compara o campo selecionado entre a confirmação de encomenda e a ordem de compra utilizando o operador especificado.
* **Execução da ação:** Se a condição for avaliada como **verdadeira** ou **falsa**, o texto especificado é escrito no campo designado.

## **Configuração**

* Para configurar este cartão, os utilizadores selecionam primeiro o campo a comparar — **Unit Price**, **Discount** ou **Quantity**. De seguida, escolhem um operador para definir a condição de comparação, como **equals** ou **not equals**. Os utilizadores especificam o texto a escrever num campo de destino e selecionam quando esta ação deve ocorrer, com base no resultado da condição (**true** ou **false**).

## **Exemplo de cenário**

* Uma confirmação de encomenda indica um preço unitário de 50 $ para um produto, enquanto a ordem de compra especifica um preço de 45 $. Utilizando o operador **Not Equals (≠)**, o cartão identifica a discrepância e escreve o texto "Price Mismatch" num campo designado quando a condição é avaliada como **verdadeira**.

## **Conclusão**

O cartão de fluxo de trabalho "\[Unit Price/Discount/Quantity] in Order Confirmation" oferece uma solução prática para garantir a consistência dos documentos. Ao assinalar automaticamente discrepâncias e ao escrever texto relevante em campos especificados, melhora a eficiência e reduz os erros nos processos de gestão de encomendas.

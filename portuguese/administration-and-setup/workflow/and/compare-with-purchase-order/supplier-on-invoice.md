# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão de fluxo de trabalho foi concebido para comparar a informação do fornecedor numa fatura com a informação do fornecedor na ordem de compra relacionada. O cartão assegura que o fornecedor na fatura corresponde ao fornecedor na ordem de compra. Esta comparação ajuda a verificar que o fornecedor correto está a faturar a encomenda e pode acionar ações com base em quaisquer discrepâncias.

## **Componentes do cartão:**

1. **Operador:**
   * **Descrição**: Define a condição para comparar o fornecedor na fatura com o fornecedor na ordem de compra.
   * **Opções**:
     * **Is**: Verifica se o fornecedor na fatura corresponde ao fornecedor na ordem de compra.
     * **Is Not**: Garante que o fornecedor na fatura não corresponde ao fornecedor na ordem de compra.

## **Funcionalidade:**

* **Avaliação da condição:** O sistema compara o fornecedor na fatura com o fornecedor na ordem de compra com base no operador selecionado. Se a condição de comparação for verdadeira (por exemplo, o fornecedor é o mesmo ou diferente, conforme exigido), o fluxo de trabalho prossegue em conformidade.
* **Execução da ação:**
  * **Condição Verdadeira**: Se a condição for avaliada como verdadeira (por exemplo, o fornecedor na fatura corresponde ao fornecedor na ordem de compra), o fluxo de trabalho continua sem acionar quaisquer erros.
  * **Condição Falsa**: Se a condição for avaliada como falsa (por exemplo, o fornecedor na fatura não corresponde ao fornecedor na ordem de compra), o fluxo de trabalho não continuará.

## **Configuração:**

* Os utilizadores escolhem o operador adequado ("Is" ou "Is Not") para definir como os fornecedores serão comparados.

## **Exemplo de cenário:**

* Uma fatura indica um fornecedor com o ID "SUP123" e a ordem de compra relacionada também indica "SUP123" como fornecedor. Utilizando o operador "Is", o cartão compara os fornecedores e verifica que são o mesmo, pelo que o fluxo de trabalho prossegue sem qualquer problema.

## **Conclusão:**

O cartão de fluxo de trabalho "Supplier Comparison" assegura que o fornecedor correto está a faturar a ordem de compra, ajudando a prevenir discrepâncias e erros no processo de compras. Ao verificar automaticamente a informação do fornecedor, as organizações podem simplificar o seu processo de aprovação de faturas e reduzir o risco de fraude ou de erros na faturação de fornecedores.

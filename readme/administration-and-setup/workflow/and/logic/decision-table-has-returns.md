# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão DocBits verifica se uma tabela de decisão especificada tem valores de retorno para um determinado documento e determina se os dados retornados devem ser utilizados nos passos subsequentes do fluxo de trabalho. Assegura que os fluxos de trabalho se podem adaptar dinamicamente com base nos resultados da tabela de decisão.

## **Funcionalidade:**

* **Validação da tabela de decisão:** Este cartão verifica se a tabela de decisão selecionada fornece valores de retorno para o documento que está a ser processado.
* **Seleção da tabela de decisão:** Os utilizadores especificam o nome da tabela de decisão a verificar.
* **Utilizar dados de retorno:** Os utilizadores podem especificar se devem utilizar os dados de retorno em cartões posteriores através de uma definição **Boolean**:
  * **True:** Os dados de retorno estão disponíveis e serão utilizados nos passos subsequentes do fluxo de trabalho.
  * **False:** Os dados de retorno não serão utilizados e o fluxo de trabalho prossegue sem eles.

## **Utilização:**

Este cartão é ideal para fluxos de trabalho que envolvem lógica condicional ou tomada de decisões com base em regras predefinidas numa tabela de decisão. Assegura uma integração transparente dos resultados da tabela de decisão nos processos de fluxo de trabalho.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para verificar a tabela de decisão **"Invoice Processing Rules"** quanto a valores de retorno. O **Boolean** está definido como **True**, indicando que os dados de retorno (por exemplo, requisitos de aprovação) serão utilizados em cartões posteriores para orientar as decisões do fluxo de trabalho.

Ao utilizar o cartão "Decision Table Check", as organizações podem melhorar a flexibilidade do fluxo de trabalho, simplificar o processamento baseado em regras e assegurar consistência na tomada de decisões ao longo dos fluxos de trabalho automatizados.

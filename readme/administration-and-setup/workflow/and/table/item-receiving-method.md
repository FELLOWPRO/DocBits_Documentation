# Método de recebimento de itens

<figure><img src="../../../../.gitbook/assets/workflow-card-qa-20261021-card-ba8550d6feb0-pt.png" alt="Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real." width="563"><figcaption><p>Campos do cartão na versão apresentada. Os campos ainda não estão configurados. Algumas etiquetas desta versão da interface ainda não estão traduzidas ou têm uma tradução incorreta. As explicações desta página usam os termos corretos; a imagem mostra a interface real.</p></figcaption></figure>

## **Propósito:**

Este cartão DocBits verifica se os itens de um conjunto de dados têm um método de receção especificado. Os utilizadores podem optar por validar **qualquer** item ou **todos** os itens do conjunto de dados com base numa condição selecionada, tornando-o adequado para cenários em que os fluxos de trabalho dependem dos métodos de receção dos itens, como na gestão da cadeia de abastecimento ou no controlo de inventário.

## **Funcionalidade:**

* **Validação do método de receção:** Este cartão verifica o método de receção dos itens face a uma condição especificada. Os utilizadores podem escolher entre **qualquer** item ou **todos** os itens do conjunto de dados e definir a condição como **equals** ou **não é igual**.
* **Seleção de itens:** Os utilizadores podem especificar:
  * **Any Item:** O cartão é acionado se pelo menos um item cumprir a condição de método de receção especificada.
  * **Todos os itens:** O cartão é acionado apenas se todos os itens cumprirem a condição de método de receção especificada.
* **Operadores:** Os seguintes operadores estão disponíveis para definir a condição:
  * **Igual a (=):** Verifica se o método de receção corresponde ao valor especificado.
  * **Não é igual (≠):** Garante que o método de receção não corresponde ao valor especificado.

## **Utilização:**

Este cartão é ideal para gestores de armazém, coordenadores de inventário ou pessoal de logística que precisam de validar os métodos de receção dos itens antes de permitir ações adicionais, como processamento, armazenamento ou expedição.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para verificar se **todos os itens** têm o método de receção **igual a "Entrega Direta"**. Se todos os itens cumprirem esta condição, o fluxo de trabalho prossegue, confirmando que todos os itens se destinam a entrega direta.

Ao utilizar o cartão "Receiving Method Validation", as organizações podem assegurar a conformidade com os protocolos de receção, melhorar os fluxos de trabalho de logística e manter a precisão no tratamento dos itens com base em métodos de receção específicos.

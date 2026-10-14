# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão DocBits é utilizado para validar se **todos os valores** numa coluna específica de uma tabela correspondem a um padrão regex fornecido. Para que o fluxo de trabalho continue, todas as entradas da coluna têm de cumprir a condição, tornando este cartão ideal para assegurar consistência e integridade dos dados em todas as entradas.

## **Funcionalidade:**

* **Validação de padrão regex:** Este cartão verifica se **todos os valores** numa coluna especificada de uma tabela correspondem ao padrão de expressão regular fornecido. O fluxo de trabalho só prosseguirá se todas as entradas da coluna cumprirem a condição.
* **Operador:** Os utilizadores definem a coluna e especificam o padrão regex. A condição disponível inclui:
  * **Matches Regex Pattern:** Verifica se todos os valores na coluna especificada correspondem ao padrão regex.
* **Seleção de tabela e coluna:** Os utilizadores especificam a tabela e a coluna que pretendem verificar quanto à correspondência completa do padrão regex.

## **Utilização:**

Este cartão é ideal para casos em que é necessária uniformidade de dados, como garantir que todos os números de telefone, IDs de produto ou outras entradas de campo respeitam um formato específico. Assegura que os fluxos de trabalho só prosseguem quando todas as entradas relevantes são consistentes com o padrão.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para verificar a coluna "Phone Number" na tabela "Contacts", utilizando um padrão regex para validar formatos de números de telefone. Se todas as entradas de número de telefone na coluna corresponderem ao padrão, o cartão aciona o passo seguinte do fluxo de trabalho, confirmando uma formatação de dados uniforme.

Ao utilizar o cartão "All Values Regex Pattern Matching", as organizações podem impor padrões de dados rigorosos e melhorar a precisão do fluxo de trabalho, assegurando que todas as entradas numa coluna especificada cumprem o formato exigido antes de prosseguir.

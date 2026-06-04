# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

Este cartão DocBits é utilizado para validar se algum valor numa coluna específica de uma tabela corresponde a um padrão regex fornecido. Se uma única entrada da coluna corresponder ao padrão, o fluxo de trabalho continuará, sendo ideal para casos de utilização em que identificar uma única correspondência aciona os passos seguintes do processo.

## **Funcionalidade:**

* **Validação de padrão regex:** Este cartão verifica se algum valor numa determinada coluna de uma tabela corresponde ao padrão de expressão regular fornecido. O cartão será acionado e permitirá a continuação do fluxo de trabalho se pelo menos uma entrada da coluna cumprir a condição.
* **Operador:** Os utilizadores definem a coluna e especificam o padrão regex. A condição disponível inclui:
  * **Matches Regex Pattern:** Verifica se pelo menos um valor na coluna especificada corresponde ao padrão regex.
* **Seleção de tabela e coluna:** Os utilizadores especificam a tabela e a coluna que pretendem verificar quanto à correspondência do padrão regex.

## **Utilização:**

Este cartão é particularmente útil para cenários em que uma tabela contém dados que podem exigir correspondências específicas, como validar endereços de e-mail, números de fatura ou IDs de produto. Assegura que os fluxos de trabalho prosseguem quando alguma entrada relevante corresponde ao padrão definido, sem ser necessário verificar todas as entradas.

## **Exemplo de cenário:**

* Um utilizador configura o cartão para verificar entradas na coluna "Email Address" da tabela "Customers", utilizando um padrão regex para formatos de e-mail válidos. Se pelo menos um endereço de e-mail na coluna corresponder ao padrão, o cartão aciona o passo seguinte do fluxo de trabalho, assegurando que o sistema processa a entrada válida.

Ao utilizar o cartão "Regex Pattern Matching", as organizações podem automatizar fluxos de trabalho com base em validações dinâmicas baseadas em padrões, simplificando processos e assegurando que apenas as entradas relevantes acionam ações adicionais.

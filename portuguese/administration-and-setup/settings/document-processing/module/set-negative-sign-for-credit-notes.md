# Definir sinal negativo para notas de crédito

### Visão geral

A configuração **Definir sinal negativo para notas de crédito** (Set Negative Sign for Credit Notes) garante que as **notas de crédito** sejam armazenadas com **valores negativos**. Uma nota de crédito estorna ou reembolsa parte de uma fatura, portanto, na contabilidade, seus valores devem reduzir os totais — ou seja, ser negativos. Quando esta configuração está ativada, o DocBits aplica esse sinal negativo automaticamente.

Esta configuração está **ativada por padrão**.

### O que faz?

Quando um documento é reconhecido como uma **nota de crédito**, o DocBits converte automaticamente os seus valores em valores negativos durante o processamento. Isso afeta os campos monetários, incluindo os valores líquidos, os valores de impostos e os totais (por exemplo, valor líquido, valor do imposto, valor total do imposto, valor líquido total e valor total).

* **Ativada (padrão)** — Os valores das notas de crédito são salvos como valores negativos (por exemplo, `150,00` torna-se `-150,00`). As faturas normais não são afetadas.
* **Desativada** — Os valores são mantidos exatamente como foram lidos do documento, sem alteração de sinal.

{% hint style="info" %}
Isso se aplica apenas a documentos identificados como **notas de crédito**. As faturas normais permanecem sempre inalteradas.
{% endhint %}

### Benefícios

* **Contabilidade correta**: As notas de crédito reduzem os saldos, portanto os valores negativos são o que os seus sistemas contábeis e ERP esperam.
* **Sem edição manual**: A sua equipe não precisa inverter o sinal manualmente em cada nota de crédito.
* **Consistência**: Cada nota de crédito é tratada da mesma forma em toda a sua organização.

### Como usar

1. Vá para **Configurações**.
2. Selecione **Processamento de Documentos**.
3. Selecione **Módulo**.
4. Abra a seção **Tipo de Documento**.
5. Encontre **Definir sinal negativo para notas de crédito** e ligue ou desligue o botão.

### Quando usar este recurso

* **Mantenha ativado** se o seu sistema contábil ou ERP espera que as notas de crédito cheguem com valores negativos (esta é a configuração mais comum).
* **Desative** apenas se o seu sistema posterior já tratar o sinal por conta própria ou esperar que os valores das notas de crédito permaneçam positivos.

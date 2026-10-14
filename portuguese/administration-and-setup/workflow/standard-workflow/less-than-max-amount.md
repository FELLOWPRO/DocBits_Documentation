# Less than Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice.png" alt="DocBits Fatura"><figcaption></figcaption></figure>

Este título sugere que a regra ou condição a configurar foi concebida para tratar faturas em que o montante total é inferior ou igual a um montante máximo especificado.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição verifica se o documento que está a ser processado é uma fatura. Isto é fundamental para garantir que a regra só se aplica a faturas e não a outros tipos de documentos.
2. **And…**
   * **Document Status is Pending Approval**: Isto especifica que a fatura tem de estar no estado "Pending Approval". Esta verificação de estado garante que a regra se aplica apenas a faturas que aguardam aprovação.
   * **Compare two fields: Total Amount Less Or Equals Approver Max Amount**: Esta condição compara o montante total da fatura com o montante máximo autorizado de um aprovador. Se o montante total da fatura for inferior ou igual a esse montante máximo, a regra prossegue para o passo seguinte. Isto inclui provavelmente um nível de tolerância que permite pequenos desvios dentro dos limites especificados.

#### Ação (Then…):

* **Assign user from field Approver Name, use user User as fallback**: Se as condições especificadas forem cumpridas, a fatura é automaticamente atribuída a um aprovador cujo nome está especificado num campo. Se este campo estiver vazio ou indisponível, é atribuído um utilizador predefinido (provavelmente um administrador ou outro colaborador designado) como alternativa para tratar da aprovação.

#### Elementos da interface:

* **Add Card**: Este botão permite provavelmente aos utilizadores adicionar mais condições ou ações à regra, aumentando a flexibilidade e a especificidade do fluxo de trabalho.
* **Save**: Guarda a regra configurada no sistema.

#### Objetivo desta regra:

Esta configuração foi concebida para simplificar o processo de aprovação de faturas, encaminhando-as automaticamente para o aprovador adequado com base no montante e garantindo que apenas as que se encontram dentro de um determinado limiar são tratadas desta forma automatizada. Ajuda a gerir os controlos financeiros e acelera o fluxo de trabalho, reduzindo as verificações manuais para cada fatura.

\

# Above Max Amount

<figure><img src="../../../../.gitbook/assets/docbits_invoice_2.png" alt="DocBits Fatura 2"><figcaption></figcaption></figure>

Este título indica que a regra foi concebida para gerir os casos em que o total da fatura é superior ao montante máximo que um aprovador está autorizado a tratar.

#### Configuração da regra:

1. **When…**
   * **Document Type is Invoice**: Esta condição garante que a regra se aplica apenas a faturas, o que é essencial para encaminhar o fluxo de trabalho corretamente.
2. **And…**
   * **Document Status is Pending Approval**: A fatura tem de estar no estado "Pending Approval". Este estado é fundamental para garantir que a regra é aplicada a faturas que ainda estão a ser processadas e que ainda não foram finalizadas.
   * **Compare two fields: Total Amount Greater Than Approver Max Amount**: Esta condição verifica se o montante total da fatura excede o montante máximo que um aprovador pode tratar. Esta comparação pode também incluir uma definição de tolerância, permitindo pequenas variações com base em critérios predefinidos.

#### Ação (Then…):

* **Assign user from field Next Level Approver, use user User as fallback**: Se a fatura exceder o montante máximo especificado, é automaticamente atribuída a um aprovador de nível superior, indicado pelo campo 'Next Level Approver'. Se este campo não estiver preenchido ou se o utilizador especificado não estiver disponível, é utilizado um utilizador predefinido (provavelmente um administrador ou outro colaborador designado) como alternativa, para garantir que a fatura é revista sem atrasos.

#### Elementos da interface:

* **Add Card**: Esta opção permite adicionar condições ou ações adicionais à regra, proporcionando flexibilidade para responder a cenários complexos.
* **Save**: Este botão guarda a configuração da regra no sistema.

#### Objetivo desta regra:

O objetivo desta regra é garantir que as faturas que excedem determinados limiares financeiros são revistas por aprovadores com os níveis de autorização adequados. Isto ajuda a manter o controlo e a supervisão financeira, garantindo que as despesas são revistas por pessoal com os limites de aprovação exigidos, protegendo assim a organização contra despesas não autorizadas ou inadequadas.

Esta regra, tal como a anterior, ajuda a automatizar o fluxo de trabalho, reduzindo o esforço manual e reforçando a conformidade com as políticas financeiras da organização. É um exemplo de como a automação de fluxos de trabalho pode ser utilizada eficazmente para gerir processos financeiros complexos dentro de uma empresa.

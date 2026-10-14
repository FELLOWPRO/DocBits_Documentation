# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Propósito**

Este cartão de fluxo de trabalho gere a execução de operações com base no facto de uma tarefa ou documento estar atribuído a um determinado utilizador ou conjunto de utilizadores. Utiliza lógica condicional para acionar ou impedir ações específicas, sendo ideal para fluxos de trabalho que exijam tratamento específico por utilizador.

**Componentes do cartão**

1. **Operador**
   * **Descrição**: Define a condição lógica a aplicar à atribuição de utilizador.
   * **Opções**:
     * **IS**: Aciona a operação se o utilizador atribuído ao documento ou tarefa corresponder a algum utilizador da lista especificada.
     * **IS NOT**: Aciona a operação se o utilizador atribuído ao documento ou tarefa não corresponder a nenhum utilizador da lista especificada.
2. **User List**
   * **Descrição**: Uma lista ou seleção de utilizadores a comparar com o utilizador atribuído.
   * **Detalhe**: Esta lista pode incluir um ou vários utilizadores, permitindo que o cartão trate eficazmente tanto condições de utilizador único como de utilizadores múltiplos. A seleção pode ser feita através de caixas de verificação, de uma lista pendente de seleção múltipla ou de elementos de interface semelhantes.

**Funcionalidade**

* **Identificação da atribuição de utilizador**: Identifica automaticamente o utilizador ou utilizadores atribuídos a uma determinada tarefa ou documento dentro do sistema ERP.
* **Avaliação da condição**:
  * Com o operador **IS**, o cartão verifica se o utilizador atribuído está entre os indicados na User List.
  * Com o operador **IS NOT**, o cartão garante que o utilizador atribuído não está entre os indicados.
* **Execução da ação**:
  * **Condição Verdadeira**: Se a atribuição de utilizador cumprir a condição (IS ou IS NOT), são acionadas as ações relevantes, como notificações, início de tarefas, aprovações ou outros passos do fluxo de trabalho.
  * **Condição Falsa**: Se a condição não for cumprida, o fluxo de trabalho não continuará.

**Interações do utilizador**

* **Configuração**: Os utilizadores configuram o cartão selecionando um operador e especificando os utilizadores relevantes a partir da User List. A configuração deve ser simples e intuitiva, de modo a acomodar seleções a partir de bases de utilizadores potencialmente extensas.
* **Monitorização e relatórios**: O sistema ERP deve disponibilizar funcionalidades para monitorizar e gerar relatórios sobre as operações acionadas por este cartão, oferecendo informações sobre a precisão das atribuições e a eficiência do processo.
* **Tratamento de erros e notificações**: Os utilizadores devem ter a opção de receber alertas ou notificações caso existam problemas com as atribuições, como tarefas não atribuídas ou erros na seleção de utilizadores.

#### Conclusão

O cartão de fluxo de trabalho "Assigned User Condition" é uma ferramenta crucial para gerir fluxos de documentos e tarefas que dependem de atribuições de utilizador. Ao permitir condições baseadas no facto de uma tarefa ou documento estar atribuído a utilizadores específicos, garante que os fluxos de trabalho só são acionados por interações de utilizador apropriadas, reforçando tanto a responsabilização como o alinhamento de tarefas dentro das equipas. Documentar este cartão com clareza ajudará os utilizadores a compreender a sua importância e a integrá-lo eficazmente nos seus fluxos de trabalho, assegurando operações fluidas e eficientes adaptadas aos papéis e responsabilidades dos utilizadores.

# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Create Task with Fallback"** assegura uma delegação de tarefas eficiente ao atribuir tarefas a funções específicas — dispatcher ou purchaser — incorporando ao mesmo tempo um mecanismo alternativo para evitar falhas na atribuição de tarefas. Este cartão melhora a fiabilidade e a adaptabilidade do fluxo de trabalho em cenários dinâmicos.

## **Componentes do cartão:**

1. **Title**
   * **Descrição**: Especifica o título da tarefa que está a ser criada.
   * **Detalhe**: Fornece um identificador conciso para a tarefa.
2. **Description**
   * **Descrição**: Descreve o propósito ou o contexto da tarefa.
   * **Detalhe**: Clarifica os detalhes da tarefa.
3. **Priority**
   * **Descrição**: Define o nível de urgência da tarefa.
   * **Opções**:
     * **High**: Exige atenção imediata.
     * **Medium**: Importante mas não urgente.
     * **Low**: Pode ser tratado posteriormente.
4. **Assigned Role**
   * **Descrição**: Especifica a função principal à qual a tarefa é atribuída.
   * **Opções**:
     * **Disponent**: Atribui a tarefa ao disponent.
     * **Purchaser**: Atribui a tarefa ao purchaser.
5. **Email Notification**
   * **Descrição**: Permite notificar o utilizador atribuído por e-mail.
   * **Opções**:
     * **True**: Envia uma notificação por e-mail ao utilizador.
     * **False**: Não é enviada qualquer notificação por e-mail.
6. **Fallback User**
   * **Descrição**: Fornece uma opção alternativa para a atribuição da tarefa caso a função de destinatário não seja encontrada.
   * **Detalhe**: Permite selecionar um utilizador a partir de uma lista pendente para assegurar a delegação da tarefa.

## **Funcionalidade:**

* **Avaliação da condição**:\
  O cartão só é executado se as condições nas secções **"Where"** e **"And Sections"** forem cumpridas.
* **Atribuição da tarefa**:
  * A tarefa é atribuída à função selecionada (dispatcher ou purchaser).
  * Se a função especificada não for encontrada, a tarefa é atribuída a um utilizador da lista pendente alternativa.
* **Notificação por e-mail**:\
  Envia um e-mail ao utilizador atribuído se a notificação por e-mail estiver ativada.

## **Configuração:**

1. **Especificar os detalhes da tarefa**: Introduza o título, a descrição e a prioridade da tarefa.
2. **Selecionar a função principal**: Escolha a função à qual a tarefa será atribuída (dispatcher ou purchaser).
3. **Configurar o Fallback User**: Selecione um utilizador alternativo a partir da lista pendente para assegurar a atribuição da tarefa caso a função principal não seja encontrada.
4. **Ativar a notificação por e-mail**: Indique se o utilizador atribuído deve receber uma notificação por e-mail.

## **Conclusão:**

O cartão de fluxo de trabalho **"Create Task with Fallback"** assegura uma delegação de tarefas transparente ao integrar um mecanismo alternativo. Ao atribuir tarefas com base em funções e ao fornecer uma opção de utilizador alternativo, melhora a fiabilidade e a flexibilidade nos processos de gestão de tarefas.

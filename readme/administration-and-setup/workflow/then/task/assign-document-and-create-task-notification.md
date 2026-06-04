# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito**

O cartão de fluxo de trabalho "**Assign Document and Create Task/Notification Based on Decision Table**" atribui um documento e cria uma tarefa ou notificação com detalhes configuráveis. O responsável é determinado pelo retorno de uma decision table, e o cartão permite definir prioridades e enviar notificações por e-mail.

## **Componentes do cartão**

1. **Assignee Type**
   * **Descrição:** Especifica se o retorno da decision table atribui o documento e a tarefa/notificação a um utilizador ou a um grupo.
   * **Detalhe:** Um campo para configurar o tipo de responsável como "User" ou "Group" com base no resultado da decision table.
2. **Task/Notification**
   * **Descrição:** Especifica o tipo de ação a criar para o responsável.
   * **Detalhe:** Uma lista pendente para selecionar "Task" ou "Notification" consoante as necessidades do fluxo de trabalho.
3. **Title**
   * **Descrição:** O título da tarefa ou notificação.
   * **Detalhe:** Um campo para fornecer um título conciso que identifica a tarefa ou notificação.
4. **Description**
   * **Descrição:** Detalhes adicionais sobre a tarefa ou notificação.
   * **Detalhe:** Um campo para descrever o propósito e o contexto da tarefa ou notificação.
5. **Priority**
   * **Descrição:** Define o nível de urgência da tarefa ou notificação.
   * **Opções:**
     * **High:** Exige atenção imediata.
     * **Medium:** Importante mas não urgente.
     * **Low:** Pode ser tratado posteriormente.
6. **Assignee Type**
   * **Descrição:** Este campo determina o tipo de responsável (User ou Group) ao qual o documento e a tarefa/notificação são atribuídos.
   * **Detalhe:** Um menu pendente para selecionar se a tarefa/notificação é atribuída a um utilizador ou a um grupo com base no resultado da decision table.
7. **Send Mail**
   * **Descrição:** Configura se é enviada uma notificação por e-mail ao responsável.
   * **Opções:**
     * **True:** Envia uma notificação por e-mail.
     * **False:** Não é enviada qualquer notificação por e-mail.
8. **Value**
   * **Descrição:** Define a prioridade numérica para a atribuição do documento.
   * **Detalhe:** Um campo para introduzir um valor numérico, em que números mais baixos indicam uma prioridade mais elevada.

## **Funcionalidade**

* **Avaliação da condição:**\
  O cartão só executa as suas ações se as condições do fluxo de trabalho forem cumpridas.
* **Avaliação da decision table:**\
  A decision table determina se o documento e a tarefa/notificação são atribuídos a um utilizador ou a um grupo.
* **Atribuição do documento e criação de tarefa/notificação:**\
  O documento é atribuído ao resultado da decision table. É criada uma tarefa ou notificação com o título, descrição e nível de prioridade especificados.
* **Notificação por e-mail:**\
  Se "Send Mail" estiver definido como True, é enviada uma notificação por e-mail ao responsável.

## **Configuração**

1. **Definir o Assignee Type:**
   * Configure o campo Assignee Type como "User" ou "Group" com base no resultado da decision table.
2. **Selecionar Task/Notification:**
   * Escolha "Task" ou "Notification" na lista pendente Task/Notification.
3. **Definir os detalhes da tarefa/notificação:**
   * Introduza o Title e a Description da tarefa ou notificação.
   * Selecione a Priority (High, Medium ou Low) na lista pendente.
4. **Ativar a notificação por e-mail:**
   * Defina a opção Send Mail como True ou False, consoante deva ser enviada uma notificação por e-mail.
5. **Definir a prioridade numérica:**
   * Introduza um valor numérico no campo Value para determinar a prioridade da atribuição, em que os números mais baixos são processados em primeiro lugar.
6. Guarde a configuração do cartão e ative o fluxo de trabalho.

## **Conclusão**

O cartão de fluxo de trabalho "Assign Document and Create Task/Notification Based on Decision Table" assegura que as tarefas ou notificações são atribuídas dinamicamente ao utilizador ou grupo adequado com base nos resultados da decision table. Este cartão facilita uma delegação de tarefas eficiente, prioridades personalizáveis e notificações por e-mail opcionais para melhorar a capacidade de resposta do fluxo de trabalho.

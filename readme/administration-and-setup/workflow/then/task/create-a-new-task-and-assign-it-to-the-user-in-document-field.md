# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Propósito:**

O cartão de fluxo de trabalho **"Create Field-Based Task or Notification"** é utilizado para criar tarefas ou notificações atribuídas dinamicamente a utilizadores identificados em campos de documento específicos. Este cartão oferece um mecanismo alternativo opcional para assegurar uma execução fluida do fluxo de trabalho mesmo quando o campo do documento não especifica um utilizador válido.

## **Componentes do cartão:**&#x20;

1. **Title**
   * **Descrição**: Especifica o título da tarefa ou notificação.
   * **Detalhe**: Utilizado para nomear e identificar a tarefa ou notificação que está a ser criada.
2. **Description**
   * **Descrição**: Fornece detalhes adicionais sobre a tarefa ou notificação.
   * **Detalhe**: Assegura que o destinatário compreende o propósito e o contexto da tarefa ou notificação.
3. **Priority**
   * **Descrição**: Define a urgência da tarefa ou notificação.
   * **Opções**:
     * **High**: Exige atenção imediata.
     * **Medium**: Importante mas menos urgente.
     * **Low**: Pode ser tratado posteriormente.
4. **Field Name**
   * **Descrição**: Especifica o campo do documento que será utilizado para atribuir a tarefa ou notificação.
   * **Detalhe**: O campo selecionado determinará dinamicamente o utilizador ao qual a tarefa ou notificação será atribuída. Se o campo estiver vazio ou for inválido, a tarefa ou notificação será atribuída ao utilizador alternativo selecionado na lista pendente.
5. **Email Notification**
   * **Descrição**: Configura se o utilizador atribuído é notificado por e-mail.
   * **Opções**:
     * **True**: Envia uma notificação por e-mail ao utilizador atribuído.
     * **False**: Não é enviada qualquer notificação por e-mail.
6. **Fallback User**
   * **Descrição**: Permite a seleção de um utilizador a partir de uma lista pendente para atribuir a tarefa ou notificação quando não é encontrado nenhum utilizador válido no campo do documento.
   * **Detalhe**: Assegura que a tarefa ou notificação é atribuída mesmo que o campo do documento esteja vazio ou seja inválido.

## **Componentes adicionais na Versão 3:**

1. **Notification Type**&#x20;
   * **Descrição**: Especifica se o cartão cria uma tarefa ou uma notificação.
   * **Opções**:
     * **Task**: Cria uma tarefa atribuída ao utilizador especificado.
     * **Notification**: Envia uma notificação em vez de criar uma tarefa.

## **Funcionalidade:**

* **Avaliação da condição**:\
  O cartão só executa a sua ação se tanto a secção **"Where"** como as **"And Sections"** forem avaliadas como verdadeiras.
* **Criação de tarefa ou notificação**:
  * Atribui a tarefa ou notificação ao utilizador identificado no campo do documento.
  * Na Versão 3, permite criar uma tarefa ou uma notificação.
* **Mecanismo alternativo**:\
  Se o campo do documento não identificar um utilizador válido, o cartão atribui a tarefa ou notificação ao utilizador alternativo selecionado na lista pendente.
* **Notificação por e-mail**:\
  Envia uma notificação por e-mail ao utilizador atribuído se assim for configurado.

## **Configuração:**

1. **Definir os detalhes da tarefa ou notificação**: Introduza o título, a descrição e a prioridade.
2. **Selecionar o campo do documento**: Escolha o campo que especifica o utilizador para a atribuição da tarefa ou notificação.
3. **Ativar a notificação por e-mail**: Especifique se deve ser enviada uma notificação por e-mail ao utilizador atribuído.
4. **Selecionar o Fallback User**: Escolha um utilizador alternativo a partir da lista pendente para a atribuição caso o campo do documento não identifique um utilizador válido.
5. **Especificar o Notification Type (Versão 3)**: Indique se o cartão cria uma tarefa ou uma notificação.

## **Conclusão:**

O cartão de fluxo de trabalho **"Create Field-Based Task or Notification"** simplifica a gestão de tarefas e notificações ao atribuir dinamicamente responsabilidades com base nos campos do documento. O seu mecanismo de utilizador alternativo e as opções melhoradas na Versão 3 proporcionam flexibilidade, assegurando que as tarefas ou notificações são sempre atribuídas, mesmo quando os dados do documento estão incompletos.

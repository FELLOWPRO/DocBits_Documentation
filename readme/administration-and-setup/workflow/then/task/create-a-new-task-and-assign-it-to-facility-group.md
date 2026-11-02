# Crie uma nova tarefa e atribua-a ao grupo da instalação

<figure><img src="../../../../.gitbook/assets/workflow_card_action_assign_task_to_facility_group_v2-pt-pt.png" alt="Crie uma nova tarefa e atribua-a ao grupo da instalação, Versão 2" width="634"><figcaption><p>Versão 2</p></figcaption></figure>

## Propósito:

Este cartão de fluxo de trabalho cria uma tarefa ou notificação para o grupo responsável pela instalação da ordem de compra do documento. A instalação não é selecionada no cartão: é obtida a partir das ordens de compra com as quais o documento está associado. Em seguida, o cartão procura um grupo de utilizadores cujo nome contenha tanto o nome de grupo introduzido no cartão como o código da instalação, e cria a tarefa para esse grupo. O documento propriamente dito não é reatribuído.

Para um cartão que também atribui o documento ao grupo da instalação no âmbito de uma atribuição sequencial, pode ser utilizado **Assign to Facility Group and Create a Task/Notification**.

## Componentes do cartão:

1. **Tarefa/Notificação**
   * **Descrição:** Define se é criada uma tarefa ou uma notificação para o grupo.
   * **Opções:**
     * **Tarefa:** É criada uma tarefa.
     * **Notificação:** É criada uma notificação.
2. **Nome do grupo**
   * **Descrição:** A parte do nome que os grupos de instalações têm em comum.
   * **Detalhe:** Um texto que é comparado com os nomes dos grupos de utilizadores da organização. Um grupo corresponde se o seu nome contiver este texto e o código da instalação da ordem de compra. A comparação não distingue maiúsculas de minúsculas. Por exemplo, com o nome de grupo **Warehouse** e uma ordem de compra para a instalação **1000**, corresponderia um grupo chamado **Warehouse 1000**.
3. **Título**
   * **Descrição:** O título da tarefa ou notificação.
   * **Detalhe:** Um texto curto que identifica a tarefa ou notificação.
4. **Descrição**
   * **Descrição:** Mais detalhes sobre a tarefa ou notificação.
   * **Detalhe:** Um texto que descreve o que deverá ser feito ou por que motivo o grupo é informado.
5. **Prioridade**
   * **Descrição:** A urgência da tarefa ou notificação.
   * **Opções:**
     * **peso elevado:** A tarefa ou notificação é criada com prioridade elevada.
     * **peso médio:** A tarefa ou notificação é criada com prioridade média.
     * **baixo peso:** A tarefa ou notificação é criada com prioridade baixa.
6. **Enviar e-mail**
   * **Descrição:** Define se o grupo é também informado por e-mail sobre a tarefa.
   * **Opções:**
     * **Verdadeiro:** É enviada uma notificação por e-mail ao grupo.
     * **Falso:** Não é enviada qualquer notificação por e-mail.

## Funcionalidade:

* **Determinação da instalação:** O cartão lê as ordens de compra com as quais o documento está associado e recolhe o código da instalação (a localização da ordem de compra) de cada uma delas.
* **Determinação do grupo:** Para cada código de instalação, o cartão procura grupos de utilizadores cujo nome contenha tanto o **Nome do grupo** indicado no cartão como o código da instalação. Os códigos de instalação para os quais não é encontrado nenhum grupo são listados no registo do fluxo de trabalho.
* **Criação da tarefa:** É criada para o grupo correspondente uma tarefa ou notificação com o título, a descrição e a prioridade do cartão, associada ao documento. Se vários grupos corresponderem, a tarefa é criada para apenas um deles; o cartão não determina qual.
* **Valores predefinidos:** Se não for definida nenhuma prioridade, é utilizado **peso médio**. Se **Enviar e-mail** não estiver definido, não é enviado nenhum e-mail. Se **Tarefa/Notificação** não estiver definido, é criada uma tarefa e o registo do fluxo de trabalho indica a definição em falta.
* **Dados em falta:**
  * Se o nome do grupo, o título ou a descrição estiverem vazios, o cartão não é executado e regista os dados em falta no registo do fluxo de trabalho.
  * Se o documento não estiver associado a uma ordem de compra, o cartão regista os dados em falta em vez de criar uma tarefa.
  * Se nenhum grupo corresponder a qualquer dos códigos de instalação, não é criada nenhuma tarefa e o registo do fluxo de trabalho indica que não foi encontrado nenhum grupo correspondente.

## Configuração:

* Os grupos de utilizadores deverão ser nomeados de forma a que cada nome contenha a parte comum do nome e o código da instalação, por exemplo **Warehouse 1000**, **Warehouse 2000**.
* O cartão pode ser adicionado a partir da categoria **Tarefa**. Em seguida, podem ser configurados o tipo (**Tarefa** ou **Notificação**), a parte comum do nome dos grupos, o título, a descrição, a prioridade e a definição de e-mail.

## Conclusão:

O cartão de fluxo de trabalho "Create a New Task and assign it to Facility Group" envolve no processo a equipa da instalação certa sem alterar a quem o documento está atribuído. Um único cartão abrange todas as instalações, desde que os grupos de utilizadores sigam um esquema de nomes consistente, com o código da instalação no nome.

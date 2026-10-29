# Tarefas e Notificações

### Visão geral

A configuração **Tarefas e Notificações** (Tasks & Notifications) ativa o gerenciamento de tarefas integrado do DocBits. Quando ativada, os membros da equipe podem criar tarefas, atribuir documentos uns aos outros (por exemplo, para validação, correção ou aprovação) e receber notificações sobre eles.

Esta configuração está **desativada por padrão**. Quando ativada, mais quatro opções aparecem abaixo dela:

* **Contagem de tarefas do painel**: mostra no painel quais documentos têm tarefas em aberto.
* **Permitir filtro "Todos" para usuários não administradores**: permite que usuários que não são administradores vejam todas as tarefas.
* **Exclusão de tarefas não administrativas**: define quais tarefas os usuários que não são administradores podem excluir.
* **Conclusão de tarefas não administrativas**: define quais tarefas os usuários que não são administradores podem encerrar.

Os administradores da organização nunca são restringidos por essas opções.

### O que faz?

* **Ativada** — Os recursos de Tarefas e Notificações ficam disponíveis no DocBits. Os usuários podem atribuir tarefas, acompanhar o status e ser notificados quando algo exigir sua atenção.
* **Desativada** — A atribuição de tarefas e as notificações relacionadas ficam desativadas. Desativá-la também desativa a **Contagem de tarefas do painel**.

### Contagem de tarefas do painel

A **Contagem de tarefas do painel** (Dashboard Tasks Count) controla se o painel mostra quais documentos têm tarefas em aberto.

* **Ativada** — Um documento com tarefas no status **Aberto** ou **Em andamento** exibe um ícone de tarefa na lista do painel. Ao passar o mouse sobre o ícone, é exibido quantas tarefas em aberto o documento tem, por exemplo "2 Tarefa(s) aberta(s)". Tarefas concluídas, rejeitadas ou excluídas não são contadas.
* **Desativada** — O ícone fica oculto. As tarefas continuam funcionando normalmente.

{% hint style="info" %}
A **Contagem de tarefas do painel** depende de **Tarefas e Notificações**. Se você desativar Tarefas e Notificações, a contagem de tarefas também será desativada.
{% endhint %}

### Permitir filtro "Todos" para usuários não administradores

A visão geral de tarefas tem um filtro **Atribuído a** com as opções **Todos** e **Atribuído a mim**. Os administradores sempre têm as duas opções.

* **Ativada** — Usuários que não são administradores também podem escolher **Todos** e ver todas as tarefas da organização.
* **Desativada** (padrão) — Usuários que não são administradores têm apenas **Atribuído a mim**, de modo que a visão geral mostra as tarefas atribuídas a eles.

### Exclusão de tarefas não administrativas

Apesar do nome exibido no aplicativo, a opção **Exclusão de tarefas não administrativas** não se refere a um tipo de tarefa: ela define quais tarefas e notificações os **usuários que não são administradores** podem excluir. Os administradores sempre podem excluir todas as tarefas.

| Opção | Usuários que não são administradores podem excluir |
| --- | --- |
| **Nenhum** | Nenhuma tarefa. |
| **Somente tarefas criadas** | As tarefas que eles mesmos criaram. |
| **Criou e atribuiu tarefas** | As tarefas que eles criaram e as tarefas atribuídas a eles ou a um de seus grupos. É o comportamento aplicado enquanto a opção nunca tiver sido alterada. |
| **Todas as tarefas** | Todas as tarefas. |

Os usuários sempre podem excluir as tarefas que criaram, exceto com **Nenhum**. Por isso, uma tarefa que não está atribuída a ninguém só pode ser excluída pelo usuário que a criou, por administradores ou com **Todas as tarefas**. Uma tarefa sem criador registrado, por exemplo uma criada pelo sistema, só pode ser excluída pelos usuários aos quais está atribuída (com **Criou e atribuiu tarefas**), por administradores ou com **Todas as tarefas**.

{% hint style="warning" %}
Excluir uma tarefa a remove da lista de tarefas sem uma decisão. Se as tarefas só puderem ser encerradas por meio de uma decisão, configure a **Exclusão de tarefas não administrativas** como **Nenhum** e a **Conclusão de tarefas não administrativas** (veja abaixo) como **Apenas para administradores**.
{% endhint %}

### Conclusão de tarefas não administrativas

Apesar do nome exibido no aplicativo, a opção **Conclusão de tarefas não administrativas** não se refere a um tipo de tarefa: ela define quais **usuários que não são administradores** podem encerrar uma tarefa, ou seja, defini-la como **Feito** ou **Rejeitado**. Os administradores sempre podem encerrar tarefas, independentemente do que for selecionado aqui.

| Opção | Quem pode encerrar uma tarefa |
| --- | --- |
| **Comportamento padrão** | A configuração não acrescenta nenhuma restrição. Os usuários podem encerrar as tarefas atribuídas a eles ou a um de seus grupos, como antes da existência desta configuração. É o comportamento aplicado enquanto a opção nunca tiver sido alterada. |
| **Administradores e usuários atribuídos** | Os administradores e os usuários aos quais a tarefa está atribuída, diretamente ou por meio de um de seus grupos. Uma tarefa atribuída a outra pessoa, ou a ninguém, não pode ser encerrada por outros usuários. O DocBits também verifica isso quando uma tarefa é alterada pela API. |
| **Apenas para administradores** | Somente os administradores. |

Com **Administradores e usuários atribuídos** ou **Apenas para administradores**, um usuário que não pode encerrar uma tarefa:

* não vê o botão verde **Feito** na página da tarefa, e a lista de status oferece apenas **Aberto** e **Em andamento**;
* não pode clicar no círculo de status da tarefa no painel de tarefas do documento. Ao passar o mouse sobre ele, é exibida a mensagem "Você não tem permissão para marcar esta tarefa como concluída ou rejeitada.";
* não vê **Marcar como concluído** para essa tarefa na lista de tarefas, e **Marcar como concluído** para uma seleção fica oculto enquanto uma tarefa desse tipo estiver selecionada;
* não pode arrastar a tarefa para a coluna **Feito** ou **Rejeitado** do quadro de tarefas. O cartão volta para sua coluna e a mesma mensagem é exibida.

A configuração restringe apenas o encerramento. Os usuários mantêm todos os outros direitos que tinham antes: os usuários aos quais uma tarefa está atribuída ainda podem editá-la, salvá-la, movê-la entre **Aberto** e **Em andamento** e reabri-la depois de concluída. Os usuários aos quais uma tarefa não está atribuída não podiam alterar o status dela antes, e continuam sem poder.

Para tipos de documento com **Histórico de aprovação** ativado, **Aprovar** continua concluindo tarefas em aberto do documento, independentemente do que for selecionado aqui: as tarefas atribuídas ao aprovador ou a um de seus grupos e as tarefas não atribuídas a ninguém. Se o aprovador for administrador, todas as tarefas em aberto do documento são concluídas.

#### Tarefas em documentos devolvidos para validação

Como os usuários não podem encerrar suas próprias tarefas com **Administradores e usuários atribuídos** ou **Apenas para administradores**, o próprio DocBits encerra as tarefas em aberto de um documento quando um documento aguardando aprovação é devolvido para validação:

* **Reiniciar o fluxo de trabalho** na tela de aprovação: todas as tarefas em aberto do documento são rejeitadas.
* **Rejeitar e corrigir**: todas as tarefas em aberto do documento são rejeitadas.
* **Aprovar e corrigir**: as tarefas que **Aprovar** concluiria (veja acima) são concluídas, somente para tipos de documento com **Histórico de aprovação** ativado. Todas as demais tarefas em aberto são rejeitadas.

As tarefas em aberto são encerradas antes de o documento voltar para a validação. Os fluxos de trabalho executados na mudança de status podem então criar novas tarefas para o que ainda precisar de atenção.

Com **Comportamento padrão**, as tarefas em aberto permanecem abertas quando um documento é devolvido, como antes.

### Benefícios

* **Responsabilidades claras**: Os documentos podem ser atribuídos à pessoa certa em vez de depender de e-mail.
* **Nada é esquecido**: As notificações lembram os usuários sobre documentos que exigem sua ação.
* **Trabalho em aberto rapidamente visível**: Com a Contagem de tarefas do painel, o painel mostra quais documentos ainda têm tarefas em aberto.
* **Decisões rastreáveis**: Com as opções de exclusão e conclusão, as tarefas só saem da fila por meio de uma decisão ou de um administrador.

### Como usar

1. Vá para **Configurações**.
2. Selecione **Processamento de documentos**.
3. Selecione **Módulo**.
4. Abra a seção **Tipo de documento**.
5. Ative **Tarefas e Notificações**.
6. (Opcional) Ative **Contagem de tarefas do painel** para exibir o ícone de tarefa no painel.
7. (Opcional) Ative **Permitir filtro "Todos" para usuários não administradores** se todos os usuários devem ver todas as tarefas.
8. (Opcional) Escolha em **Exclusão de tarefas não administrativas** quais tarefas os usuários podem excluir.
9. (Opcional) Escolha em **Conclusão de tarefas não administrativas** quem pode encerrar tarefas.

As opções de exclusão e conclusão são salvas assim que você escolhe um valor.

### Quando usar este recurso

* **Equipes que compartilham o trabalho com documentos**: Ative quando várias pessoas validam ou aprovam documentos e precisam repassar o trabalho entre si.
* **Visibilidade da carga de trabalho**: Ative também a Contagem de tarefas do painel quando a equipe precisar ver no painel quais documentos ainda têm tarefas em aberto.
* **Tarefas que só um administrador ou uma decisão devem encerrar**: Defina **Conclusão de tarefas não administrativas** como **Apenas para administradores** ou **Administradores e usuários atribuídos**, e **Exclusão de tarefas não administrativas** como **Nenhum**, quando os usuários não puderem remover tarefas que não foram realmente realizadas.
* **Configurações de usuário único ou totalmente automatizadas**: Você pode deixar desativado se ninguém precisar atribuir documentos ou acompanhar tarefas.

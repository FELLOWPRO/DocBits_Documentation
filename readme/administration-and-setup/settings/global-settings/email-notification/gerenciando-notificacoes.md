# Gerenciando Notificações

Abra **Configurações → Notificação Por E-Mail** para ver as regras da sua organização. Uma regra liga um status de documento a um modelo de e-mail e a um destinatário. O exemplo abaixo usa uma regra de demonstração para faturas e permanece **inativa** na Sandbox do DocBits.

As imagens mostram a interface Sandbox com dados de demonstração controlados. Elas não comprovam o salvamento nem o envio de uma notificação real.

## Exemplo: uma fatura está pronta para validação

Antes de criar uma regra, prepare um modelo de e-mail para **Fatura** (Invoice) em **Configurações → Modelos de e-mail**. Neste exemplo, o modelo se chama **Docs Demo Invoice Notification**. O modelo fornece o assunto e a mensagem do e-mail.

1. Selecione **Novo** na página **Notificação Por E-Mail**.
2. Digite **Docs Demo Invoice Validation** como nome, selecione **Fatura** (Invoice) como tipo de documento e escolha o modelo de e-mail preparado.
3. Escolha **Pronto para validação** (Ready for validation) como status e **Médio** como prioridade. Defina **Unidade de tempo** como **MINUTOS** e **Atraso** como **10**. O atraso mínimo em minutos é de cinco.
4. Selecione **Enviar e-mail para usuário/grupo atribuído**. Ative **Não repita** se a mensagem deve ser enviada apenas uma vez. Revise o destinatário e o momento do envio e selecione **Salvar**.

<figure><img src="../../../../.gitbook/assets/dbdc645-notifications-form-pt-20261011-corrected.png" alt="Regra de notificação preenchida para Invoice, com atraso de dez minutos e envio ao usuário ou grupo atribuído"><figcaption><p>A regra de demonstração aberta para edição. Os valores controlados mostram quando e para quem a notificação seria enviada.</p></figcaption></figure>

A regra agora aparece na lista. O exemplo da documentação foi desativado depois, então seu menu **Actions** oferece **Ativar**; uma regra ativa oferece **Desativar**. Verifique o nome, o tipo de documento, o status, o atraso e o destinatário na sua própria lista antes de ativar uma regra.

<figure><img src="../../../../.gitbook/assets/dbdc645-notifications-list-pt-20261011-corrected.png" alt="Lista de Notificação Por E-Mail com a regra de exemplo no lugar de uma tabela vazia"><figcaption><p>O detalhe da lista mostra Docs Demo Invoice Validation, o tipo Fatura e o estado Inativo. O atraso e o destinatário aparecem no formulário acima.</p></figcaption></figure>

## Editar, ativar ou excluir uma regra

Abra o menu **Actions** da linha. **Editar** abre a regra com seus valores atuais. **Ativar** habilita este exemplo inativo; uma regra ativa oferece **Desativar** em vez disso. **Registros** abre o histórico de notificações da regra. **Excluir** remove a regra após a confirmação. Verifique os destinatários e o momento do envio antes de ativar ou alterar uma regra.

<figure><img src="../../../../.gitbook/assets/dbdc645-notifications-actions-pt-20261011-corrected.png" alt="Menu Actions da regra de exemplo inativa com Editar, Ativar, Registros e Excluir"><figcaption><p>O detalhe mostra o menu da mesma regra inativa. A coluna Nome foi arrastada para junto de Actions para tornar o nome e as ações legíveis. A regra inativa oferece Ativar; uma regra ativa oferece Desativar.</p></figcaption></figure>

Se a lista mostrar **No Record Found!**, crie uma regra primeiro. Se a lista de **Tipo de documento** ou de modelos de e-mail estiver vazia, configure um tipo de documento ativo e um modelo correspondente antes de voltar a este formulário.

Para mais informações sobre a configuração inicial, consulte [Configurando Notificações](configurando-notificacoes.md). Se os e-mails não chegarem como esperado, consulte [Solução de Problemas](solucao-de-problemas.md).

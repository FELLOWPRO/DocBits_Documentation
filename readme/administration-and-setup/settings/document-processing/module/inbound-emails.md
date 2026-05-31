# E-mails recebidos

### Visão geral

O DocBits pode buscar documentos diretamente do e-mail — sem upload manual. Há **duas formas** de trazer documentos por e-mail, ambas em **Configurações → Processamento de Documentos → Importar**:

| Método | Como funciona | Ideal para |
|--------|---------------|------------|
| **Conta de importação de e-mail** | O DocBits se conecta a uma caixa de correio sua (**IMAP**, **OAuth Office365** ou **OAuth Office365 – Tenant**) e importa os documentos que encontra. | Uma caixa dedicada que já recebe seus documentos (p. ex. `faturas@suaempresa.com`). |
| **E-mails encaminhados (E-mails recebidos)** | O DocBits fornece um endereço exclusivo; qualquer remetente autorizado pode **encaminhar** documentos para ele. | Encaminhamento pontual de muitos remetentes sem compartilhar credenciais da caixa. |

Você pode usar cada método separadamente ou ambos juntos.

### Método 1 — Conectar uma caixa de correio (Importação de e-mail)

Vá para **Configurações → Processamento de Documentos → Importar** e abra a seção **Importação de e-mail**. Clique em **Novo** para adicionar uma conexão de caixa de correio.

<figure><img src="../../../../.gitbook/assets/inbound_emails_email_import_entry.png" alt="Seção Importação de e-mail com o botão Novo"><figcaption><p>Na seção Importação de e-mail, clique em <strong>Novo</strong> para conectar uma caixa de correio.</p></figcaption></figure>

O assistente de configuração abre. O primeiro campo, **Protocolo**, determina como o DocBits se conecta — escolha **IMAP**, **OAuth Office365** ou **OAuth Office365 – Tenant**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_protocol_select.png" alt="Lista suspensa Protocolo com IMAP, OAuth Office365 e OAuth Office365 - Tenant"><figcaption><p>A lista <strong>Protocolo</strong> oferece os três tipos de conexão.</p></figcaption></figure>

#### IMAP

Para uma caixa padrão, escolha **IMAP** e preencha os dados do servidor e as credenciais da conta:

* **Nome do servidor** e **Porta** (padrão `993`) do seu servidor de e-mail.
* **Criptografia** — `SSL`, `TLS` ou `None`.
* **Nome de usuário**, **e-mail** e **senha** da caixa.

<figure><img src="../../../../.gitbook/assets/inbound_emails_imap.png" alt="Formulário de conexão IMAP com servidor, porta, criptografia e credenciais"><figcaption><p>O formulário IMAP: a conexão com o servidor de e-mail mais as credenciais da caixa.</p></figcaption></figure>

#### OAuth Office365

Para uma única caixa de usuário do Microsoft 365, escolha **OAuth Office365**. Em vez de uma senha, você autoriza o DocBits pela Microsoft: escolha o destino do **Roteamento de documentos**, depois clique em **Autenticar** e conclua o login da Microsoft.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365.png" alt="Formulário OAuth Office365 com Roteamento de documentos e um botão Autenticar"><figcaption><p>O OAuth Office365 conecta-se pelo login da Microsoft — nenhuma senha é armazenada no DocBits.</p></figcaption></figure>

#### OAuth Office365 – Tenant

Para conectar no nível do locatário (organização) por meio de um registro de aplicativo do Azure, escolha **OAuth Office365 – Tenant** e insira as credenciais do Azure: **ID do locatário** (Tenant ID), **ID do aplicativo cliente** (Client App ID) e **Valor do aplicativo cliente** (segredo do cliente). Use **Testar conexão** para verificar e depois **Salvar**.

<figure><img src="../../../../.gitbook/assets/inbound_emails_o365_tenant.png" alt="Configuração do locatário do Azure com ID do locatário, ID do aplicativo cliente e Valor do aplicativo cliente"><figcaption><p>O OAuth Office365 – Tenant usa um registro de aplicativo do Azure (ID do locatário, ID do aplicativo cliente, segredo do cliente).</p></figcaption></figure>

{% hint style="info" %}
O **Roteamento de documentos** decide para onde vão os documentos importados — **DocBits** (o painel padrão) ou **AI Workforce**. Após conectar, as próximas etapas do assistente permitem escolher de qual **pasta** importar, uma **caixa compartilhada** opcional e se os e-mails processados devem ser **movidos** para outra pasta.
{% endhint %}

### Método 2 — Encaminhar e-mails para o DocBits (E-mails recebidos)

Este método requer que o módulo **E-mails recebidos** esteja ativado primeiro. Vá para **Configurações → Processamento de Documentos → Módulo**, abra a seção **Tipo de Documento**, encontre **E-mails recebidos** e ative o botão.

<figure><img src="../../../../.gitbook/assets/inbound_emails_1.png" alt="Ativando o módulo E-mails recebidos"><figcaption><p>Ative <strong>E-mails recebidos</strong> em Configurações → Processamento de Documentos → Módulo.</p></figcaption></figure>

Uma vez ativado, uma seção **E-mails recebidos** aparece em **Configurações → Processamento de Documentos → Importar**. Ela contém tudo o que é necessário para receber documentos encaminhados:

<figure><img src="../../../../.gitbook/assets/inbound_emails_forward.png" alt="Seção E-mails recebidos: endereço de importação, remetentes predefinidos e endereço de notificação de falha"><figcaption><p>A seção E-mails recebidos: seu endereço de importação, a lista de remetentes predefinidos e o endereço de notificação de falhas.</p></figcaption></figure>

* **Endereço de importação** — um endereço exclusivo gerado pelo sistema no formato `org_id@environment.inbound.docbits.com`. Encaminhe ou envie documentos para este endereço e o DocBits os importa automaticamente. Use o ícone de copiar para obtê-lo.
* **Importar documentos apenas de e-mails predefinidos** — quando ativado, somente os endereços de remetente listados aqui são aceitos; e-mails de qualquer outro são ignorados. Para cada remetente, você pode escolher uma **Suborganização** (deixe vazio para atribuir à organização principal). Use **Adicionar** para listar mais remetentes e **Excluir** para remover um.
* **Responder a este e-mail se a importação não puder ser feita** — quando ativado, insira um endereço a ser notificado sempre que uma tentativa de importação falhar, para que os problemas não passem despercebidos.

Clique em **Salvar** para aplicar suas alterações.

### Quando usar cada método

* **Use uma conta de importação de e-mail** quando os documentos já chegam a uma caixa dedicada e você quer que o DocBits os busque sozinho — IMAP para servidores de e-mail genéricos, OAuth Office365 para Microsoft 365.
* **Use e-mails encaminhados** quando as pessoas devem encaminhar documentos sob demanda, ou quando você não quer compartilhar as credenciais da caixa com o DocBits.
* **Combine ambos** se alguns documentos chegam a uma caixa fixa enquanto outros são encaminhados pontualmente.

{% hint style="info" %}
Restringir os remetentes (Método 2) e escolher o destino correto do **Roteamento de documentos** (Método 1) são as duas formas mais comuns de manter um fluxo de entrada limpo — apenas os documentos que você espera, direcionados para onde você quer.
{% endhint %}

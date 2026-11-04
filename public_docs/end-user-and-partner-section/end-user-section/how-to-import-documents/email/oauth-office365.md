# OAuth Office365

{% embed url="https://youtu.be/Vvy38N_5g3Y" %}

Aqui você só precisa inserir a sub-organização desejada e pressionar **Autenticar**

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-authenticate-pt-20261009.png" alt="Janela »Configuração do servidor de e-mail« com o protocolo OAuth Office365, o roteamento de documentos e o botão »Autenticar«."><figcaption><p>Escolha o roteamento e pressione Autenticar.</p></figcaption></figure>

Você será levado a esta página da Microsoft e precisará inserir um código.

![](https://lh7-us.googleusercontent.com/Q76mIMXr5bWCrcu_6TOKDrh6yQIMESIrFvEcfvqg7mJp-K_4ES2e5ekPY4Ghhwxym-uRKz_QVCHyqk2u5onyoCCmg7fMbt3mnIUyCrc8XT4jBGn9ueEYij3DRg1-oODWHd-vDfM9FfbU3omF6RJJKsE)

Este código pode ser encontrado voltando ao DocBits — o código será exibido lá como abaixo. Basta copiar o código e inseri-lo na página da Microsoft. Depois disso, você precisará inserir as suas próprias credenciais da Microsoft.

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-code-pt-20261009.png" alt="Janela »Configuração do servidor de e-mail« com o código de autenticação da Microsoft, o botão »Cópia« e o botão »Concluir autenticação«."><figcaption><p>O código da Microsoft é exibido no DocBits.</p></figcaption></figure>

Pressione o botão **Concluir autenticação** e você será levado a este menu

<figure><img src="../../../../.gitbook/assets/a-email-oauth-office365-options-pt-20261009.png" alt="Janela »Configuração do servidor de e-mail« após a autenticação, com as opções »Usar pasta«, »Usar caixa de correio compartilhada« e »Mover e-mails para outra pasta«."><figcaption><p>Opções após a conclusão da autenticação.</p></figcaption></figure>

**Usar pasta**

Se você estiver usando uma pasta diferente da sua caixa de entrada, insira o nome da pasta após ativar a opção.

**Usar caixa de correio compartilhada**

Se você quiser que a importação de e-mails acesse uma caixa de entrada ou uma pasta de uma caixa de correio compartilhada, insira aqui o endereço de e-mail após ativar a opção.

**Mover e-mails importados para a lixeira**

(Na janela, a opção chama-se **Mover e-mails para outra pasta**.)

Se você quiser importar todos os e-mails — e não apenas os não lidos — e movê-los para outra pasta (por exemplo, a lixeira), ative esta opção. Caso contrário, serão verificados apenas os e-mails não lidos: os documentos são importados, o e-mail é marcado como lido e permanece no seu local. Essa mesma opção é descrita na página [Importar](../../../../administration-and-setup/settings/document-processing/import.md).

Caso você receba uma mensagem de erro indicando que não tem permissões para estabelecer essa conexão, alguém com permissões de administrador no Azure precisará autorizar essa conexão. Para mais informações, visite a seguinte página: [https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps](https://learn.microsoft.com/en-us/entra/identity/enterprise-apps/grant-admin-consent?pivots=portal#grant-tenant-wide-admin-consent-in-enterprise-apps)

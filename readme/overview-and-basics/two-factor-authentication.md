# Autenticação de Dois Fatores (2FA)

## Visão geral

A Autenticação de Dois Fatores (2FA) adiciona uma segunda etapa ao seu login. Depois da sua senha, o DocBits solicita um segundo fator que só você possui — um código de um aplicativo autenticador, um código enviado para você por e-mail ou uma chave de acesso (Touch ID, Windows Hello, YubiKey, 1Password). Mesmo que alguém descubra a sua senha, não poderá entrar sem esse segundo fator.

A 2FA é **opcional para cada usuário** e pode ser **exigida pelo administrador da sua organização**. Os logins com Single Sign-On (SSO) (Google, Microsoft, SAML) estão isentos — o seu provedor de identidade já aplica o próprio MFA.

Você pode cadastrar mais de um método. Os métodos que o DocBits suporta são:

* **Aplicativo autenticador (TOTP)** — Google Authenticator, Microsoft Authenticator, 1Password, Authy, etc.
* **Código por e-mail** — um código de 6 dígitos enviado para o e-mail da sua conta.
* **Chave de acesso (WebAuthn/FIDO2)** — Touch ID, Windows Hello, uma chave de hardware (YubiKey) ou um gerenciador de senhas.

Ao ativar o seu primeiro fator, o DocBits também fornece **dez códigos de backup** para usar caso você perca o acesso ao seu método.

## Onde encontrar

Abra as suas **configurações de perfil / conta** (menu da conta no canto superior direito → **Editar perfil**) e selecione **Autenticação de dois fatores**. A caixa de diálogo de 2FA mostra o seu status atual e os métodos que você pode adicionar.

<figure><img src="../.gitbook/assets/mfa-2fa-dialog.png" alt="The Two-factor authentication dialog"><figcaption><p>A caixa de diálogo de Autenticação de dois fatores. A partir daqui você pode ativar um aplicativo autenticador, a verificação por e-mail, adicionar uma chave de acesso ou abrir <strong>Gerenciar</strong>.</p></figcaption></figure>

## Configurar um aplicativo autenticador (TOTP)

1. Na caixa de diálogo de 2FA, clique em **Ativar 2FA**.
2. Escaneie o código QR com o seu aplicativo autenticador (Google Authenticator, 1Password, Authy, …). Se não conseguir escanear, use a **chave manual** exibida abaixo do código QR.
3. Digite o código de 6 dígitos exibido pelo seu aplicativo e confirme.
4. O DocBits ativa a 2FA e exibe os seus **códigos de backup** (veja abaixo).

<figure><img src="../.gitbook/assets/mfa-totp-setup.png" alt="The authenticator-app setup screen with QR code"><figcaption><p>Escaneie o código QR com o seu aplicativo autenticador ou digite a chave manual. Em seguida, confirme com o código de 6 dígitos exibido pelo aplicativo.</p></figcaption></figure>

## Configurar a verificação por e-mail

1. Na caixa de diálogo de 2FA, clique em **Ativar verificação por e-mail**.
2. O DocBits envia um código de 6 dígitos por e-mail para o endereço da sua conta.
3. Digite o código para confirmar. A verificação por e-mail agora está ativada.

## Adicionar uma chave de acesso

1. Na caixa de diálogo de 2FA, clique em **Adicionar uma chave de acesso**.
2. O seu navegador ou dispositivo solicita a confirmação com Touch ID, Windows Hello, uma chave de hardware ou o seu gerenciador de senhas.
3. A chave de acesso é salva. Você pode adicionar várias chaves de acesso e renomeá-las ou removê-las posteriormente.

## Códigos de backup

Ao ativar o seu **primeiro** fator, o DocBits exibe **dez códigos de backup** — **uma única vez**. Cada código funciona apenas uma vez e permite que você entre caso perca o seu autenticador ou telefone.

* Guarde-os em um lugar seguro (um gerenciador de senhas é ideal).
* Você pode gerar um novo conjunto a qualquer momento com **Regenerar códigos de backup** (isso invalida o conjunto antigo).

<figure><img src="../.gitbook/assets/mfa-backup-codes.png" alt="The backup codes screen"><figcaption><p>Os seus dez códigos de backup, exibidos uma única vez. Cada um funciona apenas uma vez — guarde-os em um lugar seguro.</p></figcaption></figure>

{% hint style="warning" %}
Os códigos de backup são exibidos apenas no momento em que são gerados. O DocBits não pode exibi-los novamente — guarde-os imediatamente.
{% endhint %}

## Entrar com 2FA

1. Digite o seu e-mail e senha normalmente.

    <figure><img src="../.gitbook/assets/mfa-login.png" alt="The DocBits login screen"><figcaption><p>A tela de login. Você também pode entrar sem senha usando <strong>Entrar com uma chave de acesso</strong>.</p></figcaption></figure>
2. O DocBits solicita o seu segundo fator. Escolha o seu método:
   * **Autenticador** — digite o código atual de 6 dígitos do seu aplicativo.
   * **E-mail** — clique em **Enviar um código por e-mail** para receber um código por e-mail e, em seguida, digite-o.
   * **Chave de acesso** — clique em **Usar uma chave de acesso** e confirme com Touch ID / Windows Hello / a sua chave.
   * **Código de backup** — caso você não possa usar o seu método habitual.

    <figure><img src="../.gitbook/assets/mfa-challenge.png" alt="The second-factor challenge screen"><figcaption><p>Depois da sua senha, o DocBits solicita o seu segundo fator. Troque de método com <strong>Usar uma chave de acesso</strong> ou <strong>Enviar um código por e-mail</strong> e, opcionalmente, confie no dispositivo por 30 dias.</p></figcaption></figure>
3. Se tudo der certo, você estará conectado.

### Como é o código por e-mail

Se você escolher **E-mail**, o DocBits envia uma mensagem com um código de 6 dígitos que expira em 10 minutos:

<figure><img src="../.gitbook/assets/mfa-email-otp.png" alt="The DocBits verification-code email"><figcaption><p>O e-mail com o código de verificação. O código expira após 10 minutos e pode ser usado uma vez.</p></figcaption></figure>

## Confiar neste dispositivo

Na tela do segundo fator, você pode marcar **Lembrar deste dispositivo**. O DocBits então ignora a etapa de 2FA nesse dispositivo por **30 dias**. A confiança é removida automaticamente quando você altera a sua senha, e você pode revogá-la a qualquer momento (veja abaixo).

## Gerenciar as suas chaves de acesso e dispositivos confiáveis

Abra a caixa de diálogo de 2FA e clique em **Gerenciar** para revisar o que está cadastrado.

* **Chaves de acesso** — renomeie uma chave de acesso (clique no nome dela) ou exclua-a. Excluir o seu último fator restante desativa a 2FA.
* **Dispositivos confiáveis** — revogue um único dispositivo ou use **Revogar todos os dispositivos** para forçar uma nova solicitação de 2FA em todos os lugares.

<figure><img src="../.gitbook/assets/mfa-passkeys-list.png" alt="Managing enrolled passkeys and trusted devices"><figcaption><p>A visão Gerenciar lista as suas chaves de acesso cadastradas e os dispositivos confiáveis, onde você pode renomeá-los ou removê-los.</p></figcaption></figure>

## Desativar a 2FA

Na caixa de diálogo de 2FA, clique em **Desativar 2FA** e confirme com um código atual do autenticador ou um código de backup. Desativar a 2FA também apaga os seus códigos de backup e revoga os seus dispositivos confiáveis.

{% hint style="info" %}
Se a sua organização **exige** MFA, você não poderá entrar com uma senha até que pelo menos um fator esteja configurado. Pergunte ao seu administrador se não tiver certeza se o MFA é obrigatório para a sua organização.
{% endhint %}

## Login sem senha (opcional)

Depois de ter uma chave de acesso, você pode entrar **sem digitar a sua senha** usando **Entrar com uma chave de acesso** na tela de login. A sua senha continua funcionando como alternativa. O login sem senha exige que a chave de acesso verifique a sua identidade (Touch ID / Windows Hello / PIN), por isso é mais rápido e resistente a phishing.

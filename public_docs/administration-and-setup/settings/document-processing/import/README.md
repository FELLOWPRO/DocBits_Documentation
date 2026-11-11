# Import

## Visão geral

É necessária uma conta de administrador para criar uma ligação. Utilize **Import** para configurar a importação automática de documentos a partir de um servidor FTP/SFTP, de uma caixa de correio ligada ou do endereço de e-mail de entrada do DocBits. Verifique a organização e o ambiente atuais antes de introduzir os dados da ligação.

<figure><img src="../../../../.gitbook/assets/import-settings-overview-pt-20261109.png" alt="Página de definições de Import com o diagrama Import Pipeline, a lista FTP Import com um botão New e a lista Email Import com um botão New"><figcaption><p>A página Import: o diagrama Import Pipeline só de leitura, a lista FTP Import e a lista Email Import, cada uma com o seu próprio botão <strong>New</strong>.</p></figcaption></figure>

## Como aceder

1. Navegue até **Settings** → **Document Processing** → **Import**.
2. Expanda a secção necessária. **FTP Import** e **Email Import** têm cada uma o seu próprio botão **New**.

## **Document Settings**

A atual página Import contém **Import Pipeline**, **FTP Import**, **Email Import** e, quando ativado, **Inbound Emails**. O limite de páginas, as condições de pagamento predefinidas e os campos de padrão de data não são controlos nesta vista Import.

**Import Pipeline** mostra a topologia de encaminhamento FTP/SFTP, incluindo as regiões de origem e de destino. Verifique qualquer aviso apresentado antes de alterar uma ligação. O separador **Email** do pipeline apresenta atualmente uma mensagem de funcionalidade futura; não mostra um diagrama de processamento de e-mail.

## **FTP Import**

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-overview-en-20261030.png" alt="Tabela FTP Import com o botão New e colunas para tipo, servidor, nome de utilizador, porta, suborganização e diretório"><figcaption><p>Utilize New em FTP Import para adicionar uma ligação a um servidor. As linhas de ligações existentes estão ocultadas neste exemplo.</p></figcaption></figure>

### Requisitos

* Um servidor FTP, FTPS ou SFTP acessível ao serviço de importação.
* O endereço do servidor, o protocolo, a porta, o nome de utilizador e a palavra-passe fornecidos pelo seu administrador.
* Um diretório de importação e, se for necessário arquivar, um diretório de arquivo aprovado.

### Adicionar nova ligação

1. Clique em **New** em **FTP Import**.
2. Introduza as definições da ligação. Um novo formulário começa com **SFTP** e porta **22**; substitua estes valores quando o seu servidor utilizar outro protocolo ou outra porta.

<figure><img src="../../../../.gitbook/assets/dbdc-179-ftp-blank-form-en-20261030.png" alt="Novo formulário de ligação FTP com SFTP, porta 22, campos de diretório, definições de repetição e Save e Cancel"><figcaption><p>Introduza o servidor e os dados de início de sessão e, em seguida, verifique os diretórios, o encaminhamento e as definições de repetição. Os campos de palavra-passe e de chave API estão ocultados; este exemplo não foi guardado.</p></figcaption></figure>

* **Type**, **Server name**, **Port**, **Username** e **Password** identificam e autenticam a ligação ao servidor.
* **Primary Directory** define o diretório base. **Import Directory** seleciona a pasta a processar; a seleção de pastas fica disponível depois de a ligação ser guardada.
* **Document Type** e **Sub-Organizations** controlam a atribuição. **File name matching patterns** limita os nomes de ficheiro considerados.
* **Archive after Import** permite mover os ficheiros processados para o diretório de arquivo indicado. **Include Subfolder Files** alarga o processamento às subpastas.
* **Retry interval (min)**, **Retry duration (hours)** e **Notification emails (comma-separated)** controlam o comportamento de repetição e de notificação. Os valores predefinidos ilustrados são 60 minutos e 48 horas.
* **API Key** utiliza a chave de subscrição de aplicação existente da organização. O ícone de olho mostra ou oculta essa chave; o ícone de cópia copia-a para a área de transferência. Estes controlos não criam uma nova chave. Mantenha-a confidencial; não a inclua em capturas de ecrã ou mensagens de suporte.

Utilize **Cancel** ou o ícone de fechar para sair de um novo formulário de ligação sem o guardar.

3. Reveja os valores e clique em **Save** quando a ligação estiver pronta a ser criada.
4. No menu **Actions** da linha guardada, escolha **Activate** quando as importações estiverem autorizadas a ser executadas.

### Ações para FTP

O menu **Actions** da ligação guardada disponibiliza:

* **Test Connection**: contacta o servidor configurado para verificar a ligação.
* **Connection Logs**: inspeciona as tentativas de ligação e os erros.
* **Activate/Deactivate**: ativa ou interrompe o processamento automático desta ligação.
* **Edit**: altera a sua configuração.
* **Delete**: remove a ligação.

Testar, ativar, editar e eliminar afetam uma ligação real. Verifique a linha e a organização selecionadas antes de as utilizar.

## **Email Import**

Uma caixa de correio ligada é independente do endereço de e-mail de entrada do DocBits descrito no tutorial abaixo. Escolha o método que se adequa ao seu processo.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-overview-en-20261030.png" alt="Tabela Email Import com New, o ícone do registo de importação e colunas de configuração da caixa de correio"><figcaption><p>Utilize New para uma ligação de caixa de correio ou o ícone de registo para rever as importações. As linhas de ligações existentes e a ligação informativa estão ocultadas.</p></figcaption></figure>

<mark style="color:red;">**Note**</mark>: Apenas serão importados documentos com os seguintes tipos de ficheiro:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

{% hint style="info" %}
**Como os anexos são reconhecidos**

Para além das extensões de ficheiro indicadas acima, o DocBits também identifica um documento pelo seu **conteúdo real** (assinatura do ficheiro) e não apenas pelo tipo de conteúdo declarado pelo sistema de correio que o envia. Isto é relevante para mensagens **reencaminhadas**: os servidores ou gateways de correio intermédios reetiquetam frequentemente um anexo com um tipo genérico (`application/octet-stream`) em vez de, por exemplo, `application/pdf` ou `application/xml`. O DocBits continua a reconhecer e a importar corretamente esses anexos.

* Mensagens **`.eml` reencaminhadas** e anexos Outlook **`winmail.dat`** (TNEF) são descompactados e os documentos que contêm são importados.
* **Codificação XML:** quando uma fatura XML é reetiquetada com um tipo genérico (`application/octet-stream`), o DocBits reconhece-a pela sua declaração `<?xml`, tolerando um byte-order mark (BOM) inicial **UTF-8** ou **UTF-16** (LE/BE) — atualmente apenas estas codificações BOM são detetadas automaticamente a partir do conteúdo. Um anexo que mantenha um nome de ficheiro `.xml` é importado independentemente da sua codificação.
* **Ignorado:** as imagens incorporadas que acompanham uma mensagem (logótipos de assinatura ou gráficos incorporados — PNG, JPG, GIF, BMP) são ignoradas silenciosamente e **não** são contabilizadas como importações falhadas.

Se um anexo não puder ser importado e a opção **“Reply to this email if import can not be done”** estiver ativada para o endereço de entrada, o endereço de resposta configurado é notificado.
{% endhint %}

### Adicionar nova ligação IMAP

1. Clique em **New** em **Email Import** e selecione **IMAP** em **Protocol**.
2. Em **Email Server Setup**, introduza o nome do servidor, a porta, a encriptação, o nome de utilizador, o endereço de e-mail e a palavra-passe. Utilize os valores exigidos pelo seu fornecedor de correio; o valor 993 apresentado é um exemplo de porta, não uma definição preenchida.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-step1-en-20261030.png" alt="IMAP Email Server Setup com protocolo, servidor, porta, encriptação, credenciais da conta e Next"><figcaption><p>Preencha os campos obrigatórios do servidor e da conta antes de Next. A área da palavra-passe está ocultada; neste exemplo não foram submetidas credenciais de caixa de correio.</p></figcaption></figure>

O ícone de cópia junto a **Password** copia a palavra-passe introduzida para a área de transferência. **Cancel** ou o ícone de fechar encerra este assistente de nova ligação sem o guardar.

3. Clique em **Next** para abrir **Options**. Escolha se pretende **Merge attached documents** ou **Block duplicate filename import**. **Email Notification** ativa um e-mail de confirmação após a importação; ative-a apenas quando esse comportamento for pretendido.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-options-en-20261030.png" alt="Passo IMAP Options com merge attachments, filtragem de nomes de ficheiro duplicados, notificação por e-mail, Back e Next"><figcaption><p>Options separa o comportamento de importação da notificação por e-mail. Ambas as caixas de verificação e o interruptor de notificação estão desligados neste exemplo não guardado.</p></figcaption></figure>

4. Clique em **Next** para abrir **Config**. Selecione as **Sub-Organizations** necessárias, reveja a **API Key** existente, defina o destinatário para erros de importação e verifique **Document Routing**. Expanda **Advanced Settings** apenas quando o processo necessitar de opções adicionais.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-imap-config-en-20261030.png" alt="Passo IMAP Config com organização, chave API ocultada, notificações de erro, encaminhamento de documentos, Advanced Settings e Save"><figcaption><p>Config reúne a atribuição de organização, a chave existente, as notificações de erro e o encaminhamento. A chave está ocultada e Save não foi utilizado.</p></figcaption></figure>

Em **Config**, o ícone de olho mostra ou oculta a **API Key** existente e **Copy** copia-a para a área de transferência. Nenhum dos controlos gera uma nova chave.

5. Clique em **Save** quando a configuração estiver pronta. Em seguida, utilize **Activate** no menu **Actions** da ligação guardada para iniciar o processamento automático.

Para uma ligação IMAP guardada, **Edit** disponibiliza opções de pasta e de tratamento após a importação. Selecione a pasta de origem e a pasta de destino das mensagens movidas apenas depois de a ligação ter sido criada e de as pastas disponíveis poderem ser carregadas.

### Ações para IMAP

O menu **Actions** da ligação guardada disponibiliza **Test Connection**, **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** e **Delete**. O teste de ligação contacta a caixa de correio configurada; a ativação permite o processamento. Reveja os registos antes de repetir uma importação falhada.

### Adicionar nova ligação OAuth Office365

1. Clique em **New** em **Email Import** e selecione **OAuth Office365** em **Protocol**. Para uma aplicação de tenant gerida pelo administrador, selecione **OAuth Office365 - Tenant** e siga [O365 Tenant](o365-tenant.md).
2. Reveja **Document Routing** antes da autenticação.

<figure><img src="../../../../.gitbook/assets/dbdc-179-email-oauth-before-authentication-en-20261030.png" alt="Configuração OAuth Office365 com Document Routing e o botão Authenticate antes da autenticação Microsoft"><figcaption><p>Selecione a rota antes de Authenticate. Esta vista é anterior ao início de sessão; não foi iniciada nenhuma autenticação Microsoft.</p></figcaption></figure>

3. Clique em **Authenticate** quando a ligação à caixa de correio estiver autorizada. Conclua o início de sessão por código de dispositivo da Microsoft com o código apresentado pelo DocBits e, em seguida, regresse e selecione **Finish Authentication**.
4. Após a autenticação, reveja a organização, a pasta, a caixa de correio partilhada, a pasta de destino e as opções de notificação de erros disponibilizadas para a ligação. Utilize **Next** para continuar para **Config** quando estiver disponível e, depois, guarde as definições pretendidas.
5. Ative a ligação guardada quando as importações automáticas deverem ser executadas. **Import**, quando disponibilizado para uma ligação guardada, inicia uma importação real; utilize-o de forma deliberada.

### Ações para OAuth Office365

O menu **Actions** da ligação guardada disponibiliza **Connection Logs**, **Import Log**, **Activate/Deactivate**, **Edit** e **Delete**. A desativação interrompe o processamento automático; a eliminação remove a configuração.

### Import Log

Utilize o ícone de registo no canto superior direito de **Email Import** para rever as importações de todas as ligações de caixa de correio configuradas. Utilize a ação **Import Log** de uma linha guardada para essa ligação. Inspecione o assunto, o remetente, o estado e os detalhes de erro disponíveis antes de decidir se deve repetir.

## Inbound Emails

As duas capturas de ecrã do tutorial abaixo mostram o endereço de entrada do DocBits e os respetivos registos. Isto é independente das ligações de caixa de correio acima.

* Utilize o ícone de cópia junto a **E-Mail** para copiar o endereço de receção apresentado para a organização e o ambiente atuais.
* **Add** insere outra linha de remetente permitido no formulário. Escolha o remetente e a suborganização pretendida e, em seguida, utilize **Save** para persistir a configuração. Adicionar uma linha, por si só, não a guarda.
* **Logs** abre o registo de e-mails recebidos. **Errors** filtra por erros; **Inbound** e **Outbound** selecionam a direção da mensagem.
* Expanda uma linha de registo com o respetivo chevron para inspecionar os detalhes do anexo. O ícone de cópia junto ao ID de rastreio copia esse ID para resolução de problemas. **Original email**, quando disponível para uma linha de entrada, transfere a mensagem original selecionada como um ficheiro `.eml`; não repete a importação.

## Tutorial em vídeo: caixa de entrada de e-mail e resolução de erros

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/pt.mp4" %}
Caixa de entrada de e-mail e resolução de erros
{% endembed %}

[Ver com legendas e navegação por capítulos](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/email-import-admin/v2/pt.html)

Alguns rótulos nativos do produto podem permanecer noutro idioma. Os IDs técnicos dos campos são preservados.

Em definições e importação, utilizo o endereço de entrada do DocBits neste exemplo. Uma caixa de correio ligada diretamente é um método de importação distinto. Para esta formação, trabalho numa organização de demonstração dedicada com faturas sintéticas. As notificações permanecem desativadas.

Primeiro, verifico o endereço de receção apresentado e o âmbito. O endereço pertence exatamente a esta organização e ao seu ambiente. Para outra empresa ou um ambiente de produção, utilizo sempre o endereço efetivamente apresentado nesse local.

Aqui restringo a caixa de entrada ao nosso remetente de teste aprovado. Só seleciono a atribuição a uma suborganização se esta fizer parte do processo pretendido. Guardo a definição e volto a abri-la. O remetente permitido foi mantido; os e-mails de resposta automática continuam desativados nesta formação.

<figure><img src="../../../../.gitbook/assets/admin-save-en-accounting-email-v1.png" alt="Remetente permitido guardado com as notificações desativadas"><figcaption><p>Remetente permitido guardado com as notificações desativadas</p></figcaption></figure>

Para esta formação, foi submetida uma mensagem de teste diretamente ao processamento de e-mails recebidos do DocBits. Este teste não confirma a entrega de e-mail externo. No registo, verifico o assunto, o remetente e o anexo importado correspondentes. Depois, verifico o documento que foi efetivamente criado.

Abro o documento correspondente e comparo o anexo PDF com a fatura no DocBits. O nome do ficheiro, o número da fatura, o fornecedor e o valor têm de corresponder. Uma importação bem-sucedida não diz nada sobre uma aprovação ou um registo no ERP.

Um segundo teste controlado provém de um remetente não aprovado. No registo, procuro especificamente esta entrada e ativo o filtro de erros. Os detalhes indicam o remetente rejeitado. Verifico a causa através do assunto e do ID de rastreio, em vez de acionar a importação várias vezes.

Num caso real, esclareço primeiro se este remetente está sequer autorizado. Uma alteração aprovada à lista de remetentes é guardada e verificada novamente. Depois, verifico uma nova entrada de teste única até ao documento criado. Para erros técnicos, entrego o ID de rastreio e a mensagem de erro concreta.

<figure><img src="../../../../.gitbook/assets/admin-error-en-accounting-email-v1.png" alt="Importação falhada com anexo, motivo e rastreio"><figcaption><p>Importação falhada com anexo, motivo e rastreio</p></figcaption></figure>

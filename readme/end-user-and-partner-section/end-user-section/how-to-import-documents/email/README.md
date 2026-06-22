---
hidden: true
noIndex: true
---

# E-mail

O DocBits pode importar documentos a partir do e-mail de duas formas. Ambas são configuradas em **Configurações → Importação** (Processamento de documentos).

## Método 1 — Importação por e-mail (conectar uma caixa de correio)

Conecte uma conta de e-mail e o DocBits importa os documentos automaticamente à medida que novos e-mails chegam. Na página de Importação, abra a seção **Importação por e-mail** e clique em **+ Novo**.

<figure><img src="../../../../.gitbook/assets/email_import_section.png" alt="Seção Importação por e-mail"><figcaption>Importação por e-mail — conecte uma caixa de correio para a importação automática de documentos</figcaption></figure>

Em seguida, escolha o protocolo da sua caixa de correio:

* **IMAP** — consulte [IMAP](imap.md)
* **OAuth (Office 365)** — consulte [OAuth Office365](oauth-office365.md)

## Método 2 — E-mails recebidos (encaminhar para o DocBits)

Encaminhe — ou envie diretamente — os e-mails para o endereço de entrada exclusivo da sua organização e o DocBits importa os anexos automaticamente. Não é necessário conectar nenhuma caixa de correio. Abra a seção **E-mails recebidos** na página de Importação.

<figure><img src="../../../../.gitbook/assets/inbound_emails_section.png" alt="Seção E-mails recebidos"><figcaption>E-mails recebidos — encaminhe documentos para o seu endereço do DocBits</figcaption></figure>

* **Info / E-mail** — o endereço de entrada exclusivo da sua organização (formato `<org-id>@inbound.docbits.com`). Encaminhe seus documentos para este endereço; use o ícone de copiar para copiá-lo.
* **Importar documentos apenas de e-mails predefinidos** — quando ativado, somente os e-mails dos remetentes adicionados à lista de permissões são importados; e-mails de qualquer outro remetente são ignorados.
* **Responder a este e-mail se a importação não for possível** — envia uma resposta automática ao remetente quando a importação falha.
* **Notificar o remetente quando a importação falhar** — avisa o remetente se o e-mail dele não pôde ser importado.
* **Logs** — abre o registro de processamento de e-mails recebidos. Clique em **Salvar** para aplicar as alterações.

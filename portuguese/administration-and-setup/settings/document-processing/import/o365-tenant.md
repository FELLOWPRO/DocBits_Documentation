# Tenant do Office 365

## Registrar App no Azure AD

<mark style="color:red;">**Nota**</mark>: As permissões podem exigir autorização de um administrador.

1. Entre no [Portal do Azure](https://portal.azure.com/) usando suas credenciais.
2. Nos serviços do Azure, localize e abra o Azure Active Directory (também conhecido como Azure AD).

![Entrada Azure Active Directory na pesquisa e na lista de serviços do portal do Azure](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Na seção **Manage**, selecione **App registrations**.

![Página de descrição geral do Azure Active Directory com a secção Manage e a entrada App registrations no menu esquerdo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Na tela App registrations, clique em **+ New registration**.

![Página App registrations com o botão + New registration na barra de ferramentas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. A tela **Register an application** é exibida. Insira o nome de exibição voltado para o usuário para o App em **Name**.

![Formulário Register an application com o campo Name e o texto de ajuda para o nome apresentado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecione um dos seguintes tipos de conta dependendo de suas necessidades:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![Lista Supported account types com as opções para inquilino único, vários inquilinos e contas Microsoft pessoais](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Deixe a opção **Redirect URI (optional)** como está.

![Formulário Register an application com os tipos de conta suportados e a opção de vários inquilinos selecionada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Clique em **Register** para concluir o registro do App. Isso o levará de volta à tela do novo App.
9. Na tela do App, localize o **Application (client) ID**. Copie-o para ser usado ao configurar a importação de e-mail para o **DocBits**.

![Secção Redirect URI (optional) do formulário de registo e o botão Register por baixo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. No painel esquerdo, selecione **Certificates & secrets**:

![Página de descrição geral da aplicação registada com Display name, Application (client) ID e os botões Delete e Endpoints](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Na tela **Certificates & secrets**, clique no botão **+ New client secret** na seção **Client secrets**:

![Entrada Certificates & secrets no menu esquerdo da aplicação registada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Na caixa de diálogo **Add a client secret**, clique no botão **Add**:

![Secção Client secrets com a sua descrição e a indicação de que ainda não foi criado nenhum segredo de cliente](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

É recomendável preencher uma descrição para identificar este segredo entre muitos (até agora o limite é de 2 segredos por App).

![Caixa de diálogo Add a client secret com o campo Description e as opções de expiração 1 ano, 2 anos e nunca](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Selecione esta data de expiração de acordo com a política da sua empresa. Uma vez expirado, um novo client secret precisará ser criado e especificado para cada configuração de e-mail onde foi usado anteriormente.

13. O client secret recém-gerado ficará visível. Copie este client secret para ser usado ao configurar a importação de e-mail para o DocBits.

![Tabela Client secrets com o segredo criado, a data de expiração e o ícone de cópia junto ao valor](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Certifique-se de ter copiado o client secret, pois o client secret não será exibido novamente após ser fechado.

14. Selecione **Authentication** no painel esquerdo. Isso apresentará a tela **Authentication** no lado direito.

![Entrada Authentication no menu esquerdo da aplicação registada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Na seção **Advanced settings**, clique em **Yes** para **Default client type**.

![Página Authentication, secção Advanced settings, com Default client type em Yes para cliente público](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Clique em **Save** para confirmar as alterações.

![Página Authentication com os botões Save e Discard na barra de ferramentas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecione **API permissions** no painel esquerdo. Isso apresentará a tela de permissões de API.

![Entrada API permissions no menu esquerdo da aplicação registada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Por padrão, a permissão **User.Read** do **Microsoft Graph** está presente, deixe como está.

![Tabela API permissions com a permissão delegada User.Read do Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Esta é uma permissão obrigatória. Se esta permissão não estiver disponível, adicione a permissão com as etapas mencionadas abaixo para a permissão **Mail.ReadWrite**.

19. Clique em **+ Add a permission**. Isso abrirá o painel **Request API permissions**.

![Painel Configured permissions com o botão + Add a permission e uma lista de permissões vazia](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Clique em **Microsoft Graph**.

![Painel Request API permissions com a entrada Microsoft Graph entre as APIs da Microsoft mais utilizadas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Das duas subcategorias, selecione **App Permissions**.

![Painel de permissões do Microsoft Graph com a escolha entre Delegated permissions e Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Digite **Mail.ReadWrite** na caixa de pesquisa. Selecione a caixa de seleção **Mail.ReadWrite** para a permissão.

![Painel Request API permissions com Mail.ReadWrite na pesquisa de permissões e a permissão Mail correspondente](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Isso habilitará o botão **Add permissions** na parte inferior do painel. Clique em **Add permissions**.

![Painel Request API permissions com a caixa Mail.ReadWrite marcada e o botão Add permissions ativo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Isso adicionará a permissão **Mail.ReadWrite** à lista de **Configured permissions** para o App.

<mark style="color:red;">**Nota**</mark>: Permissões de administrador podem ser necessárias. O administrador terá que autorizar o App para usar essas permissões. Uma vez autorizado, o status concedido será indicado da seguinte forma:

![Painel Configured permissions com a permissão Mail.ReadWrite e o botão Grant admin consent para o inquilino](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)

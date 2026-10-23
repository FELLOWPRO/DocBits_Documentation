# Tenant do Office 365

## Registrar App no Azure AD

<mark style="color:red;">**Nota**</mark>: As permissões podem exigir autorização de um administrador.

1. Entre no [Portal do Azure](https://portal.azure.com/) usando suas credenciais.
2. Nos serviços do Azure, localize e abra o Azure Active Directory (também conhecido como Azure AD).

![Página do portal do Azure com a entrada Azure Active Directory e a barra de pesquisa de serviços](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Na seção **Manage**, selecione **App registrations**.

![Página de descrição geral do Azure Active Directory com o menu Manage à esquerda aberto e App registrations destacado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Na tela App registrations, clique em **+ New registration**.

![Ecrã App registrations no Azure com o botão New registration na barra de ferramentas e a lista de aplicações registadas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. A tela **Register an application** é exibida. Insira o nome de exibição voltado para o usuário para o App em **Name**.

![Ecrã Register an application no portal do Azure com o campo Name vazio para a nova aplicação](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecione um dos seguintes tipos de conta dependendo de suas necessidades:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![Ecrã Register an application com as opções de botão de rádio do tipo de conta suportado para diretórios organizacionais e contas Microsoft pessoais](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Deixe a opção **Redirect URI (optional)** como está.

![Ecrã Register an application com a secção Redirect URI (optional) mantida inalterada na parte inferior](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Clique em **Register** para concluir o registro do App. Isso o levará de volta à tela do novo App.
9. Na tela do App, localize o **Application (client) ID**. Copie-o para ser usado ao configurar a importação de e-mail para o **DocBits**.

![Página de descrição geral da aplicação registada mostrando o Display name Ephesoft OAuth2 App e o Application client ID](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. No painel esquerdo, selecione **Certificates & secrets**:

![Página de visão geral da aplicação registada com Certificates and secrets selecionado na secção Manage do painel esquerdo](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Na tela **Certificates & secrets**, clique no botão **+ New client secret** na seção **Client secrets**:

![Ecrã de Certificates & secrets com a secção Client secrets e o botão + New client secret](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Na caixa de diálogo **Add a client secret**, clique no botão **Add**:

![Diálogo Add a client secret com os campos Description e Expires e o botão Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

É recomendável preencher uma descrição para identificar este segredo entre muitos (até agora o limite é de 2 segredos por App).

![Lista de client secrets que mostra o novo segredo com as colunas de descrição, Value e Expires](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Selecione esta data de expiração de acordo com a política da sua empresa. Uma vez expirado, um novo client secret precisará ser criado e especificado para cada configuração de e-mail onde foi usado anteriormente.

13. O client secret recém-gerado ficará visível. Copie este client secret para ser usado ao configurar a importação de e-mail para o DocBits.

![Secção Client secrets de Certificates & secrets com o valor do segredo gerado pronto para copiar](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Certifique-se de ter copiado o client secret, pois o client secret não será exibido novamente após ser fechado.

14. Selecione **Authentication** no painel esquerdo. Isso apresentará a tela **Authentication** no lado direito.

![Ecrã de autenticação do registo da aplicação aberto a partir do painel esquerdo com as definições de plataforma à direita](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Na seção **Advanced settings**, clique em **Yes** para **Default client type**.

![Secção Advanced settings do ecrã de Authentication com a opção Default client type definida como Yes](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Clique em **Save** para confirmar as alterações.

![Barra superior do registo da aplicação com o botão Save destacado após ativar o tipo de cliente predefinido](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecione **API permissions** no painel esquerdo. Isso apresentará a tela de permissões de API.

![Ecrã API permissions aberto a partir do painel esquerdo a mostrar as permissões configuradas para a aplicação](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Por padrão, a permissão **User.Read** do **Microsoft Graph** está presente, deixe como está.

![Lista de permissões configuradas a mostrar a permissão delegada predefinida User.Read para o Microsoft Graph](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Esta é uma permissão obrigatória. Se esta permissão não estiver disponível, adicione a permissão com as etapas mencionadas abaixo para a permissão **Mail.ReadWrite**.

19. Clique em **+ Add a permission**. Isso abrirá o painel **Request API permissions**.

![Painel Request API permissions com Microsoft APIs, APIs my organization uses e o fluxo de + Add a permission](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Clique em **Microsoft Graph**.

![Painel Request API permissions com o Microsoft Graph destacado entre as API da Microsoft mais utilizadas](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Das duas subcategorias, selecione **App Permissions**.

![Painel Request API permissions para o Microsoft Graph com as opções Delegated permissions e Application permissions](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Digite **Mail.ReadWrite** na caixa de pesquisa. Selecione a caixa de seleção **Mail.ReadWrite** para a permissão.

![Caixa de pesquisa de permissões da aplicação com Mail.ReadWrite digitado e a caixa de verificação da permissão Mail.ReadWrite selecionada](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Isso habilitará o botão **Add permissions** na parte inferior do painel. Clique em **Add permissions**.

![Painel Request API permissions com a permissão Mail.ReadWrite selecionada e o botão Add permissions na parte inferior](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Isso adicionará a permissão **Mail.ReadWrite** à lista de **Configured permissions** para o App.

<mark style="color:red;">**Nota**</mark>: Permissões de administrador podem ser necessárias. O administrador terá que autorizar o App para usar essas permissões. Uma vez autorizado, o status concedido será indicado da seguinte forma:

![Lista de permissões configuradas com a permissão de aplicação Mail.ReadWrite adicionada e o respetivo estado concedido apresentado](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)

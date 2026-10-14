# O365 Tenant

## Registrar App no Azure AD

<mark style="color:red;">**Nota**</mark>: As permissões podem exigir autorização de um administrador.

1. Entre no [Portal do Azure](https://portal.azure.com/) usando suas credenciais.
2. Nos serviços do Azure, localize e abra o Azure Active Directory (também conhecido como Azure AD).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_1.png)

3. Na seção **Manage**, selecione **App registrations**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_2.png)

4. Na tela App registrations, clique em **+ New registration**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_3.png)

5. A tela **Register an application** é exibida. Insira o nome de exibição voltado para o usuário para o App em **Name**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_4.png)

6. Selecione um dos seguintes tipos de conta dependendo de suas necessidades:

* **Accounts in any organizational directory (Any Azure AD directory Multitenant) and personal Microsoft accounts (e.g. Skype, Xbox)**
* **Accounts in any organizational directory (Any Azure AD directory Multitenant)**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_5.png)

7. Deixe a opção **Redirect URI (optional)** como está.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_6.png)

8. Clique em **Register** para concluir o registro do App. Isso o levará de volta à tela do novo App.
9. Na tela do App, localize o **Application (client) ID**. Copie-o para ser usado ao configurar a importação de e-mail para o **DocBits**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_7.png)

10. No painel esquerdo, selecione **Certificates & secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_8.png)

11. Na tela **Certificates & secrets**, clique no botão **+ New client secret** na seção **Client secrets**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_9.png)

12. Na caixa de diálogo **Add a client secret**, clique no botão **Add**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_10.png)

É recomendável preencher uma descrição para identificar este segredo entre muitos (até agora o limite é de 2 segredos por App).

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_11.png)

<mark style="color:red;">**Nota**</mark>: Selecione esta data de expiração de acordo com a política da sua empresa. Uma vez expirado, um novo client secret precisará ser criado e especificado para cada configuração de e-mail onde foi usado anteriormente.

13. O client secret recém-gerado ficará visível. Copie este client secret para ser usado ao configurar a importação de e-mail para o DocBits.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_12.png)

**Importante:** Certifique-se de ter copiado o client secret, pois o client secret não será exibido novamente após ser fechado.

14. Selecione **Authentication** no painel esquerdo. Isso apresentará a tela **Authentication** no lado direito.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_13.png)

15. Na seção **Advanced settings**, clique em **Yes** para **Default client type**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_14.png)

16. Clique em **Save** para confirmar as alterações.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_15.png)

17. Selecione **API permissions** no painel esquerdo. Isso apresentará a tela de permissões de API.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_16.png)

18. Por padrão, a permissão **User.Read** do **Microsoft Graph** está presente, deixe como está.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_17.png)

<mark style="color:red;">**Nota**</mark>: Esta é uma permissão obrigatória. Se esta permissão não estiver disponível, adicione a permissão com as etapas mencionadas abaixo para a permissão **Mail.ReadWrite**.

19. Clique em **+ Add a permission**. Isso abrirá o painel **Request API permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_18.png)

20. Clique em **Microsoft Graph**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_19.png)

21. Das duas subcategorias, selecione **App Permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_20.png)

22. Digite **Mail.ReadWrite** na caixa de pesquisa. Selecione a caixa de seleção **Mail.ReadWrite** para a permissão.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_21.png)

23. Isso habilitará o botão **Add permissions** na parte inferior do painel. Clique em **Add permissions**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_22.png)

24. Isso adicionará a permissão **Mail.ReadWrite** à lista de **Configured permissions** para o App.

<mark style="color:red;">**Nota**</mark>: Permissões de administrador podem ser necessárias. O administrador terá que autorizar o App para usar essas permissões. Uma vez autorizado, o status concedido será indicado da seguinte forma:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/o365_tenant_23.png)

---
description: Usando o DocBits com o seu Login da Microsoft sem usar uma senha (separada)
---

# SSO do Azure

### Criar SAML SSO no Azure AD

Execute as etapas a seguir para adicionar SAML SSO no Azure AD:

*   No Azure, acesse o seu console do \`Azure Active Directory\`

    ![Painel de navegação do portal do Azure com favoritos como Resource groups, All resources e Azure Active Directory](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* No painel à esquerda, clique em \`Enterprise applications\`

![Painel esquerdo do Azure Active Directory com as entradas Manage Users, Groups, Roles and administrators e Enterprise applications](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Clique em \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Ecrã de validação com a lista de campos extraídos à esquerda, a pré-visualização do documento do fornecedor à direita e botões de aprovação em baixo"><figcaption></figcaption></figure>

* Clique em \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Página Configuraciones General com as caixas de verificação Quien puede subir documentos, Quien puede subir dados e Quien puede validar y exportar"><figcaption></figcaption></figure></div>

* Insira um nome para a sua aplicação. Mantenha as demais seleções padrão.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Diálogo Create your own application no Azure com o nome da aplicação MyApplication e as opções de integração de aplicações"><figcaption></figcaption></figure>

* Clique em \`Create\`

### Atribuir Usuários à Configuração de SSO

Em seguida, atribua usuários ou grupos à configuração de SSO.

**Importante**: Você já deve ter criado usuários e grupos no Azure AD. Se você não tiver nenhum usuário ou grupo, crie-os agora antes de prosseguir.

* Em \`Getting Started\`, clique em \`Assign Users and Groups\`.
* Clique em \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Página Users and groups da MyApplication no Azure com os botões Add user, Edit e Remove e uma lista de Display Name vazia" width="563"><figcaption></figcaption></figure>

* Selecione os usuários e grupos que você deseja atribuir a esta configuração de SSO. Esses usuários poderão se autenticar no DocBits (usando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Painel de seleção de utilizadores e grupos no Azure com uma lista de utilizadores Daniel e um painel Selected items"><figcaption></figcaption></figure>

* Clique em \`Select\`
* Quando estiver satisfeito com a sua seleção, clique em \`Assign\`

![Diálogo Add Assignment no Azure com 2 users selected, 2 groups selected e Select Role definido como User](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Página de definições de Integration and SSO com a tabela Claves API e as colunas Nombre, Caduca, Ultimo Uso, Estado e Actions"><figcaption></figcaption></figure></div>

* Acesse a lista de visualização \`Groups\` e localize os grupos atribuídos.

### Configurar o SSO no Azure

Em seguida, você precisa concluir a configuração do single-sign-on no Azure.\\

* No painel à esquerda, clique em \`Single sign-on\`

![Menu de descrição geral da aplicação empresarial no Azure com as entradas Manage Properties, Owners, Users and groups, Single sign-on e Provisioning](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Clique em \`SAML\`

![Cartão de opção SAML no Azure que descreve uma autenticação rica e segura com o protocolo Security Assertion Markup Language](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Clique em \`Upload metadata file\`

![Painel SAML-based Sign-on no Azure com Upload metadata file e Set up Single Sign-On](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Faça o upload do **metadata.xml** do DocBits, que você pode encontrar no menu de Configurações **Integration** em **SSO Service Provider Settings** da sua conta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Página SSO Service Provider Settings com o Tenant ID, o Entity ID e os campos SSO Url, SLO Url e Metadata Url"><figcaption></figcaption></figure>

* Edite a \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Ecrã de configuração do início de sessão único com SAML a mostrar Basic SAML Configuration com Identifier, Reply URL, Sign on URL e Logout Url"><figcaption></figcaption></figure>

* Verifique se o \`Entity ID\`, a \`ACS URL\`, a \`Sign on URL\` e a \`Logout URL\` foram preenchidos corretamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Editor de Basic SAML Configuration no Azure com os campos Identifier, Reply URL, Sign on URL, Relay State e Logout Url, além de Save"><figcaption></figcaption></figure>

* Faça o download do **Federation Metadata XML** recém-gerado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Secção SAML Signing Certificate no Azure com impressão digital, data de expiração e links de download para Certificate (Raw) e Federation Metadata XML"><figcaption></figcaption></figure>

* Faça o upload do FederationMetadata.xml nas **Identity Service Provider Settings** da sua conta DocBits, que você pode encontrar no menu de Configurações **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Diálogo Identity Service Provider Settings no DocBits com o Tenant ID FELLOWPRO_PRD e o botão Upload file"><figcaption></figcaption></figure>

---
description: Usando o DocBits com o seu Login da Microsoft sem usar uma senha (separada)
---

# Azure SSO

### Criar SAML SSO no Azure AD

Execute as etapas a seguir para adicionar SAML SSO no Azure AD:

*   No Azure, acesse o seu console do \`Azure Active Directory\`

    ![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* No painel à esquerda, clique em \`Enterprise applications\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Clique em \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt=""><figcaption></figcaption></figure>

* Clique em \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt=""><figcaption></figcaption></figure></div>

* Insira um nome para a sua aplicação. Mantenha as demais seleções padrão.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt=""><figcaption></figcaption></figure>

* Clique em \`Create\`

### Atribuir Usuários à Configuração de SSO

Em seguida, atribua usuários ou grupos à configuração de SSO.

**Importante**: Você já deve ter criado usuários e grupos no Azure AD. Se você não tiver nenhum usuário ou grupo, crie-os agora antes de prosseguir.

* Em \`Getting Started\`, clique em \`Assign Users and Groups\`.
* Clique em \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="" width="563"><figcaption></figcaption></figure>

* Selecione os usuários e grupos que você deseja atribuir a esta configuração de SSO. Esses usuários poderão se autenticar no DocBits (usando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt=""><figcaption></figcaption></figure>

* Clique em \`Select\`
* Quando estiver satisfeito com a sua seleção, clique em \`Assign\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt=""><figcaption></figcaption></figure></div>

* Acesse a lista de visualização \`Groups\` e localize os grupos atribuídos.

### Configurar o SSO no Azure

Em seguida, você precisa concluir a configuração do single-sign-on no Azure.\\

* No painel à esquerda, clique em \`Single sign-on\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Clique em \`SAML\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Clique em \`Upload metadata file\`

![](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Faça o upload do **metadata.xml** do DocBits, que você pode encontrar no menu de Configurações **Integration** em **SSO Service Provider Settings** da sua conta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt=""><figcaption></figcaption></figure>

* Edite a \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt=""><figcaption></figcaption></figure>

* Verifique se o \`Entity ID\`, a \`ACS URL\`, a \`Sign on URL\` e a \`Logout URL\` foram preenchidos corretamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt=""><figcaption></figcaption></figure>

* Faça o download do **Federation Metadata XML** recém-gerado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt=""><figcaption></figcaption></figure>

* Faça o upload do FederationMetadata.xml nas **Identity Service Provider Settings** da sua conta DocBits, que você pode encontrar no menu de Configurações **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt=""><figcaption></figcaption></figure>

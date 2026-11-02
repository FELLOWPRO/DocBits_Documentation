---
description: Usando o DocBits com o seu Login da Microsoft sem usar uma senha (separada)
---

# SSO do Azure

### Criar SAML SSO no Azure AD

Execute as etapas a seguir para adicionar SAML SSO no Azure AD:

*   No Azure, acesse o seu console do \`Azure Active Directory\`

    ![Página inicial do portal do Azure com o Azure Active Directory nos favoritos da navegação esquerda](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_1.png)
* No painel à esquerda, clique em \`Enterprise applications\`

![Navegação esquerda do Azure Active Directory com o grupo Gerir e a entrada Aplicações empresariais](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_2.png)

* Clique em \`+ New application

<figure><img src="../../../../../../.gitbook/assets/image (213).png" alt="Página Aplicações empresariais do Azure Active Directory com a lista Todas as aplicações e o botão Nova aplicação"><figcaption></figcaption></figure>

* Clique em \`+ Create your own application\`

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (215).png" alt="Janela Procurar na galeria do Azure AD com os botões Criar a sua própria aplicação e Pedir nova aplicação da galeria e o campo de pesquisa Procurar aplicação"><figcaption></figcaption></figure></div>

* Insira um nome para a sua aplicação. Mantenha as demais seleções padrão.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_5.png" alt="Janela Criar a sua própria aplicação com o nome MyApplication e a opção selecionada Integrar qualquer outra aplicação que não encontre na galeria"><figcaption></figcaption></figure>

* Clique em \`Create\`

### Atribuir Usuários à Configuração de SSO

Em seguida, atribua usuários ou grupos à configuração de SSO.

**Importante**: Você já deve ter criado usuários e grupos no Azure AD. Se você não tiver nenhum usuário ou grupo, crie-os agora antes de prosseguir.

* Em \`Getting Started\`, clique em \`Assign Users and Groups\`.
* Clique em \`+ Add user\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_6.png" alt="Página Utilizadores e grupos da aplicação MyApplication com os botões Adicionar utilizador, Editar, Remover e Atualizar e a mensagem Nenhuma atribuição de aplicação encontrada" width="563"><figcaption></figcaption></figure>

* Selecione os usuários e grupos que você deseja atribuir a esta configuração de SSO. Esses usuários poderão se autenticar no DocBits (usando SSO).

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_7.png" alt="Painel de seleção de utilizadores com vários utilizadores listados e a secção Selecionados"><figcaption></figcaption></figure>

* Clique em \`Select\`
* Quando estiver satisfeito com a sua seleção, clique em \`Assign\`

![Janela Adicionar atribuição do inquilino chimdustries com a mensagem 2 utilizadores selecionados e 2 grupos selecionados](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_8.png)

<div align="left"><figure><img src="../../../../../../.gitbook/assets/image (216) (1).png" alt="Botão Atribuir realçado com um contorno verde na janela de atribuição do Azure Active Directory"><figcaption></figcaption></figure></div>

* Acesse a lista de visualização \`Groups\` e localize os grupos atribuídos.

### Configurar o SSO no Azure

Em seguida, você precisa concluir a configuração do single-sign-on no Azure.\\

* No painel à esquerda, clique em \`Single sign-on\`

![Navegação esquerda da aplicação empresarial MyApplication com a entrada Início de sessão único](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_10.png)

* Clique em \`SAML\`

![Página Início de sessão único com o mosaico SAML e o texto Autenticação segura e fiável para aplicações através do protocolo SAML](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_11.png)

* Clique em \`Upload metadata file\`

![Página Início de sessão baseado em SAML com as ligações Carregar ficheiro de metadados e Configurar início de sessão único](https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_12.png)

* Faça o upload do **metadata.xml** do DocBits, que você pode encontrar no menu de Configurações **Integration** em **SSO Service Provider Settings** da sua conta DocBits.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_Metadata-1024x216.png" alt="Definições do fornecedor de serviços SSO no DocBits com o Entity ID, o SLO URI e o SSO URI e os botões Transferir certificado e Transferir metadados"><figcaption></figcaption></figure>

* Edite a \`Basic SAML Configuration\`

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.png" alt="Página Configurar início de sessão único com SAML com a secção Configuração SAML básica e os campos Identificador Entity ID, URL de resposta, URL de início de sessão, Estado de retransmissão e URL de terminar sessão"><figcaption></figcaption></figure>

* Verifique se o \`Entity ID\`, a \`ACS URL\`, a \`Sign on URL\` e a \`Logout URL\` foram preenchidos corretamente.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_13.1.png" alt="Configuração SAML básica no Azure com os textos descritivos, o Identificador Entity ID definido para o URL de metadados SAML do inquilino e o URL de resposta como Assertion Consumer Service URL"><figcaption></figcaption></figure>

* Faça o download do **Federation Metadata XML** recém-gerado.

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_14.png" alt="Secção Certificado de assinatura SAML com o estado Ativo, a impressão digital, a data de expiração, o e-mail de notificação e as ligações de transferência Certificado não processado e XML de metadados de federação"><figcaption></figcaption></figure>

* Faça o upload do FederationMetadata.xml nas **Identity Service Provider Settings** da sua conta DocBits, que você pode encontrar no menu de Configurações **Integration**.

\\

<figure><img src="https://docbits.com/wp-content/uploads/2023/09/DocBits_Azure_15-1024x204.png" alt="Definições do fornecedor de serviços de identidade no DocBits com o Tenant ID, os botões Carregar ficheiro e Importar e a entrada do ficheiro existente"><figcaption></figcaption></figure>

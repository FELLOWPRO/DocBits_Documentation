# Company Information

<figure><img src="../../../../.gitbook/assets/company_information.png" alt="Formulário Company Information na organização de teste Sandbox do DocBits em inglês"><figcaption><p>Company Information: edite o nome da organização, o endereço, os identificadores legais e os dados de contato e, em seguida, selecione Save.</p></figcaption></figure>

A página Company Information permite gerenciar o perfil da sua empresa, as preferências e os detalhes da assinatura. Ela é organizada nas seguintes seções:

## Company Information

Esta seção contém os dados principais da sua empresa, agrupados em quatro áreas:

### Identidade da empresa

* **Name** *(obrigatório)*: o nome legal da sua empresa.

### Endereço

* **Street + Number**: o endereço (rua) da sua empresa.
* **Postal Code**: CEP ou código postal.
* **City**: nome da cidade.
* **Country**: selecione o seu país na lista suspensa.

### Informações legais

* **Company ID**: um identificador exclusivo da sua empresa, usado para integrações e como referência interna.
* **Tax ID**: seu número de identificação fiscal para relatórios financeiros.
* **Commercial Register ID**: seu número de registro comercial para a documentação legal.

### Contato

* **Official Company Phone Number**: o telefone principal da sua empresa.
* **E-Mail**: o endereço de e-mail principal usado para comunicações oficiais.

Depois de inserir ou atualizar qualquer campo, clique em **Save** para aplicar as alterações. Os ícones **?** ao lado dos identificadores legais mostram orientações adicionais sobre o campo. Selecione o título da seção para expandir ou recolher o formulário.

## E-mail domains

Os administradores da organização podem abrir **Settings → Company Information → E-mail domains** para gerenciar os domínios usados na atribuição automática à organização. Quando alguém entra com Microsoft ou Google e ainda não é membro de uma organização, o DocBits pode atribuí-lo a esta organização se o endereço de e-mail dessa pessoa usar um dos domínios listados. Um domínio pode pertencer a apenas uma organização.

<figure><img src="../../../../.gitbook/assets/company_email_domains_en.png" alt="Seção E-mail domains expandida com uma lista de domínios vazia, campo de entrada e botão Add domain"><figcaption><p>A seção E-mail domains em inglês antes de um domínio ser adicionado. Insira um domínio da empresa e selecione Add domain.</p></figcaption></figure>

Insira apenas o domínio, como `example.com`, no campo e selecione **Add domain** ou pressione Enter. O primeiro domínio se torna o domínio principal. Se houver mais domínios listados, use **Make primary** em outra linha para alterá-lo ou o ícone de lixeira para remover um domínio. Erros como domínio inválido, provedor de e-mail pessoal ou domínio já atribuído a outra organização aparecem abaixo do campo. **No domains assigned yet** significa que esta organização não tem nenhuma regra de domínio.

Antes de adicionar um domínio, verifique qual organização deve receber os novos logins. Para gerenciar as associações existentes, continue em [Users](../groups-users-and-permissions/users/README.md).

## Company Preferences

Configure as definições padrão válidas para toda a empresa:

* **Date Pattern**: escolha como as datas são exibidas em todo o DocBits (por exemplo, `%m/%d/%Y`, `%d.%m.%Y`).
* **Amount Formatting**: selecione o formato numérico dos valores (por exemplo, Deutsch para `1.000,00`, English para `1,000.00`).
* **New Version Info Dialog**: define se os usuários veem uma notificação quando uma nova versão do DocBits é lançada.

Clique em **Save** depois de fazer as alterações.

## App-Color

Personalize a cor primária da interface do DocBits. Isso é útil para distinguir visualmente diferentes ambientes (por exemplo, dev e produção).

* **Color**: insira um código de cor hexadecimal (por exemplo, `#2388AE`) ou use o seletor de cores.
* Clique em **Save** para aplicar ou em **Reset** para restaurar a cor padrão.

## Subscription Plan

Veja seus planos de assinatura ativos e os respectivos detalhes:

* **Plan Name**: o nome de cada plano ativo (por exemplo, DocBits, DocFlow Users, DocSearch).
* **Days Left**: quantos dias faltam para o plano expirar.
* **Start Date / End Date**: o período da assinatura.
* **Users Count**: número total de usuários na sua organização.
* **Sub Organizations Count**: número de suborganizações configuradas.
* **Suppliers Count**: número de fornecedores cadastrados.

## Subscription Usage

Acompanhe seu consumo mensal de tokens e de workflows:

| Coluna | Descrição |
|--------|-------------|
| **Type** | O tipo de uso (Document ou Workflow). |
| **From / To** | As datas do período de faturamento. |
| **Tokens Used** | Número de tokens consumidos no período atual. |
| **Remaining Tokens** | Tokens ainda disponíveis no período atual. |

Use o botão **Select** para filtrar por intervalos de datas específicos.

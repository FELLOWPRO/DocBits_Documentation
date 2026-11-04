# Portal do Fornecedor

## Visão Geral

Esta página explica como ativar e usar o **Portal do Fornecedor**, bem como onde encontrar todas as configurações relevantes. O Portal do Fornecedor permite que você convide fornecedores para **DocBits**. Uma vez que o acesso é concedido, os fornecedores podem fazer login para visualizar o status de seus **Pedidos de Compra** e **Faturas** diretamente dentro do **DocBits**.

## Como Ativar o Portal do Fornecedor

1.  Vá para **Configurações → Processamento de documentos → Módulo**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_module.png)
2.  Na seção **Envio e Fornecedor**, ative a opção **Portal do Fornecedor**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_1.png)

## Configurações do Fornecedor

Uma vez que o recurso **Portal do Fornecedor** está ativado, uma nova seção **Configurações do Fornecedor** aparecerá na parte inferior do menu **Configurações**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_suppplier_settings.png)

[**Configurações gerais do fornecedor**](../settings/supplier-setting/supplier-general-settings.md): Aqui, você pode personalizar o **Portal do Fornecedor** fazendo o upload do logotipo da sua empresa—exibido no cabeçalho de todos os modelos de e-mail—e gerenciando documentos legais, como os Termos de Uso e a Política de Privacidade.

[**Modelos de e-mail**](../settings/supplier-setting/editing-email-templates.md)**:** Aqui você pode criar e testar os modelos de e-mail de convite que serão enviados aos fornecedores convidados.

**Layout do Fornecedor:** Aqui você pode criar e gerenciar os layouts que definem quais informações novos fornecedores devem fornecer durante o processo de registro.

[**Configuração de exportação**](../settings/supplier-setting/export-configuration-for-supplier-portal-for-m3.md): Aqui você pode definir como os dados são mapeados e sincronizados entre o **Portal do Fornecedor** e o sistema **Infor M3** usando arquivos de mapeamento ION e IDM.

**Permissões do Fornecedor**: Aqui você pode configurar as permissões que os fornecedores terão dentro do **Portal do Fornecedor**. Você também pode agrupar fornecedores, facilitando a gestão de acesso e configurações entre vários fornecedores.

Um guia detalhado sobre todas as Configurações do Fornecedor pode ser encontrado [aqui](../settings/supplier-setting/).

## Painel do Fornecedor <a href="#supplier-permissions" id="supplier-permissions"></a>

Você pode acessar o **Painel do Fornecedor** no menu à esquerda, conforme mostrado abaixo.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_2.png)

Todos os seus Fornecedores criados são exibidos aqui.

## Filtro para Fornecedores

Você pode pesquisar fornecedores por N**ome** ou N**úmero**, ou usar os filtros avançados para restringir os resultados por:

* **Grupos de Fornecedores**
* **Status**
* **Criado Em**

Você também pode especificar quantos fornecedores devem ser exibidos por página.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_9.png)

Além disso, você pode rapidamente filtrar pelos status **Aprovação pendente** ou **Registro pendente** clicando na categoria correspondente à esquerda da barra de filtro.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/10.png)

## Status do Fornecedor

Se você estiver usando o **Portal do Fornecedor**, é importante entender os diferentes status que os fornecedores podem ter. Abaixo está uma lista de todos os possíveis status dos fornecedores e seus significados:

* **Abrir**: Fornecedor existente que ainda não foi convidado para o portal.
* **Registro pendente**: O fornecedor foi convidado, mas ainda não completou o processo de registro.
* **Entrada do fornecedor pendente**: O registro está completo, mas mais informações ou alterações são necessárias do fornecedor.
* **Aprovação pendente**: O fornecedor completou o registro e está aguardando a primeira aprovação.
* **Aprovação AP pendente**: O fornecedor recebeu a primeira aprovação e está aguardando uma segunda aprovação (Contas a Pagar).
* **Aprovado**: O fornecedor completou o processo e foi totalmente aprovado.
* **Rejeitado**: O registro ou aprovação do fornecedor foi rejeitado.

## Ferramentas no Painel do Fornecedor

À direita da barra de pesquisa, você encontrará várias ferramentas que ajudam a interagir e gerenciar o painel de forma mais eficiente.

### Atualizar tabela <a href="#refresh-table" id="refresh-table"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_3.png)

Clique neste botão para atualizar o painel e carregar os dados e status mais recentes.

### Definir colunas da tabela para organização <a href="#set-table-columns-for-organization" id="set-table-columns-for-organization"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_4.png)

Clique neste botão para abrir um menu onde você pode gerenciar a visibilidade das colunas na tabela de pedidos de compra. Use as caixas de seleção e os botões de seta para mover colunas entre as seções visíveis e ocultas. Você também pode reordenar colunas arrastando e soltando os nomes das colunas. Clique em **Feito** para salvar suas alterações.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_7.png)

### Análise <a href="#analytics" id="analytics"></a>

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_5.png)

Clicar neste botão abrirá uma nova seção mostrando quantos fornecedores estão prestes a expirar e quando.\
Clique em qualquer categoria para aplicar um filtro e visualizar apenas aqueles fornecedores.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_8.png)

## Criar Fornecedor e Enviar E-mail de Registro

### **Para criar um novo fornecedor:**

1.  Clique no ícone de mais (+) no canto superior direito.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_6.png)
2.  Preencha os campos obrigatórios e clique em **Salvar**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_11.png)
3. O fornecedor receberá automaticamente um e-mail com um link para criar sua conta.

### **Para enviar um e-mail de registro a um fornecedor existente:**

1. Localize o fornecedor no **Painel do Fornecedor**.
2. Clique no menu de três pontos na coluna **Ações**.
3.  Selecione **Link Mágico**.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_12.png)
4. Verifique os detalhes do fornecedor.
5.  Clique em **Enviar** para enviar o link de registro por e-mail.

    ![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/supplier_portal_13.png)

## Como Funciona o Processo de Registro para o Fornecedor?

Após o envio de um e-mail de convite, o fornecedor deve completar o processo de registro para acessar o **Portal do Fornecedor**.

Um guia detalhado passo a passo sobre o processo de registro pode ser encontrado [aqui](../../end-user-and-partner-section/end-user-section/supplier-portal/supplier-registration.md).

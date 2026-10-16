---
description: Como configurar o Power BI
---

# Conectar via ClickHouse

Este guia mostra como conectar o **ClickHouse** ao **Power BI Desktop** usando o **driver ODBC**. Ele aborda a instalação do driver, a configuração do ODBC, a integração com o Power BI e a configuração da atualização de dados.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}

#### 1. Instale o driver ODBC do ClickHouse

* Baixe o **driver ODBC do ClickHouse** mais recente em:
  * [ClickHouse GitHub - clickhouse-odbc](https://github.com/ClickHouse/clickhouse-odbc)
* Execute o instalador e siga o assistente de configuração.

#### 2. Configure a fonte de dados ODBC

* Abra o **Administrador de Fonte de Dados ODBC (64 bits)** pelo Painel de Controle ou pela Pesquisa do Windows.
* Vá para a guia **DSN do Sistema** e clique em **Adicionar**.
* Selecione **ClickHouse ODBC Driver** na lista e clique em **Concluir**.
*   Preencha os campos obrigatórios. Você encontra as informações necessárias em:

    **DocBits** → **Settings** → **Document Processing** → **Module** → **AI Dashboard** → **ClickHouse Direct Access**

    <figure><img src="../../.gitbook/assets/clickhouse_direct_access_settings.png" alt="Configurações do ClickHouse Direct Access"><figcaption></figcaption></figure>

    **Campos obrigatórios:**

    * **Nome**: um nome para a conexão (por exemplo, `ClickHouse_Prod`)
    * **Descrição**: uma breve descrição para sua referência (opcional)
    * **Host**: copie o valor do host do DocBits
    * **Porta**: copie o valor da porta do DocBits
    * **Banco de dados**: copie o nome do banco de dados do DocBits
    * **Nome de usuário**: copie o nome de usuário do DocBits
    * **Senha**: copie a senha do DocBits

#### 3. Conecte o ClickHouse ao Power BI

* Abra o **Power BI Desktop**.
*   Selecione **Obter Dados** → **ODBC** → **Conectar**.\\

    <figure><img src="../../.gitbook/assets/clickhouse_1.png" alt="Obter dados ODBC no Power BI"><figcaption></figcaption></figure>
*   Na lista de DSN, selecione a fonte configurada (por exemplo, `ClickHouse_Prod`).\\

    <figure><img src="../../.gitbook/assets/powerbi_select_dsn.png" alt="Seleção do DSN no Power BI"><figcaption></figcaption></figure>
* Clique em **OK**. Insira as credenciais novamente, se solicitado.

#### 4. Carregue e transforme os dados

* No painel **Navegador**, navegue e selecione as tabelas ou views que deseja importar.
* Escolha:
  * **Carregar**: para importar diretamente
  *   **Transformar Dados**: para abrir o Power Query e moldar os dados\\

      <figure><img src="../../.gitbook/assets/powerbi_navigator_load_transform.png" alt="Navegador do Power BI com as opções Carregar e Transformar Dados"><figcaption></figcaption></figure>

#### 5. Visualize seus dados

* Use a tela de relatórios para criar visualizações.
* Arraste campos, adicione segmentações de dados, escolha tipos de gráfico e use expressões **DAX** conforme necessário.
* Aproveite o **Editor do Power Query** para limpar ou pivotar seus dados do ClickHouse antes de criar os visuais.
* Documentação do Power BI: [https://learn.microsoft.com/en-us/power-bi/](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Ative a atualização agendada (opcional)

<mark style="color:red;">**Observação:**</mark> **Requer Power BI Pro ou Premium + Gateway**

* Para manter seus relatórios sincronizados com o ClickHouse:
* Publique o arquivo `.pbix` no **Serviço do Power BI**.
* Instale o **Gateway do Power BI** (modo Padrão) em uma máquina com acesso de rede ao ClickHouse.
* No Serviço do Power BI:
  * Vá para o seu conjunto de dados → **Configurações** → **Atualização agendada**
  * Mapeie o seu DSN e forneça as credenciais
* Mais informações [aqui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

#### 7. Exemplos de dashboards e visualizações de dados

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Exemplo de dashboard do Power BI 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Exemplo de dashboard do Power BI 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Exemplo de dashboard do Power BI 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Exemplo de dashboard do Power BI 4"><figcaption></figcaption></figure></div>

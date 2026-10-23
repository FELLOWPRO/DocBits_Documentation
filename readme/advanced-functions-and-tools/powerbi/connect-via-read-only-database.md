# Conectar via banco de dados somente leitura

Este guia mostra como conectar o **banco de dados somente leitura do DocBits ao Power BI Desktop** usando o **driver ODBC do PostgreSQL**. Ele aborda a instalação do driver, a configuração do ODBC, a integração com o Power BI e a atualização agendada.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}

#### 1. Instale o driver ODBC do PostgreSQL

* Baixe o driver ODBC do PostgreSQL mais recente (**psqlODBC**) no site oficial:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Execute o instalador e siga o assistente de configuração.

#### 2. Configure a fonte de dados ODBC

* Abra o **Administrador de Fonte de Dados ODBC (64 bits)** pelo Painel de Controle ou pela Pesquisa do Windows.
* Vá para a guia **DSN do Sistema** e clique em **Adicionar**.
* Selecione o driver **PostgreSQL Unicode(x64)** na lista e clique em **Concluir**.
* Preencha os campos obrigatórios com as credenciais disponíveis em:\n  **DocBits → Settings → Document Processing → Module → AI Dashboard → Read-Only DB Access**

<figure><img src="../../.gitbook/assets/connect_read_only_4.png" alt="Painel Navigator do Power BI mostrando a fonte de dados ODBC dsn-Sandbox-Read_Only com o esquema public e suas tabelas listadas"><figcaption></figcaption></figure>

**Campos obrigatórios:**

* **Nome:** um nome para a conexão (por exemplo, `Sandbox-Read_Only`)
* **Servidor:** copie o valor do host do DocBits
* **Porta:** copie o valor da porta do DocBits
* **Banco de dados:** copie o nome do banco de dados do DocBits
* **Nome de usuário:** copie o nome de usuário do DocBits
* **Senha:** copie a senha do DocBits
* **Modo SSL:** defina como **Require** (garante a comunicação criptografada)

#### 3. Conecte o banco de dados somente leitura ao Power BI

* Abra o **Power BI Desktop**.
*   Selecione **Obter Dados** → **ODBC** → **Conectar**.

    <figure><img src="../../.gitbook/assets/powerbi_get_data_odbc.png" alt="Obter dados ODBC no Power BI"><figcaption></figcaption></figure>
* Na lista de DSN, selecione a fonte configurada (por exemplo, `Sandbox-Read_Only`).

<figure><img src="../../.gitbook/assets/connect_read_only_3.png" alt="Power BI Navigator com tabelas de sandbox-doc2api como supplier group, supplier header e task assignment, com os botões Select Related Tables, Load e Transform Data"><figcaption></figcaption></figure>

* Clique em **OK**. Insira as credenciais novamente, se solicitado.
  * Se surgir `password authentication failed for user`, verifique o servidor, a base de dados, o utilizador e a palavra-passe. Introduza a palavra-passe real na caixa de diálogo de credenciais. As chavetas para escape numa cadeia de ligação ODBC fazem parte da sintaxe do controlador e não são uma solução geral para falhas de autenticação.

#### 4. Carregue e transforme os dados

* No painel **Navegador**, expanda a lista de esquemas.
* Abra o esquema **`public`**.
* Selecione as tabelas que deseja importar.

![Painel de Read-Only DB Access do DocBits mostrando os campos de nome de usuário, senha, banco de dados, host e porta e a lista de tabelas disponíveis](../../.gitbook/assets/connect_read_only_1.png)

![Diálogo From ODBC do Power BI com o menu suspenso Data source name (DSN) e opções avançadas](../../.gitbook/assets/connect_read_only_2.png)

* Escolha:
  * **Carregar** → importar diretamente para o Power BI
  * **Transformar Dados** → abrir o Power Query para moldar e filtrar os dados antes de carregá-los

#### 5. Visualize seus dados

* Use a tela de relatórios do Power BI para criar dashboards.
* Arraste campos, adicione segmentações de dados, escolha tipos de gráfico e aplique cálculos DAX.
* Use o **Editor do Power Query** para limpar ou combinar dados antes de criar os visuais.
* Referência: [Documentação do Power BI](https://learn.microsoft.com/en-us/power-bi/)

#### 6. Ative a atualização agendada (opcional)

A atualização agendada depende da licença ou capacidade do espaço de trabalho, do conector e do modo de ligação. Para esta ligação ODBC, configure um gateway acessível com o controlador, o DSN e as credenciais adequados. Consulte os requisitos atuais na documentação oficial.

* Para manter seus relatórios sincronizados com o PostgreSQL:
* Publique o arquivo `.pbix` no **Serviço do Power BI**.
* Instale o **Gateway do Power BI** (modo Padrão) em uma máquina com acesso de rede ao PostgreSQL.
* No Serviço do Power BI:
  * Vá para o seu conjunto de dados → **Configurações** → **Atualização agendada**
  * Mapeie o seu DSN e forneça as credenciais
* Mais informações [aqui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).&#x20;

#### 7. Exemplos de dashboards e visualizações de dados&#x20;

<div><figure><img src="../../.gitbook/assets/powerbi_dashboard_example_1.png" alt="Exemplo de dashboard do Power BI 1"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_2.png" alt="Exemplo de dashboard do Power BI 2"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_3.png" alt="Exemplo de dashboard do Power BI 3"><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/powerbi_dashboard_example_4.png" alt="Exemplo de dashboard do Power BI 4"><figcaption></figcaption></figure></div>

[Documentação oficial — ODBC](https://learn.microsoft.com/en-us/power-query/connectors/odbc)

[Documentação oficial — psqlODBC](https://odbc.postgresql.org/docs/config-opt.html)

[Documentação oficial — Power BI](https://learn.microsoft.com/en-us/power-bi/connect-data/refresh-scheduled-refresh)

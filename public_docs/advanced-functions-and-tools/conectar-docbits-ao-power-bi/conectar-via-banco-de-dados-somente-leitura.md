# Conectar via Banco de Dados Somente Leitura

Este guia o orienta a conectar o **Banco de Dados Somente Leitura do DocBits ao Power BI Desktop** usando o **driver ODBC do PostgreSQL**. Ele abrange a instalação do driver, configuração do ODBC, integração com o Power BI e atualização programada.

{% embed url="https://youtu.be/O1MtuXf_R_M" %}
{% endembed %}


### 1. Instalar o Driver ODBC do PostgreSQL

* Baixe o driver ODBC mais recente do PostgreSQL (**psqlODBC**) no site oficial:
  * [https://www.postgresql.org/ftp/odbc/releases/](https://www.postgresql.org/ftp/odbc/releases/)
* Execute o instalador e siga o assistente de configuração.

### 2. Configurar a Fonte de Dados ODBC

* Abra o **Administrador de Fontes de Dados ODBC (64 bits)** via Painel de Controle ou Pesquisa do Windows.
* Vá para a aba **DSN do Sistema** e clique em **Adicionar**.
* Selecione o driver **PostgreSQL Unicode(x64)** na lista e clique em **Concluir**.
* Preencha os campos obrigatórios com as credenciais de: **DocBits → Configurações → Processamento de Documentos → Módulo → Painel de IA → Acesso ao BD Somente Leitura**

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FupCHowPUuMJ8hO9Y36EY%252Fconnect_read_only_4.png%3Falt%3Dmedia%26token%3D3eb69744-6696-41e2-90be-63295b9b6f6d\&width=768\&dpr=4\&quality=100\&sign=647db68c\&sv=2)

**Campos Obrigatórios:**

* **Nome:** Um nome para a conexão (por exemplo, `Sandbox-Read_Only`)
* **Servidor:** Copie o valor do host do DocBits
* **Porta:** Copie o valor da porta do DocBits
* **Banco de Dados:** Copie o nome do banco de dados do DocBits
* **Nome de Usuário:** Copie o nome de usuário do DocBits
* **Senha:** Copie a senha do DocBits
* **Modo SSL:** Defina como **Requerido** (garante comunicação criptografada)

### 3. Conectar BD Somente Leitura ao Power BI

* Abra o **Power BI Desktop**.
*   Selecione **Obter Dados** → **ODBC** → **Conectar**.

    ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F1aIDfi4Rj6WD9oXsvUjt%252FScreenshot%25202025-05-19%2520163621.png%3Falt%3Dmedia%26token%3D4ec15da7-fa79-4b9e-a83b-cb4b0a545cfd\&width=768\&dpr=4\&quality=100\&sign=59fba2e3\&sv=2)
* Na lista de DSN, selecione sua fonte configurada (por exemplo, `Sandbox-Read_Only`).

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FKPDLjfDw2SRYvzvFKWXq%252Fconnect_read_only_3.png%3Falt%3Dmedia%26token%3Dc67c1362-7f63-479e-a373-974d198f5eb7\&width=768\&dpr=4\&quality=100\&sign=f001e759\&sv=2)

* Clique em **OK**. Insira as credenciais novamente se solicitado.
  * **Nota:** Se você ver o erro **“autenticação de senha falhou para o usuário”**, tente inserir sua senha entre **chaves** `**{}**`.

### 4. Carregar e Transformar Dados

* No painel **Navegador**, expanda a lista de esquemas.
* Abra o esquema `**public**`.
* Selecione as tabelas que deseja importar.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSmtEspL1H6ieOJhtDwYb%252Fconnect_read_only_1.png%3Falt%3Dmedia%26token%3Dd402a928-175e-4904-bd21-592ff114fad7\&width=300\&dpr=4\&quality=100\&sign=464e3a3d\&sv=2) ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F3Phea1Pf3ZBJtMzw3rxi%252Fconnect_read_only_2.png%3Falt%3Dmedia%26token%3D94037886-57e3-440d-bf08-61cd37c65b98\&width=300\&dpr=4\&quality=100\&sign=5ead9fe9\&sv=2)

* Escolha:
  * **Carregar** → Importar diretamente para o Power BI
  * **Transformar Dados** → Abrir o Power Query para moldar e filtrar antes de carregar

### 5. Visualizar Seus Dados

* Use o canvas de relatório do Power BI para construir painéis.
* Arraste campos, adicione filtros, escolha tipos de gráficos e aplique cálculos DAX.
* Use o **Editor do Power Query** para limpar ou unir dados antes de criar visuais.
* Referência: [Documentação do Power BI](https://learn.microsoft.com/en-us/power-bi/?utm_source=chatgpt.com)

### 6. Ativar Atualização Programada (Opcional)

**Nota:** **Requer Power BI Pro ou Premium + Gateway**

* Para manter seus relatórios em sincronia com o ClickHouse:
* Publique seu arquivo `.pbix` no **Serviço do Power BI**.
* Instale o **Gateway do Power BI** (modo Padrão) em uma máquina com acesso à rede do ClickHouse.
* No Serviço do Power BI:
  * Vá para seu conjunto de dados → **Configurações** → **Atualização Programada**
  * Mapeie seu DSN e forneça credenciais
* Mais informações [aqui](https://learn.microsoft.com/en-us/power-bi/connect-data/service-gateway-deployment-guidance).

### 7. Exemplo de Painéis e Visualizações de Dados

![](<../../.gitbook/assets/example_4 (1).avif>)![](<../../.gitbook/assets/example_3 (1).avif>)![](<../../.gitbook/assets/example_2 (1).avif>)![](<../../.gitbook/assets/example_1 (1).avif>)

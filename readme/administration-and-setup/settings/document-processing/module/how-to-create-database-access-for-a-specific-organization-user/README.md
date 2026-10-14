# Como criar acesso ao banco de dados para um usuário específico da organização

### **1. Faça login no DocBits** <a href="#id-1.-login-to-the-docbits" id="id-1.-login-to-the-docbits"></a>

1. Acesse a página de login do seu aplicativo.
2. Insira suas credenciais (nome de usuário e senha) para fazer login.

### **2. Acesse as configurações** <a href="#id-2.-access-the-settings" id="id-2.-access-the-settings"></a>

1. Depois de fazer login, localize o ícone de **Configurações** (engrenagem ⚙️) na barra lateral esquerda.
2. Clique em **Configurações** para abrir o painel de configuração do sistema.

### **3. Abra o módulo Document Processing** <a href="#id-3.-open-the-document-processing-module" id="id-3.-open-the-document-processing-module"></a>

1. Em **Configurações**, localize a seção **Document Processing**.
2. Em **Document Processing**, encontre e clique na opção **Module**.
   * Isso abrirá a página de configuração do módulo, onde você pode prosseguir com a criação do usuário para o banco de dados.

### 4. Passos para ativar e acessar o AI Document e o usuário do banco de dados: <a href="#id-4.-steps-to-enable-and-access-the-ai-document-and-database-user" id="id-4.-steps-to-enable-and-access-the-ai-document-and-database-user"></a>

1. **Alterne os recursos**:
   * Use as chaves à direita para ativar ou desativar recursos específicos:
     * **AI Document Warehouse**: ative esta opção para habilitar o acesso aos recursos de IA.
     * **DB Access**: ative esta opção para conceder acesso ao banco de dados ao usuário.
2. **Credenciais do banco de dados**:
   * O painel fornece os seguintes detalhes de conexão com o banco de dados:
     * **Username**: um nome de usuário exclusivo é exibido
     * **Password**: certifique-se de armazenar ou copiar a senha com segurança
     * **Database**: o nome do banco de dados
     * **Host**: o nome do host
     * **Port**: a porta
     * **SSL Mode:** a conexão exige `sslmode=require` para uma comunicação segura.
3. **Copie as credenciais**:
   * Use os ícones de cópia ao lado de cada campo para copiar rapidamente as credenciais e usá-las no seu cliente de banco de dados ou aplicativo.
4. **Conexão via DBeaver**:
   * Conectar via Host
     * escolha PostgreSQL
     * Preencha as informações necessárias
     * mude para a guia SSL e marque Use SSL. Role até SSL mode e selecione require
   * Conectar via URL
     * Preencha as informações necessárias:\n - substitua Host pelas informações de host fornecidas\n - substitua Port pelas informações de porta fornecidas\n - substitua Database pelas informações de banco de dados fornecidas\n - em Username, selecione as informações de nome de usuário fornecidas\n - em Password, selecione as informações de senha fornecidas
5. **Teste a conexão**:
   * Clique no botão **"Test Connection"** para garantir que as credenciais e os detalhes da conexão estejam corretos.
   * Se o teste for bem-sucedido, prossiga com a conexão.
6. **Explore o banco de dados**:
   * Depois de conectado, navegue até a seção de **schema** ou **tabelas** no seu cliente de banco de dados.
   * Confira as tabelas disponíveis.

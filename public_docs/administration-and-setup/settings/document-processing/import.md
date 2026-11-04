# Importar

## Visão Geral

Nas configurações de **Importar**, você pode configurar opções específicas de documentos para importação ou configurar importações automatizadas via FTP ou email. Esta página fornece uma visão detalhada de todas as configurações disponíveis.

## Como Acessar

1.  Navegue até **Configurações** -> **Processamento de Documentos** -> **Importar**

    <figure><img src="../../../.gitbook/assets/ftp_0.png" alt=""><figcaption></figcaption></figure>

## **Configurações do Documento**

* **Restringir a páginas**: Esta configuração permite limitar o processamento a um certo número de páginas por documento. O padrão é **60 páginas**, o que significa que documentos que excedem esse limite serão reduzidos para **60 páginas**, e quaisquer **páginas restantes serão descartadas.**
* **Dias de Condições de Pagamento**: Define as condições de pagamento padrão (em dias) que podem ser aplicadas aos documentos.
* **Padrão de Data**: Define o padrão de como as datas devem ser reconhecidas e formatadas dentro dos documentos importados.

<figure><img src="../../../.gitbook/assets/document_settins_1.png" alt=""><figcaption></figcaption></figure>

## **Importação via FTP**

### Requisitos

Para usar FTP para importar dados automaticamente, certifique-se de que os seguintes requisitos sejam atendidos:

* Servidor FTP corretamente configurado e compatível com Linux
* Nome do Host FTP, Nome de Usuário e Senha
* Pasta de Importação dedicada

### Adicionar nova conexão

1.  Para adicionar uma nova conexão, clique no botão **Adicionar** na seção FTP.

    <figure><img src="../../../.gitbook/assets/ftp_7.png" alt=""><figcaption></figcaption></figure>
2.  Insira suas credenciais FTP nos campos designados. O campo da Chave da API será preenchido automaticamente.

    * **Tipo:** Especifica o protocolo FTP a ser usado. Você pode escolher entre **FTP**, **FTPS** ou **SFTP**.
    * **Porta:** Especifica o número da porta a ser usado para o protocolo FTP selecionado.
    * **Nome do Servidor (obrigatório):** O endereço do servidor de onde os documentos serão recuperados.
    * **Nome de Usuário (obrigatório):** O nome de login usado para acessar o servidor FTP.
    * **Senha (obrigatório):** A senha associada ao nome de usuário para acessar o servidor FTP.
    * **Padrões de correspondência de nome de arquivo:** Para especificar quais arquivos importar com base em seus nomes.
    * **Sub-Organizações:** Selecione a sub-organização à qual a importação via FTP deve se aplicar.
    * **Chave da API (obrigatório):** Este campo será preenchido automaticamente com base na organização em que você está logado.
    * **Diretório Principal:** Especifica o diretório no servidor FTP de onde os arquivos serão importados.
    * **Diretório de Importação:** Permite especificar um subdiretório dentro do diretório principal de onde os arquivos serão importados.
    * **Arquivar Após Importação:** Permite arquivar arquivos após a importação. Uma vez ativado, você pode especificar o diretório para onde os arquivos devem ser movidos após uma importação bem-sucedida.
    * **Incluir Arquivos de Subpasta:** Quando ativado, subdiretórios dentro do diretório principal também serão pesquisados por arquivos a serem importados.

    <figure><img src="../../../.gitbook/assets/ftp_4.png" alt=""><figcaption></figcaption></figure>
3. Depois de inserir todos os detalhes necessários do seu FTP, clique em **SALVAR**.
4. Após salvar sua conexão, você pode ativá-la clicando nos três pontos na coluna **Ação** da sua conexão e, em seguida, selecionando **Ativar**.

### Ações para FTP

Você pode clicar nos três pontos na coluna **Ação** para acessar as seguintes opções para sua conexão:

<figure><img src="../../../.gitbook/assets/ftp_5.png" alt="" width="158"><figcaption></figcaption></figure>

* **Testar Conexão:** Testa a conexão com seu servidor FTP.
* **Logs de Conexão:** Abre os logs da sua conexão FTP, incluindo mensagens de erro, se houver problemas.
* **Ativar/Desativar:** Ativa/desativa sua conexão.
* **Editar:** Permite que você faça alterações na sua conexão.
* **Excluir:** Exclui sua conexão.

## **Importação via Email**

Você pode configurar uma importação de email que importa automaticamente documentos da sua caixa de entrada assim que eles chegam. Você pode escolher configurar uma conexão IMAP ou OAuth.

<mark style="color:red;">**Nota**</mark>: Apenas documentos com os seguintes tipos de arquivo serão importados:

* `.pdf`
* `.tiff` / `.tif`
* `.eml`
* `.dat`
* `.xml`
* `.edi`
* `.purchaseorder`

### Adicionar nova conexão IMAP

1.  Para adicionar uma nova conexão IMAP, clique no botão **Adicionar** na seção **Importação de Email**.

    <figure><img src="../../../.gitbook/assets/email_1.png" alt=""><figcaption></figcaption></figure>
2. Selecione IMAP como o protocolo.
3. Insira suas credenciais de email nos campos designados. O campo da Chave da API será preenchido automaticamente.
   * **Criptografia:** Selecione o tipo de criptografia a ser usado — **SSL** ou **TLS**.
   * **Nome do servidor:** O endereço do servidor de email.
   * **Nome de Usuário:** O identificador usado para sua configuração de importação de email no DocBits.
   * **E-mail:** O endereço de email usado para importar documentos para o sistema.
   * **Senha:** A senha associada ao endereço de email fornecido.
   * **Sub-Organizações:** Selecione a sub-organização à qual a importação de email deve se aplicar.
   * **Chave da API:** Este campo será preenchido automaticamente com base na organização em que você está logado.
   * **Enviar Notificação de Erro de Importação para este Endereço de Email:** Especifique um endereço de email para receber notificações de erro se algo der errado durante o processo de importação.
   * **Porta:** Especifica o número da porta a ser usado para a configuração de importação de email selecionada.
   * **Pasta:** Selecione uma pasta da qual os documentos serão importados.\
     <mark style="color:red;">**Nota**</mark>: A opção **Pasta** torna-se disponível apenas após você ter criado com sucesso uma conexão IMAP. Para adicionar uma pasta após a criação, clique nos três pontos na coluna **Ação**, em seguida, selecione **Editar**. A opção deve agora estar disponível.
   * **Mover Emails para Outra Pasta:** Quando ativado, permite que você especifique uma pasta para onde os emails serão movidos após uma importação bem-sucedida.\
     <mark style="color:red;">**Nota**</mark>: A opção **Mover Emails para Outra Pasta** torna-se disponível apenas após você ter criado com sucesso uma conexão IMAP. Para ativar esta configuração, clique nos três pontos na coluna **Ação**, em seguida, selecione **Editar**. A opção deve agora estar disponível.
   * **Mesclar Documentos Anexados:** Combina vários documentos anexados em um único documento.
   * **Enviar Email ao Remetente após Importação:** Envia um email de confirmação ao remetente original após a conclusão da importação. Uma vez ativado, você pode especificar o assunto e o corpo do email.
   * **Bloquear Importação de Nomes de Arquivo Duplicados:** Impede a importação se um documento com o mesmo nome já existir.
4. Após salvar sua conexão, você pode ativá-la clicando nos três pontos na coluna **Ação** da sua conexão e, em seguida, selecionando **Ativar**.

### Ações para IMAP

Você pode clicar nos três pontos na coluna **Ação** para acessar as seguintes opções para sua conexão:

<figure><img src="../../../.gitbook/assets/email_7.png" alt="" width="145"><figcaption></figcaption></figure>

* **Testar Conexão:** Testa a conexão com seu cliente IMAP.
* **Logs de Conexão:** Abre os logs da sua conexão de email, incluindo quaisquer mensagens de erro que ocorram durante o processo.
* **Log de Importação:** Abre os logs de importações passadas para a respectiva conexão, incluindo quaisquer mensagens de erro que ocorreram durante o processo.
* **Ativar/Desativar:** Ativa/desativa sua conexão.
* **Editar:** Permite que você faça alterações na sua conexão.
* **Excluir:** Exclui sua conexão.

### Adicionar nova conexão OAuth Office365

1.  Para adicionar uma nova conexão OAuth Office365, clique no botão **Adicionar** na seção **Importação de Email**.

    <figure><img src="../../../.gitbook/assets/email_1.png" alt=""><figcaption></figcaption></figure>
2.  Selecione **OAuth Office365** como o protocolo e clique em **Autenticar**.

    <figure><img src="../../../.gitbook/assets/email_3.png" alt=""><figcaption></figcaption></figure>
3.  Você será redirecionado para uma página da Microsoft onde será solicitado que você insira um código. Para recuperar esse código, volte para o DocBits — o código será exibido lá, conforme mostrado abaixo. Copie o código e insira-o na página da Microsoft. Depois, você será solicitado a inserir suas credenciais da Microsoft.

    <figure><img src="../../../.gitbook/assets/email_4.png" alt=""><figcaption></figcaption></figure>
4. Siga os passos na página da Microsoft. Quando terminar, volte para o DocBits e clique em **Concluir Autenticação**.
5.  Agora você pode configurar as seguintes configurações:

    * **Sub-Organizações:** Selecione a sub-organização à qual a importação de email deve se aplicar.
    * **Usar Pasta:** Selecione uma pasta da qual os documentos serão importados.
    * **Usar Caixa de Correio Compartilhada:** Especifique o endereço de email compartilhado de onde os documentos devem ser importados.
    * **Mover Email para outra pasta:** Especifique uma pasta para a qual os emails devem ser movidos após uma importação bem-sucedida.
    * **Enviar Notificação de Erro de Importação para este Endereço de Email:** Especifique um endereço de email para receber notificações de erro se algo der errado durante o processo de importação.

    <figure><img src="../../../.gitbook/assets/email_5.png" alt=""><figcaption></figcaption></figure>
6. Uma vez que você tenha configurado o comportamento desejado, você pode começar a importar emails clicando em **Importar** ou salvar suas alterações clicando em **Salvar**.
7. Após salvar sua conexão, você pode ativá-la clicando nos três pontos na coluna **Ação** da sua conexão e, em seguida, selecionando **Ativar**.

### Ações para OAuth Office365

Você pode clicar nos três pontos na coluna **Ação** para acessar as seguintes opções para sua conexão:

<figure><img src="../../../.gitbook/assets/email_6.png" alt="" width="148"><figcaption></figcaption></figure>

* **Logs de Conexão:** Abre os logs da sua conexão de email, incluindo quaisquer mensagens de erro que ocorram durante o processo.
* **Log de Importação:** Abre os logs de importações passadas para a respectiva conexão, incluindo quaisquer mensagens de erro que ocorreram durante o processo.
* **Ativar/Desativar:** Ativa/desativa sua conexão.
* **Editar:** Permite que você faça alterações na sua conexão.
* **Excluir:** Exclui sua conexão.

### Log de Importação

Você pode visualizar o log de importação de todas as conexões de email criadas, incluindo quaisquer mensagens de erro que ocorreram durante o processo, clicando no botão **Log de Importação** no canto superior direito da seção de Importação de Email.

<figure><img src="../../../.gitbook/assets/email_8.png" alt=""><figcaption></figcaption></figure>

Você pode filtrar os logs por assunto ou remetente, classificar colunas em ordem crescente ou decrescente clicando nos cabeçalhos das colunas e reorganizar colunas usando arrastar e soltar.

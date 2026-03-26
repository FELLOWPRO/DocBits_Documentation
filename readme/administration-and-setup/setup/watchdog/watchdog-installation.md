# Instalação do WatchDog

<figure><img src="../../../.gitbook/assets/watchdog-infographic-pt.png" alt="WatchDog Infographic"><figcaption></figcaption></figure>

### Configurando o WatchDog no DocBits

1. **Acessar Configurações do WatchDog**
   * Navegue até **Configurações → Processamento de Documentos → WatchDog**.
2. **Configurações da Pasta**
   * Defina os caminhos onde o WatchDog encontra e processa documentos.
   *   Os caminhos das pastas devem corresponder àqueles criados durante a instalação:

       * `C:/WatchDog/Read`
       * `C:/WatchDog/Processed`

       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FzG1EFmtSO4AxZjWir401%252Fimage.png%3Falt%3Dmedia%26token%3Dc356e023-8cfb-4f45-b863-b27c5af1d9df\&width=768\&dpr=4\&quality=100\&sign=1b1ae0c4\&sv=2)
   * <mark style="color:red;">**Nota:**</mark>**&#x20;É recomendável usar caminhos locais. Estes devem corresponder às pastas na Instalação do DocBits**
3. **Configurações Gerais**
   *   Selecione os tipos de documentos a serem processados marcando as caixas de seleção correspondentes.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZbCt5UHd37PdNZsVItdt%252Fimage.png%3Falt%3Dmedia%26token%3Db3c3f203-0f60-42a0-bd56-ee70c204f5e8\&width=768\&dpr=4\&quality=100\&sign=becd5e31\&sv=2)
   * **Divisor de Código de Barras:** Quando ativado, habilita a divisão de código de barras.
   * **Operador DocBits:** Quando habilitado, abre um navegador Chrome em segundo plano para o Operador DocBits.
   * **Destino de Exportação:** Define o destino da exportação.
     * **Infor:** Documentos são exportados para o Infor.
     * **Pasta de Exportação:** Documentos são exportados para uma pasta definida que pode ser configurada abaixo.
4. **Configurações de Exportação**
   * Exibe todas as exportações configuradas para **processamento local**.
   *   Mostra o timestamp da **última conexão bem-sucedida** para cada configuração.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FRvK5qn6EggWJxcSYNP5J%252Fimage.png%3Falt%3Dmedia%26token%3D195b9cc6-c5ac-4ee6-90da-b3ee9696ee30\&width=768\&dpr=4\&quality=100\&sign=3bc11ec5\&sv=2)
5. **Configuração bod\_mapping (Opcional)**
   * <mark style="color:red;">**Campos obrigatórios:**</mark> Antes de adicionar mapeamentos de metadados personalizados, você deve definir os seguintes dois valores
     * **`file_name`**
     * **`pdf_path`**
   *   Clique em **Adicionar Linha** para definir mapeamentos de metadados.\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlzUqcr51kq18OrmYAR8X%252Fimage.png%3Falt%3Dmedia%26token%3D3035122b-f1d3-44cc-bfe6-5230943bd77d\&width=768\&dpr=4\&quality=100\&sign=e98d5a1b\&sv=2)
   * **Valor:** Especifica o nome do campo para os metadados.
   * **Caminho:** A expressão XPath apontando para os dados XML que devem ser atribuídos ao campo.
   * **Ícone de Lixeira:** Usado para excluir uma linha específica.
6. **Baixar a Configuração**
   * Salvar a configuração
   *   Baixar a configuração\


       ![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FZXiz4KB7QpnaqD9XwX3o%252Fimage.png%3Falt%3Dmedia%26token%3D04c9f8dc-7d79-443f-9ce4-6d4214edc98b\&width=768\&dpr=4\&quality=100\&sign=574a4218\&sv=2)

### Guia de Instalação do WatchDog

1. **Criar Pastas Necessárias**
   * Crie um diretório principal: `C:/WatchDog`
   * Dentro de `C:/WatchDog`, crie as seguintes subpastas: **Nota:** estas devem corresponder às pastas no DocBits.
     * `C:/WatchDog/Read`
     * `C:/WatchDog/Processed`
   * <mark style="color:red;">**Nota:**</mark>**&#x20;É recomendável usar caminhos locais. Estes devem corresponder às pastas na Configuração do DocBits**
2. **Baixar o WatchDog**
   * Baixe a versão mais recente do `WatchDog.exe` de: [https://github.com/Fellow-Consulting-AG/WatchDog](https://github.com/Fellow-Consulting-AG/WatchDog)
   * Coloque o arquivo `WatchDog.exe` baixado em `C:/WatchDog`.
   * Coloque o arquivo `watchdog-config.json` baixado em `C:/WatchDog`.
   * Abra o `watchdog-config.json` e altere o **config\_path.**
   * Neste exemplo:
     * `"config_path": "C:/WatchDog/watchdog-config.json"`
3. **Instalar o WatchDog**
   * Abra o **Prompt de Comando (CMD)** com **direitos de Administrador**.
   * Navegue até a pasta do WatchDog.
   *   Execute o seguinte comando para instalar o WatchDog:

       `WatchDog.exe install`
4. **Iniciar o Serviço WatchDog**
   *   Execute o seguinte comando no CMD:

       `WatchDog.exe start`
5. **Definir Tipo de Inicialização**
   * Abra **Serviços** (Pressione `Win + R`, digite `services.msc` e pressione **Enter**).
   * Localize **WatchDog** na lista de serviços.
   * Clique duas vezes para abrir suas propriedades.
   * Defina o **Tipo de Inicialização** como **Automático (Início Atrasado)**.
   * Clique em **OK**.

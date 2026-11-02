# M3

## Passo 1: Criar um Connection Point

1. Navegue para **OS > ION > Connect > Connection Points**
2. Clique em **Add** e selecione **IMS via API Gateway** como tipo de conexão.
3. Configure as seguintes definições:
   * **Name**: Defina como `DocBits_Export`.
   * **Description**: Defina como `DocBits_Export`.
   * **Desmarque**: _Application has IMS End Point_.
   * **ION API Client ID**:
     * Abra o ficheiro ION API.
     * Procure por `"ci"` dentro do ficheiro.
     * Copie o valor dentro das aspas (sem as aspas).

![Janela Infor Application Connection Point IMS via API Gateway com os separadores Usage, Connection e Documents, o nome DocBits_Export, a opção Application has IMS End Point não selecionada, o campo ION API Client ID e o Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_1.png)

4. Em **Documents**, adicione `Sync.CaptureDocument`.

![Separador Connection do ponto de aplicação com o nome DocBits_Export, o documento sync.captureDocument como Send from Application e o Logical ID inforims.docbits_export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_2.png)

5. Clique em **Save** para finalizar a configuração.

## Passo 2: Carregar Mappings

{% file src="../../../.gitbook/assets/CaptureDocument_to_ProcessSupplierInvoice.xml" %}

1. Descarregue o ficheiro M3 Mapping.
2. Navegue para **Infor** > **OS** > **ION** > **Connect** > **Mappings**.
3. Clique em **Import** e selecione o ficheiro de mapping apropriado para **M3**.

![Página Mappings do ION Desk com o campo de pesquisa, os controlos de filtro e o botão Add](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_3.png)

4. Depois de os ficheiros serem importados, aprove os mappings para os ativar.

![Mapeamento importado com a origem Sync.CaptureDocument e o destino Process.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_4.png)

## Passo 3: Criar o Data Flow

1. Navegue para **OS** -> **ION** -> **Connect** -> **Data Flows**.
2. Clique em **Add** e selecione **Document Flow**.
3. Preencha os detalhes:
   * **Name**: `DocBits_Export_to_M3`
4. Adicione nós ao fluxo:

#### Application Node

1. Adicione um **Application Node** ao fluxo.
   * **Name**: `DocBits` ou `DocBits-Export`.
2. Clique em **Add** e selecione o **Connection Point** criado no Passo 1.

![Fluxo de dados no ION Desk com a paleta de nós em cima e o painel Application Activity Properties à direita com o nome DocBits-Dev-Demo-Export](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_5.png)

3. Clique no **Document Icon** ao lado do Application Node.
   * Clique em **Add** e selecione `Sync.CaptureDocument`.

![Fluxo de dados no ION Desk com o nó de aplicação selecionado e o painel Documents aberto com a entrada Sync.CaptureDocument](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_6.png)

#### Mapping Node

1. Adicione um **Mapping Node** à direita do Application Node.
   * **Name**: `Capt2process`.
   * **Mapping**: `CaptureDocument_to_ProcessSupplierInvoice`.

![Fluxo de dados no ION Desk com o nó de mapeamento selecionado e o painel Mapping Properties à direita com o nome e o mapeamento SyncCaptDoc_SyncSuppInv](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_7.png)

#### Application Node

1. Adicione um **Application Node** à direita do Mapping Node anterior.
   * **Name**: `M3`.
2. Clique em **Add** e selecione a **M3 Application** do cliente.

![Fluxo de dados no ION Desk com o nó de aplicação M3 selecionado e o painel Application Activity Properties à direita com a entrada M3 BODs](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_8.png)

3. Clique no **Document Icon** ao lado do Application Node.
   * Clique em **Add** e selecione `Acknowledge.SupplierInvoice`.

![Fluxo de dados no ION Desk com o nó de aplicação M3 selecionado e o painel Documents aberto com a entrada Acknowledge.SupplierInvoice](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_9.png)

#### API Node

1. Adicione um **API Node** à direita do Application Node.
   * **Name**: `DocBits-Error`.
   * **ION API Connector**: `DocBits_Import`.
   * Se `DocBits_Import` não existir, consulte o **Passo 1** e o **Passo 2** da documentação Import from M3 para criar o Connection Point.

![Fluxo de dados no ION Desk com o nó de API selecionado e o painel ION API Activity Properties à direita com o ION API Connector DocBits Dev Demo-Import](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_10.png)

#### Guardar e ativar o Flow

* Depois de todos os nós serem adicionados e configurados, clique em **Save**.
* Ative o fluxo para concluir a configuração.

![Fluxo de dados no ION Desk com os nós DocBits_Demo_to_M3, o nó de mapeamento, o nó M3 e o nó de erro ligados em fila e o botão REMOVE CONNECTION POINTS por cima da área de trabalho](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/export_to_m3_from_docbits_11%20\(1\).png)

## Passo 4: Configurar Export no DocBits

### On-Premise:

1. Abra **DocBits**.
2.  Navegue para **Configurações > Processamento de documentos > Exportar**.

    ![Página de definições do DocBits com o grupo de navegação Document Processing expandido e as entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Crie uma nova exportação:
   * **Selecionar**: **Infor IDM + ION BOD**.
   * **Título**: Escolha um título significativo.
   * **Tipo de documento**: Defina como **Fatura**.
   * **Sub-organização**: Pode ser deixado vazio ou definido para uma sub-organização específica se necessário.
4. **Carregue os ficheiros necessários**:
   * **ION Mapping File**: Pode encontrá-lo em **Infor OS → API Gateway → Authorized Apps**. Procure pela aplicação **DocBits**, abra-a e descarregue as credenciais.
   * **IDM Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).
   * **BOD Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).

### Cloud:

1. Abra **DocBits**.
2.  Navegue para **Configurações > Processamento de documentos > Exportar**.

    ![Página de definições do DocBits com o grupo de navegação Document Processing expandido e as entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Crie uma nova exportação:
   * **Selecionar**: **Infor IDM + M3 (API)**.
   * **Título**: Escolha um título significativo.
   * **Tipo de documento**: Defina como **Fatura**.
   * **Sub-organização**: Pode ser deixado vazio ou definido para uma sub-organização específica se necessário.
4. **Carregue os ficheiros necessários**:
   * **ION Mapping File**: Pode encontrá-lo em **Infor OS → API Gateway → Authorized Apps**. Procure pela aplicação **DocBits**, abra-a e descarregue as credenciais.
   * **IDM Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).
   * **M3 Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).

### Cloud com toml:

1. Abra **DocBits**.
2.  Navegue para **Configurações > Processamento de documentos > Exportar**.

    ![Página de definições do DocBits com o grupo de navegação Document Processing expandido e as entradas Documents, Expiry, Import, Rule Management, OCR Settings, Classification and Extraction, Master Data Lookup, List of Values e Module](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/settings_export.png)
3. Crie uma nova exportação:
   * **Selecionar**: **Infor IDM + M3 (API)**.
   * **Título**: Escolha um título significativo.
   * **Tipo de documento**: Defina como **Fatura**.
   * **Sub-organização**: Pode ser deixado vazio ou definido para uma sub-organização específica se necessário.
4. **Carregue os ficheiros necessários**:
   * **ION Mapping File**: Pode encontrá-lo em **Infor OS → API Gateway → Authorized Apps**. Procure pela aplicação **DocBits**, abra-a e descarregue as credenciais.
   * **IDM Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).
   * **M3 toml Mapping File**: (Forneça o caminho do ficheiro relevante ou localização).

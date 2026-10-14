# Importar do Infor M3 para o DocBits via API

## Passo 1: Criar uma API

1. Abra o **Infor OS** e navegue até **API Gateway** > **Available APIs**.
2. Click em **Add**, depois selecione **Create New**.
3. Preencha os detalhes da API:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod`, ou `DocBits-Demo` (baseado no seu ambiente).
   * **Suite Name**: O mesmo que o nome da aplicação.
   * **API Context**: O mesmo que o nome da aplicação.
   * **Description**: O mesmo que o nome da aplicação.
   * **Icon**: Selecione um ícone de documento azul.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Adicione um **Target Endpoint**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Use a URL apropriada para seu ambiente:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod`, ou `Demo` (correspondente ao ambiente).
* **Proxy Context**: O mesmo que o ambiente (`Stage`, `Sandbox`, `Prod`, ou `Demo`).
* **Proxy Security**: Selecione **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Recupere a API key do **DocBits** navegando até **Settings** > **Global Settings** > **Integration**, depois copie a API key e cole-a como o valor da chave.
* Salve a configuração do target endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Adicione Documentação da API:

* Retorne à seção de documentação da API clicando no **Documentation Icon** no Endpoint criado.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Role para baixo até a seção **Documentation** e click em **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod`, ou `DocBits-Demo` (correspondente ao ambiente).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Use a URL do arquivo Swagger apropriado para seu ambiente:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Certifique-se de que não há espaço no final da URL.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* A documentação da API será automaticamente adicionada, e a atualização dos metadados será acionada.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Passo 2: Criar um API Connection Point

1. Navegue até **OS** > **ION** > **Connect** > **Connection Point**.
2. Click em **Add** e selecione **API** como o tipo de conexão.
3. Preencha os detalhes necessários:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Faça upload do arquivo de conta de serviço que foi criado anteriormente.

### Passo 2.1: Adicionar e Configurar Documentos

* Você não precisa adicionar todos os documentos—apenas os necessários.
* Os documentos **Sync.ChartOfAccounts** e **Sync.CodeDefinition** são necessários para contabilização automática.

## Sync.SupplierPartyMaster

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Click em **Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Configure a ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Para **Product**, escolha o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Click em **OK** para confirmar a seleção.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Configure o **Request Body**:
   * Para **File**, selecione **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Configure o Request Body**:
   * Para **File**, selecione **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Configure a ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Configure o Request Body**: Adicione os seguintes valores na seção **Request Body**:
   * Para **idm\_doc\_type**, defina **Value** = `M3_SupplierInvoice`
   * Para **idm\_bod\_id\_field\_name**, defina **Value** = `BOD_AlternateDocumentID_1`
   *   Para **attributes\_map**, defina **Value** =

       ```
       {"Export": "Success"}
       ```
   * Para **acl\_from**, defina **Value** = `Public`
   * Para **acl\_to**, defina **Value** = `Private`
   * Para **set\_to\_error\_on\_rejected**, defina **Value** = `True`
   * Para **delete\_from\_idm\_on\_rejected**, defina **Value** = `True`
   * Para **File**, defina **Input Document = No Compression**.
   * Para **ionapi\_json**: Adicione o conteúdo do arquivo ionapi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Configure o Request Body**:
   * Para **File**, defina **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Configure o Request Body**:
   * Para **File**, defina **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Configure o Request Body**:
   * Para **data\_type**, defina **Value** = `AdvanceShipNotice`
   *   Para **field\_mappings**, defina **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Para **File**, defina **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Configure o Request Body**:
   * Para **data\_type**, defina Value = `ChartOfAccounts`
   *   Para **field\_mappings**, defina Value =

       ```
       {
           "ID": "//DataArea/ChartOfAccounts/IDs/ID",
           "NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
           "AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
           "Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
           "DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
           "Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
           "Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
           "Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
           "Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
           "Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
           "Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
           "Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
           "Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
           "Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
           "Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
           "Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
           "Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
           "Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
           "Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
       }
       ```
   * Para **File**, defina **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Navegue até a aba **Documents** no API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e preencha os seguintes detalhes:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Configure a ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Para **Product**, selecione o endpoint de API criado no **Passo 1: Criar uma API**.
   *   Localize e selecione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Configure o Request Body**:
   * Para **data\_type**, defina Value = `M3Dimension`
   *   Para **field\_mappings**, defina Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Para **File**, defina **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Passo 3: Criar o Document Flow

1. Navegue até **OS** > **ION** > **Connect** > **Data Flows**.
2. Click em **Add** e selecione **Document Flow**.
3. Preencha os campos necessários:
   * **Name**: Use um nome específico para seu ambiente, como `M3-to-DocBits-Stage-Import-API`
   * para stage, `M3-to-DocBits-Sandbox-Import-API` para sandbox, ou `M3-to-DocBits-Prod-Import-API` para produção.
   * **Description**: O mesmo que o nome acima.
4. Configure o Application Node:
   * Em **Application**, defina o **Name** como `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Click no botão **+** e selecione o connection point do cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Click no ícone **Document** ao lado do application node.

    * Selecione todos os documentos que você deseja exportar/sincronizar do LN para o DocBits.
    * Certifique-se de que esses documentos correspondem aos selecionados no **Passo 2: Criar um API Connection Point**.
    * Se algum documento estiver faltando, ele deve ser adicionado ao connection point do cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Configure o API Node:
   * Adicione um node **API** e posicione-o à direita do application node.
   * Preencha os campos necessários:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Use o connection point criado no **Passo 2: Criar um API Connection Point**.
   * Click no ícone **Document** ao lado do stream node. Este deve estar vazio.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Finalize a Configuração:
   * Salve a configuração.
   * Click em **Activate** para completar a configuração.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

# Importazione da Infor M3 a DocBits tramite API

## Passo 1: Creare un'API

1. Apri **Infor OS** e naviga su **API Gateway** > **Available APIs**.
2. Fai clic su **Add**, quindi seleziona **Create New**.
3. Compila i dettagli dell'API:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` o `DocBits-Demo` (in base al tuo ambiente).
   * **Suite Name**: Uguale al nome dell'applicazione.
   * **API Context**: Uguale al nome dell'applicazione.
   * **Description**: Uguale al nome dell'applicazione.
   * **Icon**: Seleziona un'icona documento blu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Aggiungi un **Target Endpoint**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Utilizza l'URL appropriato per il tuo ambiente:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod` o `Demo` (corrispondente all'ambiente).
* **Proxy Context**: Uguale all'ambiente (`Stage`, `Sandbox`, `Prod` o `Demo`).
* **Proxy Security**: Seleziona **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Recupera la chiave API da **DocBits** navigando su **Settings** > **Global Settings** > **Integration**, quindi copia la chiave API e incollala come valore della chiave.
* Salva la configurazione del Target Endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Aggiungi la documentazione API:

* Torna alla sezione della documentazione API facendo clic su **Documentation Icon** nell'Endpoint creato.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Scorri verso il basso fino alla sezione **Documentation** e fai clic su **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` o `DocBits-Demo` (corrispondente all'ambiente).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Utilizza l'URL appropriato del file Swagger per il tuo ambiente:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Assicurati che non ci siano spazi alla fine dell'URL.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* La documentazione API verrà aggiunta automaticamente e verrà attivato l'aggiornamento dei metadati.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Passo 2: Creare un API Connection Point

1. Naviga su **OS** > **ION** > **Connect** > **Connection Point**.
2. Fai clic su **Add** e seleziona **API** come tipo di connessione.
3. Compila i dettagli richiesti:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Carica il file dell'account di servizio creato in precedenza.

### Passo 2.1: Aggiungere e configurare i documenti

* Non è necessario aggiungere tutti i documenti, solo quelli necessari.
* I documenti **Sync.ChartOfAccounts** e **Sync.CodeDefinition** sono richiesti per la contabilità automatica.

## Sync.SupplierPartyMaster

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Fai clic su **Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Configura l'ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Per **Product**, scegli l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Fai clic su **OK** per confermare la selezione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Imposta il **Request Body**:
   * Per **File**, seleziona **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Configura il Request Body**:
   * Per **File**, seleziona **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Configura l'ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Configura il Request Body**: Aggiungi i seguenti valori nella sezione **Request Body**:
   * Per **idm\_doc\_type**, imposta **Value** = `M3_SupplierInvoice`
   * Per **idm\_bod\_id\_field\_name**, imposta **Value** = `BOD_AlternateDocumentID_1`
   *   Per **attributes\_map**, imposta **Value** =

       ```
       {"Export": "Success"}
       ```
   * Per **acl\_from**, imposta **Value** = `Public`
   * Per **acl\_to**, imposta **Value** = `Private`
   * Per **set\_to\_error\_on\_rejected**, imposta **Value** = `True`
   * Per **delete\_from\_idm\_on\_rejected**, imposta **Value** = `True`
   * Per **File**, imposta **Input Document = No Compression**.
   * Per **ionapi\_json**: Aggiungi il contenuto del file ionapi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Configura il Request Body**:
   * Per **File**, imposta **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Configura il Request Body**:
   * Per **File**, imposta **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Configura il Request Body**:
   * Per **data\_type**, imposta **Value** = `AdvanceShipNotice`
   *   Per **field\_mappings**, imposta **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Per **File**, imposta **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Configura il Request Body**:
   * Per **data\_type**, imposta Value = `ChartOfAccounts`
   *   Per **field\_mappings**, imposta Value =

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
   * Per **File**, imposta **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Naviga sulla scheda **Documents** nell'API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** e compila i seguenti dettagli:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Configura l'ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Per **Product**, seleziona l'endpoint API creato nel **Passo 1: Creare un'API**.
   *   Trova e seleziona:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** per confermare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Configura il Request Body**:
   * Per **data\_type**, imposta Value = `M3Dimension`
   *   Per **field\_mappings**, imposta Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Per **File**, imposta **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Passo 3: Creare il Document Flow

1. Naviga su **OS** > **ION** > **Connect** > **Data Flows**.
2. Fai clic su **Add** e seleziona **Document Flow**.
3. Compila i campi richiesti:
   * **Name**: Utilizza un nome specifico per il tuo ambiente, come `M3-to-DocBits-Stage-Import-API`
   * per stage, `M3-to-DocBits-Sandbox-Import-API` per sandbox, o `M3-to-DocBits-Prod-Import-API` per production.
   * **Description**: Uguale al nome sopra.
4. Configura l'Application Node:
   * In **Application**, imposta il **Name** su `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Fai clic sul pulsante **+** e seleziona il Connection Point del cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Fai clic sull'icona **Document** accanto all'Application Node.

    * Seleziona tutti i documenti che desideri esportare/sincronizzare da LN a DocBits.
    * Assicurati che questi documenti corrispondano a quelli selezionati nel **Passo 2: Creare un API Connection Point**.
    * Se mancano documenti, devono essere aggiunti al Connection Point del cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Configura l'API Node:
   * Aggiungi un **API** Node e posizionalo a destra dell'Application Node.
   * Compila i campi richiesti:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Utilizza il Connection Point creato nel **Passo 2: Creare un API Connection Point**.
   * Fai clic sull'icona **Document** accanto allo Stream Node. Questo dovrebbe essere vuoto.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Finalizza la configurazione:
   * Salva la configurazione.
   * Fai clic su **Activate** per completare la configurazione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

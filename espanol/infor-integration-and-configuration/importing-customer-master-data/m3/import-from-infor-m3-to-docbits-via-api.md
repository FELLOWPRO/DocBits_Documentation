# Importación desde Infor M3 a DocBits a través de API

## Paso 1: Crear una API

1. Abra **Infor OS** y navegue a **API Gateway** > **Available APIs**.
2. Haga clic en **Add** y luego seleccione **Create New**.
3. Complete los detalles de la API:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` o `DocBits-Demo` (según su entorno).
   * **Suite Name**: Igual que el Application Name.
   * **API Context**: Igual que el Application Name.
   * **Description**: Igual que el Application Name.
   * **Icon**: Seleccione un icono de documento azul.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Agregue un **Target Endpoint**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Use la URL apropiada para su entorno:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod` o `Demo` (según el entorno).
* **Proxy Context**: Igual que el entorno (`Stage`, `Sandbox`, `Prod` o `Demo`).
* **Proxy Security**: Seleccione **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Recupere la clave API de **DocBits** navegando a **Settings** > **Global Settings** > **Integration**, luego copie la clave API y péguela como Key Value.
* Guarde la configuración del Target Endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Agregue documentación de API:

* Regrese a la sección de documentación de API haciendo clic en el **Documentation Icon** en el Endpoint creado.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Desplácese hacia abajo hasta la sección **Documentation** y haga clic en **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` o `DocBits-Demo` (según el entorno).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Use la URL apropiada del archivo Swagger para su entorno:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Asegúrese de que no haya un espacio al final de la URL.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* La documentación de la API se agregará automáticamente y se activará la actualización de metadatos.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Paso 2: Crear un API Connection Point

1. Navegue a **OS** > **ION** > **Connect** > **Connection Point**.
2. Haga clic en **Add** y seleccione **API** como tipo de conexión.
3. Complete los detalles requeridos:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Cargue el archivo de Service Account que se creó anteriormente.

### Paso 2.1: Agregar y configurar documentos

* No necesita agregar todos los documentos, solo los necesarios.
* Los documentos **Sync.ChartOfAccounts** y **Sync.CodeDefinition** son necesarios para la contabilidad automática.

## Sync.SupplierPartyMaster

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Haga clic en **Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Configure la ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Para **Product**, elija el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Haga clic en **OK** para confirmar la selección.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Configure el **Request Body**:
   * Para **File**, seleccione **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Configure el Request Body**:
   * Para **File**, seleccione **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Configure la ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Configure el Request Body**: Agregue los siguientes valores en la sección **Request Body**:
   * Para **idm\_doc\_type**, establezca **Value** = `M3_SupplierInvoice`
   * Para **idm\_bod\_id\_field\_name**, establezca **Value** = `BOD_AlternateDocumentID_1`
   *   Para **attributes\_map**, establezca **Value** =

       ```
       {"Export": "Success"}
       ```
   * Para **acl\_from**, establezca **Value** = `Public`
   * Para **acl\_to**, establezca **Value** = `Private`
   * Para **set\_to\_error\_on\_rejected**, establezca **Value** = `True`
   * Para **delete\_from\_idm\_on\_rejected**, establezca **Value** = `True`
   * Para **File**, establezca **Input Document = No Compression**.
   * Para **ionapi\_json**: Agregue el contenido del archivo ionapi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Configure el Request Body**:
   * Para **File**, establezca **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Configure el Request Body**:
   * Para **File**, establezca **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Configure el Request Body**:
   * Para **data\_type**, establezca **Value** = `AdvanceShipNotice`
   *   Para **field\_mappings**, establezca **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Para **File**, establezca **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Configure el Request Body**:
   * Para **data\_type**, establezca Value = `ChartOfAccounts`
   *   Para **field\_mappings**, establezca Value =

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
   * Para **File**, establezca **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Navegue a la pestaña **Documents** en el API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** y complete los siguientes detalles:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Configure la ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Para **Product**, seleccione el endpoint de API creado en el **Paso 1: Crear una API**.
   *   Localice y seleccione:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** para confirmar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Configure el Request Body**:
   * Para **data\_type**, establezca Value = `M3Dimension`
   *   Para **field\_mappings**, establezca Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Para **File**, establezca **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Paso 3: Crear el Document Flow

1. Navegue a **OS** > **ION** > **Connect** > **Data Flows**.
2. Haga clic en **Add** y seleccione **Document Flow**.
3. Complete los campos requeridos:
   * **Name**: Use un nombre específico para su entorno, como `M3-to-DocBits-Stage-Import-API`
   * para stage, `M3-to-DocBits-Sandbox-Import-API` para sandbox, o `M3-to-DocBits-Prod-Import-API` para production.
   * **Description**: Igual que el nombre anterior.
4. Configure la Application Node:
   * En **Application**, establezca el **Name** como `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Haga clic en el botón **+** y seleccione el Connection Point del cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Haga clic en el icono **Document** junto a la Application Node.

    * Seleccione todos los documentos que desea exportar/sincronizar desde LN a DocBits.
    * Asegúrese de que estos documentos coincidan con los seleccionados en el **Paso 2: Crear un API Connection Point**.
    * Si faltan documentos, deben agregarse al Connection Point del cliente.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Configure la API Node:
   * Agregue una **API** Node y colóquela a la derecha de la Application Node.
   * Complete los campos requeridos:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Use el Connection Point creado en el **Paso 2: Crear un API Connection Point**.
   * Haga clic en el icono **Document** junto a la Stream Node. Esto debe estar vacío.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Finalice la configuración:
   * Guarde la configuración.
   * Haga clic en **Activate** para completar la configuración.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

# Import von Infor M3 zu DocBits über API

## Schritt 1: Erstellen einer API

1. Öffnen Sie **Infor OS** und navigieren Sie zu **API Gateway** > **Available APIs**.
2. Klicken Sie auf **Add** und wählen Sie dann **Create New**.
3. Füllen Sie die Details für die API aus:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` oder `DocBits-Demo` (basierend auf Ihrer Umgebung).
   * **Suite Name**: Gleich wie der Application Name.
   * **API Context**: Gleich wie der Application Name.
   * **Description**: Gleich wie der Application Name.
   * **Icon**: Wählen Sie ein blaues Dokumentensymbol.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Fügen Sie einen **Target Endpoint** hinzu:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Verwenden Sie die entsprechende URL für Ihre Umgebung:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod` oder `Demo` (passend zur Umgebung).
* **Proxy Context**: Gleich wie die Umgebung (`Stage`, `Sandbox`, `Prod` oder `Demo`).
* **Proxy Security**: Wählen Sie **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Rufen Sie den API-Schlüssel von **DocBits** ab, indem Sie zu **Settings** > **Global Settings** > **Integration** navigieren, kopieren Sie dann den API-Schlüssel und fügen Sie ihn als Key Value ein.
* Speichern Sie die Target Endpoint-Konfiguration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Fügen Sie API-Dokumentation hinzu:

* Kehren Sie zum API-Dokumentationsbereich zurück, indem Sie auf das **Documentation Icon** im erstellten Endpoint klicken.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Scrollen Sie nach unten zum Abschnitt **Documentation** und klicken Sie auf **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` oder `DocBits-Demo` (passend zur Umgebung).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Verwenden Sie die entsprechende Swagger-Datei-URL für Ihre Umgebung:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Stellen Sie sicher, dass am Ende der URL kein Leerzeichen steht.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* Die API-Dokumentation wird automatisch hinzugefügt und die Metadaten-Aktualisierung wird ausgelöst.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Schritt 2: Erstellen eines API Connection Points

1. Navigieren Sie zu **OS** > **ION** > **Connect** > **Connection Point**.
2. Klicken Sie auf **Add** und wählen Sie **API** als Connection Type.
3. Füllen Sie die erforderlichen Details aus:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Laden Sie die Service Account-Datei hoch, die zuvor erstellt wurde.

### Schritt 2.1: Dokumente hinzufügen und konfigurieren

* Sie müssen nicht alle Dokumente hinzufügen—nur die notwendigen.
* Die Dokumente **Sync.ChartOfAccounts** und **Sync.CodeDefinition** sind für die automatische Buchung erforderlich.

## Sync.SupplierPartyMaster

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Klicken Sie auf **Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Konfigurieren Sie die ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Klicken Sie auf **OK**, um die Auswahl zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Legen Sie den **Request Body** fest:
   * Für **File** wählen Sie **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **File** wählen Sie **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Konfigurieren Sie den Request Body**: Fügen Sie die folgenden Werte im Abschnitt **Request Body** hinzu:
   * Für **idm\_doc\_type** setzen Sie **Value** = `M3_SupplierInvoice`
   * Für **idm\_bod\_id\_field\_name** setzen Sie **Value** = `BOD_AlternateDocumentID_1`
   *   Für **attributes\_map** setzen Sie **Value** =

       ```
       {"Export": "Success"}
       ```
   * Für **acl\_from** setzen Sie **Value** = `Public`
   * Für **acl\_to** setzen Sie **Value** = `Private`
   * Für **set\_to\_error\_on\_rejected** setzen Sie **Value** = `True`
   * Für **delete\_from\_idm\_on\_rejected** setzen Sie **Value** = `True`
   * Für **File** setzen Sie **Input Document = No Compression**.
   * Für **ionapi\_json**: Fügen Sie den Inhalt der ionapi-Datei hinzu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **File** setzen Sie **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **File** setzen Sie **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **data\_type** setzen Sie **Value** = `AdvanceShipNotice`
   *   Für **field\_mappings** setzen Sie **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Für **File** setzen Sie **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **data\_type** setzen Sie Value = `ChartOfAccounts`
   *   Für **field\_mappings** setzen Sie Value =

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
   * Für **File** setzen Sie **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Navigieren Sie zum Tab **Documents** im API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** und füllen Sie die folgenden Details aus:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Konfigurieren Sie die ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Für **Product** wählen Sie den API-Endpoint, der in **Schritt 1: Erstellen einer API** erstellt wurde.
   *   Suchen und wählen Sie:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK**, um die Konfiguration zu bestätigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Konfigurieren Sie den Request Body**:
   * Für **data\_type** setzen Sie Value = `M3Dimension`
   *   Für **field\_mappings** setzen Sie Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Für **File** setzen Sie **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Schritt 3: Erstellen des Document Flows

1. Navigieren Sie zu **OS** > **ION** > **Connect** > **Data Flows**.
2. Klicken Sie auf **Add** und wählen Sie **Document Flow**.
3. Füllen Sie die erforderlichen Felder aus:
   * **Name**: Verwenden Sie einen Namen, der spezifisch für Ihre Umgebung ist, wie z.B. `M3-to-DocBits-Stage-Import-API`
   * für stage, `M3-to-DocBits-Sandbox-Import-API` für sandbox oder `M3-to-DocBits-Prod-Import-API` für production.
   * **Description**: Gleich wie der Name oben.
4. Konfigurieren Sie die Application Node:
   * Unter **Application** setzen Sie den **Name** auf `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Klicken Sie auf die Schaltfläche **+** und wählen Sie den Connection Point des Kunden.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Klicken Sie auf das **Document**-Symbol neben der Application Node.

    * Wählen Sie alle Dokumente aus, die Sie von LN zu DocBits exportieren/synchronisieren möchten.
    * Stellen Sie sicher, dass diese Dokumente mit denen übereinstimmen, die in **Schritt 2: Erstellen eines API Connection Points** ausgewählt wurden.
    * Wenn Dokumente fehlen, müssen sie zum Connection Point des Kunden hinzugefügt werden.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Konfigurieren Sie die API Node:
   * Fügen Sie eine **API**-Node hinzu und positionieren Sie sie rechts neben der Application Node.
   * Füllen Sie die erforderlichen Felder aus:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Verwenden Sie den Connection Point, der in **Schritt 2: Erstellen eines API Connection Points** erstellt wurde.
   * Klicken Sie auf das **Document**-Symbol neben der Stream Node. Dies sollte leer sein.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Finalisieren Sie die Einrichtung:
   * Speichern Sie die Konfiguration.
   * Klicken Sie auf **Activate**, um die Einrichtung abzuschließen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

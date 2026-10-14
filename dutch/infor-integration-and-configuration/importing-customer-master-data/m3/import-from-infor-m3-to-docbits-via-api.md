# Import van Infor M3 naar DocBits via API

## Stap 1: Een API aanmaken

1. Open **Infor OS** en navigeer naar **API Gateway** > **Available APIs**.
2. Klik op **Add** en selecteer vervolgens **Create New**.
3. Vul de details voor de API in:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` of `DocBits-Demo` (afhankelijk van uw omgeving).
   * **Suite Name**: Hetzelfde als de applicatienaam.
   * **API Context**: Hetzelfde als de applicatienaam.
   * **Description**: Hetzelfde als de applicatienaam.
   * **Icon**: Selecteer een blauw documentpictogram.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Voeg een **Target Endpoint** toe:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Gebruik de juiste URL voor uw omgeving:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod` of `Demo` (overeenkomend met de omgeving).
* **Proxy Context**: Hetzelfde als de omgeving (`Stage`, `Sandbox`, `Prod` of `Demo`).
* **Proxy Security**: Selecteer **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Haal de API-sleutel op van **DocBits** door te navigeren naar **Settings** > **Global Settings** > **Integration**, kopieer vervolgens de API-sleutel en plak deze als de sleutelwaarde.
* Sla de configuratie van het Target Endpoint op.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Voeg API-documentatie toe:

* Keer terug naar de API-documentatiesectie door te klikken op **Documentation Icon** in het aangemaakte Endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Scroll naar beneden naar de sectie **Documentation** en klik op **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` of `DocBits-Demo` (overeenkomend met de omgeving).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Gebruik de juiste Swagger-bestands-URL voor uw omgeving:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Zorg ervoor dat er geen spatie aan het einde van de URL staat.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* De API-documentatie wordt automatisch toegevoegd en de metadata-verversing wordt geactiveerd.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Stap 2: Een API Connection Point aanmaken

1. Navigeer naar **OS** > **ION** > **Connect** > **Connection Point**.
2. Klik op **Add** en selecteer **API** als het verbindingstype.
3. Vul de vereiste details in:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Upload het serviceaccountbestand dat eerder is aangemaakt.

### Stap 2.1: Documenten toevoegen en configureren

* U hoeft niet alle documenten toe te voegen—alleen de noodzakelijke.
* De documenten **Sync.ChartOfAccounts** en **Sync.CodeDefinition** zijn vereist voor automatische boekhouding.

## Sync.SupplierPartyMaster

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Klik op **Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Configureer de ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Voor **Product**, kies het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Klik op **OK** om de selectie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Stel de **Request Body** in:
   * Voor **File**, selecteer **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Configureer de Request Body**:
   * Voor **File**, selecteer **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Configureer de ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Configureer de Request Body**: Voeg de volgende waarden toe in de sectie **Request Body**:
   * Voor **idm\_doc\_type**, stel **Value** in = `M3_SupplierInvoice`
   * Voor **idm\_bod\_id\_field\_name**, stel **Value** in = `BOD_AlternateDocumentID_1`
   *   Voor **attributes\_map**, stel **Value** in =

       ```
       {"Export": "Success"}
       ```
   * Voor **acl\_from**, stel **Value** in = `Public`
   * Voor **acl\_to**, stel **Value** in = `Private`
   * Voor **set\_to\_error\_on\_rejected**, stel **Value** in = `True`
   * Voor **delete\_from\_idm\_on\_rejected**, stel **Value** in = `True`
   * Voor **File**, stel in **Input Document = No Compression**.
   * Voor **ionapi\_json**: Voeg de inhoud van het ionapi-bestand toe.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Configureer de Request Body**:
   * Voor **File**, stel in **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Configureer de Request Body**:
   * Voor **File**, stel in **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Configureer de Request Body**:
   * Voor **data\_type**, stel **Value** in = `AdvanceShipNotice`
   *   Voor **field\_mappings**, stel **Value** in =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Voor **File**, stel in **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Configureer de Request Body**:
   * Voor **data\_type**, stel Value in = `ChartOfAccounts`
   *   Voor **field\_mappings**, stel Value in =

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
   * Voor **File**, stel in **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Navigeer naar het tabblad **Documents** in het API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** en vul de volgende details in:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Configureer de ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Voor **Product**, selecteer het API-endpoint dat is aangemaakt in **Stap 1: Een API aanmaken**.
   *   Zoek en selecteer:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** om de configuratie te bevestigen.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Configureer de Request Body**:
   * Voor **data\_type**, stel Value in = `M3Dimension`
   *   Voor **field\_mappings**, stel Value in =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Voor **File**, stel in **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Stap 3: De Document Flow aanmaken

1. Navigeer naar **OS** > **ION** > **Connect** > **Data Flows**.
2. Klik op **Add** en selecteer **Document Flow**.
3. Vul de vereiste velden in:
   * **Name**: Gebruik een naam die specifiek is voor uw omgeving, zoals `M3-to-DocBits-Stage-Import-API`
   * voor stage, `M3-to-DocBits-Sandbox-Import-API` voor sandbox, of `M3-to-DocBits-Prod-Import-API` voor production.
   * **Description**: Hetzelfde als de naam hierboven.
4. Configureer de Application Node:
   * Onder **Application**, stel de **Name** in op `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Klik op de knop **+** en selecteer het Connection Point van de klant.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Klik op het pictogram **Document** naast de Application Node.

    * Selecteer alle documenten die u wilt exporteren/synchroniseren van LN naar DocBits.
    * Zorg ervoor dat deze documenten overeenkomen met degene die zijn geselecteerd in **Stap 2: Een API Connection Point aanmaken**.
    * Als er documenten ontbreken, moeten deze worden toegevoegd aan het Connection Point van de klant.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Configureer de API Node:
   * Voeg een **API** Node toe en positioneer deze rechts van de Application Node.
   * Vul de vereiste velden in:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Gebruik het Connection Point dat is aangemaakt in **Stap 2: Een API Connection Point aanmaken**.
   * Klik op het pictogram **Document** naast de Stream Node. Dit moet leeg zijn.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Voltooi de installatie:
   * Sla de configuratie op.
   * Klik op **Activate** om de installatie te voltooien.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

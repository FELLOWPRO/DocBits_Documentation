# Import z Infor M3 do DocBits przez API

## Krok 1: Utwórz API

1. Otwórz **Infor OS** i przejdź do **API Gateway** > **Available APIs**.
2. Kliknij **Add**, następnie wybierz **Create New**.
3. Wypełnij szczegóły API:
   * **Application Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` lub `DocBits-Demo` (w zależności od środowiska).
   * **Suite Name**: To samo co nazwa aplikacji.
   * **API Context**: To samo co nazwa aplikacji.
   * **Description**: To samo co nazwa aplikacji.
   * **Icon**: Wybierz niebieską ikonę dokumentu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Dodaj **Target Endpoint**:

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL**: Użyj odpowiedniego adresu URL dla swojego środowiska:
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description**: `Stage`, `Sandbox`, `Prod` lub `Demo` (zgodnie ze środowiskiem).
* **Proxy Context**: To samo co środowisko (`Stage`, `Sandbox`, `Prod` lub `Demo`).
* **Proxy Security**: Wybierz **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security**:
  * **Authentication Type**: API Key
  * **Key Mode**: Header
  * **Key Name**: `X-API-KEY`
  * **Key Value**: Pobierz klucz API z **DocBits**, przechodząc do **Settings** > **Global Settings** > **Integration**, następnie skopiuj klucz API i wklej go jako wartość klucza.
* Zapisz konfigurację target endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Dodaj dokumentację API:

* Wróć do sekcji dokumentacji API, klikając **Documentation Icon** w utworzonym Endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Przewiń w dół do sekcji **Documentation** i kliknij **+ Add Documentation**.
  * **Name**: `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` lub `DocBits-Demo` (zgodnie ze środowiskiem).
  * **Type**: Swagger
  * **Enter URL or Upload Swagger JSON/YAML**: Użyj odpowiedniego adresu URL pliku Swagger dla swojego środowiska:
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Upewnij się, że na końcu adresu URL nie ma spacji.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* Dokumentacja API zostanie automatycznie dodana, a odświeżenie metadanych zostanie uruchomione.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Krok 2: Utwórz API Connection Point

1. Przejdź do **OS** > **ION** > **Connect** > **Connection Point**.
2. Kliknij **Add** i wybierz **API** jako typ połączenia.
3. Wypełnij wymagane szczegóły:
   * **Name**: `DocBits_Import`
   * **Description**: `DocBits_Import`
   * **Service Account**: Prześlij plik konta usługi, który został utworzony wcześniej.

### Krok 2.1: Dodaj i skonfiguruj dokumenty

* Nie musisz dodawać wszystkich dokumentów—tylko niezbędne.
* Dokumenty **Sync.ChartOfAccounts** i **Sync.CodeDefinition** są wymagane do automatycznego księgowania.

## Sync.SupplierPartyMaster

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Kliknij **Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Skonfiguruj ION API:
   * **API Call Name**: `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Kliknij **OK**, aby potwierdzić wybór.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Skonfiguruj **Request Body**:
   * Dla **File** wybierz **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Skonfiguruj Request Body**:
   * Dla **File** wybierz **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Acknowledge.SupplierInvoice`
3. **Skonfiguruj ION API**:
   * **API Call Name**: `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Skonfiguruj Request Body**: Dodaj następujące wartości w sekcji **Request Body**:
   * Dla **idm\_doc\_type** ustaw **Value** = `M3_SupplierInvoice`
   * Dla **idm\_bod\_id\_field\_name** ustaw **Value** = `BOD_AlternateDocumentID_1`
   *   Dla **attributes\_map** ustaw **Value** =

       ```
       {"Export": "Success"}
       ```
   * Dla **acl\_from** ustaw **Value** = `Public`
   * Dla **acl\_to** ustaw **Value** = `Private`
   * Dla **set\_to\_error\_on\_rejected** ustaw **Value** = `True`
   * Dla **delete\_from\_idm\_on\_rejected** ustaw **Value** = `True`
   * Dla **File** ustaw **Input Document = No Compression**.
   * Dla **ionapi\_json**: Dodaj zawartość pliku ionapi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.PurchaseOrder`
   * **Click on Select**
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Skonfiguruj Request Body**:
   * Dla **File** ustaw **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.ReceiveDelivery`
   * **Click on Select**
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Skonfiguruj Request Body**:
   * Dla **File** ustaw **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.AdvanceShipNotice`
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Skonfiguruj Request Body**:
   * Dla **data\_type** ustaw **Value** = `AdvanceShipNotice`
   *   Dla **field\_mappings** ustaw **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Dla **File** ustaw **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.ChartOfAccounts`
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Skonfiguruj Request Body**:
   * Dla **data\_type** ustaw Value = `ChartOfAccounts`
   *   Dla **field\_mappings** ustaw Value =

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
   * Dla **File** ustaw **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Przejdź do zakładki **Documents** w API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Kliknij Add New Document** i wypełnij następujące szczegóły:
   * **Scenario**: `Send to API`
   * **Documents**: `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Skonfiguruj ION API**:
   * **API Call Name**: `Sync.CodeDefinition-AccountingDimension`
   * Dla **Product** wybierz endpoint API utworzony w **Krok 1: Utwórz API**.
   *   Znajdź i wybierz:

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Kliknij OK**, aby potwierdzić konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Skonfiguruj Request Body**:
   * Dla **data\_type** ustaw Value = `M3Dimension`
   *   Dla **field\_mappings** ustaw Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Dla **File** ustaw **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Krok 3: Utwórz Document Flow

1. Przejdź do **OS** > **ION** > **Connect** > **Data Flows**.
2. Kliknij **Add** i wybierz **Document Flow**.
3. Wypełnij wymagane pola:
   * **Name**: Użyj nazwy specyficznej dla środowiska, takiej jak `M3-to-DocBits-Stage-Import-API`
   * dla stage, `M3-to-DocBits-Sandbox-Import-API` dla sandbox lub `M3-to-DocBits-Prod-Import-API` dla produkcji.
   * **Description**: To samo co nazwa powyżej.
4. Skonfiguruj Application Node:
   * W **Application** ustaw **Name** na `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Kliknij przycisk **+** i wybierz connection point klienta.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Kliknij ikonę **Document** obok application node.

    * Wybierz wszystkie dokumenty, które chcesz eksportować/synchronizować z LN do DocBits.
    * Upewnij się, że te dokumenty pasują do wybranych w **Krok 2: Utwórz API Connection Point**.
    * Jeśli brakuje jakichkolwiek dokumentów, należy je dodać do connection point klienta.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Skonfiguruj API Node:
   * Dodaj węzeł **API** i umieść go po prawej stronie application node.
   * Wypełnij wymagane pola:
     * **Name**: `DocBits-API`
     * **Description**: `DocBits-API`
     * **ION API Connector**: Użyj connection point utworzonego w **Krok 2: Utwórz API Connection Point**.
   * Kliknij ikonę **Document** obok stream node. Powinien być pusty.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Sfinalizuj konfigurację:
   * Zapisz konfigurację.
   * Kliknij **Activate**, aby zakończyć konfigurację.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

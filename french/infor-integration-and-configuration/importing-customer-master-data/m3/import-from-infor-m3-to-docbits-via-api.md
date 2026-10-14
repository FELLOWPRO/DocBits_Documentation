# Import depuis Infor M3 vers DocBits via API

## Étape 1 : Créer une API

1. Ouvrez **Infor OS** et naviguez vers **API Gateway** > **Available APIs**.
2. Cliquez sur **Add**, puis sélectionnez **Create New**.
3. Remplissez les détails de l'API :
   * **Application Name** : `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` ou `DocBits-Demo` (selon votre environnement).
   * **Suite Name** : Identique au nom de l'application.
   * **API Context** : Identique au nom de l'application.
   * **Description** : Identique au nom de l'application.
   * **Icon** : Sélectionnez une icône de document bleu.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_1.png)

4. Ajoutez un **Target Endpoint** :

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_2.png)

* **Target Endpoint URL** : Utilisez l'URL appropriée pour votre environnement :
  * `https://stage.api.docbits.com`
  * `https://sandbox.api.docbits.com`
  * `https://api.docbits.com`
  * `https://demo.api.docbits.com`
* **Target Endpoint Description** : `Stage`, `Sandbox`, `Prod` ou `Demo` (correspondant à l'environnement).
* **Proxy Context** : Identique à l'environnement (`Stage`, `Sandbox`, `Prod` ou `Demo`).
* **Proxy Security** : Sélectionnez **OAuth 2.0**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_3.png)

* **Target Endpoint Security** :
  * **Authentication Type** : API Key
  * **Key Mode** : Header
  * **Key Name** : `X-API-KEY`
  * **Key Value** : Récupérez la clé API depuis **DocBits** en naviguant vers **Settings** > **Global Settings** > **Integration**, puis copiez la clé API et collez-la comme valeur de clé.
* Enregistrez la configuration du Target Endpoint.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_4.png)

5. Ajoutez la documentation de l'API :

* Retournez à la section de documentation de l'API en cliquant sur **Documentation Icon** dans le Endpoint créé.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_5.png)

* Faites défiler vers le bas jusqu'à la section **Documentation** et cliquez sur **+ Add Documentation**.
  * **Name** : `DocBits-Stage`, `DocBits-Sandbox`, `DocBits-Prod` ou `DocBits-Demo` (correspondant à l'environnement).
  * **Type** : Swagger
  * **Enter URL or Upload Swagger JSON/YAML** : Utilisez l'URL appropriée du fichier Swagger pour votre environnement :
    * `https://stage.api.docbits.com/openapi.json`
    * `https://sandbox.api.docbits.com/openapi.json`
    * `https://api.docbits.com/openapi.json`
    * `https://demo.api.docbits.com/openapi.json`
  * Assurez-vous qu'il n'y a pas d'espace à la fin de l'URL.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_6.png)

* La documentation de l'API sera automatiquement ajoutée et l'actualisation des métadonnées sera déclenchée.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_7.png)

## Étape 2 : Créer un API Connection Point

1. Naviguez vers **OS** > **ION** > **Connect** > **Connection Point**.
2. Cliquez sur **Add** et sélectionnez **API** comme type de connexion.
3. Remplissez les détails requis :
   * **Name** : `DocBits_Import`
   * **Description** : `DocBits_Import`
   * **Service Account** : Téléchargez le fichier de compte de service créé précédemment.

### Étape 2.1 : Ajouter et configurer des documents

* Vous n'avez pas besoin d'ajouter tous les documents — seulement les nécessaires.
* Les documents **Sync.ChartOfAccounts** et **Sync.CodeDefinition** sont requis pour la comptabilité automatique.

## Sync.SupplierPartyMaster

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. Cliquez sur **Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.SupplierPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_8.png)

3. Configurez l'ION API :
   * **API Call Name** : `Sync.SupplierPartyMaster`
   * **Click on Select**
   * Pour **Product**, choisissez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * Cliquez sur **OK** pour confirmer la sélection.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_9.png)

4. Définissez le **Request Body** :
   * Pour **File**, sélectionnez **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_10.png)

## Sync.RemitToPartyMaster

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.RemitToPartyMaster`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_11.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.RemitToPartyMaster`
   * **Click on Select**
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/supplier_bod
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_12.png)

4. **Configurez le Request Body** :
   * Pour **File**, sélectionnez **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_13.png)

## Acknowledge.SupplierInvoice

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Acknowledge.SupplierInvoice`
3. **Configurez l'ION API** :
   * **API Call Name** : `Acknowledge.SupplierInvoice`
   * **Click on Select**
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/infor/idm/handle_ack_bod
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_15.png)

4. **Configurez le Request Body** : Ajoutez les valeurs suivantes dans la section **Request Body** :
   * Pour **idm\_doc\_type**, définissez **Value** = `M3_SupplierInvoice`
   * Pour **idm\_bod\_id\_field\_name**, définissez **Value** = `BOD_AlternateDocumentID_1`
   *   Pour **attributes\_map**, définissez **Value** =

       ```
       {"Export": "Success"}
       ```
   * Pour **acl\_from**, définissez **Value** = `Public`
   * Pour **acl\_to**, définissez **Value** = `Private`
   * Pour **set\_to\_error\_on\_rejected**, définissez **Value** = `True`
   * Pour **delete\_from\_idm\_on\_rejected**, définissez **Value** = `True`
   * Pour **File**, définissez **Input Document = No Compression**.
   * Pour **ionapi\_json** : Ajoutez le contenu du fichier ionapi.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_16.png)

## Sync.PurchaseOrder

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.PurchaseOrder`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_17.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.PurchaseOrder`
   * **Click on Select**
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/purchase_order_bod
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_18.png)

4. **Configurez le Request Body** :
   * Pour **File**, définissez **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_19.png)

## Sync.ReceiveDelivery

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.ReceiveDelivery`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_20.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.ReceiveDelivery`
   * **Click on Select**
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/import/receive_delivery_bod
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_21.png)

4. **Configurez le Request Body** :
   * Pour **File**, définissez **Input Document = No Compression**.

## Sync.AdvanceShipNotice

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.AdvanceShipNotice`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_23.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.AdvanceShipNotice`
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_24.png)

4. **Configurez le Request Body** :
   * Pour **data\_type**, définissez **Value** = `AdvanceShipNotice`
   *   Pour **field\_mappings**, définissez **Value** =

       ```
       { "ID": "//DataArea/LnTaxCode/DocumentID/ID" }
       ```
   * Pour **File**, définissez **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_25.png)

## Sync.ChartOfAccounts

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.ChartOfAccounts`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_26.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.ChartOfAccounts`
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_27.png)

4. **Configurez le Request Body** :
   * Pour **data\_type**, définissez Value = `ChartOfAccounts`
   *   Pour **field\_mappings**, définissez Value =

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
   * Pour **File**, définissez **Input Document = No Compression**.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_28.png)

## Sync.CodeDefinition-AccountingDimension

1. Naviguez vers l'onglet **Documents** dans le API Connection Point.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_32.png)

2. **Click Add New Document** et remplissez les détails suivants :
   * **Scenario** : `Send to API`
   * **Documents** : `Sync.CodeDefinition`

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_29.png)

3. **Configurez l'ION API** :
   * **API Call Name** : `Sync.CodeDefinition-AccountingDimension`
   * Pour **Product**, sélectionnez le endpoint API créé dans **Étape 1 : Créer une API**.
   *   Localisez et sélectionnez :

       ```
       CustomerApi/DocBits-Sandbox/Sandbox/master_data_lookup/xml/import_xml_file
       ```
   * **Click OK** pour confirmer la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_30.png)

4. **Configurez le Request Body** :
   * Pour **data\_type**, définissez Value = `M3Dimension`
   *   Pour **field\_mappings**, définissez Value =

       ```
       {
           "ID": "//DataArea/CodeDefinition/DocumentID/ID",
           "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
           "ListID": "//DataArea/CodeDefinition/ListID",
           "CodeValue": "//DataArea/CodeDefinition/CodeValue",
           "Description": "//DataArea/CodeDefinition/Description"
       }
       ```
   * Pour **File**, définissez **Input Document = No Compression**

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_31.png)

## Étape 3 : Créer le Document Flow

1. Naviguez vers **OS** > **ION** > **Connect** > **Data Flows**.
2. Cliquez sur **Add** et sélectionnez **Document Flow**.
3. Remplissez les champs requis :
   * **Name** : Utilisez un nom spécifique à votre environnement, tel que `M3-to-DocBits-Stage-Import-API`
   * pour stage, `M3-to-DocBits-Sandbox-Import-API` pour sandbox, ou `M3-to-DocBits-Prod-Import-API` pour production.
   * **Description** : Identique au nom ci-dessus.
4. Configurez l'Application Node :
   * Sous **Application**, définissez le **Name** sur `M3`.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_33.png)

* Cliquez sur le bouton **+** et sélectionnez le Connection Point du client.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_34.png)

* Cliquez sur l'icône **Document** à côté de l'Application Node.

    * Sélectionnez tous les documents que vous souhaitez exporter/synchroniser de LN vers DocBits.
    * Assurez-vous que ces documents correspondent à ceux sélectionnés dans **Étape 2 : Créer un API Connection Point**.
    * Si des documents manquent, ils doivent être ajoutés au Connection Point du client.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_35.png)

5. Configurez l'API Node :
   * Ajoutez une **API** Node et positionnez-la à droite de l'Application Node.
   * Remplissez les champs requis :
     * **Name** : `DocBits-API`
     * **Description** : `DocBits-API`
     * **ION API Connector** : Utilisez le Connection Point créé dans **Étape 2 : Créer un API Connection Point**.
   * Cliquez sur l'icône **Document** à côté de la Stream Node. Cela devrait être vide.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_36.png)

6. Finalisez la configuration :
   * Enregistrez la configuration.
   * Cliquez sur **Activate** pour compléter la configuration.

![](https://raw.githubusercontent.com/Fellow-Consulting-AG/docbits/refs/heads/main/readme/.gitbook/assets/import_from_infor_m3_to_docbits_via_api_37.png)

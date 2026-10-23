# Création d'un fichier de mappage IDM

## Champs du fichier de mappage IDM

Lors de la création d'un fichier de mappage IDM, les champs suivants sont requis :

* **Définition du type de document**
  * Assurez-vous que le code du type de document dans DocBits correspond au nom utilisé dans l'URL des paramètres de champ, comme pour le fichier de mappage BOD.
  * Vérifiez que le nom du type de document dans IDM correspond à la configuration de votre système. Par exemple, dans M3, il peut s'agir de **M3_SupplierInvoice**, tandis que dans LN il sera différent selon votre configuration.
    * Un guide sur la navigation dans IDM se trouve sous Document Manager dans IDM sur cette page.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **Valeurs statiques**

    * Commencez par définir toutes les valeurs statiques sur une seule ligne avec la clé **Static_Values** :

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * Attribuez ensuite une valeur à chaque variable statique avec le préfixe **SV_** :

    ```properties
    SV_FileNameSeparator=_ 
    SV_ACLString=Public
    ```

```properties
#Define mappings for the static values
#Example: Static_Values=<StaticVariableName>
Static_Values=FileNameSeparator,ACLString
#Example: SF_<StaticVariableName> = StaticValue
SV_FileNameSeparator=_
SV_ACLString=Public
```

* **Champs statiques**
  * Les champs statiques servent à définir des valeurs précises et invariables pour tous les documents. Ces valeurs restent identiques d'un document à l'autre.
  *   Commencez par lister tous les champs **statiques** utilisés, en précisant l'**IDMAttributeId** et le type.

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   Attribuez ensuite des valeurs statiques à chaque champ avec le préfixe `SF_` :

      ```properties
      SF_BOD_AccountingEntityID=921_VVB
      SF_M3_Company=921
      SF_M3_Division=VVB
      ```

```properties
#Define mappings for the static fields
#Example: Static_Fields=<IDMAttributeId>:<type>
Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
#Example: SF_<IDMAttributeId> = StaticValue
#SF_MDS_EntityType=InforERPEnterpriseFinancialsReceivedInvoice
SF_BOD_AccountingEntityID=921_VVB
SF_M3_Company=921
SF_M3_Division=VVB
```

* **Champs d'index**
  *   Commencez par lister tous les champs d'index utilisés, en précisant l'**IDMAttributeId** et le type.

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   Chaque champ mappé suit le format :

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * Vérifiez que **IndexFieldFromDocBits = IDMAttributeID**, afin que le mappage des champs dans DocBits corresponde aux attributs dans IDM (Document Type → Attributes).\        Un guide sur la navigation dans IDM se trouve sous Document Manager dans IDM sur cette page.

```properties
#Define index fields
#Example: Index_Fields=<IndexFieldIdFromIDM>:<type>
Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
#Example: IF_<DocBitsFieldID> = <IDMAttributeId>
IF_INVOICE_ID=BOD_SupplierInvoiceID
IF_CORRELATION_ID=BOD_AlternateDocumentID_1
IF_INVOICE_DATE=M3_InvoiceDate
IF_COMPANY=M3_Company
IF_DIVISION=M3_Division
IF_DIVISION_NO=BOD_AccountingEntityID
IF_SUPPLIER_ID=BOD_RemitToPartyID
IF_SUPPLIER_NAME=BOD_SupplierPartyID
```

* **Définition du champ ACL**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nom recherchable dans IDM**
  * Le **Searchable PDF Name** sera le nom du document dans IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="Exemple de fichier de mappage IDM"><figcaption></figcaption></figure>

## Exportation de fichiers XML et EDI

Pour exporter le fichier XML/EDI d'origine avec le PDF généré, vous devez modifier le fichier de mappage IDM dans la configuration d'exportation. Mettez d'abord à jour la section **Static_Values** en ajoutant le préfixe et l'extension du fichier. Définissez ensuite le mappage proprement dit afin de garantir une configuration d'exportation correcte.

Si une exportation des factures vers IDM est déjà configurée, le PDF généré devrait déjà être inclus dans l'exportation. Si vous n'avez pas besoin du fichier XML, vous pouvez ignorer la suite. En revanche, si vous avez besoin du fichier XML, suivez les étapes ci-dessous.

### Mise à jour des valeurs statiques :

Repérez le champ **Static_Values** et ajoutez ce qui suit :

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Ajoutez ensuite les entrées suivantes sous **SV_ACLString** :

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="Exemple de configuration des valeurs statiques"><figcaption></figcaption></figure>

### Mappage XML

Ajoutez le mappage suivant en bas du fichier :

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

Remarque : assurez-vous que **export_doc_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="Exemple de mappage XML"><figcaption></figcaption></figure>

### Mappage EDI

Ajoutez le mappage suivant en bas du fichier :

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Remarque : assurez-vous que **export_doc_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="Exemple de mappage EDI"><figcaption></figcaption></figure>

### Document Manager dans Infor

Accédez à Document Manager et sélectionnez le nom du type de document actuel que vous essayez d'exporter, par exemple Supplier Invoice.

![Liste de documents d'Infor Document Manager avec le type de document Rental_Invoice et ses détails de création et de modification](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

Cliquez sur l'icône ci-dessus, puis sur Administration → Document Type et recherchez dans la liste le type de document dont vous avez besoin.

![Page Document Type d'Infor Control Center listant des types de documents tels que Bank Statement CAMT053 et Customer invoice](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

Comme illustré ci-dessous, vous voyez alors le nom du type de document tel qu'il est dans INFOR

![Page MONGOOSE Reports d'Infor Document Manager avec l'onglet Attributes et une liste de types de documents incluant Purchase Order](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

Assurez-vous que le nom apparaît de cette façon dans le fichier de mappage IDM

## Télécharger le fichier dans DocBits

Une fois le fichier préparé, téléchargez-le dans votre configuration d'exportation dans DocBits. Elle est disponible sous Paramètres → Exporter.

![Page Export Settings de DocBits avec une entrée de facture utilisant la méthode d'exportation webhook INVOKE et IDM Mapping File sélectionné](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)

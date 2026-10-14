# Création d'un fichier de mappage IDM

## Champs Requis pour le Fichier de Mapping IDM

Lors de la création d'un fichier de mapping IDM, les champs suivants sont requis :

* **Définition du Type de Document**
  * Assurez-vous que le code de type de document dans DocBits correspond au nom utilisé dans l'URL des paramètres de champ, similaire au Fichier de Mapping BOD.
  * Vérifiez que le nom du type de document dans IDM est en accord avec la configuration de votre système. Par exemple, dans M3, cela peut être **M3\_SupplierInvoice**, tandis que dans LN, cela sera différent selon votre configuration.
    * Un guide sur la façon de naviguer dans IDM peut être trouvé dans le Gestionnaire de Documents dans IDM sur cette page.

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

* **Valeurs Statique**
  *   Tout d'abord, définissez toutes les valeurs statiques sur une seule ligne en utilisant la clé **Static\_Values** :

      ```properties
      Static_Values=FileNameSeparator,ACLString
      ```
  *   Ensuite, assignez des valeurs à chaque variable statique en utilisant le préfixe **SV\_** :

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

* **Définition du Champ ACL**

```properties
Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **Nom Recherchable dans IDM**
  * Le **Nom PDF Recherchable** sera le nom du document dans IDM.

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID
```

## Mapping des Champs

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

*   Commencez par lister tous les champs d'index utilisés, en spécifiant l'ID et le type de champ.

    ```properties
    Index_Fields=INVOICE_ID:STRING,INVOICE_DATE:STRING,COMPANY:STRING,DIVISION:STRING,DIVISION_NO:STRING,CORRELATION_ID:STRING,SUPPLIER_ID:STRING,SUPPLIER_NAME:STRING
    ```
*   Chaque champ mappé suit le format :

    ```properties
    IF_<DocBitsFieldID> = <IDMAttributeId>
    ```

    * Confirmez que **IndexFieldFromDocBits = IDMAttributeID**, en vous assurant que le mapping des champs dans DocBits est en accord avec les attributs dans IDM (Type de Document → Attributs). Un guide sur la façon de naviguer dans IDM peut être trouvé dans le Gestionnaire de Documents dans IDM sur cette page.

![](https://files.gitbook.com/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FT2n2w4uDCJvv7CJ5zrdk%2Fuploads%2FzT9MMKlFCSBJtRW1pf4s%2Fimage.png?alt=media\&token=ea2f6ae2-f9f2-48d3-98e3-ed06dcda69f1)

### Exportation de fichiers XML et EDI

Pour exporter le fichier XML/EDI original avec le PDF généré, vous devez modifier le fichier de mappage IDM, dans la configuration d'exportation. Tout d'abord, mettez à jour la section **Static\_Values** en ajoutant le préfixe et l'extension du fichier. Après cela, définissez le mappage réel pour garantir la bonne configuration d'exportation.

Si une exportation pour les factures vers IDM est déjà configurée, le PDF généré devrait déjà être inclus dans l'exportation. Si vous n'avez pas besoin du fichier XML, vous pouvez passer à la partie suivante. Cependant, si vous avez besoin du fichier XML, suivez les étapes ci-dessous.

#### Mise à jour des valeurs statiques :

Trouvez le champ **Static\_Values** et ajoutez ce qui suit :

```
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

Ensuite, ajoutez les entrées suivantes sous **SV\_ACLString** :

```
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

Après cela, ajoutez le mappage réel, en vous assurant que le type de document d'exportation correspond au type de fournisseur IDM.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252F6k18wa4zSaSZkvfEKMwW%252Fimage.png%3Falt%3Dmedia%26token%3De6c49d36-44b9-4d18-9d22-63d30205dbd5\&width=768\&dpr=4\&quality=100\&sign=3ac8bc32\&sv=2)

#### Mappage XML

Ajoutez le mappage suivant en bas du fichier :

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
```

Remarque : Assurez-vous que **export\_doc\_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FlXToG368VI7Fc7HDguCn%252Fimage.png%3Falt%3Dmedia%26token%3Dcb153977-34e1-4f5f-a416-60e3141b4aca\&width=768\&dpr=4\&quality=100\&sign=b7d9585c\&sv=2)

#### Mappage EDI

Ajoutez le mappage suivant en bas du fichier :

```
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

Remarque : Assurez-vous que **export\_doc\_type** est défini sur le type de facture IDM. Dans cet exemple, il est défini pour **M3**.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2F578966019-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FT2n2w4uDCJvv7CJ5zrdk%252Fuploads%252FSrF54zkGq6aYYuJq1KAI%252Fimage.png%3Falt%3Dmedia%26token%3D403c9bfa-7e97-4d3c-a4b0-1bb82b98fe50\&width=768\&dpr=4\&quality=100\&sign=a768865f\&sv=2)

#### Gestionnaire de documents dans Infor

Allez dans le Gestionnaire de documents et sélectionnez le nom du type de document actuel que vous essayez d'exporter, par exemple, Facture fournisseur.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FEV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk\&width=768\&dpr=4\&quality=100\&sign=a2f25ec9\&sv=2)

Cliquez sur l'icône ci-dessus, puis cliquez sur Administration → Type de document et trouvez le type de document dont vous avez besoin dans la liste.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8\&width=768\&dpr=4\&quality=100\&sign=a1149783\&sv=2)

Comme montré ci-dessous, vous verrez ensuite le nom du type de document tel qu'il est dans INFOR.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FKSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw\&width=768\&dpr=4\&quality=100\&sign=62bfe0a6\&sv=2)

Assurez-vous que c'est ainsi que le nom est affiché dans le fichier de mappage IDM.

### Télécharger le fichier sur DocBits

Une fois le fichier préparé, téléchargez-le dans votre configuration d'exportation dans DocBits. Cela est disponible dans Paramètres → Exporter.

![](https://docs.docbits.com/~gitbook/image?url=https%3A%2F%2Flh7-us.googleusercontent.com%2FrUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM\&width=768\&dpr=4\&quality=100\&sign=a13b8c88\&sv=2)

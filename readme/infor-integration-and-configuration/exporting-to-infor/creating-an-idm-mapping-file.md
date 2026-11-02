# 创建 IDM 映射文件

## IDM 映射文件的字段

创建 IDM 映射文件时，需要以下字段：

* **文档类型定义**
  * 确保 DocBits 中的文档类型代码与字段设置 URL 中使用的名称一致，方式与 BOD 映射文件类似。
  * 确认 IDM 中的文档类型名称与系统配置一致。例如，在 M3 中，该名称可能是 **M3_SupplierInvoice**；在 LN 中，名称会根据您的设置而有所不同。
    * 本页的 IDM 中的文档管理器部分提供了 IDM 导航指南。

```properties
#Define Name of document
#Example: <DocBitsDocumentType>=<IDMDocumentType>
#INVOICE=LN_SupplierInvoice
INVOICE=M3_SupplierInvoice
```

*   **静态值**

    * 首先，使用 **Static_Values** 键在一行中定义所有静态值：

    ```properties
    Static_Values=FileNameSeparator,ACLString
    ```

    * 然后，使用 **SV_** 前缀为每个静态变量分配值：

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

* **静态字段**
  * 静态字段用于为所有文档设置特定且不变的值。这些值在各文档中保持一致。
  *   首先，列出所有使用的 **Static** 字段，并指定 **IDMAttributeId** 和类型。

      ```properties
      Static_Fields=BOD_AccountingEntityID:STRING,M3_Company:STRING,M3_Division:STRING
      ```
  *   然后，使用 `SF_` 前缀为每个字段分配静态值：

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

* **索引字段**
  *   首先，列出所有使用的索引字段，并指定 **IDMAttributeId** 和类型。

      ```properties
      Index_Fields=delivery_note_id:STRING,delivery_date:STRING,CORRELATION_ID:STRING,ACCOUNTING_ENTITY:STRING,GROUP_ACCOUNTING_ENTITY:STRING,supplier_name:STRING,supplier_id:STRING,purchase_order:STRING
      ```
  *   每个映射字段遵循以下格式：

      ```properties
      IF_<DocBitsFieldID> = <IDMAttributeId>
      ```

      * 确认 **IndexFieldFromDocBits = IDMAttributeID**，确保 DocBits 中的字段映射与 IDM 中的属性（文档类型 → 属性）一致。\ 本页的 IDM 中的文档管理器部分提供了 IDM 导航指南。

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

* **ACL 字段定义**

```properties
#Define ACL Field value
#Example: ACL_Fields= Concatenation of other defined fields that together should be a valid ACL in IDM
ACL_Fields=SV_ACLString
```

* **IDM 中的可搜索名称**
  * **可搜索 PDF 名称**将是 IDM 中的文档名称。

```properties
#Define Resource Mapping
#Example: Searchable_PDF_Name= Concatenation of other defined fields
Searchable_PDF_Name=IF_INVOICE_ID 
```



<figure><img src="../../.gitbook/assets/idm_mapping_file_example.png" alt="IDM 映射文件示例"><figcaption></figcaption></figure>

## XML 和 EDI 文件导出

若要将原始 XML/EDI 文件与生成的 PDF 一同导出，需要在导出配置中修改 IDM 映射文件。首先，在 **Static_Values** 部分添加文件前缀和扩展名。然后定义实际映射，以确保导出配置正确。

如果已设置将发票导出到 IDM，则生成的 PDF 应已包含在导出内容中。如果不需要 XML 文件，可以跳过下一部分。如果需要 XML 文件，请按照以下步骤操作。

### 更新静态值：

找到 **Static_Values** 字段并添加以下内容：a

```properties
,EDI_FILE_PREFIX,XML_FILE_PREFIX,PDF_FILE_PREFIX,PDF_FILE_EXTENSION,EDI_FILE_EXTENSION,XML_FILE_EXTENSION
```

然后，在 **SV_ACLString** 下方添加以下条目：

```properties
SV_EDI_FILE_PREFIX=EDI_810_
SV_XML_FILE_PREFIX=XML_810_
SV_PDF_FILE_PREFIX=INV_EDI_
SV_PDF_FILE_EXTENSION=.pdf
SV_EDI_FILE_EXTENSION=.xml
SV_XML_FILE_EXTENSION=.xml
```

<figure><img src="../../.gitbook/assets/static_values_configuration_example.png" alt="静态值配置示例"><figcaption></figcaption></figure>

### XML 映射

在文件底部添加以下映射：

<pre class="language-properties"><code class="lang-properties"><strong>EMBEDDED_FILES_EXPORT = TRANSFORMED, XML
</strong>EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION

EFE_XML_SOURCE_NAME = XML_DOCUMENT.xml
EFE_XML_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_XML_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_ID+SV_XML_FILE_EXTENSION
</code></pre>

注意：确保 **export_doc_type** 设置为 IDM 发票类型。在此示例中，它设置为 **M3**。

<figure><img src="../../.gitbook/assets/xml_mapping_example.png" alt="XML 映射示例"><figcaption></figcaption></figure>

### EDI 映射

在文件底部添加以下映射：

```properties
EMBEDDED_FILES_EXPORT = TRANSFORMED, EDI
EFE_TRANSFORMED_SOURCE_NAME = Transformed.xml
EFE_TRANSFORMED_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_TRANSFORMED_EXPORT_FILENAME = SV_XML_FILE_PREFIX+IF_INVOICE_NUMBER+SV_XML_FILE_EXTENSION

EFE_EDI_SOURCE_NAME = EDI.edi
EFE_EDI_EXPORT_DOC_TYPE = M3_SupplierInvoice
EFE_EDI_EXPORT_FILENAME = SV_EDI_FILE_PREFIX+IF_INVOICE_NUMBER+SV_EDI_FILE_EXTENSION
```

注意：确保 **export_doc_type** 设置为 IDM 发票类型。在此示例中，它设置为 **M3**。

<figure><img src="../../.gitbook/assets/edi_mapping_example.png" alt="EDI 映射示例"><figcaption></figcaption></figure>

### Infor 中的文档管理器

打开文档管理器，并选择您要导出的当前文档类型名称，例如“供应商发票”。

![Infor Document Manager的文档列表，包含Rental_Invoice文档类型及其创建和修改详情](https://lh7-us.googleusercontent.com/EV3uw3R1L6_RRANB7FRLwtUFMbv_KGtL4x6kAk6lEYhwI90UeG2uWqFD2Azpxv-SRFl9zfvdratOZbXxp2D1-SryLo3Boj2x9Xc4PQXJ6vUhX5c9pvhv4XHuCk-qMK51DZ885vRUJ5dwES7k84uhoyk)

点击上方图标，然后依次点击 Administration → Document Type，再从列表中找到所需的文档类型。

![Infor Control Center的Document Type页面，列出Bank Statement CAMT053和Customer invoice等文档类型](https://lh7-us.googleusercontent.com/ldsuINS9SCUQm3E57s8j_95gzBGwHQFavcf6d3myg6tuVxRoQHtq8R-6we5OEJ63swDxwPc9w7hbySWqWdfaMsGdQpn99m6EchPY5f5DzXEj-8mjocwPNtdJVNP34CuPvw0JIImDgFX1Q05M8-ogZo8)

如下所示，您将看到 INFOR 中的文档类型名称。

![Infor Document Manager的MONGOOSE Reports页面，包含Attributes标签页和含Purchase Order在内的文档类型列表](https://lh7-us.googleusercontent.com/KSreWGS7TqdMP64BqtufM24xk0RDnNDHUZapnPsSuRj_umPJ3icll89KI2RYpbtet2F6ccL8QfYbl27-2j1nQPwQ0z-Nq873c4Tv72ee9AJhKMxynIUxmJKKsQQCupW_dpRfw_5BXm0WvAnw4HOALmw)

请确保 IDM 映射文件中的名称与此处显示的名称一致。

## 将文件上传到 DocBits

文件准备就绪后，将其上传到 DocBits 的导出配置中。此配置位于 Settings → Export。

![DocBits的Export Settings页面，其中一条发票条目使用INVOKE webhook导出方法并选中了IDM Mapping File](https://lh7-us.googleusercontent.com/rUHhvImiWamK6JxnWSPL4JEioAJq3AmvdsubJDo-DoDV9F_i5mZ42YDnjqZUYKYSJu1Cetc_4fLwlvvmoZXYIzmBf3hoyW6RjfP9HQ8FkNDhW1IbLHvNTCHWFRaeCECdZ97u79-Eu37TvzqnqGPEayM)

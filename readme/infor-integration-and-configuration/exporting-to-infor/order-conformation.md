# Confirmación de Pedido

Pequeña actualización para Confirmación de Pedido



{% hint style="info" %}
Enlace al [Archivo](../../../../../BOD-Mapping%20\(OrderConfirmation\).properties)
{% endhint %}
```
# BOD Mapping Order Confirmation Docbits
# Version: 1.0.1
# last edited by: Daniel Jordan
# edited: 7.06.2024
# Update Subline

#Abbriviations:
#SV=Static Value
#a variable, that is set once and will not be changed
#SF=Static Field:
#assigns a particular variable to all instances of this class
#SFP=Static Field Path
#SFV=Static Field Value
#GFP=General Field Path
#GFV=General Field Value
#DT=Document Type
#PO=Purchase Order
#POP=Purchase Order Path
#POF=Purchase Order Field
#IFP=Index Field Path
#IFV=Index Field Value
#PFP=Page Field Path
#TN=Table Name
#TNP=Table Name Path
#TNV=Table Name Value
#TC=Table Column
#TCP=Table Column Path
#TCV=Table Column Value

#All static field attributes.
Static_Fields=AlternateDocSchema,AlternateDocLocation,LogicalID,ConfirmationCode,actionCode,AccountingEntityID,LastModificationPerson,LocationID

SFP_AlternateDocSchema=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID\\schemeName
SFV_AlternateDocSchema=CorrelationID

SFP_AlternateDocLocation=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID\\location
SFV_AlternateDocLocation=doc2

SFP_LogicalID=SyncCaptureDocumentType\\ApplicationArea\\Sender\\LogicalID

#Example: SFV_LogicalID=*Logical ID from Infor Application Connection Point*
#Example: SFV_LogicalID=lid://infor.ims.doc2
SFV_LogicalID=lid://infor.ims.docbits_export

SFP_ConfirmationCode=SyncCaptureDocumentType\\ApplicationArea\\Sender\\ConfirmationCode
SFV_ConfirmationCode=OnError

SFP_actionCode=SyncCaptureDocumentType\\DataArea\\Sync\\ActionCriteria\\ActionExpression\\actionCode
SFV_actionCode=Change

SFP_AccountingEntityID=SyncCaptureDocumentType\\DataArea\\Sync\\AccountingEntityID
SFV_AccountingEntityID=001_RFP

SFP_LocationID=SyncCaptureDocumentType\\DataArea\\Sync\\LocationID
SFV_LocationID=D_TST100

SFP_LastModificationPerson=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\LastModificationPerson
SFV_LastModificationPerson=100138


#PO Fields
PO_Fields=LocationID

POP_LocationID=SyncCaptureDocumentType\\DataArea\\Sync\\LocationID
POF_LocationID=location_id


#All generated fields.
Generated_Fields=CreationDateTime,BODID

GFP_BODID=SyncCaptureDocumentType\\ApplicationArea\\BODID
GFV_BODID=BODID

GFP_CreationDateTime=SyncCaptureDocumentType\\ApplicationArea\\CreationDateTime
GFV_CreationDateTime=CurrentDate

#Document Type path.
DT_Path=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentType

#Mapping between DOC2 document and IDM document.
Document_Types=ORDER_CONFIRMATION
ORDER_CONFIRMATION=OrderConfirmation

#Index Field Mapping
Index_Fields=supplier_id,supplier_name,document_date,CORRELATION_ID,purchase_order,TAX_AMOUNT,NET_AMOUNT,TOTAL_AMOUNT,PROMISED_DELIVERY_DATE,SUPPLIER_ORDER_NUMBER,Firma:STRING
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/SupplierParty/PartyIDs/ID
IF_supplier_id=SupplierID
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/SupplierParty/Name
IF_supplier_name=SupplierName
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/DocumentDateTime
IF_document_date=DocumentDate
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/AlternateDocumentID/ID
IF_CORRELATION_ID=AlternateDocumentID
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/PurchaseOrderReference/DocumentID/ID
IF_purchase_order=PurchaseOrder
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/Tax/Amount
IF_TAX_AMOUNT=VATAmount
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/Tax/BasisAmount
IF_NET_AMOUNT=NetAmount
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/TotalAmount
IF_TOTAL_AMOUNT=TotalAmount
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/BillFromParty/PartyIDs/ID
IF_SUPPLIER_ORDER_NUMBER=SupplierOrderNumber
#corresponding IDM Attribute:SupplierInvoice/SupplierInvoiceHeader/DocumentID/ID @accountingEntity
IF_Firma=ACCOUNTING_ENTITY

#If index field value is to be used somewhere else define path here.

IFP_CORRELATION_ID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\AlternateDocumentID\\ID
IFP_purchase_order=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentID\\ID
IFP_Firma=SyncCaptureDocumentType\\DataArea\\Sync\\AccountingEntityID


#Index field common path
IF_COMMON_PATH=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField

IF_Attributes=languageID

IFP_languageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Name\\languageID
IFV_languageID=en-us


#IF_Elements=name,value,fieldOrderNumber,datatype,category,pageID,fieldEnumeration
IF_Elements=name,value,fieldOrderNumber,page,fieldEnumeration
IFP_name=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Name
IFP_value=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\Value
IFP_fieldOrderNumber=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\FieldOrderNumber
IFP_page=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\PageID
IFP_fieldEnumeration=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentField\\FieldValueEnumerationString


Pages_COMMON_PATH=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage

Page_Elements=pageID,sourceFileName,fileMimeType
PFP_pageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\PageID
PFP_sourceFileName=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\SourceFileName
PFP_fileMimeType=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentPage\\SourceMimeType

Batch_Level_Properties=fileSize,lastModificationPerson,lastModifiedDateTime

#Path_CreatePerson=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\CreationPerson\\Name
Path_fileSize=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\FileSize
Path_lastModificationPerson=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\LastModificationPerson\\Name
Path_lastModifiedDateTime=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\LastModificationDateTime

#Table mapping
Table_COMMON_PATH=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable

#Uncomment below tag for defining tables mapping.
Tables=InvoiceTable
TN_InvoiceTable=InvoiceTable
#corresponding IDM Attribute:
TN_InvoiceTable_TC_QUANTITY=ConfirmedQuantity
#corresponding IDM Attribute:
TN_InvoiceTable_TC_ITEM_NUMBER=ItemNumber
#corresponding IDM Attribute:
TN_InvoiceTable_TC_DESCRIPTION=Description
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_PURCHASE_ORDER=OrdenDeCompra
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_UNIT=UnidadMedida
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_POSITION=Posición
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_SUB_LINE_NUMBER=NúmeroSublínea
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_UNIT_PRICE=PrecioUnitarioConfirmado
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_TOTAL_AMOUNT=Monto
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_NET_AMOUNT=MontoNeto
# Atributo IDM correspondiente:
TN_InvoiceTable_TC_LIEFERDATUM=FechaHoraEntregaPrometida


TableColumn_StaticFields=languageID
TCP_languageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Row\\Column\\Name\\languageID
TCV_languageID=en-us

TableColumn_MappedFields=name,value
#,pageID
TCP_name=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Row\\Column\\Name
TCP_value=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Row\\Column\\Value
TCP_pageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Row\\Column\\PageID


TN_InvoiceTable_Static_Fields=nameLanguageID,name
TNP_InvoiceTable_nameLanguageID=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Name\\languageID
TNV_InvoiceTable_nameLanguageID=en-us
TNP_InvoiceTable_name=SyncCaptureDocumentType\\DataArea\\CaptureDocument\\DocumentTable\\Name
TNV_InvoiceTable_name=FilasFactura
{% hint style="info" %}
Consulte aquí una [muestra](../../../../../M3_CaptureDocumentToProcessPurchaseOrder2.xml) del flujo de trabajo de Infor OS - Actualizado el 11 de junio de 2024
{% endhint %}

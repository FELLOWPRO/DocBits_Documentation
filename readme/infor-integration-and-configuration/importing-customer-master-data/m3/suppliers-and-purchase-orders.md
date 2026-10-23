# 供应商和采购订单

## **连接点**

要稍后创建数据流，您需要创建 DocBits API 连接点。

在 InforOS 中，导航至 ION Desk → Connect → Connection Points

![Infor ION Desk导航菜单，其中包含Home、Data Flows、API Flows和Mappings条目](https://lh7-us.googleusercontent.com/ySRjNzMXFzwSOYKx9hnlKLPHPuXpmfTvRADBfV6cpT8ajiEUbS4oXpd9InhXG09mHLakhqBTJMH4yQJNG5z9RXmbAjh8YbuGhxnXSeooIH\_r3RAGOvJE6Ok67ST\_272zFfhB\_TTFYg3b-NwFq0CAv2o)

在此处创建一个新的连接点。

![ION Desk中的Connection Points页面，显示工具栏图标和空的连接点列表](https://lh7-us.googleusercontent.com/ZDv-F3iayFqnsvVLlAE1kr0NNncsvuYtzcE\_WQj-0ONoE7McRl-f6\_DDH9ErQ0KLspZFFJ43t5EfnPBJjVg25YISMEQ--X4MmK6SVWzB60-Fq6mtwdhiOBwSnL-8vASXsto9iab0dnve6eeG8yuqNoI)

**选择 API**

为连接点命名，并填写能说明其性质和环境的描述。在 Connection 选项卡下，导入为当前环境创建的服务账户。

![ION Desk中DocBits-DEV-Demo-Import的连接点设置，在Connection选项卡下显示Name、Description和服务账户](https://lh7-us.googleusercontent.com/UCuGTwKARn3auhYdDDUbQ78Ok3qBNE1KpGEMealfPvgRju4VRLn2AfKaL5tLDcAh00poLHNQU-Q6koBhG5RdxK4CJrrL6Qeb4D52qnhw3aG1LZniuzHRXwOyzGcJvRnQtLGbp6PIseXvWxHlk-AMlz0)

接下来，切换到 Documents 选项卡。您需要将以下 BOD 添加到连接点。并非所有 BOD 都是供应商和采购订单主数据所必需的，但在实施自动会计等其他功能时会很有用。

![ION Desk连接点的Documents标签页，列出Connection Documents，包括Acknowledge.SupplierInvoice、Sync.PurchaseOrder、Sync.RemitToPartyMaster和Sync.SupplierPartyMaster](https://lh7-us.googleusercontent.com/25Hizkx23i1c8-QHSrE7mPAH7zW6ux9iHTcP8\_l6EJJy548CvuNPF1R86Fuqx5iYZP9HF-Z4G6hntkaUtlOMetHIzAVZyBM6VIQ-vsvy6P5YBuAj4yscdJe8ySOHwIRQwFpShRiFGC83v467LLBaXq8)

目前我们只关注必要的 BOD：Sync.RemitToPartyMasterData、Sync.SupplierPartyMaster 和 Sync.PurchaseOrder。

* Sync.RemitToPartyMasterData 和 Sync.SupplierPartyMaster

这两个 BOD 的配置应类似于以下示例（API Call Name 各不相同）

![Sync.SupplierPartyMaster的Send to API配置，产品为DocBits-DEV，操作为post CustomerApi/DocBits-DEV/prod/import/supplier_bod](https://lh7-us.googleusercontent.com/1SeyL73b7K9vxkTzKk-pumRleoY1sx9MVwgEBMZ-oUf6GXG2C7fKIRMbnhWHHhIQhUDBS3oKQidrQIN08FZ\_7eKEt1Yp0cRqnsDlv1R5ShdZdNKmaXmU\_19DAVtiT3U0m2qm4cBOj9FcnT0eyawfJXk)

* Sync.PurchaseOrder

此 BOD 的配置应类似于以下示例

![Sync.PurchaseOrder的Send to API配置，Product为DocBits-DEV，操作为post CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/ljXpQxwepI3u6kcITZfACV9yYL1ZZZtBbWimkXW6aWFTI-yd7Gajrxw2pwxdcF1Xv3KoGDalq72yXvaipjQ-OmbcTzJ0PUUKnmE0pBa5pASEPg0amqKSbU82ZDOKr5alWXynAd53IM2i9HgZ1CsYIB4)

配置好这些 BOD 后，点击返回按钮右侧的图标即可保存连接点。

## **数据流**

数据流应类似于以下示例

![ION数据流图，将M3、一个Filter和多个DocBits API应用程序连接到End元素](https://lh7-us.googleusercontent.com/BtszuCXPwv-WYCGtnd\_beU9t0uNntEu6U2iCSstxu1GAziuCfFafQdy2LKZkYw4kbQVfzI5lBYYajOeNwXkn84xy7AXWlCFX4GLo6dukWtfkFPMsXaPga0EkbnrI0bHSKqezXsvYJKymemZYDySIfA8)

（DocBits API 数量较多，是因为每个连接都代表不同的环境。因此，您拥有的环境数量不同，数据流也可能略有不同。）

本说明以有四个独立环境为例。

### **M3**

数据流从您的 M3 应用程序开始

### **筛选器**

筛选器的配置如下所示

![ION Desk中的Filter Properties对话框，包含Properties、Attributes和Conditions选项卡以及Name和Description字段](https://lh7-us.googleusercontent.com/-rMMaL3ToAoxqMFXybclIcd61H4S25HI90xnHANGl3J7ldZ374\_T2V0q\_\_QSwuNSuXfu829G7kYRCfVslx-l9b1j5LAVKonCQqO3aK2FuWNwmtyvytAF6PaIv8jiEJhhxSwU47eKEo1ozbzyndSW7BY)

![Filter Attributes标签页，列出ChartOfAccounts、PurchaseOrder、RemitToPartyMaster和SupplierPartyMaster按AccountingEntityID筛选的Document Path Filtered Data Type行](https://lh7-us.googleusercontent.com/npa9V37wV661zRD-pccafrGqw4hRb-Tk7iZ84UyyjE0gtfAcI1ma6\_QWS3iEcBW35trveCG3CnXiZAnFIQyYM278XYJqIuzQh3SUmbAxLCmyTCHkiOhpDJwSfFDJtc8PlcbrmrBdZLACsK3B8sCSyDA)

![Filter Conditions标签页，包含Document ChartOfAccounts、Not Filtered条件以及AccountingEntityID_3 equals 780_AAA表达式](https://lh7-us.googleusercontent.com/saiZJD9diyo2JC-XV0vYCboPZJP-87zDH7LIGuBNMNzhL5alDZkShpCARfYd21oroC8eYBfYdckJiONty9IuOc7zHkIIlUWNqoxnPfygEc1R1Tnjt1KPZpSTr7-RLaa5lqS3\_2DPj96aV0vLdZk2tzw)

（会计实体 ID 当然需要是您组织的唯一 ID）

### **DocBits API**

在此处添加一个应用程序，并选择之前创建的 DocBits API。

### **文件**

配置如下所示

![从M3经一个过滤器到达DocBits-DEV-P、DocBits-DEV-S和DocBits-DEV-D应用程序的ION数据流，承载ChartOfAccounts、PurchaseOrder、RemitToPartyMaster和SupplierPartyMaster文档](https://lh7-us.googleusercontent.com/GLI8kFjQHePMo4ZBWIR1WPNAhkvmtG0BfYADpdlmNqEFMYJclMInVYmKPdaElPLyPR5qtkWOKTnqDFXMDV2pML3igNOFyFj3R9fj2XHRAs6-Rl3KWz4a8-ednk15wyLDJUziAR6ZT4GjuZO2ANw1ymY)

## **M3 BOD 触发**

导航至 Infor M3 应用程序。

进入主菜单后，按 Command + R 打开命令提示搜索框。然后输入 evs006 并搜索。

![Infor M3中的Search and Start面板，在主菜单上方打开](https://lh7-us.googleusercontent.com/Vn2WD1-8RuDURsYmzrTARO4mBafwhBUvDImM3z2Nd\_hDnVRWjbHgOoplV8QhBC9QtslnWqZyJNIhudvGFGaEl5S-qgloKn0rpwQsF0EuVnrzVplg1urqvSQ9fNa5Qetx8TwLuxZzL3N7wHz9kX4xr\_o)

进入此页面后，您需要将 SupplierPartyMaster、RemitToPartyMaster 和 PurchaseOrder 添加到列表中。

BOD noun: SupplierPartyMaster

Table: CIDMAS

BOD noun: RemitToPartyMaster

Table: CIDMAS

BOD noun: PurchaseOrder

Table: MPHEAD

每种情况下，您都需要点击加号图标将其添加到列表中。

![Infor M3中基于事件的BOD触发列表EVS006，其中带有Actions工具栏和Apply按钮](https://lh7-us.googleusercontent.com/3y5xAtk4nSc5Eqk-vOJLL59jQHc1w-Fmtn0PIjSiBWTeOo974zg4UjjrK890MjfnsU1a4UtiSqtwcNlHmr6el6GRBd8GrSN\_ZlPk3W\_IQIVcppHOYwnAzHEgRF22JmeRRkJSHotXvd3k\_94\_pYjt6Uw)

添加每个 BOD 后，右键点击该 BOD 的 BOD noun，然后选择 Related → Run

![Infor M3中的右键上下文菜单，列出Drill down、Select、Change、History、Copy、Delete和Display选项](https://lh7-us.googleusercontent.com/HjkKvk7khjPgpjXmfyTyOLE2vNeB2qt2oN9ShOmrQiYhhvokRlBaZ0rlPtbwWUld54EhUJZLK0OVNGH\_eIYzFj22XgFHZccEM9g2nVQ\_5BgouHYoMfzfWYQVwluSdcednqrjilSByCdt44ytHgfCNyo)

您将进入以下菜单。在此处将 BOD verb 更改为 Sync，然后点击 NEXT 以触发 BOD。

![Infor M3中针对表CIDMAS的BOD触发面板，BOD名词为SupplierPartyMaster，作业状态为Pending](https://lh7-us.googleusercontent.com/FoJTP89zGI0FwRTyLjkIKfW75MbCrvcvqD\_ka--G1SFdzIhBAp7dq63\_WKMIEC-ouCHWA7sRd25rWfWclZJmWd7SGIZLwnSQ4id3nq82hOuFV9-mzMHAtGlhfCKtYwcQnrLyMSsrTmKNyME7lpYSeNA)

触发 BOD 后，您会收到确认通知。

如果操作成功，供应商和采购订单表现在应该会显示在 Settings → Master Data Lookup 下。

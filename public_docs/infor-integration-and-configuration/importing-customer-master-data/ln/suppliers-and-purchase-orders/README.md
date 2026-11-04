# 供应商和采购订单

## **连接点**

要稍后创建数据流，您需要先创建 DocBits API 连接点。

首先，在 InforOS 中，导航到 ION Desk → Connect → Connection Points

![ION Desk 导航，连接分组已展开，包含数据流、API 流、映射、连接点和文件模板条目](https://lh7-us.googleusercontent.com/852EogukgFvteFTdg6_a6MPLaBUUqDw1J4x4H2q9BMjaVzZIGlpASC_fImhvAxe-nPBvIvOPFTI0oG8D3RlkAHiFDbLsVrsjaJMD1B5otXyIzPDkvoJvrj-JvMEHao73jgcZ5aKLAP4fCpkP7XV08JE)

进入此页面后，创建一个新的连接点。

![ION Desk 的连接点页面，导航中连接分组已打开，面包屑为主页和连接点](https://lh7-us.googleusercontent.com/eh1NyUDTS0k-59ePv89PjZpfh5IT0iyFPoV5M9xmo3fmai-Iz0ptQFXgI9onZM-sTICHii32MkAw22AhZZAT5iKs_Hjw3_NDT49XG_KRONAvyK4OuL-bX667F9UGr-juckRmcE2hATOkSQ5x8QlugxU)

**选择 API**

为连接点设置名称和描述，以说明其用途和所属环境。在 Connection 选项卡下，导入您为当前操作环境创建的服务帐户。

![API 连接点对话框 DocBits-DEV-Demo-Import，包含用法、连接和文档选项卡，名称为 DocBits-DEV-Demo-Import，身份验证条目为 DocBits-DEV-Demo-Import Service Account，逻辑 ID 为 infor.api.docbits-dev-demo-import](https://lh7-us.googleusercontent.com/WZKJSckXWzztmEHmySnz6oDSbgFDvPmxku48HCiDJn7O1vTUcpUBYnwDHMT_Ja8aSGd8sFm-YQQYzyn5DnYLw77PQeFwTxcOV6C9aPWHyj2VofevH4S6ciyduIUy5YaNvmuNV6WgVJKOZ89_6oJjuq0)

接下来，切换到 Documents 选项卡。您需要将以下 BOD 添加到连接点。

![连接点的文档选项卡，包含 Ack-SupplierInvoice、Sync.PurchaseOrder 和 Sync.ReceiveDelivery 行，每行都有方向 In 和同名的 BOD](https://lh7-us.googleusercontent.com/3Q4XIpxXLixaDqXhh7CRKPl0yUwBce34CqLfw0BGS1UFXsvFIaxD6XelEgbnwfYFUCa5En-C1oAZR74C4lQ15as_M7JIQ20Nf9ZVmrVK8zCGuLS2YtphX4bgQ5uOwS2-MJLLZvsflDC31XLrTZzTKCg)

* Ack-SupplierInvoice

此 BOD 用于在 Infor 中发生错误时通知 DocBits。下面这两个 BOD 的配置应类似于下图所示（API Call Name 会有所不同）

![BOD 配置，包含输入文档、ION API、请求参数、请求体和设置选项卡，API 调用名称为 Ack-SupplierInvoice](https://lh7-us.googleusercontent.com/vmcVsltij144O3NeysAS2YduFNds98X_VJOpn6v356vAZI3v10SO8-ZMBd7zWyBUJKR9-UMQgGcT2U34HdGgpQ8rhtbFxsmuhgwJ_K6qXbtu04AP67G8jrNwkdj32LCgAhy_m4tnFQJApQehnfX8w5Y)

* Sync.PurchaseOrder

此 BOD 的配置应类似于下图所示

![BOD 配置，包含输入文档、ION API、请求参数、请求体和设置选项卡，以及 API 调用名称 Sync.PurchaseOrder、产品 DocBits-DEV 和操作 POST CustomerApi/DocBits-DEV/prod/import/purchase_order_bod](https://lh7-us.googleusercontent.com/LPmOwFuzOnYNjwcKDfpI2S-IYJPKhjHYy4xKSUtB7EXSmPGfnG1lDfR-q6fdk4Uh9QBr-PIWjkpW3clbq31z8BP4_CGgoryKguS4GhR44gCG8xt6FJxRvqV-1i5Ul_3-wFjmiroYcchb5Ou5wBA0DF0)

* Sync.ReceiveDelivery

此 BOD 的配置应类似于下图所示

![BOD 配置，包含输入文档、ION API、请求参数、请求体和设置选项卡，API 调用名称为 Sync.ReceiveDelivery](https://lh7-us.googleusercontent.com/75TPWASsqnzrWdeoyHZ4T23Zm5DbctQLOZKVe4N05ni32ecs0kZmBAihWnr7j0J7TisLvF2lncmUbEGGF9dKz8glVcRe7pmCvmEx8TMTesh0zGeewNpveNIsQqw-gkHvcITTF4a067MhoMgY8Jp6Prc)

配置好这些 BOD 后，按下位于返回按钮右侧的图标，即可保存连接点。

## **数据流**

数据流应类似于下图所示

![ION Desk 中的数据流，左侧为 DocBits 连接点节点，右侧为结束节点](https://lh7-us.googleusercontent.com/yhSunSyXrzx2Q0VIulIa6b989LxG36g5-kyYXGwniU0okKb3cJWDe65GYhpOfkHWTYJR4xdT85Us2Ba7tHhoJsE51I-g-82ZQ2bRM5zkgF5VmaRSno8M5bfhMCbUAw4-xx5oEudkqZWYoeIUUYhJPDU)

（DocBits API 有多个，是因为每个连接对应一个不同的环境。因此，数据流可能会因环境数量不同而略有差异。）

以下示例假设有四个独立环境。

### **LN**

数据流从您的 LN 应用程序开始

### **DocBits API**

在此处添加一个应用程序，并选择您之前创建的 DocBits API。

### **文件**

配置应如下所示

![数据流细节，包含 DocBits 节点 DocBits-DEV-P、开始和结束标记以及中间第二个 DocBits 节点，还有包含 Sync.PurchaseOrder、Sync.ReceiveDelivery、Sync.RemitToPartyMaster 和 Sync.SupplierPartyMaster 的文档面板](https://lh7-us.googleusercontent.com/OEG6wQFd9LT6J_Ttcsdj7GgM2bTxrS-dpO2EbcVx4vGH1NLtZyaRTbYnr4-SDIWL2hk1zeVGr3bjuebNmwAMEx0S0U7xmNGztp-8HVjRLYyc-3lbQBL8lDU_TahhNxBugX_Bnu3QjZsKHX0Pafae-zU)

## **LN BOD 触发**

完成上述所有步骤后，您需要导航到 Infor LN 并触发 BOD，以便将供应商和采购订单所需的各种主数据发送到 DocBits。

![Infor LN 起始页面，左侧为收藏夹面板，以及采购订单、发票和仓库订单图块](https://lh7-us.googleusercontent.com/b6IsSx-x5Ri0cfYU9TTpgipqsoCkDPTxXdKoMBPaumyaopp-NRAJhoNnBfksnVVdz9Y26M0KlfdcKP4S1n_PjcTYKIu3MbVMQIfuIaTYYAL2ctyYsp29mEOrVh2TxmLPkUofeqJQ8nvBQbTOwj0-V0Y)

### **PurchaseOrder**

在上述菜单中，从左侧菜单栏选择 Common → BOD-Messaging → Publish BODs → Publish Order Management Transactional Data

选择 PurchaseOrder 选项卡并勾选复选框。

![发布订单管理事务数据对话框，包含处理、关闭、全选和全部清除按钮，选中的采购订单选项卡以及左侧展开 BOD 消息和发布 BOD 的树](https://lh7-us.googleusercontent.com/UJlicSuDjbEVtr_pzOeqkP8kkiBJIdAgzPK46FlhubqIIHiaJRYp27B__08e9IcNHdcctrBeBfZ6vFPQI3Xf3duL6R2Hu-iaL9dY7hANmy8ukiL61CTxcel0jd_66GAySp3dC1ptYKBaqLqaP1TwJco)

### **供应商**

在 LN 主页中，从左侧菜单栏导航到 Common → BOD-Messaging → Publish BODs → Publish Logistics Master Data

选择 PartyMaster 选项卡，然后勾选 Supplier → Buy-from 或 SupplierPartyMaster 复选框。

![发布物流主数据对话框，包含处理、关闭、全选和全部清除按钮，选中的业务伙伴主数据选项卡以及包含供应商、买方的业务伙伴主数据、付款方业务伙伴主数据、付款来源业务伙伴主数据和收款方业务伙伴主数据列的网格](https://lh7-us.googleusercontent.com/KY_cFaUegEZmqAlcsBLVOTaxKOkkBkMeaQUbv996H946oOa-jvxB3lDqrkWV-17elt0mZDGews6Lr_6ojbFXtReDnV1PmqzwLXfE-IX5fKJr2IeJkAdnf1R9Sk5WYoxOLGolgo2MPQ3SNeoPnQ-ysy0)

### **BOD 触发**

勾选所有需要发布的 BOD 后，选择 Options 选项卡。

应选择以下选项。

![发布物流主数据对话框，包含模式选择器、含公司 0051 的选择范围部分和 BOD 消息设置部分](https://lh7-us.googleusercontent.com/7KpYALL1XL0pqWLRCPFng8-WT8IWI4o9lEtrp2zAN5bOBnYdz-6EHfAPc_StaY9raJTWbfrksra9UUxyQAQdtg4nOZggpHox3AV3C_cL9xhDAdHV4n79yyCfbyGH2NmS30fQGfsLTe_4_tXKy54nI8U)

完成后，按下 PROCESS 按钮即可触发 BOD。屏幕上会显示一条消息，通知您 BOD 已触发。

![发布物流主数据对话框，BOD 消息设置部分包含显示动词、逻辑 ID、使用 ProcessSync 动词和日志记录复选框，以及处理、关闭、全选和全部清除按钮](https://lh7-us.googleusercontent.com/BPX5vIBHIFv641srJPwW-19Dx1N1T2QnadGwVMQu-6pBZUxnUdOjdY1olMqorIyN_oeTBqz_1knMoYsSxEA-_NtGVx_j9dBixvOfic8rKJDT91tYqwSSLNpk8YkMW8ndelpH9_fzrTZUCMs_vnoxbvM)

如果操作成功，供应商和采购订单表现在应可在 Settings → Master Data Lookup 下查看。

\\

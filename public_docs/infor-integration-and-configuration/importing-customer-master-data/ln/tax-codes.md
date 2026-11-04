# 税码

## **创建 DocBits 连接点**

打开 ION Desk → Connect → Connection Points

![ION Desk 主页，已展开 Connect 菜单，显示 Connection Points、Data Flows、API Flows、Mappings 和 File Templates](https://lh7-us.googleusercontent.com/QLQB17W\_hywZWBqme8Wio-orbdOdFHXLv5zTd89B3EkeS0WCuuo5Pv1CndLRQ2rFUefvQYM95U2Unhrl3YU3WAR23Ij\_tDw\_TOEVenWjyCh-9H8CPFSezF2gmED7u5QTR7q9WV4CSXRvDqkmKJYPqAI)

此数据流需要 4 个连接点：3 个 API 连接点，分别对应不同的税码类别（全额、减额和免税），以及一个代表 LN 公司应用程序的 Application 连接点。

&#x20;要创建新的连接点，请选择“+ADD”按钮”

![ION Desk 的 Connection Points 页面，显示现有连接点列表和 +ADD 按钮](https://lh7-us.googleusercontent.com/cECLuIswRSK3WWhUMi1n3tm2AIcrksZdpz7ZCO6-H\_MzaKe9CDT0w1b7GKJ8GtT\_d6nvvDe4ukLJfWcMocbHZ5dSSCw25Ky7-JUdrYb893GYYyaHL9tTjG1ZniORJPLSu1zJxL3c-1VQRw4IC0LpYuA)

在选项列表底部选择“API”。

![连接点类型列表，Infor Technology 下有 Infor LN 和 IMS via API Gateway，列表底部为 API](https://lh7-us.googleusercontent.com/bpeLxdmi8b10LLMGy02vMRXuLoic9kFLywnpd6SSYV0fNv82dQahyvaA85mC1PEVScNW4m63fOw89vkhQr0-ou8VWOSjkwGWG5GnP7GQl77THtjXWP3YNo8LUzAstpCs0Q5fOjxaoT\_\_ZKM4jciHA5I)

随后将进入以下页面。

![ION Desk 中空白的 API 连接点表单，显示最后修改日期和 Connection Documents 区域](https://lh7-us.googleusercontent.com/4pcN0B7aibjn\_Qn8nMgkzRc\_NiXev-c1wJudDKo2V5r0ORuajVzfzAWnWu0Wt68hKMKSLYkieUhOYChkcZuCZDWkg-F22Rq2WvVqgPweSg3by2TGrrJHweKWTlf\_DK1X2pCkoNU4yoGo3DyHsoqcGjg)

在此处输入 TaxCode 连接点的所有详细信息。为要创建的三个连接点分别执行以下操作：

* 输入名称：TaxCodeFull、TaxCodeReduced、TaxCodeFree
* Description：可填写与名称相同或相近的内容
* 导入已创建的服务帐户。

切换到“Documents”选项卡，然后选择加号图标以添加所需的 BOD，如下所示。

![API 连接点的方案栏，显示 Get from API、Send to API 和 Trigger 图标](https://lh7-us.googleusercontent.com/byhA18LzkcY9ZyfnzyDlru5qBx88E8U1yggMNNkoHGsYVCbNkflNFXGVvJwMvE\_104VCjoYOM0SQIJVniyBBdn5UKasVR0uat6UvmCmpzz9ZYsY2Wv14B4ElOwqcg2qklxYAQVU84UOG70l3fMLRrwo)

搜索 BOD。

![连接点的 Document 选项卡，包含 Input Document、ION API Request Parameters、Request Body 和 Settings 子选项卡](https://lh7-us.googleusercontent.com/DAKzvEsjCmk1jy7L6GwrVY2DWg3\_InluNftWnR7hGlnyeBxSDW6XTDPBMLqtJuUc9Lq3Nga6-EKS4tZpOjE09h5FUJaTm\_E70UdA4l17jWGQ6BSr121lC3LzhffUXi6Bsk5EZEz4XHyjekk1Njb3H4I)

搜索名为“Sync.LnTaxCode”的 BOD，点击该项，然后按“OK”添加 BOD。

![Select Document Type 对话框，筛选文本为 sync.lntax，结果列表中有 Sync.LnTaxCode](https://lh7-us.googleusercontent.com/7BLwrq8kr9OTHleI2anmAr2-4ChksQ0pptddwm1quFHquGfnMBEW32RFx31ETGbrxf0KGVr-VzlZC9h9heD3ymTq9L5NZEV1b9E67IIR0is18UGBCoJ5j7KIMmF533EDMvZzgi4LXqAkV9zgCyl0\_Lk)

转到 ION API 部分。在 API Call Name 下，可使用 BOD 的名称 Sync.LnTaxCode。

按“SELECT”按钮。

![ION API Request Parameters 选项卡，API Call Name 为 Sync.LnTaxCode，Product 为 LN](https://lh7-us.googleusercontent.com/7MukO6oUAzVBFMPhFepwMvugqnhDDMhX9j7wZRU7BU0OusW3CKpMgqQNC7uNlehPp6eFniVxrX3DxjgsGZ\_Tmt\_cQOWGGiBfXAQfCC85amOGp1VY8RGo3nPABCiwzaIkYmnQF6t3FPVZ1fPV6fLazNc)

选择为当前环境配置的 API，然后搜索以下 API。选中后，按“OK”。

![Search ION API Operation 对话框，Product 为 DocBits-Demo，筛选为 import_xml，并显示匹配的 import_xml 操作](https://lh7-us.googleusercontent.com/IpUUqJaXF0MmIeR6gtE9GDCccLfNsQLZ-RSHhQGVwJEj8WJwI-twgiHpFomBKhbnTUUKrhxJ0EUZ7F\_21MCSBjNS2VQq3azprekoxctRJZ-NJUHhb4J9rHUSRDoR\_OCzDHTG5q5KTwWMHOR5qNoNd38)

接下来，切换到 Request Body 选项卡。

这里需要针对每个连接点稍作调整：为每种税码分配的字段映射略有不同。

![Request Body 选项卡，格式为 multipart/form-data，并显示 data_type、field_mappings 和 file 的数据类型行](https://lh7-us.googleusercontent.com/f4c-1M9mgCci2jjxkhaCDFX9bRWzMDaRwVv4XiaUH7BpHchPklvMnWoP\_ILSm6VB7GoFJNJzHsEPzk3eCFyLm1Kc3QI8OufjQ1mr7PqowjzViFDWc2opiNE1ODICtI9yEyUOi\_d\_hzN8CGo8gu6Ec84)

在 field_mappings 行的 value 下，填写所创建税码连接点（全额、减额或免税）对应的具体字段映射。可在 https://docbits.com/doc/field-mappings/ 查看这些映射。

最终效果应与上图相同或相似。完成后，点击此处的 SAVE 选项。

![API 连接点 DocBits-Stage-Import-LnTaxCodeFull，方案为 Send to API，API Call Name 为 Sync.LnTaxCode，待发送文档为 Sync.LnTaxCode](https://lh7-us.googleusercontent.com/LSYrbElw6BgQbbIdSstbakfwLENZ\_09WQcQhjO7kbb2U3jSK\_\_wFnr43tIj2hTHYegQ9lrSZBuJ9N7MNewr2W3yjPCrrVLeP9UAZjvrKKBzeY9h-q6FrVd5gPtlH0iP0GpMcvhGxjAnHN7BlY8CmT3c)

## **数据流配置**

导航至 ION Desk → Connect → Data Flows

![ION Desk 菜单，已展开 API Flows 组并选中 Connection Points](https://lh7-us.googleusercontent.com/cpWAepQyLP8V0b-Oj7djzl21eZLU2JdnJPEMPs53Uq-adZbaCegl35RjguLx8rsP2E87ZmwbNgISFIpAy6kOeahaBCSygDVSJzmv1GQGn1w1MgR8N08mnnfhb02XjsLnt\_rVJKr4Y0UtiTf14NqTHLQ)

点击“+ADD”，然后选择 document flow。

![ION Desk 的 Data Flows 页面，显示文档流 Ln-Docbits 和 Data Lake Flow 条目及最后修改用户](https://lh7-us.googleusercontent.com/HYqc\_P2DQjBoc-mpsyZ\_nlPFNiU17ZCLHfiOa282-Sa5JSA3Hv1XlwFjmlPhVGnAaEAqqalJ5ka43AJOzEO3uljwVAogAHkTVer7Q9JgI0WaOVX2Uo5Z8KGEqoa3BH\_zZwup7Bh4lKe4O5kr6hmAZm4)

通过拖放顶部菜单中的组件，创建以下数据流。

![ION Desk 中空白的数据流画布，显示 Application、Database、Network 和 Message Queue 组件面板](https://lh7-us.googleusercontent.com/V\_aJHPhFJssPUQ4mAHU20SVPSfhqhjU8BOQ2Ws1MtaauKp6OVAENLXod2uQe6Zbuc5JKZx6Bp3WyJtkQtkbnDluZZS5GLMGcaC9EuCrV8cn2aJk2y-Cih3PP2dg-umW0iDhak5UXNUuPxwkgqVg-mvk)

### **应用（LN）**

![数据流中的 Application 节点及其通往 End 的 Get from 和 Send to 分支](https://lh7-us.googleusercontent.com/2CCNlz0S-Z8p\_l9kPPUMqPkreoO3aLy8MkqY6UFMIABJRNFXGTFMXbaw78E42g8fEO4ZxFL\_oJMf2QnWn2xZLtS4zjN8AzCS\_B2i2x-tjWmmjyVLa1jSLQAnSB8-EhNfNISzf2uuX9kcqN-QixUUXvw)

在此处选择 LN 公司，最终效果应与以下内容相似。

![Application Activity Properties 对话框，Name 为 LN_companyno，Application 为 in01_1100](https://lh7-us.googleusercontent.com/b5pb4YfbZMCSi2X-xT4mj-Yw\_Uu77zNyJGl3rntVdqf907PwgX6Z9uQJIoHA2FS5M\_mVbdQgkh0HWgsOgtkoySmtrT7W8CrqsqlCnPEt6hv\_yODGulfp1qdxXvrB1HL-en3W9bY285fC3kARLZfSfck)

### **文档**

![数据流中应用节点 LN_companyno 通过 Yes 和 No 分支连接到 API 节点直至 End](https://lh7-us.googleusercontent.com/U8cqu3jABU3RQLGEGsS5qCnDkc-boTpAdZEVIUA9AlmD9Oz33JvnzD43SBTmLY55i8Bsr4lbi6udeIimCcRG1NgWbynv6OllCLaJPC50kJ0gPq7rsR5Rvj50yKngMiNvnYoLLT\_Hzn5cyhp18jq\_IyI)

在此处添加之前的 Sync.LnTaxCode BOD，结果如下所示。

![应用节点的 Documents 选项卡，列表中显示文档 Sync.LnTaxCode](https://lh7-us.googleusercontent.com/bgC1y3NtmX09XBjng\_pKmP5VQ5w0E\_VuFOfMF1rYs3iGGL5OaMHkKoyQJNtcVtbS6bEvF4KdtFNaX0VxT9MF0P-zTDnOnt5mhA0Gxcs4eMcRLtbXl5a\_8y84XyLyvh61-LdoQ7f15j-wE1nl\_TSYSDg)

### **过滤器**

![数据流中决策节点 LN_companyno 分支到筛选节点和 API 节点以及三个 End 节点](https://lh7-us.googleusercontent.com/1Cv1XxqdpiNfonz6jdFgz9zGibQTRLd\_0ONFHf3FvzPB9-sQuX4lTUyuDWzm-RffuPf5jDmZAZwUqbXX-1kers1sEb9ykRMHeYYP6zGgF8yZ247Dx0nG04kSYUTTKSwt3NLS-3TwXA5tbvy5z8HA2bw)

#### **过滤器 1（顶部）– 全额**

名称和描述取决于所使用的环境以及您的偏好。

![Filter Properties 对话框，Name 和 Description 均为 TaxRateFull](https://lh7-us.googleusercontent.com/WVKWUme9uUjRRn7dZ5c\_RyPk\_GCTFEfiNxU\_H5aA979k5hOv2coDYEJHu4K1EaTLUf8\_Pd9ffOk757DaflF0Se0gZ1ZYvRk4QHlpKP0IeirfNr-L6JU3Z\_xFZJ2eeFI-Rhcctwk9QOHRORGNt1oIEpE)

![Filter Properties 对话框的 Attributes 选项卡，显示属性 RateNumeric 和文档路径 LnTaxCode/SingularRatesGroup/SingularRate/RateNumeric](https://lh7-us.googleusercontent.com/1gCPbUtC7KknzEHVZqIMKyjQGmNyNnR4c1mJ5x0LCJnAjd8D3SdW3W6nPMTsLokL-W2-XjoSM9MU1mJ77K12g887r\_jHoHBwquN1Ore2AmyjCaf\_YVT78KiKtY\_itlr-vyMvJrU7YV6ErgVSYbw5SEU)

![Filter Properties 对话框的 Conditions 选项卡，在 RateNumeric 路径上设置条件 TaxFull OR Tax16 OR Tax20](https://lh7-us.googleusercontent.com/ijzGaLt9Uhzw6Wf66ah3auWo5TbkCnM-xGDYezsXXjPEkdCe5RO1wWfhhhG0qRuKbojijLKUm-WUV21eRdq36moWu9Ft0ujexe\_1lTUUEQbfXPvtrzP7iudkSaG\_oiX\_LV7AqZRGlNAp0OXnN8BXRIM)

#### **过滤器 2（中间）– 减额**

名称和描述取决于所使用的环境以及您的偏好。

![Filter Properties 对话框，Name 和 Description 均为 TaxRateReduced](https://lh7-us.googleusercontent.com/pKLo6q5zCQOZQhiRppyd8M-nlIrX5leGUiCct4Xn-4teIZTip5GAJVP0EFc2PrJ6EeDmU2KVOHRKVCaaML4sK8jCnsgTmxbTYjc-9CNd6bOfU-WD9tySeKL7gSRltjzoTEI5Ozrd\_s-7qj2KVNOWN7s)

![Filter Properties 对话框的 Attributes 选项卡，显示降低税率筛选器的属性 RateNumeric](https://lh7-us.googleusercontent.com/87PoQQ5q\_35buL\_VNcvz3v-um1upk1U579LDASCJptnnC8ip5mwXxz89d1YmtIK59dOUhl9dfz6BrXBLSNUy6EnWU5uPmUEzbLQv-MwzR0dDkuM1BJ477yre-X4QeJzkkzprF9y5wCWY4zvaooMwIZ0)

![Filter Properties 对话框的 Conditions 选项卡，在 RateNumeric 路径上设置条件 TaxReduced AND TaxReduced2](https://lh7-us.googleusercontent.com/Pa19AN6Mhxbn6bHSc5qKEGM0xRsEV6v77ooyeg5-91i8qGhaThb4328nr\_g6a\_z-7BOCJmWpo8Gbd2twl9FQkOf1Q8QZqOkJmxsIxaTP0R6dASgZdIV6z7p8PFYPYUJ1eKp8btYOBapliANstQSUgAQ)

#### **过滤器 3（底部）– 免税**

名称和描述取决于所使用的环境以及您的偏好。

![Filter Properties 对话框，免税税率筛选器的 Name 和 Description 字段为空](https://lh7-us.googleusercontent.com/c\_SuWaZ3gF-FbOPWkxB\_eFgkT-TGJEYwV\_fQT05wGWHFNzI9SDZRQfauVMeBl0rn79QdU-W3kRgN-hWsYkfdMSevlYyiNPxxT\_3RxXcETo-lkjvI5TCygUag91PFJycrRdMA5hSQJCuzt8FekMwpu98)

![Filter Properties 对话框的 Attributes 选项卡，显示免税税率筛选器的属性 RateNumeric](https://lh7-us.googleusercontent.com/HGZ8fR6XgYtZ46i8Rov8xIr5J4z8DmGFfJkeovDGzT7S68VYI-OdG5jpMdoOiROIZckYMbVIlPQmS\_kWQazJVbco1t4ZH5Sr73b4xePlisnbm9ZLJrOPwtXn7-90F1FcFH99P6ZKI0hCWdI6z4d7qNA)

![Filter Properties 对话框的 Conditions 选项卡，在 RateNumeric 路径上设置条件 TaxFree](https://lh7-us.googleusercontent.com/\_APmMO6A2AG2km4H4em-ZMrn6\_XRpO3zxRhZwftiaKi5uoDhv3TTzCBfi8WVDCf6mOQNgtcEJ-z-BmP28J86noGJ5dgqVni2QIxePaO5-LU8fdwRqySUQt\_6wmFWiOFzTMmItcClQPRaSKUaosgWwNk)

### **API**

![数据流中的 API 节点和决策节点 LN_companyno 与其 End 节点相连](https://lh7-us.googleusercontent.com/XDhVCKHYaxrRIFyYfq0guXwnZH6jK-WZIFj2i0Wkr4kxyNcdCH1TzKd0Pb3-H6qs-b7JZ3UUIGm0BVHiUL7Aya-D7YOSV8p8tnwQeAfBN30T4fW5-ANePN1TcvUr1gzLJPwj7rRO4Hw4ziuyYrqZBX8)

此处需要选择之前创建的 API 连接点：在“Select ION API Connector”下拉菜单中选择相应的 API。

#### **API 1（顶部）– 全额**

名称和描述取决于所使用的环境以及您的偏好。

![ION API Activity Properties 对话框，Name 和 Description 为 DocBits-PRO-Full，ION API Connector 为 DocBits-PRO-Import-LnTaxCodeFull](https://lh7-us.googleusercontent.com/90c2E47fMC9CKNVY8DtgyaNUAqAnQmfErZm\_R-njUlEdIX6mafMUOk3GcAooaWfCzD4-OmdPUq5VSuMXmTSNjVEc924ASIPqmTxAQXqsq6eKs5y82rvwHxqnsT4S-sEm2mQRNwleiubkwIO\_kS9Vwzg)

#### **API 2（中间）– 减额**

名称和描述取决于所使用的环境以及您的偏好。

![降低税率的 API 调用的 ION API Activity Properties 对话框，显示 ION API Connector 和 ION API Call Name 字段](https://lh7-us.googleusercontent.com/vw1hM3W4eCt\_8OG7Ht203tckaWarPOLi463WvQzGgixTMnfk7iC27JzL3iNgd5LmvBzWTFnYa3QNy5y\_oNSHJ9R-Ck5CAgLoBmGurbCn1RZ32jiSJr-LUnL3b0nhHctBqcCx\_25L1Ce-\_va3ZgfKXY8)

#### **API 3（底部）– 免税**

名称和描述取决于所使用的环境以及您的偏好。

![ION API Activity Properties 对话框，Name 和 Description 为 DocBits-PRO-Free](https://lh7-us.googleusercontent.com/C0wmqAkrlgyXlMjKsGMOqre4MPLuHawrZB1oYDzkGFocperUB5dKea7kx44hrA\_Kz6Ptx495cQbwq\_EHfEGNvvpr\_0dvCuUS2zz0-SARyuNbf2gKsK3vTdd4Sfg3jWtE1YAN3o0VpoK\_HRn7T-fFOR8)

完成上述所有步骤后，点击以下按钮 SAVE 并 ACTIVATE 数据流。

![数据流画布下方的保存和激活按钮](https://lh7-us.googleusercontent.com/f8gkYY1Z\_W1if2h1es9vbjebtDX0zGiqY4p9OD68gKSAcNU6si-guvyIg8hzdjP7TulZ6Yq8NcbT2EyuHleVeNxpY\_6TDlbgIUaxDJ72ILcy8kVvFuSja7FT6gpYhMLFGw7wv-r0XyFN8xIrQ3OuUGI)

## **BOD 触发（LN）**

在 Infor 中打开 LN。

![Infor LN 起始页，显示应用程序菜单和公司选择](https://lh7-us.googleusercontent.com/aAKRLInqsogQLv9nye2rHLtVFlW4yaCpnQ8A4cKG5A2145Tl6poOxthfo2InYimNk5dd8RabYrX9xP7sPO0aJ5ThF07ZVfKvUXBqVoxRJg53IhpeOeiA4B\_CGOpeLKWlPbCf4EaFXjgzmBOcezocF9k)

导航至 Common → BOD Messaging → Publish BODs → Publish Financial Master Data。

![Infor LN 中的 Publish Financial Master Data 会话，显示 Options 选项卡、Insertion 模式和公司选择](https://lh7-us.googleusercontent.com/pMAgPzyhBNrEsFkTm8-iniHBhEXIPswoJ8URt\_v0fv\_7dSayrS8UkN7F9WMAOZQB9Q6sCe9faRl4rRDDft3VdrzfNUT-IbWxE6GyWPPKZh4R67JRmXmJ2NsTVPdjLo6uJdCpki7QDpgiY\_azWtqaqKA)

选择 MORE，然后点击 LnTaxCode。

![Publish Financial Master Data 会话的 MORE 菜单，列出 AccountingBookDefinition、AccountingEntity 和 LnTaxCode 等 BOD](https://lh7-us.googleusercontent.com/MtjE7Glgv7e\_F\_CJ4LXMuWk6SaInmNFlKzhGJu71iGgxRWtjI96lX5J0gqxRcj3y1u4E6Aq-xNEpuf83dsjHh6op0qeH89oBMvlVTTD\_VhGs10-gjuIb0eyc9b3dcCk75Wa5sASreXKW6SbQPYrs8sM)

勾选复选框以选择 LnTaxCode BOD。

![BOD 列表，LnTaxCode 行已勾选，并显示 PROCESS、CLOSE、SELECT ALL 和 CLEAR ALL 按钮](https://lh7-us.googleusercontent.com/VTFntcBK0GVsUdr\_fZBUaN8rXYdufObLE7PnwwNg9QU69zYwKHvwFZ7En9WZ6p\_WGIkVdqEjBBYeIYSuHHJWBWYonwd6Edtr0ZZuGsX3qhNMDWQWefOaGfrYxrq\_yLm6\_gEw967PGp3HK0hzO-G2XiQ)

返回 OPTIONS 选项卡，配置应如下所示。

![Publish Financial Master Data 会话的 OPTIONS 选项卡，显示模式、公司选择范围 005108 和 Settings 选项](https://lh7-us.googleusercontent.com/2tr7VHNOLActJCiLGC6jyWsdyqwZV7Je6UsekeoBo57qNpOBDYtOQuoelKOdvLMRo6uQJWn1S4ir\_zRZHAx2C96NyKp4ZjIUyFCYt58T59TqO3ml0ZfiEtSLwdRPp9g8pkMemN0xDS5ao8DL5xgosWE)

需要发布 BOD 时，选择 PROCESS。

最终，DocBits 环境中应会显示类似的表格。

![DocBits 中的文档列表，显示已导入的税码文档及其处理状态](https://lh7-us.googleusercontent.com/4wK-mfKl0UNqvp5ngolE54miiwAKxAcOERO2mSDWzZ5t838VhFZrZGzCMeIyg7WDPpHvNzkeWRJV7ZZdsaxwXiFS9uxm29QZUYHhs9gU2v6QgSz07vfjpHXW3oTb5ZiiiTjI93gmV9MDTHbNWJmrvHY)

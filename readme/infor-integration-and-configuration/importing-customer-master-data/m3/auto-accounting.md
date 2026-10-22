# 使用 Infor M3 自动会计

使用本指南规划 DocBits 中 M3 自动会计所需的主数据。仅启用设置不会导入科目或成本要素。您的 Infor 管理员必须确认 BOD 映射、DocBits API 操作，以及您所在组织中的处理结果。

## 检查 DocBits 设置

管理员可以打开**设置 → 模块 → 订单与财务 → 自动会计**。**类型**菜单提供 **LN** 和 **M3**。选择与实际集成相符的系统，并在主数据和数据流就绪后启用；更改类型和开关会保存组织设置。下图中的测试环境当前显示 M3，不能据此推断主数据导入或会计处理已成功。

<figure><img src="../../../.gitbook/assets/site-complete-auto-accounting-settings-zh.png" alt="中文自动记账模块入口；此测试环境当前显示 M3。截图只展示类型与开关，不代表账户、维度或实际记账结果已经验证；未更改配置。"><figcaption><p>中文自动记账模块入口；此测试环境当前显示 M3。截图只展示类型与开关，不代表账户、维度或实际记账结果已经验证；未更改配置。</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/site-complete-auto-accounting-types-zh.png" alt="中文自动会计类型菜单的 LN 和 M3 选项。菜单仅被展开，没有改变类型或保存设置。"><figcaption><p>中文自动会计类型菜单的 LN 和 M3 选项。菜单仅被展开，没有改变类型或保存设置。</p></figcaption></figure>

## 准备 M3 数据流

1. 确定要交换数据的 M3 公司和 DocBits 组织。向 DocBits 管理员确认当前哪个 API 操作可接收会计主数据。不要从旧租户的截图中复制端点或凭据。
2. 在 M3 中，确认已为相关会计实体启用所需的 BOD。此前的租户示例使用 `Sync.ChartOfAccounts` 和 `Sync.CodeDefinition` 处理会计维度。请根据您的 M3 配置和接收端 API 契约确认确切的 noun、版本和字段。Infor 介绍了[如何启用 BOD 发布](https://docs.infor.com/m3core/2025.x/en-us/useradminlib_cloud/m3cecoreag_cloud/wbr1509377469290.html)。
3. 在 **ION Desk → Connect → Connection Points** 中配置 M3 源和 API 目标，并指定经批准的 DocBits 操作和服务账户。在 **Data Flows** 中仅路由经批准的文档，检查筛选条件和字段映射，然后保存并激活数据流。请参阅 [Infor 连接点列表](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/documentflowdesk_connectionpointmasterlist.html)和[数据流激活说明](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532178755.html)。
4. 从 M3 发布一个不含敏感信息的测试标识符。初始加载可能会使用 M3 **EVS006**；具体操作和表名称取决于已安装的 M3 版本。请遵循 [Infor 初始加载说明](https://docs.infor.com/m3core/2025.x/en-us/useradminlib_cloud/m3cecoreag_cloud/pbi1544012609638.html)。在 **ION OneView** 中跟踪该标识符经过数据流的情况，并使用 [Infor OneView](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532196155.html) 检查 API 结果。
5. 在 DocBits **设置 → 文档处理 → 查找主数据** 中检查同一标识符。[M3 到 DocBits 的 API 指南](import-from-infor-m3-to-docbits-via-api.md)介绍了导入检查。只有在所需记录已存在且管理员已验证映射后，才启用 M3 自动会计。

## 成本要素

此前的租户示例从 M3 **PPS280** 导出成本要素到 Excel，删减列后通过旧版 HTTP API 页面上传 CSV。这组截图所示流程并非通用的安全导入步骤：需要针对当前环境确认列名、分隔符、端点和身份验证方式。请使用最新的[成本要素表格指南](table-extraction-for-costing-element.md)准备文件，并查看 DocBits 中可用的 CSV 控件。管理员检查文件列是否与目标表匹配之前，请勿上传文件。

如果 BOD 已到达 ION，但 DocBits 中没有出现行，请先检查 ION 路由、API 响应、组织、标识符和映射，再启用该功能。不要仅凭数据流已激活或已有演示数据就判断处理成功。

本页以当前 DocBits 控件和带有来源链接的步骤，替代了一个较早 Infor 租户的 43 张截图。由于无法访问 Infor 租户或实时 BOD 传输，未进行端到端测试；您的租户管理员必须验证最终映射、导入和会计结果。

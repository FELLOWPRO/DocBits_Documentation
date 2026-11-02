# 自动会计

## 从 LN 主数据记录到已检查的科目分配

<figure><img src="../../../.gitbook/assets/process-accounting-zh-20261028.png" alt="Auto Accounting 的财务主数据: Infor LN 集成的数据路径和检查点。"><figcaption><p>Infor LN 集成的数据路径和检查点。 该图是示意性的；您组织的活动设置决定了实际行为。</p></figcaption></figure>

本指南涵盖了 LN 集成的财务主数据的提供。选择 **LN** 或启用 **Auto Accounting** 不会取代提供数据或检查科目分配结果。

| 交接 | 你应该证明什么 |
| --- | --- |
| **LN → BOD 出版物** | 正确的公司和所需的帐户或维度数据；首先计数或模拟选择。 |
| **BOD → ION** | 匹配文档版本、来源、过滤器和映射；跟踪 ION OneView 中的测试标识符。 |
| **ION → DocBits** | 接收端点响应、正确的组织和接受的记录。仅激活流是不够的。 |
| **DocBits → 账户分配结果** | 批准激活后，使用代表性测试文档检查科目和维度对于业务流程是否正确。 |

**可追溯性示例：** 使用来自批准的测试数据集的非敏感测试标识符。在源 BOD、ION 和 DocBits 接收日志中找到相同的标识符。这有助于在特定切换时定位丢失的映射，而不是重复更改交换机。

随后的导出和 ERP 过帐必须单独验证。本指南中的现有图像显示了 DocBits 控件；它们不能证明执行了 LN 传输。以下部分描述了负责管理员的准备工作和端到端验证。技术交接参见[从 DocBits 导出](../../exporting-in-docbits/README.md)。

当 Infor LN 管理员希望 DocBits 使用导入的财务主数据进行自动会计时，请使用本指南。旧版页面展示了来自某个 Infor 租户的 48 个界面。该租户的连接点名称、映射、凭据和端点地址不能作为可复用的配置。

## 在 DocBits 中查找设置

使用管理员账户打开 **设置 → 模块 → 订单与财务 → 自动会计**。**类型** 菜单提供 **LN** 和 **M3**。对于 LN 集成，请确认所选类型为 **LN**。只有在确认目标 LN 公司、BOD 流和已导入的主数据无误后，才启用开关。更改类型或开关可能会影响会计行为，因此请遵循组织的变更流程。

以下中文截图展示当前测试环境的控件：当前值为 M3，类型菜单提供 LN 和 M3。没有选择其他值，也没有保存设置。配置 LN 集成时，应按自己的目标环境检查并选择 LN；不要照搬截图中的当前值。

<figure><img src="../../../.gitbook/assets/site-complete-auto-accounting-settings-zh.png" alt="中文自动会计设置入口。测试环境当前显示 M3；是否应启用及使用 LN 或 M3 必须按实际集成决定，不能根据此图判断主数据或会计处理成功。"><figcaption><p>中文自动会计设置入口。测试环境当前显示 M3；是否应启用及使用 LN 或 M3 必须按实际集成决定，不能根据此图判断主数据或会计处理成功。</p></figcaption></figure>

<figure><img src="../../../.gitbook/assets/site-complete-auto-accounting-types-zh.png" alt="中文自动会计“类型”菜单提供 LN 和 M3。本图只展开菜单，没有选择类型或保存设置。"><figcaption><p>中文自动会计“类型”菜单提供 LN 和 M3。本图只展开菜单，没有选择类型或保存设置。</p></figcaption></figure>

## 准备 LN 和 ION

1. 确认 LN 公司、会计实体、DocBits 组织和目标环境。与 DocBits 管理员商定当前哪个 API 操作和字段映射将接收科目和维度。请将 API 凭据保存在经批准的密钥存储中，切勿放入截图或 Jira 附件。
2. 在 LN 中配置 BOD 发布并验证发布数据设置。Infor 在其 [LN BOD 发布指南](https://docs.infor.com/ln/10.7.in/en-us/lnolh/help/tc/onlinemanual/000520.html)中介绍了 **BOD Parameters (tcbod0100m000)** 和 **Validate Publishing Data Setup (tcbod0300m000)**。
3. 检查 LN 版本和 DocBits 接收操作所需的名词。先前的示例使用 `Sync.ChartOfAccounts` 和 `Sync.CodeDefinition` 传输会计科目表和维度数据。Infor 的 [Publish Financial Master Data (tfbia0200m000)](https://docs.infor.com/ln/2025.x/en-us/lnolh/tfolh/help/tf/bia/tfbia0200m000.html)列出了会计科目表和 CodeDefinition 选项。只有在指定并批准维度映射后，才会显示某些 CodeDefinition 选项卡。在路由这些文档之前，请确认租户中的确切文档版本和字段。
4. 在 **ION Desk → Connect → Connection Points** 中，将 LN 源连接到经批准的 DocBits API 目标。在 **Data Flows** 中路由所选文档，检查筛选器和映射，然后保存并激活。Infor 区分了[保存流与激活流](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532178755.html)。
5. 在 LN 中使用非敏感测试标识符。在 **Publish Financial Master Data** 中，先使用 **Count** 或 **Simulate** 检查所选内容，然后仅在管理员批准的变更流程下使用 **Publish**。发布操作并非针对特定目标：Infor 表示，它会将数据发送给所有订阅方。请在 [ION OneView](https://docs.infor.com/inforos/latest/en-us/useradminlib_cloud/iondeskceug/lsm1436532196155.html)中跟踪该标识符及任何错误。

## 确认 DocBits 中的结果

请 DocBits 管理员在当前导入日志或 API 日志中验证接收到的记录、组织和会计字段。如果相关查找表已开放，请在 **设置 → 文档处理 → 查找主数据** 下搜索同一标识符。ION 流成功激活本身并不能证明 DocBits 已接受记录。如果缺少某个值，请先比较源 BOD、ION 映射、API 响应和目标组织，再启用自动会计。

本次端到端测试无法使用 LN 租户或实时财务 BOD 传输。当前中文图片仅验证 DocBits 控件。租户管理员必须验证最终映射和会计结果。

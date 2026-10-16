# NOVA – 主要版本 2026 年 11 月 4 日

**NOVA R1.1 可用性：** 自 **2026 年 10 月 16 日** 起已在沙盒环境中开放。生产环境发布计划于 **2026 年 11 月 4 日** 进行。

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/zh.mp4" %}

**DocBits 是产品名称。NOVA 是发布周期的名称。** [观看 DocBits 新版本介绍视频](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/zh.mp4) · [字幕](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/nova-release/v1/zh.vtt).

**沙盒服务版本快照：2026 年 10 月 16 日**

NOVA 将之前在 VESTA 中作为测试版提供的所有功能纳入常规功能，同时提供引导式文档验证、更多提升自动化的方式、更清晰的电子发票检查以及对导入和文档处理的更好控制。这些说明描述了以下服务版本中相对于最近发布的 [VESTA 热修复版本 R1.0.15（2026 年 10 月 14 日）](incremental-updates-14-october-2026.md)（包括更早的 VESTA 热修复版本）面向客户的新增内容。

该快照标识了这些说明所涵盖的构建版本。有关在您的沙盒或生产环境中的可用性以及在渠道之间切换的信息，请参阅 [DocBits 发布生命周期](../docbits-release-lifecycle-strategy.md)。具有组织或文档类型开关的功能仍需由管理员启用。

## 原 VESTA 测试版功能：已包含在 NOVA <a href="#former-vesta-beta-features-included-in-nova" id="former-vesta-beta-features-included-in-nova"></a>

**所有原 VESTA 测试版功能均已作为常规功能纳入 NOVA 沙盒。** 对于未使用 VESTA 测试版的客户，这扩展了其团队可用的功能，包括 **管理布局**、[**自定义验证规则**](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) 和 [**转换规则**](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md)。组织设置、文档类型开关和访问权限继续适用。

这些原测试版功能将在 **下一个 VESTA 热修复版本（计划于 [2026 年 11 月 11 日](vesta-hotfix-11-november-2026.md) 发布）** 中成为 VESTA 的正式功能。本公告说明原 VESTA 测试版功能的正式开放；以下章节还介绍了 NOVA 的其他新增功能和改进。

## NOVA 为客户带来的新增内容 <a href="#what-nova-adds-for-customers" id="what-nova-adds-for-customers"></a>

以下比较涵盖了新可用的原测试版功能、新功能以及对现有功能的扩展。VESTA 基线包括仅在测试版中可用的功能；将其纳入 NOVA 的常规功能集是一项面向客户的发布变更。

| 功能 | VESTA 基线（包括测试版） | 客户通过 NOVA 获得的内容 |
| --- | --- | --- |
| **使用原测试版功能** | 通过 VESTA 测试版提供的功能 | **常规 NOVA 功能：** 包含所有原 VESTA 测试版功能。其作为常规 VESTA 功能的引入计划于 2026 年 11 月 11 日的热修复版本中进行。 |
| **验证文档时提供帮助** | 设置助手和表头字段检查 | **新的验证助手：** 识别阻塞字段，跳转到相关值，查看建议的更正，并将聊天窗口保持在独立窗口中。 |
| **通过日常更正改进自动化** | Touchless Intelligence 仪表板、供应商诊断和变更建议 | **新的审查和测量流程：** 提交改进请求，审查学习到的规则建议，查看受影响文档的证据，对机会进行排名，并在激活后测量结果。 |
| **理解和解决电子发票错误** | 电子文档检查、规则目录和 XML 查看器 | **扩展的电子发票验证：** 按验证级别分组的报告、策略控制和变更历史、从报告中拒绝以及在受支持的 PDF 发票内进行 XML 检查。 |
| **控制 FTP/SFTP 导入** | 导入连接和源文件保留或归档 | **新的引导式设置和控制：** 连接向导、逐步日志、可配置的重试和失败通知，以及在成功导入后删除源文件。 |
| **处理规则和布局** | 规则引擎、执行日志和主数据查找后的转换；管理面板需要测试版链接 | **更广泛的访问权限和更好的工具：** 直接打开管理面板，搜索和预览目标布局，打开文档的布局编辑器并记录布局选择执行。 |
| **通过设置助手采取行动** | 设置聊天、预览/确认/撤销和主动导入健康警告 | **额外操作：** 管理失败的连接，查看停用历史，更改选定的配置项，从目录创建非活动验证规则，并观看页面解释。 |
| **控制文档处理** | 组织页面限制和文档重启 | **新的文档级选择：** 使用选定的页数重启，查看已处理与总页数，并选择是否提取隐藏字段。 |
| **匹配复杂交付** | 采购订单匹配和手动行链接 | **更灵活的匹配：** 在任一方向选择行，可选地保留每个匹配的文档子行，并按配置的行列分组导出请求。 |
| **区分已导出和已完成的工作** | 现有导出和 Finished 工作流 | **新增状态控制：** 使用 Exported 进行后续处理，可选择锁定 Finished 文档，并查找因工作流执行限制而被搁置的文档。 |

### 启用需要配置的功能

* **验证助手：** 由组织管理员在 **设置 → 公司信息 → 助手** 中启用。该功能独立于设置助手，默认关闭，需手动启用。
* **改进审查和咨询报告：** 需要组织管理员和 Analytics 访问权限。已学习的建议需要修正历史记录；测量结果需要足够的数据并完成后续观察期。
* **规则和布局控制：** 其文档类型启用开关仍然适用。NOVA 使管理面板无需 Beta 链接即可访问。
* **可选处理行为：** 按连接配置 FTP 清理和重试。一对多子行展开和已完成文档锁定为可选启用设置。

有关您环境中的可用性和发布渠道切换，请参阅[发布生命周期](../docbits-release-lifecycle-strategy.md)。

## 观看功能视频 <a href="#watch-the-feature-videos" id="watch-the-feature-videos"></a>

将以下演示教程与发布说明配合使用，以了解相关功能及其配置。提供简体中文的视频已在下方链接；其他视频均明确标注为英文。

* [选择合适的自动化方式——包括采购订单匹配规则的适用场景 (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/choose-automation/v1/en.mp4)
* [转换规则 (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/transformation-rules/v1/en.mp4)
* [自定义验证规则 (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/custom-validation-rules/v1/en.mp4)
* [布局和选择规则 (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/layouts/v1/en.mp4)
* [Touchless Intelligence (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/touchless-intelligence/v1/en.mp4)
* [电子发票验证 (英文视频)](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/einvoice-validation/v1/en.mp4)
* [用户和管理员访问](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/users/v1/zh.mp4)
* [子组织](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/sub_organizations/v1/zh.mp4)

### AI Table：六段短视频

这些视频为英文。可观看完整系列或选择您需要的主题。

1. [阅读 AI 表格](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part1/v1/en.mp4)
2. [修正列并教导 DocBits](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part2/v1/en.mp4)
3. [三个典型问题](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part3/v1/en.mp4)
4. [折扣、税和零数量行](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part4/v1/en.mp4)
5. [AI 已正确识别的内容](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part5/v1/en.mp4)
6. [助手及权限说明](https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/ai-table-part6/v2/en.mp4)

有关截图和详细操作说明，请参阅 [AI Table 指南](../../end-user-and-partner-section/end-user-section/ai-table/README.md)。

## 验证助手：协助处理当前文档

* **找出阻碍进度的原因。** 询问文档为何无法继续处理。助手会识别受影响的字段、解释问题原因，并提供跳转到相应字段或表格单元格的选项。它使用当前文档和用户自身的访问权限。
* **在上下文中审查建议的修正。** 在支持的情况下，审核人员可以应用建议的字段或表格值、使用主数据候选项、重复查找或打开相关匹配界面。表单更改仍受文档正常审核和保存流程约束。只读文档和无编辑权限的用户不会获得编辑操作。
* **询问匹配和会计相关信息。** 助手可在打开采购订单或会计界面时解释相关上下文。对验证表单的更改在验证界面中进行。
* **在使用前了解改进建议。** 解释将建议的规则或设置与文档的实际值关联起来。在可用时，可包含图示和用户语言的语音讲解。建议始终聚焦于当前文档。
* **在独立窗口中使用对话。** 在审阅文档时将对话弹出到独立窗口。更改表单的操作仍保留在文档窗口中。
* **查看提取值背后的更多细节。** 值来源视图新增了详细信息，例如 OCR 与 PDF 文本层的对比、提取规则匹配情况以及提供该值的查找来源。AI 表格说明增加了更具可操作性的设置建议和更清晰的计数。

组织管理员在 **设置 → 公司信息 → 助手** 下单独启用验证助手，与设置助手分开管理。

## 将重复修正转化为自动化改进

现有的 [Touchless Intelligence](../../administration-and-setup/analytics-dashboard/touchless-intelligence/README.md) 仪表板新增了审核和跟进流程：

* **学习到的规则建议。** 重复的手动修正可以建议一条[转换规则](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md)。管理员可以查看该规则将写入的内容、支持示例，以及该规则将在哪些文档上替换团队已接受的值。建议需经审核后方可成为生效规则。
* **来自审核者的改进请求。** 用户可以从文档助手提交改进请求，供管理员在 Touchless Intelligence 中审核。请求将说明和决策保留在一起。
* **衡量激活后的效果。** 对于支持的转换规则，DocBits 会比较激活前后的手动修正情况，并在旁边显示无接触处理率。衡量使用 14 天周期，并在数据不足时明确标识，而非虚构改进结果。修改规则会为该修订版启动新的衡量周期。
* **咨询报告。** 管理员可以生成跨提取、主数据、采购订单匹配、会计、设置和处理流程的改进机会排名视图。在未经衡量之前，预估影响会标注为估算值。
* **供应商特定的匹配建议。** 重复出现的供应商和物料匹配问题可以为容差或[采购订单匹配规则](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) 的建议提供依据。建议会区分采购订单缺失与规则或容差问题。
* **跟进摘要。** 每周管理员摘要汇总待处理的改进请求、主要改进机会和已完成的衡量结果（在有内容可报告时）。当衡量结果可用时，可以通知请求者。

## 设置助手：更多操作和页面说明

[设置助手](../../administration-and-setup/settings/global-settings/company-information/settings-assistant/README.md)，包括主动的邮件/FTP 健康警告，已在 VESTA 中发布。NOVA 在该现有体验中增加了操作和上下文信息：

* **从健康通知执行连接操作。** 打开受影响的连接，查看可用操作并在助手中确认。健康通知也可以被忽略。基本的按通道警告卡片及其错误/重试信息已在 VESTA 中存在。
* **可见的停用历史。** 在有记录的情况下，已禁用的导入会显示其关闭时间和操作人。
* **更多经审核的操作。** 管理员可以预览并确认支持的操作，例如激活文档类型、重命名分组、更改查找字段的搜索模式、删除字段，或从目录中创建未激活的自定义验证规则。
* **管理失败的导入连接。** 支持的卡片可以在确认后关闭或删除连接。可逆操作提供撤销选项；永久删除会明确标识。
* **页面说明。** 选定的设置页面提供带字幕和文字稿的视频，包括布局、用户、子组织、转换规则以及电子发票验证（在有对应语言版本时）。

## 规则和布局：直接访问和更好的诊断

* **原 Beta 控件成为正式功能。** 管理布局、[自定义验证规则](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) 和[转换规则](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md) 在 NOVA 的文档类型高级设置中直接可见，无需 Beta 链接。其启用开关仍由管理员控制。这些控件将随所有其他原 VESTA Beta 功能一起包含在计划于 2026 年 11 月 11 日发布的 VESTA 热修复中。
* **更实用的规则诊断。** 布局选择规则新增了 **记录执行** 选项。规则搜索支持规则标识符，打开编辑器时会加载当前已保存的规则。现有的规则执行日志仍然是查看已执行内容的位置。
* **选择并打开布局时获得更多上下文。** 搜索目标布局、预览其内容，并从选择规则中直接打开目标。审批选择规则可正确接受受支持的审批布局类型。管理员还可以从文档验证中获取快捷方式，直接跳转到该文档类型的布局编辑器。
* **选择多个条件值。** 诸如 **属于以下之一** 等条件支持选择多个值。
* **更快找到重复检测字段。** 文档类型重复设置中的字段选择器支持搜索。

主数据查找后的转换、基本规则执行日志、更宽的规则编辑器以及标准规则克隆修复已在 VESTA 基线中实现。NOVA 延续了这些功能，并将原 Beta 管理控件作为常规功能提供。

有关设置步骤、示例和测试，请参阅 [自定义验证规则](../../administration-and-setup/settings/global-settings/document-types/custom-validation-rules.md) 和 [转换规则](../../administration-and-setup/settings/global-settings/document-types/transformation-rules.md)。要选择文档使用的布局，请参阅 [布局选择规则](../../administration-and-setup/settings/global-settings/document-types/layout-manager/layout-selection-rules.md)。

## 电子发票验证：更清晰的发现结果和策略控制

* **按验证级别组织的报告。** 发现结果按语法、架构、业务规则、交叉校验规则和国家特定规则分组，并包含其他标准检查和值检查的附加分组。在提供翻译的情况下，消息和摘要使用用户的语言。
* **更完整的检查和更清晰的结果。** 更新后的验证器和报告可区分错误、警告以及组织特定配置后的有效严重性。该页面命名为 **电子发票验证**。
* **按文档类型设置策略。** 管理员可以查看电子发票验证是否已启用，以及失败是否阻止处理。策略视图可识别子类型覆盖，策略变更记录在变更历史中。
* **检查 PDF 发票中的 XML。** XML 查看器可读取受支持的 ZUGFeRD/Factur-X PDF 中嵌入的 XML，打开发现结果所引用的位置并返回文档。
* **附带记录原因的拒绝。** 经授权的审核人员可以从验证报告中拒绝符合条件的文档。报告会根据其错误为审核人员准备一个原因，供其在确认前检查。
* **更多格式修正。** EDNA 公用事业 CII 发票可被识别，XRechnung 增值税映射的修正改善了相关发票值到达 DocBits 字段的方式。

请参阅 [电子文档验证规则](../../administration-and-setup/settings/document-processing/e-documents/validation-rules/README.md)。

## FTP/SFTP 和电子邮件导入

* **引导式 FTP/SFTP 设置。** 连接向导将服务器详细信息、导入选项和配置分开。连接检查和更清晰的错误提示帮助管理员识别不正确的连接或缺失的源文件夹。
* **按步骤查看导入日志。** 查看文件在 FTP 导入中的进度，包括上传和对源文件执行的已配置操作。
* **可配置的重试和通知行为。** 设置后续重试之间的间隔、重试持续时间以及通知接收人。当重试窗口耗尽时，连接可被自动禁用并通知接收人；助手会显示停用通知。
* **导入成功后删除。** 除了保留或归档源文件外，管理员还可以选择在成功导入后从 FTP/SFTP 服务器删除源文件。归档和删除是互斥的替代选项。
* **更可靠的导入恢复。** 防止重叠的 FTP 运行重复上传同一源文件。编辑连接时，除非被替换，否则保留其存储的密码。电子邮件处理在复制失败时不会将消息标记为删除。
* **签名电子邮件支持。** 包含发票的不透明签名 S/MIME 消息可被解包而非跳过。
* **电子邮件配置历史和状态。** 导入设置显示最后保存或激活配置的人员。入站邮件开关反映存储的激活状态，包括新保存的配置。

请参阅 [FTP 导入](../../end-user-and-partner-section/end-user-section/how-to-import-documents/ftp.md) 和 [测试 FTP 导入连接](../../administration-and-setup/settings/document-processing/import/test-ftp-import-connection.md)。

## 文档处理与提取

* **按指定页数重启。** 仪表板新增了重启操作，允许审核人员为特定文档指定要处理的页数，且不超过该文档的实际页数。
* **查看处理限制。** 仪表板可以显示受限文档的已处理页数与总页数。组织的 **处理页数** 设置归入 **分类与提取** 下的文档处理分组中。
* **控制隐藏字段的提取。** 管理员可以通过 **提取隐藏字段** 设置选择隐藏字段是否参与提取。
* **大批量处理更高效。** 批量文档重启、主数据 CSV 导入、PDF 处理以及基于规则的字段提取均获得了性能提升。
* **AI 提取更具韧性。** 超时情况会以超时状态报告，受支持模型的故障可回退至其他可用模型。额外修复处理了 AI 输出中的重复键、已配置的字段同义词以及空的已保存表定义。
* **保留刚输入的值。** 在未先点击其他位置的情况下保存表格单元格可保留已输入的值。含 OCR 混淆月份名称的日期处理更加可靠。

## 采购订单匹配、审批与导出

[采购订单匹配规则指南](../../administration-and-setup/settings/global-settings/document-types/more-settings/purchase-order/purchase-order-matching-rules.md) 介绍了如何启用基于规则的匹配、配置匹配类型和容差、设置执行顺序以及管理规则版本。

* **双向匹配。** 可以选择文档行并将其连接到采购订单行，也可以从采购订单行开始。当多条交货单行对应一条采购订单行时，此功能尤为实用。
* **保留一对多行明细。** 匹配配置现在可以在多条文档行匹配一条采购订单行时，为每条文档行保留独立的子行。此选项默认关闭。通用 API 导出可按已配置的行列对请求进行分组，支持需要独立目标记录的交货或集装箱场景。
* **配置末行回退。** 组织可以控制剩余的文档行和采购订单行是否允许被单行回退匹配。
* **更准确的匹配与显示。** 修复了包装换算匹配的正确价格基准保留问题，计划行继承采购订单行的状态，并显示来自收货行的已收数量。
* **防止过早审批和重复操作。** 当相关采购订单差异尚未审批时，最终审批将被阻止。重复执行工作流不会为同一组创建另一个待办任务，且重复导出检查在审批前执行。
* **区分 Exported 与 Finished。** 导出操作可在成功导出后选择状态。**Exported** 拥有独立的仪表板徽章。启用已完成文档锁定的组织可防止普通工作流或重启重新打开已完成文档；授权覆盖操作会被记录。
* **更清晰的工作流排障。** 仪表板筛选器可查找因工作流执行限制而被搁置的文档。工作流运行可在弹窗中查看，被拒绝的状态变更会指明文档的状态。
* **额外导出修复。** M3 验证和审批重试已调整，条件性供应商导出配置可正确处理。

## 日常可用性与访问

* **更可靠的导航。** 更新后的文档地址为旧链接提供了重定向。NOVA 深度链接在登录后保持目标频道，加载进度会显示页面正在准备的部分。
* **个人工作偏好。** 采购订单列顺序按用户保存，审批界面会记住用户打开的侧边栏面板。
* **更可靠的任务和仪表板视图。** 无指派人的任务可以被列出、打开和指派。任务板在所选组织就绪时重新加载，自定义仪表板日期范围正确应用，并避免重复的文档行。
* **更好的标签和日志。** 管理员可以编辑字段和表格列的翻译键。文档日志列可以调整大小，自定义仪表板列可处理大小写混合的字段标识符，长标签和文件名显示更加一致。
* **通知范围。** 文档状态邮件规则可以限定到子组织。
* **供应商入驻。** 供应商门户注册魔法链接的有效期从 **7 天延长至 21 天**。管理员还可以为供应商布局中的文件字段配置上传错误标题。
* **登录可靠性。** SAML 登录不再复用已过期或已撤销的会话。管理登录支持必需的 MFA 步骤，且非活跃成员资格无法接收新的设置密码邀请。
* **创意板图片。** 上传的图片与创意描述分开存储和提供，从而改进了图片处理。
* **受控渠道切换。** 当环境未启用切换功能时，可将发布渠道设置设为只读。可用性请遵循发布通知。

## 连接的助手和集成工具

对于使用 DocBits MCP 集成的组织和合作伙伴，NOVA 新增了以下工具：列出已解析的验证规则、针对文档测试单个规则而不保存更改，以及解释存储的规则执行证据。连接的助手还可以列出改进请求，并通过与 Web 应用相同的审核流程提交经管理员授权的批准。现有的组织和文档权限仍然适用。

## VESTA 中已具备的功能

NOVA 还延续了以下列出的功能。此前仅限 VESTA 测试版访问的功能，其常规可用性已包含在本次 NOVA 发布中，并计划于 2026 年 11 月 11 日的 VESTA 热修复中提供。以下列表描述了早期功能，以及上述可用性变更和增强功能：

* 原始设置助手、其文档搜索、基本的预览/确认/撤销流程以及主动的电子邮件/FTP 导入健康警告。
* Fast、Full、Nexus 和 Auto AI 层级以及视觉模式设置。
* 表头字段检查以及原始的值来源报告。
* 首个 Touchless Intelligence 发布版、供应商诊断、批量分析和采购订单决策图。
* 底层验证、转换和布局选择规则引擎、主数据查找后的转换以及基本的规则执行日志。
* 早期的仪表板搜索改进、MFA、已验证的组织电子邮件域名、费用容差以及将工作流执行限制增加到 50。

有关 VESTA 发布历史，请参阅 [10 月 14 日 VESTA 热修复](incremental-updates-14-october-2026.md)、[9 月 15 日热修复](incremental-updates-15-september-2026.md) 和 [早期发布说明](README.md#vesta-hotfix-releases)。

## NOVA 服务版本

下表列出**自 2026 年 10 月 16 日起在沙盒中可用的 NOVA 构建版本**及各服务的部署时间。生产环境发布计划于 **2026 年 11 月 4 日** 进行；此沙盒快照不代表最终的生产环境构建版本。时间戳对应各个服务的部署。

| 服务 | 版本 | 部署时间戳 |
| --- | --- | --- |
| API Service | `13.26.5` | 16.10.2026 11:57:49 |
| Auth Bridge | `0.5.11` | 08.10.2026 10:56:15 |
| Auth Service | `1.84.3` | 16.10.2026 12:19:50 |
| Auto Accounting | `1.23.6` | 15.09.2026 09:42:57 |
| Barcode Service | `1.20.3` | 15.10.2026 14:17:18 |
| Docflow Service | `2.13.9` | 15.10.2026 16:14:37 |
| Docnet Service | `1.59.1` | 12.10.2026 00:59:12 |
| Email Service | `1.44.4` | 16.10.2026 11:44:58 |
| Extraction Service | `1.63.1` | 15.10.2026 19:34:17 |
| FTP Service | `1.37.4` | 15.10.2026 10:42:01 |
| Fulltext Service | `1.46.1` | 12.10.2026 05:16:16 |
| Ideas Service | `0.5.6` | 14.10.2026 12:06:00 |
| OCR Service | `1.11.8` | 12.10.2026 01:00:00 |
| Operator Service | `1.45.0` | 12.10.2026 09:35:25 |
| PO Match Service | `1.65.7` | 14.10.2026 16:14:20 |
| Web App | `10.72.2` | 16.10.2026 12:04:41 |

版本号在两个渠道上独立递增。较大的数字本身并不意味着服务具有新的客户功能。已审核的 Auto Accounting、Barcode、Docnet、Fulltext、OCR 和 Operator 变更属于维护或处理可靠性变更；它们在此对比中并未引入独立的客户工作流。Auth Bridge 更新提高了跨区域账户同步的可靠性。

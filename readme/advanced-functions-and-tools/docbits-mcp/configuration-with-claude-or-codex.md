# 使用 Claude 或 Codex 配置 DocBits

先描述预期结果，让助手读取当前配置，再审核建议并执行约定的更改。DocBits MCP 在 Claude 和 Codex 中提供相应工具，权限与所连接的 DocBits 帐户一致。配置更改需要相应的管理员权限。

本指南介绍操作方法，不代表已为客户完成修复，也不代表导出测试已通过。

## 1. 连接正确的组织

根据[端点与登录指南](setup-and-configuration.md)选择区域和环境。以下命令使用 **EU 沙盒**；如果测试组织使用其他端点，请替换 URL。在运行助手的主机上执行命令，然后在浏览器中登录并授权访问 DocBits。

{% tabs %}
{% tab title="Claude Code" %}
```bash
claude mcp add --transport http docbits https://eu.sandbox.api.docbits.com/v3/mcp
claude mcp login docbits
```
{% endtab %}
{% tab title="Codex CLI" %}
```bash
codex mcp add docbits --url https://eu.sandbox.api.docbits.com/v3/mcp
codex mcp login docbits
```
{% endtab %}
{% endtabs %}

在 Codex 应用中使用 MCP 设置，或使用同一主机上与 CLI 共享的配置。Claude Desktop 用户可在套餐支持时添加自定义远程连接器，并使用相同的 HTTP 端点。如果看不到工具，请新建对话。当前客户端说明：[Codex MCP](https://developers.openai.com/codex/mcp) 和 [Claude MCP](https://code.claude.com/docs/en/mcp)。

```text
只读。使用 get_api_info 和 get_current_user 检查当前连接的 DocBits
环境与组织，并列出可用的配置工具。显示组织 ID 和 API 主机，
不要显示令牌或密钥片段。不要修改设置，也不要处理文档。
```

如果尚未确定组织，请读取相关配置并核对响应中的 `org_id`。如果不是目标组织，请停止操作。工具名称可能带有客户端或服务器前缀；请以当前连接实际公布的工具与参数结构为准。

## 2. 修改简单设置

```text
使用 find_setting 查找此测试组织的二维码提取设置，显示准确的
setting_key 和当前值。若匹配多个设置，请询问我具体指哪一个。
如果 apply_setting 支持此设置，请预览启用后的变化，显示
current_value 和 proposed_value。在调用 confirm_setting_change
之前等待我确认这一具体方案。
```

`apply_setting` 只生成预览。您确认具体方案后，`confirm_setting_change(preview_id)` 才会保存更改。随后重新读取设置，并保留返回的 `undo_id`；可在返回的有效期内通过 `undo_setting_change` 撤销。预览通常在 5 分钟后过期，撤销窗口通常为 15 分钟。如果值已改变或预览已过期，请重新生成并审核预览。

对于支持的结构化更改，流程为 `preview_settings_action` → `confirm_settings_action` → `undo_settings_action`。先读取可用的操作类型。如果没有支持的写入操作，请让助手提供 `app_path`，再到 DocBits 中修改。不要编造偏好设置键，也不要用泛化的 `set_preference` 调用替代该流程。

## 3. 排查被保存为 Invoice 的贷项通知单

即使原始 XML 包含贷项代码，Custom 转换仍可能固定输出 `<INVOICE_TYPE>Invoice</INVOICE_TYPE>`。[贷项排查指南及真实 DocBits 界面视频](../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md)介绍了这一配置场景。

```text
只读。根据提供的原始 XML 和文档 ID，确定 eDoc 系列、语法、版本/配置文件
以及原始类型代码。列出 Custom 和 Default 属性。使用
get_edoc_attribute_source 读取实际生效和默认的 TRANSFORMATION 与
EXTRACTION_PATHS，记录 attribute_id、active_version、active_value_id，
并读取版本历史。追踪 TypeCode -> 转换后的 XML -> invoice_type ->
已保存字段、导出预览以及后续脚本。说明证据和仍不确定的事项。
不要激活、删除、重新处理、审批或导出任何内容。
```

请使用**实际检测到的准确格式名称**，不要猜测 ZUGFeRD 或 Factur-X 版本。技术参数 `doc_type_key` 仍可能是 `INVOICE`；需要检查的业务字段值是 `invoice_type`。

| 读取内容 | MCP 工具 |
| --- | --- |
| Custom 和 Default 属性 | `list_edoc_custom_attributes` |
| 生效或默认源代码及当前 ID | `get_edoc_attribute_source`，使用 `source: "effective"` 或 `"default"` |
| 版本历史及草稿 | `list_edoc_attribute_versions`，需要时使用 `include_values: true` |
| 已保存字段、日志、导出预览 | `get_extracted_fields`、`get_document_logs`、`get_export_preview` |

当前激活的版本不能证明历史文档当时使用了哪个版本。如果日志无法确定，请保留这一不确定性。PDF 预览不能证明已保存的类型或实际导出的金额。

<figure><img src="../../.gitbook/assets/edocs-transformation-zh.png" alt="开发环境只读示例：DocBits 源代码与版本编辑器。请通过 MCP 读取本组织实际生效的源代码和激活值；此图不表示已保存更改。"><figcaption><p>开发环境只读示例：DocBits 源代码与版本编辑器。请通过 MCP 读取本组织实际生效的源代码和激活值；此图不表示已保存更改。</p></figcaption></figure>

## 4. 预览最小范围的修正

```text
针对现有 Custom 转换提出最小修改，使代码 381 输出 Credit Note。
保留其他映射以及已经支持的贷项代码。不要将 383 或 384 归为 Credit Note。
显示差异，在测试文档上预览候选代码但不要保存。显示转换后的
INVOICE_TYPE 和相关金额，并明确列出尚未完成的检查。
```

对于**本组织已有的属性**，使用完整候选源代码调用 `preview_edoc_custom_xslt`：

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "candidate_value": "<complete_candidate_xslt>",
  "doc_id": "<test_document_id_in_this_org>"
}
```

将所有占位符替换为您自己响应中的值。XSLT/JSON 必须是完整源代码，并作为 JSON 字符串正确转义。该工具使用同一组织中已有的文档：`TRANSFORMATION` 返回转换后的 **XML**，`EXTRACTION_PATHS` 返回字段和表格，`PREVIEW` 返回 **PDF**，不会保存候选代码。若要比较默认转换，可将默认源代码作为另一个候选值，使用同一个 Custom 属性和文档进行预览。

`compare_edoc_extraction` 比较的是 **EXTRACTION_PATHS**，并要求已有自定义提取路径属性；它不比较两个转换。不要仅为使用该工具创建不必要的覆盖规则。

如果还没有 Custom 属性，请在生产环境创建前停止：`create_edoc_custom_attribute` 创建的首个版本会**立即激活**，没有仅创建草稿的选项。请在测试组织准备新的覆盖规则，或使用 DocBits 编辑器支持的预览与创建流程。不要尝试全局修改共享默认规则。

## 5. 保存草稿，再明确激活

审核差异和预览输出后，重新读取当前源代码。如果期间发生变化，请再次比较。对于已有 Custom 属性，使用 `update_edoc_custom_attribute`：

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "new_value": "<complete_reviewed_xslt>",
  "activate": false
}
```

此草稿步骤必须明确传入 `activate: false`，因为工具默认值为 `true`。记录返回的版本值 ID，并通过 `list_edoc_attribute_versions` 确认旧版本仍处于激活状态。已保存的草稿不会影响正常处理。

完成测试后，让管理员确认具体组织、属性、差异和版本。然后使用 `activate_edoc_attribute_version` 激活：

```json
{
  "attribute_id": "<custom_attribute_id_from_response>",
  "draft_id": "<value_id_of_reviewed_version>"
}
```

`draft_id` 是**版本值的 ID**，不是版本号或属性 ID。重新读取生效源代码和版本历史，确认激活的是准确的值。eDocs 直接使用这些工具，不使用通用设置的 `preview_id` 确认流程。请在目标环境读取 ID；沙盒 ID 不能直接用于生产环境。

## 6. 验证分类、金额和导出

`test_electronic_document` 在不保存文档的情况下试运行**当前激活的配置**，没有选择候选代码或草稿的参数。通过远程 HTTP MCP 调用时，请用 `file_content_base64` 发送原始 XML，并提供 `file_name`；远程服务器无法读取您电脑上的本地 `file_path`。要检查候选配置的完整处理流程，必须先明确将它激活到测试组织。仅预览 XSLT 不能测试后续脚本或导出。

| 原始代码 | 预期检查 |
| --- | --- |
| 380 | Invoice 仍为 Invoice |
| 381 | 贷项通知单变为 Credit Note |
| 261 | 在格式/映射支持时保留贷项行为 |
| 383 | 借项通知单不能仅因调整发票就变成 Credit Note |
| 384 | 更正发票不能仅因执行更正就变成 Credit Note |

同时检查自定义字段、明细、总额和负号设置。在隔离测试组织中处理一个**新的测试文档**，并控制自动导出行为。比较保存的 `invoice_type`、仪表板和 `get_export_preview`。向目标系统实际导出需要另行约定测试；试运行与导出预览均不能证明 ERP 已成功接收。

`validate_all_edocs` 对服务器可用的测试文件进行试运行；`verify_electronic_documents` 会**上传并处理**测试文件。它们不能替代代表性文档和下游验证。如果工具或测试文件不可用，请使用提供的样本。

## 7. 回退，并单独处理历史文档

要回退，请调用 `activate_edoc_attribute_version`，将之前记录的 `active_value_id` 用作 `draft_id`，然后再次检查生效源代码。不要为了修正一个字段而删除整个自定义规则：这会丢失其他映射并恢复默认规则。

不要批量重新处理历史文档。重新处理可能删除已提取数据和导出日志，并重复审批或导出。请逐一检查导出状态、审批和人工修改，再决定如何修正。

其他配置问题可从 `find_setting` 或 `run_config_checks` 开始，让助手给出受支持的操作或界面路径。请在变更记录中保存修改前后方案、测试结果、激活值 ID 和回退参考。

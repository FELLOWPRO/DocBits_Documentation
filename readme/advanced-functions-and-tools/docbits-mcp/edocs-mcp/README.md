# eDocs MCP

DocBits API 提供了一个 **模型上下文协议（MCP）** 服务器，用于检查和自定义电子文档（eDoc）处理。任何兼容 MCP 的客户端（Claude Code、Claude Desktop 或自定义集成）都可以连接并使用这些工具。

## 可以做什么？

使用 eDocs MCP 工具，你可以：

- **检查**任何电子文档类型的分类方式以及适用的提取规则
- **测试**文档经过完整处理管道的情况，而不将其保存到数据库
- **为组织创建自定义规则**，例如 XSLT 预览、提取路径和转换
- **更新**自定义规则并创建新版本（可选择是否立即激活）
- **删除**自定义规则，以恢复内置默认规则
- **验证**所有受支持的 eDoc 测试样例是否都能正确处理

## 权限模型

DocBits 提供了一组适用于所有客户的内置默认规则。这些默认规则使用保留的组织 ID `00000000-0000-0000-0000-000000000000`。

**无法通过 MCP 修改默认规则。** 每个写入工具都会在发出任何请求前检查你的组织 ID。如果解析出的组织 ID 是默认组织，操作会立即被拒绝，不会发出任何 API 调用。

客户只能在**自己的组织内**创建、更改或删除规则。如果你的组织有自定义规则，该规则的优先级高于默认规则。删除自定义规则后，系统会自动恢复默认行为。

```
Your org rule  ──► used if present
      │
      ▼ (if absent)
Default rule   ──► built-in, immutable via MCP
```

## 工具概览

### 检查（只读）

| 工具 | 说明 |
|------|-------------|
| `test_electronic_document` | 对完整 eDoc 管道进行试运行，包括分类、提取和预览；不会保存文档 |
| `list_electronic_document_types` | 列出所有受支持的 eDoc 类型及其配置状态 |
| `get_extraction_rules` | 显示用于为指定文档类型提取字段的 XPath 规则 |
| `get_extracted_fields` | 获取从已处理文档中提取的表头字段 |
| `get_extracted_tables` | 获取从已处理文档中提取的行项目 |
| `get_preview_pdf` | 获取通过 XSLT 渲染的文档预览 PDF |
| `get_preview_image` | 获取已处理文档的渲染页面图像 |
| `extract_edoc_table` | 提取你提供的 XML/EDI 文件，并以平面表格形式返回字段及生成每个字段的规则 |
| `compare_edoc_extraction` | 比较一个文档的默认提取结果、自定义提取结果，以及可选的候选规则结果 |

### 自定义（限定组织范围，默认组织被禁止）

| 工具 | 说明 |
|------|-------------|
| `list_edoc_custom_attributes` | 列出指定文档类型的组织自定义覆盖项和内置默认项 |
| `create_edoc_custom_attribute` | 创建一条自定义规则（EXTRACTION_PATHS、TRANSFORMATION 或 PREVIEW） |
| `update_edoc_custom_attribute` | 为自定义规则添加新版本，可选择立即激活 |
| `delete_edoc_custom_attribute` | 删除自定义规则；系统会自动回退到默认规则 |
| `preview_edoc_custom_xslt` | 在激活前，对 XML 文档试运行 XSLT 转换 |
| `get_edoc_attribute_source` | 获取属性（PREVIEW、EXTRACTION_PATHS、TRANSFORMATION）的可编辑源内容，以便修改 |
| `list_edoc_attribute_versions` | 查看自定义属性的版本历史，包括草稿和当前生效版本 |
| `activate_edoc_attribute_version` | 激活指定版本或草稿（用于回滚） |
| `delete_edoc_attribute_draft` | 删除尚未激活的草稿 |

### 验证

| 工具 | 说明 |
|------|-------------|
| `verify_electronic_documents` | 上传测试样例，并端到端验证分类、提取和预览 |
| `validate_all_edocs` | 对所有 eDoc 测试样例运行试运行管道并报告问题 |

## 属性类型

每条可自定义规则都有特定的类型和格式：

| 属性名称 | 格式 | 用途 |
|----------------|--------|---------|
| `EXTRACTION_PATHS` | JSON | 将 XML 节点映射到 DocBits 字段的 XPath 表达式 |
| `TRANSFORMATION` | XSLT | 提取前应用于 XML 的样式表 |
| `PREVIEW` | XSLT | 用于渲染人类可读 PDF 预览的样式表 |
| `STRUCTURE_DESCRIPTOR` | JSON | 仅适用于 EDI 文档的结构映射 |

`create_edoc_custom_attribute` 工具会根据属性名称自动推断正确的格式。

## 快速入门

### 查看组织自定义了哪些内容

```
list_edoc_custom_attributes
  electronic_document_type: "XRECHNUNG 2.1 CII"
```

返回两个列表：`custom`（组织的覆盖项）和 `default`（继承的共享规则）。

### 为 XRechnung 创建自定义预览

```
create_edoc_custom_attribute
  electronic_document_type: "XRECHNUNG 2.1 CII"
  attribute_name: "PREVIEW"
  attribute_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
```

返回新的 `attribute_id`，请保存此 ID，以便后续更新或删除该属性。

### 更新现有自定义规则

```
update_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
  new_value: "<xsl:stylesheet ...>...</xsl:stylesheet>"
  activate: true
```

创建并激活一个新版本。先前版本会保留在历史记录中。

### 恢复默认规则

```
delete_edoc_custom_attribute
  attribute_id: "069cd17c-673c-7c94-8000-b512417eefe3"
```

移除自定义覆盖项。系统会立即回退到内置默认规则。

## 安全规则

| 操作 | 是否允许 |
|--------|---------|
| 读取默认规则 | ✅ 是 |
| 为组织创建自定义规则 | ✅ 是 |
| 为组织更新自定义规则 | ✅ 是 |
| 为组织删除自定义规则 | ✅ 是 |
| 修改或删除默认规则 | ❌ **绝不允许**——在 MCP 层被拦截 |

尝试向 `00000000-0000-0000-0000-000000000000` 写入内容会返回：

```json
{
  "error": true,
  "blocked": true,
  "detail": "Writing to the default org is forbidden via MCP. Default rules are immutable and shared across all customers."
}
```

## 实际生效的规则与激活

如果电子贷项通知单显示为 Invoice，请按照[分类故障排查指南](../../../administration-and-setup/settings/global-settings/document-types/edi/credit-note-recognized-as-invoice.md)进行检查。该指南涵盖实际生效的自定义或默认源代码、类型代码、Extraction Paths，以及安全激活步骤。

# DocFlow MCP

DocFlow 提供 **模型上下文协议（MCP）** 服务器，让 AI 助手能够以编程方式管理工作流和合作伙伴卡片。任何兼容 MCP 的客户端——Claude Code、Claude Desktop、OpenAI Codex 或自定义集成——都可以连接并使用这些工具。

## 可以做什么？

借助 DocFlow MCP，你可以：

- **列出、创建、更新和删除**高级工作流
- 使用真实或模拟文档**测试工作流**
- 使用 Partner Card SDK**构建自定义卡片**
- **验证、测试、审批和管理**合作伙伴卡片提交
- 直接从 GitHub 仓库**导入卡片**

## 工具概览

DocFlow MCP 将工具分为以下类别。工作流本身是在 DocFlow 设计器中创建和编辑的；MCP 可读取、测试、运行和删除工作流。大多数工作流和 Card SDK 工具对应现有的 REST 端点，详情请参阅 API 参考。以下类别涵盖 MCP 专属功能以及使用 MCP 所需了解的工作流概念。

### 工作流管理

| 工具 | 说明 |
|------|-------------|
| `list_workflows` | 列出当前组织的所有工作流 |
| `get_workflow` | 根据 ID 获取特定工作流的详细信息 |
| `delete_workflow` | 根据 ID 删除工作流 |
| `list_workflow_variables` / `set_workflow_variable` | 读取和设置工作流变量 |

### 工作流测试

| 工具 | 说明 |
|------|-------------|
| `test_advanced_workflow` | 使用可选文档测试高级工作流的执行情况 |
| `run_workflow_with_assertions` | 初始化变量，使用真实执行器运行工作流并检查结果 |
| `list_test_scenarios` | 列出所有工作流测试场景 |
| `list_cards` | 列出可用的工作流卡片/操作 |
| `search_workflow_logs` / `get_workflow_log_detail` | 查找并检查工作流运行记录 |

### Card SDK 管理

| 工具 | 说明 |
|------|-------------|
| `sdk_list_submissions` | 列出所有合作伙伴卡片提交 |
| `sdk_get_submission_status` | 获取提交的验证状态 |
| `sdk_approve_card` | 审批已验证的合作伙伴卡片（管理员） |
| `sdk_reject_card` | 驳回合作伙伴卡片提交（管理员） |
| `sdk_delete_submission` | 停用或删除提交（管理员） |
| `sdk_list_cards_picker` | 列出所有已启用且带有角色标记的卡片 |

### Card SDK 开发

| 工具 | 说明 |
|------|-------------|
| `sdk_create_card` | 根据源代码创建新的合作伙伴卡片 |
| `sdk_validate_card` | 运行验证流程但不保存 |
| `sdk_test_card` | 在沙盒环境中执行卡片 |
| `sdk_import_github` | 从 GitHub 导入合作伙伴应用 |

## 入门

1. [设置 MCP 客户端](setup-and-configuration.md)
2. 了解[工作流工具](workflow-tools.md)
3. 探索[Card SDK 工具](card-sdk-tools.md)
4. 参阅端到端[示例](examples.md)

{% hint style="info" %}
DocFlow MCP 使用 **Streamable HTTP** 传输方式。服务器端点位于 DocFlow 主机上的 `/v3/mcp/`（例如 `https://docflow.docbits.com/v3/mcp/`）。完整 URL 列表请参阅[设置与配置](setup-and-configuration.md)。
{% endhint %}

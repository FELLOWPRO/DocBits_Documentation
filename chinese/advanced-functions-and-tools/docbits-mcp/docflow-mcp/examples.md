# 示例

以下是完整的端到端示例，展示如何组合使用 DocFlow MCP 工具。

## 示例 1：创建自定义卡片并在工作流中使用

本示例将带你完成整个流程：创建合作伙伴卡片、验证卡片、测试卡片、审批卡片，并构建一个使用该卡片的工作流。

### 步骤 1：创建卡片

调用 `sdk_create_card`：

```json
{
  "app_manifest": {
    "id": "com.example.invoice-tools",
    "name": "Invoice Tools",
    "version": "1.0.0",
    "partner": {
      "id": "example-partner",
      "name": "Example Corp"
    }
  },
  "card_manifest": {
    "id": "high-value-check",
    "title": {"en": "High Value Invoice Check"},
    "entry_point": "src/high_value.py",
    "class_name": "HighValueCheck",
    "args": [
      {
        "id": "threshold",
        "title": {"en": "Amount Threshold"},
        "type": "number",
        "required": true
      }
    ]
  },
  "card_type": "condition",
  "source_code": "from api.sdk.base import PartnerCard\nfrom api.sdk.result import CardResult, CardStatus\n\nclass HighValueCheck(PartnerCard):\n    def execute(self, context):\n        threshold = float(self.variables.get('threshold', 1000))\n        total = float(context.document_fields.get('total_amount', 0))\n        if total > threshold:\n            return CardResult(status=CardStatus.SUCCESS, message=f'High value: {total}')\n        return CardResult(status=CardStatus.FAILURE, message=f'Below threshold: {total}')",
  "test_code": "def test_high_value():\n    assert True  # Basic test"
}
```

记下响应中的 `card_id`，后续步骤会用到。

### 步骤 2：验证卡片

使用卡片 ID 调用 `sdk_validate_card`：

```json
{
  "card_id": "returned-card-uuid"
}
```

查看验证报告。5 个阶段都应通过。

### 步骤 3：测试卡片

使用模拟文档上下文调用 `sdk_test_card`：

```json
{
  "card_id": "returned-card-uuid",
  "variables": {"threshold": "1000"},
  "mock_context": {
    "document_type": "INVOICE",
    "document_fields": {
      "total_amount": "2500.00",
      "currency": "EUR"
    }
  }
}
```

确认响应显示 `CardStatus.SUCCESS`。

### 步骤 4：审批卡片

调用 `sdk_approve_card`（需要管理员权限）：

```json
{
  "card_id": "returned-card-uuid"
}
```

现在，该卡片已激活，可在工作流中使用。

### 步骤 5：使用该卡片构建工作流

在 Web 应用中打开 **DocFlow designer**，创建一个高级工作流并添加已审批的卡片作为节点。例如，添加 *Document Received* 触发器、*High Value Check* 卡片，以及 `true` 分支上的 *Approval* 节点。工作流图在设计器中创建和编辑；MCP 不会创建工作流图。

返回助手，确认工作流已存在并读取其结构：

```json
{
  "tool": "get_workflow",
  "workflow_id": "<id from list_workflows>"
}
```

### 步骤 6：测试工作流

调用 `test_advanced_workflow`：

```json
{
  "workflow_id": "new-workflow-uuid"
}
```

查看执行日志，确认每个节点都已正确执行。

---

## 示例 2：使用内置卡片构建工作流

本示例仅使用内置卡片创建工作流（无需自定义卡片）。

### 步骤 1：发现可用卡片

调用 `sdk_list_cards_picker`，查看所有可用卡片及其角色标记：

```json
// Response includes cards like:
{
  "card_id": "doc-type-uuid",
  "card_name": "Document Type Is",
  "is_when": true,
  "is_and": false,
  "is_then": false
}
```

按角色筛选：

- `is_when: true` — 用于 WHEN 节点（触发器）
- `is_and: true` — 用于 AND 节点（附加条件）
- `is_then: true` — 用于 THEN 节点（操作）

### 步骤 2：创建工作流

```json
{
  "name": "Invoice Document Type Router",
  "description": "When document is an invoice, apply validation",
  "nodes": [
    {
      "node_id": "when-1",
      "node_type": "when",
      "position": {"x": 250, "y": 50},
      "label": "Document is Invoice",
      "card": {
        "id": "doc-type-card-uuid",
        "card_type": "document_type_is",
        "version": 1,
        "variables": [
          {"id": "var-uuid", "data": "INVOICE", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "and-1",
      "node_type": "and",
      "position": {"x": 250, "y": 200},
      "label": "Amount > 1000",
      "card": {
        "id": "amount-card-uuid",
        "card_type": "field_value_check",
        "version": 1,
        "variables": [
          {"id": "field-var", "data": "total_amount", "data_type": "string"},
          {"id": "op-var", "data": ">", "data_type": "string"},
          {"id": "val-var", "data": "1000", "data_type": "string"}
        ]
      }
    },
    {
      "node_id": "then-1",
      "node_type": "then",
      "position": {"x": 250, "y": 350},
      "label": "Set Status to Review",
      "card": {
        "id": "status-card-uuid",
        "card_type": "set_document_status",
        "version": 1,
        "variables": [
          {"id": "status-var", "data": "review", "data_type": "string"}
        ]
      }
    }
  ],
  "edges": [
    {
      "edge_id": "e1",
      "source_node_id": "when-1",
      "target_node_id": "and-1",
      "source_handle": "success",
      "target_handle": "input"
    },
    {
      "edge_id": "e2",
      "source_node_id": "and-1",
      "target_node_id": "then-1",
      "source_handle": "success",
      "target_handle": "input"
    }
  ]
}
```

这将创建一个工作流：**WHEN** 文档是发票，**AND** 金额 > 1000，**THEN** 将状态设为待审核。

---

## 示例 3：从 GitHub 导入卡片

如果合作伙伴卡片位于 GitHub 仓库中，可以直接导入：

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main"
}
```

对于私有仓库，请提供 GitHub 令牌：

```json
{
  "github_url": "https://github.com/your-org/docflow-cards",
  "branch": "main",
  "token": "ghp_your_token_here"
}
```

导入后，系统会自动验证这些卡片。使用 `sdk_list_submissions` 查看卡片状态，并使用 `sdk_approve_card` 审批卡片。

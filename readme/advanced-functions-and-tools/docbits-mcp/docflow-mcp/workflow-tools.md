# 工作流工具

DocFlow MCP 提供用于管理和测试高级工作流的工具，以及读取工作流日志和管理工作流变量的工具。

{% hint style="info" %}
**通过 DocBits MCP 网关调用时的工具名称。** 通过统一的 DocBits MCP（`api.docbits.com/v3/mcp`）连接时，每个 DocFlow 工具名称都会带有前缀 `docflow_`：`list_workflows` 调用时为 `docflow_list_workflows`，`run_workflow_with_assertions` 调用时为 `docflow_run_workflow_with_assertions`。参数完全相同。下方列出的是不带前缀的 DocFlow 工具名称。

工作流在 Web 应用的 DocFlow 设计器中**创建和编辑**。MCP 可以读取、测试、运行和删除工作流，但不会创建或修改工作流图。
{% endhint %} Card SDK 工具位于单独的页面，请参阅 [Card SDK 工具](card-sdk-tools.md)。

## list\_workflows

列出当前组织的所有工作流。

**参数：** 无

## get\_workflow

获取特定工作流的详细信息，包括其节点和边结构。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `workflow_id` | string | 是 | 工作流的 UUID |

## delete\_workflow

按 ID 删除工作流（软删除）。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `workflow_id` | string | 是 | 要删除的工作流的 UUID |

## test\_advanced\_workflow

测试高级工作流的执行。可选提供文档 ID，以便使用真实文档进行测试。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `workflow_id` | string | 是 | 高级工作流的 UUID |
| `doc_id` | string | 否 | 用于测试的文档 UUID |

## list\_test\_scenarios

列出该组织的所有工作流测试场景。

**参数：** 无

## list\_cards

列出所有可用的工作流卡片及其条件和配置。

**参数：** 无

{% hint style="info" %}
卡片具有角色标志：`when_condition`（触发条件）、`and_condition`（附加条件）和 `then_condition`（操作）。可根据这些标志判断卡片可用于哪种节点类型。
{% endhint %}

## list\_workflow\_variables

列出该组织的所有工作流变量，包括名称、类型和当前值。

**参数：** 无

## set\_workflow\_variable

创建工作流变量或更新其值。文档类型变量本身没有值；它们由工作流在运行时设置。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `name` | string | 是 | 变量名称 |
| `value` | string | 否 | 新值 |
| `var_type` | string | 否 | 创建变量时使用的变量类型（例如 `string`、`number`、`document`） |

## search\_workflow\_logs

搜索工作流执行日志，以查明运行失败、成功或遇到条件不匹配的原因。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `workflow_id` | string | 否 | 限定为一个工作流 |
| `doc_id` | string | 否 | 限定为一个文档的运行记录 |
| `status` | string | 否 | 用于筛选的运行状态 |
| `keyword` | string | 否 | 按日志中的自由文本筛选 |
| `include_workflow_data` | boolean | 否 | 包含每次运行对应的工作流定义快照 |
| `limit` / `offset` | integer | 否 | 分页 |

## get\_workflow\_log\_detail

获取某次运行的完整详情：原始卡片执行日志，以及运行时的工作流定义。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `log_id` | string | 是 | 来自 `search_workflow_logs` 的日志条目 ID |

## run\_workflow\_with\_assertions

为工作流变量提供初始值，使用真实执行器运行高级工作流，并根据数据库检查运行结果。变量会实际写入，而非使用模拟值；可用此工具从助手集成测试工作流。

**参数：**

| 参数 | 类型 | 必填 | 描述 |
|-----------|------|----------|-------------|
| `workflow_id` | string | 是 | 要运行的工作流 UUID |
| `doc_id` | string | 否 | 要针对其运行工作流的文档 |
| `seed_variables` | array | 否 | 运行前要创建或更新的变量；文档类型变量可通过 `value` 指向某个 `doc_id` |

# 自动会计 BOD 映射

DocBits 的自动会计工作流会使用来自 Infor M3 的两个 BOD，为成本发票补充有效的会计维度：

- **`Sync.CodeDefinition`** — 提供每个会计维度（成本中心、项目、科目组等）的有效值列表。
- **`Sync.ChartOfAccounts`** — 提供科目表以及附加到每个科目的维度配置。

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — 原始 BOD 映射参考（PDF）
{% endfile %}

## Sync.CodeDefinition

→ DocBits 主数据查找表：**m3flexdimension**

#### 情况 1：同一 ID 出现在多个维度中

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### 情况 2：ID 只出现在一个维度中

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### 字段参考

| DocBits 字段 | 描述 |
|---|---|
| `ID` | `m3flexdimension` 中的主键。在**情况 1**中，会将维度代码添加为 M3 `DocumentID/ID` 的前缀，以确保同一代码出现在不同维度中时条目仍然唯一；**情况 2**使用原始 M3 ID。 |
| `Dimension` | 维度名称（例如成本中心、项目）。通过 `substring(..., 21)` 从 `CodeValue/@listID` 中提取 — 详见下文说明。 |
| `ListID` | 完整、未截断的 `ListID` 值。此值与 `Dimension` 一并保留，以便在审计和下游工具中保留原始命名空间前缀。 |
| `CodeValue` | 实际的维度代码值（例如成本中心编号 `1000`）。 |
| `Description` | 代码的易读描述（例如“市场营销”）。 |

### 关于 `substring(..., 21)` 表达式

XPath 的 `substring()` 函数的第二个参数是从 1 开始计数的起始位置，**不是** `listID` 值。M3 发出的 `@listID` 带有一个长度为 20 个字符的命名空间式前缀（例如 `lng.m3.dimension.D1`），因此 `substring(value, 21)` 会返回该前缀之后的维度代码（此例中为 `D1`）。如果你的 M3 发出的前缀长度不同，则必须调整偏移量 — 在针对非标准租户配置自动会计之前，请提供一个 BOD 示例。

维度代码值的规范来源是 `/SyncCodeDefinition/DataArea/CodeDefinition/DocumentID/ID`。此处保留 `substring(@listID, 21)` 形式，作为 `DocumentID/ID` 未填充的租户的备用方案。计划后续优化映射，使其优先使用 `DocumentID/ID`，并按 `CodeDefinitionVariant='Accounting Dimension'` 进行筛选（见下一节）。 <!-- tracked in DOCB-12315 -->

### DocBits 会处理哪些 `CodeDefinition` 变体？

`Sync.CodeDefinition` 是一种通用 BOD，M3 会针对许多不同对象（会计维度、状态代码、分类列表等）发出此类 BOD。对于自动会计工作流，只有包含 `Property/NameValue[@name='CodeDefinitionVariant']='Accounting Dimension'` 的条目才相关。在处理器原生支持此筛选之前，建议在 BOD 到达 DocBits 之前，于 ION DataFlow 中按 `CodeDefinitionVariant` 进行筛选 — 否则，非维度类的 `CodeDefinition` BOD 会被载入 `m3flexdimension`，导致成本发票 UI 中的选择器内容杂乱。 <!-- tracked in DOCB-12315 -->

### 维度如何应用于成本发票

当发票被分类为成本发票时，DocBits 会根据科目表（见下文）建议会计行。对于建议的总账科目所需的每个维度，UI 都会提供存储在 `m3flexdimension` 中的值 — 这些值由最新的 `Sync.CodeDefinition` BOD 预先填充。AP 用户选择正确的值或接受自动建议，随后 DocBits 会通过相应的 `Sync.SupplierInvoice` BOD 将结果导出回 M3。

## Sync.ChartOfAccounts

→ DocBits 主数据查找表：**ChartOfAccounts**

```json
{
    "ID": "//DataArea/ChartOfAccounts/IDs/ID",
    "NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
    "AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
    "Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
    "DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
    "Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
    "Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
    "Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
    "Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
    "Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
    "Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
    "Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
    "Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
    "Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
    "Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
    "Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
    "Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
    "Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
    "Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
}
```

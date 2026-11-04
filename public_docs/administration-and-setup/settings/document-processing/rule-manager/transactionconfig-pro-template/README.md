# TransactionConfig Pro Template

## 配置财务文档处理

_TransactionConfig Pro Template_ 介绍发票、借项通知单和贷项通知单等财务文档的映射示例。规则管理器可使用已配置的 `conflict_resolution` 规则与表达式确定处理操作。这份文档并不能证明您的环境中已部署某个预定义模板。

字段映射、交易类型及工作流决策须针对相应的 Infor M3/LN 集成进行配置。这些示例帮助解释配置方式，不保证结果准确、无需调整即可完成集成，也不保证符合全球财务标准。

### 配置范围

* **映射：** 定义各交易类型的来源字段和目标字段，并验证输出数据。
* **自定义：** 配置业务流程及审批流程的规则。
* **自动化：** 仅自动执行生效规则与表达式明确涵盖的决策。
* **集成：** 检查导出映射及目标 Infor M3/LN 系统的要求。
* **合规：** 单独评估会计和税务要求；配置本身不保证符合法律要求。

## 冲突解决示例

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

### [案例 1、2、3：数量和单价在容差范围内](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**场景:** 发票数量和单价均在相对于 PO 配置的容差范围内。

**示例操作:** 示例映射接受发票数值，并计算数量 × 单价。

### [案例 4、5：数量在容差内，单价超出容差（已审批）](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**场景:** 数量在容差内；价格偏差超出容差，但已获审批。

**示例操作:** 示例映射使用 PO 单价，并在已配置时将获批差额映射为明细费用。

### [案例 6：数量在容差内，单价低于允许下限（已拒绝）](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**场景:** 数量在容差内；价格低于允许范围，且偏差已被拒绝。

**示例操作:** 示例映射使用 PO 价格。带正负号的差额不会自动成为贷项通知单；调整的类型及正负号取决于映射。

### [案例 7：数量在容差内，单价高于允许上限（已拒绝）](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**场景:** 数量在容差内；正向价格偏差已被拒绝。

**示例操作:** 示例映射使用 PO 价格。针对差额的任何通知单或调整均取决于导出映射。

### [案例 8a、9a：数量超出容差（已审批），单价在容差内](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**场景:** 数量偏差已获审批，价格仍在容差内。

**示例操作:** 示例映射使用已获批的发票数量及发票单价。

### [案例 11a：数量高于允许上限（已拒绝），单价在容差内](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**场景:** 数量超出容差且已被拒绝；价格在容差内。

**示例操作:** 示例映射使用获批数量并保留单价。超出数量的处理方式取决于已配置的规则。

### [案例 10a：数量低于允许下限（已拒绝），单价在容差内](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**场景:** 数量低于容差下限且已被拒绝；价格在容差内。

**示例操作:** 示例映射使用获批数量并保留单价。

### [案例 8b、9b：数量和单价均超出容差（已审批）](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**场景:** 数量偏差和价格偏差均已获审批。

**示例操作:** 示例映射使用已获批的发票数值，并应用明确配置的明细费用或调整。

### [案例 10b：数量低于下限且单价超出容差（已拒绝）](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**场景:** 负向数量偏差和价格偏差均未获审批。

**示例操作:** 示例映射使用 PO 值或获批值。任何借项通知单或贷项通知单均须符合相应映射及审批结果。

### [案例 11b：数量高于上限且单价超出容差（已拒绝）](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**场景:** 正向数量偏差和价格偏差均已被拒绝。

**示例操作:** 示例映射使用获批的 PO 值；超出部分的处理取决于生效配置。

### [案例 12、13：明细费用的单位费用在容差内](charge-per-unit-within-tolerance.md)

**场景:** 明细单位费用在相对于 PO 配置的容差内。

**示例操作:** 示例映射接受发票上的明细费用，不作调整。

### [案例 14：明细费用的单位费用超出容差（已审批）](charge-per-unit-outside-tolerance-approved-1.md)

**场景:** 明细单位费用超出容差，但已获审批。

**示例操作:** 示例映射应用获批的明细费用。

### [案例 15：明细费用的单位费用超出容差（已拒绝）](charge-per-unit-outside-tolerance-rejected.md)

**场景:** 明细单位费用超出容差，且已被拒绝。

**示例操作:** 示例映射使用 PO 明细费用或获批值。针对差额的任何通知单均取决于导出映射。

### [案例 12、13：表头费用的单位费用在容差内](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**场景:** 表头单位费用在相对于 PO 配置的容差内。

**示例操作:** 示例映射应用发票上的表头费用，不作调整。

### [案例 14：表头费用的单位费用超出容差（已审批）](charge-per-unit-outside-tolerance-approved.md)

**场景:** 表头单位费用超出容差，但已获审批。

**示例操作:** 示例映射应用获批的表头费用。

### [案例 15：表头费用的单位费用超出容差（已拒绝）](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**场景:** 表头单位费用超出容差，且已被拒绝。

**示例操作:** 示例映射使用 PO 表头费用或获批值。任何单独通知单均取决于已配置的处理方式。

### [税额明细](tax-lines.md "mention")

**场景:** 发票税额与 PO 税额不同。

**示例操作:** 示例映射使用获批的税率和税额。应根据适用税务要求检查配置；此示例不保证符合法律要求。

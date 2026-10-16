# TransactionConfig Pro Template

## 财务文档处理综合配置工具

_TransactionConfig Pro Template_ 是一款功能强大的配置工具，专为企业环境设计，用于管理发票、借项通知单和贷项通知单等财务文档的处理。该工具提供详细的映射和字段定义，使企业能够精准地自动化和自定义财务工作流。_TransactionConfig Pro Template_ 可与现有 Infor ERP 系统无缝集成，确保准确处理复杂交易，同时符合全球财务标准。

### 主要功能

• 详细映射：可在各种交易类型之间精确映射字段，确保数据一致且准确。

• 自定义：支持自定义财务文档工作流，以满足特定业务需求。

• 自动化：自动处理财务交易，减少人工错误并提高效率。

• 集成：可轻松集成现有 Infor M3/LN ERP 系统，增强组织整体财务处理能力。

• 合规性：确保符合国际财务标准和法规，帮助企业有效管理全球交易。



## 冲突解决案例详解

_TransactionConfig Pro Template_ 包含一系列预定义规则，用于处理发票数据与采购订单（PO）数据之间的常见差异。这些规则旨在在出现偏差时自动进行决策，确保财务处理的一致性和准确性。

### [案例 1、2、3：数量和单价在容差范围内](case-1-2-3-quantity-and-unit-price-within-tolerance.md)

**场景：** 与采购订单相比，发票上的数量和单价均在可接受的容差范围内。

• **操作：** 系统接受发票上的数值，并根据提供的数量和单价计算总金额。

### [案例 4、5：数量在容差范围内，单价超出容差范围（已审批）](case-4-5-quantity-within-tolerance-unit-price-outside-tolerance-approved.md)

**场景：** 发票上的数量在容差范围内，但单价超出容差范围，且此偏差已获审批。

• **操作：** 系统会调整单价，使其与采购订单一致，并应用任何必要的行费用以补足差额。

### [案例 6：数量在容差范围内，单价超出负向容差范围（已拒绝）](case-6-quantity-within-tolerance-unit-price-outside-negative-tolerance-rejected.md)

**场景：** 数量在容差范围内，但单价低于可接受范围（负向容差），且未获审批。

• **操作：** 系统拒绝该单价，将其调整为与采购订单一致，并针对差额生成贷项通知单。必要时还可应用额外的表头费用。

### [案例 7：数量在容差范围内，单价超出容差范围（正向偏差已拒绝）](case-7-quantity-within-tolerance-unit-price-outside-tolerance-positive-rejected.md)

**场景：** 数量在容差范围内，但单价超过可接受范围（正向容差），且未获审批。

• **操作：** 系统拒绝发票单价，将其调整为与采购订单一致，并可针对超收金额生成借项通知单。

### [案例 8a、9a：数量超出容差范围（已审批），单价在容差范围内](case-8a-9a-quantity-outside-tolerance-approved-unit-price-within-tolerance.md)

**场景：** 发票上的数量超出可接受容差范围，但已获审批；单价仍在容差范围内。

• **操作：** 系统接受已审批的数量和发票上的单价，并据此处理交易。

### [案例 11a：数量超出容差范围（正向偏差已拒绝），单价在容差范围内](case-11a-quantity-outside-tolerance-positive-rejected-unit-price-within-tolerance.md)

**场景：** 发票上的数量超过可接受范围（正向偏差）并被拒绝，但单价在容差范围内。

• **操作：** 系统将数量调整至已审批的水平，保留单价并处理交易。超出的数量将被拒绝，不予开票。

### [案例 10a：数量超出容差范围（负向偏差已拒绝），单价在容差范围内](case-10a-quantity-outside-tolerance-negative-rejected-unit-price-within-tolerance.md)

**场景：** 数量低于可接受范围（负向容差）且未获审批，但单价在容差范围内。

• **操作：** 系统将数量调整为与已审批的水平一致，同时保持单价不变，并据此处理交易。

### [案例 8b、9b：数量超出容差范围（已审批），单价超出容差范围（已审批）](case-8b-9b-quantity-outside-tolerance-approved-unit-price-outside-tolerance-approved.md)

**场景：** 数量和单价均超出容差范围，但都已获审批。

• **操作：** 系统使用发票上的数量和单价处理交易，并应用任何必要的调整或行费用。

### [案例 10b：数量超出容差范围（负向偏差已拒绝），单价超出容差范围（已拒绝）](case-10b-quantity-outside-tolerance-negative-rejected-unit-price-outside-tolerance-rejected.md)

**场景：** 数量和单价均超出容差范围，且两者均未获审批。

• **操作：** 系统拒绝发票数据，将数值调整为与采购订单一致，并生成必要的借项或贷项通知单。

### [案例 11b：数量超出容差范围（正向偏差已拒绝），单价超出容差范围（已拒绝）](case-11b-quantity-outside-tolerance-positive-rejected-unit-price-outside-tolerance-rejected.md)

**场景：** 数量超过可接受范围（正向偏差）并被拒绝，单价也超出容差范围并被拒绝。

• **操作：** 系统将数量和单价调整至采购订单中已审批的水平，拒绝任何超出部分，并处理交易。

### [案例 12、13：费用行——单位费用在容差范围内](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**场景：** 发票上的单位费用与采购订单相比，在可接受的容差范围内。

• **操作：** 系统接受发票上的单位费用，无需调整即可处理交易。

### [案例 14：费用行——单位费用超出容差范围（已审批）](charge-per-unit-outside-tolerance-approved-1.md)

**场景：** 单位费用超出容差范围，但已获审批。

• **操作：** 系统接受该单位费用并应用已审批的费用，据此处理交易。

### [案例 15：费用行——单位费用超出容差范围（已拒绝）](charge-per-unit-outside-tolerance-rejected.md)

**场景：** 单位费用超出容差范围且未获审批。

• **操作：** 系统将单位费用调整为与采购订单或已审批的水平一致，并生成任何必要的借项或贷项通知单。

### [案例 12、13：表头费用——单位费用在容差范围内](case-12-13-header-charge-charge-per-unit-within-tolerance.md)

**场景：** 表头单位费用与采购订单相比，在可接受的容差范围内。

• **操作：** 系统按发票所列处理表头费用，无需调整即可应用该费用。

### [案例 14：表头费用——单位费用超出容差范围（已审批）](charge-per-unit-outside-tolerance-approved.md)

**场景：** 表头单位费用超出容差范围，但已获审批。

• **操作：** 系统处理已审批的单位费用，并将其应用于交易。

### [案例 15：表头费用——单位费用超出容差范围（已拒绝）](case-15-header-charge-charge-per-unit-outside-tolerance-rejected.md)

**场景：** 表头单位费用超出容差范围且未获审批。

• **操作：** 系统将表头费用调整为与采购订单一致，据此处理交易，并生成任何必要的通知单。

### [tax-lines.md](tax-lines.md "mention")

**场景：** 处理发票与采购订单之间的税额差异。

• **操作：** 系统根据已审批的税率和金额调整税行，确保符合适用的税务法规。

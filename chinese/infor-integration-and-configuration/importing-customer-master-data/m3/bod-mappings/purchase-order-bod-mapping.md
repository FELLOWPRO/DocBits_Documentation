# 采购订单 BOD 映射

本页介绍 DocBits 如何接收 Infor M3 `SyncPurchaseOrder` BOD，并将字段映射到内部的 `PURCHASE_ORDER_HEADER` 和采购订单行表。

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
原始 BOD 映射参考（PDF）
{% endfile %}

## 关键原则

- **DocBits 不进行货币转换。**金额会按照 M3 在 BOD 中提供的值原样保存，并同时保存其 `@currencyID`。可用的表头金额有三种：`ExtendedAmount`（交易货币）、`ExtendedBaseAmount`（公司本位货币）、`ExtendedReportAmount`（报告货币）。
- **DocBits 不进行计量单位转换。**数量会与其 `@unitCode` 一起保存。`ReceivedBaseUOMQuantity` 是 M3 预先计算的基本计量单位值，DocBits 会原样保存。
- **如果有 SXE 阶段值，表头状态以该值为准。**DocBits 会读取 `UserArea/Property[@name='poeh.stagecd']`（值 `1..8` 对应 Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled），并将其作为权威表头状态。标准 `Status/Code` 也会保存，以便在 BOD 未填充 `poeh.stagecd` 时作为回退值。是否发送此 UserArea 属性取决于租户。
- **没有自动的部分数量状态逻辑。**DocBits 不会根据已收数量与订购数量推导状态；M3 提供的状态会被原样采用。
- **`CONO`/`AccountingEntityID` 不属于 PurchaseOrder BOD。**公司编号路由适用于供应商主数据（请参阅[供应商 BOD 映射](supplier-bod-mapping.md)）；采购订单通过 `LocationID` 确定范围。请注意，`LocationID` **并非全局唯一**：当 M3 公司（CONO）在环境之间复制时（例如 PRD → TST），同一个 `LocationID` 可能存在于多个 CONO 下。在这种配置中，请在 ION DataFlow 中按预期的 `AccountingEntity` 筛选入站 BOD 流，以避免不同环境之间发生冲突。

## 表头映射

→ DocBits 主数据查找表：**PURCHASE\_ORDER\_HEADER**

```python
header_mappings = {
            "purchase_order_number": "//DataArea/PurchaseOrder/PurchaseOrderHeader/DocumentID/ID",
            "warehouse_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ShipToParty/Location[@type='Warehouse']/ID",
            "location_id": "//DataArea/Sync/LocationID",
            "status": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Status/Code",
            "supplier_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/PartyIDs/ID",
            "supplier_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/Name",
            "order_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/OrderDateTime",
            "requested_shipment_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/RequiredDeliveryDateTime",
            "total_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "buyer_contact_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/ID",
            "buyer_contact_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/Name",
            "order_last_modified_by": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationPerson/IDs/ID",
            "order_last_modified_on": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationDateTime",
            "disponent_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/IDs/ID",
            "disponent_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/Name",
            "extended_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "extended_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedBaseAmount",
            "extended_report_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedReportAmount",
            "canceled_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledAmount",
            "canceled_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledBaseAmount",
            "canceled_reporting_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledReportingAmount",
            "type_code": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification/Codes/Code[@listID='Purchase Order Types']",
            "type_description": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification[Codes/Code[@listID='Purchase Order Types']]/Description",
            "sxe_stage": "//DataArea/PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='poeh.stagecd']/text()",
        }
```

### 表头字段参考

| DocBits 字段 | M3 来源 | 描述 |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3 采购订单号，主键。 |
| `warehouse_id` | — | 读取 `ShipToParty/Location[@type='Warehouse']/ID`。M3 很少设置 `@type='Warehouse'` 属性；在这种情况下，该字段为 NULL。M3 原生仓库请使用 `location_id`。 |
| `location_id` | `MPHEAD.IAFACI` | BOD 来源的 M3 分部/工厂（仓库）。用于 DocBits 内部的组织/工厂路由，包括与发票工厂匹配。 |
| `status` | `MPHEAD.IAPUSL` | BOD 中原始的 `Status/Code`。当 `sxe_stage` 为空时用作回退值。 |
| `sxe_stage` | `MPHEAD.IAPUSL` | 权威表头状态，取自 `poeh.stagecd` 用户区域属性。M3 SXE 阶段代码 1..8 对应 Ordered、Entered、Released、Allocated、Picked、Delivered、Invoiced、Cancelled。设置后，该值会在工作流决策中覆盖 `status`。启用 `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` 偏好设置后，DocBits 会将此状态传递给关联的发票。 |
| `supplier_id` | `MPHEAD.IASUNO` | 采购订单上的供应商编号。 |
| `supplier_name` | `CIDMAS.IDSUNM` | 供应商显示名称。 |
| `order_date` | `MPHEAD.IAPUDT` | 采购订单在 M3 中的创建日期。 |
| `requested_shipment_date` | — | 如果存在，则从表头级别的 `RequiredDeliveryDateTime` 读取。大多数 M3 配置只在线项目上提供此值；在这种情况下，请使用行级别的 `requested_ship_date`。 |
| `total_amount` | `MPHEAD.IAOURR` | 以交易货币计的订单总额。按 `ExtendedAmount` 原样保存。 |
| `extended_amount` | `MPHEAD.IAOURR` | 与 `total_amount` 来源相同。作为单独的原始列保留，以便追踪，并供需要规范 BOD 路径的下游使用方使用。 |
| `extended_base_amount` | `MPHEAD.IAOUVA` | 以公司本位货币表示的订单总额。M3 有值时会填充此字段；是否填充取决于租户。如果无法复现有值的情况，请提供一个 BOD 示例。 |
| `extended_report_amount` | `MPHEAD.IAOUVB` | 以公司报告货币表示的订单总额。是否填充取决于租户（与 `extended_base_amount` 相同）。 |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | 以交易货币/本位货币/报告货币表示的取消金额。只有发生取消事件后，M3 才会填充这些字段。 |
| `type_code` / `type_description` | — | 从 `Classification/Codes/Code[@listID='Purchase Order Types']` 读取的采购订单类型（及其 `Description`）。例如：`P10` 普通采购订单，`P20` 库存补货采购订单。仅用于显示，不参与筛选逻辑。 |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / linked user | 分配给该采购订单的采购员。 |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | 审计字段。 |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / linked user | 计划员参考信息。 |

## 行映射

→ DocBits 主数据查找表：**Purchase Order**

```python
line_mappings = {
        "sub_line_number": "SubLineNumber",
        "item_id": [
            "Item/ItemID/ID[not(@schemeName)]",
            "Item/ItemID/ID[@schemeName='NonStock']",
        ],
        "supplier_item_id": [
            "Item/ItemID/ID[@schemeName='Supplier']",
            "Item/Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']",
            "Item/SupplierItemID/ID",
        ],
        "schedule_line_number ": "DocumentReference/ScheduleLineNumber",
        "description": "Item/Description",
        "note": "Note",
        "quantity": "Quantity",
        "open_quantity": "OpenQuantity",
        "confirmed_quantity": "BackOrderedQuantity",
        "received_quantity": "ReceivedQuantity",
        "received_base_mou_quantity": "ReceivedBaseUOMQuantity",
        "unit_of_measure": "Quantity/@unitCode",
        "unit_price": "UnitPrice/Amount",
        "unit_price_per": "UnitPrice/PerQuantity",
        "unit_code_price": "UnitPrice/PerQuantity/@unitCode",
        "total_amount": ["TotalAmount", "ExtendedAmount"],
        "extended_amount": "ExtendedAmount",
        "currency": ["TotalAmount/@currencyID", "ExtendedAmount/@currencyID"],
        "buyer_id": "BuyerParty/PartyIDs/ID",
        "buyer_name": "BuyerParty/Name",
        "status": "Status/Code",
        "geo_code": "UserArea/Property/NameValue[@name='GeoCode']",
        "delivery_method": "UserArea/Property/NameValue[@name='m3.DeliveryMethod']",
        "order_multiple": "Classification/Codes/Code[@listID='Order multiple']",
        "standard_quantity": "UserArea/Property/NameValue[@name='StandardQuantity']",
        "promised_delivery_date": "PromisedDeliveryDateTime",
        "requested_ship_date": "RequiredDeliveryDateTime",
    }
```

### 行字段参考

| DocBits 字段 | M3 来源 | 描述 |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3 物料编号。非库存物料会回退到 `@schemeName='NonStock'`。 |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | 供应商侧的物料编号。按以下三个回退路径依次解析：`ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`。 |
| `description` | `MPLINE.IBPITT` | 行项目描述。 |
| `note` | `MSYTXL.TLTX60` | 行备注文本。 |
| `quantity` | `MPLINE.IBORQA` | 订购数量。与 `unit_of_measure` 一起保存（不进行转换）。 |
| `open_quantity` | `CFQA - RVQA` | 尚未完成的数量（订购数量减去已收数量）。使用相同的 `unit_of_measure`。 |
| `confirmed_quantity` | — | 供应商确认的数量。M3 不填充此字段；发送 `BackOrderedQuantity` 的 ERP 会填充此字段。 |
| `received_quantity` | `MPLINE.IBRVQA` | 已收货数量。 |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (base UoM) | M3 自行转换为基本计量单位的已收数量。DocBits 不会计算此值，而是保存 M3 发送的值。可用于库存核算。 |
| `unit_of_measure` | `MPLINE.IBPUUN` | 交易计量单位。适用于 `quantity`、`open_quantity`、`received_quantity`。 |
| `unit_price` | `MPLINE.IBPUPR` | 以交易货币计的单价。 |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | 计价数量及其单位代码（价格修正因子，例如每 100 PCS 的价格）。 |
| `total_amount` | `LNAM + EXEP` | 行总额。按回退顺序 `[TotalAmount, ExtendedAmount]` 解析；缺少 `TotalAmount` 时，`total_amount` 等于 `extended_amount`。两者都存在时，`TotalAmount` 可能包含税费/折扣，而 `extended_amount` 等于 `quantity × unit_price`。 |
| `extended_amount` | `LNAM` / `LNA2` | 原始 `ExtendedAmount`（不含税费/折扣的行小计）。 |
| `currency` | `MPHEAD.IACUCD` | 交易货币。从 `TotalAmount/@currencyID` 读取；如果没有，则回退到 `ExtendedAmount/@currencyID`。 |
| `status` | `MPLINE.IBPUST` | 行状态。保存用于报表；DocBits 不会据此推导工作流逻辑。 |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / linked user | 行级别的采购员。M3 很少在线项目上填充 `buyer_name`；供应商级别的采购员参考信息请参阅[供应商 BOD 映射](supplier-bod-mapping.md)。 |
| `geo_code` | — | 美国/加拿大税务引擎地理代码。仅由会发送此字段的 ERP 填充。 |
| `delivery_method` | `MPLINE.IBMODL` | 行交付方式（M3 `MODL` 代码）。 |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | 供应商确认的交付日期。 |
| `requested_ship_date` | `MPLINE.IBDWDT` | 行上的要求发货日期，即业务上相关的要求交付日期。 |
| `sub_line_number` | — | 可选的子行标识符。有值时会保存；M3 通常留空。 |
| `schedule_line_number` | — | 适用于计划交付采购订单的可选计划行参考信息。 |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | 行订购量级（最小订购倍数）和标准包装数量。 |

## 常见问题

### DocBits 如何处理外币采购订单？

DocBits 不会转换货币。交易金额（`total_amount`、`extended_amount`、`unit_price`）会与其 `@currencyID` 一起保存。如果公司的本位货币或报告货币与交易货币不同，M3 会通过 `extended_base_amount` 和 `extended_report_amount` 提供预先转换的值，这些值会作为表头的附加列保存。

### DocBits 如何推导部分收货状态？

DocBits 不会推导此状态。表头状态反映发送 BOD 时的 M3 SXE 阶段（`poeh.stagecd`）。如果需要部分收货指示，请根据行表中的 `open_quantity` 与 `quantity` 推导。

### 行上的 `total_amount` 和 `extended_amount` 有什么区别？

这两列是为兼容历史数据和 UI 而保留的。`total_amount` 按 `[TotalAmount, ExtendedAmount]` 的顺序解析，因此在缺少 `TotalAmount` 时等于 `extended_amount`。M3 同时发送两者时，`TotalAmount` 可能会在 `extended_amount` 所保存的 `quantity × unit_price` 值基础上包含税费或折扣。

### 为什么仓库映射到两个不同的路径？

`warehouse_id` 读取 `ShipToParty/Location[@type='Warehouse']/ID`，大多数 M3 安装环境会将其留空（很少设置 `@type` 属性）。`location_id` 读取 `DataArea/Sync/LocationID`，M3 始终会填充此值，它对应采购订单所属的分部/工厂。请将 `location_id` 视为 M3 原生仓库标识符。

### 有些字段有文档说明，但始终为空（`buyer_name`、`geo_code`、`confirmed_quantity`、`sub_line_number` 等）。为什么仍然映射这些字段？

这些映射用于防御性兼容：BOD 架构允许这些字段，其他 ERP 或自定义 M3 扩展也可能填充这些字段。M3 将这些字段留空时，DocBits 中相应的列会是 NULL。

### 即使 PurchaseOrder BOD 中没有 `CONO`，我仍应在 ION DataFlow 中筛选 `AccountingEntity`（CONO）吗？

是的，在同一家 M3 公司曾被复制的环境中（例如 PRD → TST，或两个并行租户）。在这些配置中，仅凭 `LocationID` 无法区分不同的 CONO，因此复制公司发出的 BOD 可能与活动环境中的记录冲突。推荐做法是在 BOD 到达 DocBits 之前，在 ION 中按预期的 `AccountingEntity` 值筛选入站流。

### 我的 BOD 始终不包含 `UserArea/Property[@name='poeh.stagecd']`，会发生什么情况？

DocBits 会回退到表头上的标准 `Status/Code` 元素。是否发送 `poeh.stagecd` 取决于租户。如果预期应有此属性但在 BOD 中找不到，请向 DocBits 团队提供一个 BOD 示例，以便我们确认生成该属性的 M3 定制配置。

### 表头上的 `ExtendedBaseAmount` / `ExtendedReportAmount` 真的会填充吗？

只要 M3 在表头发送这些值，DocBits 就会将其保存到专用列（`extended_base_amount`、`extended_report_amount`）中。是否填充取决于 M3 的货币设置：本位/报告货币与交易货币不同的公司通常会收到这两种金额。如果无法在自己的租户中复现有值的情况，请提供一个 BOD 示例，以便我们一起核实相关条件。

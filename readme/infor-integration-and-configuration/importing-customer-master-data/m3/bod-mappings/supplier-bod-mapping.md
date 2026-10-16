# 供应商 BOD 映射

本文介绍 DocBits 如何通过 `SyncSupplierPartyMaster` 和 `SyncRemitToPartyMaster` BOD 接收 Infor M3 供应商主数据。两个 BOD 都会填充 DocBits 中同一个 `SUPPLIER` 主数据表。

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — 原始 BOD 映射参考文档（PDF）
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — 原始 BOD 映射参考文档（PDF）
{% endfile %}

## 关键原则

- **CONO + SUNO 是匹配键。** DocBits 中的 `supplier_header` 行由 `(customer_number = sharedCONO, supplier_number = sharedSUNO)` 唯一标识。这样，一个 DocBits 组织可以整合多个 M3 公司。
- **`variationID` 可防止 BOD 乱序处理。** M3 可能在很短时间内多次发送同一条主数据记录；只有当传入的 `variationID` 大于已存储值时，才会接受更新。两个 BOD 会分别跟踪自己的 `variationID`（`variation_id_supplier_bod`、`variation_id_remit_to_party`）。
- **不会静默覆盖。** SupplierPartyMaster 和 RemitToPartyMaster 共用若干字段（名称、电话、增值税号、银行、状态）。每个 BOD 只更新自己负责的字段，且仅在其 `variationID` 增大时更新。在这些共用字段中，最近收到的 BOD（按 BOD 类型分别判断）生效。
- **多银行账户同步由偏好设置控制。** 默认情况下，最后一个 `FinancialParty` 会写入标头的 `bank_id`。启用偏好设置 `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` 后，每个 `FinancialParty` 条目都会保存到 `supplier_account`（IBAN、账户 ID、货币代码、偏好指示符）。
- **可选地去除 CONO 后缀。** 某些 M3 安装会在公司编号后附加部门后缀（例如 `100_01`）。偏好设置 `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` 会去除末尾的 `_*`，使 DocBits 键保持一致。请注意，启用此设置后，多个按部门发送的 RemitToPartyMaster BOD 会合并到同一个匹配键上，并由 `variationID` 最高的 BOD 生效。请参阅下方常见问题“*每个部门都发送一个 RemitToPartyMaster BOD 时会发生什么？*”。

## Sync.SupplierPartyMaster

→ DocBits 主数据查找表：**SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### 字段参考

| DocBits 字段 | M3 来源 | 描述 |
|---|---|---|
| `sharedCONO` | M3 公司编号 | 映射到 `supplier_header` 上的 `customer_number`。是匹配键的一部分。 |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3 供应商编号。是匹配键的一部分。 |
| `variationID` | BOD 属性 | 存储为 `variation_id_supplier_bod`。只有当传入 BOD 的 `variationID` 大于已存储值时，才会接受该 BOD。缺少此属性时按 `0` 处理（强制更新）。 |
| `supplierName` | `CIDMAS.IDSUNM` | 供应商显示名称。 |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | 来自 `Phone` 通信渠道的电话号码。 |
| `vatNo` | `CIDMAS.IDVRNO` | 增值税标识符。从 `PartyIDs/TaxID` 读取（M3 接收路径不按 `@schemeName` 过滤）。**待确认** — 当 M3 发送多个 `@schemeName` 值不同的 `TaxID` 元素（例如 `VatCode`、`TaxIdentificationNumber`）时，采用第一个。计划增加可配置的 `schemeName` 筛选条件；请提供 BOD 示例，以便我们确定合适的默认值。 <!-- tracked in DOCB-12313 --> |
| `paymentTermId` | `CIDVEN.IITEPY` | 付款条款标识符。 |
| `paymentMethodCode` | — | 付款方式代码（如有提供）。 |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | 指定采购员（M3 用户）的引用标识和显示名称。 |
| `supplier_category` | — | 从 `Classification/Codes/Code[@listID='Supplier Categories']` 读取。可选的 UserArea 扩展字段；标准 M3 安装不会填写该字段。 |
| `supplier_group` | `CIDVEN.IISUCL` | 供应商分类组。 |
| `discount_terms_description` | — | 可选的 UserArea 扩展字段（`eam.UDFCHAR06`），供 DocBits 的折扣日期计算器使用。供应商在此提供折扣天数后，DocBits 会将其与发票日期结合，为应付账款团队计算折扣到期日。 |
| `status` | `CIDMAS.IDSTAT` | 供应商启用/停用状态，取自 `SupplierPartyMaster/Status/Code`。 |
| `bank_id` | `CBANAC.BCBKNO` | 默认银行账户，取自最后一个 `FinancialParty`。启用 `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` 后，也可以将每个 `FinancialParty` 同步到 `supplier_account` 表。 |

## Sync.RemitToPartyMaster

→ DocBits 主数据查找表：**SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### 字段参考

| DocBits 字段 | M3 来源 | 描述 |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3 公司 / `CIDMAS.IDSUNO` | 含义与 `SupplierPartyMaster` 中相同。会关联到同一条 `supplier_header` 行。 |
| `variationID` | BOD 属性 | 存储为 `variation_id_remit_to_party`，与 SupplierPartyMaster 的 `variationID` 分别跟踪。 |
| `supplierName` | `CIDMAS.IDSUNM` | 收款方显示名称。写入共用的 `supplier_name` 列。 |
| `phone` | `CIDREF.IRPHNO` | 来自收款方通信区块的电话号码。 |
| `vatNo` | `CIDMAS.IDCORG` | 收款方的增值税标识符。与 SupplierPartyMaster 中相同的 `@schemeName` 限制也适用，即采用第一个匹配项。 <!-- tracked in DOCB-12313 --> |
| `bank_id` | `CBANAC.BCBKNO` | 收款方银行账户（`FinancialParty[last()]`）。同样适用多银行账户偏好设置。 |
| `status` | `CIDMAS.IDSTAT` | 收款方启用/停用状态。 |

## 两个 BOD 如何在共用的 `SUPPLIER` 表中交互

两个 BOD 都会填充同一条 `supplier_header` 行。对于它们共用的字段（`supplierName`、`phone`、`vatNo`、`bank_id`、`status`），DocBits 会应用以下规则：

1. 按 `(customer_number = sharedCONO, supplier_number = sharedSUNO)` 匹配该行。
2. 将传入的 `variationID` 与同一 BOD 类型已存储的 `variationID` 比较。
3. 如果传入的 `variationID` 更大（或为表示强制更新的 `0`），则更新该 BOD 负责的字段；否则丢弃该 BOD。
4. 不会更改另一种 BOD 类型的 `variationID`，其此前存储的值也会保留。

更新时，与该供应商关联的 `supplier_address` 和 `supplier_account` 行会先删除再重新插入，因此辅助表始终反映最新的 BOD。这样会产生一个副作用：当 M3 按部门分别发送 RemitToPartyMaster BOD 时（有些租户也会在空部门维护银行连接，因此会发生这种情况），`EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` 会去除部门后缀，使每个按部门发送的 BOD 都指向相同的 `(customer_number, supplier_number)` 键。`variationID` 最高的 BOD 会生效。如果这个“胜出”的 BOD 来自没有银行连接的部门，重新插入时就会清除先前 BOD 的银行账户。

## 常见问题

### 如果所有供应商都来自同一个 M3 公司，DocBits 为什么还要跟踪 CONO？

由于 DocBits 从设计上支持多租户，因此 CONO 路由是必需的：一个组织可以接收来自多个 M3 公司的 BOD。CONO 是匹配键的一部分，可避免不同公司的供应商发生冲突。如果你只有一家公司，可以忽略该值，但该键列仍会填入数据。

### 两个 BOD 都写入同一条供应商记录，最新的 BOD 会覆盖所有内容吗？

不会。每种 BOD 类型只负责自己发送的字段，并且更新由各自独立的 `variationID` 控制。SupplierPartyMaster 只更改供应商名称时，不会回滚之后由 RemitToPartyMaster 写入的电话号码。

### M3 从未发送 `Supplier Categories` 和 `eam.UDFCHAR06`，我该怎么办？

这两个字段都是可选的 UserArea 扩展字段。如果没有这些扩展，相应列会保持为 NULL，DocBits 的功能也不会依赖它们。只有在 M3 已配置为发送 `eam.UDFCHAR06` 时，才启用折扣日期逻辑。

### `vatNo` 是否应按 `schemeName='TaxIdentificationNumber'` 过滤？

M3 BOD 接收路径目前会读取 `PartyIDs/TaxID`，而不按 `schemeName` 过滤。该筛选条件用于电子发票 XSLT 路径（Facturae、XRechnung、KSeF），不用于 M3 接收路径。当 M3 发送多个 `@schemeName` 值不同的 `TaxID` 元素时，采用第一个，这可能导致增值税标识符不正确。计划增加可配置的筛选条件；提供来自你所在租户的 BOD 示例，有助于我们确定合适的默认 `schemeName`。 <!-- tracked in DOCB-12313 -->

### 每个部门都发送一个 RemitToPartyMaster BOD 时会发生什么？

有些 M3 租户会同时在空部门和特定部门维护银行连接，因此 M3 会按部门分别发送 RemitToPartyMaster BOD。DocBits 中的匹配键为 `(customer_number = sharedCONO, supplier_number = sharedSUNO)`，部门不属于匹配键的一部分。

- 启用 `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` 后，按部门发送的 BOD 会合并到同一行。`variationID` 最高的 BOD 会生效，并且 `supplier_account` 行只会根据该 BOD 重新插入。如果胜出的 BOD 来自没有银行连接的部门，先前存储的银行账户会被清除。
- 禁用该偏好设置后（CONO 保留部门后缀），按部门发送的 BOD 会指向不同的键，并且可以共存。

如果你的租户会按部门发送 RemitToPartyMaster BOD，且依赖合并后的银行账户列表，请提供一个示例联系我们，以便我们规划改进方案。

### 我想同步每个供应商的所有银行账户，而不只是最后一个。如何设置？

启用偏好设置 `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC`。启用此标记后，BOD 中的每个 `FinancialParty` 条目都会保存到 `supplier_account` 表（IBAN、金融账户 ID、货币代码、偏好指示符）。为保持向后兼容，旧版 `bank_id` 标头列仍会存储最后一个条目。

# 案例 1、2、3：数量和单价在容差范围内

以下场景用于说明一种已配置的映射，并不代表已核实部署的默认模板。实际输出、金额、正负号和文档类型取决于当前生效的 `conflict_resolution` 规则与表达式、导出映射及审批决定。下文提到的借项通知单或贷项通知单均以这些配置为前提；示例不保证自动开具，也不保证符合法律要求。

## 场景：

与采购订单相比，发票上的数量和单价都在可接受的容差范围内。

## 操作：

系统接受发票上的数值，并根据提供的数量和单价计算总金额。

## 示例：

**Purchase Order (PO):**

数量：100 件

单价：每件 $10.00

Total Amount: $1,000.00

**Invoice Received:**

数量：101 件（在 1% 的容差范围内）

单价：每件 $10.05（在 0.5% 的容差范围内）

Total Amount: $1,015.05

**Tolerance Levels:**

Quantity Tolerance: ±2%

Unit Price Tolerance: ±1%


由于数量（101 件）和单价（$10.05）都在与采购订单相比可接受的容差范围内，系统将：


1\. **Accept the Invoice Values:**由于发票上的数量和单价处于定义的容差范围内，因此将其视为有效值并予以接受。

2\. **Calculate the Total Amount:**使用接受的数值计算总金额：

• Total Amount = Quantity × Unit Price

• Total Amount = 101 units × $10.05 per unit = $1,015.05

3\. **Process the Invoice:**系统将按总金额 $1,015.05 处理发票，并相应更新财务记录。

这种做法可确保在可接受容差范围内的轻微差异不会导致发票被拒或付款延迟，从而简化财务流程。

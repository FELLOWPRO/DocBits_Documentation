# 示例脚本

适用于常见 DocBits 自动化用例的生产就绪脚本示例。每个示例都包含完整脚本、分步说明以及所用函数的链接。

## 按用例分类的示例

### 数据验证

- [供应商查询验证](lookup-supplier-validation.md) — 根据主数据验证供应商
- [表格总和验证](table-sum-validation.md) — 验证行项目合计是否与净额一致

### 自动化

- [自动采购订单匹配](auto-po-matching.md) — 触发自动采购订单匹配
- [根据条件自动导出](status-auto-export.md) — 跳过低风险发票的验证
- [到期日计算](due-date-calculation.md) — 计算付款期限并跳过周末

### 业务规则

- [税码检测](tax-code-detection.md) — 根据全文和金额确定税码
- [大额发票审批任务](task-high-amount.md) — 为大额发票创建审批任务
- [动态必填字段](dynamic-required-fields.md) — 根据货币调整必填字段

### 全文与向量搜索

- [重复发票检测](duplicate-invoice-detection.md) — 使用全文搜索查找重复发票
- [相似文档检测](similar-document-detection.md) — 使用向量搜索标记相似文档
- [合规文本搜索](compliance-text-search.md) — 搜索合规关键词（例如，反向征税）
- [ERP 供应商验证](erp-vendor-validation.md) — 根据 ERP 主数据验证供应商
- [从历史记录填充缺失字段](fill-missing-fields-from-history.md) — 根据相似的历史文档自动填充字段

### 旧版示例

- [计算费用总额](calculating-total-charges-script-for-docbits-1.md) — 汇总运费和包装费金额
- [删除空行](delete-lines-with-empty-quantity-and-amount.md) — 删除数量或金额为零的行
- [导出证书编号](formatting-export-certificate-reference-numbers-script-for-docbits.md) — 在参考编号前补零
- [扩展发票编号](generating-extended-invoice-numbers-script-for-docbits-1.md) — 拼接发票 ID 和采购订单编号
- [USD 默认货币](usd-as-default-currency.md) — 将 USD 设为默认货币

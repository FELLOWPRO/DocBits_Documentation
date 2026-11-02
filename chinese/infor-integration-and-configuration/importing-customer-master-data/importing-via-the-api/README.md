---
description: 使用 API 手动将主数据发送到 DocBits
---

# 通过 API 导入

主数据通常会通过 ION 数据流自动进入 DocBits。本节中的页面介绍如何通过 API 测试界面手动发送相同的数据——适用于重新导入记录、加载从未成功接收的数据，或在启用自动数据流之前测试新的字段映射。

每个页面都遵循相同的五个步骤：打开适用于你所在环境的 API 链接，使用 Org ID 和 API 密钥进行授权，填写表单，执行操作，并检查数据是否已送达。

* [导入供应商（Supplier BOD）](supplier-bod.md)
* [导入采购订单（Purchase Order BOD）](purchase-order-bod.md)
* [导入收货记录（Receive Delivery BOD）](receive-delivery-bod.md)
* [从 XML 导入主数据](master-data-xml.md)

## 所需内容

* **API 密钥** — 请参阅 [API 密钥管理](../../../administration-and-setup/settings/global-settings/integration/api-key-management.md)。
* **Org ID** — 位于 **设置 → 集成与 SSO** 下的 **ID** 区域。
* **数据本身**，以 XML 文件形式提供，或提供可粘贴的 XML 内容。

{% hint style="warning" %}
导入会直接写入组织的主数据。执行前，请确认目标环境、区域和组织是否正确。
{% endhint %}

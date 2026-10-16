# 基于条件自动导出

## 此脚本的作用是什么？

当满足特定条件时，自动将文档状态设为“ready for export”：供应商是已知/可信的供应商，且发票金额低于阈值。这样可以跳过低风险发票的手动验证。

## 触发器

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
# Read relevant fields
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Define trusted suppliers for auto-export
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Auto-export for known suppliers with small amounts
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Auto-exported (small amount, known supplier)"
    )
```

## 分步说明

1. **读取净额和供应商名称**，从文档中获取（比较时供应商使用 `is_clean=True`）
2. **定义可信供应商** — 列出已知供应商名称（已清理/大写）
3. **检查条件** — 供应商必须在可信列表中，且金额必须低于 500
4. **更改状态** 为 `"ready_for_export"`，并附上描述性消息

{% hint style="warning" %}
**注意：** 状态更改会触发下游工作流（DocFlow、导出钩子）。请确保条件足够严格，以避免意外导出。
{% endhint %}

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — 更改文档状态

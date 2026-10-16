# 自动采购订单匹配

## 此脚本的作用是什么？

当发票上存在采购订单号时，自动触发采购订单匹配。po-match-service 微服务会将发票行项目与采购订单进行比较，并填充匹配结果。

## 触发条件

文档类型为 **INVOICE** 时触发 `AFTER_FORMATTING`

## 完整脚本

```python
# Read PO number from the document
po_nr = get_field_value(document_data, "purchase_order", "")

if po_nr:
    # Clean up PO number: remove prefix and whitespace
    po_nr = po_nr.strip()
    if po_nr.upper().startswith("PO"):
        po_nr = po_nr[2:].strip()
    if po_nr.startswith("-") or po_nr.startswith(" "):
        po_nr = po_nr[1:].strip()

    # Update cleaned PO number
    set_field_value(document_data, "purchase_order", po_nr)

    # Trigger automatic PO matching
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

## 分步说明

1. 从发票中**读取采购订单号**
2. 通过移除“PO-”或“PO ”等常见前缀，**清理**采购订单号
3. 将清理后的采购订单号**更新**回文档
4. **触发采购订单匹配**，调用 po-match-service 比较发票行项目与采购订单行项目

## 匹配后会发生什么？

`document_data` 将更新以下内容：

- `po_items` — 已匹配的采购订单行项目
- `po_match_status` — 匹配结果（`"matched"`、`"partially_matched"` 等）
- `po_multi_matched` — 是否匹配到多个采购订单

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 写入清理后的采购订单号
- [auto\_po\_match\_for\_purchase\_orders()](../business-logic-functions.md#auto\_po\_match\_for\_purchase\_orders) — 触发采购订单匹配

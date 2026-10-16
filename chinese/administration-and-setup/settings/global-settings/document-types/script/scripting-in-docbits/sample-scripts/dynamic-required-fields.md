# 动态必填字段

## 此脚本的作用

根据文档内容动态设置字段要求。在此示例中：当发票币种不是 EUR 时，汇率字段将变为必填且可见。对于 EUR 发票，汇率字段将隐藏且为选填。

## 触发条件

在文档类型 **INVOICE** 上使用 `ON_FIELD_CHANGE`

## 完整脚本

```python
# Read current currency
currency = get_field_value(document_data, "currency", "EUR")

# Foreign currency: exchange rate is required and visible
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: exchange rate is optional and hidden
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## 变体：采购发票与费用发票

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Purchase invoice: PO number is required
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Cost invoice: PO number not needed, hide table
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## 分步说明

1. **读取控制字段**（此处为币种）
2. **应用业务规则** — 根据字段值设置不同的要求
3. **设置可见性** — 隐藏无关字段，使界面保持简洁
4. **设置必填要求** — 将相关字段设为必填

{% hint style="info" %}
**触发条件选择：** `ON_FIELD_CHANGE` 会在用户每次修改字段时运行，因此要求会实时更新。`AFTER_FORMATTING` 仅在初次提取完成后运行一次。
{% endhint %}

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取控制字段
- [set\_is\_required()](../field-functions.md#set\_is\_required) — 将字段设为必填或选填
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — 显示或隐藏字段
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 设置类别字段
- [delete\_tables()](../table-functions.md#delete\_tables) — 移除费用发票的表格

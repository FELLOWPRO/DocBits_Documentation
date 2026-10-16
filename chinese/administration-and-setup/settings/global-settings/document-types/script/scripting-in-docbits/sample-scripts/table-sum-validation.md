# 表格金额总和验证

## 此脚本的作用是什么？

验证发票表格中所有行合计的总和是否与文档的净额一致。如果差异大于 0.01，则用计算出的总和替换提取的净额，确保行项目与表头字段保持一致。

## 触发条件

文档类型为 **INVOICE** 时触发 `AFTER_FORMATTING`

## 完整脚本

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    # Calculate sum of all line totals
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    # Compare with extracted net amount
    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        if abs(float(net_amount) - total) > 0.01:
            # Line sum differs from header — update net amount
            set_amount_value(document_data, "net_amount", str(round(total, 2)))
    except ValueError:
        pass
```

## 变体：标记为无效，而不是覆盖

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    total = 0
    for row in table["rows"]:
        line_total = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(line_total)
        except ValueError:
            pass

    net_amount = get_field_value(document_data, "net_amount", "0")
    try:
        diff = abs(float(net_amount) - total)
        if diff > 0.01:
            set_field_as_invalid(document_data, "net_amount",
                f"Line total sum ({round(total, 2)}) differs from net amount ({net_amount})")
        else:
            set_field_as_valid(document_data, "net_amount", "Amounts match")
    except ValueError:
        pass
```

## 分步说明

1. 从 `tables_dict` **获取发票表格**
2. **汇总**表格各行中的所有 LINE_TOTAL 值
3. **比较**计算出的总和与提取的净额
4. **更新或标记**——替换净额，或将其标记为无效

## 使用的函数

- [get\_column\_value()](../table-functions.md#get\_column\_value) — 读取行中的列值
- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取净额
- [set\_amount\_value()](../field-functions.md#set\_amount\_value) — 设置更正后的金额
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — 将字段标记为无效
- [set\_field\_as\_valid()](../field-functions.md#set\_field\_as\_valid) — 将字段标记为有效

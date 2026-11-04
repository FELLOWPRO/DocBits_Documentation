# 删除数量和金额为空的行

#### 第 1 部分：删除数量和金额为空的行

脚本的这一部分会处理发票表格，删除数量和总金额均为零或未提供的行。

* **检查 INVOICE\_TABLE：** 首先检查 `tables_dict` 字典中是否存在 `INVOICE_TABLE` 键。
* **遍历行：** 对表格中的每一行，脚本都会初始化标志和变量，用于确定是否存在 `TOTAL_AMOUNT` 和 `QUANTITY` 列，并获取相应的值。
* **检查列名：** 遍历行中的每一列时，查找名为 `TOTAL_AMOUNT` 和 `QUANTITY` 的列。
  * 如果找到 `TOTAL_AMOUNT`，则获取其值。如果该值非零，则将其转换为浮点数。
  * 对 `QUANTITY` 列执行相同的操作：获取其值，并在非零时将其转换为浮点数。
* **标记要删除的行：** 检查完一行中的两列后，如果总金额和数量都为零（包括值为零或列不存在的情况），则将 `row['is_deleted']` 设置为 `True`，标记该行以供删除。

#### 第 2 部分：验证行项目总额与发票总额

此部分会计算发票中所有行项目的金额总和，并与发票报告的总额进行比较，以验证两者是否一致。

* **初始化行项目总额：** 将变量 `lines_total` 设为 0.0，用于累计所有行项目的金额。
* **汇总行项目金额：** 遍历 `INVOICE_TABLE` 中的每一行，提取其中的 `TOTAL_AMOUNT` 并将其加到 `lines_total`。
* **获取并转换发票总额：** 使用辅助函数 `get_field_value` 获取发票总金额，并将其转换为浮点数。
* **比较总额：** 最后，检查计算出的行项目总额（`lines_total`）与发票报告的总额（`total_amount`）之间的绝对差值是否超过 0.05。如果超过，则使用另一个辅助函数 `set_field_as_invalid` 将发票总额字段标记为无效，并说明两者不匹配。

```python
##################################################
# Delete lines with empty quantity and amount 
##################################################


if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        amount_col_found = False
        quantity_col_found = False
        line_amount = 0.0
        line_quantity = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                amount_col_found = True
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
            if col['name'] == 'QUANTITY':
                quantity_col_found = True
                line_quantity = col.get('value', 0)
                if line_quantity:
                    line_quantity = float(line_quantity)
            if amount_col_found and quantity_col_found:
                break
        if amount_col_found and quantity_col_found and (not line_amount and not line_quantity or (line_amount + line_quantity) == 0):
            row['is_deleted'] = True
        
##################################################
# End: Delete lines with empty quantity and amount 
##################################################

##################################################
# Validating Line total againg invoice total
##################################################
lines_total = 0.0
# Getting Lines Total
if tables_dict.get('INVOICE_TABLE'):
    for row in tables_dict['INVOICE_TABLE']['rows']:
        line_amount = 0.0
        for col in row['columns']:
            if col['name'] == 'TOTAL_AMOUNT':
                line_amount = col.get('value', 0)
                if line_amount:
                    line_amount = float(line_amount)
                break
        lines_total += line_amount

# Getting Invoice total
total_amount = get_field_value(fields_dict, "net_amount", "0.0")
if total_amount:
    total_amount = float(total_amount)

# Comparing lines total with invoice total    
if abs(total_amount - lines_total) > 0.05:
    set_field_as_invalid(fields_dict, "net_amount", "Invoice total mismatches lines total", "AMOUNTS_MISMATCH")

##################################################
# End: Validating Line total againg invoice total
##################################################






    
```

#### 总结

该脚本通过以下方式有效确保数据完整性：

1. 删除因缺少数量或金额而无法计入发票财务总额的数据行。
2. 验证各行金额之和与发票总额是否一致，并标出差异以便后续处理。

此自动化有助于保持财务记录准确，对于 ERP 等要求会计和财务报告数据精确的系统尤为重要。

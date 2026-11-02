# Docbits 扩展发票编号生成脚本

本文档详细介绍了“生成扩展发票编号”脚本，该脚本可自动生成扩展发票编号。扩展发票编号将多个文档标识符（例如发票 ID 和采购订单号）组合成一个完整的标识符。此脚本可增强文档的可追溯性，并简化记录管理。

### 用途

此脚本旨在通过自动拼接发票 ID 和采购订单号，简化扩展发票编号的生成流程，从而为每份发票文档提供统一且唯一的标识符。

### 脚本概述

脚本会检查文档中是否存在发票 ID 和采购订单号字段；如果两者都存在，则将其值（以连字符分隔）拼接起来，并更新或创建一个新字段来存储组合后的值。

#### 代码片段

```python
invoice_id = get_field_value(fields_dict, 'invoice_id')
purchase_order = get_field_value(fields_dict, 'purchase_order')

# Combining invoice ID and purchase order number with a hyphen separator
extended_number = '-'.join(filter(None, [invoice_id, purchase_order]))

# Check if there is an extended number to set
if extended_number:
    # Updating the 'invoice_extended_number' field with the combined value
    if not 'invoice_extended_number' in fields_dict:
        new_field = create_new_field('invoice_extended_number', extended_number)
        fields_dict['invoice_extended_number'] = new_field
        document_json['fields'].append(new_field)
    else:
        set_field_value(fields_dict, 'invoice_extended_number', extended_number)
```

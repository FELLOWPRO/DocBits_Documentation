# Docbits 总费用计算脚本

“计算总费用”脚本可自动汇总发票文档中的各种费用和额外金额。本指南将介绍脚本的设置、逻辑和应用，帮助你准确计算文档中的总费用。

### 用途

此脚本旨在动态计算发票总费用，方法是累加不同类型的费用，例如基本费用、运费（Fracht）和包装费（Verpackung）。随后，脚本会将计算结果更新到发票的总费用字段中，确保账单信息准确无误。

### 脚本概览

脚本会从指定字段中获取值，将其转换为浮点数并求和，然后使用结果更新 `total_charges` 字段。如果 `total_charges` 字段不存在，脚本会创建该字段并设置相应的值。

#### 代码片段

```python
total_charges = get_field_value(fields_dict, 'total_charges', None)
fracht = get_field_value(fields_dict, 'additional_amount_2', None)
verpackung = get_field_value(fields_dict, 'additional_amount', None)

# Initialize total to 0
total = 0

# Add fracht to total if it exists
if fracht:
    fracht = float(fracht)
    total += fracht

# Add verpackung to total if it exists
if verpackung:
    verpackung = float(verpackung)
    total += verpackung

# Formatting the total to two decimal places
formatted_total = "{0:.2f}".format(total)

# Checking if the total_charges field exists and updating or creating accordingly
if 'total_charges' not in fields_dict:
    new_field = create_new_field('total_charges', formatted_total)
    fields_dict['total_charges'] = new_field
    document_json['fields'].append(new_field)
else:
    set_field_value(fields_dict, 'total_charges', formatted_total)
```

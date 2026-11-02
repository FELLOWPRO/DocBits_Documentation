---
description: "用于将 USD 设置为默认货币并检查其是否有效的脚本"
---

# 将 USD 设为默认货币

### 概述

此脚本旨在将 USD（美元）设为应用程序或系统的默认货币，确保所有金额均以 USD 显示和处理，除非另有指定。

### 目标

此脚本的主要目标是自动将货币字段填入 USD，并检查其是否有效。

### 脚本实现

#### 代码片段

```
// currency = get_field_value(document_data, 'currency', None)

if not currency:
    if 'currency' not in fields_dict:
        new_field = create_new_field('currency','')
        fields_dict['currency'] = new_field
        document_json['fields'].append(new_field)
    set_field_value(document_data, "currency", "USD")
    
elif currency == "USD US Dollar" or currency == "U.S. Dollars":
    set_field_value(document_data, "currency", "USD")
    
if currency != "USD" and currency != "EUR" and currency != "GBP" and currency != "CAD" and currency != "AUD" and currency != "CHF":
    set_field_as_invalid(document_data, "currency", "Currency is not valid")
else:
    set_field_attribute(document_data, "currency", "is_valid", True)
    set_field_attribute(document_data, "currency", "validation_message","")
```

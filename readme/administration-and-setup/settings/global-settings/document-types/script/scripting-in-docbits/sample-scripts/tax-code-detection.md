# 税码检测

## 此脚本的作用是什么？

根据文档全文内容以及税额/净额，自动确定正确的税码。检测反向征税情形和免税发票，并计算税率以分配相应的税码（例如，19% 对应 S1，7% 对应 S2）。

## 触发条件

文档类型为 **INVOICE** 时触发 `AFTER_FORMATTING`

## 完整脚本

```python
# Get document fulltext and amounts
content = get_document_content(document_data)
tax_amount = get_field_value(document_data, "tax_amount", "0")
net_amount = get_field_value(document_data, "net_amount", "0")

try:
    tax = float(tax_amount) if tax_amount else 0
    net = float(net_amount) if net_amount else 0
except ValueError:
    tax = 0
    net = 0

# Rule 1: Reverse charge detection via fulltext
if "REVERSE CHARGE" in content.upper() or "UMKEHR DER STEUERSCHULD" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Rule 2: Zero tax = tax-free
elif tax == 0:
    set_field_value(document_data, "tax_code", "Z0")

# Rule 3: Calculate tax rate from amounts
elif net > 0:
    tax_rate = round((tax / net) * 100, 0)
    if tax_rate == 19:
        set_field_value(document_data, "tax_code", "S1")    # Standard rate
    elif tax_rate == 7:
        set_field_value(document_data, "tax_code", "S2")    # Reduced rate
    else:
        set_field_value(document_data, "tax_code", "S3")    # Other rate
```

## 分步说明

1. 使用 `get_document_content()` **读取全文**以检测关键词
2. **读取税额和净额**以计算税率
3. 在文档文本中**检查反向征税**关键词（德语和英语）
4. **检查零税额**——如果税额为 0，则分配免税税码
5. 根据税额/净额比值**计算税率**并分配匹配的税码

## 使用的函数

- [get\_document\_content()](../business-logic-functions.md#get\_document\_content) — 读取 OCR 全文
- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取字段值
- [set\_field\_value()](../field-functions.md#set\_field\_value) — 设置税码

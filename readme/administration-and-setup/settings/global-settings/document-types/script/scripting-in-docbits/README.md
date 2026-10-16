# DocBits 中的脚本编写

## DocBits 脚本指南

欢迎阅读 DocBits 脚本指南！在这里，您将学习如何使用脚本自动化和增强 DocBits 中的文档处理。脚本可用于在各种文档类型中自定义字段、转换数据和实现逻辑。

### 入门

DocBits 中的脚本使用 Python 编写。它们与文档字段和元数据交互，以执行各种操作，从简单的数据格式化到复杂的逻辑处理。

#### 关键函数

* `get_field_value(fields_dict, field_name, default=None)`：获取指定字段的值。
* `set_field_value(fields_dict, field_name, value)`：设置指定字段的值。
* `create_new_field(field_name, value)`：创建具有指定名称和值的新字段。
* `format_decimal_to_locale(value, locale)`：根据指定区域设置格式化十进制值。

### 脚本示例

以下示例展示了常见的脚本编写任务。

#### 示例 1：发票币种映射

将币种符号或文本统一转换为 ISO 币种代码。

```python
currency_map = {
    "€": "EUR",
    "EURO": "EUR",
    "$": "USD",
    "£": "GBP"
}
currency_value = get_field_value(fields_dict, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(fields_dict, "currency", currency_value)
```

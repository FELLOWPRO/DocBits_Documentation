# DocBits 中的脚本编写

## 视频教程：最重要的脚本函数

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/settings-assistant/doc-config-script-functions/v3/zh.mp4" %}
DocBits 中最重要的脚本函数
{% endembed %}

视频在脚本编辑器中演示如何读取字段（`get_field_value`）、设置值（`set_field_value`）、计算到期日（`set_date_value`）、将字段标记为无效（`set_field_as_invalid`）并设为必填（`set_is_required`）。

## DocBits 脚本指南

欢迎阅读 DocBits 脚本指南！在这里，您将学习如何使用脚本自动化和增强 DocBits 中的文档处理。脚本可用于在各种文档类型中自定义字段、转换数据和实现逻辑。

### 入门

DocBits 中的脚本使用 Python 编写。它们与文档字段和元数据交互，以执行各种操作，从简单的数据格式化到复杂的逻辑处理。

#### 关键函数

每个脚本都会以 `document_data` 的名称接收文档。请将它作为第一个参数传递给字段函数。完整参考请参见 [字段函数](field-functions.md) 页面。

* `get_field_value(document_data, field_name, default_value=None, is_clean=False)`：读取字段的值。
* `set_field_value(document_data, field_name, value)`：向字段写入值；如果字段不存在，则创建该字段。
* `set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False)`：写入日期，可选择增加天数并跳过周末。
* `set_amount_value(document_data, field_name, value)`：按文档区域设置的格式写入金额。
* `set_field_as_invalid(document_data, field_name, message, code=None)`：将字段标记为无效，并向用户显示该消息。
* `set_is_required(document_data, field_name, value)`：将字段设为必填或取消必填。

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
currency_value = get_field_value(document_data, "currency", None)
if currency_value:
    currency_value = currency_value.upper()
    if currency_value in currency_map:
        currency_value = currency_map[currency_value]
    set_field_value(document_data, "currency", currency_value)
```

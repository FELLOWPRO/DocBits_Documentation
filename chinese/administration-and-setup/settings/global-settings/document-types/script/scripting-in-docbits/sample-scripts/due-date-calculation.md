# 到期日计算

## 此脚本的作用

根据发票日期，通过增加可配置的天数（例如 30 天）来计算付款到期日。系统会自动跳过周末，因此到期日始终为工作日。

## 触发条件

文档类型 **INVOICE** 上的 `AFTER_FORMATTING`

## 完整脚本

```python
# Read invoice date
inv_date = get_field_value(document_data, "invoice_date")

if inv_date:
    # Calculate due date: 30 days after invoice date, skip weekends
    set_date_value(document_data, "due_date", inv_date,
                   add_days=30, skip_weekend=True)

    # Also set accounting date = invoice date
    set_date_value(document_data, "accounting_date", inv_date)
```

## 变体

### 14 天，排除星期一

```python
set_date_value(document_data, "due_date", inv_date,
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

### 60 天，不跳过周末

```python
set_date_value(document_data, "due_date", inv_date, add_days=60)
```

### 将交付日期设为今天

```python
set_date_value(document_data, "delivery_date", None)  # None = today
```

## 分步说明

1. **读取发票日期**：从文档中读取
2. 使用 `set_date_value()` 和 `add_days=30`、`skip_weekend=True` **计算到期日**
3. **日期格式会自动设置**：使用文档的 `date_format_pattern`（例如 `%d.%m.%Y`）
4. **跳过周末**：确保到期日落在星期一至星期五

## `exclude_final_days` 的星期代码

`MONDAY`、`TUESDAY`、`WEDNESDAY`、`THURSDAY`、`FRIDAY`、`SATURDAY`、`SUNDAY`

## 使用的函数

- [get\_field\_value()](../field-functions.md#get\_field\_value) — 读取发票日期
- [set\_date\_value()](../field-functions.md#set\_date\_value) — 计算并设置到期日

# 实用函数

用于字符串处理、数学运算、日期操作、正则表达式和数据类型的内置函数。

**来源：** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## 字符串函数

### 类型转换

```python
str(value)       # Convert to string
int(value)       # Convert to integer
float(value)     # Convert to float
str_to_bool(s)   # "true"/"1"/"yes" → True, everything else → False
```

### 字符串方法

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
这些函数既可作为独立函数使用，也可作为字符串的方法调用：

```python
# Both work:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## 模糊字符串匹配

### levenshtein\_distance()

计算两个字符串之间的编辑距离（即所需的字符更改次数）。

```python
levenshtein_distance(s1, s2)
```

**示例：**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Strings are similar enough
    pass
```

### jaro\_winkler\_similarity()

计算 0.0 到 1.0 之间的相似度分数。

```python
jaro_winkler_similarity(s1, s2)
```

**示例：**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (very similar, typo)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (dissimilar)
```

{% hint style="success" %}
**该使用哪种方法？**
- **Levenshtein**：适用于较短的字符串，可精确计算错误数量
- **Jaro-Winkler**：更适合名称和地址，会更重视开头部分的匹配
{% endhint %}

---

## 正则表达式函数

基于 Python 的 `re` 模块，但可作为独立函数使用。

### re\_search()

搜索模式的首次匹配项。

```python
re_search(pattern, string)
```

**返回值：** 匹配对象或 `None`

**示例 — 从全文中提取订单号：**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

将匹配的模式替换为替换字符串。

```python
re_sub(pattern, replacement, string)
```

**示例 — 从发票 ID 中移除特殊字符：**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

查找模式的所有匹配项。

```python
re_findall(pattern, string)
```

**示例 — 查找文档中的所有采购订单号：**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## 日期/时间函数

### datetime\_today()

以 `datetime` 对象的形式返回今天的日期。

```python
today = datetime_today()
```

### datetime\_date

用于创建日期的 `date` 类。

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

将日期字符串解析为 datetime 对象。

```python
strptime(date_string, format)
```

**示例 — 解析并使用发票日期：**

```python
inv_date_str = get_field_value(document_data, "invoice_date", "")
try:
    date_obj = strptime(inv_date_str, "%Y-%m-%d")
    year = date_obj.year
    month = date_obj.month
except ValueError:
    pass
```

### strftime()

将 datetime 对象格式化为字符串。

```python
strftime(datetime_obj, format)
```

**示例 — 设置处理日期：**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

根据 ISO 日历周创建日期。

```python
fromisocalendar(year, week, day)
```

**示例 — 将日历周转换为日期：**

```python
# CW 12/2026, Monday
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**德国客户的常见情况：** 交货日期通常以“KW 12”的形式表示。模式：

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # Monday of the CW
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

返回某月 1 日是星期几，以及该月的天数。

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**示例：**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## 小数/区域设置函数

### parse\_decimal()

根据区域设置检测，将字符串解析为十进制数。

```python
parse_decimal(value, locale="en_US")
```

**示例：**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

根据区域设置格式化十进制数。

```python
format_decimal_to_locale(value, locale)
```

**示例：**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## 数学函数

完整的 `math` 模块均可使用：

| 函数 | 描述 |
| -------- | ----------- |
| `abs(x)` | 绝对值 |
| `round(x, n)` | 四舍五入到 n 位小数 |
| `floor(x)` | 向下取整 |
| `ceil(x)` | 向上取整 |
| `sqrt(x)` | 平方根 |
| `pow(x, y)` | 幂运算 |
| `log(x)` / `log10(x)` | 对数 |
| `pi` | π (3.14159...) |
| `e` | 欧拉数 (2.71828...) |
| `sin`, `cos`, `tan` | 三角函数 |
| `acos`, `asin`, `atan` | 反三角函数 |
| `degrees`, `radians` | 度 ↔ 弧度 |
| `exp`, `fabs`, `fmod` | 其他数学函数 |
| `hypot`, `ldexp`, `frexp` | 特殊计算 |
| `modf` | 分离整数部分和小数部分 |

---

## 数据结构函数

```python
dict()            # New dictionary
list()            # New list
set()             # New set
tuple()           # New tuple
defaultdict(type) # collections.defaultdict

len(x)            # Length
isinstance(x, t)  # Type check
type(x)           # Get type
deepcopy(x)       # Deep copy (copy.deepcopy)

print(x)          # Debug output (for testing only)
```

{% hint style="warning" %}
`print()` 仅用于调试。输出会写入服务器日志，不会显示给用户。
{% endhint %}

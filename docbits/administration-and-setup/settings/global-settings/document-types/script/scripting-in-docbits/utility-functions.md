# Utility Functions

Built-in functions for string processing, math, date operations, regex, and data types.

**Source:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## String Functions

### Type Conversion

```python
str(value)       # Convert to string
int(value)       # Convert to integer
float(value)     # Convert to float
str_to_bool(s)   # "true"/"1"/"yes" → True, everything else → False
```

### String Methods

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
These are available as standalone functions but can also be called as methods on strings:

```python
# Both work:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Fuzzy String Matching

### levenshtein\_distance()

Calculates the edit distance between two strings (number of changes needed).

```python
levenshtein_distance(s1, s2)
```

**Example:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Strings are similar enough
    pass
```

### jaro\_winkler\_similarity()

Calculates a similarity score between 0.0 and 1.0.

```python
jaro_winkler_similarity(s1, s2)
```

**Example:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (very similar, typo)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (dissimilar)
```

{% hint style="success" %}
**When to use which?**
- **Levenshtein**: Good for short strings, exact error count
- **Jaro-Winkler**: Better for names/addresses, weights matches at the beginning more heavily
{% endhint %}

---

## Regex Functions

Based on Python's `re` module, but available as standalone functions.

### re\_search()

Searches for the first occurrence of a pattern.

```python
re_search(pattern, string)
```

**Returns:** Match object or `None`

**Example — Extract order number from fulltext:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Replaces pattern matches with a replacement string.

```python
re_sub(pattern, replacement, string)
```

**Example — Remove special characters from invoice ID:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Finds all occurrences of a pattern.

```python
re_findall(pattern, string)
```

**Example — Find all PO numbers in document:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Date/Time Functions

### datetime\_today()

Returns today's date as a `datetime` object.

```python
today = datetime_today()
```

### datetime\_date

The `date` class for date creation.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Parses a date string into a datetime object.

```python
strptime(date_string, format)
```

**Example — Parse and use invoice date:**

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

Formats a datetime object as a string.

```python
strftime(datetime_obj, format)
```

**Example — Set processing date:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

Creates a date from ISO calendar week.

```python
fromisocalendar(year, week, day)
```

**Example — Convert calendar week to date:**

```python
# CW 12/2026, Monday
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Common with German customers:** Delivery dates are often specified as "KW 12". Pattern:

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

Returns the weekday of the 1st and number of days in a month.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Example:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Decimal/Locale Functions

### parse\_decimal()

Parses a string to a decimal number with locale detection.

```python
parse_decimal(value, locale="en_US")
```

**Example:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Formats a decimal number according to locale.

```python
format_decimal_to_locale(value, locale)
```

**Example:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Math Functions

The full `math` module is available:

| Function | Description |
| -------- | ----------- |
| `abs(x)` | Absolute value |
| `round(x, n)` | Round to n decimal places |
| `floor(x)` | Floor (round down) |
| `ceil(x)` | Ceiling (round up) |
| `sqrt(x)` | Square root |
| `pow(x, y)` | Power |
| `log(x)` / `log10(x)` | Logarithm |
| `pi` | π (3.14159...) |
| `e` | Euler's number (2.71828...) |
| `sin`, `cos`, `tan` | Trigonometry |
| `acos`, `asin`, `atan` | Inverse trigonometry |
| `degrees`, `radians` | Degrees ↔ Radians |
| `exp`, `fabs`, `fmod` | Additional math functions |
| `hypot`, `ldexp`, `frexp` | Special calculations |
| `modf` | Separate integer/decimal parts |

---

## Data Structure Functions

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
`print()` is only available for debugging purposes. Output goes to the server log, not to the user.
{% endhint %}

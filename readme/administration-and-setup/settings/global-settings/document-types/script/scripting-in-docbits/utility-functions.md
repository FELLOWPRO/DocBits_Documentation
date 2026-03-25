# Yardımcı Fonksiyonlar

String işleme, matematik, tarih işlemleri, regex ve veri türleri için yerleşik fonksiyonlar.

**Kaynak:** `module/script/helper/script_processor.py:get_allowed_functions_list()`

---

## String Fonksiyonları

### Tür Dönüştürme

```python
str(value)       # String'e dönüştür
int(value)       # Integer'a dönüştür
float(value)     # Float'a dönüştür
str_to_bool(s)   # "true"/"1"/"yes" → True, diğer her şey → False
```

### String Metotları

```python
lower(s)              # str.lower — "ABC" → "abc"
upper(s)              # str.upper — "abc" → "ABC"
split(s, sep)         # str.split — "a,b,c".split(",") → ["a","b","c"]
strip(s)              # str.strip — " abc " → "abc"
startswith(s, prefix) # str.startswith
endswith(s, suffix)   # str.endswith
```

{% hint style="info" %}
Bunlar bağımsız fonksiyonlar olarak mevcuttur ancak stringler üzerinde metot olarak da çağrılabilir:

```python
# Her ikisi de çalışır:
result = upper("hello")      # → "HELLO"
result = "hello".upper()     # → "HELLO"
```
{% endhint %}

---

## Bulanık String Eşleştirme

### levenshtein\_distance()

İki string arasındaki düzenleme mesafesini hesaplar (gereken değişiklik sayısı).

```python
levenshtein_distance(s1, s2)
```

**Örnek:**

```python
dist = levenshtein_distance("ACME Corp", "ACME Corporation")
# dist = 7
if dist < 5:
    # Stringler yeterince benzer
    pass
```

### jaro\_winkler\_similarity()

0.0 ile 1.0 arasında bir benzerlik puanı hesaplar.

```python
jaro_winkler_similarity(s1, s2)
```

**Örnek:**

```python
score = jaro_winkler_similarity("Invoice", "Invocie")
# score ≈ 0.96 (çok benzer, yazım hatası)

score = jaro_winkler_similarity("Invoice", "Receipt")
# score ≈ 0.45 (benzer değil)
```

{% hint style="success" %}
**Hangisini ne zaman kullanmalı?**
- **Levenshtein**: Kısa stringler için iyi, kesin hata sayısı
- **Jaro-Winkler**: İsimler/adresler için daha iyi, başlangıçtaki eşleşmelere daha fazla ağırlık verir
{% endhint %}

---

## Regex Fonksiyonları

Python'un `re` modülüne dayalıdır, ancak bağımsız fonksiyonlar olarak kullanılabilir.

### re\_search()

Bir kalıbın ilk eşleşmesini arar.

```python
re_search(pattern, string)
```

**Döndürür:** Match nesnesi veya `None`

**Örnek — Tam metinden sipariş numarası çıkarma:**

```python
content = get_document_content(document_data)
match = re_search(r"Order number:\s*(\d+)", content)
if match:
    po_number = match.group(1)
    set_field_value(document_data, "purchase_order", po_number)
```

### re\_sub()

Kalıp eşleşmelerini bir değiştirme stringi ile değiştirir.

```python
re_sub(pattern, replacement, string)
```

**Örnek — Fatura ID'sinden özel karakterleri kaldırma:**

```python
inv_id = get_field_value(document_data, "invoice_id", "")
cleaned = re_sub(r"[^A-Za-z0-9\-]", "", inv_id)
set_field_value(document_data, "invoice_id", cleaned)
```

### re\_findall()

Bir kalıbın tüm eşleşmelerini bulur.

```python
re_findall(pattern, string)
```

**Örnek — Belgedeki tüm SB numaralarını bulma:**

```python
content = get_document_content(document_data)
po_numbers = re_findall(r"PO[- ]?\d{6,}", content)
if po_numbers:
    set_field_value(document_data, "purchase_order", po_numbers[0])
```

---

## Tarih/Saat Fonksiyonları

### datetime\_today()

Bugünün tarihini `datetime` nesnesi olarak döndürür.

```python
today = datetime_today()
```

### datetime\_date

Tarih oluşturma için `date` sınıfı.

```python
d = datetime_date(2026, 3, 25)  # date(2026, 3, 25)
```

### strptime()

Bir tarih stringini datetime nesnesine dönüştürür.

```python
strptime(date_string, format)
```

**Örnek — Fatura tarihini ayrıştırma ve kullanma:**

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

Bir datetime nesnesini string olarak biçimlendirir.

```python
strftime(datetime_obj, format)
```

**Örnek — İşlem tarihi ayarlama:**

```python
today = datetime_today()
formatted = strftime(today, "%d.%m.%Y")  # "25.03.2026"
set_field_value(document_data, "processing_date", formatted)
```

### fromisocalendar()

ISO takvim haftasından tarih oluşturur.

```python
fromisocalendar(year, week, day)
```

**Örnek — Takvim haftasını tarihe dönüştürme:**

```python
# TH 12/2026, Pazartesi
d = fromisocalendar(2026, 12, 1)  # date(2026, 3, 16)
set_date_value(document_data, "delivery_date", str(d))
```

{% hint style="success" %}
**Alman müşterilerinde yaygın:** Teslimat tarihleri genellikle "KW 12" olarak belirtilir. Kalıp:

```python
content = get_document_content(document_data)
match = re_search(r"KW\s*(\d{1,2})[/\s]*(\d{4})", content)
if match:
    week = int(match.group(1))
    year = int(match.group(2))
    d = fromisocalendar(year, week, 1)  # TH'nın Pazartesisi
    set_date_value(document_data, "delivery_date", str(d))
```
{% endhint %}

### calendar\_monthrange()

Ayın 1'inin haftanın gününü ve aydaki gün sayısını döndürür.

```python
weekday_of_first, num_days = calendar_monthrange(year, month)
```

**Örnek:**

```python
_, days_in_month = calendar_monthrange(2026, 2)
# days_in_month = 28
```

---

## Ondalık/Yerel Ayar Fonksiyonları

### parse\_decimal()

Bir stringi yerel ayar algılama ile ondalık sayıya dönüştürür.

```python
parse_decimal(value, locale="en_US")
```

**Örnek:**

```python
amount = parse_decimal("1.234,56", "de_DE")  # → Decimal('1234.56')
amount = parse_decimal("1,234.56", "en_US")  # → Decimal('1234.56')
```

### format\_decimal\_to\_locale()

Bir ondalık sayıyı yerel ayara göre biçimlendirir.

```python
format_decimal_to_locale(value, locale)
```

**Örnek:**

```python
formatted = format_decimal_to_locale(1234.56, "de_DE")  # → "1.234,56"
formatted = format_decimal_to_locale(1234.56, "en_US")  # → "1,234.56"
```

---

## Matematik Fonksiyonları

Tam `math` modülü mevcuttur:

| Fonksiyon | Açıklama |
| -------- | ----------- |
| `abs(x)` | Mutlak değer |
| `round(x, n)` | n ondalık basamağa yuvarla |
| `floor(x)` | Aşağı yuvarla |
| `ceil(x)` | Yukarı yuvarla |
| `sqrt(x)` | Karekök |
| `pow(x, y)` | Üs alma |
| `log(x)` / `log10(x)` | Logaritma |
| `pi` | π (3.14159...) |
| `e` | Euler sayısı (2.71828...) |
| `sin`, `cos`, `tan` | Trigonometri |
| `acos`, `asin`, `atan` | Ters trigonometri |
| `degrees`, `radians` | Derece ↔ Radyan |
| `exp`, `fabs`, `fmod` | Ek matematik fonksiyonları |
| `hypot`, `ldexp`, `frexp` | Özel hesaplamalar |
| `modf` | Tam sayı/ondalık kısımları ayırma |

---

## Veri Yapısı Fonksiyonları

```python
dict()            # Yeni sözlük
list()            # Yeni liste
set()             # Yeni küme
tuple()           # Yeni demet
defaultdict(type) # collections.defaultdict

len(x)            # Uzunluk
isinstance(x, t)  # Tür kontrolü
type(x)           # Türü al
deepcopy(x)       # Derin kopya (copy.deepcopy)

print(x)          # Hata ayıklama çıktısı (yalnızca test için)
```

{% hint style="warning" %}
`print()` yalnızca hata ayıklama amacıyla kullanılabilir. Çıktı kullanıcıya değil, sunucu günlüğüne gider.
{% endhint %}

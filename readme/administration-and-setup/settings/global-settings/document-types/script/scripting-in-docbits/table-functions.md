# Tablo Fonksiyonları

Tabloları ve tablo satırlarını okuma, yazma ve işleme fonksiyonları.

**Kaynak:** `module/script/helper/document_table_script_functions.py`

---

## get\_column\_value()

Bir tablo satırından bir sütunun değerini okur.

```python
get_column_value(row, column_name, default_value=None, is_clean=False)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `row` | `dict` | `table["rows"]` içinden bir satır nesnesi |
| `column_name` | `str` | Sütun adı (büyük/küçük harf duyarsız) |
| `default_value` | `any` | Sütun boş/eksikse dönüş değeri |
| `is_clean` | `bool` | `True` ise: BÜYÜK HARF ve boşluklar kaldırılmış |

**Örnek — Tablo satırlarını yineleme:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
```

{% hint style="info" %}
Sütun adı karşılaştırması **büyük/küçük harf duyarsızdır**: `"DESCRIPTION"` aynı zamanda `"description"` veya `"Description"` ile de eşleşir.
{% endhint %}

---

## set\_column\_value()

Bir tablo satırındaki bir sütunun değerini ayarlar.

```python
set_column_value(row, column_name, value)
```

**Döndürür:** Değer değiştiyse `True`, aynıysa `False`

**Yan etkiler:**
- `extraction_method = "SCRIPT"` ayarlar
- Sütun mevcut değilse otomatik olarak oluşturur

**Örnek — Satır toplamlarını hesaplama:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        qty = get_column_value(row, "QUANTITY", "0")
        price = get_column_value(row, "UNIT_PRICE", "0")
        try:
            total = float(qty) * float(price)
            set_column_value(row, "LINE_TOTAL", str(total))
        except ValueError:
            pass
```

---

## set\_column\_date\_value()

Biçimlendirme ve tarih aritmetiği ile bir tablo hücresinde tarih değeri ayarlar.

```python
set_column_date_value(document_data, row, column_name, value,
                      add_days=0, skip_weekend=False, exclude_final_days=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `date_format_pattern` için gerekli |
| `row` | `dict` | Tablo satırı |
| `column_name` | `str` | Sütun adı |
| `value` | `str` | ISO tarih `"2026-03-25"` |
| `add_days` | `int` | Eklenecek gün sayısı |
| `skip_weekend` | `bool` | Hafta sonlarını atla |
| `exclude_final_days` | `str/list` | Hariç tutulacak günler |

**Örnek — Satır başına teslimat tarihleri hesaplama:**

```python
for row in table["rows"]:
    order_date = get_column_value(row, "ORDER_DATE")
    if order_date:
        set_column_date_value(document_data, row, "DELIVERY_DATE",
                              order_date, add_days=14, skip_weekend=True)
```

---

## set\_column\_amount\_value()

Yerel ayar biçimlendirmesi ile bir tablo hücresinde tutar değeri ayarlar.

```python
set_column_amount_value(document_data, row, column_name, value)
```

**Örnek — Satır toplamlarını hesaplama ve biçimlendirme:**

```python
for row in table["rows"]:
    qty = float(get_column_value(row, "QUANTITY", "0"))
    price = float(get_column_value(row, "UNIT_PRICE", "0"))
    set_column_amount_value(document_data, row, "LINE_TOTAL", qty * price)
```

{% hint style="info" %}
`value` ayarlanmadan önce otomatik olarak `str()` ile dönüştürülür.
{% endhint %}

---

## add\_table\_column()

Bir tablonun tüm satırlarına yeni bir sütun ekler.

```python
add_table_column(table, col_name, default_value=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `table` | `dict` | Tablo nesnesi (`tables_dict` değil!) |
| `col_name` | `str` | Yeni sütunun adı |
| `default_value` | `any` | Tüm satırlar için başlangıç değeri |

**Yan etkiler:**
- `is_extra_column = True` (orijinal olmayan olarak işaretlenir)
- `is_mapped = True`
- `extraction_method = "SCRIPT"`

**Örnek — Vergi kodu sütunu ekleme:**

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_CODE", "S1")

    # Şimdi satır başına değerleri ayarla
    for row in table["rows"]:
        amount = float(get_column_value(row, "LINE_TOTAL", "0"))
        if amount == 0:
            set_column_value(row, "TAX_CODE", "Z0")
```

{% hint style="warning" %}
**Tekrar koruma:** Sütun zaten mevcutsa (büyük/küçük harf duyarsız kontrol), tekrar **eklenmez**.
{% endhint %}

---

## remove\_rows\_from\_table()

Bir tablodan belirli sayıda satır kaldırır.

```python
remove_rows_from_table(document_data, table_name, count, start)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `table_name` | `str` | Tablonun adı |
| `count` | `int` | Kaldırılacak satır sayısı |
| `start` | `int` | Başlangıç indeksi (0 tabanlı) |

**Hata:** `start` veya `count` aralık dışındaysa `ValueError` fırlatır

**Örnek — Başlık satırlarını veya son satırı kaldırma:**

```python
# İlk 2 satırı kaldır (ör. başlık satırları)
remove_rows_from_table(document_data, "INVOICE_TABLE", 2, 0)

# Son satırı kaldır
table = tables_dict.get("INVOICE_TABLE")
if table:
    row_count = len(table["rows"])
    remove_rows_from_table(document_data, "INVOICE_TABLE", 1, row_count - 1)
```

---

## remove\_all\_rows\_except\_one\_from\_table()

Yalnızca belirli bir satırı tutar ve diğerlerini kaldırır.

```python
remove_all_rows_except_one_from_table(document_data, line_number)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `line_number` | `int` | Satır numarası (1 tabanlı!) |

{% hint style="warning" %}
`line_number=1` ilk satırı tutar. 0 tabanlı indekslerle karıştırmayın.
{% endhint %}

**Örnek:**

```python
# Yalnızca 3. satırı tut
remove_all_rows_except_one_from_table(document_data, 3)
```

---

## delete\_tables()

Belgedeki tüm tabloları siler (yedekle birlikte).

```python
delete_tables(document_data)
```

**Yan etkiler:**
- Tabloları `last_deleted_table` altında kaydeder
- `po_items`, `po_multi_matched`, `po_match_status`'u kaldırır

**Örnek:**

```python
# Tabloları sil (ör. satır öğesi olmayan maliyet faturaları için)
delete_tables(document_data)
```

---

## restore\_tables()

`delete_tables()` ile daha önce silinen tabloları geri yükler.

```python
restore_tables(document_data)
```

**Örnek:**

```python
restore_tables(document_data)
```

{% hint style="success" %}
**Silme + Geri Yükleme kalıbı:** Tabloları geçici olarak kaldırmak ve belirli koşullar altında geri yüklemek istediğinizde kullanışlıdır.
{% endhint %}

---

## Yaygın Kalıplar

### Sütun toplamı hesaplama

```python
table = tables_dict.get("INVOICE_TABLE")
total = 0
if table:
    for row in table["rows"]:
        val = get_column_value(row, "LINE_TOTAL", "0")
        try:
            total += float(val)
        except ValueError:
            pass
    set_field_value(document_data, "calculated_total", str(round(total, 2)))
```

### Boş satırları filtreleme

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    empty_indices = []
    for i, row in enumerate(table["rows"]):
        desc = get_column_value(row, "DESCRIPTION", "")
        if not desc.strip():
            empty_indices.append(i)

    # Arkadan öne doğru kaldır
    for idx in reversed(empty_indices):
        remove_rows_from_table(document_data, "INVOICE_TABLE", 1, idx)
```

### Diğer sütunlardan sütun hesaplama

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    add_table_column(table, "TAX_AMOUNT", "0")
    for row in table["rows"]:
        net = float(get_column_value(row, "NET_AMOUNT", "0"))
        tax_rate = float(get_column_value(row, "TAX_RATE", "0"))
        tax = net * tax_rate / 100
        set_column_amount_value(document_data, row, "TAX_AMOUNT", tax)
```

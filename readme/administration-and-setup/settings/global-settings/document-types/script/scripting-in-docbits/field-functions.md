# Alan Fonksiyonları

Belge alanlarını okuma, yazma ve kontrol etme fonksiyonları.

**Kaynak:** `module/script/helper/document_script_functions.py`

---

## get\_field\_value()

Belgeden bir alanın değerini okur.

```python
get_field_value(document_data, field_name, default_value=None, is_clean=False)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `document_data` bağlam nesnesi |
| `field_name` | `str` | Alanın adı (ör. `"invoice_id"`) |
| `default_value` | `any` | Alan boş/eksikse dönüş değeri (varsayılan: `None`) |
| `is_clean` | `bool` | `True` ise: değer BÜYÜK HARFE dönüştürülür ve boşluklar kaldırılır |

**Döndürür:** Alan değerini string olarak veya `default_value`

**Örnek — Yedek değerle fatura numarası okuma:**

```python
# Varsayılan değerle alan okuma
inv_id = get_field_value(document_data, "invoice_id", "UNKNOWN")

# is_clean=True ile: "INV 001" "INV001" olur
inv_id = get_field_value(document_data, "invoice_id", "", is_clean=True)
```

**Ne olur:** Alan değerini döndürür. `is_clean=True` olduğunda, değer `value.upper().replace(" ", "").strip()` ile dönüştürülür — karşılaştırmalar için kullanışlıdır.

---

## set\_field\_value()

Bir alanın değerini ayarlar. Alan mevcut değilse otomatik olarak oluşturur.

```python
set_field_value(document_data, field_name, value, remove_link=False)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `document_data` | `dict` | `document_data` bağlam nesnesi |
| `field_name` | `str` | Alanın adı |
| `value` | `any` | Yeni değer |
| `remove_link` | `bool` | `True` ise: koordinatları, güven düzeyini, kuralı vb. kaldırır |

**Döndürür:** Değer değiştiyse `True`, aynıysa `False`

**Yan etkiler:**
- `highlight_field = True` ayarlar (UI'da görsel gösterge)
- `extraction_method = "SCRIPT"` ayarlar
- `formatted_value = value` ayarlar

**Örnek — Koşullu değer atama:**

```python
# Fatura ID'si ayarlama
set_field_value(document_data, "invoice_id", "INV-2026-001")

# remove_link ile: OCR bağlantısını kaldırır (koordinatlar, güven düzeyi vb.)
set_field_value(document_data, "custom_field", "Calculated", remove_link=True)
```

**Ne olur:** Alan değeri güncellenir ve script tarafından değiştirilmiş olarak işaretlenir. Alan mevcut değilse, `extraction_method: "SCRIPT"` ile otomatik olarak oluşturulur ve hem `fields` hem de `fields_dict`'e eklenir.

---

## set\_date\_value()

Otomatik biçimlendirme ve isteğe bağlı tarih aritmetiği ile bir tarih değeri ayarlar.

```python
set_date_value(document_data, field_name, value, add_days=0, skip_weekend=False,
               remove_link=False, exclude_final_days=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `value` | `str` | ISO tarih: `"2026-03-25"`. Boşsa: bugünün tarihi |
| `add_days` | `int` | Eklenecek gün sayısı (ör. ödeme koşulları için `30`) |
| `skip_weekend` | `bool` | Gün eklerken hafta sonlarını atla |
| `exclude_final_days` | `str/list` | Hariç tutulacak ek günler (ör. `"MONDAY,FRIDAY"`) |

**Örnek — Ödeme vadesini hesaplama (30 gün, hafta sonları hariç):**

```python
# Vade tarihi: fatura tarihinden 30 gün sonra, hafta sonlarını atla
inv_date = get_field_value(document_data, "invoice_date")
set_date_value(document_data, "due_date", inv_date,
               add_days=30, skip_weekend=True)

# Teslimat tarihini bugün olarak ayarla
set_date_value(document_data, "delivery_date", None)  # None = bugün

# 14 gün, Cumartesi ve Pazartesi hariç
set_date_value(document_data, "delivery_date", "2026-04-01",
               add_days=14, skip_weekend=True, exclude_final_days="MONDAY")
```

**Ne olur:** Tarih, günler eklenerek (isteğe bağlı olarak hafta sonları/belirli günler atlanarak) hesaplanır ve belgenin `date_format_pattern`'ine göre otomatik olarak biçimlendirilir (ör. Almanya için `%d.%m.%Y`).

**`exclude_final_days` için gün kodları:**
`MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, `SUNDAY`

---

## set\_amount\_value()

Otomatik yerel ayar biçimlendirmesi ile bir tutar değeri ayarlar.

```python
set_amount_value(document_data, field_name, value, remove_link=False)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `value` | `str/number` | İngilizce formatta tutar (ör. `"1234.56"`) |

**Örnek — Net tutarı ayarlama:**

```python
set_amount_value(document_data, "net_amount", "1234.56")
# formatted_value ör. de_DE yerel ayarı için "1.234,56" olur
```

**Ne olur:** Tutar, `document_json`'daki `amount_format_locale`'a göre biçimlendirilir (ör. `de_DE`, `en_US`).

---

## create\_new\_field()

Yeni bir alan sözlüğü oluşturur (belgeye eklemeden).

```python
create_new_field(field_name, value="")
```

**Döndürür:** `name`, `value`, `formatted_value`, `extraction_method: "SCRIPT"` içeren Dict

**Örnek:**

```python
new_field = create_new_field("custom_reference", "REF-001")
document_json["fields"].append(new_field)
fields_dict["custom_reference"] = new_field
```

{% hint style="success" %}
**Daha basit alternatif:** Bunun yerine `set_field_value()` kullanın — alan mevcut değilse otomatik olarak oluşturur. `create_new_field()` yalnızca alan sözlüğünü manuel olarak değiştirmek istediğinizde gereklidir.
{% endhint %}

---

## delete\_field()

Belgeden bir alanı kaldırır.

```python
delete_field(document_data, field_name)
```

**Döndürür:** Silme işleminden sonra `(doc_json, fields_dict)` Tuple'ı

**Örnek:**

```python
delete_field(document_data, "unnecessary_field")
```

---

## set\_field\_as\_invalid()

Bir alanı hata mesajıyla geçersiz olarak işaretler.

```python
set_field_as_invalid(document_data, field_name, message, code=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `message` | `str` | Hata mesajı (UI'da görüntülenir) |
| `code` | `str` | Hata kodu (varsayılan: `INVALID_VALUE`) |

**Yan etkiler:**
- `is_valid = False`
- `invalidated_by_script = True`
- `highlight_field = True`
- `validation_message = message`
- `validation_code = code`

**Örnek — IBAN doğrulama:**

```python
iban = get_field_value(document_data, "iban", "")
if len(iban) < 15:
    set_field_as_invalid(document_data, "iban",
                         "IBAN en az 15 karakter olmalıdır",
                         "IBAN_TOO_SHORT")
```

**Ne olur:** Alan, doğrulama ekranında kırmızıyla vurgulanır ve kullanıcıya hata mesajı görüntülenir.

---

## set\_field\_as\_valid()

Bir alandan geçersiz durumu kaldırır.

```python
set_field_as_valid(document_data, field_name, message, code=None)
```

**Örnek:**

```python
set_field_as_valid(document_data, "iban", "IBAN geçerli")
```

**Ne olur:** `invalidated_by_script`, `validation_message`, `validation_code`'u kaldırır ve `is_valid = True` olarak ayarlar.

---

## set\_field\_attribute()

Bir alanda rastgele bir öznitelik ayarlar.

```python
set_field_attribute(document_data, field_name, attribute_name, value)
```

**Örnek:**

```python
set_field_attribute(document_data, "invoice_id", "highlight_field", True)
set_field_attribute(document_data, "supplier_name", "custom_flag", "reviewed")
```

Aşağıdaki [Desteklenen Öznitelikler](#desteklenen-öznitelikler) listesinin tamamına bakın.

---

## set\_is\_required()

Bir alanı zorunlu yapar veya zorunluluğu kaldırır.

```python
set_is_required(document_data, field_name, value)
```

**Örnek — Satınalma faturaları için SB numarası zorunlu:**

```python
doc_type_detail = get_field_value(document_data, "document_type_detail", "")
if doc_type_detail == "PURCHASE_INVOICE":
    set_is_required(document_data, "purchase_order", True)
else:
    set_is_required(document_data, "purchase_order", False)
```

---

## set\_is\_readonly()

Bir alanı salt okunur veya düzenlenebilir yapar.

```python
set_is_readonly(document_data, field_name, value)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `value` | `bool/None` | `True` = salt okunur, `False` = düzenlenebilir, `None` = özniteliği kaldır |

**Örnek:**

```python
set_is_readonly(document_data, "total_amount", True)
```

---

## set\_is\_hidden()

UI'da bir alanı gizler veya gösterir.

```python
set_is_hidden(document_data, field_name, value)
```

**Örnek — Alt organizasyon alanlarını yalnızca ilgili olduğunda göster:**

```python
if not document_json.get("sub_org_id"):
    set_is_hidden(document_data, "sub_org_reference", True)
```

---

## set\_force\_validation()

Bir alan için manuel doğrulamayı zorlar.

```python
set_force_validation(document_data, field_name, value, reset_validation=False)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `value` | `bool` | `True` = doğrulamayı zorla, `False` = kaldır |
| `reset_validation` | `bool` | `True` ise: `is_validated`'i `False`'a sıfırlar |

**`value=True` olduğunda yan etkiler:**
- `force_validation = True`
- `is_valid = False` (henüz doğrulanmadıysa)
- `validation_code = "FORCED_VALIDATION"`

**Örnek — Yüksek tutarlar için doğrulamayı zorla:**

```python
amount = get_field_value(document_data, "total_amount", "0")
try:
    if float(amount) > 10000:
        set_force_validation(document_data, "total_amount", True)
except ValueError:
    pass
```

---

## Desteklenen Öznitelikler

### Temel Alan Öznitelikleri

| Öznitelik | Tür | Açıklama |
| --------- | ---- | ----------- |
| `value` | any | Ham alan değeri |
| `formatted_value` | string | Görüntüleme için biçimlendirilmiş değer |
| `content` | string | Orijinal çıkarılmış içerik |
| `is_required` | bool | Alanın zorunlu olup olmadığı |
| `is_valid` | bool | Doğrulama durumu |
| `is_validated` | bool | Alanın kullanıcı tarafından doğrulanıp doğrulanmadığı |
| `is_readonly` | bool | Alanın salt okunur olup olmadığı |
| `is_hidden` | bool | Alanın UI'da gizli olup olmadığı |
| `force_validation` | bool | Kullanıcıyı bu alanı doğrulamaya zorla |
| `highlight_field` | bool | Alanı UI'da vurgula |
| `extraction_method` | string | Değerin nasıl çıkarıldığı (ör. `"SCRIPT"`) |

### Doğrulama Öznitelikleri

| Öznitelik | Tür | Açıklama |
| --------- | ---- | ----------- |
| `validation_message` | string | Kullanıcıya gösterilen hata mesajı |
| `validation_code` | string | Hata kodu (ör. `"FORCED_VALIDATION"`, `"INVALID_VALUE"`) |
| `invalidated_by_script` | bool | Alanı script tarafından geçersiz kılınmış olarak işaretler |

### Çıkarma/OCR Öznitelikleri

| Öznitelik | Tür | Açıklama |
| --------- | ---- | ----------- |
| `coords` | object | Belgedeki sınırlayıcı kutu koordinatları |
| `confidence` | float | OCR/çıkarma güven puanı |
| `score` | float | Eşleşme/doğrulama puanı |
| `score_description` | string | Puanın açıklaması |
| `page` | int | Alanın bulunduğu sayfa numarası |
| `rule` | string | Uygulanan çıkarma kuralı |

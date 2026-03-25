# İş Mantığı Fonksiyonları

Aramalar, SB eşleştirme, görevler, kullanıcı/grup yönetimi ve durum değişiklikleri için fonksiyonlar.

**Kaynak:** `module/script/helper/document_script_functions.py`

---

## get\_lookup\_records()

Arama tablolarından ana veri sorgular (tedarikçiler, kalemler, muhasebe hesapları vb.).

```python
get_lookup_records(org_id, sub_org_id, lookup_name, filters, **kwargs)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organizasyon UUID'si |
| `sub_org_id` | `str/None` | Alt organizasyon UUID'si (veya `None`) |
| `lookup_name` | `str` | Aramanın adı (ör. `"supplier"`, `"item"`, `"gl_account"`) |
| `filters` | `list` | Filtre koşulları (aşağıdaki formatlar) |
| `skip` | `int` | Sayfalama için offset (varsayılan: 0) |
| `limit` | `int` | Maks sonuç (varsayılan: 100) |
| `match_all` | `bool` | `True` = VE, `False` = VEYA (varsayılan: `True`) |
| `sort_order` | `list` | Sıralama (isteğe bağlı) |

### Filtre Formatları

Üç format desteklenir:

```python
# Format 1: field/operator/value içeren Dict
filters = [
    {"field": "VENDOR_ID", "operator": "exact", "value": "V001"},
    {"field": "NAME", "operator": "contains", "value": "ACME"},
]

# Format 2: 2 elemanlı Tuple/Liste (field, value) → operator = "exact"
filters = [
    ["VENDOR_ID", "V001"],
    ["CITY", "Munich"],
]

# Format 3: 3 elemanlı Tuple/Liste (field, operator, value)
filters = [
    ["VENDOR_ID", "exact", "V001"],
    ["NAME", "contains", "ACME"],
]
```

### Sıralama

```python
# Format 1: Dict
sort_order = [{"field": "NAME", "direction": "asc"}]

# Format 2: Tuple/Liste
sort_order = [["NAME", "asc"], ["VENDOR_ID", "desc"]]
```

**Örnek — Tedarikçi numarasına göre tedarikçi arama:**

```python
# Tedarikçi numarasına göre tedarikçi bulma
supplier_id = get_field_value(document_data, "supplier_id", "")
records = get_lookup_records(
    org_id, None, "supplier",
    [["VENDOR_ID", supplier_id]],
)
if records:
    supplier = records[0]
    set_field_value(document_data, "supplier_name", supplier.get("NAME", ""))
```

**Örnek — Birden fazla filtre ile muhasebe hesapları arama:**

```python
records = get_lookup_records(
    org_id, document_json.get("sub_org_id"), "gl_account",
    [
        {"field": "ACCOUNT_TYPE", "operator": "exact", "value": "EXPENSE"},
        {"field": "IS_ACTIVE", "operator": "exact", "value": "true"},
    ],
    limit=50,
    sort_order=[["ACCOUNT_NUMBER", "asc"]],
)
```

{% hint style="info" %}
Dahili olarak bulanık eşleştirmeyi destekleyen `search_operator="SMART"` kullanır.
{% endhint %}

---

## is\_supplier\_valid()

Tedarikçinin arama verilerinde mevcut olup olmadığını kontrol eder.

```python
is_supplier_valid(user, filter_data_json, sub_org_id=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | `user` bağlam nesnesi |
| `filter_data_json` | `dict` | `{"match_all": True, "filters": [...]}` formatında filtre |
| `sub_org_id` | `str/None` | Alt organizasyon |

**Döndürür:** En az 1 eşleşme varsa `True`, aksi halde `False`

**Örnek — Tedarikçi doğrulama:**

```python
supplier_id = get_field_value(document_data, "supplier_id", "")
is_valid = is_supplier_valid(user, {
    "match_all": True,
    "filters": [{"field": "VENDOR_ID", "operator": "exact", "value": supplier_id}]
})
if not is_valid:
    set_field_as_invalid(document_data, "supplier_id", "Tedarikçi ana verilerde bulunamadı")
```

---

## auto\_po\_match\_for\_purchase\_orders()

po-match-service mikroservisi aracılığıyla otomatik SB eşleştirmeyi tetikler.

```python
auto_po_match_for_purchase_orders(user, document_data, po_numbers)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Gerçek bir kullanıcı nesnesi olmalıdır |
| `document_data` | `dict` | Belge bağlamı |
| `po_numbers` | `str/list` | SB numaraları (virgülle ayrılmış veya liste) |

**Döndürür:** `po_items`, `po_match_status`, `po_multi_matched` ile güncellenmiş `document_data`

**Örnek — Otomatik SB eşleştirme:**

```python
po_nr = get_field_value(document_data, "purchase_order", "")
if po_nr:
    auto_po_match_for_purchase_orders(user, document_data, po_nr)
```

{% hint style="warning" %}
**Tekrar koruma:** Zaten doğrulanmış SB numaraları `already_verified_po_numbers` içinde saklanır ve tekrar eşleştirilmez.
{% endhint %}

---

## get\_next\_sequence\_number()

Veritabanında bir sıra numarası alır ve atomik olarak artırır.

```python
get_next_sequence_number(org_id, sequence_name, default_value=1)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organizasyon UUID'si |
| `sequence_name` | `str` | `"sequence"` içermeli (ör. `"invoice_sequence"`) |
| `default_value` | `int` | Sıra yeni oluşturulduğunda başlangıç değeri |

**Döndürür:** `int` — sonraki numara veya ad geçersizse `None`

**Örnek — Dahili belge numarası oluşturma:**

```python
seq_nr = get_next_sequence_number(org_id, "invoice_sequence", 1000)
set_field_value(document_data, "internal_number", str(seq_nr))
```

{% hint style="danger" %}
**Adlandırma kuralı:** `sequence_name` "sequence" ile başlamalı veya bitmeli ya da "SEQUENCE\_" içermelidir. Aksi takdirde fonksiyon `None` döndürür.
{% endhint %}

---

## create\_document\_task()

Mevcut belge için bir görev oluşturur.

```python
create_document_task(user, document_data, title, description, priority,
                     assigned_to_user_id, assigned_to_group_id, send_email)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `user` | `UserAuthentication` | Kullanıcı bağlamı |
| `title` | `str` | Görev başlığı |
| `description` | `str` | Açıklama |
| `priority` | `str/int` | Öncelik |
| `assigned_to_user_id` | `str/None` | Atanan kullanıcı |
| `assigned_to_group_id` | `str/None` | Atanan grup |
| `send_email` | `bool` | E-posta bildirimi gönder |

**Örnek — Yüksek tutarlı faturalar için görev oluşturma:**

```python
amount = float(get_field_value(document_data, "total_amount", "0"))
if amount > 50000:
    create_document_task(
        user, document_data,
        title="Yüksek fatura tutarı - inceleme gerekli",
        description=f"Fatura tutarı: {amount} 50.000 eşiğini aşıyor",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id="uuid-of-finance-group",
        send_email=True
    )
```

---

## set\_document\_sub\_org\_id()

Bir belgeye alt organizasyon atar.

```python
set_document_sub_org_id(document_data, sub_org_id)
```

**Yan etkiler:**
- `document_json` içinde `sub_org_id` ayarlar
- Doğrudan veritabanına kaydeder (`doc_id` mevcutsa)

**Örnek — Tedarikçiye göre yönlendirme:**

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
sub_org_map = {
    "ACMECORP": "uuid-acme-sub-org",
    "WIDGETSINC": "uuid-widgets-sub-org",
}
for key, sub_org in sub_org_map.items():
    if key in supplier:
        set_document_sub_org_id(document_data, sub_org)
        break
```

---

## update\_document\_status\_with\_doc\_id()

Bir belgenin durumunu değiştirir.

```python
update_document_status_with_doc_id(doc_id, user, org_id, status, message=None,
                                    doc_classification_class=None)
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `doc_id` | `str` | Belge UUID'si |
| `status` | `str` | Yeni durum (ör. `"error"`, `"ready_for_validation"`) |
| `message` | `str/None` | Durum mesajı |
| `doc_classification_class` | `str/None` | `CLASSIFIED` durumu için: yeni belge türü |

**Örnek — Belgeyi hata durumuna ayarlama:**

```python
doc_id = document_json["doc_id"]
update_document_status_with_doc_id(
    doc_id, user, org_id, "error",
    message="Zorunlu alan eksik: tedarikçi numarası"
)
```

{% hint style="warning" %}
**Dikkat:** Durum değişiklikleri sonraki işlemleri tetikler (DocFlow iş akışları, durum değişikliği kancaları). Yalnızca gerekli olduğunda kullanın.
{% endhint %}

---

## get\_document\_content()

Belgenin tam OCR metnini döndürür.

```python
get_document_content(document_data)
```

**Döndürür:** `str` — Tüm sayfaların birleştirilmiş metni

**Örnek — Tam metinde anahtar kelime arama:**

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")

# Tam metinde regex arama
match = re_search(r"Order number:\s*(\S+)", content)
if match:
    set_field_value(document_data, "purchase_order", match.group(1))
```

{% hint style="info" %}
Sonuç 60 saniye süreyle önbelleğe alınır (maks 128 girişli TTL önbellek).
{% endhint %}

---

## get\_user\_by\_id() / get\_user\_by\_email()

Bir kullanıcıyı ID veya e-posta ile arar.

```python
get_user_by_id(user_id)
get_user_by_email(email)
```

**Döndürür:** `.email`, `.first_name`, `.last_name`, `.user_id` gibi özniteliklere sahip `UsersCache` nesnesi

**Örnek — Belirli bir kullanıcıya görev atama:**

```python
user_obj = get_user_by_email("manager@company.com")
if user_obj:
    create_document_task(user, document_data,
        title="İnceleme gerekli",
        description="...",
        priority="MEDIUM",
        assigned_to_user_id=str(user_obj.user_id),
        assigned_to_group_id=None,
        send_email=True)
```

---

## get\_group\_by\_id() / get\_group\_by\_name()

Bir kullanıcı grubunu ID veya ada göre arar.

```python
get_group_by_id(group_id)
get_group_by_name(org_id, group_name)
```

**Döndürür:** `GroupCache` nesnesi

**Örnek — Görev ataması için grup bulma:**

```python
finance_group = get_group_by_name(org_id, "Finance")
if finance_group:
    create_document_task(user, document_data,
        title="Onay gerekli",
        description="...",
        priority="HIGH",
        assigned_to_user_id=None,
        assigned_to_group_id=str(finance_group.id),
        send_email=True)
```

---

## compare\_values()

Tür dönüştürmesi ile akıllı değer karşılaştırması.

```python
compare_values(value1, value2)
```

**Karşılaştırma mantığı:**
1. `None == None` → `True`
2. `None != non-None` → `False`
3. Sayı olan stringler → sayısal karşılaştırma (`"1.0" == "1.00"` → `True`)
4. Stringler → büyük/küçük harf duyarsız, boşluk duyarsız (`"ABC " == " abc"` → `True`)
5. Bool vs String → string karşılaştırması (`True == "true"` → `True`)
6. Yedek olarak Decimal karşılaştırması

**Örnek — Tutarların eşleşip eşleşmediğini doğrulama:**

```python
if compare_values(get_field_value(document_data, "net_amount"),
                  get_field_value(document_data, "calculated_net")):
    set_field_as_valid(document_data, "net_amount", "Tutarlar eşleşiyor")
```

---

## get\_lov\_values()

Değer Listesi (LOV) girişlerini getirir.

```python
get_lov_values(org_id, key, return_type="list_of_objects", sub_org_id=None, language_code="")
```

**Parametreler:**

| Ad | Tür | Açıklama |
| ---- | ---- | ----------- |
| `org_id` | `str` | Organizasyon UUID'si |
| `key` | `str` | LOV anahtarı |
| `return_type` | `str` | `"list_of_objects"` veya `"list_of_values"` |
| `sub_org_id` | `str/None` | İsteğe bağlı alt organizasyon filtresi |
| `language_code` | `str` | Dil kodu (ör. `"en"`, `"de"`) |

**Döndürür:** LOV değerlerini nesne listesi veya düz liste olarak.

**Örnek — Yapılandırılmış vergi kodlarını getirme:**

```python
tax_codes = get_lov_values(org_id, "tax_codes", return_type="list_of_values")
```

# Bağlam Değişkenleri

Her script, yürütme bağlamında otomatik olarak aşağıdaki değişkenleri alır. Bunların içe aktarılmasına gerek **yoktur** — doğrudan kullanılabilirler.

---

## Ana Değişkenler

### `document_data` (takma ad: `doc`)

Tüm belge verilerini içeren kök nesne:

```python
document_data = {
    "document_json": { ... },   # Belgenin kendisi
    "fields": [ ... ],          # Tüm alanların dizisi
    "fields_dict": { ... },     # Ada göre dizinlenmiş alanlar
    "tables": [ ... ],          # Tüm tabloların dizisi
    "tables_dict": { ... },     # Ada göre dizinlenmiş tablolar
}
```

{% hint style="info" %}
`doc` bir takma addır — `doc` ve `document_data` aynı nesneyi işaret eder. Her ikisi de birbirinin yerine kullanılabilir.
{% endhint %}

### `document_json`

`document_data["document_json"]`'a doğrudan erişim. İçerir:

```python
document_json = {
    "doc_id": "uuid-...",
    "org_id": "uuid-...",
    "sub_org_id": "uuid-..." or None,
    "doc_type": "INVOICE",
    "sub_doc_type": None,
    "status": "ready_for_validation",
    "date_format_pattern": "%d.%m.%Y",      # Tarih biçimlendirme için
    "amount_format_locale": "de_DE",         # Tutar biçimlendirme için
    "fields": [ ... ],                        # Alan dizisi
    "tables": [ ... ],                        # Tablo dizisi
    "po_items": [ ... ],                      # SB eşleştirme sonuçları
    "po_match_status": "matched" | None,
    "already_verified_po_numbers": [ ... ],
}
```

### `fields` ve `fields_dict`

```python
# fields = Tüm alanların dizisi
fields = [
    {
        "name": "invoice_id",
        "value": "INV-2026-001",
        "formatted_value": "INV-2026-001",
        "content": "INV-2026-001",           # Ham OCR değeri
        "confidence": 0.95,
        "extraction_method": "AI",            # veya "SCRIPT", "MANUAL"
        "is_valid": True,
        "is_validated": False,
        "is_required": True,
        "is_readonly": False,
        "is_hidden": False,
        "force_validation": False,
        "highlight_field": False,
        "validation_message": None,
        "validation_code": None,
        "coords": { ... },                    # Belgedeki sınırlayıcı kutu
        "page": 1,
    },
    ...
]

# fields_dict = Ada göre dizinlenmiş
fields_dict = {
    "invoice_id": { ... },      # fields[] içindeki nesnelerle aynı
    "invoice_date": { ... },
    "net_amount": { ... },
    "tax_amount": { ... },
    "total_amount": { ... },
    "supplier_name": { ... },
    "purchase_order": { ... },
    "currency": { ... },
    ...
}
```

{% hint style="danger" %}
**`set_field_value` ile otomatik oluşturma:** `set_field_value()` kullanılırken bir alan mevcut değilse, **otomatik olarak oluşturulur** ve hem `fields` hem de `fields_dict`'e eklenir.
{% endhint %}

### `tables` ve `tables_dict`

```python
# tables = Tüm tabloların dizisi
tables = [
    {
        "name": "INVOICE_TABLE",
        "rows": [
            {
                "columns": [
                    {
                        "name": "DESCRIPTION",
                        "value": "Widget A",
                        "formatted_value": "Widget A",
                        "content": "Widget A",
                        "is_validated": False,
                        "is_mapped": True,
                        "extraction_method": "AI",
                        "location": [ ... ],
                    },
                    {
                        "name": "QUANTITY",
                        "value": "10",
                        ...
                    },
                    {
                        "name": "UNIT_PRICE",
                        "value": "25.00",
                        ...
                    },
                    {
                        "name": "LINE_TOTAL",
                        "value": "250.00",
                        ...
                    },
                ],
            },
            ...  # Daha fazla satır
        ],
    },
]

# tables_dict = Tablo adına göre dizinlenmiş
tables_dict = {
    "INVOICE_TABLE": { ... },   # tables[] içindeki nesnelerle aynı
}
```

### `user_id`, `org_id`, `user`

```python
user_id    # Integer — Mevcut kullanıcının ID'si
org_id     # String (UUID) — Belgenin organizasyonu
user       # UserAuthentication nesnesi — is_supplier_valid() gibi API çağrıları için
```

{% hint style="warning" %}
**`user` her zaman tam olarak mevcut değildir:** Celery worker bağlamında (otomatik işleme) `user` sınırlı özelliklere sahiptir. UI bağlamında (`ON_FIELD_CHANGE`, `ON_SAVE`) tam kullanıcı nesnesidir.
{% endhint %}

---

## Yaygın Erişim Kalıpları

### Alanları okuma ve yazma

```python
# Önerilen: yardımcı fonksiyonlar aracılığıyla
inv_nr = get_field_value(document_data, "invoice_id")
set_field_value(document_data, "invoice_id", inv_nr.strip())

# Alternatif: doğrudan fields_dict üzerinden
inv_field = fields_dict.get("invoice_id")
if inv_field:
    raw_value = inv_field["value"]
```

### Tabloları yineleme

```python
table = tables_dict.get("INVOICE_TABLE")
if table:
    for row in table["rows"]:
        desc = get_column_value(row, "DESCRIPTION", "")
        qty = get_column_value(row, "QUANTITY", "0")
        set_column_value(row, "TOTAL", str(float(qty) * float(price)))
```

### Belgede tam metin arama

```python
content = get_document_content(document_data)
if "REVERSE CHARGE" in content.upper():
    set_field_value(document_data, "tax_code", "RC")
```

### Alt organizasyon yönlendirmesi

```python
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)
if "ACME" in supplier:
    set_document_sub_org_id(document_data, "uuid-of-acme-sub-org")
```

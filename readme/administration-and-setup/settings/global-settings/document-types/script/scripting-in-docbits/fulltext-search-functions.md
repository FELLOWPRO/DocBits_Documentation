# Fulltext ve Vektör Arama Fonksiyonları

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir**

Bu fonksiyonlar, kuruluşunuz için **OPENSEARCH\_ENABLED** lisansının/tercihinin etkinleştirilmesini gerektirir. Etkinleştirilmeden tüm fonksiyonlar `RuntimeError("Fulltext search license is missing")` hatası fırlatır.
{% endhint %}

Belge arşivlerini aramak, benzer belgeleri bulmak ve ERP ana verilerini sorgulamak için fonksiyonlar. Bunlar kuruluşun **tüm belgelerini** arar — yalnızca mevcut belgenin metnini okuyan `get_document_content()` fonksiyonundan farklı olarak.

{% hint style="success" %}
**Security:** The `org_id` is automatically injected by the script sandbox. You never need to pass it — your scripts always operate within your own organization's data.
{% endhint %}

**Kaynak:** `module/script/helper/document_script_functions.py`

---

## fulltext\_search()

Kuruluştaki **tüm belgelerin** tam OCR metnini arar. `pages.pageText`, `tfidfCustomPageText` ve `ai_text` alanlarında fulltextsearch mikroservisi aracılığıyla metin bulur.

```python
fulltext_search(query, **kwargs)
```

**Parametreler:**

| Ad | Tip | Varsayılan | Açıklama |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | zorunlu | Arama terimi (tüm belgelerin OCR metninde aranır) |
| `search_type` | `str` | `"match_phrase"` | `"match_phrase"` (tam ifade), `"fuzzy"` (hata toleranslı, 2 karakter farkına kadar), `"prefix"` (ile başlayan) |
| `doc_type` | `str` | `None` | Belge türüne göre filtrele (virgülle ayrılmış, ör. `"INVOICE,CREDIT_NOTE"`) |
| `status` | `str` | `None` | Belge durumuna göre filtrele (virgülle ayrılmış, ör. `"ready_for_validation,exported"`) |
| `vendor_name` | `str` | `None` | Tedarikçi adına göre filtrele |
| `date_range` | `str` | `None` | `"last_30_days"`, `"last_90_days"`, `"last_180_days"`, `"last_365_days"` |
| `size` | `int` | `10` | Maksimum sonuç (50 ile sınırlı) |

**Döndürür:** `list[dict]` — Her dict şunları içerir:

| Alan | Açıklama |
| ----- | ----------- |
| `doc_id` | Belge UUID'si |
| `name` | Dosya adı (ör. `"INV-2026-001.pdf"`) |
| `doc_type` | Belge türü (`"INVOICE"`, `"ORDER_CONFIRMATION"`, vb.) |
| `vendor_name` | Tedarikçi adı |
| `status` | Belge durumu |
| `total_amount` | Toplam tutar |
| `ocr_content` | Belgeden eşleşen metin alıntısı |
| `highlights` | Alan başına vurgulanan eşleşmeleri içeren dict |

**Örnek — Tam ifade arama:**

```python
results = fulltext_search("REVERSE CHARGE",
                          doc_type="INVOICE", size=10)
for doc in results:
    print(doc["name"], doc["ocr_content"])
```

**Örnek — Bulanık arama (OCR hatalarına toleranslı):**

```python
# "REVERS CHARG" gibi OCR hatalarında bile "REVERSE CHARGE" bulur
results = fulltext_search("REVERSE CHARGE",
                          search_type="fuzzy",
                          vendor_name="ACME Corp")
```

**Örnek — Önek araması:**

```python
# "Rechn" ile başlayan kelimeleri içeren tüm belgeleri bulur
results = fulltext_search("Rechn", search_type="prefix",
                          date_range="last_90_days")
```

{% hint style="warning" %}
**Boş sorgu:** Boş bir dize geçmek, HTTP çağrısı yapmadan hemen `[]` döndürür.
{% endhint %}

{% hint style="info" %}
**Hata yönetimi:** Fulltextsearch servisi erişilemez durumdaysa, fonksiyon `[]` döndürür ve bir uyarı kaydeder. Bir istisna **fırlatmaz**.
{% endhint %}

---

## vector\_search()

Vektör gömmeleri kullanarak anlamsal olarak benzer belgeleri bulur (384 boyutlu vektörlerle k-NN araması). Tam ifadeden bağımsız olarak benzer içeriğe sahip belgeleri bulmak için kullanışlıdır.

```python
vector_search(doc_id, **kwargs)
```

**Parametreler:**

| Ad | Tip | Varsayılan | Açıklama |
| ---- | ---- | ------- | ----------- |
| `doc_id` | `str` | zorunlu | Kaynak belge UUID'si (benzer eşleşmeleri bulmak istediğiniz belge) |
| `k` | `int` | `5` | Döndürülecek benzer belge sayısı (50 ile sınırlı) |

**Döndürür:** `list[dict]` — Her dict şunları içerir:

| Alan | Açıklama |
| ----- | ----------- |
| `doc_id` | Benzer belge UUID'si |
| `name` | Dosya adı |
| `doc_type` | Belge türü |
| `similarity_score` | Ham benzerlik puanı (0-1) |
| `similarity_percent` | Yüzde olarak benzerlik (0-100) |

**Örnek — Benzer belgeleri bulma:**

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)
for doc in similar:
    print(f"{doc['name']}: {doc['similarity_percent']}% benzer")
```

{% hint style="info" %}
**Nasıl çalışır:** Her belge indekslendiğinde 384 boyutlu bir vektöre dönüştürülür. Vektör araması bu vektör uzayında en yakın komşuları bulur, bunlar anlamsal olarak benzer belgelere karşılık gelir.
{% endhint %}

---

## fulltext\_search\_erp()

OpenSearch'te indekslenmiş ERP ana verilerini (tedarikçiler, satın alma siparişleri, müşteriler, malzemeler) arar.

```python
fulltext_search_erp(query, **kwargs)
```

**Parametreler:**

| Ad | Tip | Varsayılan | Açıklama |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | zorunlu | Arama terimi |
| `entity_types` | `str` | `None` | Varlık türüne göre filtrele (virgülle ayrılmış: `"vendor"`, `"purchase_order"`, `"customer"`, `"material"`) |
| `vendor_number` | `str` | `None` | Tedarikçi numarasına göre filtrele |
| `vendor_name` | `str` | `None` | Tedarikçi adına göre filtrele |
| `company_code` | `str` | `None` | Şirket koduna göre filtrele |
| `size` | `int` | `10` | Maksimum sonuç (50 ile sınırlı) |

**Döndürür:** `list[dict]` — Varlık türüne özgü alanlar (tedarikçi kayıtlarında `vendor_number`, `vendor_name` vb. bulunur)

**Örnek — Tedarikçiyi ERP'de doğrulama:**

```python
vendor = get_field_value(document_data, "supplier_name", "")
if vendor:
    matches = fulltext_search_erp(vendor,
                                   entity_types="vendor", size=5)
    if not matches:
        set_field_as_invalid(document_data, "supplier_name",
                             "Vendor not found in ERP master data")
```

**Örnek — Satın alma siparişlerini arama:**

```python
po_number = get_field_value(document_data, "purchase_order", "")
if po_number:
    results = fulltext_search_erp(po_number,
                                   entity_types="purchase_order")
    if results:
        # SB ERP'de bulundu
        set_field_as_valid(document_data, "purchase_order", "PO verified in ERP")
```

---

## fulltext\_suggestions()

Arama terimleri için otomatik tamamlama önerileri döndürür. Sonuçları kategoriye göre gruplar (tedarikçiler, dosya adları, fatura numaraları).

```python
fulltext_suggestions(query, **kwargs)
```

**Parametreler:**

| Ad | Tip | Varsayılan | Açıklama |
| ---- | ---- | ------- | ----------- |
| `query` | `str` | zorunlu | Önek / arama terimi |
| `limit` | `int` | `10` | Kategori başına maksimum öneri (20 ile sınırlı) |

**Döndürür:** `dict` gruplandırılmış önerilerle:

```python
{
    "vendors": ["ACME Corp", "ACME International"],
    "filenames": ["INV-2026-001.pdf", "INV-2026-002.pdf"],
    "invoice_numbers": ["INV-2026-001", "INV-2026-002"]
}
```

**Örnek — Tedarikçi önerileri alma:**

```python
suggestions = fulltext_suggestions("ACM", limit=5)
vendor_list = suggestions.get("vendors", [])
```

{% hint style="warning" %}
**Boş sorgu:** Boş bir dize geçmek hemen `{}` döndürür.
{% endhint %}

---

## Hızlı Başvuru

| Fonksiyon | Amaç | Döndürür |
| -------- | ------- | ------- |
| `fulltext_search(query, ...)` | Tüm belgelerde OCR metni arama | `list[dict]` |
| `vector_search(doc_id, ...)` | Anlamsal olarak benzer belgeleri bulma | `list[dict]` |
| `fulltext_search_erp(query, ...)` | ERP ana verilerini arama | `list[dict]` |
| `fulltext_suggestions(query, ...)` | Otomatik tamamlama önerileri | `dict` |

---

## Yaygın Kalıplar

### Lisans Kontrolü

Dört fonksiyonun tümü `OPENSEARCH_ENABLED` tercihini otomatik olarak kontrol eder. Etkin değilse:

```python
# Bu RuntimeError("Fulltext search license is missing") fırlatır
results = fulltext_search("test")
```

Scriptlerde bunu zarif bir şekilde yönetmek için:

```python
try:
    results = fulltext_search("test")
except RuntimeError:
    # Bu kuruluş için OpenSearch etkin değil — aramayı atla
    results = []
```

### Alan Fonksiyonlarıyla Birleştirme

```python
# Ara → doğrula → alan ayarla
results = fulltext_search(invoice_number,
                          status="exported", size=1)
if results:
    set_field_as_invalid(document_data, "invoice_id",
                         f"Already exists: {results[0]['name']}")
else:
    set_field_as_valid(document_data, "invoice_id", "No duplicate found")
```

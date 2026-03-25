# Koşullara Göre Otomatik Dışa Aktarma

## Bu script ne yapar?

Belirli koşullar karşılandığında belge durumunu otomatik olarak "dışa aktarmaya hazır" olarak ayarlar: tedarikçi bilinen/güvenilir bir satıcıdır VE fatura tutarı bir eşiğin altındadır. Bu, düşük riskli faturalar için manuel doğrulamayı atlar.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE** üzerinde

## Tam Script

```python
# İlgili alanları oku
net = get_field_value(document_data, "net_amount", "0")
supplier = get_field_value(document_data, "supplier_name", "", is_clean=True)

try:
    net_float = float(net)
except ValueError:
    net_float = 0

# Otomatik dışa aktarma için güvenilir tedarikçileri tanımla
auto_export_suppliers = ["OFFICEDEPOT", "STAPLES", "AMAZON"]

# Bilinen tedarikçiler ve küçük tutarlar için otomatik dışa aktarma
if any(s in supplier for s in auto_export_suppliers) and net_float < 500:
    doc_id = document_json["doc_id"]
    update_document_status_with_doc_id(
        doc_id, user, org_id, "ready_for_export",
        message="Otomatik dışa aktarıldı (küçük tutar, bilinen tedarikçi)"
    )
```

## Adım Adım Açıklama

1. **Net tutar ve tedarikçi adını** belgeden oku (karşılaştırma için tedarikçi `is_clean=True` ile)
2. **Güvenilir tedarikçileri tanımla** — bilinen satıcı adlarının listesi (temizlenmiş/büyük harf)
3. **Koşulları kontrol et** — tedarikçi güvenilir listede olmalı VE tutar 500'ün altında olmalı
4. **Durumu değiştir** — açıklayıcı bir mesajla `"ready_for_export"` olarak ayarla

{% hint style="warning" %}
**Dikkat:** Durum değişiklikleri sonraki iş akışlarını tetikler (DocFlow, dışa aktarma kancaları). İstenmeyen dışa aktarmaları önlemek için koşulların yeterince sıkı olduğundan emin olun.
{% endhint %}

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Alan değerlerini okuma
- [update\_document\_status\_with\_doc\_id()](../business-logic-functions.md#update\_document\_status\_with\_doc\_id) — Belge durumunu değiştirme

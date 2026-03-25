# Dinamik Zorunlu Alanlar

## Bu script ne yapar?

Belge içeriğine göre alan gereksinimlerini dinamik olarak ayarlar. Bu örnekte: fatura para birimi EUR değilse, döviz kuru alanı zorunlu ve görünür hale gelir. EUR faturalarında döviz kuru alanı gizlenir ve isteğe bağlı olur.

## Tetikleyici

`ON_FIELD_CHANGE` belge türü **INVOICE** üzerinde

## Tam Script

```python
# Mevcut para birimini oku
currency = get_field_value(document_data, "currency", "EUR")

# Yabancı para birimi: döviz kuru zorunlu ve görünür
if currency and currency != "EUR":
    set_is_required(document_data, "exchange_rate", True)
    set_is_hidden(document_data, "exchange_rate", False)
else:
    # EUR: döviz kuru isteğe bağlı ve gizli
    set_is_required(document_data, "exchange_rate", False)
    set_is_hidden(document_data, "exchange_rate", True)
```

## Varyasyon: Satınalma faturası vs. maliyet faturası

```python
po = get_field_value(document_data, "purchase_order", "")

if po and po.strip():
    # Satınalma faturası: SB numarası zorunlu
    set_field_value(document_data, "invoice_category", "PURCHASE_INVOICE")
    set_is_required(document_data, "purchase_order", True)
else:
    # Maliyet faturası: SB numarası gerekli değil, tabloyu gizle
    set_field_value(document_data, "invoice_category", "COST_INVOICE")
    set_is_required(document_data, "purchase_order", False)
    delete_tables(document_data)
```

## Adım Adım Açıklama

1. **Kontrol alanını oku** (bu durumda para birimi)
2. **İş kurallarını uygula** — değere göre farklı alan gereksinimleri
3. **Görünürlüğü ayarla** — UI'ı temiz tutmak için ilgisiz alanları gizle
4. **Gereksinimleri ayarla** — ilgili alanları zorunlu yap

{% hint style="info" %}
**Tetikleyici seçimi:** `ON_FIELD_CHANGE` kullanıcı bir alanı her değiştirdiğinde çalışır, böylece gereksinimler gerçek zamanlı olarak güncellenir. `AFTER_FORMATTING` yalnızca ilk çıkarmadan sonra bir kez çalışır.
{% endhint %}

## Kullanılan Fonksiyonlar

- [get\_field\_value()](../field-functions.md#get\_field\_value) — Kontrol alanını okuma
- [set\_is\_required()](../field-functions.md#set\_is\_required) — Alanı zorunlu/isteğe bağlı ayarlama
- [set\_is\_hidden()](../field-functions.md#set\_is\_hidden) — Alanları gösterme/gizleme
- [set\_field\_value()](../field-functions.md#set\_field\_value) — Kategori alanını ayarlama
- [delete\_tables()](../table-functions.md#delete\_tables) — Maliyet faturaları için tabloları kaldırma

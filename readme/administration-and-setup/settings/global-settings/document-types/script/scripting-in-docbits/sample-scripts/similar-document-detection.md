# Benzer Belge Tespiti (Vektör Araması)

{% hint style="info" %}
**Sürüm 11.48.0'dan itibaren kullanılabilir** — `OPENSEARCH_ENABLED` lisansı gerektirir.
{% endhint %}

## Bu script ne yapar?

Mevcut belgeye anlamsal olarak benzer belgeleri bulmak için vektör tabanlı benzerlik araması kullanır. %95'ten fazla benzerliğe sahip bir belge bulunursa, fatura numarası potansiyel olarak sahte veya kopya olarak işaretlenir.

## Tetikleyici

`AFTER_FORMATTING` belge türü **INVOICE**

## Tam Script

```python
doc_id = document_json["doc_id"]
similar = vector_search(doc_id, k=5)

for doc in similar:
    if doc["similarity_percent"] > 95:
        set_field_as_invalid(
            document_data, "invoice_id",
            f"95%+ similar to: {doc['name']} (Score: {doc['similarity_percent']}%)"
        )
        break
```

## Adım Adım Açıklama

1. **Mevcut belge ID'sini al** `document_json`'dan
2. **Benzer belgeleri bul** `vector_search()` ile en yakın 5 komşuyu döndürerek
3. **Benzerlik eşiğini kontrol et**: Herhangi bir belge %95 benzerliği aşarsa, işaretle
4. **Geçersiz olarak işaretle** benzer belgenin adı ve benzerlik puanıyla

## Vektör Araması Nasıl Çalışır

Her belgenin OCR metni indekslendiğinde 384 boyutlu bir vektör gömmeye dönüştürülür. `vector_search()`, k-NN (k-En Yakın Komşu) kullanarak bu vektör uzayında en yakın komşuları bulur ve içeriği anlamsal olarak benzer olan belgeleri döndürür — tam kelimeler farklı olsa bile.

**Kullanım alanları:**
- Dolandırıcılık tespiti (farklı "tedarikçilerden" neredeyse aynı faturalar)
- Tam metin eşleşmesinin ötesine geçen kopya tespiti
- Farklı formatlarda veya dillerde ilgili belgeleri bulma

## Kullanılan Fonksiyonlar

- [vector\_search()](../fulltext-search-functions.md#vector\_search) — Anlamsal olarak benzer belgeleri bul
- [set\_field\_as\_invalid()](../field-functions.md#set\_field\_as\_invalid) — Doğrulama hatası göster

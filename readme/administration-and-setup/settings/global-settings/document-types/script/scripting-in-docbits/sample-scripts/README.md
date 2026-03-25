# Örnek Scriptler

Yaygın DocBits otomasyon kullanım senaryoları için üretime hazır script örnekleri. Her örnek, tam scripti, adım adım açıklamayı ve kullanılan fonksiyonlara bağlantıları içerir.

## Kullanım Senaryosuna Göre Örnekler

### Veri Doğrulama
- [Tedarikçi Lookup Doğrulaması](lookup-supplier-validation.md) — Tedarikçiyi ana verilere karşı doğrulama
- [Tablo Toplamı Doğrulaması](table-sum-validation.md) — Satır kalem toplamlarının net tutarla eşleştiğini doğrulama

### Otomasyon
- [Otomatik SB Eşleştirme](auto-po-matching.md) — Otomatik SB eşleştirmeyi tetikleme
- [Koşullara Göre Otomatik Dışa Aktarma](status-auto-export.md) — Düşük riskli faturalar için doğrulamayı atlama
- [Vade Tarihi Hesaplama](due-date-calculation.md) — Hafta sonu atlama ile ödeme koşullarını hesaplama

### İş Kuralları
- [Vergi Kodu Tespiti](tax-code-detection.md) — Tam metin ve tutarlardan vergi kodunu belirleme
- [Yüksek Tutar için Görev](task-high-amount.md) — Büyük faturalar için onay görevi oluşturma
- [Dinamik Zorunlu Alanlar](dynamic-required-fields.md) — Para birimine göre zorunlu alanları ayarlama

### Fulltext ve Vektör Arama
- [Yinelenen Fatura Tespiti](duplicate-invoice-detection.md) — Fulltext arama kullanarak yinelenen faturaları bulma
- [Benzer Belge Tespiti](similar-document-detection.md) — Vektör arama kullanarak benzer belgeleri işaretleme
- [Uyumluluk Metin Araması](compliance-text-search.md) — Uyumluluk anahtar kelimelerini arama (ör. Reverse Charge)
- [ERP Tedarikçi Doğrulaması](erp-vendor-validation.md) — Tedarikçiyi ERP ana verilerine karşı doğrulama
- [Eksik Alanları Geçmişten Doldurma](fill-missing-fields-from-history.md) — Benzer geçmiş belgelerden alanları otomatik doldurma

### Eski Örnekler
- [Toplam Masrafların Hesaplanması](calculating-total-charges-script-for-docbits-1.md) — Navlun ve paketleme tutarlarını toplama
- [Boş Satırları Silme](delete-lines-with-empty-quantity-and-amount.md) — Sıfır miktar/tutarlı satırları kaldırma
- [İhracat Sertifikası Referans Numaraları](formatting-export-certificate-reference-numbers-script-for-docbits.md) — Referans numaralarını öndeki sıfırlarla doldurma
- [Genişletilmiş Fatura Numaraları](generating-extended-invoice-numbers-script-for-docbits-1.md) — Fatura ID'si ve SB numarasını birleştirme
- [USD Varsayılan Para Birimi](usd-as-default-currency.md) — Varsayılan para birimi olarak USD ayarlama

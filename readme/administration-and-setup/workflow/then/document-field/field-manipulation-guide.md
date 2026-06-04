# Field & Table Manipulation Cards - Eksiksiz Kılavuz

**Kapsam:** Belge alanlarını ve tabloları değiştirmek için 9 kart

---

Bu sayfadaki alan ve tablo kartları, Workflow Builder'ın **Then** grubuna gider — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p>Alan ve tablo manipülasyon kartları <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Çok Sürümlü Kartlar:** CALC_COLUMNS (v2), CALC_COLUMNS_REGEX (v2), EDIT_COLUMN (v2), AI_CALC_MTZ_ETZ (v2)

**Sürüm Kalıbı:** Tüm alan manipülasyon kartları v1 → v2 kalıbını izler
**Temel Değişiklik:** v2, çeviri anahtarlarıyla uluslararasılaştırma (i18n) desteği ekler

📖 [Eksiksiz Sürüm Geçmişi](../../../changelog/release.md#-data-manipulation-cards) | [Kart Sürüm Veritabanı](../../../../DocFlow/docs/card_version.md)

---

# Belge Alanı Manipülasyonu

## Kart: ACTION_SET_FIELD_TO_TEXT / Alanı Metin Değerine Ayarla

### Amaç
Bir belge alanını otomatik olarak belirli bir metinle doldurur

### Ne Zaman Kullanılır
- Karardan alanı doldurma
- Varsayılan değerler ayarlama
- Standartlaştırılmış bilgiyi doldurma
- Koşullara göre alanı güncelleme

### Nasıl Çalışır
```
IF Condition is true
    THEN Set Field "Category" to Value "Premium"
```

### Örnek Senaryolar

**Senaryo 1: Onay Kategorisi Ayarlama**
```
Condition: Invoice amount > €10,000
    ↓
Action: Set "Approval_Category" field to "High Value"
    ↓
Result: Document now shows "Approval_Category: High Value"
```

**Senaryo 2: Tedarikçi Kategorisi Ayarlama**
```
Condition: Supplier name contains "ABC"
    ↓
Action: Set "Supplier_Type" field to "Preferred Supplier"
    ↓
Result: Document marked as "Preferred Supplier"
```

**Senaryo 3: İşleme Notları Ayarlama**
```
Condition: Document has been rejected
    ↓
Action: Set "Processing_Notes" to "Requires supplier revision"
    ↓
Result: Note appears for next processor
```

### Parametreler

**Alan Adı**
Hangi alanın güncelleneceği
```
Examples: Category, Type, Status, Comment, Notes
```

**Metin Değeri**
Alana ne konacağı
```
Examples: "Approved", "Pending Review", "High Priority"
```

### Yapılandırma Adımları
1. Doldurulacak alanı seçin
2. Metin değerini girin
3. Koşulları ayarlayın (ne zaman doldurulacak)
4. Kaydedin

---

## Kart: ACTION_SET_BOOLEAN_FIELD / Onay Kutusu Alanını Ayarla

### Amaç
Bir onay kutusu alanını otomatik olarak işaretler veya işaretsiz bırakır

### Ne Zaman Kullanılır
- İşlenmiş olarak işaretleme
- Onay bayraklarını ayarlama
- Seçenekleri etkinleştirme/devre dışı bırakma
- Dışa aktarma için işaretleme

### Nasıl Çalışır
```
IF Condition is true
    THEN Check/Uncheck the "Approved" box
```

### True = İşaretli, False = İşaretsiz

**Örnekler:**

**Örnek 1: Doğrulanmış Olarak İşaretleme**
```
Condition: PO matches perfectly
    ↓
Action: Check "Verified" checkbox
    ↓
Result: ✅ Verified (checked)
```

**Örnek 2: Manuel İnceleme için İşaretleme**
```
Condition: Price variance > 10%
    ↓
Action: Check "Requires_Manual_Review" checkbox
    ↓
Result: ✅ Requires_Manual_Review (marked)
```

**Örnek 3: Önceden Doldurulmuş Kutuyu İşaretsiz Bırakma**
```
Condition: Supplier is blacklisted
    ↓
Action: Uncheck "Approved_for_Payment" checkbox
    ↓
Result: ☐ Approved_for_Payment (unchecked - blocked)
```

### Parametreler
```
Checkbox Field: [Choose field]
Set To: ☑ Checked (✅ True)
   or: ☐ Unchecked (❌ False)
```

---

## Kart: ACTION_INVERT_BOOLEAN_FIELD / Onay Kutusunu Değiştir

### Amaç
Onay kutusu durumunu tersine çevirir (işaretli → işaretsiz ve tam tersi)

### Ne Zaman Kullanılır
- Onay durumunu değiştirme
- İşleme modunu değiştirme
- Önceki durumu tersine çevirme
- Boolean bayraklarını güncelleme

### Nasıl Çalışır
```
Current state: ✅ (Checked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ☐ (Unchecked)

OR

Current state: ☐ (Unchecked)
    ↓
ACTION_INVERT: Toggle the box
    ↓
New state: ✅ (Checked)
```

### Örnek
```
Invoice received with "Priority" checked
    ↓
After processing, invert "Priority" checkbox
    ↓
Checkbox now unchecked (no longer priority)
```

---

## Kart: ACTION_COPY_DOCFIELD_TO_DOCFIELD / Alan Değerini Kopyala

### Amaç
Bir alandan başka bir alana değer kopyalar

### Ne Zaman Kullanılır
- Tedarikçi bilgisini faturalama bilgisine kopyalama
- Alanlar arasında veriyi çoğaltma
- Veri biçimini standartlaştırma
- Değerin yedeğini oluşturma

### Nasıl Çalışır
```
Source Field: "Invoice_Supplier"  Value: "ABC Corp"
    ↓
COPY TO
    ↓
Target Field: "Billing_Partner"  Value: "ABC Corp"

Both fields now have same value
```

### Gerçek Örnekler

**Örnek 1: Teslimat Adresini Kopyala**
```
Source: "Delivery_Address" = "123 Main St, Berlin"
    ↓
Copy to: "Billing_Address"
    ↓
Result: Both fields show "123 Main St, Berlin"
```

**Örnek 2: Tedarikçi Kodunu Kopyala**
```
Source: "Supplier_Code_External" = "SUPP-789"
    ↓
Copy to: "Supplier_Code_Internal"
    ↓
Result: Both codes match, system recognizes supplier
```

**Örnek 3: Doğrulama için Tutarı Kopyala**
```
Source: "Invoice_Total" = "€5000"
    ↓
Copy to: "Amount_to_Validate"
    ↓
Result: Validation field has correct amount
```

### Parametreler
```
Source Field: [Choose field to copy FROM]
Target Field: [Choose field to copy TO]
```

### Notlar
- Orijinal alan değişmez
- Hedef alan kaynak değeriyle üzerine yazılır
- Veriyi standartlaştırmak için iyidir

---

# Tablo Manipülasyonu

## Kart: EDIT_COLUMN / Tablo Sütununu Düzenle

### Amaç
Koşullara göre bir tablo sütunundaki değerleri değiştirir

### Ne Zaman Kullanılır
- Satır öğelerindeki fiyatlandırma hatalarını düzeltme
- Miktarları güncelleme
- Öğe açıklamalarını düzeltme
- Değerleri standartlaştırma

### Nasıl Çalışır
```
Table Column: "Unit_Price"
Original Values: [100, 105, 103]
    ↓
FIND: Values matching condition
REPLACE: With new value
    ↓
Updated Column: [100, 110, 110] (example)
```

### Örnek: Fiyatlandırmayı Düzelt

**Senaryo: Fiyatlar yanlış para biriminde**
```
Table "Line_Items" with column "Price"

Current prices: [100, 100, 100] (in wrong currency)
    ↓
Condition: "If Price column equals 100"
    ↓
Action: Replace with 95 (corrected price)
    ↓
Result: [95, 95, 95] (prices corrected)
```

### Parametreler
```
Table: [Choose table]
Column: [Choose column to edit]
Find: [Value to find]
Replace with: [New value]
Condition: [When to apply]
```

### Yaygın Kullanımlar
- Birim fiyatları düzeltme
- Açıklamaları standartlaştırma
- Miktarları düzeltme
- SKU numaralarını güncelleme

---

## Kart: CALC_COLUMNS / Sütun Değerlerini Hesapla

### Amaç
Tablo sütunları üzerinde hesaplama yapar ve sonucu depolar

### Ne Zaman Kullanılır
- Satır toplamlarını hesaplama (Adet × Birim Fiyat)
- Sütunları toplama
- İndirimleri hesaplama
- Yüzdeleri hesaplama

### Nasıl Çalışır
```
Column A (Quantity): 100
Column B (Unit Price): €50
    ↓
CALCULATE: A × B
    ↓
Column C (Line Total): €5000
```

### Hesaplama Türleri

**Tür 1: Basit Çarpma**
```
Formula: Qty × Unit Price = Line Total

Example:
100 units × €50/unit = €5000

Config:
  Column 1: Quantity
  Operator: ×
  Column 2: Unit Price
  Result Column: Line Total
```

**Tür 2: Toplama**
```
Formula: Base Price + Shipping + Tax = Total

Example:
€5000 + €100 + €950 = €6050

Config:
  Column 1: Base Price
  Operator: +
  Column 2: Shipping
  Operator: +
  Column 3: Tax
  Result Column: Total
```

**Tür 3: Yüzde Hesaplaması**
```
Formula: Amount × (1 + Tax%) = Total with Tax

Example:
€5000 × 1.19 = €5950

Config:
  Column: Amount
  Operator: × (1 + Tax%)
  Result Column: Amount_with_Tax
```

**Tür 4: Çıkarma**
```
Formula: Original Price - Discount = Final Price

Example:
€100 - €10 = €90

Config:
  Column 1: Original Price
  Operator: -
  Column 2: Discount
  Result Column: Final Price
```

### Gerçek Dünya Örneği

**Fatura Satır Öğeleri Hesaplaması:**
```
Table: Invoice_Lines

Row 1:
  Quantity: 100
  Unit Price: €25.00
  Calculate: 100 × €25.00 = €2500.00 (Line Total)

Row 2:
  Quantity: 50
  Unit Price: €40.00
  Calculate: 50 × €40.00 = €2000.00 (Line Total)

Row 3:
  Quantity: 200
  Unit Price: €10.00
  Calculate: 200 × €10.00 = €2000.00 (Line Total)

Subtotal: €6500.00 (sum of line totals)
Tax (19%): €1235.00
Shipping: €100.00
TOTAL: €7835.00
```

### Parametreler
```
Table: [Select table]
Column 1: [First column]
Operator: [×, +, -, ÷, %]
Column 2: [Second column] (if needed)
Result Column: [Where to put answer]
```

---

## Kart: CALC_COLUMNS_REGEX / Regex Kalıbıyla Hesapla

### Amaç
Kalıp eşleştirmeye göre sütun değerlerini hesaplar

### Ne Zaman Kullanılır
- Kalıplar kullanarak metinden değerler çıkarma
- Kurallara göre veriyi biçimlendirme
- Kalıplara göre değerleri dönüştürme
- Yapılandırılmış metni ayrıştırma

### Nasıl Çalışır

**Regex Kalıbı Eşleştirme:**
```
Original Value: "ABC-12345-XYZ"
Pattern: Extract numbers only
Calculation: Convert to "12345"
Result: "12345"
```

### Örnek: Tedarikçi Kodunu Çıkar

**Senaryo: Makale numaraları tedarikçi bilgisi içeriyor**
```
Table Column: "Article_Code"
Values: ["SUPP001-2025-A", "SUPP002-2025-B"]

Pattern: Extract supplier code (first 7 characters)
    ↓
Calculate: SUPP001, SUPP002
    ↓
Store in: "Supplier_Code" column

Result:
Article_Code: SUPP001-2025-A  →  Supplier_Code: SUPP001
Article_Code: SUPP002-2025-B  →  Supplier_Code: SUPP002
```

### Örnek: Telefon Numaralarını Biçimlendir

**Senaryo: Biçimlendirilmemiş telefon numaraları**
```
Original: "491234567890"
Pattern: Format as: +49 123 4567 890
Result: "+49 123 4567 890"
```

### Örnek: Metinden Fiyatları Çıkar

**Senaryo: Metin biçiminde fiyatlar**
```
Original: "Price is 99.99 EUR"
Pattern: Extract number only
Result: "99.99"
```

### Parametreler
```
Table: [Select table]
Column: [Column to analyze]
Regex Pattern: [Pattern to find]
Replacement: [What to replace with]
Result Column: [Where to store result]
```

### Yaygın Regex Kalıpları
```
Numbers only: [0-9]+
Letters only: [a-zA-Z]+
First word: ^\w+
Extract €: €(\d+\.\d{2})
Date format: \d{4}-\d{2}-\d{2}
```

---

# Hesaplama Örnekleri

## Örnek 1: Fatura Toplam Hesaplaması
```
Step 1: Calculate line totals
  Each row: Qty × Unit Price

Step 2: Sum all line totals
  Sum: €2500 + €2000 + €2000 = €6500

Step 3: Calculate tax
  Tax: €6500 × 0.19 = €1235

Step 4: Add shipping
  Final: €6500 + €1235 + €100 = €7835
```

## Örnek 2: Sapma Hesaplaması
```
PO Price: €100
Invoice Price: €103

Variance = |(Invoice - PO)| / PO × 100
Variance = |3| / 100 × 100 = 3%

Store in "Price_Variance%" column
```

## Örnek 3: İndirim Uygulaması
```
Original Price: €100
Discount %: 10%
Discount Amount: €100 × 0.10 = €10
Final Price: €100 - €10 = €90
```

---

# Alan Manipülasyonu İş Akışı Örneği

```
Document arrives
    ↓
Check condition: "Amount > €5000?"
    ↓
YES → Set field "Category" = "High Value"
    ↓
Check condition: "Supplier is preferred?"
    ↓
YES → Check "FastTrack" checkbox
    ↓
Copy "Delivery_Address" to "Invoice_Address"
    ↓
In table: Calculate line totals (Qty × Price)
    ↓
In table: Calculate total with tax
    ↓
Document now has all calculated and populated fields
```

---

# En İyi Uygulamalar

✅ **Yapın:**
- Formülleri basit tutun
- Hesaplamaları örnek veriyle test edin
- Sonuçların mantıklı olduğunu doğrulayın
- Alanları neden değiştirdiğinizi belgeleyin
- Veri aynıysa alan kopyalamayı kullanın

❌ **Yapmayın:**
- Döngüsel referanslar oluşturma (A=B, B=A)
- Önemli veriyi nedensiz üzerine yazma
- Aşırı karmaşık regex kalıpları oluşturma
- Hesaplama sonuçlarını doğrulamayı unutma
- Yanlış tablo/sütunlarda hesaplama yapma

---

# Sorun Giderme

## "Alan güncellenmiyor"
**Neden:** Koşul karşılanmadı veya kart tetiklenmedi

**Çözüm:**
- Koşulun doğru olduğunu kontrol edin
- Kartın iş akışında olduğunu doğrulayın
- Örnek veriyle test edin
- Alan adında yazım hatası olup olmadığını kontrol edin

## "Hesaplama sonucu yanlış"
**Neden:** Yanlış sütunlar seçildi veya formül yanlış

**Çözüm:**
- Kaynak sütunları doğrulayın
- Formülün doğru olduğunu kontrol edin
- Manuel olarak test edin
- Ondalık basamakları/yuvarlamayı gözden geçirin

## "Tablo hata gösteriyor"
**Neden:** Başvurulan sütun yok

**Çözüm:**
- Sütun adı yazımını doğrulayın
- Sütunun veri içerdiğini kontrol edin
- Sütun veri türünün hesaplamayla eşleştiğinden emin olun
- Gerekirse eksik sütunları ekleyin

---

# İlgili Kartlar

- **ACTION_COPY_DOCFIELD_TO_DOCFIELD** - Değerleri kopyala
- **EDIT_COLUMN** - Tablo değerlerini değiştir
- **CALC_COLUMNS** - Formülleri hesapla
- **ACTION_SET_FIELD_TO_TEXT** - Metin değerleri ayarla
- **ACTION_SET_BOOLEAN_FIELD** - Kutuları işaretle

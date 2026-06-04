# Data Transformation Pattern

**Kalıp Türü:** Veri İşleme ve Manipülasyon
**Karmaşıklık:** Orta
**Tahmini Kurulum:** 30-45 dakika
**Yaygın Kullanım Durumları:** Alan hesaplamaları, veri biçimlendirme, para birimi dönüşümü, birim dönüşümü, veri zenginleştirme

---

Bu kalıbı **Workflow Builder**'da (Workflow Dashboard → Workflow List → Add Workflow) oluşturursunuz. **Add Card**'a tıklayın ve **Document Field** kategorisini açın — bu kalıbın zincirlediği okuma, yazma, hesaplama ve biçimlendirme kartlarını içerir:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder'da kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — alan okuma/yazma, hesaplama ve biçimlendirme kartları <strong>Document Field</strong> kategorisi altında bulunur.</p></figcaption></figure>

---

## Kalıp Genel Bakışı

Bu kalıp, DocBits iş akışlarında belge verilerinin nasıl dönüştürüleceğini, hesaplanacağını, biçimlendirileceğini ve zenginleştirileceğini gösterir. Veri dönüşümü, dışa aktarma için veri hazırlamak, hesaplamalar yapmak, biçimleri standartlaştırmak ve belgeleri ek bilgilerle zenginleştirmek için gereklidir.

**Bu Kalıbın Yaptıkları:**
1. Belge alanlarından veri çıkarır
2. Hesaplamalar ve dönüşümler yapar
3. Veriyi gerekli standartlara biçimlendirir
4. Birimler, para birimleri, tarihler arasında dönüştürür
5. Belgeleri türetilmiş veya arama verileriyle zenginleştirir
6. Veriyi doğrular ve temizler

---

## Bu Kalıbı Ne Zaman Kullanmalı

Bu kalıbı şu durumlarda kullanın:
- ✅ Toplamları, ara toplamları, vergileri hesaplama
- ✅ Para birimlerini veya birimleri dönüştürme
- ✅ Tarihleri, sayıları, metni biçimlendirme
- ✅ Mevcut alanlardan değerler türetme
- ✅ Harici kaynaklardan veri zenginleştirme
- ✅ Veri biçimlerini standartlaştırma
- ✅ Veriyi temizleme ve doğrulama
- ✅ Dışa aktarma için veri hazırlama

**Bu kalıbı şu durumlarda kullanmayın:**
- ❌ Dönüşüm gerekmiyorsa
- ❌ Veri zaten doğru biçimdeyse
- ❌ Basit alan kopyalama yeterliyse

---

## Veri Dönüşümü Türleri

### 1. Hesaplamalar

**Matematiksel İşlemler:**
```
- Addition: Quantity + Bonus_Quantity = Total_Quantity
- Subtraction: Invoice_Total - Tax_Amount = Net_Amount
- Multiplication: Quantity × Unit_Price = Line_Total
- Division: Total_Amount / Quantity = Unit_Price
- Percentage: (Discount / Subtotal) × 100 = Discount_Percent
```

### 2. Dize İşlemleri

**Metin Manipülasyonu:**
```
- Concatenation: First_Name + " " + Last_Name = Full_Name
- Uppercase: "invoice" → "INVOICE"
- Lowercase: "SUPPLIER" → "supplier"
- Substring: "INV-2025-001" → "2025" (extract year)
- Replace: "01/23/2025" → "2025-01-23"
- Trim: "  ABC Corp  " → "ABC Corp"
```

### 3. Veri Türü Dönüşümü

**Tür Dönüşümleri:**
```
- String to Number: "123.45" → 123.45
- Number to String: 123.45 → "123.45"
- Date to String: 2025-10-23 → "October 23, 2025"
- String to Date: "23.10.2025" → 2025-10-23
- Boolean to String: true → "Yes"
```

### 4. Birim Dönüşümleri

**Ölçü Dönüşümleri:**
```
- Weight: kg → lbs, tons → kg
- Length: cm → inches, m → ft
- Volume: liters → gallons
- Temperature: Celsius → Fahrenheit
- Quantity: pieces → dozens, units → pallets
```

### 5. Para Birimi Dönüşümleri

**Döviz Kuru Uygulamaları:**
```
- USD → EUR: Amount_USD × Rate = Amount_EUR
- Multi-currency: Convert all to base currency
- Historical rates: Use rate from invoice date
```

### 6. Tarih Dönüşümleri

**Tarih İşlemleri:**
```
- Format change: 10/23/2025 → 2025-10-23
- Add days: Invoice_Date + 30 = Due_Date
- Calculate age: Today - Invoice_Date = Age_Days
- Extract parts: "2025-10-23" → Year: 2025, Month: 10, Day: 23
```

---

## Eksiksiz İş Akışı Örneği

### Senaryo: Fatura Toplam Hesaplaması ve Veri Zenginleştirme

**İş Gereksinimi:**
- Faturadan satır öğelerini çıkar
- Satır toplamlarını hesapla (Adet × Fiyat)
- Ara toplamı hesapla (satır toplamlarının toplamı)
- Vergi tutarını hesapla (Ara toplam × Vergi_Oranı)
- Genel toplamı hesapla (Ara toplam + Vergi)
- Fatura başka para birimindeyse EUR'ya dönüştür
- Tutarları 2 ondalık basamağa biçimlendir
- Ürün kategorisine göre şirket GL hesabı ekle
- Hesaplamaları fatura toplamına karşı doğrula
- Sapma > %1 ise işaretle

**Kullanılan İş Akışı Kartları:**
1. ACTION_CALCULATE_FIELD - Hesaplamalar yap
2. ACTION_SET_FIELD_TO_TEXT - Sonuçları depola
3. ACTION_COPY_FIELD_VALUE - Değerleri kopyala
4. CALL_API - Döviz kurlarını al (gerekirse)
5. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Hesaplamaları doğrula
6. ACTION_SET_FIELD_FROM_MASTER_DATA - GL hesaplarıyla zenginleştir

---

## Adım Adım Uygulama

### Adım 1: Satır Öğesi Hesaplamaları

**Satır Toplamlarını Hesapla:**

**Kart:** ACTION_CALCULATE_FIELD

**Her satır öğesi için:**
```
Field: Line_Total
Formula: {{TABLE_FIELD:Quantity}} * {{TABLE_FIELD:Unit_Price}}
Result Type: Number
Decimal Places: 2
```

**Örnek:**
```
Line 1:
  Quantity: 100
  Unit Price: €50.00
  Calculation: 100 × 50.00 = €5,000.00
  Store in: Line_Total

Line 2:
  Quantity: 50
  Unit Price: €20.00
  Calculation: 50 × 20.00 = €1,000.00
  Store in: Line_Total

Line 3:
  Quantity: 25
  Unit Price: €15.50
  Calculation: 25 × 15.50 = €387.50
  Store in: Line_Total
```

**Kılavuz Referansı:** [Field Manipulation Guide - Calculations](../then/document-field/field-manipulation-guide.md#calculate-field)

---

### Adım 2: Belge Ara Toplamını Hesapla

**Tüm Satır Toplamlarını Topla:**

**Kart:** ACTION_CALCULATE_FIELD

**Yapılandırma:**
```
Field: Calculated_Subtotal
Formula: SUM({{TABLE_COLUMN:Line_Total}})
Result Type: Number
Decimal Places: 2
```

**Örnek:**
```
Line 1 Total: €5,000.00
Line 2 Total: €1,000.00
Line 3 Total: €387.50

Subtotal = 5000 + 1000 + 387.50 = €6,387.50
Store in: Calculated_Subtotal
```

---

### Adım 3: Vergi Tutarını Hesapla

**Ara Toplama Vergi Oranı Uygula:**

**Kart:** ACTION_CALCULATE_FIELD

**Yapılandırma:**
```
Field: Calculated_Tax_Amount
Formula: {{Calculated_Subtotal}} * ({{Tax_Rate}} / 100)
Result Type: Number
Decimal Places: 2
```

**Örnek:**
```
Calculated_Subtotal: €6,387.50
Tax_Rate: 19% (VAT)

Tax Amount = 6387.50 × (19 / 100)
          = 6387.50 × 0.19
          = €1,213.63

Store in: Calculated_Tax_Amount
```

---

### Adım 4: Genel Toplamı Hesapla

**Ara Toplam ve Vergiyi Topla:**

**Kart:** ACTION_CALCULATE_FIELD

**Yapılandırma:**
```
Field: Calculated_Grand_Total
Formula: {{Calculated_Subtotal}} + {{Calculated_Tax_Amount}}
Result Type: Number
Decimal Places: 2
```

**Örnek:**
```
Calculated_Subtotal: €6,387.50
Calculated_Tax_Amount: €1,213.63

Grand Total = 6387.50 + 1213.63 = €7,601.13

Store in: Calculated_Grand_Total
```

---

### Adım 5: Para Birimi Dönüşümü (gerekirse)

**Dönüşümün gerekli olup olmadığını kontrol et:**

**Kart:** CONDITION_DOC_FIELD_IS

**Yapılandırma:**
```
Field: Invoice_Currency
Operator: IS NOT EQUAL TO
Value: EUR
```

**Dönüşüm gerekiyorsa:**

**Adım 5a: Döviz Kurunu Al**

**Kart:** CALL_API

**Yapılandırma:**
```
Endpoint: https://api.exchangerate-api.com/v4/latest/{{Invoice_Currency}}
Method: GET
Response Path: rates.EUR
Store in: Exchange_Rate_To_EUR
```

**Örnek:**
```
Invoice Currency: USD
API Response: {
  "base": "USD",
  "rates": {
    "EUR": 0.92
  }
}

Exchange_Rate_To_EUR = 0.92
```

**Adım 5b: Tutarları Dönüştür**

**Kart:** ACTION_CALCULATE_FIELD

**Yapılandırma:**
```
Field: Grand_Total_EUR
Formula: {{Calculated_Grand_Total}} * {{Exchange_Rate_To_EUR}}
Result Type: Number
Decimal Places: 2
```

**Örnek:**
```
Grand Total (USD): $7,601.13
Exchange Rate: 0.92

Grand Total (EUR) = 7601.13 × 0.92 = €6,993.04

Store in: Grand_Total_EUR
```

**Kılavuz Referansı:** [API Integration Pattern - Currency Conversion](api-integration-pattern.md#currency-conversion-example)

---

### Adım 6: Veri Zenginleştirme - GL Hesapları Ekle

**Ürün Kategorisine Göre GL Hesabı Ara:**

**Kart:** ACTION_SET_FIELD_FROM_MASTER_DATA

**Yapılandırma:**
```
Lookup Table: GL_Account_Mapping
Lookup Key: {{TABLE_FIELD:Product_Category}}
Return Field: GL_Account_Number
Store in: GL_Account
```

**Örnek:**
```
Line 1:
  Product Category: "Office Supplies"
  Lookup → GL_Account_Mapping table
  Result: GL Account "4200-100" (Office Expense)

Line 2:
  Product Category: "IT Equipment"
  Lookup → GL_Account_Mapping table
  Result: GL Account "6100-200" (IT Assets)

Line 3:
  Product Category: "Services"
  Lookup → GL_Account_Mapping table
  Result: GL Account "5000-300" (Services Expense)
```

**Kılavuz Referansı:** [Field Manipulation Guide - Master Data](../then/document-field/field-manipulation-guide.md#master-data-lookup)

---

### Adım 7: Hesaplamaları Doğrula

**Hesaplanan Toplamı Fatura Toplamıyla Karşılaştır:**

**Kart:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Yapılandırma:**
```
Field 1: Calculated_Grand_Total
Field 2: Invoice_Total (from OCR)
Operator: Calculate Variance Percentage
Tolerance: 1%
```

**Hesaplama:**
```
Variance % = |Calculated - Invoice| / Invoice × 100

Example:
  Calculated Total: €7,601.13
  Invoice Total: €7,600.00

  Variance = |7601.13 - 7600.00| / 7600.00 × 100
          = 1.13 / 7600.00 × 100
          = 0.015%

  Is 0.015% ≤ 1% tolerance? YES ✅
  Result: PASS (calculations match invoice)
```

**Mantık:**
```
IF Variance ≤ 1%:
  Set Validation_Status = "PASS"
  Continue processing
ELSE:
  Set Validation_Status = "FAIL"
  Create review task
  Flag for manual verification
```

**Kılavuz Referansı:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Adım 8: Dışa Aktarma için Veriyi Biçimlendir

**Biçimleri Standartlaştır:**

**Kart:** ACTION_SET_FIELD_TO_TEXT

**Tarih Biçimlendirme:**
```
Field: Invoice_Date_Formatted
Value: FORMATDATE({{Invoice_Date}}, "YYYY-MM-DD")
Example: 10/23/2025 → 2025-10-23
```

**Sayı Biçimlendirme:**
```
Field: Amount_Formatted
Value: FORMATNUMBER({{Grand_Total_EUR}}, 2, ",", ".")
Example: 7601.13 → 7.601,13 (German format)
```

**Metin Biçimlendirme:**
```
Field: Supplier_Name_Upper
Value: UPPERCASE({{Supplier_Name}})
Example: "ABC Corporation" → "ABC CORPORATION"
```

---

## Gelişmiş Dönüşümler

### Dönüşüm 1: Çok Düzeyli Vergi Hesaplaması

**Senaryo:** Satır öğesi başına farklı vergi oranları

```
Line 1: Product A (Tax Rate 19%)
Line 2: Product B (Tax Rate 7% - reduced)
Line 3: Product C (Tax Rate 0% - exempt)

Calculation:
  Line 1 Tax = €5,000.00 × 0.19 = €950.00
  Line 2 Tax = €1,000.00 × 0.07 = €70.00
  Line 3 Tax = €387.50 × 0.00 = €0.00

  Total Tax = €950.00 + €70.00 + €0.00 = €1,020.00
```

**Uygulama:**
```
For each line:
  1. Get product tax category
  2. Lookup applicable tax rate
  3. Calculate: Line_Net × Tax_Rate = Line_Tax
  4. Sum all Line_Tax values = Total_Tax
```

---

### Dönüşüm 2: İndirim Hesaplamaları

**Senaryo:** Hacim indirimi ve erken ödeme indirimi uygula

```
Original Subtotal: €10,000.00

Step 1: Volume Discount (10% for orders > €5,000)
  Discount = €10,000.00 × 0.10 = €1,000.00
  After Volume Discount = €10,000.00 - €1,000.00 = €9,000.00

Step 2: Early Payment Discount (2% if paid within 10 days)
  Discount = €9,000.00 × 0.02 = €180.00
  After Payment Discount = €9,000.00 - €180.00 = €8,820.00

Step 3: Calculate Tax (on discounted amount)
  Tax = €8,820.00 × 0.19 = €1,675.80

Final Total = €8,820.00 + €1,675.80 = €10,495.80
```

**Uygulama:**
```
1. Check order value for volume discount eligibility
2. Calculate volume discount
3. Apply volume discount to subtotal
4. Check payment terms for early payment discount
5. Calculate early payment discount
6. Apply early payment discount
7. Calculate tax on final discounted amount
8. Calculate grand total
```

---

### Dönüşüm 3: Ölçü Birimi Dönüşümü

**Senaryo:** Fatura ölçü birimini standart ölçü birimine dönüştür

```
Invoice shows:
  Product: Steel Rods
  Quantity: 50
  Unit: Meters
  Unit Price: €10.00/meter
  Line Total: €500.00

Company standard UOM: Feet

Conversion:
  1 meter = 3.28084 feet

  Quantity (feet) = 50 meters × 3.28084 = 164.042 feet
  Unit Price (feet) = €10.00/meter ÷ 3.28084 = €3.05/foot

  Verification: 164.042 feet × €3.05/foot ≈ €500.00 ✅
```

**Uygulama:**
```
1. Identify invoice UOM
2. Get conversion factor to standard UOM
3. Convert quantity
4. Convert unit price
5. Verify line total remains same
6. Store both original and converted values
```

---

### Dönüşüm 4: Tarih Hesaplamaları

**Senaryo:** Ödeme koşullarını ve vade tarihlerini hesapla

```
Invoice Date: 2025-10-23
Payment Terms: NET30

Calculations:
  Due Date = Invoice Date + 30 days = 2025-11-22

  Early Payment Discount Available If:
    Payment Date ≤ Invoice Date + 10 days
    Discount End Date = 2025-11-02

  Days Until Due = Due Date - Today
    If Today = 2025-10-23: Days = 30
    If Today = 2025-11-15: Days = 7
    If Today = 2025-11-23: Days = -1 (overdue)
```

**Uygulama:**
```
1. Extract Invoice_Date
2. Extract Payment_Terms (e.g., "NET30", "NET60", "2/10 NET30")
3. Parse payment terms
4. Calculate Due_Date
5. Calculate Discount_End_Date (if applicable)
6. Calculate Days_Until_Due
7. Set Status: "Current", "Due Soon", "Overdue"
```

---

### Dönüşüm 5: Metin Ayrıştırma ve Çıkarma

**Senaryo:** Yapılandırılmamış metinden yapılandırılmış veri çıkar

```
Original Field: "PO-2025-ABC-12345-REV2"

Extract:
  Year: "2025"
  Department: "ABC"
  PO Number: "12345"
  Revision: "2"

Method:
  Split by delimiter "-"
  Array: ["PO", "2025", "ABC", "12345", "REV2"]

  Extract:
    Year = Array[1] = "2025"
    Department = Array[2] = "ABC"
    PO_Number = Array[3] = "12345"
    Revision = Extract digits from Array[4] = "2"
```

---

## Eksiksiz Dönüşüm İş Akışı Diyagramı

```
INVOICE DATA EXTRACTED
│
├─ STEP 1: LINE ITEM CALCULATIONS
│  For each line:
│    Quantity × Unit_Price = Line_Total
│  Result: Line totals calculated
│
├─ STEP 2: SUBTOTAL CALCULATION
│  SUM(All Line_Totals) = Subtotal
│  Result: €6,387.50
│
├─ STEP 3: TAX CALCULATION
│  Subtotal × Tax_Rate = Tax_Amount
│  €6,387.50 × 19% = €1,213.63
│
├─ STEP 4: GRAND TOTAL CALCULATION
│  Subtotal + Tax_Amount = Grand_Total
│  €6,387.50 + €1,213.63 = €7,601.13
│
├─ STEP 5: CURRENCY CHECK
│  │
│  ├─ Currency = EUR? YES
│  │  → Skip conversion
│  │  → Use Grand_Total as is
│  │
│  └─ Currency ≠ EUR? NO (e.g., USD)
│     │
│     ├─ Call Exchange Rate API
│     │  Get: USD → EUR rate (0.92)
│     │
│     ├─ Convert Amount
│     │  $7,601.13 × 0.92 = €6,993.04
│     │
│     └─ Store converted amount
│        Grand_Total_EUR = €6,993.04
│
├─ STEP 6: DATA ENRICHMENT
│  For each line:
│    Lookup Product_Category → GL_Account
│    Store GL_Account in line item
│  Result: All lines have GL accounts
│
├─ STEP 7: VALIDATION
│  │
│  ├─ Compare Calculated vs Invoice Total
│  │  Variance = |Calculated - Invoice| / Invoice × 100
│  │
│  ├─ Variance ≤ 1%? ✅
│  │  Set Validation_Status = "PASS"
│  │  Continue processing
│  │
│  └─ Variance > 1%? ❌
│     Set Validation_Status = "FAIL"
│     Create review task
│     Flag for manual check
│
├─ STEP 8: FORMATTING
│  │
│  ├─ Format Dates
│  │  10/23/2025 → 2025-10-23
│  │
│  ├─ Format Numbers
│  │  7601.13 → 7.601,13 (locale-specific)
│  │
│  ├─ Format Text
│  │  "abc corp" → "ABC CORP"
│  │
│  └─ Format for Export
│     All fields in ERP-compatible format
│
└─ TRANSFORMATION COMPLETE
   Document ready for next workflow step
```

---

## Yapılandırma Şablonları

### Şablon 1: Standart Fatura Hesaplamaları

```json
{
  "transformations": [
    {
      "step": 1,
      "name": "Calculate Line Totals",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Quantity}} * {{Unit_Price}}",
      "result_field": "Line_Total"
    },
    {
      "step": 2,
      "name": "Calculate Subtotal",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "SUM({{Line_Total}})",
      "result_field": "Calculated_Subtotal"
    },
    {
      "step": 3,
      "name": "Calculate Tax",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} * {{Tax_Rate}} / 100",
      "result_field": "Calculated_Tax"
    },
    {
      "step": 4,
      "name": "Calculate Total",
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Calculated_Subtotal}} + {{Calculated_Tax}}",
      "result_field": "Calculated_Total"
    }
  ]
}
```

---

### Şablon 2: Para Birimi Dönüşümü İş Akışı

```json
{
  "currency_conversion": {
    "check_needed": {
      "card": "CONDITION_DOC_FIELD_IS",
      "field": "Invoice_Currency",
      "operator": "NOT EQUAL TO",
      "value": "EUR"
    },
    "get_rate": {
      "card": "CALL_API",
      "endpoint": "https://api.exchangerate.com/v1/rates/{{Invoice_Currency}}",
      "method": "GET",
      "response_path": "rates.EUR"
    },
    "convert": {
      "card": "ACTION_CALCULATE_FIELD",
      "formula": "{{Amount}} * {{Exchange_Rate}}",
      "result_field": "Amount_EUR"
    },
    "store_details": {
      "original_currency": "{{Invoice_Currency}}",
      "original_amount": "{{Amount}}",
      "exchange_rate": "{{Exchange_Rate}}",
      "converted_amount": "{{Amount_EUR}}",
      "conversion_date": "{{Today}}"
    }
  }
}
```

---

## Hata Yönetimi

### Yaygın Dönüşüm Hataları

**Hata 1: Sıfıra Bölme**
```
Problem: Unit_Price = Total / Quantity, but Quantity = 0

Solution:
  IF Quantity = 0 OR Quantity IS NULL:
    Set Unit_Price = 0
    Flag for review
  ELSE:
    Calculate normally
```

**Hata 2: Geçersiz Sayı Biçimi**
```
Problem: Field contains "€1,234.56" but need number 1234.56

Solution:
  1. Remove currency symbols
  2. Remove thousand separators
  3. Convert decimal separator if needed
  4. Parse to number
  5. Validate result
```

**Hata 3: Tarih Ayrıştırma Hatası**
```
Problem: Date in unexpected format

Solution:
  1. Try multiple date formats
  2. If all fail: Set to null
  3. Flag for manual review
  4. Log original value
```

**Hata 4: Eksik Dönüşüm Faktörü**
```
Problem: Unknown UOM conversion

Solution:
  1. Check conversion table
  2. If not found: Skip conversion
  3. Flag for admin to add conversion
  4. Use original values
```

---

## Test Kontrol Listesi

- [ ] Tüm hesaplamalar doğru sonuçlar üretiyor
- [ ] Ondalık hassasiyet korunuyor
- [ ] Para birimi dönüşümleri doğru
- [ ] Tarih hesaplamaları doğru
- [ ] Metin dönüşümleri çalışıyor
- [ ] Null/boş değerler ele alınıyor
- [ ] Sıfıra bölme önleniyor
- [ ] Sayı biçimleri doğrulanıyor
- [ ] Yuvarlama kuralları doğru uygulanıyor
- [ ] Tüm dönüştürülmüş alanlar dolduruldu
- [ ] Doğrulama hataları yakalıyor
- [ ] Dışa aktarma biçimi doğru

---

## İlgili Kalıplar

### İyi Birlikte Çalışan Kalıplar:

- **[API Integration Pattern](api-integration-pattern.md)** - Döviz kurları, zenginleştirme verisi alma
- **[PO Matching Pattern](po-matching-pattern.md)** - Sapma hesaplamaları
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Hesaplanan değerlere göre yönlendirme
- **[Task Management Pattern](task-management-pattern.md)** - Doğrulama hataları için görevler oluşturma

---

## İlgili Kılavuzlar

### Önkoşullar
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Tüm alan işlemleri
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Doğrulama koşulları
- [Call API Guide](../then/action/call-api-guide.md) - Harici veri alma

### İlgili Kartlar
- **ACTION_CALCULATE_FIELD** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#calculate-field)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **ACTION_COPY_FIELD_VALUE** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#copy-field)
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Sonraki Adımlar
- Sonuçları doğrulayın: [Decision Logic Pattern](decision-logic-pattern.md)
- Hatalar için görevler oluşturun: [Task Management Pattern](task-management-pattern.md)
- PO eşleştirmede kullanın: [PO Matching Pattern](po-matching-pattern.md)

---

**Kalıp Sürümü:** 1.0
**Son Güncelleme:** 23 Ekim 2025
**Zorluk:** Orta
**Tahmini Süre:** 30-45 dakika
**Başarı Oranı:** Yüksek

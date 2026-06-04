# PO Matching Pattern

**Kalıp Türü:** Doğrulama ve Karşılaştırma
**Karmaşıklık:** Orta-Yüksek
**Tahmini Kurulum:** 60-90 dakika
**Yaygın Kullanım Durumları:** Üç yönlü eşleştirme, fatura doğrulama, sapma kontrolü, tolerans yönetimi

---

Bu kalıbı **Workflow Builder**'da (Workflow Dashboard → Workflow List → Add Workflow) oluşturursunuz. **Add Card**'a tıklayın ve **Compare with Purchase Order** kategorisini açın — bu kalıbın kullandığı her eşleştirme kartını içerir (fiyat, miktar, tolerans ve satır öğesi karşılaştırma kartları):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Compare with Purchase Order kartlarını gösteren Add Card kütüphanesi"><figcaption><p><strong>Compare with Purchase Order</strong> kategorisi — bu kalıp boyunca kullanılan fiyat, miktar, tolerans ve satır öğesi eşleştirme kartları.</p></figcaption></figure>

---

## Kalıp Genel Bakışı

Bu kalıp, DocBits'te kapsamlı Satınalma Siparişi (PO) eşleştirme iş akışlarının nasıl uygulanacağını gösterir. PO eşleştirme, ödeme onayından önce tutarsızlıkları tespit etmek için fatura verilerini satınalma siparişi verileriyle karşılaştıran kritik bir kontrol sürecidir.

**Bu Kalıbın Yaptıkları:**
1. Faturadaki PO numarasına göre PO verilerini alır
2. Fatura satır öğelerini PO satır öğeleriyle karşılaştırır
3. Sapmaları (fiyat, miktar, toplamlar) hesaplar
4. Tolerans kurallarını uygular
5. Eşleştirme sonuçlarına göre onay veya yükseltme için yönlendirir
6. Eşleştirme geçmişini ve istisnaları izler

---

## Bu Kalıbı Ne Zaman Kullanmalı

Bu kalıbı şu durumlarda kullanın:
- ✅ Faturaları satınalma siparişlerine karşı doğrulama
- ✅ Ödemeden önce fiyatlandırma hatalarını tespit etme
- ✅ Miktar tutarsızlıklarını belirleme
- ✅ Satınalma kontrollerini uygulama
- ✅ Yinelenen ödemeleri önleme
- ✅ Üç yönlü eşleştirmeyi otomatikleştirme
- ✅ Manuel fatura inceleme iş yükünü azaltma

**Bu kalıbı şu durumlarda kullanmayın:**
- ❌ Fatura için PO yoksa (PO'suz faturalar)
- ❌ PO verileri DocBits'te mevcut değilse
- ❌ Otomasyon yerine manuel inceleme tercih ediliyorsa
- ❌ PO eşleştirme iş politikası tarafından gerekli değilse

---

## PO Eşleştirmeyi Anlamak

### Üç Yönlü Eşleştirme

**Geleneksel satınalma kontrolü:**
```
Purchase Order (PO)  →  Created when ordering
        ↓
Goods Receipt (GR)   →  Created when receiving
        ↓
Invoice              →  Created by supplier

THREE-WAY MATCH = PO + GR + Invoice all match
```

**DocBits Uygulaması (İki Yönlü Eşleştirme):**
```
Purchase Order (PO)  →  Imported to DocBits
        ↓
Invoice              →  Scanned by DocBits
        ↓
COMPARISON           →  Invoice vs PO validation
```

---

## Sapma Hesaplama Formülleri

### Birim Fiyat Sapması

**Formül:**
```
Variance % = |(Invoice Unit Price - PO Unit Price)| / PO Unit Price × 100
```

**Örnek:**
```
PO Unit Price:       €100.00
Invoice Unit Price:  €103.00

Variance = |103 - 100| / 100 × 100
        = 3 / 100 × 100
        = 3%

Tolerance: 5%
Result: 3% ≤ 5% → PASS ✅
```

---

### Miktar Sapması

**Formül:**
```
Variance % = |(Invoice Quantity - PO Quantity)| / PO Quantity × 100
```

**Örnek:**
```
PO Quantity:        100 units
Invoice Quantity:   98 units

Variance = |98 - 100| / 100 × 100
        = 2 / 100 × 100
        = 2%

Tolerance: 10%
Result: 2% ≤ 10% → PASS ✅
```

---

### Toplam Tutar Sapması

**Formül:**
```
Variance % = |(Invoice Total - PO Total)| / PO Total × 100
```

**Örnek:**
```
PO Total:       €10,000.00
Invoice Total:  €10,450.00

Variance = |10450 - 10000| / 10000 × 100
        = 450 / 10000 × 100
        = 4.5%

Tolerance: 5%
Result: 4.5% ≤ 5% → PASS ✅
```

---

## Eksiksiz İş Akışı Örneği

### Senaryo: Tolerans Tabanlı Yönlendirmeyle Fatura Doğrulama

**İş Gereksinimi:**
- PO referanslı tüm faturalar doğrulanmalıdır
- Fiyat sapması toleransı: %5
- Miktar sapması toleransı: %10
- Toplam tutar sapması toleransı: %3
- Tolerans içinde: Otomatik onayla
- Tolerans dışında: İnceleme görevi oluştur
- PO eksik: Satınalmaya yükselt

**Kullanılan İş Akışı Kartları:**
1. CONDITION_DOC_FIELD_EXISTS - PO numarasının mevcut olup olmadığını kontrol et
2. PURCHASE_ORDER_FULL_MATCH - Tam eşleştirme dene
3. CONDITION_DOC_TO_PO_UNIT_PRICE - Fiyat sapmasını kontrol et
4. CONDITION_DOC_TO_PO_QUANTITY - Miktar sapmasını kontrol et
5. CONDITION_DOC_TO_PO_TAX_LINES - Vergi hizalamasını kontrol et
6. ACTION_SET_FIELD_TO_TEXT - Eşleştirme sonuçlarını depola
7. tasks_create - İnceleme görevleri oluştur
8. ACTION_SEND_EMAIL_TO_GROUPS - Bildirimler gönder

---

## Adım Adım Uygulama

### Adım 1: PO Referansını Kontrol Et

**Kart:** CONDITION_DOC_FIELD_EXISTS veya CONDITION_DOC_FIELD_CONTAINS

**Yapılandırma:**
```
Field: PO_Number
Operator: IS NOT EMPTY
```

**Mantık:**
```
IF PO_Number exists:
  → Continue to PO matching
ELSE:
  → Route to "Non-PO Invoice" workflow
  → Create manual review task
  → Skip PO matching
```

**Kılavuz Referansı:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Adım 2: PO Verilerini Al

**DocBits'te Otomatik:**
- Sistem, PO_Number alanına göre PO'yu arar
- PO satır öğelerini alır
- Veriyi karşılaştırma için kullanılabilir hale getirir

**Manuel Yapılandırma (gerekirse):**
```
PO Source: DocBits Master Data
PO Lookup Field: PO_Number
Match Type: Exact Match
Include Closed POs: No (or Yes if policy allows)
```

---

### Adım 3: Tam PO Eşleştirme Kontrolü

**Kart:** PURCHASE_ORDER_FULL_MATCH

**Amaç:** Her şeyin mükemmel eşleşip eşleşmediğini hızlıca kontrol etme

**Yapılandırma:**
```
Match Level: Full Match
Include: All line items, prices, quantities, totals
Tolerance: None (exact match)
```

**Mantık:**
```
IF Full Match = TRUE:
  → Set "PO_Match_Status" = "FULL MATCH"
  → Auto-approve document
  → Skip detailed checks
  → END ✅

IF Full Match = FALSE:
  → Continue to detailed variance checks
  → Identify specific variances
```

**Sonuç:**
- **TRUE**: Mükemmel eşleşme, otomatik onayla
- **FALSE**: Ayrıntılı kontrollere geç

---

### Adım 4: Birim Fiyat Sapmasını Kontrol Et

**Kart:** CONDITION_DOC_TO_PO_UNIT_PRICE (v5 önerilir)

**Yapılandırma:**
```
Comparison Mode: Percentage Variance
Tolerance: 5%
Operator: Variance is Less Than or Equal To
Apply To: All line items
```

**Adım Adım:**
```
For each line item:
  1. Get Invoice Unit Price
  2. Get PO Unit Price (matched by product code)
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 5%?
  5. Store result
```

**Örnek Hesaplama:**
```
Line Item 1:
  Product: ABC123
  Invoice Price: €52.00
  PO Price: €50.00
  Variance = |52-50|/50 × 100 = 4%
  Tolerance: 5%
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Price: €120.00
  PO Price: €100.00
  Variance = |120-100|/100 × 100 = 20%
  Tolerance: 5%
  Result: FAIL ❌

Overall Result: FAIL (one or more items failed)
```

**Kılavuz Referansı:** [PO Matching Complete Guide - Unit Price](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price-comparison)

---

### Adım 5: Miktar Sapmasını Kontrol Et

**Kart:** CONDITION_DOC_TO_PO_QUANTITY

**Yapılandırma:**
```
Comparison Mode: Percentage Variance
Tolerance: 10%
Operator: Variance is Less Than or Equal To
Apply To: All line items
Allow Under-Delivery: Yes (within tolerance)
Allow Over-Delivery: No (strict)
```

**Mantık:**
```
For each line item:
  1. Get Invoice Quantity
  2. Get PO Quantity
  3. Calculate: Variance % = |Invoice - PO| / PO × 100
  4. Check: Variance % ≤ 10%?
  5. Special rules:
     - Under-delivery: Allow within tolerance
     - Over-delivery: Reject (or apply stricter tolerance)
```

**Örnek:**
```
Line Item 1:
  Product: ABC123
  Invoice Qty: 98 units
  PO Qty: 100 units
  Variance = |98-100|/100 × 100 = 2%
  Under-delivery: 2% (within 10% tolerance)
  Result: PASS ✅

Line Item 2:
  Product: XYZ789
  Invoice Qty: 115 units
  PO Qty: 100 units
  Variance = |115-100|/100 × 100 = 15%
  Over-delivery: 15% (exceeds 10% tolerance)
  Result: FAIL ❌ (Escalate)
```

**Kılavuz Referansı:** [PO Matching Complete Guide - Quantity](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity-comparison)

---

### Adım 6: Vergi Satırları Hizalamasını Kontrol Et

**Kart:** CONDITION_DOC_TO_PO_TAX_LINES

**Yapılandırma:**
```
Match Tax Codes: Yes
Match Tax Rates: Yes
Match Tax Amounts: With 1% tolerance
Tax Calculation: Verify recalculation
```

**Doğrulama:**
```
1. Check tax codes match (e.g., "VAT19" on both)
2. Check tax rates match (19% on both)
3. Verify tax amount calculation:
   Tax Amount = Net Amount × Tax Rate
4. Allow small rounding differences
```

**Örnek:**
```
Invoice:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

PO:
  Net Amount: €100.00
  Tax Rate: 19%
  Tax Amount: €19.00
  Total: €119.00

Result: Tax alignment PASS ✅
```

---

### Adım 7: Eşleştirme Sonuçlarını Depola

**Kart:** ACTION_SET_FIELD_TO_TEXT (birden fazla örnek)

**Yapılandırma:**

**Alan 1: PO_Match_Status**
```
Field: PO_Match_Status
Value: {{CALCULATED}}
Options: "FULL MATCH" | "WITHIN TOLERANCE" | "OUT OF TOLERANCE" | "NO MATCH"
```

**Alan 2: Price_Variance_Percent**
```
Field: Price_Variance_Percent
Value: {{CALCULATED_PRICE_VARIANCE}}
Format: "4.5%" (example)
```

**Alan 3: Quantity_Variance_Percent**
```
Field: Quantity_Variance_Percent
Value: {{CALCULATED_QUANTITY_VARIANCE}}
Format: "2.0%" (example)
```

**Alan 4: Match_Details**
```
Field: Match_Details
Value: "Price Variance: 4.5% (within 5% tolerance)\nQuantity Variance: 2.0% (within 10% tolerance)\nTotal: PASS"
```

**Kılavuz Referansı:** [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md)

---

### Adım 8: Eşleştirme Sonuçlarına Göre Yönlendir

**Senaryo A: Mükemmel Eşleşme (Full Match)**
```
IF PO_Match_Status = "FULL MATCH":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "FULL"
  3. ACTION_APPROVE_DOCUMENT
  4. Export to ERP
  5. Send confirmation email
  → END ✅
```

**Senaryo B: Tolerans İçinde**
```
IF PO_Match_Status = "WITHIN TOLERANCE":
  1. Set Approval_Status = "AUTO APPROVED"
  2. Set Match_Type = "TOLERANCE"
  3. Log variance details
  4. ACTION_APPROVE_DOCUMENT
  5. Export to ERP
  → END ✅
```

**Senaryo C: Tolerans Dışında (Küçük)**
```
IF Variance < 15% (minor exceptions):
  1. Set Match_Status = "REVIEW REQUIRED"
  2. Create Task: "Review PO Variance"
     - Assign to: Accounts Payable Officer
     - Priority: Medium
     - Deadline: 3 days
  3. Send email with variance details
  4. Wait for task completion
  5. IF Approved: Continue processing
     IF Rejected: Return to supplier
```

**Senaryo D: Tolerans Dışında (Büyük)**
```
IF Variance ≥ 15% (major exceptions):
  1. Set Match_Status = "ESCALATION REQUIRED"
  2. Create Task: "URGENT: Major PO Variance"
     - Assign to: Procurement Manager
     - Priority: High
     - Deadline: 1 day
  3. Send urgent email to:
     - Procurement Manager
     - Finance Manager
     - Supplier contact
  4. Block document from processing
  5. Wait for resolution
```

**Senaryo E: PO Eksik veya Eşleşme Yok**
```
IF PO not found OR no items match:
  1. Set Match_Status = "NO MATCH"
  2. Create Task: "PO Not Found"
     - Assign to: Procurement Team
     - Priority: High
  3. Send email to procurement
  4. Block document
  5. Request PO creation or correction
```

---

## Eksiksiz İş Akışı Diyagramı

```
INVOICE ARRIVES
│
├─ CHECK: Does invoice have PO number?
│  │
│  ├─ NO PO NUMBER ❌
│  │  │
│  │  ├─ Set Match_Status = "NO PO"
│  │  ├─ Route to Non-PO workflow
│  │  └─ Create manual review task
│  │     → END (Non-PO Invoice)
│  │
│  └─ PO NUMBER EXISTS ✅
│     │
│     ├─ RETRIEVE PO DATA
│     │  - Lookup PO by PO_Number
│     │  - Get PO line items
│     │  - Get PO totals
│     │  │
│     │  ├─ PO FOUND ✅
│     │  │  │
│     │  │  ├─ STEP 1: Check Full Match
│     │  │  │  Card: PURCHASE_ORDER_FULL_MATCH
│     │  │  │  │
│     │  │  │  ├─ FULL MATCH ✅✅✅
│     │  │  │  │  │
│     │  │  │  │  ├─ Set Match_Status = "FULL MATCH"
│     │  │  │  │  ├─ Auto-Approve
│     │  │  │  │  └─ Export to ERP
│     │  │  │  │     → END (Perfect Match)
│     │  │  │  │
│     │  │  │  └─ NO FULL MATCH ⚠️
│     │  │  │     │
│     │  │  │     ├─ STEP 2: Check Unit Price Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_UNIT_PRICE
│     │  │  │     │  Tolerance: 5%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Invoice-PO|/PO × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ PRICE VARIANCE ≤ 5% ✅
│     │  │  │     │  │  Store variance: 3.2% (example)
│     │  │  │     │  │  Price Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ PRICE VARIANCE > 5% ❌
│     │  │  │     │     Store variance: 12.5% (example)
│     │  │  │     │     Price Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 3: Check Quantity Variance
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_QUANTITY
│     │  │  │     │  Tolerance: 10%
│     │  │  │     │  │
│     │  │  │     │  ├─ Calculate for each line:
│     │  │  │     │  │  Variance % = |Inv Qty-PO Qty|/PO Qty × 100
│     │  │  │     │  │
│     │  │  │     │  ├─ QUANTITY VARIANCE ≤ 10% ✅
│     │  │  │     │  │  Store variance: 2.0% (example)
│     │  │  │     │  │  Quantity Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ QUANTITY VARIANCE > 10% ❌
│     │  │  │     │     Store variance: 15.0% (example)
│     │  │  │     │     Quantity Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ STEP 4: Check Tax Lines
│     │  │  │     │  Card: CONDITION_DOC_TO_PO_TAX_LINES
│     │  │  │     │  │
│     │  │  │     │  ├─ TAX ALIGNED ✅
│     │  │  │     │  │  Tax Check: PASS
│     │  │  │     │  │
│     │  │  │     │  └─ TAX MISMATCH ❌
│     │  │  │     │     Tax Check: FAIL
│     │  │  │     │     → Flag for review
│     │  │  │     │
│     │  │  │     ├─ EVALUATE RESULTS
│     │  │  │     │  │
│     │  │  │     │  ├─ ALL CHECKS PASS ✅
│     │  │  │     │  │  (Within tolerance)
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "WITHIN TOLERANCE"
│     │  │  │     │  │  ├─ Log variance details
│     │  │  │     │  │  ├─ Auto-Approve
│     │  │  │     │  │  └─ Export to ERP
│     │  │  │     │  │     → END (Approved with Variance)
│     │  │  │     │  │
│     │  │  │     │  ├─ MINOR FAILURES (Variance < 15%) ⚠️
│     │  │  │     │  │  │
│     │  │  │     │  │  ├─ Set Match_Status = "REVIEW REQUIRED"
│     │  │  │     │  │  ├─ Create Review Task
│     │  │  │     │  │  │  - Assign to: AP Officer
│     │  │  │     │  │  │  - Priority: Medium
│     │  │  │     │  │  │  - Deadline: 3 days
│     │  │  │     │  │  ├─ Send email with details
│     │  │  │     │  │  │
│     │  │  │     │  │  └─ WAIT FOR TASK COMPLETION
│     │  │  │     │  │     │
│     │  │  │     │  │     ├─ TASK APPROVED ✅
│     │  │  │     │  │     │  Approve & Export
│     │  │  │     │  │     │  → END (Manual Approval)
│     │  │  │     │  │     │
│     │  │  │     │  │     └─ TASK REJECTED ❌
│     │  │  │     │  │        Reject & Return to Supplier
│     │  │  │     │  │        → END (Rejected)
│     │  │  │     │  │
│     │  │  │     │  └─ MAJOR FAILURES (Variance ≥ 15%) 🚨
│     │  │  │     │     │
│     │  │  │     │     ├─ Set Match_Status = "ESCALATION"
│     │  │  │     │     ├─ Create Urgent Task
│     │  │  │     │     │  - Assign to: Procurement Manager
│     │  │  │     │     │  - Priority: High
│     │  │  │     │     │  - Deadline: 1 day
│     │  │  │     │     ├─ Send urgent emails to:
│     │  │  │     │     │  * Procurement Manager
│     │  │  │     │     │  * Finance Manager
│     │  │  │     │     │  * Supplier
│     │  │  │     │     ├─ Block document processing
│     │  │  │     │     │
│     │  │  │     │     └─ WAIT FOR RESOLUTION
│     │  │  │     │        → END (Pending Escalation)
│     │  │  │     │
│     │  │  │     └─ [Variance checks complete]
│     │  │  │
│     │  │  └─ [Full match check complete]
│     │  │
│     │  └─ PO NOT FOUND ❌
│     │     │
│     │     ├─ Set Match_Status = "PO NOT FOUND"
│     │     ├─ Create Task: "Missing PO"
│     │     │  - Assign to: Procurement Team
│     │     │  - Priority: High
│     │     ├─ Send email to procurement
│     │     └─ Block document
│     │        → END (Missing PO)
│     │
│     └─ [PO retrieval complete]
│
└─ [PO check complete]
```

---

## Yapılandırma Şablonları

### Şablon 1: Standart PO Eşleştirme (Muhafazakar)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 3,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": false
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": true,
    "match_tax_rates": true,
    "tax_amount_tolerance": 0.5
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 10,
    "assign_to": "procurement_manager"
  }
}
```

**Kullanım:** Sıkı kontrol ortamı, sapmaya düşük tolerans

---

### Şablon 2: Esnek PO Eşleştirme (Hoşgörülü)

```json
{
  "full_match_check": true,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 10,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": true,
    "tolerance_percent": 15,
    "tolerance_type": "percentage",
    "allow_under_delivery": true,
    "allow_over_delivery": true
  },
  "tax_validation": {
    "enabled": true,
    "match_tax_codes": false,
    "match_tax_rates": true,
    "tax_amount_tolerance": 2
  },
  "auto_approve": {
    "full_match": true,
    "within_tolerance": true
  },
  "escalation": {
    "threshold_percent": 20,
    "assign_to": "accounts_payable"
  }
}
```

**Kullanım:** Esnek ortam, güvenilir tedarikçiler, daha yüksek tolerans

---

### Şablon 3: Yalnızca Fiyat Eşleştirme

```json
{
  "full_match_check": false,
  "price_variance": {
    "enabled": true,
    "tolerance_percent": 5,
    "tolerance_type": "percentage"
  },
  "quantity_variance": {
    "enabled": false
  },
  "tax_validation": {
    "enabled": false
  },
  "auto_approve": {
    "full_match": false,
    "within_tolerance": true
  }
}
```

**Kullanım:** Yalnızca fiyatın önemli olduğu, miktar değişimlerinin beklendiği durumlar

---

## Gelişmiş Senaryolar

### Senaryo 1: Kısmi Teslimat Yönetimi

**Zorluk:** Kısmi PO teslimatı için fatura

**Çözüm:**
```
1. Allow quantity under-delivery within tolerance
2. Track cumulative invoiced quantity vs PO quantity
3. Update PO remaining quantity
4. Create field: "PO_Percentage_Invoiced"
5. When 100% invoiced: Close PO automatically
```

**Uygulama:**
```
IF Cumulative_Invoiced_Quantity ≤ PO_Quantity:
  Calculate: Percentage = (Cumulative/PO) × 100
  Store in: PO_Percentage_Invoiced
  IF Percentage ≥ 100:
    Set PO_Status = "FULLY INVOICED"
    Close PO
```

---

### Senaryo 2: Çoklu Para Birimi PO Eşleştirme

**Zorluk:** Fatura para birimi PO para biriminden farklı

**Çözüm:**
```
1. Detect currency mismatch
2. Get exchange rate (from API or master data)
3. Convert invoice amount to PO currency
4. Compare converted amounts
5. Store both original and converted amounts
```

**Uygulama:**
```
IF Invoice_Currency ≠ PO_Currency:
  1. Get exchange rate for Invoice_Currency → PO_Currency
  2. Convert: Invoice_Amount_Converted = Invoice_Amount × Rate
  3. Compare: Invoice_Amount_Converted vs PO_Amount
  4. Store: Original_Currency_Amount and Converted_Amount
  5. Flag: "Currency_Conversion_Applied"
```

---

### Senaryo 3: Genel PO / Çerçeve Anlaşması

**Zorluk:** Tek bir PO'ya karşı birden fazla fatura

**Çözüm:**
```
1. Identify PO type = "Blanket"
2. Track cumulative invoiced value
3. Check: Cumulative ≤ Blanket PO Total
4. Update remaining PO value after each invoice
5. Alert when approaching PO limit
```

**Uygulama:**
```
IF PO_Type = "Blanket":
  Calculate: Total_Invoiced_To_Date
  Check: Total_Invoiced_To_Date + Current_Invoice ≤ PO_Total_Value
  IF Within limit:
    Approve invoice
    Update: Remaining_PO_Value
  ELSE:
    Escalate: "Blanket PO limit exceeded"
```

---

## Hata Yönetimi ve Sınır Durumları

### Sınır Durumu 1: Faturada Eksik Satır Öğesi

**Sorun:** Faturada PO'da olmayan bir öğe var

**Çözüm:**
```
1. Identify unmatched line items
2. Calculate: Unmatched_Amount
3. IF Unmatched_Amount < €100 (threshold):
     Create review task (minor issue)
   ELSE:
     Escalate immediately (major issue)
4. Store unmatched item details
5. Flag: "Additional_Items_Present"
```

---

### Sınır Durumu 2: PO Kapatılmış ama Fatura Geliyor

**Sorun:** PO zaten kapatılmış, geç fatura alındı

**Çözüm:**
```
1. Check: PO_Status = "CLOSED"
2. Check: Invoice_Date vs PO_Close_Date
3. IF Invoice within 30 days of close:
     Reopen PO temporarily
     Process invoice
     Close PO again
   ELSE:
     Create task: "Late Invoice for Closed PO"
     Assign to procurement
     Manual decision required
```

---

### Sınır Durumu 3: Tek Faturada Birden Fazla PO

**Sorun:** Fatura birden fazla PO'ya başvuruyor

**Çözüm:**
```
1. Parse invoice for multiple PO numbers
2. For each PO:
     Retrieve PO data
     Match respective line items
3. Aggregate match results
4. Overall match = ALL individual POs must match
5. Report on each PO separately
```

---

## Performans İpuçları

✅ **En İyi Uygulamalar:**
- Aramaları azaltmak için PO verilerini önbelleğe alın
- Uygun toleranslar ayarlayın (çok sıkı değil, çok hoşgörülü değil)
- Önce tam eşleştirme kontrolü kullanın (daha hızlı)
- Tüm sapma hesaplamalarını günlüğe kaydedin
- Tolerans ayarlarını üç ayda bir gözden geçirin
- Otomatik onay oranlarını izleyin
- Yaygın sapma nedenlerini izleyin

❌ **Kaçının:**
- Sıfır tolerans (çok sıkı, çok fazla manuel inceleme)
- Aşırı yüksek tolerans (amacı boşa çıkarır)
- Sistematik sapmaları görmezden gelme
- Sapma eğilimlerini izlememe
- PO olmadan işleme (gerekli olduğunda)

---

## İzleme ve Raporlama

### İzlenecek Temel Metrikler

1. **Eşleştirme Oranı:**
   - Tam Eşleşme: X%
   - Tolerans İçinde: Y%
   - Tolerans Dışında: Z%

2. **Sapma Analizi:**
   - Ortalama fiyat sapması
   - Ortalama miktar sapması
   - Yaygın sapma nedenleri

3. **İşleme Verimliliği:**
   - Otomatik onay oranı
   - Manuel inceleme oranı
   - Ortalama inceleme süresi

4. **Tedarikçi Performansı:**
   - Tedarikçiye göre sapmalar
   - Tedarikçiye göre eşleştirme oranı
   - Sorunlu tedarikçiler

---

## Test Kontrol Listesi

- [ ] Mükemmel eşleşme senaryosu (full match)
- [ ] Tolerans içinde senaryosu (küçük sapma)
- [ ] Tolerans dışında senaryosu (büyük sapma)
- [ ] PO eksik senaryosu
- [ ] Yanlış PO numarası senaryosu
- [ ] Kısmi teslimat senaryosu
- [ ] Fazla teslimat senaryosu
- [ ] Para birimi uyuşmazlığı senaryosu
- [ ] Birden fazla PO senaryosu
- [ ] Kapatılmış PO senaryosu
- [ ] Vergi sapması senaryosu
- [ ] Yükseltme iş akışı
- [ ] Görev oluşturma
- [ ] E-posta bildirimleri
- [ ] Alan güncellemeleri
- [ ] Onaydan sonra dışa aktarma

---

## İlgili Kalıplar

### İyi Birlikte Çalışan Kalıplar:

- **[Task Management Pattern](task-management-pattern.md)** - Sapmalar için inceleme görevleri oluşturma
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Sapma düzeylerine göre karmaşık yönlendirme
- **[API Integration Pattern](api-integration-pattern.md)** - Karşılaştırma için güncel fiyatlandırma alma
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Para birimi dönüşümü, birim dönüşümü

---

## İlgili Kılavuzlar

### Önkoşullar
- [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md) - Tüm PO eşleştirme kartları
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Koşul mantığı
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Alan işlemleri

### İlgili Kartlar
- **PURCHASE_ORDER_FULL_MATCH** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#full-match)
- **CONDITION_DOC_TO_PO_UNIT_PRICE** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#unit-price)
- **CONDITION_DOC_TO_PO_QUANTITY** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#quantity)
- **CONDITION_DOC_TO_PO_TAX_LINES** - [PO Matching Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#tax-lines)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Sonraki Adımlar
- İnceleme görevleri oluşturun: [Task Management Pattern](task-management-pattern.md)
- E-posta bildirimleri ekleyin: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Karmaşık yönlendirme uygulayın: [Decision Logic Pattern](decision-logic-pattern.md)

---

**Kalıp Sürümü:** 1.0
**Son Güncelleme:** 23 Ekim 2025
**Zorluk:** Orta-Yüksek
**Tahmini Süre:** 60-90 dakika
**Başarı Oranı:** Yüksek (düzgün yapılandırıldığında)

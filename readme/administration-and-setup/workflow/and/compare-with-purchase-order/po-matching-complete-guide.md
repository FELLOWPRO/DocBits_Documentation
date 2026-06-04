# Satınalma Siparişi (PO) Eşleştirme Kartları - Eksiksiz Kılavuz

**Durum:** Ayrıntılı hesaplamalarla 15 PO karşılaştırma kartını kapsar

---

Bu sayfadaki PO karşılaştırma kartları, Workflow Builder'ın **And** grubuna gider — Then eylemleri çalışmadan önce fatura verilerini eşleştirilen satınalma siparişiyle karşılaştırırlar:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p>PO karşılaştırma kartları <strong>And</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**En Çok Geliştirilen Kart:** CONDITION_DOC_TO_PO_UNIT_PRICE (5 sürüm, v5 en yeni)
**Diğer Karmaşık Kartlar:** CONDITION_OC_TO_PO_ITEMS (v4), CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v4)

**Temel Kalıplar:**
- **v2 → v3+:** Esnek eşleştirme için tolerans parametrelerinin eklenmesi
- **v3 → v4:** Karşılaştırma modu parametrelerinin eklenmesi
- **v4 → v5:** Birden fazla birimle (%, EUR, $, vb.) gelişmiş tolerans

📖 [Eksiksiz Sürüm Geçmişi](../../../changelog/release.md#-po-comparison--validation-cards) | [Kart Sürüm Veritabanı](../../../../DocFlow/docs/card_version.md)

---

## PO Eşleştirmeyi Anlamak

Bir fatura aldığınızda, daha önce verilen Satınalma Siparişi (PO) ile eşleşmelidir. PO eşleştirme kartları, fatura verilerinin PO verileriyle eşleşip eşleşmediğini otomatik olarak kontrol eder.

**Genel Resim:**
```
PO Placed     Invoice Arrives     PO Matching     Decision
(€100)    →   (€103)          →   (Check if       → Approve/Reject
Qty: 100      Qty: 100            within tolerance)
```

---

# 1. Satınalma Siparişi Tam Eşleşme (Full Match)

## Amaç
Tüm faturanın PO ile mükemmel veya tolerans içinde eşleşip eşleşmediğini kontrol eder

## Ne Zaman Kullanılır
- Bir faturayı onaylamadan önce
- Ön kalite kontrolü olarak
- Sorunları erken belirlemek için

## Nasıl Çalışır
Sistem şunları karşılaştırır:
- Fatura miktarları vs PO miktarları
- Fatura fiyatları vs PO fiyatları
- Fatura öğeleri vs PO öğeleri
- Fatura toplamı vs PO toplamı

## Sonuç
- **TRUE** (Tam Eşleşme): Her şey eşleşir, devam et
- **FALSE** (Uyuşmazlık): Bir şey eşleşmiyor, inceleme gerekiyor

## Örnek
```
PO:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Invoice:
- Item ABC: Qty 100, Unit Price €50 = €5000
- Item XYZ: Qty 50, Unit Price €20 = €1000
- Total: €6000

Result: ✅ FULL MATCH
```

---

# 2. Birim Fiyat Karşılaştırması (Belge vs PO)

## Amaç
Faturadaki birim fiyatı PO'daki birim fiyatla karşılaştırır

## Parametreler
- **Birim Fiyat Toleransı**: Bu miktara kadar sapmaya izin ver
- **Tolerans Türü**: Yüzde (%) veya Mutlak (€/$)
- **Operatör**: Eşittir, Büyüktür, Küçüktür vb.

## Nasıl Çalışır (Yüzde Toleransı)

**Formül:**
```
Variance % = |(Invoice Price - PO Price)| / PO Price × 100

Check: Is Variance % ≤ Tolerance %?
```

**Adım Adım Örnek:**
```
Step 1: Get prices
  PO Unit Price: €100.00
  Invoice Unit Price: €103.00

Step 2: Calculate difference
  Difference = |€103.00 - €100.00| = €3.00

Step 3: Calculate percentage
  Percentage = (€3.00 / €100.00) × 100 = 3%

Step 4: Check tolerance (5% allowed)
  Is 3% ≤ 5%? YES ✅

Result: PASS - Within tolerance
```

## Gerçek Dünya Örnekleri

### Örnek 1: Küçük Artış (Kabul Edildi)
```
PO Price: €50.00
Invoice Price: €51.50
Tolerance: ±3%

Calculation:
  Variance = |(€51.50 - €50.00)| / €50.00 × 100
  Variance = €1.50 / €50.00 × 100 = 3%

Is 3% ≤ 3%? YES ✅ ACCEPT
```

### Örnek 2: Büyük Artış (Reddedildi)
```
PO Price: €50.00
Invoice Price: €55.00
Tolerance: ±3%

Calculation:
  Variance = |(€55.00 - €50.00)| / €50.00 × 100
  Variance = €5.00 / €50.00 × 100 = 10%

Is 10% ≤ 3%? NO ❌ REJECT - NEEDS REVIEW
```

### Örnek 3: İndirim (Bu da Kontrol Edilir)
```
PO Price: €100.00
Invoice Price: €97.00
Tolerance: ±5%

Calculation:
  Variance = |(€97.00 - €100.00)| / €100.00 × 100
  Variance = €3.00 / €100.00 × 100 = 3%

Is 3% ≤ 5%? YES ✅ ACCEPT (Discount is within tolerance)
```

### Örnek 4: Mutlak Değer Toleransı
```
PO Price: €10.00
Invoice Price: €10.50
Tolerance: ±€1.00 (absolute, not %)

Calculation:
  Variance = |€10.50 - €10.00| = €0.50

Is €0.50 ≤ €1.00? YES ✅ ACCEPT
```

## Sonuçlarla Ne Yapmalı

**PASS ✅ ise:**
- Bir sonraki kontrole devam et
- Veya faturayı onayla
- Veya dışa aktarmayla devam et

**FAIL ❌ ise:**
- Manuel inceleme için işaretle
- Tedarikçiden açıklama iste
- Satınalma ekibiyle iletişime geç
- Kabul edilebilirse notla onayla

---

# 3. Miktar Karşılaştırması

## Amaç
Sipariş edilen miktarın fatura edilen miktarla eşleşip eşleşmediğini kontrol eder

## Parametreler
- **Tolerans**: Farklılaşmasına izin verilen miktar veya %
- **Operatör**: Eşittir, Büyüktür, Küçüktür
- **Miktar Türü**: Sipariş Edilen, Teslim Alınan, Açık

## Hesaplama Örneği

**Yüzde Toleransı:**
```
Formula:
  Quantity Variance % = |(Invoice Qty - PO Qty)| / PO Qty × 100

Example:
  PO Quantity: 100 units
  Invoice Quantity: 103 units
  Tolerance: ±5%

  Variance = |(103 - 100)| / 100 × 100
  Variance = 3 / 100 × 100 = 3%

  Is 3% ≤ 5%? YES ✅ ACCEPT
```

**Mutlak Tolerans:**
```
Formula:
  Quantity Variance = |Invoice Qty - PO Qty|

Example:
  PO Quantity: 100 units
  Invoice Quantity: 102 units
  Tolerance: ±5 units

  Variance = |102 - 100| = 2 units

  Is 2 units ≤ 5 units? YES ✅ ACCEPT
```

## Gerçek Dünya Senaryoları

### Fazla Teslimat (Sipariş Edilenden Fazla)
```
Ordered: 100 units
Invoiced: 110 units
Tolerance: ±5%

Variance = |(110-100)|/100 × 100 = 10%

Is 10% ≤ 5%? NO ❌

Decision: Contact supplier - more delivered than ordered
Possible reason: Error by supplier, partial shipment already received
```

### Eksik Teslimat (Sipariş Edilenden Az)
```
Ordered: 100 units
Invoiced: 95 units
Tolerance: ±5%

Variance = |(95-100)|/100 × 100 = 5%

Is 5% ≤ 5%? YES ✅

Decision: Accept - within tolerance
Possible reason: Partial shipment, rest to follow
```

---

# 4. Miktar Farkının Birleşik Fiyatı

## Amaç
Miktar farklı olduğunda, toplam fiyat farkının kabul edilebilir olup olmadığını hesaplar

## Bu Neden Önemli
```
Scenario: You ordered 100 units but received 110
- Quantity is 10% over (bad)
- BUT: You're only charged for 10% extra
- Combined effect might be acceptable
```

## Hesaplama

**Formül:**
```
Combined Variance = Quantity Variance × Price Variance

If both are within tolerance, combined is usually acceptable
```

**Örnek:**
```
PO:
- Unit Price: €100
- Quantity: 100
- Total: €10,000

Invoice:
- Unit Price: €102 (2% higher)
- Quantity: 105 (5% higher)
- Total: €10,710

Analysis:
- Price variance: 2% ✅
- Quantity variance: 5% ✅
- Combined effect: 1.02 × 1.05 = 1.071 = 7.1% total increase

Is combined variance acceptable? Usually YES ✅
```

---

# 5. Öğe Kimliği / Tedarikçi Öğe Numarası Karşılaştırması

## Amaç
Faturadaki öğelerin PO'daki öğelerle eşleşip eşleşmediğini kontrol eder

## Nasıl Çalışır

**Tam Eşleşme (En Basit):**
```
PO Item ID: ABC-123
Invoice Item ID: ABC-123
Result: ✅ MATCH
```

**Tedarikçi Öğe Numarası (Daha Yaygın):**
```
PO Item: ABC-123 (Our internal code)
Supplier Item: SUPP-456 (Their code for same item)
System matches these as same item
Result: ✅ MATCH
```

## Senaryo: Eşleşmezse Ne Olur?

```
PO Item: ABC-123 (Copper Wire, 2mm)
Invoice Item: ABC-124 (Steel Wire, 2mm)

Result: ❌ NO MATCH

Actions:
1. Is this a substitution? Check with procurement
2. Is this an error? Contact supplier
3. Is the description similar? Verify manually
```

---

# 6. Sipariş Türü Doğrulaması

## Amaç
Satınalma siparişi türünün doğru olduğunu doğrular

## Sipariş Türleri
- **Standard Order**: Normal satın alma
- **Rush Order**: Acil, prim olabilir
- **Frame Agreement**: Uzun vadeli sözleşme
- **Blanket Order**: Açık uçlu sözleşme
- **Consignment**: Kullanılana kadar ödeme yapmazsınız

## Kontrol Örneği
```
PO Order Type: Standard Order
Invoice Order Type: Standard Order
Result: ✅ MATCH

If mismatch: Could affect terms, payment, pricing
```

---

# 7. Teslimat Tarihi Doğrulaması

## Amaç
Teslimat tarihinin PO'daki vaat edilen tarihle eşleşip eşleşmediğini kontrol eder

## Hesaplama

**Geç Teslimat:**
```
Formula:
  Days Late = Invoice Delivery Date - PO Promised Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-22
  Days Late = 7 days

If tolerance is ±3 days:
  Is 7 ≤ 3? NO ❌ LATE
```

**Erken Teslimat:**
```
Formula:
  Days Early = PO Promised Date - Invoice Delivery Date

Example:
  PO Promised: 2025-10-15
  Actual Delivery: 2025-10-10
  Days Early = 5 days

Early delivery is usually OK ✅
Unless you need it at specific time
```

## Tolerans Ayarları
```
±3 days: Allow 3 days late or early
±5 days: Allow up to 5 days variance
0 days: Must match exactly
```

---

# 8. Ücret Doğrulaması (Vergiler, Nakliye vb.)

## Amaç
Ek ücretlerin (vergiler, nakliye, işleme) PO ile eşleşip eşleşmediğini kontrol eder

## Yaygın Ücretler
```
- Shipping: €50
- Handling: €10
- Packaging: €5
- Insurance: €15
- Taxes: €300
```

## Hesaplama

**Örnek: Nakliye Ücreti Kontrolü**
```
PO Shipping: €50.00
Invoice Shipping: €51.00
Tolerance: ±3%

Variance = |€51.00 - €50.00| / €50.00 × 100 = 2%

Is 2% ≤ 3%? YES ✅ ACCEPT
```

**Örnek: Birden Fazla Ücret**
```
PO Total Charges:
  - Shipping: €50
  - Taxes: €300
  - Handling: €10
  Total: €360

Invoice Total Charges:
  - Shipping: €50
  - Taxes: €312 (11% tax)
  - Handling: €10
  Total: €372

Difference: €12
Check if within tolerance ✅ or ❌
```

---

# 9. Vergi Doğrulaması

## Amaç
Vergi tutarlarının doğru hesaplandığını doğrular

## Hesaplama

**Formül:**
```
Tax Amount = Subtotal × Tax Rate

Example:
  Subtotal: €1000
  Tax Rate: 19%
  Expected Tax: €1000 × 0.19 = €190

Invoice Tax: €190
Match? YES ✅
```

**Yaygın Sorunlar:**
```
1. Tax rate changed (region-based)
2. Tax applied to wrong amount (before/after discounts)
3. Multiple tax rates (some items 7%, others 19%)
4. Tax exempt items (0% tax)
```

**Örnek: Çoklu Oranlı Vergilendirme**
```
Item A: €100 @ 19% tax = €119
Item B: €100 @ 7% tax = €107
Item C: €100 @ 0% tax = €100
Total: €326

Invoice shows €325 (€1 error)

Check: Within tolerance or needs attention?
```

---

# 10. Tesis/Maliyet Merkezi Eşleştirmesi

## Amaç
Faturanın doğru tesis/maliyet merkezi için olduğundan emin olur

## Örnek
```
PO is for:
- Facility: Berlin Plant
- Cost Center: CC-2025

Invoice should have:
- Facility: Berlin Plant ✅
- Cost Center: CC-2025 ✅

If different facility: May need different approval
```

---

# 11. Tedarikçi Durumu Doğrulaması

## Amaç
Tedarikçinin hâlâ onaylı/etkin olup olmadığını kontrol eder

## Durum Türleri
```
✅ ACTIVE: Approved, can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

## Kontrol Örneği
```
Supplier: ABC Corp
Status in Database: ACTIVE
Status when creating PO: ACTIVE
Status when invoice arrives: INACTIVE

Alert: Supplier status changed! Investigate why.
```

---

# Hangi Toleransı Kullanmalıyım?

## Sıkı Toleranslar (Daha Düşük Risk, Daha Fazla Manuel İş)
```
Use for:
- High-value items
- Items where exactness matters
- Regulated industries

Settings:
- Unit Price: ±1%
- Quantity: ±1%
- Delivery Date: ±1 day
- Charges: ±1%
```

## Orta Toleranslar (Dengeli)
```
Use for:
- Most business transactions
- Standard items
- Normal purchasing

Settings:
- Unit Price: ±3-5%
- Quantity: ±3-5%
- Delivery Date: ±3 days
- Charges: ±5%
```

## Gevşek Toleranslar (Daha Yüksek Risk, Daha Az Manuel İş)
```
Use for:
- Low-value items
- Bulk purchases
- Supplier agreements with flexibility

Settings:
- Unit Price: ±10%
- Quantity: ±10%
- Delivery Date: ±7 days
- Charges: ±10%
```

---

# PO Eşleştirme İş Akışı Örneği

```
Invoice Arrives
    ↓
Condition: "Is amount > €5000?" → YES
    ↓
Check: Full Match? → NO (10% price difference)
    ↓
Check: Unit Price within 5%? → NO (12% difference)
    ↓
Check: Quantity within 5%? → YES (2% difference)
    ↓
Decision: FAIL - Price variance too high
    ↓
Flag for: Manual review / Buyer approval
    ↓
Wait for: Buyer comment
    ↓
If Approved: Continue to Export
If Rejected: Return to Supplier
```

---

# PO Eşleştirme Sorun Giderme

## "PO Not Found"
```
Cause: Invoice PO number doesn't exist in system
Fix:
1. Verify PO number spelling
2. Check if PO was created
3. Verify PO is in correct organization
4. Ask supplier for PO reference
```

## "Items Don't Match"
```
Cause: Invoice items are different from PO items
Possible Reasons:
1. Substitution approved by procurement
2. Different item numbers for same item
3. Error by supplier
Fix: Contact procurement or supplier
```

## "Price Higher Than PO"
```
Cause: Invoice price > PO price
Possible Reasons:
1. Price increase approved
2. Supplier error
3. Currency difference
4. Additional services included
Fix: Verify with procurement
```

## "Delivery Date Wrong"
```
Cause: Invoice dated after promised delivery
Possible Reasons:
1. Shipment was delayed
2. Receiving date different from invoice date
3. Partial shipment
Fix: Check shipping documents or contact supplier
```

---

# Özet Tablosu

| Kart | Neyi Kontrol Eder | Ana Hesaplama | Yaygın Tolerans |
|------|----------------|------------------|-----------------|
| Full Match | Her şey | Tüm kontroller | Değişir |
| Unit Price | Birim başına fiyat | % veya € farkı | ±3-5% |
| Quantity | Sipariş edilen miktar | % veya birim farkı | ±3-5% |
| Combined Price | Miktar değişimiyle toplam | Adet × Fiyat | ±5-10% |
| Item ID | Doğru öğeler | Dize eşleşmesi | Tam |
| Order Type | Satın alma türü | Dize eşleşmesi | Tam |
| Delivery Date | Ne zaman geldi | Gün farkı | ±3 gün |
| Charges | Ek ücretler | % veya € farkı | ±5% |
| Tax | Vergi tutarı | Vergi % hesaplaması | ±1% |
| Facility | Maliyet merkezi | Dize eşleşmesi | Tam |
| Supplier | Onaylı mı? | Durum kontrolü | Yalnızca etkin |

---

# İlgili Belgeler

- Eksiksiz iş akışı için "Invoice Validation" kılavuzuna bakın
- Sektöre göre önerilen değerler için "Tolerance Settings"e bakın
- Hatalarla ne yapılacağı için "Exception Handling"e bakın
- Belirli tolerans politikaları için satınalma ekibinizle iletişime geçin

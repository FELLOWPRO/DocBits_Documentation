# API Integration Pattern

**Kalıp Türü:** Entegrasyon
**Karmaşıklık:** Orta
**Tahmini Kurulum:** 45-60 dakika
**Yaygın Kullanım Durumları:** Harici veri alma, fiyatlandırma doğrulama, ana veri araması

---

Bu kalıbı **Workflow Builder**'da (Workflow Dashboard → Workflow List → Add Workflow) oluşturursunuz. Kart kütüphanesini açmak için **Add Card**'a tıklayın ve bu kalıbın kullandığı kartları seçin — `CALL_API`, `CONDITION_HTTPS_REQUEST_STATUS`, `ACTION_SET_FIELD_TO_TEXT` ve `CONDITION_COMPARE_TWO_DOCFIELD_VALUES`:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder'da kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — bu kalıbın kullandığı API, koşul ve alan kartlarını bu kategorilerden seçin.</p></figcaption></figure>

---

## Kalıp Genel Bakışı

Bu kalıp, DocBits'i harici sistemlerden veri almak, doğrulamak ve depolamak için harici API'lerle nasıl entegre edeceğinizi gösterir. DocBits'i fiyatlandırma sistemlerine, doğrulama servislerine, ERP sistemlerine ve diğer harici veri kaynaklarına bağlamak için en yaygın iş akışı kalıplarından biridir.

**Bu Kalıbın Yaptıkları:**
1. Veri almak için harici bir API çağırır
2. API yanıtını doğrular
3. Yanıt verilerini belge alanlarında depolar
4. Alınan verilere göre kararlar verir
5. Belgeleri buna göre yönlendirir

---

## Bu Kalıbı Ne Zaman Kullanmalı

Bu kalıbı şu durumlarda kullanın:
- ✅ Harici sistemlerden gerçek zamanlı fiyatlandırma alma
- ✅ Tedarikçi bilgilerini ana veritabanına karşı doğrulama
- ✅ Katalog sistemlerinden ürün ayrıntılarını arama
- ✅ Para birimi servislerinden döviz kurları alma
- ✅ Adresleri coğrafi kodlama servisleriyle doğrulama
- ✅ Depo sistemlerinden stok seviyelerini kontrol etme
- ✅ Vergi servislerinden vergi oranlarını doğrulama

**Bu kalıbı şu durumlarda kullanmayın:**
- ❌ Veri zaten DocBits ana verisindeyse (bunun yerine ana veri aramasını kullanın)
- ❌ Harici sistemin API'si yoksa (bunun yerine DocOperator Script kalıbını kullanın)
- ❌ Veri sık değişmiyorsa (manuel içe aktarmayı düşünün)

---

## Eksiksiz İş Akışı Örneği

### Senaryo: Fatura Fiyatını Güncel Fiyatlandırma API'sine Karşı Doğrulama

**İş Gereksinimi:**
- Tedarikçi fatura gönderir
- Fatura €52.00 birim fiyat gösterir
- Bunun güncel tedarikçi fiyatlandırmasıyla eşleştiğini doğrulamamız gerekir
- Fiyat %5'ten fazla değişirse, inceleme için yükselt

**Kullanılan İş Akışı Kartları:**
1. CALL_API - Tedarikçi API'sinden güncel fiyatı al
2. CONDITION_HTTPS_REQUEST_STATUS - API çağrısının başarılı olup olmadığını kontrol et
3. ACTION_SET_FIELD_TO_TEXT - API fiyatını belge alanında depola
4. CONDITION_COMPARE_TWO_DOCFIELD_VALUES - Fatura fiyatını API fiyatıyla karşılaştır
5. ACTION_ASSIGN_TO_USER - Karşılaştırma sonucuna göre yönlendir
6. tasks_create - Gerekirse inceleme görevi oluştur

---

## Adım Adım Uygulama

### Adım 1: Harici API'yi Çağır

**Kart:** CALL_API veya ACTION_CALL_EXTERNAL_API

**Yapılandırma:**
```json
{
  "api_endpoint": "https://api.supplier-system.com/v1/pricing",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
  },
  "request_body": {
    "product_id": "{{DOCUMENT_FIELD:Product_Code}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "quantity": "{{DOCUMENT_FIELD:Quantity}}",
    "currency": "EUR"
  }
}
```

**Beklenen Yanıt:**
```json
{
  "success": true,
  "data": {
    "product_id": "ABC123",
    "unit_price": 50.00,
    "currency": "EUR",
    "valid_until": "2025-12-31",
    "discount_applicable": true
  }
}
```

**Kılavuz Referansı:** [Call API Guide](../then/action/call-api-guide.md)

---

### Adım 2: API Yanıtını Doğrula

**Kart:** CONDITION_HTTPS_REQUEST_STATUS

**Yapılandırma:**
```
Operator: IS EQUAL TO
Status Code: 200
```

**Mantık:**
```
IF API returns 200 (success):
  → Continue to store data
ELSE:
  → Route to "API Error" handling workflow
  → Send email notification
  → Create manual review task
```

**Kılavuz Referansı:** [Condition Cards Guide - HTTP Status](../and/condition-cards-complete-guide.md#condition-https-request-status)

---

### Adım 3: API Yanıtını Belge Alanlarında Depola

**Kart:** ACTION_SET_FIELD_TO_TEXT (veya eşdeğer alan ayarlayıcı)

**Yapılandırma:**

**Alan 1: Current_API_Price**
```
Field Name: Current_API_Price
Field Value: {{API_RESPONSE:data.unit_price}}
Field Type: Number
```

**Alan 2: API_Price_Valid_Until**
```
Field Name: API_Price_Valid_Until
Field Value: {{API_RESPONSE:data.valid_until}}
Field Type: Date
```

**Alan 3: API_Discount_Available**
```
Field Name: API_Discount_Available
Field Value: {{API_RESPONSE:data.discount_applicable}}
Field Type: Boolean
```

**Sonuç:** API'den gelen veri artık daha sonra kullanılmak üzere belge alanlarında depolanmıştır

**Kılavuz Referansı:** [Field Manipulation Guide - API Data Storage](../then/document-field/field-manipulation-guide.md#storing-api-data)

---

### Adım 4: Fatura Fiyatını API Fiyatıyla Karşılaştır

**Kart:** CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**Yapılandırma:**
```
Field 1: Invoice_Unit_Price (from OCR extraction)
Field 2: Current_API_Price (from API response)
Operator: Calculate variance percentage
Tolerance: 5%
```

**Hesaplama:**
```
Variance % = |(Invoice_Price - API_Price)| / API_Price × 100

Example:
  Invoice Price: €52.00
  API Price: €50.00
  Variance = |52 - 50| / 50 × 100 = 4%

  Is 4% ≤ 5% tolerance? YES ✅
  Result: PASS
```

**Kılavuz Referansı:** [Condition Cards Guide - Field Comparison](../and/condition-cards-complete-guide.md#field-comparison)

---

### Adım 5: Doğrulama Sonucuna Göre Yönlendir

**Senaryo A: Fiyat Tolerans İçinde (Geçti)**

**Kartlar:**
- ACTION_SET_FIELD_TO_TEXT
  - "Price_Validation_Status" alanını = "PASS" olarak ayarla
  - "Price_Variance_Percent" alanını = "4%" olarak ayarla
- ACTION_APPROVE_DOCUMENT
  - Belgeyi otomatik onayla

**Senaryo B: Fiyat Tolerans Dışında (Kaldı)**

**Kartlar:**
- ACTION_SET_FIELD_TO_TEXT
  - "Price_Validation_Status" alanını = "FAIL" olarak ayarla
  - "Price_Variance_Percent" alanını = "12%" olarak ayarla (örnek)
- tasks_create
  - Task Title: "Review Price Variance - {{DOCUMENT_NUMBER}}"
  - Task Description: "Invoice price (€{{Invoice_Unit_Price}}) exceeds API price (€{{Current_API_Price}}) by {{Price_Variance_Percent}}"
  - Priority: High
- ACTION_ASSIGN_TO_USER
  - Şuna ata: Procurement Manager
- ACTION_SEND_EMAIL_TO_GROUPS
  - Procurement Team'e bildirim gönder

**Kılavuz Referansları:**
- [Assignment Guide](../then/assignee/assignment-user-guide.md)
- [Task Assignment Guide](../then/task/task-assignment-guide.md)
- [Send Email Guide](../then/action/send-email-groups-guide.md)

---

## Eksiksiz İş Akışı Diyagramı

```
DOCUMENT ARRIVES (Invoice with Product ABC123, Price €52)
│
├─ STEP 1: Call Pricing API
│  Card: CALL_API
│  Request: Get current price for ABC123
│  │
│  ├─ SUCCESS (200) ✅
│  │  Response: {"unit_price": 50.00}
│  │  │
│  │  ├─ STEP 2: Check API Status
│  │  │  Card: CONDITION_HTTPS_REQUEST_STATUS
│  │  │  Result: 200 = Success
│  │  │  │
│  │  │  ├─ STEP 3: Store API Data
│  │  │  │  Card: ACTION_SET_FIELD_TO_TEXT
│  │  │  │  Action: Store €50 in "Current_API_Price" field
│  │  │  │  │
│  │  │  │  ├─ STEP 4: Compare Prices
│  │  │  │  │  Card: CONDITION_COMPARE_TWO_DOCFIELD_VALUES
│  │  │  │  │  Calculate: Variance = |52-50|/50 = 4%
│  │  │  │  │  │
│  │  │  │  │  ├─ IF Variance ≤ 5% (PASS) ✅
│  │  │  │  │  │  │
│  │  │  │  │  │  ├─ Set Status Field: "PASS"
│  │  │  │  │  │  └─ Auto-Approve Document
│  │  │  │  │  │     → END (Document Approved)
│  │  │  │  │  │
│  │  │  │  │  └─ IF Variance > 5% (FAIL) ❌
│  │  │  │  │     │
│  │  │  │  │     ├─ Set Status Field: "FAIL"
│  │  │  │  │     ├─ Create Review Task
│  │  │  │  │     ├─ Assign to Procurement Manager
│  │  │  │  │     └─ Send Email Notification
│  │  │  │  │        → END (Pending Review)
│  │  │  │  │
│  │  │  │  └─ [Field storage complete]
│  │  │  │
│  │  │  └─ [Status check complete]
│  │  │
│  │  └─ [API data retrieved]
│  │
│  └─ ERROR (Non-200) ❌
│     │
│     ├─ Set Error Status
│     ├─ Create "API Error" Task
│     ├─ Assign to IT Support
│     └─ Send Email to Admin
│        → END (API Error - Manual Review)
```

---

## Yapılandırma Şablonları

### Şablon 1: Basit GET İsteği (Arama)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/lookup",
  "method": "GET",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}"
  },
  "parameters": {
    "id": "{{DOCUMENT_FIELD:Lookup_ID}}"
  }
}
```

**Kullanım:** ID'ye göre basit veri araması

---

### Şablon 2: Gövdeli POST İsteği (Doğrulama)

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/validate",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document_number": "{{DOCUMENT_NUMBER}}",
    "supplier_id": "{{DOCUMENT_FIELD:Supplier_Code}}",
    "total_amount": "{{DOCUMENT_FIELD:Total_Amount}}",
    "currency": "{{DOCUMENT_FIELD:Currency}}"
  }
}
```

**Kullanım:** Doğrulama için belge verisi gönderme

---

### Şablon 3: İç İçe Verili Karmaşık İstek

```json
{
  "card": "CALL_API",
  "endpoint": "https://api.example.com/process",
  "method": "POST",
  "headers": {
    "Authorization": "Bearer {{API_KEY}}",
    "Content-Type": "application/json"
  },
  "body": {
    "document": {
      "type": "{{DOCUMENT_TYPE}}",
      "number": "{{DOCUMENT_NUMBER}}",
      "date": "{{DOCUMENT_FIELD:Invoice_Date}}"
    },
    "vendor": {
      "code": "{{DOCUMENT_FIELD:Supplier_Code}}",
      "name": "{{DOCUMENT_FIELD:Supplier_Name}}"
    },
    "items": [
      {
        "product": "{{TABLE_FIELD:Product_Code}}",
        "quantity": "{{TABLE_FIELD:Quantity}}",
        "unit_price": "{{TABLE_FIELD:Unit_Price}}"
      }
    ]
  }
}
```

**Kullanım:** Tablo verisiyle karmaşık belge işleme

---

## Hata Yönetimi

### Yaygın Hatalar ve Çözümler

#### Hata 1: Bağlantı Zaman Aşımı

**Belirtiler:**
- API yanıt vermiyor
- İş akışı beklemede takılı kalıyor

**Çözüm:**
```
1. Check API endpoint URL (typo?)
2. Verify network connectivity
3. Check API service status
4. Implement timeout handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = TIMEOUT:
     → Create "API Timeout" task
     → Assign to IT Support
     → Send email notification
     → Use fallback value (if available)
```

#### Hata 2: 401 Unauthorized

**Belirtiler:**
- API 401 durumu döndürür
- Kimlik doğrulama başarısız

**Çözüm:**
```
1. Verify API key is correct
2. Check if API key expired
3. Ensure Authorization header formatted correctly
4. Implement auth error handling:

   IF CONDITION_HTTPS_REQUEST_STATUS = 401:
     → Create "API Auth Failed" task
     → Assign to Admin
     → Log error details
     → Stop workflow execution
```

#### Hata 3: Geçersiz Yanıt Biçimi

**Belirtiler:**
- Yanıt alındı ama ayrıştırılamıyor
- Beklenen alanlar eksik

**Çözüm:**
```
1. Verify API documentation
2. Check response structure matches expectations
3. Implement response validation:

   IF API_RESPONSE:data.unit_price IS NULL:
     → Set default value
     → Create "Invalid Response" task
     → Log response for debugging
```

**Kılavuz Referansı:** [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)

---

## Gelişmiş Varyasyonlar

### Varyasyon 1: Çoklu API Zincirleme

**Senaryo:** Birden fazla API'den veri gerekir

```
Step 1: Call Supplier API → Get Supplier Details
Step 2: Call Product API → Get Product Info (using Supplier ID from Step 1)
Step 3: Call Pricing API → Get Price (using Product ID from Step 2)
Step 4: Validate & Store all data
```

---

### Varyasyon 2: Koşullu API Çağrıları

**Senaryo:** Yalnızca belirli koşullarda API çağırma

```
IF DOCUMENT_TYPE = "Invoice" AND AMOUNT > 10000:
  → Call Pricing Validation API
  → Verify prices
ELSE:
  → Skip API call (not needed for small amounts)
```

---

### Varyasyon 3: API Yanıtı Önbelleğe Alma

**Senaryo:** Yanıtları önbelleğe alarak API çağrılarını azaltma

```
1. Check if "API_Last_Called" date is today
2. IF Yes:
     → Use cached value from "Cached_API_Price" field
3. IF No:
     → Call API
     → Store response in "Cached_API_Price"
     → Set "API_Last_Called" to today
```

---

## Performans Değerlendirmeleri

### En İyi Uygulamalar

✅ **Yapın:**
- Mümkün olduğunda API yanıtlarını önbelleğe alın
- Zaman aşımı ayarları kullanın (30-60 saniye)
- Geçici hatalar için yeniden deneme mantığı uygulayın
- Hata ayıklama için API çağrılarını günlüğe kaydedin
- API kullanımını/maliyetlerini izleyin
- Önce örnek belgelerle test edin

❌ **Yapmayın:**
- Her belge için API'leri eşzamanlı çağırma (toplu işlemeyi düşünün)
- Yanıt hatalarını görmezden gelme
- Kimlik bilgilerini iş akışına sabit kodlama
- Gereksiz API çağrıları yapma
- Zaman aşımlarını ele almayı unutma

---

## Test Kontrol Listesi

Bu kalıbı dağıtmadan önce:

- [ ] Geçerli veriyle API çağrısını test edin
- [ ] Geçersiz veriyle API çağrısını test edin
- [ ] Zaman aşımı senaryosunu test edin (API yavaşsa ne olur?)
- [ ] Kimlik doğrulama hatasını test edin
- [ ] Geçersiz yanıt biçimini test edin
- [ ] Alan depolamasını test edin (veri doğru depolandı mı?)
- [ ] Karşılaştırma mantığını test edin (doğru hesaplama?)
- [ ] Yönlendirmeyi test edin (belgeler doğru yere gidiyor mu?)
- [ ] Hata yönetimini test edin (hatalar düzgün ele alınıyor mu?)
- [ ] Yüksek hacimle test edin (performans kabul edilebilir mi?)

---

## Gerçek Dünya Örnekleri

### Örnek 1: Döviz Kuru Araması

**API:** https://api.exchangerate-api.com/v4/latest/USD

**İş Akışı:**
1. Fatura para birimini çıkar: "GBP"
2. Döviz kuru API'sini çağır
3. GBP→EUR döviz kurunu al
4. EUR karşılığını hesapla
5. "Amount_EUR" alanında depola
6. EUR tutarıyla işlemeye devam et

---

### Örnek 2: Tedarikçi Kredi Kontrolü

**API:** Dahili kredi kontrol servisi

**İş Akışı:**
1. Tedarikçi kodunu çıkar
2. Kredi kontrol API'sini çağır
3. Kredi durumunu al: "APPROVED" veya "BLOCKED"
4. BLOCKED ise:
   - İşlemeyi durdur
   - Acil görev oluştur
   - Finans ekibine bildir
5. APPROVED ise:
   - Normal iş akışına devam et

---

### Örnek 3: Ürün Ana Verisi Zenginleştirme

**API:** Ürün katalog servisi

**İş Akışı:**
1. Faturadan ürün kodunu çıkar
2. Ürün API'sini çağır
3. Şunları al: Ürün adı, kategori, GL hesabı
4. Belge alanlarında depola
5. Otomatik muhasebe için kullan

---

## İlgili Kalıplar

### Bu Kalıp İyi Çalışır:

- **[Data Transformation Pattern](data-transformation-pattern.md)** - API yanıt verilerini dönüştürme
- **[Decision Logic Pattern](decision-logic-pattern.md)** - API verilerine göre yönlendirme
- **[Task Management Pattern](task-management-pattern.md)** - API hataları için görevler oluşturma
- **[PO Matching Pattern](po-matching-pattern.md)** - API fiyatlandırmasını PO doğrulamasıyla birleştirme

---

## İlgili Kılavuzlar

### Önkoşullar
- [Call API Guide](../then/action/call-api-guide.md) - API kart belgeleri
- [Condition Cards Guide](../and/condition-cards-complete-guide.md) - Koşul mantığı
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Alan işlemleri

### İlgili Kartlar
- **CALL_API** - [Call API Guide](../then/action/call-api-guide.md)
- **ACTION_HTTPS_REQUEST** - [HTTPS Request Guide](../then/action/https-request-guide.md)
- **CONDITION_HTTPS_REQUEST_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-https-request-status)
- **ACTION_SET_FIELD_TO_TEXT** - [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md#set-field)
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-comparison)

### Sonraki Adımlar
- Hata yönetimi uygulayın: [Error Handling Pattern](error-handling-pattern.md)
- Görev oluşturma ekleyin: [Task Management Pattern](task-management-pattern.md)
- Veriyi dönüştürün: [Data Transformation Pattern](data-transformation-pattern.md)

---

## Destek ve Kaynaklar

**Yardıma mı İhtiyacınız Var?**
- [Call API Troubleshooting](../then/action/call-api-guide.md#troubleshooting)'i inceleyin
- [API Response Codes](../then/action/call-api-guide.md#response-scenarios)'ı kontrol edin
- Önce API'yi Postman ile test edin
- API sağlayıcı desteğiyle iletişime geçin

**Geri Bildirim:**
- Kalıp sorunlarını şuraya bildirin: docs@docbits.com
- İyileştirmeler önerin
- Kullanım durumlarınızı paylaşın

---

**Kalıp Sürümü:** 1.0
**Son Güncelleme:** 23 Ekim 2025
**Zorluk:** Orta
**Tahmini Süre:** 45-60 dakika
**Başarı Oranı:** Yüksek (API kararlı olduğunda)

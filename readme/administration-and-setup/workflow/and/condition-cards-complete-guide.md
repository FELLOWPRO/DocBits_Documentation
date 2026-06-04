# Condition Cards - Eksiksiz Kılavuz

**Kapsam:** Kalan 31 koşul kartı

---

Bu sayfadaki koşul kartları, Workflow Builder'ın **When** ve **And** gruplarına gider — Then eylemlerinin çalışıp çalışmayacağına karar verirler:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p>Koşul kartları <strong>When</strong> ve <strong>And</strong> gruplarına <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Durum:** Çoğu koşul kartı tek veya çift sürümlü yapılarla kararlıdır
**Sürüm Kalıbı:** Çoğu v1 → v2 kalıbını izler (i18n desteği ekler)
**Çok Sürümlü Örnek:** CONDITION_DECISION_TREE_DATA (v2-v3)

**Not:** Bazı PO karşılaştırma koşul kartlarında 4-5 sürüm vardır (ayrıntılar için PO Matching Guide'a bakın)

📖 [Eksiksiz Sürüm Geçmişi](../../../changelog/release.md) | [Kart Sürüm Veritabanı](../../../../DocFlow/docs/card_version.md) | [PO Matching Guide](../compare-with-purchase-order/po-matching-complete-guide.md)

---

# Belge Hâli ve Durumu Koşulları

## Kart: CONDITION_DOC_STATUS_IS_ISNOT / Belge Durumu Kontrolü

### Amaç
Belgenin belirli bir duruma sahip olup olmadığını kontrol eder

### Ne Zaman Kullanılır
- Onaylamadan önce
- Belirli bir iş akışı aşamasında
- Durum tabanlı yönlendirme

### Belge Durumu Türleri
```
- Upload: Being uploaded
- OCR: Being scanned
- Classification: Type detection
- Ready for Validation: Waiting for review
- Workflow: In process
- Pending Approval: Needs approval
- Pending Second Approval: Needs secondary approval
- Auto Accounting: Auto-booking
- Export: Being exported
- Error: Problem occurred
```

### Nasıl Çalışır
```
Current Status: "Pending Approval"
    ↓
Check: Is status = "Pending Approval"?
    ↓
YES → Continue with action
NO → Stop or do alternative action
```

### Örnek
```
Condition: "Document status IS Pending Approval?"
    ↓
If YES: Create approval task
If NO: Do something else
```

### Parametreler
```
Operator: IS / IS NOT
Status: [Select status]
```

---

## Kart: CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST

### Amaç
Durumun bir listedeki herhangi biriyle eşleşip eşleşmediğini kontrol eder

### Ne Zaman Kullanılır
- Birden fazla geçerli durum
- Durum için OR mantığı

### Örnek
```
Condition: "Status is one of: [Pending Approval, Pending Second Approval, Workflow]?"
    ↓
If status matches any: Continue
If doesn't match: Stop
```

---

## Kart: CONDITION_DOC_TYPE_IS_ISNOT / Belge Türü Kontrolü

### Amaç
Belgenin belirli bir tür olup olmadığını kontrol eder

### Belge Türleri
```
- Invoice
- Credit Note
- Purchase Order
- Delivery Note
- ASN (Advanced Ship Notice)
- Receipt
- Return
- Custom Types
```

### Nasıl Çalışır
```
Document type: "Invoice"
    ↓
Check: Is type = "Invoice"?
    ↓
YES → Process as invoice
NO → Process differently
```

### Örnek
```
Condition: "Document type IS Invoice?"
    ↓
If YES: Check PO match
If NO: Skip PO validation
```

---

## Kart: CONDITION_DOC_TYPE_IS_ISNOT_LIST

### Amaç
Türün listedeki herhangi biriyle eşleşip eşleşmediğini kontrol eder

### Örnek
```
Condition: "Type is one of: [Invoice, Credit Note]?"
    ↓
YES: Process financial document
NO: Skip financial checks
```

---

## Kart: CONDITION_SUB_ORG_IS_ISNOT / Alt Kuruluş Kontrolü

### Amaç
Belgeye hangi kuruluşun/departmanın sahip olduğunu kontrol eder

### Kuruluşlar
```
- Finance Department
- Procurement
- Warehouse
- Manufacturing
- Quality Control
- Distribution
- Regional Offices
```

### Örnek
```
Document belongs to: "Berlin Office"
    ↓
Check: Sub-Org = "Berlin Office"?
    ↓
YES: Assign to Berlin team
NO: Check other offices
```

---

## Kart: CONDITION_PURCHASE_ORDER_IMPORT / PO İçe Aktarma Kontrolü

### Amaç
PO'nun yeni içe aktarılmış mı yoksa mevcut mu olduğunu kontrol eder

### Nasıl Çalışır
```
PO Status: "Newly Imported" (First time seeing this PO)
    ↓
Check: Is new import?
    ↓
YES: Do initial validation
NO: Use cached PO data
```

### Ne Zaman Kullanılır
- Yeni PO'lar için farklı işleme
- Bilinen PO'lar için doğrulamayı atlama
- Tedarikçiyi ilk kez görmeyi izleme

---

# Atanan (Assignee) Koşulları

## Kart: CONDITION_USER_IS_ISNOT / Kullanıcı Kontrolü

### Amaç
Belgenin belirli bir kullanıcıya atanıp atanmadığını kontrol eder

### Nasıl Çalışır
```
Assigned to: "John Smith"
    ↓
Check: Is assigned to "John Smith"?
    ↓
YES: Continue
NO: Stop
```

### Örnek
```
Condition: "Assigned to IS 'Finance Manager'"?
    ↓
If YES: Create approval task
If NO: Skip approval
```

---

## Kart: CONDITION_USER_IS_ISNOT_IN_LIST

### Amaç
Listedeki herhangi bir kullanıcıya atanıp atanmadığını kontrol eder

### Örnek
```
Condition: "Assigned to one of: [John, Sarah, Mike]?"
    ↓
YES: Continue
NO: Stop
```

---

## Kart: CONDITION_GROUP_IS_ISNOT / Grup Kontrolü

### Amaç
Belirli bir gruba atanıp atanmadığını kontrol eder

### Örnek
```
Assigned to: "Finance Team" (10 members)
    ↓
Check: Is assigned to Finance Team?
    ↓
YES: Process for group
NO: Check other groups
```

---

## Kart: CONDITION_GROUP_IS_ISNOT_IN_LIST

### Amaç
Listedeki herhangi bir gruba atanıp atanmadığını kontrol eder

### Örnek
```
Condition: "Assigned to one of: [Finance, Procurement, Quality]?"
    ↓
YES: Continue
NO: Stop
```

---

# Tarih ve Saat Koşulları

## Kart: CONDITION_TIME_IS_ISNOT_BETWEEN / Tarih Aralığı Kontrolü

### Amaç
Bir tarihin iki tarih arasına düşüp düşmediğini kontrol eder

### Nasıl Çalışır
```
Document Date: 2025-10-23
    ↓
Check: Is date between 2025-10-01 and 2025-10-31?
    ↓
YES (October) → Continue
NO (Other month) → Stop
```

### Hesaplama
```
Formula:
  Start Date ≤ Document Date ≤ End Date?

Example:
  2025-01-01 ≤ 2025-10-23 ≤ 2025-10-31?
  YES ✅ Within range
```

### Ne Zaman Kullanılır
- Mali dönemde olup olmadığını kontrol et
- Son teslim tarihi içinde olup olmadığını kontrol et
- Promosyon döneminde olup olmadığını kontrol et

### Örnek
```
Condition: "Document date between Oct 1 and Oct 31?"
    ↓
If YES: Oct invoices (monthly processing)
If NO: Other month invoices
```

### Parametreler
```
Start Date: [Select or enter]
End Date: [Select or enter]
Date Field: [Which field to check]
```

---

## Kart: CONDITION_TODAY_IS_ISNOT / Bugün Kontrolü

### Amaç
Bugünün tarihinin ölçütlerle eşleşip eşleşmediğini kontrol eder

### Nasıl Çalışır
```
Today: 2025-10-23
    ↓
Check: Is today > 2025-10-31?
    ↓
NO → Deadline not passed
YES → Deadline passed (overdue)
```

### Kullanım Durumları
```
Is today past deadline? → Invoice is overdue
Is today past promotion date? → Promotion ended
Is today in quarter? → For quarterly reporting
```

### Örnek
```
Condition: "Is today AFTER invoice due date?"
    ↓
If YES: Invoice is overdue, escalate
If NO: Invoice still within deadline
```

---

## Kart: CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA

### Amaç
Teslimat tarihinin takvimdeki onaylı teslimat tarihleriyle eşleşip eşleşmediğini kontrol eder

### Nasıl Çalışır
```
Delivery Date from Invoice: 2025-10-25
    ↓
Check Master Calendar: Is 2025-10-25 acceptable?
    ↓
(Master calendar has list of acceptable dates)
    ↓
YES: Date is acceptable
NO: Date not in approved list
```

### Ne Zaman Kullanılır
- Teslimatın üzerinde anlaşılan tarihlerle eşleştiğini doğrula
- Tatil takvimine karşı kontrol et
- Sözleşmeli tarihlere karşı doğrula

### Örnek
```
Supplier promised: 2025-10-25
Invoice shows delivery: 2025-10-25
Check Master Calendar: Is 2025-10-25 valid delivery date?
    ↓
YES: Delivery date acceptable ✅
```

---

# Mantık (Logic) Koşulları

## Kart: CONDITION_DECISION_TREE_DATA / Karar Tablosu Dönüşleri

### Amaç
Karar tablosunun dönüş değerlerine sahip olup olmadığını kontrol eder

### Nasıl Çalışır
```
Run Decision Table
    ↓
Does it return values?
    ↓
YES: Data is available for next cards
NO: No matching results
```

### Ne Zaman Kullanılır
- Karar tablosu sonuçlarını kullanmadan önce
- Geçit koşulu olarak
- Yönlendirmenin kullanılabilir olup olmadığını kontrol etmek için

### Örnek
```
Decision Table: "Route by supplier"
    ↓
Condition: "Decision table returns data?"
    ↓
If YES: Use returned values for routing
If NO: Use default routing
```

---

## Kart: CONDITION_CONTINUE_CHANCE / Rastgele Olasılık

### Amaç
Belirtilen bir olasılıkla devam eder

### Nasıl Çalışır
```
Probability: 50%
    ↓
Roll dice
    ↓
Random chance: 50% YES, 50% NO
```

### Ne Zaman Kullanılır
- A/B testi iş akışları
- Belgeleri örnekleme
- Rastgele kalite kontrolleri

### Örnek
```
Condition: "Continue with 10% chance?"
    ↓
90% of documents: Stop here
10% of documents: Continue for detailed review
```

### Hesaplama
```
If probability = 50%:
  - 50% of documents continue
  - 50% of documents stop

If probability = 10%:
  - 10% continue (1 in 10 documents)
  - 90% stop
```

---

## Kart: CONDITION_MODULE_IS_ISNOT_ACTIVE / Özellik Kontrolü

### Amaç
Belirli bir modülün/özelliğin etkin olup olmadığını kontrol eder

### Modüller
```
- PO Matching
- Auto Accounting
- OCR
- Document Classification
- Supplier Management
- Custom Modules
```

### Nasıl Çalışır
```
Module: "PO Matching"
    ↓
Is PO Matching enabled?
    ↓
YES: Do PO match validation
NO: Skip PO checks
```

### Ne Zaman Kullanılır
- Özelliğe bağlı iş akışları
- İsteğe bağlı işleme
- Lisanslı özelliğin etkin olup olmadığını kontrol etme

---

## Kart: CONDITION_HTTPS_REQUEST_STATUS / İstek Sonucu Kontrolü

### Amaç
HTTPS isteğinin başarılı olup olmadığını kontrol eder

### Durum Kodları
```
200-299: ✅ Success
300-399: ↪️ Redirect
400-499: ❌ Client Error
500-599: ❌ Server Error
```

### Nasıl Çalışır
```
Send HTTPS request
    ↓
Receive response code
    ↓
Check: Was request successful (200)?
    ↓
YES: Continue with response data
NO: Error handling
```

### Örnek
```
Send pricing request to API
    ↓
Condition: "Did request return 200 (success)?"
    ↓
If YES: Use returned price
If NO: Use fallback price
```

---

## Kart: CONDITION_SUPPLIER_STATUS_IS_ISNOT / Tedarikçi Durumu Kontrolü

### Amaç
Tedarikçinin sistemdeki durumunu kontrol eder

### Tedarikçi Durumları
```
✅ ACTIVE: Can do business
⚠️ ON HOLD: Temporarily blocked
❌ INACTIVE: No longer doing business
⚠️ CONDITIONAL: Only for specific items
```

### Nasıl Çalışır
```
Supplier: ABC Corp
Status in Database: ACTIVE
    ↓
Check: Is status ACTIVE?
    ↓
YES: Process normally
NO: Flag for review
```

### Örnek
```
Invoice from ABC Corp
    ↓
Condition: "Is supplier status ACTIVE?"
    ↓
If YES: Process normally
If NO: Block or escalate
```

---

## Kart: CONDITION_SPECIFY_SUPPLIER_TYPE

### Amaç
Tedarikçi türünü belirtir/kontrol eder

### Tedarikçi Türleri
```
- Preferred Supplier
- Standard Supplier
- Spot Purchase
- Framework Agreement
- Strategic Partner
```

### Nasıl Çalışır
```
Supplier Type: "Preferred"
    ↓
Check: Is preferred supplier?
    ↓
YES: Apply preferred supplier discounts
NO: Standard pricing
```

---

# Örnek Karar Akışları

## Akış 1: Durum Tabanlı İşleme
```
Document Arrives
    ↓
Check: Status = "Ready for Validation"?
    ↓
YES: Validate document
    ↓
Check: Status = "Pending Approval"?
    ↓
YES: Create approval task
    ↓
Check: Status = "Error"?
    ↓
YES: Escalate to manager
```

## Akış 2: Tedarikçi Tabanlı İşleme
```
Invoice Arrives
    ↓
Check: Supplier status ACTIVE?
    ↓
NO: Block and escalate
    ↓
YES: Check: Supplier is preferred?
    ↓
YES: Fast track approval
NO: Standard approval
```

## Akış 3: Tarih Kontrolüyle Tutar Tabanlı
```
Invoice Arrives
    ↓
Check: Amount > €10,000?
    ↓
YES: Check: Date within Oct (fiscal period)?
    ↓
YES: Assign to Finance Director
NO: Assign to Finance Manager
```

---

# Koşul Kartı Karşılaştırması

| Kart | Kontrol Eder | Operatör | Kullanım |
|------|--------|----------|-----|
| CONDITION_DOC_STATUS_IS_ISNOT | Belge durumu | IS / IS NOT | Aşama kontrolü |
| CONDITION_DOC_STATUS_IS_ISNOT_IN_LIST | Listede durum | IN / NOT IN | Birden fazla durum |
| CONDITION_DOC_TYPE_IS_ISNOT | Belge türü | IS / IS NOT | Tür filtreleme |
| CONDITION_DOC_TYPE_IS_ISNOT_LIST | Listede tür | IN / NOT IN | Birden fazla tür |
| CONDITION_SUB_ORG_IS_ISNOT | Kuruluş | IS / IS NOT | Departman kontrolü |
| CONDITION_USER_IS_ISNOT | Atanan kullanıcı | IS / IS NOT | Kullanıcı kontrolü |
| CONDITION_USER_IS_ISNOT_IN_LIST | Listede kullanıcı | IN / NOT IN | Birden fazla kullanıcı |
| CONDITION_GROUP_IS_ISNOT | Atanan grup | IS / IS NOT | Grup kontrolü |
| CONDITION_GROUP_IS_ISNOT_IN_LIST | Listede grup | IN / NOT IN | Birden fazla grup |
| CONDITION_TIME_IS_ISNOT_BETWEEN | Tarih aralığı | BETWEEN | Tarih penceresi |
| CONDITION_TODAY_IS_ISNOT | Bugünün tarihi | IS / IS NOT | Bugün kontrolü |
| CONDITION_DECISION_TREE_DATA | DT dönüşleri | HAS / HAS NOT | DT sonuç kontrolü |
| CONDITION_CONTINUE_CHANCE | Olasılık | CHANCE | Rastgele geçit |
| CONDITION_MODULE_IS_ISNOT_ACTIVE | Özellik etkin | IS / IS NOT | Özellik kontrolü |
| CONDITION_HTTPS_REQUEST_STATUS | İstek sonucu | STATUS | Yanıt kontrolü |
| CONDITION_SUPPLIER_STATUS_IS_ISNOT | Tedarikçi durumu | IS / IS NOT | Tedarikçi kontrolü |

---

# Koşullar için En İyi Uygulamalar

✅ **Yapın:**
- Belirli koşullar kullanın
- Mantığı örneklerle test edin
- Koşulları mantıksal olarak sıralayın
- Tüm yollar için yedek bulundurun
- Karmaşık mantığı belgeleyin

❌ **Yapmayın:**
- Döngüsel koşullar oluşturma (A eğer B ise, B eğer A ise)
- Koşulları çok karmaşık yapma
- Sınır durumlarını unutma
- Alanın her zaman değere sahip olduğunu varsayma
- İmkansız koşullar oluşturma

---

# Birden Fazla Koşulu Birleştirme

```
Condition 1: Type = Invoice?
    AND
Condition 2: Amount > €5000?
    AND
Condition 3: Supplier status = Active?
    ↓
ALL TRUE → Process
SOME FALSE → Stop
```

---

# İlgili Kartlar

- **CONDITION_DOC_FIELD_CONTAINS** - Alan içeriği kontrolü
- **CONDITION_COMPARE_TWO_DOCFIELD_VALUES** - Alan karşılaştırması
- **CONDITION_CHECKBOX_IS** - Onay kutusu kontrolü

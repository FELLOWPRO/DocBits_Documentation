# Decision Logic Pattern

**Kalıp Türü:** Koşullu Yönlendirme ve Mantık
**Karmaşıklık:** Orta
**Tahmini Kurulum:** 30-45 dakika
**Yaygın Kullanım Durumları:** Çok yollu yönlendirme, koşullu işleme, karar ağaçları, iş kuralı uygulaması

---

Bu kalıbı **Workflow Builder**'da (Workflow Dashboard → Workflow List → Add Workflow) oluşturursunuz. **Add Card**'a tıklayın ve **Logic** kategorisini açın — karar ağacını yöneten koşul ve dallanma kartlarını içerir; bunları birden fazla koşulu değerlendirmek için **And** grubuyla birleştirirsiniz:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder'da kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — koşul ve dallanma kartları <strong>Logic</strong> kategorisi altında bulunur.</p></figcaption></figure>

---

## Kalıp Genel Bakışı

Bu kalıp, belgeleri belge özelliklerine, alan değerlerine ve iş kurallarına göre farklı işleme yollarından yönlendirmek için koşul kartlarını kullanarak DocBits iş akışlarında karmaşık karar mantığının nasıl uygulanacağını gösterir.

**Bu Kalıbın Yaptıkları:**
1. Birden fazla koşulu sırayla veya paralel olarak değerlendirir
2. Belgeleri koşullara göre farklı yollara yönlendirir
3. İş kurallarını ve politikalarını uygular
4. Karmaşık karar ağaçlarını ele alır
5. Yönlendirme kararları için birden fazla ölçütü birleştirir

---

## Bu Kalıbı Ne Zaman Kullanmalı

Bu kalıbı şu durumlarda kullanın:
- ✅ Belgeleri tutar eşiklerine göre yönlendirme
- ✅ Farklı belge türleri için farklı kurallar uygulama
- ✅ Çok düzeyli onay mantığı uygulama
- ✅ Karmaşık iş politikalarını ele alma
- ✅ Birden fazla ölçüte dayalı dinamik yönlendirme oluşturma
- ✅ İstisna yönetimi mantığı uygulama
- ✅ Onay matrisleri oluşturma

**Bu kalıbı şu durumlarda kullanmayın:**
- ❌ Basit doğrusal iş akışı yeterliyse
- ❌ Tüm belgeler aynı yolu izliyorsa
- ❌ Koşullu işleme gerekmiyorsa

---

## Karar Mantığı Türleri

### 1. Basit IF-THEN Mantığı

```
IF condition:
  → Action A
ELSE:
  → Action B
```

**Örnek:**
```
IF Amount > €10,000:
  → Assign to Director
ELSE:
  → Assign to Manager
```

### 2. Birden Fazla Ölçüt (AND Mantığı)

```
IF condition1 AND condition2 AND condition3:
  → Action A
ELSE:
  → Action B
```

**Örnek:**
```
IF Amount > €10,000 AND Supplier = "New" AND Department = "IT":
  → Assign to IT Director + CFO (dual approval)
ELSE:
  → Standard approval workflow
```

### 3. Alternatif Ölçütler (OR Mantığı)

```
IF condition1 OR condition2 OR condition3:
  → Action A
ELSE:
  → Action B
```

**Örnek:**
```
IF Amount > €50,000 OR Supplier is "Blocked" OR Document has "Urgent" flag:
  → Escalate immediately
ELSE:
  → Standard processing
```

### 4. İç İçe Karar Ağacı

```
IF condition1:
  IF condition2:
    → Action A
  ELSE:
    → Action B
ELSE:
  IF condition3:
    → Action C
  ELSE:
    → Action D
```

**Örnek:**
```
IF Document_Type = "Invoice":
  IF Amount > €10,000:
    → High-value invoice workflow
  ELSE:
    → Standard invoice workflow
ELSE IF Document_Type = "Credit Note":
  IF Amount > €5,000:
    → High-value credit workflow
  ELSE:
    → Standard credit workflow
```

---

## Eksiksiz İş Akışı Örneği

### Senaryo: Fatura Onay Matrisi

**İş Kuralları:**
1. Tutar < €1.000: Otomatik onayla
2. Tutar €1.000-€10.000: Yönetici onayı
3. Tutar > €10.000 VE Yeni Tedarikçi: Direktör + CFO onayı
4. Tutar > €10.000 VE Mevcut Tedarikçi: Yalnızca Direktör onayı
5. PO uyuşmazlığı olan herhangi bir tutar: Önce Satınalma onayı
6. Acil faturalar (işaretli): Hızlandırılmış iş akışı

**Uygulama:**

```
STEP 1: Check for PO Mismatch
  IF PO_Match_Status = "FAIL":
    → Route to Procurement for PO resolution
    → After resolution, continue below

STEP 2: Check Urgent Flag
  IF Urgent_Flag = TRUE:
    → Skip amount checks
    → Direct to highest approver
    → Set priority = HIGH
    → 1-day deadline

STEP 3: Amount-Based Routing (if not urgent)
  IF Amount < €1,000:
    → Auto-approve
    → Export immediately

  ELSE IF Amount < €10,000:
    → Create task for Manager
    → Priority: Medium
    → Deadline: 3 days

  ELSE IF Amount ≥ €10,000:
    CHECK Supplier Status:
      IF Supplier_Age < 180 days (New):
        → Create task for Director (Task 1)
        → After approval, create task for CFO (Task 2)
        → Priority: High
        → Deadline: 2 days each

      ELSE (Existing Supplier):
        → Create task for Director only
        → Priority: High
        → Deadline: 2 days
```

---

## Adım Adım Uygulama

### Adım 1: Koşul Kartlarını Tanımla

**Koşul 1: Tutar Eşiği**
```
Card: CONDITION_DOC_FIELD_AMOUNT
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Koşul 2: Belge Türü Kontrolü**
```
Card: CONDITION_DOC_TYPE_IS_ISNOT
Document Type: IS
Type: Invoice
```

**Koşul 3: Tedarikçi Durumu**
```
Card: CONDITION_SUPPLIER_STATUS_IS_ISNOT
Supplier Status: IS
Status: ACTIVE
```

**Koşul 4: Yeni Tedarikçi Kontrolü**
```
Card: CONDITION_DOC_FIELD_DATE
Field: Supplier_First_Transaction_Date
Operator: IS AFTER
Value: {{TODAY_MINUS_180_DAYS}}
```

**Kılavuz Referansı:** [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md)

---

### Adım 2: Karar Ağacını Oluştur

**Düzey 1: Belge Türü**
```
Workflow: "Invoice Processing"

IF Document_Type = "Invoice":
  → Continue to Level 2

ELSE IF Document_Type = "Credit Note":
  → Branch to "Credit Note Processing"

ELSE IF Document_Type = "Receipt":
  → Branch to "Receipt Processing"

ELSE:
  → Route to "Unknown Document Type" handling
```

**Düzey 2: Tutar Eşikleri (Faturalar için)**
```
IF Amount < €1,000:
  → Branch to "Auto-Approve Path"

ELSE IF Amount < €10,000:
  → Branch to "Manager Approval Path"

ELSE IF Amount < €50,000:
  → Branch to "Director Approval Path"
  → Check Level 3 conditions

ELSE (Amount ≥ €50,000):
  → Branch to "Executive Approval Path"
  → Dual or triple approval required
```

**Düzey 3: Tedarikçi Analizi (yüksek tutarlı faturalar için)**
```
IF Supplier_Status = "BLOCKED":
  → STOP processing
  → Create urgent escalation task
  → Notify procurement and finance

ELSE IF Supplier_Age < 180 days (New):
  → Additional approval required
  → Add CFO to approval chain
  → Enhanced verification

ELSE IF Supplier_Risk_Rating = "HIGH":
  → Additional checks required
  → Fraud detection review
  → Manager pre-approval

ELSE:
  → Standard high-value workflow
```

---

### Adım 3: Yönlendirme Eylemleri Oluştur

**Yol A: Otomatik Onay (Tutar < €1.000)**
```
Actions:
1. Set field "Approval_Type" = "AUTO"
2. Set field "Approval_Level" = "0"
3. ACTION_APPROVE_DOCUMENT
4. Export to ERP
5. Send confirmation email (optional)
```

**Yol B: Yönetici Onayı (€1.000-€10.000)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "1"
3. tasks_create:
   - Title: "Approve Invoice {{DOCUMENT_NUMBER}}"
   - Assign to: Department_Manager
   - Priority: Medium
   - Deadline: 3 days
4. Send email notification to manager
5. Wait for task completion
6. If approved: Export to ERP
7. If rejected: Return to supplier
```

**Yol C: Direktör Onayı (€10.000-€50.000)**
```
Actions:
1. Set field "Approval_Type" = "MANUAL"
2. Set field "Approval_Level" = "2"
3. Check Supplier_Age:
   IF New (< 180 days):
     - Create Task 1: Director approval
     - After Task 1: Create Task 2: CFO approval
     - Dual approval required
   ELSE:
     - Create Task: Director approval only
4. Priority: High
5. Deadline: 2 days
6. Send email notifications
7. Wait for completion
8. If all approved: Export
9. If any rejected: Return to supplier
```

**Yol D: Yönetici (Executive) Onayı (≥ €50.000)**
```
Actions:
1. Set field "Approval_Type" = "EXECUTIVE"
2. Set field "Approval_Level" = "3"
3. Sequential approvals:
   - Task 1: Finance Director
   - Task 2: CFO
   - Task 3: CEO (if > €100,000)
4. Priority: Urgent
5. Deadline: 1 day each
6. Send urgent notifications
7. Executive dashboard update
8. Wait for all approvals
9. If all approved: Export
10. If any rejected: Executive review meeting
```

---

## Gelişmiş Karar Mantığı Kalıpları

### Kalıp 1: Puan Tabanlı Yönlendirme

**Bir risk puanı hesaplayın ve buna göre yönlendirin:**

```
Risk Score Calculation:
  Score = 0

  IF Amount > €50,000: Score += 30
  IF Supplier_Age < 180 days: Score += 25
  IF PO_Variance > 10%: Score += 20
  IF Supplier_Country = "High Risk Country": Score += 15
  IF Payment_Terms < 30 days: Score += 10

  Total Score Range: 0-100

Routing:
  IF Score < 20: Auto-approve
  IF Score 20-50: Manager approval
  IF Score 51-75: Director approval
  IF Score > 75: Executive approval + fraud check
```

**Uygulama:**
```
1. ACTION_CALCULATE_FIELD: Calculate risk score
2. ACTION_SET_FIELD_TO_NUMBER: Store score
3. CONDITION_DOC_FIELD_NUMBER: Check score thresholds
4. Route based on score
```

---

### Kalıp 2: Departman Tabanlı Matris

**Departmana göre farklı onay kuralları:**

```
Department Matrix:

  IT Department:
    Amount < €5,000: IT Manager
    Amount ≥ €5,000: IT Director + CIO

  Finance Department:
    Amount < €10,000: Finance Manager
    Amount ≥ €10,000: CFO

  Operations Department:
    Amount < €3,000: Operations Manager
    Amount ≥ €3,000: COO

  General:
    Amount < €2,000: Department Manager
    Amount ≥ €2,000: Department Director
```

**Uygulama:**
```
1. Check Department field
2. Based on department, check amount threshold
3. Route to appropriate approver
4. Different thresholds per department
```

---

### Kalıp 3: Zaman Tabanlı Mantık

**Zamanlamaya dayalı farklı kurallar:**

```
Month-End Processing (Last 3 days of month):
  IF Today in last 3 days of month:
    - Priority: URGENT
    - Deadline: 1 day
    - Approver: On-duty finance manager
    - Expedited workflow
  ELSE:
    - Standard priority
    - Standard deadline
    - Standard workflow

Business Hours vs After Hours:
  IF Time between 9 AM - 5 PM:
    - Assign to current shift
  ELSE:
    - Queue for next business day
    - OR route to on-call approver

Fiscal Period:
  IF Document_Date in Current_Fiscal_Period:
    - Standard processing
  ELSE:
    - Flag as "Prior Period"
    - Require accounting approval
    - Additional checks
```

---

### Kalıp 4: İstisna Tabanlı Yönlendirme

**İstisnaları ayrı yönlendirin:**

```
Exception Detection:

  No Exception:
    → Standard workflow

  Minor Exception (Auto-fixable):
    → Auto-correct
    → Log correction
    → Continue standard workflow

  Medium Exception (Needs review):
    → Create review task
    → Flag document
    → After fix: Continue workflow

  Major Exception (Requires escalation):
    → Stop processing
    → Create urgent task
    → Notify multiple levels
    → Manual intervention required

Exception Types:
  - Missing required field
  - Invalid field value
  - PO mismatch
  - Duplicate invoice
  - Supplier mismatch
  - Amount discrepancy
```

---

## Eksiksiz Karar Mantığı Diyagramı

```
INVOICE ARRIVES
│
├─ LEVEL 1: EXCEPTION CHECK
│  │
│  ├─ Has Critical Exception? (Missing PO, Duplicate, etc.)
│  │  │
│  │  ├─ YES → Stop & Escalate
│  │  │        Create urgent task
│  │  │        Notify admin
│  │  │        → END (Exception Handling)
│  │  │
│  │  └─ NO → Continue to Level 2
│
├─ LEVEL 2: DOCUMENT TYPE
│  │
│  ├─ Type = Invoice?
│  │  └─ YES → Continue to Level 3
│  │
│  ├─ Type = Credit Note?
│  │  └─ YES → Branch to Credit Note workflow
│  │           → END (Credit Note Path)
│  │
│  └─ Other Type?
│     └─ YES → Branch to appropriate workflow
│              → END (Other Type Path)
│
├─ LEVEL 3: URGENCY CHECK (for Invoices)
│  │
│  ├─ Urgent Flag = TRUE?
│  │  │
│  │  ├─ YES → Expedited Workflow
│  │  │        Priority: URGENT
│  │  │        Deadline: 1 day
│  │  │        Assign to: Senior Approver
│  │  │        → END (Expedited Path)
│  │  │
│  │  └─ NO → Continue to Level 4
│
├─ LEVEL 4: AMOUNT THRESHOLDS
│  │
│  ├─ Amount < €1,000?
│  │  │
│  │  ├─ YES → AUTO-APPROVE PATH
│  │  │        Set Approval_Type = "AUTO"
│  │  │        Approve immediately
│  │  │        Export to ERP
│  │  │        → END (Auto-Approved)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €10,000?
│  │  │
│  │  ├─ YES → MANAGER APPROVAL PATH
│  │  │        Create task for Manager
│  │  │        Priority: Medium
│  │  │        Deadline: 3 days
│  │  │        → WAIT for approval
│  │  │           → END (Manager Path)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Amount < €50,000?
│  │  │
│  │  ├─ YES → DIRECTOR APPROVAL PATH
│  │  │        Continue to Level 5 (Supplier Check)
│  │  │
│  │  └─ NO → Continue
│  │
│  └─ Amount ≥ €50,000?
│     │
│     └─ YES → EXECUTIVE APPROVAL PATH
│              Create sequential tasks:
│              - Finance Director
│              - CFO
│              - CEO (if > €100,000)
│              Priority: URGENT
│              Deadline: 1 day each
│              → WAIT for all approvals
│                 → END (Executive Path)
│
├─ LEVEL 5: SUPPLIER ANALYSIS (for €10k-€50k range)
│  │
│  ├─ Supplier Status = "BLOCKED"?
│  │  │
│  │  ├─ YES → BLOCK & ESCALATE
│  │  │        Stop processing
│  │  │        Create urgent task
│  │  │        Notify procurement & finance
│  │  │        → END (Blocked Supplier)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Age < 180 days (New)?
│  │  │
│  │  ├─ YES → DUAL APPROVAL REQUIRED
│  │  │        Task 1: Director (2 days)
│  │  │        → WAIT for Task 1
│  │  │           IF Task 1 Approved:
│  │  │             Task 2: CFO (2 days)
│  │  │             → WAIT for Task 2
│  │  │                → END (Dual Approved)
│  │  │           IF Task 1 Rejected:
│  │  │             → END (Rejected at Level 1)
│  │  │
│  │  └─ NO → Continue
│  │
│  ├─ Supplier Risk Rating = "HIGH"?
│  │  │
│  │  ├─ YES → ENHANCED APPROVAL
│  │  │        Additional fraud checks
│  │  │        Director approval required
│  │  │        Extended deadline
│  │  │        → END (Enhanced Path)
│  │  │
│  │  └─ NO → STANDARD DIRECTOR APPROVAL
│  │           Create task for Director
│  │           Priority: High
│  │           Deadline: 2 days
│  │           → WAIT for approval
│  │              → END (Standard High-Value)
│  │
│  └─ [Supplier analysis complete]
│
└─ [All decision levels processed]
```

---

## Yapılandırma En İyi Uygulamaları

### 1. Mantığı Açık ve Bakımı Kolay Tutun

✅ **İyi:**
```
IF Amount > 10000:
  → High value path
ELSE:
  → Standard path
```

❌ **Kötü (Çok Karmaşık):**
```
IF (Amount > 10000 AND (Supplier = "A" OR Supplier = "B") AND NOT (Status = "X" OR Status = "Y") AND Department IN [1,2,3]):
  → Complex path
```

**Daha iyisi: Adımlara bölün:**
```
Step 1: IF Amount > 10000: Continue, ELSE: Standard path
Step 2: IF Supplier in allowed list: Continue, ELSE: Review
Step 3: IF Status valid: Continue, ELSE: Reject
Step 4: IF Department authorized: Approve, ELSE: Escalate
```

---

### 2. Karar Mantığını Belgeleyin

**Her zaman ekleyin:**
- Her karar noktasının amacı
- Uygulanan iş kuralı
- Beklenen sonuçlar
- İstisna yönetimi

**Örnek Belge:**
```
Decision Point: Amount Threshold Check
Business Rule: BR-INV-001 (Invoice Approval Matrix)
Purpose: Route invoices based on amount thresholds per company policy
Thresholds:
  < €1,000: Auto-approve (CFO approved threshold)
  €1,000-€10,000: Manager approval (Delegation matrix)
  > €10,000: Director approval (Signature authority)
Exceptions: Urgent invoices skip to highest level
Updated: 2025-10-23
Owner: Finance Department
```

---

### 3. Tüm Yolları Test Edin

**Test Matrisi:**

| Test Durumu | Tutar | Tür | Tedarikçi | Beklenen Yol | Durum |
|-----------|--------|------|----------|---------------|--------|
| TC1 | €500 | Invoice | Mevcut | Otomatik onay | ✅ |
| TC2 | €5.000 | Invoice | Mevcut | Yönetici | ✅ |
| TC3 | €15.000 | Invoice | Yeni | Direktör+CFO | ✅ |
| TC4 | €60.000 | Invoice | Mevcut | Yönetici (Executive) | ✅ |
| TC5 | €2.000 | Credit Note | Mevcut | Alacak dekontu iş akışı | ✅ |
| TC6 | €100.000 | Invoice | Bloklu | Durdur & Yükselt | ✅ |

---

### 4. Karar Metriklerini İzleyin

**İzleyin:**
- Karar yolları arasındaki dağılım
- Otomatik onay oranı
- Manuel inceleme oranı
- Yol başına ortalama işleme süresi
- İstisna oranları
- Yol kullanımı

**Örnek Metrikler:**
```
Month: October 2025
Total Invoices: 1,250

Decision Path Distribution:
- Auto-approved (< €1k): 680 (54%)
- Manager path (€1k-€10k): 420 (34%)
- Director path (€10k-€50k): 120 (10%)
- Executive path (> €50k): 30 (2%)

Processing Time:
- Auto-approve: < 1 minute
- Manager path: 2.5 days average
- Director path: 1.8 days average
- Executive path: 3.2 days average

Exceptions: 15 (1.2%)
```

---

## İlgili Kalıplar

### İyi Birlikte Çalışan Kalıplar:

- **[Task Management Pattern](task-management-pattern.md)** - Kararlara göre görevler oluşturma
- **[API Integration Pattern](api-integration-pattern.md)** - Karar verme için veri alma
- **[PO Matching Pattern](po-matching-pattern.md)** - PO sonuçlarını kararlarda kullanma
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Kararlardan önce veriyi dönüştürme

---

## İlgili Kılavuzlar

### Önkoşullar
- [Condition Cards Complete Guide](../and/condition-cards-complete-guide.md) - Tüm koşul kartları
- [Field Manipulation Guide](../then/document-field/field-manipulation-guide.md) - Alan işlemleri
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Yönlendirme mantığı

### İlgili Kartlar
- **CONDITION_DOC_FIELD_AMOUNT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#field-conditions)
- **CONDITION_DOC_TYPE_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-doc-type-is-isnot)
- **CONDITION_SUPPLIER_STATUS_IS_ISNOT** - [Condition Cards Guide](../and/condition-cards-complete-guide.md#condition-supplier-status-is-isnot)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)

### Sonraki Adımlar
- Görevler oluşturun: [Task Management Pattern](task-management-pattern.md)
- Karmaşık eşleştirme ekleyin: [PO Matching Pattern](po-matching-pattern.md)
- API'leri entegre edin: [API Integration Pattern](api-integration-pattern.md)

---

**Kalıp Sürümü:** 1.0
**Son Güncelleme:** 23 Ekim 2025
**Zorluk:** Orta
**Tahmini Süre:** 30-45 dakika
**Başarı Oranı:** Yüksek

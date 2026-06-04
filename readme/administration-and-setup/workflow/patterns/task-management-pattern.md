# Task Management Pattern

**Kalıp Türü:** İş Akışı Yönetimi
**Karmaşıklık:** Düşük-Orta
**Tahmini Kurulum:** 30-45 dakika
**Yaygın Kullanım Durumları:** Onay iş akışları, inceleme görevleri, istisna yönetimi, yükseltme

---

Bu kalıbı **Workflow Builder**'da (Workflow Dashboard → Workflow List → Add Workflow) oluşturursunuz. Kart kütüphanesini açmak için **Add Card**'a tıklayın ve bu kalıbın kullandığı kartları seçin — `tasks_create`, `ACTION_ASSIGN_TO_USER`, `ACTION_SEND_EMAIL_TO_GROUPS` ve `CONDITION_TASK_STATUS` (**Assignee** kategorisi görev ve atama kartlarını içerir):

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Workflow Builder'da kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — görev, atama ve bildirim kartları <strong>Assignee</strong> ve <strong>Status</strong> kategorileri altında bulunur.</p></figcaption></figure>

---

## Kalıp Genel Bakışı

Bu kalıp, DocBits iş akışları içinde görevlerin nasıl oluşturulacağını, atanacağını, izleneceğini ve yönetileceğini gösterir. Görevler, belge iş akışının devam edebilmesi için tamamlanması gereken, kullanıcılara veya gruplara atanan eyleme dönük iş öğeleridir.

**Bu Kalıbın Yaptıkları:**
1. İş akışı koşullarına göre görevler oluşturur
2. Görevleri uygun kullanıcılara veya gruplara atar
3. Görev özelliklerini ayarlar (öncelik, son teslim tarihi, açıklama)
4. Görevler oluşturulduğunda bildirimler gönderir
5. Görev durumunu ve tamamlanmasını izler
6. Belgeleri görev sonuçlarına göre yönlendirir

---

## Bu Kalıbı Ne Zaman Kullanmalı

Bu kalıbı şu durumlarda kullanın:
- ✅ Onay iş akışları oluşturma
- ✅ İnceleme görevlerini kullanıcılara atama
- ✅ İnsan müdahalesi gerektiren istisnaları ele alma
- ✅ Sorunları yöneticilere yükseltme
- ✅ Çok düzeyli onay zincirleri oluşturma
- ✅ Kimin ne yapması gerektiğini izleme
- ✅ Eylemler için son teslim tarihleri belirleme

**Bu kalıbı şu durumlarda kullanmayın:**
- ❌ İnsan eylemi gerekmiyorsa (bunun yerine otomatik işlemeyi kullanın)
- ❌ Yalnızca bildirmeniz gerekiyorsa (bunun yerine e-posta kullanın)
- ❌ Basit belge yönlendirmesi (bunun yerine atamayı kullanın)

---

## Eksiksiz İş Akışı Örneği

### Senaryo: Tutar Tabanlı Yönlendirmeyle Fatura Onayı

**İş Gereksinimi:**
- Faturalar < €1.000: Otomatik onayla (görev gerekmez)
- Faturalar €1.000-€10.000: Yöneticiye onay görevi
- Faturalar > €10.000: Çift onay (Yönetici + Direktör)
- Tüm onaylayıcılar e-posta bildirimi alır
- Görevlerin 3 günlük son teslim tarihi vardır

**Kullanılan İş Akışı Kartları:**
1. CONDITION_DOC_FIELD_AMOUNT - Fatura tutarını kontrol et
2. tasks_create - Onay görevi oluştur
3. ACTION_ASSIGN_TO_USER - Görevi onaylayıcıya ata
4. ACTION_SEND_EMAIL_TO_GROUPS - Bildirim gönder
5. CONDITION_TASK_STATUS - Görevin tamamlanıp tamamlanmadığını kontrol et
6. ACTION_APPROVE_DOCUMENT - Görev tamamlandıktan sonra onayla

---

## Adım Adım Uygulama

### Adım 1: Tutar Eşiğini Kontrol Et

**Kart:** CONDITION_DOC_FIELD_AMOUNT veya benzer alan koşulu

**Yol 1 için Yapılandırma (< €1.000):**
```
Field: Total_Amount
Operator: IS LESS THAN
Value: 1000
Currency: EUR
```

**Yol 2 için Yapılandırma (€1.000-€10.000):**
```
Field: Total_Amount
Operator: IS BETWEEN
Value Min: 1000
Value Max: 10000
Currency: EUR
```

**Yol 3 için Yapılandırma (> €10.000):**
```
Field: Total_Amount
Operator: IS GREATER THAN
Value: 10000
Currency: EUR
```

**Kılavuz Referansı:** [Condition Cards Guide](../and/condition-cards-complete-guide.md)

---

### Adım 2A: Küçük Faturaları Otomatik Onayla (< €1.000)

**Küçük tutarlar için görev gerekmez**

**Kartlar:**
- ACTION_SET_FIELD_TO_TEXT
  - "Approval_Type" = "AUTO" olarak ayarla
  - "Approval_Reason" = "Amount below threshold" olarak ayarla
- ACTION_APPROVE_DOCUMENT

**Sonuç:** Belge otomatik olarak onaylanır, görev oluşturulmaz

---

### Adım 2B: Yönetici Onay Görevi Oluştur (€1.000-€10.000)

**Kart:** tasks_create (v4 önerilir)

**Yapılandırma:**
```json
{
  "task_type": "Approval",
  "task_title": "Approve Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "Please approve invoice from {{Supplier_Name}}\n\nAmount: €{{Total_Amount}}\nInvoice Number: {{Invoice_Number}}\nInvoice Date: {{Invoice_Date}}\n\nReview and approve within 3 business days.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "{{DOCUMENT_FIELD:Approving_Manager}}",
  "task_category": "Invoice Approval",
  "required_action": "Approve or Reject"
}
```

**Alan Eşlemesi:**
- `{{DOCUMENT_NUMBER}}` - Otomatik belge ID'si
- `{{Total_Amount}}` - Alan: Total_Amount
- `{{Supplier_Name}}` - Alan: Supplier_Name
- `{{Invoice_Number}}` - Alan: Invoice_Number
- `{{Invoice_Date}}` - Alan: Invoice_Date
- `{{Approving_Manager}}` - Alan veya sabit kullanıcı

**Kılavuz Referansı:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

---

### Adım 2C: Çift Onay Görevleri Oluştur (> €10.000)

**Yüksek tutarlı faturalar için iki ardışık görev**

**Görev 1: Yönetici Onayı**
```json
{
  "task_type": "First Approval",
  "task_title": "URGENT: Approve High-Value Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "HIGH VALUE INVOICE REQUIRES APPROVAL\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nThis invoice exceeds €10,000 and requires dual approval.\nYour approval is required before Director review.",
  "priority": "High",
  "deadline_days": 2,
  "assign_to": "Finance_Manager",
  "task_category": "High-Value Approval",
  "next_task": "Director_Approval"
}
```

**Görev 2: Direktör Onayı (Görev 1 tamamlandıktan sonra oluşturulur)**
```json
{
  "task_type": "Second Approval",
  "task_title": "Final Approval: Invoice {{DOCUMENT_NUMBER}} - €{{Total_Amount}}",
  "task_description": "FINAL APPROVAL REQUIRED\n\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\n\nFirst approval: Completed by {{Task1_Approver}} on {{Task1_Date}}\n\nYour final approval required.",
  "priority": "High",
  "deadline_days": 1,
  "assign_to": "Finance_Director",
  "task_category": "Final Approval",
  "prerequisite_task": "Manager_Approval"
}
```

---

### Adım 3: Görevi Kullanıcıya/Gruba Ata

**Kart:** ACTION_ASSIGN_TO_USER veya ACTION_ASSIGN_TO_GROUP

**Seçenek 1: Belirli Kullanıcıya Ata**
```
User: John.Smith@company.com
OR
User Field: {{DOCUMENT_FIELD:Approving_Manager}}
```

**Seçenek 2: Gruba Ata**
```
Group: Finance Managers
Assignment Mode: First Available
OR
Assignment Mode: Round Robin
OR
Assignment Mode: All (everyone in group gets task)
```

**Seçenek 3: Ardışık Atama**
```
Card: ACTION_ASSIGN_SEQUENTIALLY_TO_USER

User 1: Finance_Manager
User 2: Finance_Director (only if User 1 approves)
User 3: CFO (only if User 2 approves)
```

**Kılavuz Referansı:** [Assignment User Guide](../then/assignee/assignment-user-guide.md)

---

### Adım 4: E-posta Bildirimi Gönder

**Kart:** ACTION_SEND_EMAIL_TO_GROUPS

**Yapılandırma:**
```json
{
  "recipients": [
    "{{TASK_ASSIGNEE_EMAIL}}",
    "finance-notifications@company.com"
  ],
  "subject": "New Task Assigned: Approve Invoice {{DOCUMENT_NUMBER}}",
  "body": "Dear {{TASK_ASSIGNEE_NAME}},\n\nA new approval task has been assigned to you:\n\nTask: Approve Invoice {{DOCUMENT_NUMBER}}\nSupplier: {{Supplier_Name}}\nAmount: €{{Total_Amount}}\nDeadline: {{TASK_DEADLINE}}\nPriority: {{TASK_PRIORITY}}\n\nPlease log in to DocBits to review and approve:\n{{DOCUMENT_LINK}}\n\nBest regards,\nDocBits Automation"
}
```

**E-posta Değişkenleri:**
- `{{TASK_ASSIGNEE_EMAIL}}` - Görev atananının e-postası
- `{{TASK_ASSIGNEE_NAME}}` - Görev atananının adı
- `{{DOCUMENT_NUMBER}}` - Belge ID'si
- `{{TASK_DEADLINE}}` - Görev son teslim tarihi
- `{{TASK_PRIORITY}}` - Görev öncelik düzeyi
- `{{DOCUMENT_LINK}}` - Belgeye doğrudan bağlantı

**Kılavuz Referansı:** [Send Email Groups Guide](../then/action/send-email-groups-guide.md)

---

### Adım 5: Görev Durumunu İzle

**Kart:** CONDITION_TASK_STATUS veya benzer görev durumu denetleyicisi

**Yapılandırma:**
```
Task ID: {{CREATED_TASK_ID}}
Status Check: IS COMPLETED
```

**Durum Seçenekleri:**
- CREATED - Görev yeni oluşturuldu
- ASSIGNED - Görev kullanıcıya atandı
- IN_PROGRESS - Kullanıcı göreve başladı
- COMPLETED - Görev tamamlandı
- APPROVED - Görev onaylandı
- REJECTED - Görev reddedildi
- CANCELLED - Görev iptal edildi
- OVERDUE - Görev son teslim tarihini geçti

**Mantık:**
```
IF TASK_STATUS = COMPLETED AND TASK_RESULT = APPROVED:
  → Continue to next step (or next approval level)
  → Update document status
  → Log approval

IF TASK_STATUS = COMPLETED AND TASK_RESULT = REJECTED:
  → Stop workflow
  → Send rejection notification
  → Create review task for corrections

IF TASK_STATUS = OVERDUE:
  → Escalate to manager
  → Send reminder email
  → Create escalation task
```

---

### Adım 6: Görev Sonucuna Göre İş Akışını Tamamla

**Görev Tamamlandıktan Sonra:**

**Senaryo A: Görev Onaylandı**
```
1. Set field "Approval_Status" = "APPROVED"
2. Set field "Approved_By" = {{TASK_COMPLETED_BY}}
3. Set field "Approval_Date" = {{TASK_COMPLETED_DATE}}
4. ACTION_APPROVE_DOCUMENT
5. Export document (if configured)
```

**Senaryo B: Görev Reddedildi**
```
1. Set field "Approval_Status" = "REJECTED"
2. Set field "Rejected_By" = {{TASK_COMPLETED_BY}}
3. Set field "Rejection_Reason" = {{TASK_REJECTION_REASON}}
4. ACTION_REJECT_DOCUMENT
5. Send rejection notification to supplier
6. Create "Correction Needed" task
```

**Senaryo C: Görev Süresi Doldu**
```
1. Set field "Task_Status" = "OVERDUE"
2. Create escalation task for manager
3. Send reminder email to original assignee
4. Send escalation email to manager
5. Log overdue event
```

---

## Eksiksiz İş Akışı Diyagramı

```
INVOICE ARRIVES
│
├─ CHECK AMOUNT
│  │
│  ├─ Amount < €1,000 ✅
│  │  │
│  │  ├─ Set Approval_Type = "AUTO"
│  │  └─ Auto-Approve Document
│  │     → END (Approved)
│  │
│  ├─ Amount €1,000-€10,000 ⚠️
│  │  │
│  │  ├─ CREATE TASK: Manager Approval
│  │  │  - Title: "Approve Invoice"
│  │  │  - Priority: Medium
│  │  │  - Deadline: 3 days
│  │  │  │
│  │  │  ├─ ASSIGN TO: Finance Manager
│  │  │  │
│  │  │  ├─ SEND EMAIL: Notification
│  │  │  │
│  │  │  ├─ WAIT FOR TASK COMPLETION
│  │  │  │  │
│  │  │  │  ├─ TASK APPROVED ✅
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "APPROVED"
│  │  │  │  │  └─ Approve Document
│  │  │  │  │     → END (Approved)
│  │  │  │  │
│  │  │  │  ├─ TASK REJECTED ❌
│  │  │  │  │  │
│  │  │  │  │  ├─ Set Approval_Status = "REJECTED"
│  │  │  │  │  ├─ Reject Document
│  │  │  │  │  └─ Create Correction Task
│  │  │  │  │     → END (Rejected)
│  │  │  │  │
│  │  │  │  └─ TASK OVERDUE ⏰
│  │  │  │     │
│  │  │  │     ├─ Send Reminder Email
│  │  │  │     ├─ Escalate to Director
│  │  │  │     └─ Create Escalation Task
│  │  │  │        → WAIT (Escalated)
│  │  │  │
│  │  │  └─ [Task tracking active]
│  │  │
│  │  └─ [Manager approval path]
│  │
│  └─ Amount > €10,000 🚨
│     │
│     ├─ CREATE TASK 1: Manager First Approval
│     │  - Title: "URGENT: First Approval"
│     │  - Priority: High
│     │  - Deadline: 2 days
│     │  │
│     │  ├─ ASSIGN TO: Finance Manager
│     │  ├─ SEND EMAIL: High Priority Notification
│     │  │
│     │  ├─ WAIT FOR TASK 1 COMPLETION
│     │  │  │
│     │  │  ├─ TASK 1 APPROVED ✅
│     │  │  │  │
│     │  │  │  ├─ CREATE TASK 2: Director Final Approval
│     │  │  │  │  - Title: "Final Approval Required"
│     │  │  │  │  - Priority: High
│     │  │  │  │  - Deadline: 1 day
│     │  │  │  │  │
│     │  │  │  │  ├─ ASSIGN TO: Finance Director
│     │  │  │  │  ├─ SEND EMAIL: Final Approval Notification
│     │  │  │  │  │
│     │  │  │  │  ├─ WAIT FOR TASK 2 COMPLETION
│     │  │  │  │  │  │
│     │  │  │  │  │  ├─ TASK 2 APPROVED ✅
│     │  │  │  │  │  │  │
│     │  │  │  │  │  │  ├─ Set Dual_Approval = "COMPLETE"
│     │  │  │  │  │  │  └─ Approve Document
│     │  │  │  │  │  │     → END (Dual Approved)
│     │  │  │  │  │  │
│     │  │  │  │  │  └─ TASK 2 REJECTED ❌
│     │  │  │  │  │     │
│     │  │  │  │  │     ├─ Reject Document
│     │  │  │  │  │     └─ Notify All Parties
│     │  │  │  │  │        → END (Final Rejected)
│     │  │  │  │  │
│     │  │  │  │  └─ [Task 2 tracking]
│     │  │  │  │
│     │  │  │  └─ [Task 2 created]
│     │  │  │
│     │  │  └─ TASK 1 REJECTED ❌
│     │  │     │
│     │  │     ├─ Reject Document (No Task 2 created)
│     │  │     └─ Notify Supplier
│     │  │        → END (First Rejected)
│     │  │
│     │  └─ [Task 1 tracking]
│     │
│     └─ [Dual approval path]
│
└─ [Amount check complete]
```

---

## Yapılandırma Şablonları

### Şablon 1: Basit Onay Görevi

```json
{
  "card": "tasks_create",
  "task_title": "Approve {{DOCUMENT_TYPE}} {{DOCUMENT_NUMBER}}",
  "task_description": "Please review and approve this document.",
  "priority": "Medium",
  "deadline_days": 3,
  "assign_to": "approver@company.com",
  "category": "Approval"
}
```

---

### Şablon 2: Ayrıntılı İnceleme Görevi

```json
{
  "card": "tasks_create",
  "task_title": "Review Exception: {{EXCEPTION_TYPE}}",
  "task_description": "Document: {{DOCUMENT_NUMBER}}\nException: {{EXCEPTION_REASON}}\n\nDetails:\n- Supplier: {{Supplier_Name}}\n- Amount: €{{Total_Amount}}\n- Date: {{Document_Date}}\n\nAction Required: Review and resolve exception",
  "priority": "High",
  "deadline_days": 1,
  "assign_to_group": "Exceptions Team",
  "category": "Exception Handling"
}
```

---

### Şablon 3: Yükseltme Görevi

```json
{
  "card": "tasks_create",
  "task_title": "ESCALATION: {{ORIGINAL_TASK_TITLE}}",
  "task_description": "ESCALATED TASK\n\nOriginal Task: {{ORIGINAL_TASK_ID}}\nOriginal Assignee: {{ORIGINAL_ASSIGNEE}}\nDeadline Passed: {{ORIGINAL_DEADLINE}}\nDays Overdue: {{DAYS_OVERDUE}}\n\nPlease review and take immediate action.",
  "priority": "Urgent",
  "deadline_days": 1,
  "assign_to": "manager@company.com",
  "category": "Escalation",
  "parent_task": "{{ORIGINAL_TASK_ID}}"
}
```

---

## Gelişmiş Kalıplar

### Kalıp 1: Ardışık Çok Düzeyli Onay

**Kullanım:** Faturalar sırayla birden fazla onaylayıcıdan geçmelidir

```
Level 1: Accounts Clerk (verify data)
  → IF APPROVED:
    Level 2: Accounts Manager (approve amount)
      → IF APPROVED:
        Level 3: Finance Director (final sign-off)
          → IF APPROVED:
            Document Approved ✅
```

**Uygulama:**
```
1. Create Task 1 for Clerk
2. Wait for Task 1 completion
3. IF Task 1 = APPROVED:
     Create Task 2 for Manager
4. Wait for Task 2 completion
5. IF Task 2 = APPROVED:
     Create Task 3 for Director
6. Wait for Task 3 completion
7. IF Task 3 = APPROVED:
     Approve Document
```

---

### Kalıp 2: Paralel Çoklu Onaylayıcı

**Kullanım:** Birden fazla kişi aynı anda onaylamalıdır

```
Send to ALL approvers at once:
- Finance Manager
- Procurement Manager
- Quality Manager

Document approved only when ALL approve
```

**Uygulama:**
```
1. Create 3 tasks simultaneously
2. Track all 3 task statuses
3. WAIT until ALL tasks completed
4. IF ALL = APPROVED:
     Approve Document
   ELSE:
     Reject Document
```

---

### Kalıp 3: Koşullu Görev Oluşturma

**Kullanım:** Koşullara göre farklı görevler oluşturma

```
IF Supplier = "New":
  → Create "New Supplier Review" task
ELSE IF Amount > €50,000:
  → Create "High Value Approval" task
ELSE IF Document has errors:
  → Create "Error Correction" task
ELSE:
  → Create "Standard Approval" task
```

---

### Kalıp 4: Son Teslim Tarihi Tabanlı Yükseltme

**Kullanım:** Görev zamanında tamamlanmazsa otomatik yükseltme

```
Day 0: Create task for User A (3-day deadline)
Day 3: IF not completed:
         → Send reminder to User A
Day 4: IF still not completed:
         → Create escalation task for Manager B
         → Notify both User A and Manager B
Day 5: IF still not completed:
         → Create urgent task for Director C
         → High priority notification
```

---

## Hata Yönetimi

### Senaryo 1: Atanan Bulunamadı

**Sorun:** Kullanıcı yok veya etkin değil

**Çözüm:**
```
1. Check user status with CONDITION_USER_IS_ISNOT
2. IF User = INACTIVE:
     → Assign to backup user
     → OR Assign to user's group
     → Log warning
3. Send notification to admin
```

---

### Senaryo 2: Görev Oluşturma Başarısız

**Sorun:** Görev oluşturulurken sistem hatası

**Çözüm:**
```
1. Check task creation status
2. IF Failed:
     → Retry task creation
     → Send email notification instead
     → Create admin alert task
     → Log error details
```

---

### Senaryo 3: Göreve Yanıt Yok

**Sorun:** Kullanıcı görevi son teslim tarihine kadar tamamlamıyor

**Çözüm:**
```
1. Monitor task deadline
2. Day before deadline:
     → Send reminder email
3. On deadline day:
     → Send urgent reminder
4. After deadline:
     → Create escalation task
     → Notify manager
     → Log overdue event
```

---

## Test Kontrol Listesi

- [ ] Görev başarıyla oluşturuldu
- [ ] Görev doğru kullanıcıya/gruba atandı
- [ ] E-posta bildirimi gönderildi
- [ ] Görev kullanıcının görev listesinde görünüyor
- [ ] Görev özellikleri doğru (başlık, açıklama, öncelik, son teslim tarihi)
- [ ] Kullanıcı görevi tamamlayabiliyor
- [ ] İş akışı görev tamamlandıktan sonra devam ediyor
- [ ] Onay iş akışı doğru çalışıyor
- [ ] Reddetme iş akışı doğru çalışıyor
- [ ] Yükseltme doğru zamanda tetikleniyor
- [ ] Süresi dolma yönetimi çalışıyor
- [ ] Tüm e-posta bildirimleri gönderildi
- [ ] Alan güncellemeleri doğru çalışıyor

---

## Gerçek Dünya Örnekleri

### Örnek 1: Üç Yönlü PO Eşleştirme İstisnası

**Senaryo:** Fatura PO ile eşleşmiyor, inceleme gerekiyor

```
1. PO Matching fails (price variance > 5%)
2. Create Task: "Review PO Mismatch"
   - Assign to: Procurement Officer
   - Priority: High
   - Description: Include variance details
3. Send email with comparison table
4. Wait for task completion
5. IF Approved: Continue processing
   IF Rejected: Return to supplier
```

---

### Örnek 2: Tedarikçi Fatura Onayı

**Senaryo:** Yeni tedarikçi faturası özel onay gerektiriyor

```
1. Check if supplier is new (< 6 months old)
2. IF New:
     Create Task: "New Supplier Invoice Review"
     - Assign to: Procurement Manager
     - Include supplier details
     - Require supplier verification
3. After approval:
     Add to approved supplier list
     Continue normal workflow
```

---

### Örnek 3: Ay Sonu İşlemesi

**Senaryo:** Ay sonu faturaları acil işleme gerektiriyor

```
1. Check if document date in last 3 days of month
2. IF Yes:
     Create Task: "URGENT: Month-End Invoice"
     - Priority: Urgent
     - Deadline: 1 day
     - Assign to: Finance Team (all members)
     - Flag for expedited processing
3. Send urgent email notification
4. Track completion
```

---

## Performans İpuçları

✅ **En İyi Uygulamalar:**
- Gerçekçi son teslim tarihleri belirleyin
- Açık görev başlıkları ve açıklamaları kullanın
- Görevde gerekli tüm bilgileri ekleyin
- Zamanında bildirimler gönderin
- Görev tamamlanma oranlarını izleyin
- Süresi dolan görevleri otomatik yükseltin
- Tüm görev etkinliklerini günlüğe kaydedin
- Görev kalıplarını aylık gözden geçirin

❌ **Kaçının:**
- Her şey için görev oluşturma
- Belirsiz görev açıklamaları
- Gerçekçi olmayan son teslim tarihleri
- Çok fazla bildirim e-postası
- Yükseltme yolu olmaması
- Süresi dolan görevleri görmezden gelme
- Görev metriklerini izlememe

---

## İlgili Kalıplar

### İyi Birlikte Çalışan Kalıplar:

- **[API Integration Pattern](api-integration-pattern.md)** - API hataları için görevler oluşturma
- **[PO Matching Pattern](po-matching-pattern.md)** - PO uyuşmazlıkları için görevler oluşturma
- **[Decision Logic Pattern](decision-logic-pattern.md)** - Uygun görev türüne yönlendirme
- **[Data Transformation Pattern](data-transformation-pattern.md)** - Görev oluşturmadan önce veriyi dönüştürme

---

## İlgili Kılavuzlar

### Önkoşullar
- [Task Assignment Guide](../then/task/task-assignment-guide.md) - Görev kart belgeleri
- [Assignment User Guide](../then/assignee/assignment-user-guide.md) - Kullanıcı ataması
- [Send Email Groups Guide](../then/action/send-email-groups-guide.md) - E-posta bildirimleri

### İlgili Kartlar
- **tasks_create** - [Task Assignment Guide](../then/task/task-assignment-guide.md)
- **ACTION_ASSIGN_TO_USER** - [Assignment Guide](../then/assignee/assignment-user-guide.md)
- **ACTION_SEND_EMAIL_TO_GROUPS** - [Email Guide](../then/action/send-email-groups-guide.md)
- **CONDITION_TASK_STATUS** - [Condition Cards Guide](../and/condition-cards-complete-guide.md)

### Sonraki Adımlar
- E-posta bildirimleri ekleyin: [Send Email Guide](../then/action/send-email-groups-guide.md)
- Karmaşık yönlendirme uygulayın: [Decision Logic Pattern](decision-logic-pattern.md)
- Hataları ele alın: [Error Handling Pattern](error-handling-pattern.md)

---

**Kalıp Sürümü:** 1.0
**Son Güncelleme:** 23 Ekim 2025
**Zorluk:** Düşük-Orta
**Tahmini Süre:** 30-45 dakika
**Başarı Oranı:** Çok Yüksek

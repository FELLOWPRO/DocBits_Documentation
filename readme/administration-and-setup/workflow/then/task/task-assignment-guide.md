# Task Assignment & Creation Cards - Eksiksiz Kılavuz

**Kapsam:** 12 görevle ilgili kart

---

Bu sayfadaki görev kartları, Workflow Builder'ın **Then** grubuna gider — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p>Görev ve oluşturma kartları <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**En Çok Geliştirilen Kart:** tasks_create (4 sürüm, v4 en yeni)
**Diğer Çok Sürümlü Kartlar:** ACTION_TASK_FOR_GROUP (v4), ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3), ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3), ACTION_DECISION_TREE_CREATE_TASKS (v3)

**Temel Değişiklikler:**
- **v3 → v4 Evrimi:** Karar ağacı yaklaşımı kaldırıldı, genel iş öğesi türleri (Task, Ticket, Issue) eklendi
- **v2 → v3 Geçişi:** Karar ağacı desteği eklendi (artık çoğunlukla kullanımdan kaldırıldı)

📖 [Eksiksiz Sürüm Geçmişi](../../../changelog/release.md#-task-management-cards) | [Kart Sürüm Veritabanı](../../../../DocFlow/docs/card_version.md)

---

## Genel Bakış

Görev kartları, ekip üyeleri için iş atamaları oluşturur. Bir fatura onay gerektirdiğinde, otomatik olarak bir görev oluşturabilir ve doğru kişiye atayabilirsiniz.

---

# Temel Görev Oluşturma

## Kart: tasks_create / Görev Oluştur ve Kullanıcıya Ata

### Amaç
Bir görev oluşturur ve belirli bir kişiye atar

### Ne Zaman Kullanılır
- Fatura belirli bir kişinin incelemesine ihtiyaç duyar
- Adı belirtilen bir kişiden onay gerekir
- Belirli bir ekip üyesine devir

### Parametreler

**Başlık (Title)**
Görev adı/konusu
```
Example: "Review Invoice #INV-2025-001 for approval"
```

**Açıklama (Description)**
Görev hakkında ayrıntılar
```
Example: "Invoice from Supplier ABC needs review.
Amount: €5000
Deadline: 2025-10-30
Please verify pricing and quality."
```

**Öncelik (Priority)**
- 🔴 **High**: Acil, hemen yap
- 🟡 **Medium**: Normal öncelik
- 🟢 **Low**: Daha sonra yapılabilir

**Atanan Kullanıcı (Assigned User)**
Görevi kimin alacağı
```
Example: John Smith (Finance Manager)
```

**E-posta Bildirimi (Email Notification)**
Atanan kişiye e-posta uyarısı gönderilsin mi?
```
✅ Yes: Person gets email
❌ No: Task only in system
```

### Örnek
```
Condition: "Invoice amount > €10,000"
    ↓
Create Task:
- Title: "High-Value Invoice Review Required"
- Description: "Invoice #INV-2025-789 for €15,000 needs approval"
- Priority: High
- Assigned to: Sarah Johnson (Finance Approver)
- Send Email: Yes
    ↓
Sarah receives task and email notification
```

---

## Kart: ACTION_TASK_FOR_GROUP / Grup için Görev Oluştur

### Amaç
Bir görev oluşturur ve bir gruba atar (tüm üyeler görebilir)

### Ne Zaman Kullanılır
- Birden fazla kişi görevi yapabilir
- Birey için değil, ekip için görev
- İlk müsait kişi ele almalı

### Bireysel Görevden Farkı
```
Individual Task:
- Only John sees it
- John must do it
- Others can't see it

Group Task:
- Everyone in group sees it
- Any group member can claim it
- Distributed workload
```

### Örnek İş Akışı
```
Document arrives
    ↓
Condition: "Is supplier new?"
    ↓
Create Task for Procurement Team:
- Title: "Verify New Supplier Details"
- Description: "Please validate supplier information"
- Priority: Medium
- Group: Procurement Team (10 members)
- Notify: Yes
    ↓
All 10 procurement team members see task
First person available takes it
```

---

## Kart: ACTION_DECISION_TREE_CREATE_TASKS

### Amaç
Karar tablosu mantığına göre görevler oluşturur

### Nasıl Çalışır
```
Decision Table Returns:
  If invoice from Supplier A → Assign to Procurement
  If invoice from Supplier B → Assign to Quality Team
  If invoice from Supplier C → Assign to Finance

Task is automatically created and assigned
based on which condition is true
```

### Ne Zaman Kullanılır
- Farklı tedarikçiler farklı onay gerektirir
- Birden fazla faktöre dayalı karmaşık yönlendirme
- Belge türüne göre farklı ekip

### Örnek
```
Document: Invoice from ABC Corp (Supplier A)
    ↓
Decision Table checks: Which supplier?
    ↓
Result: Supplier A → Procurement Team
    ↓
Create and assign task to Procurement Team
```

---

## Kart: ACTION_DECISION_TREE_TASKS_SEQUENTIAL

### Amaç
Karar tablosuna göre görevleri ardışık olarak oluşturur
Görevler öncelik sırasıyla birer birer atanır

### Ne Zaman Kullanılır
- Sırayla birden fazla onay gerekir
- İş akışı onay zinciri
- Her kişi inceler sonra bir sonrakine geçirir

### Nasıl Çalışır
```
Step 1: Create Task for Procurement Manager
        (Priority 1)
    ↓
Step 2: Procurement Manager approves
    ↓
Step 3: Create Task for Finance Manager
        (Priority 2)
    ↓
Step 4: Finance Manager approves
    ↓
Step 5: Export
```

### Öncelik Sistemi
```
Priority 1 → Assign to: Person A
Priority 2 → Assign to: Person B
Priority 3 → Assign to: Person C

They must complete in order (1→2→3)
```

### Örnek Yapılandırma
```
Decision Table Returns:
  Level 1: Sarah Johnson (Finance)
  Level 2: Mike Smith (Manager)
  Level 3: Director (for approval)

Task Flow:
1. Sarah reviews → Comments
2. Passes to Mike → He reviews
3. Passes to Director → Final approval
4. All complete → Export
```

---

## Kart: ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL

### Amaç
Belgeyi bir kullanıcıya atar VE ardışık görev oluşturur

### Ne Zaman Kullanılır
- Belgeyi atama VE aynı anda görev oluşturma
- Belge belirli bir kişi tarafından incelenmesi gerekir
- Hem atamayı hem görev oluşturmayı izleme

### Nasıl Çalışır
```
Two things happen:
1. Document is assigned to: Person A
2. Task is created for: Person A

Both in one action
```

### Örnek
```
High-value invoice arrives
    ↓
ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL:
- Assign Document to: Finance Manager
- Create Task: "Review & Approve High Value Invoice"
- Priority: High
    ↓
Document AND task both go to Finance Manager
```

---

## Kart: ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL

### Amaç
Belgeyi gruba atar VE görev oluşturur

### Ne Zaman Kullanılır
- Belge grup dikkati gerektirir
- Görev oluşturmayı izlemek istiyorsanız
- Önce ilk görevi sonra belge atamasını oluşturma

### Örnek
```
New supplier evaluation
    ↓
ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL:
- Document assigned to: Supplier Management Group
- Create Task: "Evaluate New Supplier Credentials"
- Assign Task to: Same group
- Priority: Medium
    ↓
Group members see document and task
```

---

# Gelişmiş Görev Oluşturma

## Kart: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP

### Amaç
Belirli bir tesis grubu için görev oluşturur

### Ne Zaman Kullanılır
- Depo/tesis ekibi için görev
- Tesise özgü operasyonlar
- Fiziksel konum önemli

### Örnek
```
Document: Shipment notification
    ↓
Create Task for Facility Group:
- Group: Berlin Warehouse Team
- Task: "Prepare items for shipment"
- Items: From document
    ↓
Berlin warehouse team gets task
```

---

## Kart: ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL

### Amaç
Tesisler arasında ardışık görev ataması

### Ne Zaman Kullanılır
- Çok tesisli operasyonlar
- Görevler tesisten tesise geçer
- Ardışık tesis işleme

### Nasıl Çalışır
```
Factory A (Step 1): Production
    ↓
Quality Check (Step 2): Verification
    ↓
Warehouse (Step 3): Packaging
    ↓
Shipping (Step 4): Dispatch
```

### Örnek
```
Manufacturing Document
    ↓
Create Sequential Tasks:
- Task 1: Factory A (Manufacturing) - Priority 1
- Task 2: Quality Team (Testing) - Priority 2
- Task 3: Warehouse (Packing) - Priority 3
- Task 4: Shipping (Dispatch) - Priority 4
    ↓
Each team completes → Passes to next
```

---

## Kart: ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP

### Amaç
Satınalma departmanı için görev oluşturur

### Ne Zaman Kullanılır
- Satınalma ekibi için görev
- Tedarikçi yönetimi görevleri
- Satın almayla ilgili iş

### Örnek
```
Supplier status change notification
    ↓
Create Task for Procurement Group:
- Task: "Update supplier records"
- Supplier: ABC Corp
- Action: Change status to 'On Hold'
- Priority: High
    ↓
Procurement team is notified
```

---

## Kart: ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL

### Amaç
Satınalma içinde ardışık görev yönlendirmesi

### Ne Zaman Kullanılır
- Çok adımlı satınalma süreçleri
- Satınalmada onay zinciri
- Yükseltme yolu

### Örnek
```
Purchase Requisition received
    ↓
Step 1: Buyer verifies (Priority 1)
    ↓
Step 2: Approver approves (Priority 2)
    ↓
Step 3: Director signs off (Priority 3)
    ↓
All sign-offs complete → Release to supplier
```

---

## Kart: ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK

### Amaç
Kullanıcıyı belge alanından al, görev ata
Kullanıcı bulunmazsa, yedek kullanıcıyı kullan

### Ne Zaman Kullanılır
- Kullanıcı belge alanında depolanmış
- Belge kimin inceleyeceğini belirtir
- Belirtilen kullanıcı kullanılamıyorsa yedek kişi olması

### Nasıl Çalışır
```
Document has field: "Approver Name: John Smith"

Card checks: Is John in system?
    If YES → Assign task to John
    If NO → Assign to Fallback User (Sarah)
```

### Örnek
```
Invoice field: "Contact: Mike Johnson"

Try to assign task to Mike Johnson
    ↓
If Mike doesn't exist in system:
    ↓
Use Fallback: Team Lead (Robert Brown)
```

### Parametreler
```
- Field to Read: "Approver Name"
- Fallback User: Robert Brown
- Task Details: Title, Description, Priority
```

---

# Yaygın Görev Parametreleri

Tüm görev kartları bu parametreleri kullanır:

### Başlık
```
Good: "Review Invoice #INV-12345 - €5000 - Supplier ABC"
Bad: "Approve something"
```

### Açıklama
```
Should include:
✅ What to do
✅ Deadline
✅ Any special requirements
✅ Who to contact
✅ Link to document
```

### Öncelik Düzeyleri
```
🔴 HIGH
   - Action needed within hours
   - Blocks other processes
   - Example: Supply missing, urgent approval

🟡 MEDIUM
   - Standard processing
   - Normal timeline
   - Example: Regular invoice review

🟢 LOW
   - Can wait days/weeks
   - Non-urgent
   - Example: Archive old documents
```

### Son Teslim Tarihi (varsa)
```
When should task be completed by?
Example: 2025-10-30 (5 days from now)
```

---

# Görev İş Akışı Senaryoları

## Senaryo 1: Basit Onay
```
Invoice Arrives (€2000)
    ↓
Condition: Amount between €1000-€5000?
    ↓
YES: Create Task for Finance Manager
    ↓
Finance Manager reviews and approves
```

## Senaryo 2: Çok Düzeyli Onay
```
Invoice Arrives (€50,000 - High Value)
    ↓
Create Sequential Tasks:
1. Finance Team (Initial review)
2. Finance Manager (Approval)
3. Director (Final sign-off)
    ↓
Each level completes → Next begins
```

## Senaryo 3: Paralel Görevler
```
Invoice Arrives (From New Supplier)
    ↓
Create Task 1: Quality Team (verify supplier)
Create Task 2: Finance Team (check prices)
Create Task 3: Procurement (check contract)
    ↓
All teams work simultaneously
All must complete before proceeding
```

## Senaryo 4: Koşullu Yönlendirme
```
Invoice Arrives
    ↓
Decision Table:
  If amount > €10k → Assign to Director
  If amount €1k-€10k → Assign to Manager
  If amount < €1k → Assign to Team Lead
    ↓
Task created for correct person
```

---

# Görev Atama En İyi Uygulamaları

✅ **Yapın:**
- Görev başlığına belirli ayrıntılar ekleyin
- Uygun öncelik düzeyleri ayarlayın
- Gerçekçi son teslim tarihleri ayarlayın
- Atananları bilgilendirin
- Belgeye bağlantı ekleyin
- Açık, eyleme dönük açıklamalar kullanın

❌ **Yapmayın:**
- Belirsiz görev başlıkları oluşturma ("Review this")
- Her şeyi High öncelik olarak ayarlama
- Atanan kişiyi bilgilendirmeyi unutma
- Aynı iş için birden fazla görev oluşturma
- Kullanılamayan kişilere atama

---

# Görevlerde Sorun Giderme

## "Görev kimseye atanmadı"
**Neden:** Kullanıcı yok veya grup boş

**Çözüm:**
- Kullanıcı adı yazımını doğrulayın
- Kullanıcının sistemde etkin olduğunu kontrol edin
- Grubun üyesi olduğunu doğrulayın
- Gerekirse yedek kullanın

## "Kişi bildirim almadığını söylüyor"
**Neden:** E-posta bildirimi devre dışı veya e-posta yanlış

**Çözüm:**
- "Send Email" onay kutusunun etkin olduğunu kontrol edin
- Alıcı e-posta adresini doğrulayın
- Spam klasörünü kontrol edin
- Bildirimi manuel olarak yeniden gönderin

## "Yanlış kişi görevi aldı"
**Neden:** Yönlendirme mantığı yanlış

**Çözüm:**
- Karar tablosu koşullarını kontrol edin
- Yedek ayarlarını doğrulayın
- Örnek belgeyle test edin
- Kullanıcı adlarında yazım hatası olup olmadığını kontrol edin

## "Çok fazla görev oluşturuldu"
**Neden:** Kart birden fazla kez tetikleniyor

**Çözüm:**
- Koşulların yeterince belirli olduğunu kontrol edin
- Kartın belge başına yalnızca bir kez çalıştığını doğrulayın
- "And" koşullarını gözden geçirin
- Ek filtreleme ekleyin

---

# Görev Kartı Karşılaştırma Tablosu

| Kart | Görev Oluşturur | Şuna Atar | Ne Zaman |
|------|-------------|-----------|------|
| tasks_create | Evet | Birey | Her zaman |
| ACTION_TASK_FOR_GROUP | Evet | Grup | Her zaman |
| ACTION_DECISION_TREE_CREATE_TASKS | Evet | Karar Tablosu Sonucu | Koşullu |
| ACTION_DECISION_TREE_TASKS_SEQUENTIAL | Evet | Birden Fazla (Ardışık) | Koşullu |
| ACTION_CREATE_TASK_FOR_USER_SEQUENTIAL | Evet | Kullanıcı + Belge | Koşullu |
| ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL | Evet | Grup + Belge | Koşullu |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP | Evet | Tesis Grubu | Koşullu |
| ACTION_ASSIGN_TASK_TO_FACILITY_GROUP_SEQUENTIAL | Evet | Birden Fazla Tesis | Koşullu |
| ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP | Evet | Satınalma Ekibi | Koşullu |
| ACTION_ASSIGN_TASK_PROCUREMENT_GROUP_SEQUENTIAL | Evet | Birden Fazla (Ardışık) | Koşullu |
| ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK | Evet | Alan/Yedek | Koşullu |

---

# İlgili Kartlar

- **ACTION_ASSIGN_DOCUMENT_TO_USER** - Görev oluşturmadan belge ata
- **ACTION_SEND_EMAIL** - Kişileri doğrudan bilgilendir
- **STAUS_CHANGE** - Görev oluşturmak yerine durumu değiştir
- **RUN_WORKFLOW** - Bunun yerine farklı bir iş akışını tetikle

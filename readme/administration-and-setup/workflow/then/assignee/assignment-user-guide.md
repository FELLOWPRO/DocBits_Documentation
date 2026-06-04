# Document Assignment & User Cards - Eksiksiz Kılavuz

**Kapsam:** 13 atama ve kullanıcıyla ilgili kart

---

Bu sayfadaki kartlar, Workflow Builder'ın **Then** grubuna gider — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p>Atama ve kullanıcı kartları <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Çok Sürümlü Kartlar:** DOC_USER_ASSIGN (v2 en yeni, v3 kullanımdan kaldırıldı), DOC_GROUP_ASSIGN (v2 en yeni, v3 kullanımdan kaldırıldı), OC_ASSIGN_DOC (v2)

**Önemli:** v3 sürümleri karar ağacı desteği ekledi ancak artık kullanımdan kaldırıldı
**Öneri:** Hem DOC_USER_ASSIGN hem de DOC_GROUP_ASSIGN için v2 kullanın

📖 [Eksiksiz Sürüm Geçmişi](../../../changelog/release.md#-assignment--routing-cards) | [Kart Sürüm Veritabanı](../../../../DocFlow/docs/card_version.md)

---

# Temel Belge Ataması

## Kart: DOC_USER_ASSIGN / Belgeyi Kullanıcıya Ata

### Amaç
Belgeyi, eylemi için belirli bir kişiye atar

### Ne Zaman Kullanılır
- Belge belirli bir kişinin incelemesine ihtiyaç duyar
- Bireysel ekip üyesine devir
- Hesap verebilirlik izleme
- İşi adı belirtilen kişiye atama

### Nasıl Çalışır
```
Document is "assigned to" = John Smith
Only John can see it as assigned to him
John is responsible for this document
```

### Örnek
```
Invoice arrives
    ↓
Assign Document to: John Smith (Finance Manager)
    ↓
Only John sees "Assigned to Me"
John must take action on it
```

### Parametreler
```
User: [Select which person]
```

### Not
Atamak şu anlama gelir:
- Belge o kişi için "assigned to me" olarak görünür
- O kişi sorumludur
- Diğerleri belgeyi hâlâ görebilir (ancak kendilerine atanmış olarak değil)
- Belge başına aynı anda bir atama

---

## Kart: DOC_GROUP_ASSIGN / Belgeyi Gruba Ata

### Amaç
Belgeyi bir gruba atar (tüm üyeler onu kendilerine atanmış olarak görür)

### Ne Zaman Kullanılır
- Birey için değil, ekip için belge
- Birden fazla kişi ele alabilir
- Paylaşılan sorumluluk
- Ekip iş yükü dağılımı

### Nasıl Çalışır
```
Document is "assigned to" = Finance Team (10 people)
All 10 team members see "Assigned to My Group"
Any team member can take action
```

### Örnek
```
New vendor invoice
    ↓
Assign Document to: Procurement Team
    ↓
All procurement team members see it
First available person handles it
```

### Parametreler
```
Group: [Select which group]
```

### Fark
```
Individual Assignment:
- One person responsible
- That person sees "Assigned to Me"
- Others don't see assignment

Group Assignment:
- Team responsible
- All members see "Assigned to My Group"
- Anyone can claim/process
```

---

## Kart: ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE

### Amaç
Belgeyi karar tablosu mantığına göre atar

### Ne Zaman Kullanılır
- Farklı tedarikçiler farklı işleyiciler gerektirir
- Tutara göre atama
- Karmaşık yönlendirme mantığı
- Atama için birden fazla koşul

### Nasıl Çalışır
```
Decision Table Logic:
  If Supplier = "ABC Corp" → Assign to: Procurement Team
  If Supplier = "XYZ Inc" → Assign to: Direct Manager
  If Amount > €10000 → Assign to: Finance Director

Document arrives
    ↓
Check: Which condition matches?
    ↓
Assign accordingly
```

### Örnek: Tutar Tabanlı Atama
```
Invoice: €2000 from ABC Corp

Decision Table checks:
  Is amount > €10000? NO
  Is amount > €5000? NO
  Is amount > €1000? YES

Result: Assign to: Finance Manager
```

### Örnek: Tedarikçi Tabanlı Atama
```
Invoice from: Preferred Supplier

Decision Table:
  If preferred supplier → Finance Team
  If new supplier → Procurement Manager
  If blacklisted → Director Review

Result: Assign to: Finance Team
```

### Parametreler
```
Decision Table: [Select decision table]
(Decision table contains assignment logic)
```

---

## Kart: ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL

### Amaç
Belgeyi önceliklerle karar tablosuna göre ardışık olarak atar

### Ne Zaman Kullanılır
- Birden fazla ardışık onay
- Farklı düzeylerde farklı kişiler
- Tutara göre onay zinciri
- Yükseltme yolu

### Nasıl Çalışır
```
First Decision: Who approves first?
    ↓
Assign to: Person 1
    ↓
Person 1 approves
    ↓
Second Decision: Who approves next?
    ↓
Assign to: Person 2
    ↓
Person 2 approves (final)
    ↓
Document Complete
```

### Öncelik Sistemi
```
Priority 1: First assignment
Priority 2: Second assignment
Priority 3: Third assignment
(etc.)

Each must complete before next begins
```

### Örnek: Çok Düzeyli Onay
```
Invoice: €50,000

Decision Table:
  €1k-€5k → Assign to: Finance Manager (Priority 1)
  €5k-€20k → Then: Assign to: Finance Director (Priority 2)
  €20k+ → Then: Assign to: CFO (Priority 3)

Invoice Flow:
1. Finance Manager reviews → approves
2. Finance Director reviews → approves
3. CFO reviews → approves final

Each step depends on previous completion
```

### Parametreler
```
Decision Table: [Select]
Priority Order: [Determined by decision table]
```

---

## Kart: ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL

### Amaç
Belgeyi ardışık öncelikle kullanıcıya atar

### Ne Zaman Kullanılır
- Belge belirli bir kişiye ihtiyaç duyar
- Açık ardışık işleme
- Sıralı tek atama

### Nasıl Çalışır
```
Assign Document to: User A (Priority 1)
    ↓
User A processes
    ↓
Then: Assign to User B (Priority 2)
    ↓
User B processes
```

### Örnek
```
Invoice processing:
1. Assign to: Accounts Payable Clerk
2. Then: Assign to: Finance Manager
3. Then: Assign to: Director

Each person has their turn
```

---

## Kart: ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL

### Amaç
Belgeyi gruplara ardışık olarak atar

### Ne Zaman Kullanılır
- Birden fazla grup onayı
- Her aşamada farklı departmanlar
- Ekip tabanlı ardışık işleme

### Nasıl Çalışır
```
Step 1: Assign to Group A (Quality Team)
        Quality verifies
    ↓
Step 2: Assign to Group B (Finance Team)
        Finance reviews
    ↓
Step 3: Assign to Group C (Procurement)
        Procurement approves
```

### Örnek
```
New Supplier Onboarding:

Step 1: Quality Team
  - Evaluate supplier capability
  - Check certifications

Step 2: Finance Team
  - Check payment terms
  - Verify pricing

Step 3: Procurement Team
  - Approve supplier
  - Set up in system

Document passes through all three
```

---

## Kart: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP

### Amaç
Belgeyi belirli bir tesis grubuna atar

### Ne Zaman Kullanılır
- Belirli bir depo/tesis için belge
- Tesis tabanlı operasyonlar
- Konuma özgü işleme

### Örnek
```
Shipment notification

Assign to: Berlin Warehouse Team
    ↓
Berlin warehouse processes shipment
    ↓
Or

Assign to: Munich Warehouse Team
    ↓
Munich warehouse processes shipment
```

---

## Kart: ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL

### Amaç
Tesisler arasında ardışık olarak atar

### Ne Zaman Kullanılır
- Çok konumlu işleme
- Sevkiyat tesislerden geçer
- Konum tabanlı iş akışı

### Örnek
```
Manufacturing Order:

Step 1: Factory A (Manufacturing) - Build product
Step 2: Quality Center (Testing) - Test product
Step 3: Distribution Center (Packing) - Package
Step 4: Warehouse (Storage) - Store

Document/shipment passes through each
```

---

## Kart: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP

### Amaç
Belgeyi satınalma departmanına atar

### Ne Zaman Kullanılır
- Satınalma ekibi tarafından ele alma
- Tedarikçiyle ilgili iş
- Satınalma siparişiyle ilgili

### Örnek
```
Vendor evaluation document
    ↓
Assign to: Procurement Group
    ↓
Procurement team evaluates vendor
```

---

## Kart: ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL

### Amaç
Satınalma içinde ardışık atama

### Ne Zaman Kullanılır
- Çok adımlı satınalma süreci
- Satınalmada onay zinciri

### Örnek
```
Purchase Requisition:

Step 1: Buyer (Creates PO)
Step 2: Approver (Reviews)
Step 3: Director (Final sign-off)

Each step in sequence
```

---

## Kart: ACTION_CHANGE_DOC_SUBORG / Belge Alt Kuruluşunu Değiştir

### Amaç
Belgeyi farklı bir alt kuruluşa atar

### Ne Zaman Kullanılır
- Yanlış kuruluş seçildi
- Doğru departmana taşıma gerekiyor
- Kurumsal yeniden yapılandırma

### Nasıl Çalışır
```
Current Sub-Org: Finance Department
    ↓
Change to: Accounting Department
    ↓
Document now belongs to Accounting
```

### Örnek
```
Document for: Berlin Office
    ↓
Realize should be: Munich Office
    ↓
Change Sub-Organization to: Munich Office
```

---

## Kart: ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT

### Amaç
Belge alanı değerine göre alt kuruluşu değiştirir

### Ne Zaman Kullanılır
- Alt kuruluş bir alanda depolanmış
- Belge konumunu alanla eşleştirme
- Otomatik kuruluş ataması

### Nasıl Çalışır
```
Document Field: "Delivery_Location" = "Berlin"
    ↓
Decision Table:
  If location = "Berlin" → Assign to: Berlin Sub-Org
  If location = "Munich" → Assign to: Munich Sub-Org

    ↓
Document assigned to: Berlin Sub-Org
```

### Örnek
```
Invoice field: "Cost Center: CC-Berlin-001"
    ↓
System recognizes: Berlin location
    ↓
Change document to: Berlin Sub-Organization
```

---

## Kart: ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK

### Amaç
Belgeyi bir alandaki kullanıcıya atar, kullanıcı bulunmazsa yedekle

### Ne Zaman Kullanılır
- Kullanıcı adı belge alanında depolanmış
- Sistemde mevcut olmayabilir
- Kullanıcı kullanılamıyorsa yedek gerekiyor

### Nasıl Çalışır
```
Document Field: "Approver: John Smith"
    ↓
Try to assign to: John Smith
    ↓
If John doesn't exist:
    ↓
Use Fallback: Sarah Johnson (Manager)
    ↓
Document assigned to: Sarah Johnson
```

### Parametreler
```
Source Field: [Field containing user name]
Fallback User: [If source user not found]
```

### Örnek
```
Invoice has field: "Contact Person: Mike Johnson"

Try to assign to: Mike Johnson
    ↓
If Mike not in system:
    ↓
Fallback to: Finance Manager (Robert)
```

---

## Kart: ACTION_ASSIGN_USER_TO_SUPPLIER

### Amaç
Belgeyi o tedarikçiyi yöneten kullanıcıya atar

### Ne Zaman Kullanılır
- Kullanıcı tedarikçiye bağlı
- Tedarikçi hesap yöneticisi
- Tedarikçi ilişkisi sahibi

### Nasıl Çalışır
```
Document Supplier: ABC Corp
    ↓
System checks: Who manages ABC Corp?
    ↓
Assign to: John Smith (ABC Corp Account Manager)
```

---

# Atama Karar Ağaçları

## Karar Tablosu Örneği 1: Tutar Tabanlı
```
Amount ≤ €1000
  → Assign to: Finance Team

Amount €1000-€5000
  → Assign to: Finance Manager

Amount €5000-€20000
  → Assign to: Finance Director

Amount > €20000
  → Assign to: CFO
```

## Karar Tablosu Örneği 2: Tedarikçi Tabanlı
```
Supplier Type = "Preferred"
  → Assign to: Account Manager

Supplier Type = "New"
  → Assign to: Procurement Manager

Supplier Type = "Problem"
  → Assign to: Procurement Director
```

## Karar Tablosu Örneği 3: Belge Türü Tabanlı
```
Document Type = "Invoice"
  → Assign to: Accounts Payable Team

Document Type = "Credit Memo"
  → Assign to: Finance Manager

Document Type = "PO"
  → Assign to: Procurement Team
```

---

# Atama İş Akışı Örnekleri

## Örnek 1: Basit Yönlendirme
```
Document Arrives
    ↓
Check: Supplier = "ABC Corp"? YES
    ↓
Assign to: John Smith
(John handles ABC Corp)
    ↓
John reviews and approves
```

## Örnek 2: Ardışık Onay
```
Document Arrives
    ↓
Assign to: Finance Manager (Step 1)
    ↓
Manager reviews
    ↓
Passes to: Finance Director (Step 2)
    ↓
Director reviews
    ↓
Passes to: CFO (Step 3)
    ↓
CFO approves final
```

## Örnek 3: Tutar Tabanlı Yönlendirme
```
Invoice: €50,000
    ↓
Decision Table: Amount > €20k?
    ↓
YES → Assign to: CFO
    ↓
CFO approves directly
```

## Örnek 4: Tesis Tabanlı
```
Shipment for: Berlin Office
    ↓
Assign to: Berlin Warehouse Team
    ↓
Then assign to: Berlin Distribution Team
    ↓
Both teams process in sequence
```

---

# Atama En İyi Uygulamaları

✅ **Yapın:**
- Karar tablolarını basit tutun
- Yönlendirme mantığını örneklerle test edin
- Tüm yolların bir yere ulaştığından emin olun
- Eksik kullanıcılar için yedek bulundurun
- Yönlendirme kararlarını belgeleyin

❌ **Yapmayın:**
- Döngüsel atamalar oluşturma (A→B→A)
- Var olmayan kullanıcılara atama (yedek olmadan)
- Yönlendirmeyi çok karmaşık yapma
- Yönlendirmeyi test etmeyi unutma
- Kullanılamayan kişilere atama

---

# Atama Sorun Giderme

## "Belge atanmadı"
**Neden:** Koşul karşılanmadı veya kullanıcı yok

**Çözüm:**
- Koşulun doğru olduğunu kontrol edin
- Kullanıcının sistemde var olduğunu doğrulayın
- Yedek ayarlarını kontrol edin
- Karar tablosu mantığını gözden geçirin

## "Yanlış kişi atandı"
**Neden:** Karar tablosu veya yönlendirme mantığı yanlış

**Çözüm:**
- Karar tablosunu test edin
- Koşulları kontrol edin
- Kullanıcı eşlemesini doğrulayın
- Alan değerlerini gözden geçirin

## "Atama birini atlıyor gibi görünüyor"
**Neden:** Ardışık sıra yanlış

**Çözüm:**
- Öncelik sayılarını kontrol edin
- Sıranın doğru olduğunu doğrulayın
- Örnekle test edin
- Karar tablosu sıralamasını gözden geçirin

---

# Atama Kartları Karşılaştırması

| Kart | Şuna Atar | Yönlendirme Türü | Kullanım Durumu |
|------|-----------|-----------|----------|
| DOC_USER_ASSIGN | Birey | Doğrudan | Basit atama |
| DOC_GROUP_ASSIGN | Grup | Doğrudan | Ekip ataması |
| ACTION_ASSIGN_DOC_BASED_ON_DECISION_TABLE | Karar Sonucu | Koşullu | Karmaşık yönlendirme |
| ACTION_ASSIGN_DOC_DECISION_TABLE_SEQUENTIAL | Birden Fazla (Ardışık) | Koşullu | Onay zinciri |
| ACTION_ASSIGN_DOC_TO_USER_SEQUENTIAL | Kullanıcı (Ardışık) | Sıralı | Ardışık kullanıcı adımları |
| ACTION_ASSIGN_DOC_TO_GROUP_SEQUENTIAL | Gruplar (Ardışık) | Sıralı | Ardışık grup adımları |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP | Tesis Grubu | Doğrudan | Tesise özgü |
| ACTION_ASSIGN_DOC_TO_FACILITY_GROUP_SEQUENTIAL | Tesisler (Ardışık) | Sıralı | Çoklu tesis |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP | Satınalma | Doğrudan | Satınalma iş akışı |
| ACTION_ASSIGN_DOC_TO_PROCUREMENT_GROUP_SEQUENTIAL | Satınalma (Ardışık) | Sıralı | Satınalma onay zinciri |
| ACTION_CHANGE_DOC_SUBORG | Alt Kuruluş | Doğrudan | Departman değişikliği |
| ACTION_CHANGE_DOC_SUBORG_BY_FIELD_TEXT | Alana Göre Alt Kuruluş | Koşullu | Alan tabanlı atama |
| ACTION_ASSIGN_USER_FROM_FIELD_WITH_FALLBACK | Alan/Yedek | Koşullu | Dinamik kullanıcı ataması |

---

# İlgili Kartlar

- **ACTION_CREATE_TASK_FOR_USER** - Görevi aynı kişiye ata
- **ACTION_SEND_EMAIL** - Atanan kişiyi bilgilendir
- **CONDITION_USER_IS_ISNOT** - Doğru kişinin atanıp atanmadığını kontrol et
- **CONDITION_GROUP_IS_ISNOT** - Doğru grubun atanıp atanmadığını kontrol et

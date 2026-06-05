# Card Versioning System - October 2025 Update

**Belge:** Workflow Card Versioning Overview
**Son Güncelleme:** 23 Ekim 2025
**Durum:** Tamamlandı

---

## Genel Bakış

DocBits Workflow Engine, geriye dönük uyumluluğu korurken kart evrimini yönetmek için **tamsayı tabanlı sürümleme** kullanır. Bu belge, sürümleme sistemine genel bir bakış sunar.

---

## Card Versioning Nedir?

### Kavram
Her workflow kartının birden fazla sürümü olabilir, bu da sistemin şunları yapmasına olanak tanır:
- Mevcut iş akışlarını bozmadan yeni özellikler ekleme
- Kullanımdan kaldırılan işlevselliği aşamalı olarak devre dışı bırakırken destekleme
- Kart yeteneklerini zaman içinde geliştirme
- Geriye dönük uyumluluğu koruma

### Sürüm Yapısı
- **Biçim:** Tamsayı değerleri (1, 2, 3, 4, 5...)
- **Tanımlama:** (card_type, card_version) bileşik anahtarı
- **Durum:** Her sürümün deprecated/enabled bayrakları vardır

### Örnek
`tasks_create` kartı 4 sürüm boyunca gelişmiştir:
- **v1:** Orijinal görev oluşturma (kullanımdan kaldırıldı)
- **v2:** Çeviri desteği eklendi (kullanımdan kaldırıldı)
- **v3:** Deneysel karar ağacı desteği (kullanımdan kaldırıldı)
- **v4:** Generic iş öğesi türü desteği (mevcut etkin)

---

## Önemli İstatistikler

### Sürümlemeye Genel Bakış
| Metrik | Değer |
|--------|-------|
| **Birden Fazla Sürümü Olan Kartlar** | 30+ |
| **Toplam Sürüm Kaydı** | 90+ |
| **Kart Başına Sürüm (ortalama)** | 3 |
| **Maksimum Sürüm** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |
| **Kullanımdan Kaldırılan Sürümler** | 9 |
| **Tamamen Devre Dışı Bırakılan Kartlar** | 2 |

### Sürüm Dağılımı
- **2 Sürüm:** 14 kart (daha basit evrim)
- **3 Sürüm:** 11 kart (orta düzey evrim)
- **4 Sürüm:** 4 kart (önemli evrim)
- **5 Sürüm:** 1 kart (en çok gelişen: CONDITION_DOC_TO_PO_UNIT_PRICE)

---

## Yaygın Sürüm Desenleri

### Desen 1: Çeviri Anahtarı Benimseme (v1 → v2)

**Etkilenen:** 15+ kart

**Değişiklik:**
```
v1: Plain text: "Call Api: [param] with method: [param]"
v2: With i18n: "trnsl_%call_api trnsl_be_% Call Api: [param]..."
```

**Amaç:** Çok dilli desteği etkinleştirme

**Kartlar:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS ve daha fazlası

**Geçiş:** Güvenli - işlevsel değişiklik yok

---

### Desen 2: Karar Ağacı Entegrasyonu (v2 → v3)

**Etkilenen:** 5 kart

**Değişiklik:** Karar ağacı parametresinin eklenmesi

```
v2: Create a new Task with title: [param], description: [param]...
v3: (same as v2) + "Use decision tree, if available: [param]"
```

**Amaç:** Karar tablosu sonuçlarını destekleme

**Kartlar:**
- tasks_create (v3 kullanımdan kaldırıldı)
- ACTION_TASK_FOR_GROUP (v3 kullanımdan kaldırıldı)
- DOC_USER_ASSIGN (v3 kullanımdan kaldırıldı)
- DOC_GROUP_ASSIGN (v3 kullanımdan kaldırıldı)
- ACTION_DECISION_TREE_CREATE_TASKS

**Durum:** Kullanımdan kaldırıldı - karar ağacı yaklaşımı deneyseldi

---

### Desen 3: Generic Tür Evrimi (v3 → v4)

**Etkilenen:** 4 kart

**Değişiklik:** "Task", esnek iş öğesi türüne dönüşür

```
v3: Create a new Task with the title: [param]
v4: Create a new [param] with the title: [param]
```

**Amaç:** Task, Ticket, Issue ve diğer iş öğesi türlerini destekleme

**Kartlar:**
- tasks_create (v4 mevcut)
- ACTION_TASK_FOR_GROUP (v4 mevcut)
- ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP (v3 mevcut)
- ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK (v3 mevcut)

**Mevcut Durum:** Etkin ve önerilen

---

### Desen 4: Tolerans Parametreleri (PO Kartları)

**Etkilenen:** 6 PO karşılaştırma kartı

**Değişiklik:** Tolerans/sapma desteğinin eklenmesi

```
v2: Document value [operator] Purchase Order value
v3+: Document value [operator] PO value with tolerance [amount] [unit]
```

**Amaç:** Eşleştirmede kabul edilebilir sapmaya izin verme (örn. %2 fiyat farkı uygun)

**Önemli Kartlar:**
- CONDITION_DOC_TO_PO_UNIT_PRICE (tolerans ile v5'e gelişti)
- CONDITION_DATES_OPERATOR_OC_LINE_ITEMS (v2 → v3)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY

**Fayda:** Daha gerçekçi eşleştirme ölçütleri

---

### Desen 5: Karşılaştırma Modu Parametreleri

**Etkilenen:** 3 PO karşılaştırma kartı

**Değişiklik:** Farklı karşılaştırma algoritmaları için destek

```
v3: Standard comparison logic
v4: Same logic + "Compare as [param]" parameter
```

**Amaç:** Esnek karşılaştırma yöntemleri

**Kartlar:**
- COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE (v2-4)
- CONDITION_OC_TO_PO_ITEMS (v3-4)
- CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY (v3-4)

---

### Desen 6: İş Akışı Tetikleyicileri

**Etkilenen:** Yalnızca STAUS_CHANGE

**Değişiklik:** Durum değişikliğinde iş akışlarını otomatik tetikleme

```
v2: Change Status to [param]
v3: Change Status to [param], trigger Workflows [param]
```

**Amaç:** Durum değişikliklerini iş akışları arasında basamaklandırma

---

## En Çok Gelişen Kartlar

### 1. CONDITION_DOC_TO_PO_UNIT_PRICE (5 sürüm)

**Evrim Yolu:** v2 → v3 → v4 → v5

- **v2:** Temel birim fiyat karşılaştırması
- **v3:** Aynı çeviri anahtarı (v2)
- **v4:** Karşılaştırma modu parametresi eklendi
- **v5:** Tolerans eşiği parametresi eklendi

**Mevcut:** v5 (tolerans desteğiyle)

---

### 2. CONDITION_OC_TO_PO_ITEMS (4 sürüm)

**Evrim Yolu:** v1 → v2 → v3 → v4

- **v1:** Temel kalem eşleştirme (kullanımdan kaldırıldı)
- **v2:** Karşılaştırma yöntemi parametresi eklendi
- **v3:** Çeviri anahtarlarıyla geliştirildi
- **v4:** Karşılaştırma modu parametresi eklendi

**Mevcut:** v4

**Kaçının:** v1 (kullanımdan kaldırıldı)

---

### 3. tasks_create (4 sürüm)

**Evrim Yolu:** v1 → v2 → v3 → v4

- **v1:** Orijinal uygulama (kullanımdan kaldırıldı)
- **v2:** Çeviri desteği eklendi (kullanımdan kaldırıldı)
- **v3:** Karar ağacı eklendi (kullanımdan kaldırıldı)
- **v4:** Generic iş öğesi türleri (mevcut)

**Mevcut:** v4 (önerilen)

**Zaman Çizelgesi:**
```
v1 → deprecated (old)
  → v2 → deprecated (translation added)
    → v3 → deprecated (decision tree experiment)
      → v4 → CURRENT & ACTIVE
```

---

## Kullanımdan Kaldırma Durumu

### Tamamen Kullanımdan Kaldırılan Sürümler (Kullanmayın)

| Kart | Sürüm | Neden | Alternatif |
|------|---------|--------|-------------|
| tasks_create | v1 | Çok eski | v4 kullanın |
| tasks_create | v3 | Karar ağacı kullanımdan kaldırıldı | v4 kullanın |
| ACTION_TASK_FOR_GROUP | v3 | Karar ağacı kullanımdan kaldırıldı | v4 kullanın |
| DOC_USER_ASSIGN | v3 | Karar ağacı kullanımdan kaldırıldı | v2 kullanın |
| DOC_GROUP_ASSIGN | v3 | Karar ağacı kullanımdan kaldırıldı | v2 kullanın |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Çok eski | v2 kullanın |
| CONDITION_OC_TO_PO_ITEMS | v1 | Çok eski | v4 kullanın |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Özellikler geri alındı | v3 kullanın |

### Tamamen Devre Dışı Bırakılan Kartlar (Kullanılamaz)

| Kart | Sürümler | Notlar |
|------|----------|-------|
| DOC_SUBORG_CHANGE | v1, v2 | Desteklenmeyen işlevsellik |
| RUN_SCRIPT | v2, v3 | ACTION_RUN_DOCOPERATOR_SCRIPT ile değiştirildi |

---

## Sürüm Önerileri

### Kullanım Senaryosuna Göre

**Yeni İş Akışı Oluşturma:**
- Her zaman **en yüksek etkin sürüm numarasını** kullanın
- En son özellikleri ve iyileştirmeleri sağlar
- Desteklenir ve belgelenir

**Mevcut İş Akışı Bakımı:**
- Çalışıyorsa mevcut sürümü kullanmaya devam edin
- Mümkün olduğunda geçişi planlayın
- Yükseltmek için acil ihtiyaç yok

**Eski İş Akışı Geçişi:**
- Şu anda kullanılan sürümü belirleyin
- Yükseltme yolunu planlayın
- Dağıtmadan önce kapsamlı şekilde test edin

---

## Sürümler Nasıl Çalışır

### Sürüm Seçimi
Bir iş akışı oluştururken, bir kartın hangi sürümünü kullanacağınızı seçersiniz. Örnek:
- Yeni görev oluşturma için `tasks_create v4` kullanın (önerilen)
- Eski sistemler gerektiriyorsa `tasks_create v2` kullanın (daha eski ama çalışır)
- `tasks_create v1` KULLANMAYIN (kullanımdan kaldırıldı)

### Geriye Dönük Uyumluluk
- Daha yeni sürümler eski iş akışlarını bozmaz
- Eski iş akışları kendi orijinal sürümleriyle çalışmaya devam eder
- İş akışları kademeli olarak yükseltilebilir

### Teknik Uygulama
Sürümler veritabanı düzeyinde yönetilir:
```
card_templates table (PostgreSQL)
- card_type: Identifies the card (e.g., "tasks_create")
- card_version: Version number (e.g., 2, 3, 4)
- deprecated: Boolean flag
- enabled: Boolean flag
- text: Card description/parameters
```

---

## Dokümantasyon Amaçları İçin

### Sürüm Bilgilerini Anlama
Dokümantasyonda "Card v3" gördüğünüzde:
- Bu, o belirli kartın 3. sürümüne atıfta bulunur
- Ayrıntılar için [Full Versioning Reference](../../docs/card_version.md) sayfasını kontrol edin
- Hangi sürümün önerildiğini doğrulayın

### Sürümünüzü Kontrol Etme
Hangi sürümü kullandığınızı öğrenmek için:
1. İş akışınızdaki kartı açın
2. Görüntülenen sürüm numarasını kontrol edin
3. Kılavuzlardaki önerilerle karşılaştırın

### Sürüm Evrimi Zaman Çizelgesi
- **2024-2025:** Devam eden evrim
- **Ekim 2025:** Eksiksiz sürümleme dokümantasyonu
- **Gelecek:** Sürekli iyileştirmeler

---

## İlgili Dokümantasyon

### Kapsamlı Referans
→ [Full Card Versioning Reference](../../docs/card_version.md)

Şunları içerir:
- Sürümleriyle birlikte 30+ kartın tamamı
- Her biri için ayrıntılı metin evrimi
- Belirli parametre değişiklikleri
- Sürüm araması için SQL sorguları

### Karta Özgü Kılavuzlar
→ [Workflow Guides](../)

Sürüm önerileriyle birlikte her kart için dokümantasyon

### Sürüm Geçmişi Ayrıntıları
Her kılavuz, sürüm bilgilerini ve geçiş notlarını içerir

---

## Hızlı Referans

### En Çok Sürümü Olan Kartlar
1. CONDITION_DOC_TO_PO_UNIT_PRICE - 5 sürüm
2. CONDITION_OC_TO_PO_ITEMS - 4 sürüm
3. tasks_create - 4 sürüm
4. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE - 3 sürüm
5. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY - 4 sürüm

### En Yaygın Evrim Deseni
**Çeviri Anahtarı Benimseme (v1 → v2)** - 15+ kart

### En Önemli Değişiklik
**Generic Tür Evrimi (v3 → v4)** - "Task"tan esnek iş öğesi türüne değiştirildi

### Tamamen Devre Dışı
- DOC_SUBORG_CHANGE
- RUN_SCRIPT

---

## Sıkça Sorulan Sorular

### S: Hangi sürümü kullanmalıyım?
C: Daha eski bir sürümü kullanmak için belirli bir nedeniniz olmadıkça **en yüksek etkin sürümü** kullanın.

### S: İş akışımı daha yeni bir sürüme yükseltebilir miyim?
C: Evet, ancak kapsamlı şekilde test edin. Bazı sürümlerin farklı parametre gereksinimleri vardır.

### S: Kullanımdan kaldırılmış bir sürüm kullanırsam ne olur?
C: Çalışmaya devam eder, ancak yeni özellikler alamazsınız. Geçiş önerilir.

### S: Devre dışı bırakılmış bir kartı kullanabilir miyim?
C: Hayır, devre dışı bırakılmış kartlar kullanılamaz. Bunun yerine önerilen alternatifi kullanın.

### S: Kartımın yükseltilmesi gerekip gerekmediğini nasıl anlarım?
C: Kart türünüz için [Full Versioning Reference](../../docs/card_version.md) sayfasını kontrol edin ve önerileri izleyin.

---

## En İyi Uygulamalar

1. **Yeni İş Akışları:** En son kararlı sürümü kullanın
2. **Güncellemeler:** Yeni sürümleri periyodik olarak kontrol edin
3. **Test:** Sürüm yükseltmelerini önce sandbox'ta test edin
4. **Dokümantasyon:** Sürüm ayrıntıları için karta özgü kılavuzlara başvurun
5. **Geçiş:** Yükseltmeleri kademeli olarak planlayın
6. **Destek:** Sürüm uyumluluğu soruları ortaya çıkarsa destekle iletişime geçin

---

## Özet Tablosu

| Kart Türü | Mevcut Sürüm | Toplam Sürüm | Durum | Notlar |
|-----------|-----------------|----------------|--------|-------|
| tasks_create | 4 | 4 | Etkin | En çok gelişen; v3 kullanımdan kaldırıldı |
| CONDITION_DOC_TO_PO_UNIT_PRICE | 5 | 4 | Etkin | En yüksek sürüm sayısı |
| CONDITION_OC_TO_PO_ITEMS | 4 | 4 | Etkin | v1 kullanımdan kaldırıldı |
| ACTION_TASK_FOR_GROUP | 4 | 3 | Etkin | v3 kullanımdan kaldırıldı |
| ACTION_RUN_DOCOPERATOR_SCRIPT | 3 | 3 | Etkin | v4 kullanımdan kaldırıldı/devre dışı |
| Çoğu kart | 2 | 2 | Etkin | v1 → v2 deseni |

---

## Ayrıca Bkz.

- 📖 [Full Card Versioning Reference](../../docs/card_version.md)
- 🔗 [Workflow Guides](../)
- 📋 [October 2025 Release Notes](./2025-10-october.md)
- 🔄 [Workflow Linking Analysis](../../WORKFLOW_LINKING_MAP.md)

---

**Son Güncelleme:** 23 Ekim 2025
**Kaynak:** postgres-dev-docflow database
**Durum:** Eksiksiz Referans

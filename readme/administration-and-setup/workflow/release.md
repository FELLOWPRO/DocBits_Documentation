---
hidden: true
---

# Workflow Card Release & Version History

## Sürüm Kontrolü İlkeleri

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 13.41.53.png" alt=""><figcaption>Workflow Version Control System</figcaption></figure>

### Version 8.5.2024 - Temel Sürümleme Özellikleri

DocBits Workflow Engine, tüm workflow kartları için sağlam bir sürüm kontrolü uygular:

1. **Sürüm Kontrolü**: Her kartın birden fazla sürümü olabilir; her biri farklı bir koşul veya eylem kümesini temsil eder. Bu, şu anda etkin olan iş akışını etkilemeden kuralları denemenize veya ince ayar yapmanıza olanak tanır.
2. **Sorunsuz Yükseltmeler**: Belge işleme gereksinimlerinizdeki değişiklikler nedeniyle bir kuralı veya koşulu güncellemeniz gerektiğinde, kartın yeni bir sürümünü oluşturabilirsiniz. Bu yaklaşım, herhangi bir değişikliğin mevcut sürümün yerini almadan önce kasıtlı ve test edilmiş olmasını sağlar. Belge işlemenizdeki hataları ve olası aksaklıkları en aza indirir.
3. **Tutarlılığı Koruma**: Yükseltmeye karar verene kadar orijinal kart sürümünü değiştirmeden tutmak, devam eden süreçlerin etkilenmemesini sağlar. Canlı verileri veya iş akışlarını etkilemeden yeni sürümde testler ve doğrulamalar çalıştırabilirsiniz.
4. **Esneklik ve Test**: Birden fazla sürüm, kontrollü bir ortamda farklı senaryoları test etmeye olanak tanır. Kalıcı değişiklikler yapmadan yeni kuralların veya değişikliklerin belge işleme iş akışınız üzerindeki etkilerini görebilirsiniz. Sonuçlardan memnun kaldığınızda yeni sürümü uygulamayı seçebilirsiniz.

---

## Card Versioning Genel Bakış

### İstatistikler

| Metrik | Değer |
|--------|-------|
| **Birden Fazla Sürümü Olan Kartlar** | 30+ |
| **Toplam Sürüm Kaydı** | 90+ |
| **Mevcut Etkin Sürümler** | 81+ |
| **Kullanımdan Kaldırılan Sürümler** | 9 |
| **Tamamen Devre Dışı Bırakılan Kartlar** | 2 |
| **En Son Sürüm (Maks.)** | 5 (CONDITION_DOC_TO_PO_UNIT_PRICE) |

### Sürüm Aralığı
- **Minimum:** v1
- **Maksimum:** v5
- **Kart Başına Ortalama Sürüm:** 3

---

## Ayrıntılı Kart Sürümü Değişiklikleri

### 🔧 ACTION CARDS - Harici Entegrasyon ve Yürütme

#### 1. CALL_API
**Sürümler:** v1, v2 (Mevcut: v2)

📖 **Kılavuz:** [Call External API Guide](../then/action/call-api-guide.md)

| Sürüm | Çeviri | Durum | Önemli Değişiklikler |
|---------|-------------|--------|-------------|
| v1 | Hayır | Etkin | Çeviri anahtarları olmadan temel API çağrısı |
| v2 | Evet | ✅ Mevcut | Çok dilli destek için `trnsl_%call_api` eklendi |

**Ne Değişti:** Çeviri anahtarlarıyla uluslararasılaştırma (i18n) desteği eklendi. İşlevsellik aynı kalır.

**Önce (v1):**
```
Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Sonra (v2):**
```
trnsl_%call_api trnsl_be_% Call Api: [endpoint] with method: [method], params: [params], data: [data]
```

**Öneri:** Tüm yeni iş akışları için v2 kullanın (dil desteği içerir)
**Geriye Dönük Uyumluluk:** ✅ v1 hâlâ çalışır

---

#### 2. HTTPS Request (HTTPS_REQUEST)
**Sürümler:** v1, v2 (Mevcut: v2)

| Sürüm | Çeviri | Durum | Önemli Değişiklikler |
|---------|-------------|--------|-------------|
| v1 | Hayır | Etkin | Basit HTTP isteği |
| v2 | Evet | ✅ Mevcut | `trnsl_%send_https_request` çeviri anahtarları eklendi |

**Ne Değişti:** Çeviri desteği eklendi. Temel webhook/istek işlevselliği değişmedi.
**Öneri:** v2 kullanın (çok dilli destek)

---

#### 3. ACTION_RUN_DOCOPERATOR_SCRIPT ⚠️
**Sürümler:** v2 (Mevcut), v3, v4 (Kullanımdan Kaldırıldı ve Devre Dışı)

| Sürüm | Çeviri | Durum | Önemli Değişiklikler |
|---------|-------------|--------|-------------|
| v2 | Evet | Etkin | Orijinal DocOperator uygulaması |
| v3 | Evet | Etkin | Ek kontrol için "Execute the prompt" parametresi eklendi |
| v4 | Evet | ❌ KULLANIMDAN KALDIRILDI VE DEVRE DIŞI | "Execute" parametresi kaldırıldı (geri alındı) |

**Evrim Yolu:** v2 → v3 (parametre eklendi) → v4 (geri alındı - önerilmez)

**Ne Değişti:**
- v2 → v3: Daha fazla esneklik için isteğe bağlı yürütme kontrolü parametresi eklendi
- v3 → v4: Daha fazla analiz sonrası parametre kaldırıldı (kullanımdan kaldırıldı)

**Öneri:** Yeni iş akışları için v3 kullanın (tüm özellikleri içeren en son etkin sürüm)
**Geçiş:** v4 kullanıyorsanız v3'e geçin ⚠️

---

#### 4. ACTION_TASK_FOR_GROUP
**Sürümler:** v2, v3 (Kullanımdan Kaldırıldı), v4 (Mevcut)

📖 **Kılavuz:** [Task Assignment Guide](../then/task/task-assignment-guide.md)

| Sürüm | Değişiklikler | Durum | Tür Parametresi |
|---------|---------|--------|-----------------|
| v2 | Orijinal uygulama | Etkin | "Task" (sabit) |
| v3 | + Karar ağacı desteği | ❌ KULLANIMDAN KALDIRILDI | "Task" (sabit) |
| v4 | - Karar ağacı, + Generic tür | ✅ Mevcut | Generic tür (esnek) |

**Evrim:** v2 → v3 (karar ağacı denemesi) → v4 (generic türler, karar ağacı kaldırıldı)

**v2 → v3 Değişikliği (Karar Ağacı Denemesi):**
```
Before: "Create a new Task with the title: [param] ... and assign to group [param]"
After:  "Create a new Task with the title: [param] ... and assign to group [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 Değişikliği (Generic Türler + Karar Ağacının Kaldırılması):**
```
Before (v3): "Create a new Task with the title: [param] ... "
After (v4):  "Create a new [param] with the title: [param] ... "
```

**Ne Değişti:**
- v2 → v3: `decision tree, if available: [param]` parametresi eklendi
- v3 → v4:
  - ❌ Karar ağacı parametresi kaldırıldı
  - ✅ "Task" → generic `[param]` olarak değiştirildi (Task, Ticket, Issue vb. destekler)
  - `trnsl_%task_for_group_v4` çeviri anahtarı eklendi

**Neden:** v3 karar ağacı yaklaşımı deneyseldi. v4, generic iş öğesi türleriyle daha iyi esneklik sağlar.
**Öneri:** v4 kullanın (mevcut, en esnek)

---

#### 5. ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Görev Türü | Durum | Önemli Fark |
|---------|-----------|--------|-----------------|
| v2 | "task" (sabit) | Etkin | Orijinal sürüm |
| v3 | Generic tür | ✅ Mevcut | Esnek `[param]` olarak değiştirildi |

**Ne Değişti:** v2 → v3: "Create a new task" → "Create a new [param]" (herhangi bir iş öğesi türünü destekler)
**Öneri:** v3 kullanın

---

#### 6. RUN_WORKFLOW
**Sürümler:** v1, v2 (Mevcut)

**Ne Değişti:** v1 → v2: `trnsl_%run_workflow` çeviri anahtarları eklendi
**Öneri:** v2 kullanın

---

### 📊 PO KARŞILAŞTIRMA VE DOĞRULAMA KARTLARI

#### 1. CONDITION_DOC_TO_PO_UNIT_PRICE ⭐ (En Çok Gelişen - 5 Sürüm)
**Sürümler:** v2, v3, v4, v5 (Mevcut)

📖 **Kılavuz:** [PO Matching Complete Guide](../and/compare-with-purchase-order/po-matching-complete-guide.md#2-unit-price-comparison-document-vs-po)

| Sürüm | Değişiklikler | Durum | Tolerans | Karşılaştırma |
|---------|---------|--------|-----------|------------|
| v2 | Temel fiyat karşılaştırması | Etkin | ❌ Hayır | Temel |
| v3 | v2 ile aynı | Etkin | ❌ Hayır | Temel |
| v4 | + Karşılaştırma modu parametresi | Etkin | ❌ Hayır | ✅ Evet |
| v5 | + Tolerans parametreleri | ✅ Mevcut | ✅ Evet (tutar + birim) | ✅ Evet |

**Evrim Yolu:** v2 → v3 (değişiklik yok) → v4 (karşılaştırma modları) → v5 (tolerans eşikleri)

**v2 → v3:** İşlevsel değişiklik yok (aynı çeviri anahtarı)

**v3 → v4 Değişikliği (Karşılaştırma Modu Eklendi):**
```
Before: "[document] unit price is [operator] to purchase order"
After:  "[document] unit price is [operator] to purchase order. Compare as [mode]"
```

**v4 → v5 Değişikliği (Tolerans Parametreleri Eklendi):**
```
Before: "[document] unit price is [operator] to purchase order. Compare as [mode]"
After:  "[document] unit price is [operator] to purchase order, with tolerance of [amount] [unit].
         Compare as [mode]"
```

**Ne Değişti:**
- **v2 → v3:** İşlevsel değişiklik yok
- **v3 → v4:** `Compare as [param]` eklendi - Farklı karşılaştırma operatörlerini destekler
- **v4 → v5:** Tolerans parametreleri eklendi:
  - `with tolerance of [amount] [unit]`
  - Örnek: "with tolerance of 2 %" veya "with tolerance of 100 EUR"
  - Destekler: %, EUR, $ ve diğer para birimleri

**Kullanım Senaryoları:**
- v2/v3: Katı eşleştirme (yalnızca tam fiyatlar)
- v4: Farklı karşılaştırma yöntemleri
- v5: Esnek sapma kabulü (örn. %2 fiyat farklarını kabul et) ✅ ÖNERİLEN

**Öneri:** Modern PO eşleştirme iş akışları için v5 kullanın

---

#### 2. CONDITION_OC_TO_PO_ITEMS
**Sürümler:** v1 (Kullanımdan Kaldırıldı), v2, v3, v4 (Mevcut)

| Sürüm | Değişiklikler | Durum | Karşılaştırma Özelliği |
|---------|---------|--------|-----------------|
| v1 | Çeviri yok, yöntem yok | ❌ KULLANIMDAN KALDIRILDI | Temel |
| v2 | + Çeviri anahtarları, + yöntem | Etkin | Temel yöntem |
| v3 | v2 ile aynı | Etkin | Temel yöntem |
| v4 | + Karşılaştırma modu parametreleri | ✅ Mevcut | ✅ Esnek |

**Ne Değişti:**
- **v1 → v2:** `trnsl_%in_order_confirmations_matches_purchase_order` + karşılaştırma yöntemi parametresi eklendi
- **v2 → v3:** Değişiklik yok
- **v3 → v4:** Esnek karşılaştırma modları için `Compare as [param1] [param2]` eklendi

**Öneri:** v4 kullanın (kullanımdan kaldırılan v1'den kaçının)

---

#### 3. CONDITION_DATES_OPERATOR_OC_LINE_ITEMS
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Tolerans Günleri | Kabul Edilen Tolerans Günleri | Durum |
|---------|-----------------|------------------------|--------|
| v2 | ❌ Hayır | ❌ Hayır | Etkin |
| v3 | ✅ Evet | ✅ Evet | ✅ Mevcut |

**Ne Değişti:** v2 → v3: Tolerans parametreleri eklendi:
- `with [param] days as tolerance`
- `and [param] as accepted tolerance days`

**Örnek:** Vaat edilen tarihten itibaren 5 gün içindeki teslimat tarihlerini kabul et
**Öneri:** v3 kullanın

---

#### 4. CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY
**Sürümler:** v2, v3, v4 (Mevcut)

| Sürüm | Karşılaştırma Modu | Durum |
|---------|-----------------|--------|
| v2 | Temel | Etkin |
| v3 | Temel (değişiklik yok) | Etkin |
| v4 | ✅ Esnek mod seçimi | ✅ Mevcut |

**Ne Değişti:** v3 → v4: Farklı karşılaştırma yaklaşımları için `compare [param]` eklendi
**Öneri:** v4 kullanın

---

#### 5. COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE
**Sürümler:** v2, v3, v4 (Mevcut)

| Sürüm | Karşılaştırma Modu | Durum |
|---------|-----------------|--------|
| v2 | Standart | Etkin |
| v3 | Standart (değişiklik yok) | Etkin |
| v4 | ✅ Esnek | ✅ Mevcut |

**Ne Değişti:** v3 → v4: `compare [param]` parametresi eklendi
**Öneri:** v4 kullanın

---

#### 6. CONDITION_CONFIRMED_DELIVERY_ACCEPTED_DATE_IN_CALENDAR_MASTER_DATA
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Teslimat Türü | Ana Veri Tablosu | Durum |
|---------|---------------|-------------------|--------|
| v2 | "Confirmed" (sabit) | Sabit referans | Etkin |
| v3 | [Yapılandırılabilir param] | Dinamik [param] | ✅ Mevcut |

**Ne Değişti:** v2 → v3:
- "Confirmed delivery" → `[param] delivery` olarak değiştirildi (esnek teslimat türü)
- Sabit tablo referansı → `stored in [param]` olarak değiştirildi (dinamik tablo seçimi)

**Esneklik:** v3, farklı teslimat tarihi türlerine ve tedarikçi tablolarına olanak tanır
**Öneri:** v3 kullanın

---

#### 7. CONDIITON_UNIT_OF_MEASURE_EQUAL
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Tedarikçi Tablosu Referansı | Durum |
|---------|--------------------------|--------|
| v2 | "supplier item price table" (sabit) | Etkin |
| v3 | [Dinamik param] | ✅ Mevcut |

**Ne Değişti:** v2 → v3: Sabit tablo referansı → `stored in [param]` (dinamik tablo seçimine olanak tanır)
**Öneri:** v3 kullanın

---

### 👥 ATAMA VE YÖNLENDİRME KARTLARI

#### 1. DOC_USER_ASSIGN
**Sürümler:** v1, v2, v3 (Kullanımdan Kaldırıldı)

| Sürüm | Çeviri | Karar Ağacı | Durum |
|---------|-------------|---------------|--------|
| v1 | Hayır | ❌ Hayır | Etkin |
| v2 | Evet | ❌ Hayır | ✅ Mevcut |
| v3 | Evet | ✅ Evet | ❌ KULLANIMDAN KALDIRILDI |

**Evrim:** v1 (i18n yok) → v2 (i18n ile) → v3 (+ karar ağacı denemesi, artık kullanımdan kaldırıldı)

**Ne Değişti:**
- v1 → v2: Çeviri anahtarları eklendi
- v2 → v3: Karar ağacı desteği eklendi (deneysel, kullanımdan kaldırıldı)

**Öneri:** v2 kullanın (i18n destekli kararlı sürüm)

---

#### 2. DOC_GROUP_ASSIGN
**Sürümler:** v2, v3 (Kullanımdan Kaldırıldı)

| Sürüm | Karar Ağacı | Durum |
|---------|---------------|--------|
| v2 | ❌ Hayır | ✅ Mevcut |
| v3 | ✅ Evet | ❌ KULLANIMDAN KALDIRILDI |

**Ne Değişti:** v2 → v3: `Use decision tree, if available [param]` eklendi (daha sonra kullanımdan kaldırıldı)
**Öneri:** v2 kullanın

---

#### 3. OC_ASSIGN_DOC
**Sürümler:** v1, v2 (Mevcut)

**Ne Değişti:** v1 → v2: `trnsl_%oc_assign_doc` çeviri anahtarları eklendi
**Öneri:** v2 kullanın

---

### 📋 GÖREV YÖNETİMİ KARTLARI

#### 1. tasks_create ⭐ (En Çok Gelişen Görev Kartı - 4 Sürüm)
**Sürümler:** v1 (Kullanımdan Kaldırıldı), v2 (Kullanımdan Kaldırıldı), v3 (Kullanımdan Kaldırıldı), v4 (Mevcut)

📖 **Kılavuz:** [Task Assignment Guide](../then/task/task-assignment-guide.md#card-tasks_create--create-task-and-assign-to-user)

| Sürüm | Çeviri | Karar Ağacı | İş Öğesi Türü | Durum |
|---------|-------------|---------------|-----------------|--------|
| v1 | Hayır | Hayır | "Task" (sabit) | ❌ KULLANIMDAN KALDIRILDI |
| v2 | Evet | Hayır | "Task" (sabit) | ❌ KULLANIMDAN KALDIRILDI |
| v3 | Evet | Evet | "Task" (sabit) | ❌ KULLANIMDAN KALDIRILDI |
| v4 | Evet | Hayır | [Generic param] | ✅ Mevcut |

**Evrim Zaman Çizelgesi:**
```
v1 (original)
  ↓ (add translation)
v2 (with i18n)
  ↓ (experiment with decision tree)
v3 (+ decision tree, BUT deprecated after this)
  ↓ (remove decision tree, add generic types)
v4 (CURRENT - flexible work items)
```

**v1 → v2 Değişikliği (Çeviri Anahtarları Eklendi):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "trnsl_%tasks_create trnsl_be_% Create a new Task with the title: [param] ... and assign to user [param]"
```

**v2 → v3 Değişikliği (Karar Ağacı Denemesi):**
```
Before: "Create a new Task with the title: [param] ... and assign to user [param]"
After:  "Create a new Task with the title: [param] ... and assign it to the user [param].
         Use decision tree, if available: [param]"
```

**v3 → v4 Değişikliği (Generic Türler + Karar Ağacının Kaldırılması):**
```
Before: "Create a new Task with the title: [param] ... "
After:  "Create a new [param] with the title: [param] ... "
```

**Ne Değişti:**
- **v1 → v2:** `trnsl_%tasks_create` çeviri anahtarları eklendi
- **v2 → v3:**
  - Karar ağacı desteği eklendi: `Use decision tree, if available: [param]`
  - "assign to user" → "assign it to the user" olarak değiştirildi
- **v3 → v4:**
  - ❌ Karar ağacı parametresi kaldırıldı
  - ✅ "Task" → generic `[param]` olarak değiştirildi (Task, Ticket, Issue vb. destekler)
  - Çeviri anahtarı `trnsl_%tasks_create_v4` olarak güncellendi

**Karar Ağacı Notu:** v3, görevleri dinamik olarak atamak için karar ağaçlarını kullandı. Bu yaklaşım deneyseldi ve doğrudan parametre tabanlı iş öğesi türü seçimi lehine v4'te kullanımdan kaldırıldı.

**Öneri:** Yeni iş akışları için yalnızca v4 kullanın
**Geçiş:** v1, v2 veya v3 kullanıyorsanız v4'e yükseltin ✅

---

#### 2. OC_TASK
**Sürümler:** v1, v2 (Mevcut)

**Ne Değişti:** v1 → v2: `trnsl_%oc_task` çeviri anahtarları eklendi
**Öneri:** v2 kullanın

---

#### 3. ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK
**Sürümler:** v1, v3 (Mevcut - v2 Atlandı)

| Sürüm | İş Öğesi Türü | Durum |
|---------|-----------------|--------|
| v1 | "Task" (sabit) | Etkin |
| v3 | [Generic param] | ✅ Mevcut |

**Ne Değişti:** v1 → v3: Generic tür evrimi (v2 üretimde atlandı)
**Öneri:** v3 kullanın

---

#### 4. ACTION_DECISION_TREE_CREATE_TASKS
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Atama Metni | Durum |
|---------|-----------------|--------|
| v2 | "Assign task with title" | Etkin |
| v3 | "Assign [generic] with title" | ✅ Mevcut |

**Ne Değişti:** v2 → v3:
- "Assign task" → "Assign [generic param]" olarak değiştirildi
- "return of decision" → "return of decision table" olarak değiştirildi (daha net terminoloji)

**Öneri:** v3 kullanın

---

### 🔄 BELGE KONTROL KARTLARI

#### APPROVE
**Sürümler:** v1, v2 (Mevcut)
**Değişiklik:** `trnsl_%approve_doc` çeviri anahtarları eklendi
**Öneri:** v2 kullanın

---

#### REJECT
**Sürümler:** v1, v2 (Mevcut)
**Değişiklik:** `trnsl_%reject_doc` çeviri anahtarları eklendi
**Öneri:** v2 kullanın

---

#### STAUS_CHANGE (Status Change)
**Sürümler:** v1, v2, v3 (Mevcut)

| Sürüm | İş Akışı Tetikleyici | Durum |
|---------|-----------------|--------|
| v1 | ❌ Hayır | Etkin |
| v2 | ❌ Hayır | Etkin |
| v3 | ✅ Evet | ✅ Mevcut |

**Ne Değişti:** v2 → v3: `trigger Workflows [param]` eklendi - Durum değişikliğinde iş akışlarını otomatik tetikler
**Öneri:** v3 kullanın

---

#### EXPORT
**Sürümler:** v1, v2, v3 (Mevcut)

| Sürüm | Doğrulama | Durum |
|---------|------------|--------|
| v1 | ❌ Hayır | Etkin |
| v2 | ❌ Hayır | Etkin |
| v3 | ✅ Evet | ✅ Mevcut |

**Ne Değişti:** v2 → v3: `Start Export with Validation: [param]` eklendi
**Öneri:** v3 kullanın

---

### 🧮 VERİ DÜZENLEME KARTLARI

#### CALC_COLUMNS, CALC_COLUMNS_REGEX, EDIT_COLUMN, AI_CALC_MTZ_ETZ
**Desen:** v1 → v2 (çeviri anahtarları eklendi)
**Öneri:** Hepsi için v2 kullanın

---

#### CONDITION_DECISION_TREE_DATA
**Sürümler:** v2, v3 (Mevcut)

| Sürüm | Veri Kullanımı | Durum |
|---------|------------|--------|
| v2 | "Use return data in later cards" | Etkin |
| v3 | "[Explicit param] returned data for use in subsequent cards" | ✅ Mevcut |

**Ne Değişti:** v2 → v3: Karar ağacı veri çıkarma üzerinde daha açık kontrol
**Öneri:** v3 kullanın

---

### ❌ DEVRE DIŞI KARTLAR (Kullanmayın)

#### DOC_SUBORG_CHANGE
**Sürümler:** v1, v2 (her ikisi de devre dışı)
**Durum:** Artık desteklenmiyor
**Alternatif:** Belge atama özelliklerini kullanın

---

#### RUN_SCRIPT
**Sürümler:** v2, v3 (her ikisi de devre dışı)
**Durum:** ACTION_RUN_DOCOPERATOR_SCRIPT ile değiştirildi
**Alternatif:** ACTION_RUN_DOCOPERATOR_SCRIPT v3 kullanın

---

## 🎯 Yaygın Sürüm Desenleri

### Desen 1: Çeviri Anahtarı Benimseme (v1 → v2)
**Etkilenen:** 15+ kart

**Değişiklik:** `trnsl_%[card_name]` çeviri anahtarları eklendi
```
v1: Plain text (no i18n)
v2: trnsl_%[key] trnsl_be_% Plain text (with i18n)
```

**Kartlar:** CALL_API, RUN_WORKFLOW, APPROVE, REJECT, CALC_COLUMNS ve daha fazlası
**Etki:** Çok dilli desteği etkinleştirir

---

### Desen 2: Karar Ağacı Entegrasyonu (v2 → v3) - KULLANIMDAN KALDIRILDI
**Etkilenen:** 5 kart (ACTION_TASK_FOR_GROUP, tasks_create, DOC_USER_ASSIGN, DOC_GROUP_ASSIGN, ACTION_DECISION_TREE_CREATE_TASKS)

**Değişiklik:** İsteğe bağlı karar ağacı parametresi eklendi
```
v2: Standard task/assignment logic
v3: + "Use decision tree, if available: [param]"
```

**Durum:** ❌ Çoğunlukla kullanımdan kaldırıldı (ACTION_DECISION_TREE_CREATE_TASKS hariç)
**Neden:** Daha basit doğrudan parametre yaklaşımı tercih edildi

---

### Desen 3: Generic Tür Evrimi (v3 → v4)
**Etkilenen:** 4 kart (tasks_create, ACTION_TASK_FOR_GROUP, ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP, ACTION_ASSIGN_TASK_TO_USER_FROM_FIELD_WITH_FALLBACK)

**Değişiklik:** "Task" → generic tür parametresi
```
v3: Create a new Task with title: [param]
v4: Create a new [param] with title: [param]
```

**Etki:** Task, Ticket, Issue ve diğer iş öğesi türlerini destekler
**Fayda:** Daha fazla esneklik ve yeniden kullanılabilirlik

---

### Desen 4: Tolerans Parametreleri (PO Kartları)
**Etkilenen:** 6 kart (CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DATES_OPERATOR_OC_LINE_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY vb.)

**Değişiklik:** Tolerans/sapma desteği eklendi
```
v2: Value [operator] Reference Value
v3+: Value [operator] Reference with tolerance [amount] [unit]
```

**Örnekler:**
- "with tolerance of 2 %"
- "with tolerance of 100 EUR"
- "with 5 days as tolerance"

**Etki:** Gerçekçi eşleştirme ölçütleri (tüm değerlerin tam olarak eşleşmesi gerekmez)

---

### Desen 5: Karşılaştırma Modu Parametreleri
**Etkilenen:** 3 kart (COMBINED_PRICE_OF_QUANTITY_DIFFERENCE_OPERATOR_VALUE, CONDITION_OC_TO_PO_ITEMS, CONDITION_LESS_THAN_TOLERANCE_AS_VALUE_OF_ORDERED_QUANTITY)

**Değişiklik:** Esnek karşılaştırma yöntemi seçimi eklendi
```
v3: Standard comparison
v4: + "Compare as [param1] [param2]"
```

**Etki:** Farklı karşılaştırma algoritmalarını destekler

---

## ✅ Sürüm Önerileri

### Yeni İş Akışları İçin
**Kural:** Her zaman en yüksek etkin sürüm numarasını kullanın
- En son özellikleri sağlar
- En iyi destek
- En çok test edilmiş
- Önerilen yaklaşım

### Mevcut İş Akışları İçin
**Güvenli Yaklaşım:**
- Çalışıyorsa mevcut sürümü kullanmaya devam edin
- Daha yeni sürümlere kademeli geçişi planlayın
- Yükseltmeleri önce sandbox'ta test edin

### Geçiş Önceliği

| Öncelik | Kartlar | Eylem |
|----------|-------|--------|
| **Yüksek** | tasks_create v1/v2/v3, ACTION_TASK_FOR_GROUP v3, CONDITION_DOC_TO_PO_UNIT_PRICE v2/v3/v4 | Mevcut sürüme yükseltin |
| **Orta** | Diğer v1/v2 çeviri yükseltmeleri, PO kartları v2/v3 | Yükseltmeyi düşünün |
| **Düşük** | İşlevsel değişikliği olmayan kartlar | İsteğe bağlı |

---

## ⚠️ Kullanımdan Kaldırılan Sürümler - Kullanmayın

| Kart | Sürüm | Neden | Bunun Yerine Kullanın |
|------|---------|--------|-------------|
| tasks_create | v1, v2, v3 | Çok eski veya karar ağacı kullanımdan kaldırıldı | v4 |
| ACTION_TASK_FOR_GROUP | v3 | Karar ağacı yaklaşımı kullanımdan kaldırıldı | v4 |
| DOC_USER_ASSIGN | v3 | Karar ağacı yaklaşımı kullanımdan kaldırıldı | v2 |
| DOC_GROUP_ASSIGN | v3 | Karar ağacı yaklaşımı kullanımdan kaldırıldı | v2 |
| CONDITION_DOC_TYPE_IS_ISNOT | v1 | Çok eski | v2 |
| CONDITION_OC_TO_PO_ITEMS | v1 | Çok eski | v4 |
| ACTION_RUN_DOCOPERATOR_SCRIPT | v4 | Özellikler geri alındı | v3 |

---

## 🔄 Tamamen Devre Dışı Bırakılan Kartlar - Kullanılamaz

| Kart | Sürümler | Neden | Alternatif |
|------|----------|--------|-------------|
| DOC_SUBORG_CHANGE | v1, v2 | Artık desteklenmiyor | Belge atama kartları |
| RUN_SCRIPT | v2, v3 | DocOperator ile değiştirildi | ACTION_RUN_DOCOPERATOR_SCRIPT v3 |

---

## İlgili Dokümantasyon

- 📖 [Card Versioning Reference](../changelog/card-versioning.md) - Ayrıntılı sürüm bilgileri
- 📚 [Workflow Guides](../) - Adım adım kart kullanımı
- 🔄 [Card Version Database](../docs/card_version.md) - Eksiksiz sürüm geçmişi
- 📋 [Workflow Logs](../workflow-logs/) - Yürütme ve hata ayıklama

---

**Son Güncelleme:** 23 Ekim 2025
**Durum:** Eksiksiz Sürüm Geçmişi
**Veritabanı Kaynağı:** postgres-dev-docflow

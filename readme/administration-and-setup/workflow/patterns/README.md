# Workflow Pattern Guides

**Sürüm:** 1.0
**Son Güncelleme:** 23 Ekim 2025

---

## Genel Bakış

Bu dizin, yaygın iş senaryolarını çözmek için birden fazla iş akışı kartının nasıl birleştirileceğini gösteren kapsamlı iş akışı kalıbı kılavuzları içerir. Her kalıp, adım adım uygulama talimatları, eksiksiz örnekler ve en iyi uygulamalar sağlar.

**İş Akışı Kalıpları Nedir?**

İş akışı kalıpları, yaygın belge işleme zorluklarına kanıtlanmış, yeniden kullanılabilir çözümlerdir. Sıfırdan başlamak yerine, bu kalıpları şablon olarak kullanabilir ve özel ihtiyaçlarınıza uyarlayabilirsiniz.

---

## Bir bakışta Workflow Builder

Bu sayfadaki her kalıp, **Workflow Builder**'da oluşturulur. Ona **Workflow Dashboard → Workflow List → Add Workflow** üzerinden (veya mevcut bir iş akışını açarak) ulaşırsınız. Dashboard, tüm iş akışlarınız için çalıştırma geçmişini ve başarı/başarısızlık oranlarını gösterir:

<figure><img src="../../../.gitbook/assets/workflow_dashboard.png" alt="Çalıştırma toplamları, başarı ve başarısızlık oranları, iş akışı çalıştırma grafiği ve son etkinlikleri gösteren Workflow Dashboard"><figcaption><p>Workflow Dashboard — her iş akışı için çalıştırma toplamları, başarı/başarısızlık oranları ve son etkinlikler.</p></figcaption></figure>

**Workflow List** sekmesi, türü, yürütme sırası ve tetikleyicisiyle birlikte her iş akışını listeler. Yeni bir tane oluşturmak için **Add Workflow** kullanın veya oluşturucuda açmak için bir iş akışına tıklayın:

<figure><img src="../../../.gitbook/assets/workflow_list.png" alt="İş akışlarını tür, yürütme sırası ve tetikleyiciyle listeleyen Workflow List sekmesi"><figcaption><p>Workflow List — her satır, açıp kapatabileceğiniz veya düzenleyebileceğiniz bir iş akışıdır.</p></figcaption></figure>

Bir iş akışı üç kart grubundan oluşturulur — **When** (tetikleyici), **And** (ek koşullar) ve **Then** (çalıştırılacak eylemler). Aşağıdaki örnek, bir alt kuruluşa ait faturalarda tetiklenir ve onları bir kullanıcıya atar:

<figure><img src="../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kartlarıyla Workflow Builder tuvali"><figcaption><p>Workflow Builder tuvali. Aşağıdaki her kalıp, yalnızca When / And / Then kartlarının farklı bir kombinasyonudur.</p></figcaption></figure>

Kart kütüphanesini açmak için herhangi bir grupta **Add Card**'a tıklayın. Kartlar kategoriye göre düzenlenmiştir (Compare with Purchase Order, Partner Cards, Document Field, Date &#x26; Time, Document, Logic, Status, Table, Assignee, …), böylece her kalıbın gerektirdiği yapı taşını bulabilirsiniz:

<figure><img src="../../../.gitbook/assets/workflow_add_card_picker.png" alt="Kart kategorilerini ve kullanılabilir kartları gösteren Add Card iletişim kutusu"><figcaption><p><strong>Add Card</strong> kütüphanesi — aşağıdaki kalıplarda başvurulan her kart buradan seçilir.</p></figcaption></figure>

---

## Kullanılabilir Kalıplar

### 1. [API Integration Pattern](api-integration-pattern.md)

**Karmaşıklık:** Orta | **Kurulum Süresi:** 45-60 dakika

DocBits'i harici sistemlerden veri almak, doğrulamak ve depolamak için harici API'lerle nasıl entegre edeceğinizi öğrenin.

**Kullanım Durumları:**
- Harici sistemlerden gerçek zamanlı fiyatlandırma alma
- Tedarikçi bilgilerini ana veritabanlarına karşı doğrulama
- Katalog sistemlerinden ürün ayrıntılarını arama
- Para birimi servislerinden döviz kurları alma
- Adresleri coğrafi kodlama servisleriyle doğrulama

**Kullanılan Kartlar:** CALL_API, CONDITION_HTTPS_REQUEST_STATUS, ACTION_SET_FIELD_TO_TEXT, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Tam Kalıbı Görüntüle →](api-integration-pattern.md)**

---

### 2. [Task Management Pattern](task-management-pattern.md)

**Karmaşıklık:** Düşük-Orta | **Kurulum Süresi:** 30-45 dakika

Onay ve inceleme süreçleri için DocBits iş akışları içinde görev oluşturma, atama, izleme ve yönetme sanatında ustalaşın.

**Kullanım Durumları:**
- Onay iş akışları oluşturma
- İnceleme görevlerini kullanıcılara atama
- İnsan müdahalesi gerektiren istisnaları ele alma
- Sorunları yöneticilere yükseltme
- Çok düzeyli onay zincirleri oluşturma
- Görev tamamlanmasını ve son teslim tarihlerini izleme

**Kullanılan Kartlar:** tasks_create, ACTION_ASSIGN_TO_USER, ACTION_SEND_EMAIL_TO_GROUPS, CONDITION_TASK_STATUS

**[Tam Kalıbı Görüntüle →](task-management-pattern.md)**

---

### 3. [PO Matching Pattern](po-matching-pattern.md)

**Karmaşıklık:** Orta-Yüksek | **Kurulum Süresi:** 60-90 dakika

Faturaları, tolerans tabanlı yönlendirmeyle PO'lara karşı doğrulamak için kapsamlı Satınalma Siparişi eşleştirme iş akışları uygulayın.

**Kullanım Durumları:**
- Faturaları satınalma siparişlerine karşı doğrulama
- Ödemeden önce fiyatlandırma hatalarını tespit etme
- Miktar tutarsızlıklarını belirleme
- Satınalma kontrollerini uygulama
- Yinelenen ödemeleri önleme
- Üç yönlü eşleştirmeyi otomatikleştirme

**Kullanılan Kartlar:** PURCHASE_ORDER_FULL_MATCH, CONDITION_DOC_TO_PO_UNIT_PRICE, CONDITION_DOC_TO_PO_QUANTITY, CONDITION_DOC_TO_PO_TAX_LINES

**[Tam Kalıbı Görüntüle →](po-matching-pattern.md)**

---

### 4. [Decision Logic Pattern](decision-logic-pattern.md)

**Karmaşıklık:** Orta | **Kurulum Süresi:** 30-45 dakika

Belgeleri iş kurallarına dayalı farklı yollardan işlemek için karmaşık karar ağaçları ve koşullu yönlendirme mantığı uygulayın.

**Kullanım Durumları:**
- Belgeleri tutar eşiklerine göre yönlendirme
- Farklı belge türleri için farklı kurallar uygulama
- Çok düzeyli onay mantığı uygulama
- Karmaşık iş politikalarını ele alma
- Birden fazla ölçüte dayalı dinamik yönlendirme oluşturma
- Onay matrisleri uygulama

**Kullanılan Kartlar:** CONDITION_DOC_FIELD_AMOUNT, CONDITION_DOC_TYPE_IS_ISNOT, CONDITION_SUPPLIER_STATUS_IS_ISNOT, ACTION_ASSIGN_TO_USER

**[Tam Kalıbı Görüntüle →](decision-logic-pattern.md)**

---

### 5. [Data Transformation Pattern](data-transformation-pattern.md)

**Karmaşıklık:** Orta | **Kurulum Süresi:** 30-45 dakika

Dışa aktarmaya hazırlanmak, hesaplamalar yapmak ve biçimleri standartlaştırmak için belge verilerini dönüştürün, hesaplayın, biçimlendirin ve zenginleştirin.

**Kullanım Durumları:**
- Toplamları, ara toplamları, vergileri hesaplama
- Para birimlerini veya birimleri dönüştürme
- Tarihleri, sayıları, metni biçimlendirme
- Mevcut alanlardan değerler türetme
- Harici kaynaklardan veri zenginleştirme
- Veri biçimlerini standartlaştırma
- Hesaplamaları doğrulama

**Kullanılan Kartlar:** ACTION_CALCULATE_FIELD, ACTION_SET_FIELD_TO_TEXT, ACTION_COPY_FIELD_VALUE, CALL_API, CONDITION_COMPARE_TWO_DOCFIELD_VALUES

**[Tam Kalıbı Görüntüle →](data-transformation-pattern.md)**

---

## Kalıp Seçim Kılavuzu

### Karmaşıklığa Göre

| Karmaşıklık | Kalıplar | En Uygun |
|------------|----------|----------|
| **Düşük-Orta** | [Task Management](task-management-pattern.md) | Yeni başlayanlar, basit iş akışları |
| **Orta** | [API Integration](api-integration-pattern.md)<br>[Decision Logic](decision-logic-pattern.md)<br>[Data Transformation](data-transformation-pattern.md) | Orta düzey kullanıcılar, standart iş akışları |
| **Orta-Yüksek** | [PO Matching](po-matching-pattern.md) | İleri düzey kullanıcılar, karmaşık doğrulama |

---

### Kullanım Durumuna Göre

| Şunu Yapmam Gerekiyor... | Bu Kalıbı Kullanın |
|--------------|------------------|
| Harici sistemlerle entegre olma | [API Integration Pattern](api-integration-pattern.md) |
| Onay iş akışları oluşturma | [Task Management Pattern](task-management-pattern.md) |
| Satınalma siparişlerine karşı doğrulama | [PO Matching Pattern](po-matching-pattern.md) |
| Koşullara göre yönlendirme | [Decision Logic Pattern](decision-logic-pattern.md) |
| Veriyi hesaplama ve dönüştürme | [Data Transformation Pattern](data-transformation-pattern.md) |

---

### Sektöre/Departmana Göre

| Sektör/Departman | Önerilen Kalıplar |
|---------------------|---------------------|
| **Finans/Muhasebe** | [PO Matching](po-matching-pattern.md), [Task Management](task-management-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Satınalma** | [PO Matching](po-matching-pattern.md), [Decision Logic](decision-logic-pattern.md), [API Integration](api-integration-pattern.md) |
| **Operasyon** | [Task Management](task-management-pattern.md), [Decision Logic](decision-logic-pattern.md) |
| **BT/Entegrasyon** | [API Integration](api-integration-pattern.md), [Data Transformation](data-transformation-pattern.md) |
| **Tüm Departmanlar** | [Decision Logic](decision-logic-pattern.md), [Task Management](task-management-pattern.md) |

---

## Bu Kalıpları Nasıl Kullanırsınız

### Adım 1: Bir Kalıp Seçin

1. Yukarıdaki kalıp açıklamalarını inceleyin
2. Kullanım durumunuzla hangi kalıbın eşleştiğini belirleyin
3. Karmaşıklığı ve tahmini kurulum süresini kontrol edin
4. Kalıp kılavuzundaki "Ne Zaman Kullanılır" bölümünü inceleyin

### Adım 2: Önkoşulları İnceleyin

Her kalıp kılavuzu şunları listeler:
- Gerekli bilgi
- Önce okunacak ilgili kılavuzlar
- Kullanılacak kartlar
- Yapılandırma gereksinimleri

### Adım 3: Adım Adım Talimatları İzleyin

Her kalıp şunları sağlar:
- Eksiksiz iş akışı örneği
- Adım adım uygulama kılavuzu
- Yapılandırma şablonları
- Gerçek dünya örnekleri
- Sorun giderme ipuçları

### Adım 4: İhtiyaçlarınıza Göre Özelleştirin

- Örneği iş kurallarınıza uyarlayın
- Eşikleri ve toleransları ayarlayın
- Yönlendirme mantığını değiştirin
- Gerektiğinde adım ekleyin/çıkarın
- Üretimde kullanmadan önce kapsamlı test edin

### Adım 5: İzleyin ve Optimize Edin

- İş akışı performansını izleyin
- Başarı oranlarını izleyin
- Kullanıcı geri bildirimi toplayın
- Yapılandırmayı iyileştirin
- Özelleştirmeleri belgeleyin

---

## Kalıp Kombinasyonları

Birçok gerçek dünya senaryosu, birden fazla kalıbı birleştirmeyi gerektirir:

### Örnek 1: Eksiksiz Fatura İşleme

```
1. API Integration Pattern → Fetch current pricing
2. Data Transformation Pattern → Calculate totals
3. PO Matching Pattern → Validate against PO
4. Decision Logic Pattern → Route based on variance
5. Task Management Pattern → Create approval tasks
```

### Örnek 2: Yüksek Tutarlı Fatura Onayı

```
1. Data Transformation Pattern → Calculate amounts
2. Decision Logic Pattern → Check thresholds
3. Task Management Pattern → Multi-level approval
4. API Integration Pattern → Notify external systems
```

### Örnek 3: İstisna Yönetimi

```
1. PO Matching Pattern → Detect variances
2. Decision Logic Pattern → Classify exception severity
3. Task Management Pattern → Create review tasks
4. Data Transformation Pattern → Calculate impact
```

---

## Kalıp Şablonları

Her kalıp bu standartlaştırılmış bölümleri içerir:

1. **Overview** - Kalıbın ne yaptığı
2. **When to Use** - Uygun kullanım durumları
3. **Complete Example** - Gerçek dünya senaryosu
4. **Step-by-Step** - Uygulama talimatları
5. **Configuration** - Kart kurulum şablonları
6. **Workflow Diagram** - Görsel temsil
7. **Advanced Variations** - Alternatif uygulamalar
8. **Error Handling** - Yaygın sorunlar ve çözümler
9. **Testing Checklist** - Doğrulama adımları
10. **Related Patterns** - Tamamlayıcı kalıplar
11. **Related Guides** - Referans belgeleri

---

## Yardım Alma

### Kalıp Destek Kaynakları

**Belgeler:**
- [Complete Workflow Guide Index](../README.md)
- [Individual Card Guides](../then/action/)
- [Condition Cards Reference](../and/condition-cards-complete-guide.md)
- [Workflow Linking Map](../../../../WORKFLOW_LINKING_MAP.md)

**Ek Kaynaklar:**
- [Quick Reference Guide](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)
- [October 2025 Release Notes](../changelog/2025-10-october.md)
- [Card Versioning Reference](../../../docs/card_version.md)

**İletişim:**
- Kalıp Geri Bildirimi: docs@docbits.com
- Teknik Destek: support@docbits.com
- Uygulama Yardımı: consulting@docbits.com

---

## Kalıp İstatistikleri

| Metrik | Değer |
|--------|-------|
| **Toplam Kalıp** | 5 |
| **Kapsanan Toplam Kart** | 30+ |
| **Birleşik Belgeler** | ~1.200 satır |
| **Örnek Senaryolar** | 25+ |
| **Yapılandırma Şablonları** | 15+ |
| **İş Akışı Diyagramları** | 5 eksiksiz diyagram |
| **Çapraz Referanslar** | 87+ dahili bağlantı |

---

## Kalıplara Katkıda Bulunma

Başkalarına yararlı olacak bir iş akışı kalıbınız mı var?

**Kalıp Katkı Kuralları:**

1. **İş Akışınızı Belgeleyin**
   - Açık iş senaryosu
   - Adım adım uygulama
   - Çalışan yapılandırma örnekleri
   - Gerçek dünya test sonuçları

2. **Kalıp Şablonunu İzleyin**
   - Standart bölüm yapısını kullanın
   - Tüm gerekli öğeleri ekleyin
   - Diyagramlar/örnekler sağlayın
   - Sorun giderme kılavuzu ekleyin

3. **İnceleme için Gönderin**
   - E-posta gönderin: docs@docbits.com
   - Şunları ekleyin: Kalıp açıklaması, kullanım durumları, uygulama kılavuzu
   - İnceleyip resmi belgelere ekleyebiliriz

**Faydalar:**
- Diğer DocBits kullanıcılarına yardımcı olun
- Belgelerde tanınma kazanın
- Genel ürün bilgi tabanını geliştirin
- Uygulamanız hakkında geri bildirim alın

---

## Değişiklik Günlüğü

### Sürüm 1.0 (23 Ekim 2025)
- 5 kapsamlı iş akışı kalıbının ilk sürümü
- API Integration Pattern eklendi
- Task Management Pattern eklendi
- PO Matching Pattern eklendi
- Decision Logic Pattern eklendi
- Data Transformation Pattern eklendi
- Çapraz referans bağlantısı uygulandı (87 bağlantı)
- Kalıp seçim kılavuzu oluşturuldu

---

## Sonraki Adımlar

**İş Akışı Kalıplarında Yeni misiniz?**
1. [Task Management Pattern](task-management-pattern.md) ile başlayın - anlaması en kolay olanı
2. [Decision Logic Pattern](decision-logic-pattern.md)'i inceleyin - tüm iş akışları için temel
3. [API Integration Pattern](api-integration-pattern.md)'i keşfedin - yaygın entegrasyon ihtiyacı

**Uygulamaya Hazır mısınız?**
1. Yukarıdaki listeden kalıbınızı seçin
2. Eksiksiz kalıp kılavuzunu okuyun
3. Önkoşulları ve ilgili kılavuzları inceleyin
4. Adım adım talimatları izleyin
5. Örnek belgelerle test edin
6. Üretime dağıtın
7. İzleyin ve optimize edin

**Daha Fazla Yardıma mı İhtiyacınız Var?**
- [Workflow Documentation Overview](../README.md)'i inceleyin
- [Quick Reference Guide](../../../../WORKFLOW_LINKING_QUICK_REFERENCE.md)'ı kontrol edin
- Destek ekibiyle iletişime geçin

---

**Son Güncelleme:** 23 Ekim 2025
**Sorumlu:** Belgeleme Ekibi
**Sürüm:** 1.0

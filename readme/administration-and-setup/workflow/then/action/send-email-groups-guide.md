# Send Email to Groups

---

Bu kartı Workflow Builder'ın **Then** grubuna ekleyin — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p><strong>Send Email to Groups</strong> kartı <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Durum:** ✅ Tek Sürüm (Kırıcı Değişiklik Yok)
**En Yeni Sürüm:** v1 (Etkin)
**Not:** Bu kart, çeviri anahtarları aracılığıyla çoklu dil desteğiyle tek sürüm modeli kullanır.

📖 [Eksiksiz Kart Veritabanı](../../../../DocFlow/docs/card_version.md)

---

## Amaç
Bu kart, kullanıcı gruplarına otomatik olarak e-posta bildirimleri gönderir. İşi tek tek kişilere atamak yerine, mesajı bir gruba gönderirsiniz ve o grubun tüm üyeleri onu alır.

**Gerçek dünya örneği:** Yüksek tutarlı bir fatura geldiğinde, "Finance Team" grubundaki herkese otomatik olarak bir e-posta bildirimi gönderin, böylece inceleme gerektiğinden haberdar olurlar.

---

## Bu Kartı Ne Zaman Kullanmalı

Bu kartı şu durumlarda kullanın:
- Birden fazla kişiyi aynı anda bilgilendirme
- Ekip gruplarına uyarılar gönderme
- Departmanlara güncellemeler yayınlama
- Grupları belge durumu değişiklikleri hakkında bilgilendirme
- Grup üyelerine hatırlatıcılar gönderme

**Yaygın senaryolar:**
- Satınalma ekibini yeni tedarikçiler hakkında bilgilendirme
- Finans ekibini yüksek tutarlı faturalar hakkında uyarma
- Depo ekibini sevkiyatlar hakkında bilgilendirme
- Belge durumu değişikliklerini yayınlama

---

## Nasıl Çalışır

1. **Koşul Kontrolü**: İş akışı "Where" ve "And" koşullarını kontrol eder
2. **E-postayı Hazırla**: Sistem, şablonu kullanarak e-postayı hazırlar
3. **Grup Üyelerini Al**: Sistem, belirtilen grubun tüm üyelerini bulur
4. **Gönder**: E-posta her grup üyesine gönderilir
5. **Günlüğe Kaydet**: E-posta gönderimi kaydedilir

---

## Parametreler Açıklaması

### E-posta Şablonu
Gönderilecek e-posta mesajı

**Seçenekler:**
- Mevcut şablonlardan seçin
- Her şablonun önceden tanımlanmış konusu, gövdesi ve biçimlendirmesi vardır
- Şablonlar {document_number}, {supplier_name} gibi yer tutucular içerebilir

**Örnek Şablon:**
```
Subject: Document {document_number} requires review

Body:
Dear Team,

A new invoice has arrived and requires review:
- Document: {document_number}
- Supplier: {supplier_name}
- Amount: {amount} {currency}
- Date: {date}

Please login to DocBits to review.

Best regards,
DocBits Automation
```

### Grup
E-postanın gönderileceği kullanıcı grubu

**Örnek gruplar:**
- Finance Team
- Procurement Team
- Warehouse Team
- Approval Committee
- Management Group

---

## Yapılandırma Adımları

### Adım 1: E-posta Şablonunu Seç
1. "Select Email Template"e tıklayın
2. Listeden şablon seçin
3. Konu ve içeriği doğrulayın

### Adım 2: Grup Seç
1. "Select Group"a tıklayın
2. Bilgilendirmek istediğiniz grubu seçin
3. Grup üyelerini doğrulayın (genellikle sayıyı gösterir)

### Adım 3: Koşulları Ayarla
1. Koşul ekleyin: "When [condition] is true"
2. Örnek: "When invoice amount is greater than €5000"

### Adım 4: Test Et
1. Örnek belgeyle test edin
2. E-postanın gruba gönderildiğini doğrulayın
3. Şablon işlemesini kontrol edin

---

## E-posta Şablonu Örnekleri

### Şablon 1: Yüksek Tutarlı Fatura Uyarısı
```
Subject: High-Value Invoice Alert - {document_number}

Body:
Team,

An invoice exceeding €10,000 has been received:

Document Number: {document_number}
Supplier: {supplier_name}
Amount: {amount} EUR
Received Date: {date}
Status: {status}

This requires immediate review and approval.

---
Sent automatically by DocBits
```

### Şablon 2: Tedarikçi Durumu Değişikliği
```
Subject: Supplier Status Update - {supplier_name}

Body:
Procurement Team,

The following supplier's status has been updated:

Supplier: {supplier_name}
Supplier Code: {supplier_code}
New Status: {status}
Effective Date: {date}

Please update your systems accordingly.

---
Sent automatically by DocBits
```

### Şablon 3: Dışa Aktarmaya Hazır Belge
```
Subject: Document Approved for Export - {document_number}

Body:
Export Team,

The following document has been approved and is ready for export:

Document Number: {document_number}
Invoice Number: {invoice_number}
Supplier: {supplier_name}

Please proceed with export to {destination_system}.

---
Sent automatically by DocBits
```

---

## Yaygın Kullanım Durumları

### Kullanım Durumu 1: Kalite Kontrol Uyarıları
**Tetikleyici:** Fatura ile PO arasında tutarsızlık bulunduğunda

**E-posta Grubu:** Quality Team

**İçerik:**
```
Invoice {number} has quality issues:
- Unit Price variance: 12% (exceeds 5% tolerance)
- Please review and take action
```

### Kullanım Durumu 2: Onay Bildirimleri
**Tetikleyici:** Belge belirli bir duruma ulaştığında

**E-posta Grubu:** Approval Committee

**İçerik:**
```
Document {number} is awaiting approval:
- Amount: {amount}
- Supplier: {supplier_name}
- Please login to approve/reject
```

### Kullanım Durumu 3: İstisna Bildirimleri
**Tetikleyici:** Koşullar karşılanmadığında

**E-posta Grubu:** Managers

**İçerik:**
```
Exception alert for document {number}:
- Supplier code missing
- Delivery date invalid
- Manual review required
```

### Kullanım Durumu 4: Durum Güncellemeleri
**Tetikleyici:** Belge durumu değiştiğinde

**E-posta Grubu:** Sonraki adımdan sorumlu ekip

**İçerik:**
```
Document {number} status changed to: {status}
Assigned to: {assigned_user}
Next steps: {next_steps}
```

---

## Sorun Giderme

### "E-posta alınmadı"

**Olası Nedenler:**
- [ ] Gruptaki kullanıcıların e-posta adresleri yok
- [ ] E-posta spam filtresi tarafından engellendi
- [ ] Gruptaki e-posta adresi yanlış
- [ ] Grubun üyesi yok

**Çözümler:**
1. Tüm grup üyelerinin e-posta adreslerinin olduğunu doğrulayın
2. Spam/önemsiz klasörünü kontrol edin
3. Grup üyeliğinin doğru olduğunu doğrulayın
4. Eksikse kullanıcıları gruba ekleyin
5. E-posta servisinin çalıştığını BT ile kontrol edin

### "Şablon doğru işlenmiyor"

**Neden:** Yer tutucu değişkenler bulunamadı

**Çözüm:**
- [ ] Alan adlarının tam olarak eşleştiğini doğrulayın
- [ ] Alanın belgede bir değere sahip olup olmadığını kontrol edin
- [ ] Doğru yer tutucu biçimini kullanın: {field_name}
- [ ] Tüm alanları içeren örnek belgeyle test edin

### "Bazı kişiler e-posta alıyor, diğerleri almıyor"

**Neden:** Eksik grup üyeliği veya geçersiz e-postalar

**Çözümler:**
- [ ] Tüm üyelerin geçerli e-postası olduğunu doğrulayın
- [ ] Bazı kullanıcıların devre dışı bırakılıp bırakılmadığını kontrol edin
- [ ] Grup üyeliğinin güncel olduğunu doğrulayın
- [ ] E-posta adreslerini doğrulamak için BT ile iletişime geçin

### "Gruptan kişi eklemek/çıkarmak istiyorum"

**Çözüm:**
- Yöneticinizle iletişime geçin
- Gruplar sistem ayarlarında yönetilir
- Bu karttan değiştirilemez
- BT'den grup üyeliği değişiklikleri isteyin

---

## E-posta Şablonu Özelleştirme

### Kullanılabilir Yer Tutucular
```
{document_number} - Document ID
{invoice_number} - Invoice ID
{supplier_name} - Supplier name
{supplier_code} - Supplier code
{amount} - Invoice amount
{currency} - Currency (EUR, USD, etc.)
{date} - Document date
{status} - Current status
{assigned_user} - Assigned person
{assigned_group} - Assigned group
{next_steps} - What needs to happen next
{reason} - Reason for exception/alert
{comment} - Comments or notes
```

### Özel Yer Tutucular Oluşturma
E-postalarda ek veriye ihtiyacınız varsa:
1. Yöneticinizle iletişime geçin
2. Yeni yer tutucu isteyin
3. Belgeye gerekli alanı ekleyin
4. E-posta şablonunu güncelleyin

---

## En İyi Uygulamalar

✅ **Yapın:**
- E-posta içeriğini kısa ve net tutun
- Eylem öğeleri ekleyin (alıcılar ne yapmalı?)
- Belgeye erişmek için bağlantı veya talimatlar ekleyin
- Şablonu örnek veriyle test edin
- Doğru gruba gönderin (aşırı bildirim yapmayın)
- Tutarlılık için şablonlar kullanın

❌ **Yapmayın:**
- Çok fazla e-posta gönderme (bildirim yorgunluğu)
- E-postalara hassas veri ekleme
- Bilgiye ihtiyacı olmayan gruplara gönderme
- Belirsiz konu satırları kullanma
- Nasıl eylem alınacağını eklemeyi unutma
- Bireylere e-posta gönderme (bunun yerine grup kullanın)

---

## Performans Notları

- Her e-posta gönderilmesi ~1 saniye sürer
- Büyük gruplar zaman alabilir (100 kişi = ~100 saniye)
- Binlerce e-posta gönderen döngüler oluşturmayın
- E-posta servisi kapasitesini izleyin
- Çok sayıda belge varsa toplu işlemeyi düşünün

---

## İlgili Kartlar

- **ACTION_SEND_EMAIL** - Bireysel kişiye gönder
- **ACTION_ASSIGN_TASK_TO_PROCUREMENT_GROUP** - Yalnızca bildirmek yerine görev ata
- **ACTION_CREATE_TASK_FOR_GROUP_SEQUENTIAL** - Görev oluştur ve bildir
- **STAUS_CHANGE** - Durumu değiştir ve bildir

---

## Tipik İş Akışı Örneği

```
Document Arrives
    ↓
Check Condition: "Is amount > €10,000?"
    ↓
YES: Send Email to Finance Team
     "High value invoice alert"
    ↓
Send Email to Procurement Team
     "New invoice from supplier"
    ↓
Workflow Continues
```

---

## SSS

**S: Birden fazla gruba gönderebilir miyim?**
C: Her grup için ayrı kartlar oluşturun

**S: Birinin e-postası geri dönerse ne olur?**
C: E-posta başarısız olarak günlüğe kaydedilir, BT sorun giderebilir

**S: E-posta şablonunu değiştirebilir miyim?**
C: Şablonları değiştirmek için yöneticinizle iletişime geçin

**S: Koşullara göre gönderebilir miyim?**
C: Evet! E-postaların ne zaman gönderileceğini kontrol etmek için "Where" ve "And" koşullarını kullanın

**S: E-postanın alınıp alınmadığını nasıl bilirim?**
C: Gönderim durumu için DocBits'teki e-posta günlüklerini kontrol edin

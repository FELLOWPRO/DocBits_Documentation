# Send HTTPS Request

---

Bu kartı Workflow Builder'ın **Then** grubuna ekleyin — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p><strong>Send HTTPS Request</strong> kartı <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Geçerli Sürüm:** v2 (En Yeni ve Önerilen)
**Durum:** ✅ Etkin

**Sürüm Geçmişi:**
- v1 → Basit HTTP isteği (artık önerilmez)
- **v2 → GEÇERLİ** (çoklu dil desteği eklendi)

**Ne Değişti:** v2, uluslararasılaştırma (i18n) desteği ekledi. Temel webhook/istek işlevselliği değişmeden kalır.

📖 [Sürüm Geçmişi ve Değişiklikler](../../../changelog/release.md#2-https-request-https_request) | [Eksiksiz Kart Veritabanı](../../../../DocFlow/docs/card_version.md)

---

## Amaç
Bu kart, bir web sitesine veya servise güvenli bir mesaj gönderir ve geri yanıt alabilir. "Call API" kartından daha basittir ve hızlı entegrasyonlar için yararlıdır.

**Gerçek dünya örneği:** Fatura verilerini muhasebe sisteminize gönderin veya harici bir sisteme bir çalışanın bu satın almayı işleme yetkisinin olup olmadığını sorun.

---

## Bu Kartı Ne Zaman Kullanmalı

Bu kartı şu durumlarda kullanın:
- Harici servislere webhook bildirimleri gönderme
- Diğer sistemlerde eylemleri tetikleme
- Basit bir web servisini sorgulama
- Diğer uygulamalara durum güncellemeleri gönderme
- Karmaşık API gereksinimleri olmadan basit entegrasyonlar gerçekleştirme

---

## Nasıl Çalışır

1. **Tetikleyici Kontrolü**: Sistem, "Where" ve "And" koşullarının karşılanıp karşılanmadığını kontrol eder
2. **İstek Oluştur**: Sistem, HTTPS isteğini parametrelerinizle hazırlar
3. **Güvenli Gönder**: Veri, güvenli HTTPS bağlantısı kullanılarak gönderilir
4. **Yanıt Al**: Harici servis yanıt verir
5. **Devam Et**: İş akışı yanıt verisiyle ilerler

---

## Parametreler

### URL
İsteğin gönderileceği web sitesi adresi

**Örnek:** `https://webhook.company.com/process`

### Başlıklar (Headers)
Alıcı için özel talimatlar

**Örnek:**
```
Content-Type: application/json
Authorization: Bearer token123
```

### Yöntem (Method)
- **GET**: Bilgi isteme
- **POST**: Veri gönderme
- **PUT**: Veri güncelleme

### Parametreler (Sorgu Dizesi)
URL'ye eklenen veri

**Örnek:** `?action=approve&user_id=123`

### İstek Verisi
Gönderilen gerçek bilgi (JSON biçiminde)

**Örnek:**
```json
{
  "invoice_number": "INV-2025-001",
  "amount": 5000,
  "currency": "EUR"
}
```

---

## Adım Adım Örnek

### Senaryo: Faturayı Muhasebe Sistemine Gönderme

**Kart Yapılandırması:**
- **URL:** `https://accounting.company.com/invoices/create`
- **Yöntem:** POST
- **Başlıklar:** `Authorization: Bearer YOUR-TOKEN`
- **İstek Verisi:**
```json
{
  "supplier_id": "SUPP001",
  "invoice_number": "12345",
  "amount": 1500.00,
  "currency": "EUR",
  "date": "2025-10-23"
}
```

**Beklenen Yanıt:**
```json
{
  "status": "success",
  "accounting_id": "ACC-98765",
  "message": "Invoice recorded in accounting system"
}
```

---

## Yaygın Kullanım Durumları

### 1. Webhook Bildirimleri
DocFlow'da bir şey olduğunda diğer sistemlere gerçek zamanlı bildirimler gönderin

**Örnek:**
- Belge onaylandı → Yerine getirme sistemine bildirim gönder
- Tedarikçi değişti → Slack/Teams webhook'u aracılığıyla satınalma ekibine bildir

### 2. Harici Sistem Entegrasyonu
Otomatik veri alışverişi için DocFlow'u diğer iş sistemleriyle bağlayın

**Örnek:**
- Belge işlendikten sonra → ERP sistemine senkronize et
- Yeni tedarikçi eklendi → Ana veri sisteminde tedarikçi kaydı oluştur

### 3. Onay İş Akışları
Belgeyi harici onay sistemine gönderin ve karar alın

**Örnek:**
- Yüksek tutarlı fatura → Onay için Finans'a gönder
- Belgeyi kararla birlikte harici sisteme geri döndür

---

## Yapılandırma Kılavuzu

### Adım 1: Uç Nokta Bilgilerini Al
Alıcı sistemden şunları isteyin:
- [ ] HTTPS URL'si
- [ ] Gerekli başlıklar
- [ ] Kimlik doğrulama yöntemi
- [ ] Beklenen istek biçimi
- [ ] Beklenen yanıt biçimi

### Adım 2: Kartı Yapılandır
1. HTTPS URL'sini girin
2. HTTP yöntemini ayarlayın (genellikle POST)
3. Gerekirse kimlik doğrulama ekleyin
4. İstek verisini JSON olarak biçimlendirin
5. Herhangi bir özel başlık ekleyin

### Adım 3: Test Et
Bir test isteği gönderin ve yanıtı doğrulayın

---

## Yanıt Yönetimi

HTTPS isteğiniz bir yanıt alacaktır. Yaygın yanıtlar:

### Başarı (200, 201)
```json
{
  "success": true,
  "id": "REC-12345",
  "status": "processed"
}
```

### Geçersiz İstek (400)
```json
{
  "error": "Missing required field: invoice_number"
}
```

### Yetkisiz (401)
```json
{
  "error": "Invalid authentication token"
}
```

### Sunucu Hatası (500)
Alıcı sistemin dahili bir sorunu var

---

## Sorun Giderme

### "Certificate Error"
**Neden:** HTTPS güvenlik sertifikası sorunu

**Çözüm:**
- URL'nin doğru olduğunu doğrulayın
- Web sitesinin sertifikasının geçerli olup olmadığını kontrol edin
- HTTPS kullandığınızdan emin olun (HTTP değil)

### "Connection Refused"
**Neden:** Sunucuya bağlanılamıyor

**Çözüm:**
- URL/IP adresinin doğru olduğunu doğrulayın
- Servisin çalışıp çalışmadığını kontrol edin
- Güvenlik duvarı kurallarını kontrol edin
- İnternet bağlantısını doğrulayın

### "No Response / Timeout"
**Neden:** Sunucu zaman sınırı içinde yanıt vermiyor

**Çözüm:**
- Servisin kullanılabilir olup olmadığını kontrol edin
- Uç nokta URL'sini doğrulayın
- Hız sınırları olup olmadığını kontrol edin
- Sistem yöneticisiyle iletişime geçin

### "Invalid JSON"
**Neden:** İstek verisi hatalı biçimlendirilmiş

**Çözüm:**
- JSON'da eksik virgülleri kontrol edin
- Tüm tırnakların doğru olduğunu doğrulayın
- JSON biçimini doğrulayın (çevrimiçi JSON doğrulayıcı kullanın)
- Özel karakterleri kontrol edin

---

## Örnekler

### Örnek 1: Webhook Servisine Gönderme
```
URL: https://webhook.site/your-unique-id
Method: POST
Data:
{
  "document_id": "DOC-123",
  "status": "approved",
  "amount": 5000
}
```

### Örnek 2: Harici Sistemi Güncelleme
```
URL: https://api.company.com/update
Method: PUT
Data:
{
  "record_id": "REC-456",
  "status": "completed",
  "timestamp": "2025-10-23T10:30:00"
}
```

### Örnek 3: Harici Servisi Sorgulama
```
URL: https://lookup.company.com/validate?id=SUP-789
Method: GET
Headers: Authorization: Bearer token
```

---

## "Call API" Kartından Farkı

| Özellik | HTTPS Request | Call API |
|---------|---------------|----------|
| Basitlik | Basit | Daha karmaşık |
| Parametreler | Temel | Gelişmiş |
| Hata Yönetimi | Temel | Ayrıntılı |
| Kullanım | Hızlı entegrasyonlar | Karmaşık API'ler |
| En uygun | Webhook'lar | Profesyonel API'ler |

---

## Güvenlik Değerlendirmeleri

✅ **Her zaman HTTPS kullanın** (güvenli bağlantı)

⚠️ **Asla:**
- Parolaları URL'ye koymayın
- API anahtarlarını günlüklerde açığa çıkarmayın
- Parametrelere kişisel veri eklemeyin
- Hassas veriler için HTTP kullanmayın

---

## En İyi Uygulamalar

✅ **Yapın:**
- Önce küçük miktarda veriyle test edin
- Hata yönetimi ekleyin
- Önemli istekleri günlüğe kaydedin
- Entegrasyonu belgeleyin
- Hatalar için izleyin

❌ **Yapmayın:**
- Gerekli değilse aynı uç noktayı tekrar tekrar çağırma
- Yanıt hatalarını görmezden gelme
- Hassas veriyi düz metin olarak dahil etme
- Servis hız sınırlarını aşma

---

## İlgili Kartlar

- **CALL_API** - Daha gelişmiş API entegrasyonu
- **CONDITION_HTTPS_REQUEST_STATUS** - İsteğin başarılı olup olmadığını kontrol et
- **ACTION_SEND_EMAIL** - Bunun yerine e-posta yoluyla gönder
- **ACTION_RUN_DOCOPERATOR_SCRIPT** - Otomatik betikler

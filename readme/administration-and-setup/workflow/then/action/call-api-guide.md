# Call External API

---

Bu kartı Workflow Builder'ın **Then** grubuna ekleyin — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p><strong>Call External API</strong> kartı <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Geçerli Sürüm:** v2 (En Yeni ve Önerilen)
**Durum:** ✅ Etkin

**Sürüm Geçmişi:**
- v1 → Temel API çağrısı (artık önerilmez)
- **v2 → GEÇERLİ** (çoklu dil desteği eklendi)

**Ne Değişti:** v2, çeviri anahtarlarıyla uluslararasılaştırma (i18n) desteği ekledi. İşlevsellik aynı kalır.

📖 [Sürüm Geçmişi ve Değişiklikler](../../../changelog/release.md#1-call_api) | [Eksiksiz Kart Veritabanı](../../../../DocFlow/docs/card_version.md#call_api)

---

## Amaç
Bu kart, harici bir web sitesine veya servise veri göndermenize ve geri bilgi almanıza olanak tanır. Bunu, harici bir servise bir soru gönderip iş akışınızda kullanabileceğiniz bir yanıt almak gibi düşünün.

**Gerçek dünya örneği:** Şirketiniz başka bir web sitesinde bir fiyatlandırma sistemi kullanıyor. Bu kart, o fiyatlandırma sistemine bir öğenin güncel fiyatını otomatik olarak sorabilir ve o fiyatı belgenize getirebilir.

---

## Bu Kartı Ne Zaman Kullanmalı

Bu kartı şu durumlarda kullanın:
- Harici bir servisten bilgi alma (fiyatlandırma, doğrulama veya arama verisi gibi)
- Belge bilgilerini işleme için başka bir sisteme gönderme
- Üçüncü taraf servislerle entegre olma
- Manuel aramalar olmadan otomatik veri alma
- Birden fazla iş sistemini birbirine bağlama

**Yaygın senaryolar:**
- Bir veritabanından tedarikçi bilgilerini arama
- Bir fiyatlandırma servisinden gerçek zamanlı fiyatlandırma alma
- Veriyi harici bir sisteme karşı doğrulama
- Bir lojistik sağlayıcısından sevkiyat bilgilerini alma

---

## Nasıl Çalışır

1. **Koşul Kontrolü**: İş akışı önce "Where" ve "And" bölümlerindeki koşulların karşılanıp karşılanmadığını kontrol eder
2. **Veriyi Hazırla**: Kart, yapılandırdığınız parametreleri toplar
3. **İstek Gönder**: Verilerinizi harici API'ye/servise gönderir
4. **Yanıt Al**: Harici servis verilerle yanıt verir
5. **Devam Et**: İş akışı bu veriyi sonraki kartlarda kullanır

---

## Parametreler Açıklaması

### API Uç Noktası URL'si
**Nedir:** İletişim kurmak istediğiniz harici servisin adresi

**Örnek:** `https://api.supplier-system.com/product/pricing`

**Nasıl bulunur:** BT ekibinizden veya servis sağlayıcısından API uç noktalarını isteyin

---

### HTTP Yöntemi
**Nedir:** Gönderilecek istek türü

**Seçenekler:**
- **GET**: Bilgi isteme (bir soru sormak gibi)
- **POST**: Yeni veri gönderme
- **PUT**: Mevcut veriyi güncelleme
- **DELETE**: Veriyi kaldırma

**En yaygın:** GET (bilgi alma için)

---

### Başlıklar (Headers)
**Nedir:** Çağırdığınız servis için ek talimatlar

**Örnek:**
```
Authorization: Bearer your-api-key
Content-Type: application/json
```

**Neden gerekli:** Servisler genellikle kimlik doğrulama veya belirli biçim talimatları gerektirir

---

### Parametreler (Sorgu Parametreleri)
**Nedir:** URL'de geçirilen ek bilgi

**Örnek:**
```
?supplier_id=12345&currency=USD
```

**Gerçek örnek:** Fiyat istiyorsanız, parametreler tedarikçi kimliğini ve para birimini içerebilir

---

### İstek Verisi (Gövde)
**Nedir:** Servise gönderdiğiniz bilgi

**Örnek:**
```json
{
  "product_id": "ABC123",
  "quantity": 100,
  "currency": "EUR"
}
```

**Ne zaman kullanılır:** POST veya PUT yöntemleri kullanılırken

---

## Adım Adım Örnek

### Senaryo: Gerçek Zamanlı Tedarikçi Fiyatlandırması Alma

**Kurulum:**
1. **Kart Türü:** Call API
2. **API Uç Noktası:** `https://api.suppliers.com/v1/prices`
3. **Yöntem:** POST
4. **Başlıklar:** `Authorization: Bearer YOUR-API-KEY`
5. **İstek Verisi:**
   ```json
   {
     "product_id": "ABC123",
     "quantity": 100
   }
   ```

**Ne olur:**
1. Belge, Product ID: ABC123, Quantity: 100 ile gelir
2. Kart, tedarikçinin API'sine istek gönderir
3. Tedarikçinin API'si şununla yanıt verir: `{"unit_price": 25.50, "total_price": 2550}`
4. İş akışı bu fiyatlandırma bilgisiyle devam eder
5. Bir sonraki kart bu veriyi fatura fiyatını doğrulamak için kullanabilir

---

## Yapılandırma Adımları

### 1. API Bilgilerini Al
Harici servis sağlayıcısıyla iletişime geçin ve şunları isteyin:
- [ ] API uç noktası URL'si
- [ ] Kimlik doğrulama yöntemi (API anahtarı, kullanıcı adı/parola, OAuth)
- [ ] Gerekli parametreler
- [ ] Beklenen yanıt biçimi
- [ ] Hız sınırları veya kotalar

### 2. Kartı Yapılandır
1. API uç noktası URL'sini girin
2. HTTP yöntemini seçin (genellikle GET veya POST)
3. Gerekirse kimlik doğrulama başlıkları ekleyin
4. Gerekli parametreleri ekleyin
5. Gerekirse istek verisini JSON olarak biçimlendirin

### 3. Kartı Test Et
1. Bir test belgesi kullanın
2. İş akışını çalıştırın
3. Yanıtın doğru alınıp alınmadığını kontrol edin
4. Veri biçiminin beklentilerle eşleştiğini doğrulayın

---

## Yaygın Yanıt Senaryoları

### Başarılı Yanıt (Durum Kodu 200)
```json
{
  "success": true,
  "data": {
    "price": 150,
    "currency": "EUR",
    "delivery_days": 5
  }
}
```
✅ Veri, sonraki kartların kullanması için kullanılabilir

### Hata Yanıtı (Durum Kodu 404)
```json
{
  "error": "Product not found"
}
```
⚠️ API aradığınız şeyi bulamadı

### Zaman Aşımı
Harici servis zaman sınırı içinde yanıt vermedi
⚠️ Servisin kullanılabilir olup olmadığını veya uç nokta URL'sinin doğru olup olmadığını kontrol edin

---

## Örnek İş Akışları

### Örnek 1: Otomatik Fiyat Doğrulaması
**Senaryo:** Fatura fiyatlarını tedarikçinin güncel fiyatlandırmasına karşı doğrulama

**Akış:**
1. Belge fatura satır öğesiyle gelir (Product: A123, Price: €50)
2. **Call API Kartı** → Tedarikçi API'sine sorar: "A123 için güncel fiyat nedir?"
3. Tedarikçi yanıtlar: "€48"
4. **Koşul Kartı** → Fatura fiyatının (€50) güncel fiyatın (€48) %5'i içinde olup olmadığını kontrol eder
5. **Onay Kartı** → Tolerans içindeyse onaylar

### Örnek 2: Otomatik Tedarikçi Araması
**Senaryo:** Merkezi veritabanından tedarikçi ana verisi alma

**Akış:**
1. Fatura Supplier Code: SUPP-789 ile gelir
2. **Call API Kartı** → Sisteme sorar: "SUPP-789 tedarikçisi için ayrıntıları ver"
3. Sistem şununla yanıt verir: Ad, İletişim, Koşullar vb.
4. **Set Field Kartları** → Belge alanlarını bu veriyle doldurur
5. **Export Kartı** → Eksiksiz bilgiyle dışa aktar

### Örnek 3: Gerçek Zamanlı Nakliye Maliyetleri
**Senaryo:** Varış noktasına göre otomatik nakliye maliyeti alma

**Akış:**
1. Belgenin teslimat adresi var
2. **Call API Kartı** → Nakliye sağlayıcısına sor: "[adres]'e maliyet nedir?"
3. Sağlayıcı nakliye maliyetiyle yanıt verir
4. **Calculate Kartı** → Nakliyeyi toplam fatura tutarına ekle
5. **Export Kartı** → Güncellenmiş toplamla gönder

---

## Sorun Giderme

### "Connection Timeout" Hatası
**Neden:** API servisi yanıt vermiyor

**Çözümler:**
- [ ] Servisin kullanılabilir olup olmadığını kontrol edin (web sitesini ziyaret edin)
- [ ] Uç nokta URL'sinin doğru olduğunu doğrulayın (yazım hatası yok)
- [ ] İnternet bağlantısını kontrol edin
- [ ] Servis sağlayıcısıyla iletişime geçin
- [ ] Servisin hız sınırları olup olmadığını kontrol edin (çok fazla istek gönderiyorsunuz)

### "Unauthorized" veya "403 Forbidden" Hatası
**Neden:** Kimlik doğrulama başarısız

**Çözümler:**
- [ ] API anahtarınızın doğru olduğunu doğrulayın
- [ ] API anahtarınızın süresinin dolup dolmadığını kontrol edin
- [ ] Kimlik doğrulama başlığının doğru biçimlendirildiğinden emin olun
- [ ] Bu uç nokta için izinlere sahip olduğunuzu doğrulayın

### "Bad Request" veya "400 Error"
**Neden:** İstek verisi biçimi yanlış

**Çözümler:**
- [ ] JSON sözdizimini kontrol edin (eksik virgüller, tırnaklar vb.)
- [ ] Tüm gerekli alanların dahil edildiğini doğrulayın
- [ ] Parametre adlarının servisin beklediğiyle eşleştiğini kontrol edin
- [ ] API belgelerine başvurun

### "Yanıt beklendiği gibi çalışmıyor"
**Çözümler:**
- [ ] API'yi Postman gibi bir araç kullanarak test edin
- [ ] Gerçek yanıt biçimini beklenen biçimle karşılaştırın
- [ ] API'nin belgelerinin değişip değişmediğini kontrol edin
- [ ] Gönderdiğiniz verinin doğru olduğunu doğrulayın

---

## Yanıt Verisi Kullanımı

API'den veri aldığınızda, sonraki kartlar onu kullanabilir:

```
API Response:
{
  "unit_price": 45.00,
  "currency": "USD",
  "available": true
}

Next Card (Set Field):
- Set "Unit_Price" field to 45.00
- Set "Currency" field to USD
- Set "In_Stock" checkbox to true
```

---

## Güvenlik Notları

⚠️ **Önemli:** Diğer kullanıcılar tarafından görülebilecek hassas bilgileri asla kart yapılandırmasına koymayın

- Parolaları sabit kodlamayın
- API anahtarlarını güvenli bir şekilde kullanın
- Günlüklere kişisel veri eklemeyin
- HTTPS uç noktaları kullanın (HTTP değil)

---

## İpuçları ve En İyi Uygulamalar

✅ **Yapın:**
- Önce küçük bir belge örneğiyle test edin
- API çağrılarını basit ve odaklı tutun
- Koşul kartlarıyla hata yönetimi ekleyin
- API kullanımını/maliyetlerini izleyin
- API gereksinimlerini ekibiniz için belgeleyin

❌ **Yapmayın:**
- Veriyi önbelleğe alabiliyorsanız her tek istek için API çağırma
- Yanıt hata kodlarını görmezden gelme
- Üretimde test API'leri kullanma
- Kimlik doğrulama başlıkları eklemeyi unutma
- API'nin her zaman kullanılabilir olacağını varsayma

---

## İlgili Kartlar

- **ACTION_HTTPS_REQUEST** - Benzer ama daha basit HTTPS istekleri
- **CONDITION_HTTPS_REQUEST_STATUS** - API çağrısının başarılı olup olmadığını kontrol et
- **ACTION_SEND_EMAIL** - Veriyi API yerine e-posta yoluyla gönder
- **CALL_API** (farklı sürüm) - Alternatif API çağrı yöntemi

---

## Yardıma mı İhtiyacınız Var?

- BT/Entegrasyon ekibinizden API belgelerini isteyin
- Önce API uç noktalarını test etmek için Postman aracını kullanın
- Servis sağlayıcısının destek portalını kontrol edin
- Gerekli biçimler için API belgelerini inceleyin

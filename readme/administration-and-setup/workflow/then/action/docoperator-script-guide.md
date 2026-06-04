# Run DocOperator Prompt (Automation Script)

---

Bu kartı Workflow Builder'ın **Then** grubuna ekleyin — When/And koşulları eşleştiğinde çalışan eylemler:

<figure><img src="../../../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kart gruplarıyla Workflow Builder tuvali"><figcaption><p><strong>Run DocOperator Prompt</strong> kartı <strong>Then</strong> grubuna <strong>Add Card</strong> aracılığıyla eklenir.</p></figcaption></figure>

---

## 📌 Sürüm Bilgileri

**Geçerli Sürüm:** v3 (En Yeni ve Önerilen)
**Durum:** ✅ Etkin

**Sürüm Geçmişi:**
- v2 → Orijinal DocOperator uygulaması
- **v3 → GEÇERLİ** (yürütme kontrol parametresi eklendi)
- v4 → Kullanımdan kaldırıldı (özellikler geri alındı)

**Ne Değişti:** v3, daha fazla kontrol için isteğe bağlı "Execute the prompt" parametresini ekledi. v4 bunu geri almaya çalıştı ancak kullanımdan kaldırıldı.

📖 [Sürüm Geçmişi ve Değişiklikler](../../../changelog/release.md#3-action_run_docoperator_script--) | [Eksiksiz Kart Veritabanı](../../../../DocFlow/docs/card_version.md#action_run_docoperator_script)

---

## Amaç
Bu kart, DocOperator kullanarak otomatik bir tarayıcı eylemi veya betiği çalıştırır. Bunu, tıpkı bir insan gibi web siteleri veya sistemlerle etkileşime girebilen bir robot gibi düşünün — düğmelere tıklama, formları doldurma, veri çıkarma vb.

**Gerçek dünya örneği:** Şirketiniz web tabanlı bir satınalma sistemi kullanıyor. Bu kart otomatik olarak oturum açabilir, bir ürün arayabilir, kullanılabilirliği kontrol edebilir ve güncel fiyatı alabilir — tümü kimse manuel olarak yapmadan.

---

## Bu Kartı Ne Zaman Kullanmalı

Bu kartı şu durumlarda kullanın:
- API'leri olmayan web sitelerindeki görevleri otomatikleştirme
- Web sayfalarından veri çıkarma
- Formları otomatik olarak doldurma
- Sistemlere oturum açma ve bilgi alma
- Tekrarlayan manuel görevleri otomatikleştirme
- Entegre olmayan eski sistemlerle etkileşim

**Yaygın senaryolar:**
- Tedarikçi web sitelerine oturum açma ve gerçek zamanlı envanteri alma
- Harici sistemlerde formları otomatik olarak doldurma
- API sunmayan web sayfalarından veri çıkarma
- Kurye web sitelerinde teslimat durumunu kontrol etme
- API erişimi olmayan sistemlerden fiyatlandırma alma

---

## Nasıl Çalışır

1. **Kart Tetiklendi**: İş akışı bu karta ulaşır ve koşullar karşılanır
2. **Betik Başlar**: DocOperator botu otomasyon betiğinizi çalıştırmaya başlar
3. **Bot Eylemleri**: Bot, tıklama, yazma, kaydırma, çıkarma gibi eylemler gerçekleştirir
4. **Veri Çıkarma**: Bot, web sayfalarından bilgi toplar
5. **Veriyi Döndür**: Veri, sonraki kartlarda kullanılmak üzere DocFlow'a geri döner
6. **Zaman Aşımı Yönetimi**: Betik çok uzun sürerse, durur ve sahip olduğunu döndürür

---

## Parametreler Açıklaması

### DocOperator Prompt'u/Betiği
DocOperator'a tam olarak ne yapacağını söyleyen otomasyon betiği

**Örnek (Düz Türkçe):**
```
1. Go to https://supplier.com/login
2. Enter username: myuser
3. Enter password: mypass
4. Click Login button
5. Search for product "ABC123"
6. Extract the price
7. Return the price
```

### Değişkenler
Betiğe AKTARMAK istediğiniz veri

**Örnek:**
```
product_id: "ABC123"
supplier_code: "SUPP-001"
```

Bu değişkenler betikte şu şekilde kullanılabilir:
```
Search for product "{product_id}"
Find supplier "{supplier_code}"
```

### Maksimum Adım
Botun gerçekleştirmesine izin verilen eylem sayısı

**Tipik değerler:**
- Basit görev (bir fiyat almak gibi): 10-20 adım
- Orta karmaşıklık (form doldur + çıkar): 20-50 adım
- Karmaşık iş akışı (oturum aç + ara + doğrula): 50-100 adım

**Neden önemli:** Sonsuz döngüleri ve çok uzun süren betikleri önler

### Maksimum Yeniden Deneme
Bot bir eylemde başarısız olursa, kaç kez tekrar denemelidir?

**Örnekler:**
- 1: Bir kez dene, başarısız olursa devam et
- 3: Pes etmeden önce 3 kez dene
- 5: Çok ısrarcı - 5 kez dene

---

## Adım Adım Örnek

### Senaryo: Web Sitesinden Tedarikçi Fiyatlandırması Alma

**Betik Tanımı:**
```
Step 1: Open website https://prices.supplier-xyz.com
Step 2: Click on "Product Lookup"
Step 3: Enter product code: ABC-123
Step 4: Click "Search"
Step 5: Wait for results to load (3 seconds)
Step 6: Extract price from the page
Step 7: Extract available quantity
Step 8: Return both values
```

**Aktarılan Değişkenler:**
```
product_code = "ABC-123"
supplier_name = "Supplier XYZ"
```

**Değişkenleri Kullanan Betik:**
```
Open website https://prices.{supplier_name}.com
Enter product code: {product_code}
Extract price and quantity
```

**Beklenen Sonuç:**
```
price: 45.50
quantity_available: 500
```

---

## DocOperator'ın Gerçekleştirebileceği Eylem Türleri

### Gezinme
- URL'ye git
- Bağlantılara tıkla
- Düğmelere bas
- Sayfayı kaydır

### Form Doldurma
- Alanlara metin yaz
- Açılır menü seçeneklerini seç
- Kutuları işaretle/işaretsiz bırak
- Düğmelere tıkla

### Veri Çıkarma
- Sayfadan metin oku
- Sayıları çıkar
- Tablo verisi al
- Bilgi kopyala

### Bekleme
- Sayfanın yüklenmesini bekle
- Öğelerin görünmesini bekle
- Dinamik içeriği bekle

### Koşullu Mantık
- Bir şey varsa, bunu yap
- Metin eşleşirse, o zaman...
- Sonuçları say ve buna göre hareket et

---

## Yaygın Kullanım Durumları

### 1. Gerçek Zamanlı Fiyatlandırma Alma
**Senaryo:** Tedarikçinin API'si yok ama web sitesi fiyatları gösteriyor

**Betik:**
```
1. Go to supplier website
2. Search for product
3. Extract price from results
4. Return price to DocFlow
5. Use price to validate invoice
```

### 2. Envanter Kullanılabilirliğini Kontrol Etme
**Senaryo:** Tedarikçinin stoku olup olmadığını bilmeniz gerekiyor

**Betik:**
```
1. Log into supplier portal
2. Search for product
3. Extract availability status
4. Extract delivery time
5. Return both to DocFlow
```

### 3. Otomatik Form Gönderimi
**Senaryo:** Harici bir sitede bir formu doldurmanız gerekiyor

**Betik:**
```
1. Navigate to form page
2. Fill Company Name field
3. Fill Contact Email field
4. Select Country from dropdown
5. Upload file attachment
6. Click Submit button
7. Capture confirmation message
```

### 4. Veri Girişi Doğrulaması
**Senaryo:** İki farklı sistemde verinin eşleştiğini doğrulama

**Betik:**
```
1. Go to System A
2. Search for Order #123
3. Extract order amount
4. Go to System B
5. Search for Order #123
6. Extract order amount
7. Compare amounts
8. Return true/false if they match
```

---

## Yapılandırma Adımları

### Adım 1: Betiği Oluştur
1. Neyi başarmak istediğinizi tanımlayın
2. Bunu küçük adımlara bölün
3. Her adımı açıkça yazın
4. Önce manuel olarak test edin (web sitesini açın, kendiniz yapın)
5. Tam olarak neyi tıkladığınızı, nereye yazdığınızı, neyi çıkardığınızı belgeleyin

### Adım 2: Değişkenleri Belirle
1. Belgeler arasında hangi veri değişecek?
2. Betiğe ne aktarılmalı?
3. Değişken adlarını tanımlayın
4. Değişkenlerin betikte nerede kullanıldığını belirtin

### Adım 3: Parametreleri Ayarla
- **Maksimum Adım**: Betik karmaşıklığına göre
- **Maksimum Yeniden Deneme**: Bot ne kadar ısrarcı olmalı?
- **Zaman Aşımı**: Sayfalar için ne kadar beklemeli?

### Adım 4: Test Et
1. Örnek veriyle test edin
2. Botun web sitesine erişebildiğini doğrulayın
3. Çıkarmanın doğru olduğunu doğrulayın
4. Değişkenlerin düzgün çalışıp çalışmadığını kontrol edin

---

## Betik Yazma İpuçları

### Açık Dil
✅ **Yapın:**
```
1. Click the "Login" button
2. Type the username in the login field
3. Wait 2 seconds for form to process
```

❌ **Yapmayın:**
```
1. Do the login thing
2. Enter stuff
3. Wait for it
```

### Belirli Seçiciler
✅ **Yapın:**
```
Click the button labeled "Submit Order"
Type in the field with placeholder "Enter Email"
```

❌ **Yapmayın:**
```
Click somewhere
Type in a field
```

### Hata Yönetimi
✅ **Yapın:**
```
1. Try to click "Next" button
2. If button not found, extract data from current page
3. Return what we have
```

❌ **Yapmayın:**
```
Click "Next" (assumes it's always there)
```

---

## Sorun Giderme

### "Script Timed Out"
**Neden:** Betiğin tamamlanması çok uzun sürdü

**Çözümler:**
- [ ] Eylem sayısını azaltın
- [ ] "Maksimum Adım" değerini artırın
- [ ] Daha hızlı yürütme için betiği optimize edin
- [ ] Çıkarmaya çalıştığınız şeyi basitleştirin

### "Element Not Found"
**Neden:** DocOperator belirttiğiniz düğmeyi/alanı bulamadı

**Çözümler:**
- [ ] Düğme/alan adının tam olarak doğru olduğunu doğrulayın
- [ ] Web sitesi düzeninin değişip değişmediğini kontrol edin
- [ ] Tıklamadan önce bekleme süresi ekleyin
- [ ] Düğmenin yalnızca belirli koşullarda görünüp görünmediğini kontrol edin

### "Login Failed"
**Neden:** Kimlik doğrulama başarısız

**Çözümler:**
- [ ] Kullanıcı adı/parolanın doğru olduğunu doğrulayın
- [ ] Parolanın özel karakterler içerip içermediğini kontrol edin
- [ ] Hesabın kilitli olmadığını doğrulayın
- [ ] Oturum açma sürecinin değişip değişmediğini kontrol edin

### "Data Not Extracted Correctly"
**Neden:** Betik çalıştı ama yanlış bilgi çıkardı

**Çözümler:**
- [ ] Doğru alanın seçildiğini doğrulayın
- [ ] Verinin beklenen konumda olup olmadığını kontrol edin
- [ ] Çıkarma mantığını manuel olarak test edin
- [ ] Sayfada ne olduğunu doğrulamak için hata ayıklama adımları ekleyin

### "Script Runs Slowly"
**Neden:** Çok fazla adım veya yavaş web sitesi

**Çözümler:**
- [ ] Gereksiz adımları kaldırın
- [ ] Bekleme sürelerini optimize edin
- [ ] İnternet bağlantısını kontrol edin
- [ ] API alternatifinin var olup olmadığını düşünün

---

## En İyi Uygulamalar

✅ **Yapın:**
- Dağıtmadan önce betikleri kapsamlı test edin
- Betikleri basit ve odaklı tutun
- Her adımı açıklayan yorumlar ekleyin
- Anlamlı değişken adları kullanın
- Betik performansını izleyin
- Betikler başarısız olduğunda yedek bulundurun

❌ **Yapmayın:**
- Aşırı uzun betikler oluşturma (>100 adım)
- Hassas parolaları günlüklere koyma
- Tam koordinatlara güvenme (web siteleri değişir)
- Çıkış koşulları olmadan döngüler oluşturma
- Hata mesajlarını görmezden gelme

---

## Performans İpuçları

- **Kullanılmayan adımları kaldırın** - Her adım zaman alır
- **Benzer eylemleri birleştirin** - İlgili tıklamaları gruplandırın
- **Beklemeleri optimize edin** - Yalnızca gerekli gecikmeleri kullanın
- **Veriyi önbelleğe alın** - Aynı veriyi iki kez çıkarmayın
- **Paralel işleme** - Mümkünse birden fazla betik çalıştırın

---

## Güvenlik Değerlendirmeleri

⚠️ **Önemli:**
- Parolaları DocFlow'da depolamayın
- Kimlik bilgilerini geçirmek için güvenli yöntemler kullanın
- Hassas veriyi günlüğe kaydetmeyin
- Neyin çıkarıldığını izleyin
- Bot etkinliğinin günlüğe kaydedildiğinden ve denetlenebilir olduğundan emin olun

---

## Değişkenler Örneği

### Kullanabileceğiniz Mevcut Değişkenler:
```
{invoice_number} - From document field
{supplier_code} - From document field
{product_id} - From document field
{quantity} - From document field
{currency} - From document field
```

### Değişkenleri Kullanan Betik:
```
1. Go to https://supplier.com/api/lookup
2. Enter supplier code: {supplier_code}
3. Search for product: {product_id}
4. Enter quantity: {quantity}
5. Extract price in currency: {currency}
6. Return extracted price
```

---

## Karşılaştırma: DocOperator vs API Ne Zaman Kullanılır

| Durum | DocOperator Kullan | API Kullan |
|-----------|-----------------|---------|
| Web sitesinin API'si var | ❌ Hayır | ✅ Evet |
| Web sitesi etkileşimli | ✅ Evet | ❌ Hayır |
| Oturum açma gerektiriyor | ✅ Evet | Değişir |
| Çok hızlı gerekiyor | ❌ Hayır | ✅ Evet |
| Karmaşık iş akışı | ✅ Evet | ❌ Belki değil |
| Veri günlük değişiyor | ✅ Evet | ✅ Evet |

---

## İlgili Kartlar

- **CALL_API** - Bunun yerine API kullanılabilir olduğunda kullan
- **ACTION_HTTPS_REQUEST** - Daha basit istekler
- **ACTION_SET_FIELD_TO_TEXT** - Çıkarılan veriyi kullan
- **CONDITION_HTTPS_REQUEST_STATUS** - İstek durumunu kontrol et

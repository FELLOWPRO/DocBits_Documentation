# Send HTTPS request to

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_1.png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"Send HTTPS Request"** iş akışı kartı, kullanıcıların özelleştirilebilir başlıklar, parametreler ve veri yüküyle belirtilen bir URL'ye HTTPS istekleri göndermesine olanak tanır. Bu kart, harici API'leri veya web servislerini doğrudan iş akışına entegre etmek için idealdir.

## Kartın Bileşenleri:

1. **URL**
   * **Açıklama:** HTTPS isteğinin gönderileceği uç noktayı belirtir.
   * **Ayrıntı:** Bağlanılacak API veya web servisinin tam URL'sini girin.
2. **Başlıklar (Headers)**
   * **Açıklama:** HTTPS isteğine dahil edilecek başlıkları tanımlar.
   * **Ayrıntı:** Kimlik doğrulama belirteçleri veya içerik türleri gibi başlıkları belirtmek için **geçerli bir JSON biçiminde** **anahtar-değer çiftleri** sağlayın. Örnek: {"Authorization": "Bearer example\_value"}
3. **Yöntem (Method)**
   * **Açıklama:** İstek için kullanılacak HTTP yöntemini belirtir.
   * **Seçenekler:**
     * **GET:** Uç noktadan veri alır.
     * **POST:** Kaynaklar oluşturmak veya güncellemek için uç noktaya veri gönderir.
     * **PUT:** Uç noktadaki mevcut kaynakları günceller.
     * **DELETE:** Uç noktadan kaynakları kaldırır.
4. **Parametreler**
   * **Açıklama:** URL'ye sorgu parametreleri olarak dahil edilecek anahtar-değer çiftleri.
   * **Ayrıntı:** Bunu, uç nokta tarafından gerekli olan filtreleri veya ek verileri geçerli bir JSON biçiminde göndermek için kullanın. Başlıklar için örneğe bakın.
5. **Veri**
   * **Açıklama:** HTTPS isteğinin gövdesi.
   * **Ayrıntı:** Veri yükünü geçerli bir JSON biçiminde sağlayın. Başlıklar için örneğe bakın.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Kart, HTTPS isteğini yalnızca **"Where"** ve **"And Bölümleri"** doğru olarak değerlendirilirse gönderir.&#x20;
  * Koşullardan biri yanlışsa, istek gönderilmez.
* **İstek Yürütme:**
  * Koşullar karşılandığında, sistem HTTPS isteğini belirtilen yapılandırmalarla gönderir.

## Kurulum ve Yapılandırma:

1. **URL'yi Tanımla:** HTTPS isteğinin gönderilmesi gereken uç noktayı girin.
2. **Başlıkları Ayarla:** Gerekli başlıkları anahtar-değer çiftleri olarak sağlayın.
3. **HTTP Yöntemini Seç:** Gerçekleştirilecek eyleme göre uygun yöntemi (**GET**, **POST**, **PUT** veya **DELETE**) seçin.
4. **Parametre Ekle:** Uç nokta tarafından gerekli olan sorgu parametrelerini belirtin.
5. **Veri Yükünü Sağla:** Gerekirse istek gövdesini gerekli biçimde (örn. JSON) girin.
6. **Koşulları Yapılandır:** İsteğin yalnızca belirli koşullar karşılandığında gönderilmesini sağlamak için **"Where"** ve **"And Bölümleri"**ni tanımlayın.

## Örnek Kart:

<figure><img src="../../../../.gitbook/assets/Then_Send_HTTPS_2.png" alt="" width="375"><figcaption></figcaption></figure>

## Sonuç:

**"Send HTTPS Request"** iş akışı kartı, kullanıcıların doğrudan iş akışlarından harici servislere özelleştirilmiş istekler yapmasına olanak tanıyarak API entegrasyonunu basitleştirir. HTTPS istekleri gönderme ve yanıtları yönetme sürecini otomatikleştirerek, bu kart iş akışı esnekliğini ve işlevselliğini artırır.

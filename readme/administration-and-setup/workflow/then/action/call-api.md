# Call Api

<figure><img src="../../../../.gitbook/assets/Then_Call_API.png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"Call API"** iş akışı kartı, kullanıcıların doğrudan iş akışından belirtilen API uç noktalarına HTTP istekleri yapmasına olanak tanır. Bu kart çeşitli HTTP yöntemlerini destekler ve parametreler ile veri göndererek harici sistemlerle dinamik etkileşimi mümkün kılar. Üçüncü taraf servisler ve özel API'lerle entegrasyonu kolaylaştırır ve sorunsuz iletişim sağlar.

## Kartın Bileşenleri:

1. **API Uç Noktası (API Endpoint)**
   * **Açıklama:** Bu kartın etkileşimde bulunacağı **DocBits API**'sinin hedef uç noktası.
   * **Ayrıntı:** Kullanıcıların API isteği için uç noktayı belirttiği bir metin alanı.
2. **HTTP Yöntemi**
   * **Açıklama:** Yapılacak HTTP isteğinin türü.
   * **Seçenekler:**
     1. **GET:** Belirtilen uç noktadan veri alır.
     2. **POST:** Uç noktaya veri gönderir.
     3. **PUT:** Uç noktadaki mevcut veriyi günceller.
     4. **DELETE:** Uç noktadaki veriyi kaldırır.
3. **Parametreler**
   * **Açıklama:** API isteğine dahil edilecek sorgu parametreleri.
   * **Ayrıntı:** İstek URL'si için anahtar-değer çiftleri girmek için bir metin alanı veya liste.
4. **Veri**
   1. **Açıklama:** API isteğinin gövdesinde gönderilecek veri yükü (POST ve PUT yöntemleri için geçerlidir).
   2. **Ayrıntı:** Veriyi JSON olarak girmek için bir alan.

## İşlevsellik:

**Koşul Değerlendirmesi:** Sistem, "Where" ve "And Bölümleri"nde tanımlanan koşulları değerlendirir:

* Her iki koşul da **doğru** ise, API isteği yapılandırıldığı şekilde yürütülür.
* Koşullardan biri **yanlış** ise, kart yürütülmez ve hiçbir API çağrısı yapılmaz.

**API İstek Yürütme:**

* Kart, seçilen yöntemi kullanarak HTTP isteğini belirtilen uç noktaya gönderir.
* Sağlanan herhangi bir parametre URL'ye eklenir ve veri istek gövdesine dahil edilir (varsa).

## Kurulum ve Yapılandırma:

1. **API Uç Noktasını Tanımla:**\
   Çağırmak istediğiniz API'nin URL'sini girin.
2. **HTTP Yöntemini Seç:**\
   API'nizin gereksinimlerine göre desteklenen yöntemlerden birini (GET, POST, PUT, DELETE) seçin.
3. **Parametreleri Sağla:**\
   Gerekli sorgu parametrelerini anahtar-değer çiftleri olarak ekleyin.
4. **Veriyi Dahil Et (varsa):**\
   POST veya PUT yöntemleri için, istek gövdesinde gönderilecek veriyi belirtin.
5. **Koşul Yapılandırması:**\
   API çağrısının ne zaman gerçekleşeceğini tanımlamak için "Where" ve "And Bölümleri"ni yapılandırın.

## Sonuç:

**"Call API"** iş akışı kartı, harici sistemlerle doğrudan etkileşimi mümkün kılarak iş akışı otomasyonunu geliştirir. Uç noktalar, yöntemler ve veriler için esnek yapılandırmalar sağlayarak, iş akışlarının üçüncü taraf API'lerle veya özel arka uçlarla sorunsuz entegre olmasını sağlar. API çağrılarını koşullu olarak yürütme yeteneği, harici iletişimleri otomatikleştirmede hassasiyet ve verimlilik sağlar.

***

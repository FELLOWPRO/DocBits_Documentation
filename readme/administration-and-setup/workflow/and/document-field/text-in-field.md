# Text in Field

<figure><img src="../../../../.gitbook/assets/image (10) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, belirtilen bir belge alanı içindeki belirli metnin varlığına veya yokluğuna göre eylemleri otomatikleştirmek için tasarlanmıştır. İş akışlarının belgelerin içeriğine dinamik olarak uyum sağlamasını sağlar, verimli işlemeyi ve doğru karar vermeyi destekler.

## **Kartın Bileşenleri:**

1. **Metin (Text)**
   * **Açıklama:** Alan içinde kontrol edilecek metin dizesini belirtir.
   * **Ayrıntı:** Bu, iş akışıyla ilgili bir kelime, ifade veya karakter dizisi olabilir.
2. **Operatör**
   * **Açıklama:** Alanda metin varlığı için koşulu tanımlar.
   * **Seçenekler:**
     * **Is:** Belirtilen metin alanda mevcutsa iş akışını tetikler.
     * **Is Not:** Belirtilen metin alanda mevcut değilse iş akışını tetikler.
3. **Alan Adı (Field Name)**
   * **Açıklama:** Değerlendirilecek belge alanının adını belirtir.
   * **Ayrıntı:** Bu, belge içindeki alanın tam tanımlayıcısıyla eşleşmelidir.

## **İşlevsellik:**

1. **Koşul Değerlendirmesi:** Sistem, seçilen operatöre (Is veya Is Not) dayanarak belirtilen metnin alanda var olup olmadığını kontrol eder.
2. **Eylem Yürütme:**
   * **Doğru Koşul:**\
     Alandaki metin varlığı belirtilen koşulla eşleşirse, sistem ilişkili eylemleri başlatır. Bunlar, uyarıları tetikleme, iş akışlarını ilerletme veya kayıtları güncellemeyi içerebilir.
   * **Yanlış Koşul:**\
     Alandaki metin varlığı koşulla eşleşmezse, iş akışı yapılandırmasına bağlı olarak alternatif eylemler veya hiçbir eylem gerçekleştirilebilir.

## **Kurulum ve Yapılandırma:**&#x20;

* Kullanıcı, kontrol edilecek metni girer. Ardından ilgili belgenin alan adını seçer.

## **Sonuç:**

"Text Presence in Field" iş akışı kartı, belge içerik analizi için basit ama güçlü bir araçtır. Metin algılamaya dayalı eylemleri otomatikleştirerek, bu kart daha akıllı iş akışlarını destekler, belge işleme doğruluğunu artırır ve manuel çabayı azaltır.

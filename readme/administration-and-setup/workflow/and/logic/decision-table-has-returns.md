# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, belirtilen bir karar tablosunun belirli bir belge için dönüş değerlerine sahip olup olmadığını kontrol eder ve döndürülen verinin sonraki iş akışı adımlarında kullanılıp kullanılmayacağını belirler. İş akışlarının karar tablosu sonuçlarına göre dinamik olarak uyum sağlamasını mümkün kılar.

## **İşlevsellik:**

* **Karar Tablosu Doğrulaması:** Bu kart, seçilen karar tablosunun işlenmekte olan belge için dönüş değerleri sağlayıp sağlamadığını doğrular.
* **Karar Tablosu Seçimi:** Kullanıcılar, kontrol edilecek karar tablosunun adını belirtir.
* **Dönüş Verisini Kullan:** Kullanıcılar, dönüş verisinin daha sonraki kartlarda kullanılıp kullanılmayacağını bir **Boolean** ayarıyla belirtebilir:
  * **True:** Dönüş verisi kullanılabilir ve sonraki iş akışı adımlarında kullanılacaktır.
  * **False:** Dönüş verisi kullanılmaz ve iş akışı onsuz devam eder.

## **Kullanım:**

Bu kart, bir karar tablosundaki önceden tanımlanmış kurallara dayalı koşullu mantık veya karar verme içeren iş akışları için idealdir. Karar tablosu çıktılarının iş akışı süreçlerine sorunsuz entegrasyonunu sağlar.

## **Örnek Senaryo:**

* Bir kullanıcı, dönüş değerleri için **"Invoice Processing Rules"** karar tablosunu kontrol etmek üzere kartı yapılandırır. **Boolean** değeri **True** olarak ayarlanır; bu, dönüş verisinin (örn. onay gereksinimleri) iş akışı kararlarına rehberlik etmek için daha sonraki kartlarda kullanılacağını gösterir.

"Decision Table Check" kartını kullanarak kuruluşlar, iş akışı esnekliğini artırabilir, kural tabanlı işlemeyi kolaylaştırabilir ve otomatik iş akışları arasında karar vermede tutarlılığı sağlayabilir.

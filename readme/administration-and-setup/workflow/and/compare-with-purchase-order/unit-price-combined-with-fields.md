# Unit Price Combined with Fields

<figure><img src="../../../../.gitbook/assets/image (26) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, birim fiyatın, belirtilen bir alan değeriyle (miktar, indirim veya ek ücretler gibi) birleştirildiğinde tanımlanmış bir koşulu karşılayıp karşılamadığını değerlendirmek için tasarlanmıştır. Kart, fiyatlandırmanın beklentilerle uyumlu olmasını sağlamaya yardımcı olmak için birim fiyatı ve alan değerini belirtilen bir eşikle karşılaştırır. Bu karşılaştırma, satınalma veya teslim alma iş akışlarında tutarsızlıkları işaretleme veya onay süreçlerini otomatikleştirme gibi belirli koşullara dayalı eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Birim fiyatla birleştirilecek değeri içeren belge alanını belirtir.
   * **Ayrıntı:** Bu, belge içindeki ilk alanın tam tanımlayıcısıyla eşleşmelidir.
2. **Operatör**
   * **Açıklama:** Birleşik değer ile belirtilen değer arasındaki karşılaştırmaya uygulanacak koşulu tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Birim fiyatın ve alanın birleşik değerinin belirtilen değerle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠):** Birim fiyatın ve alanın birleşik değerinin belirtilen değerden farklı olduğunu garanti eder.
     * **Büyüktür (>):** Birleşik değerin belirtilen değerden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥):** Birleşik değerin belirtilen değere eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<):** Birleşik değerin belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤):** Birleşik değerin belirtilen değere eşit veya ondan küçük olup olmadığını kontrol eder.
3. **Değer**
   * **Açıklama:** Birleşik birim fiyat ve alan değerinin karşılaştırılacağı değeri belirtir.
   * **Ayrıntı:** Değer sayısal bir değer olmalıdır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre dayanarak birleşik birim fiyatı ve alan değerini değerlendirir ve bunu belirtilen değerle karşılaştırır. Bu değerlendirmenin sonucu, koşulun doğru mu yoksa yanlış mı olduğunu belirler.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Karşılaştırma doğru sonuçlanırsa (örn. birleşik değer belirtilen değeri aşarsa), iş akışı doğru koşulla devam eder. Bu, onay, belge yönlendirme veya işleme kuralları uygulama gibi eylemleri tetikleyebilir.
  * **Yanlış Koşul:** Karşılaştırma yanlış sonuçlanırsa (örn. birleşik değer koşulu karşılamazsa), iş akışı yanlış koşulla devam eder. Bu, bir bildirim tetikleyebilir, belgeyi manuel inceleme için gönderebilir veya iş akışını durdurabilir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, birim fiyatla birleştirilecek değer(ler)i içeren belge alan(lar)ını seçerek başlar. Alanı seçtikten sonra, birleşik değerin belirtilen değere nasıl karşılaştırılacağını tanımlamak için uygun operatörü seçerler. Ardından değeri ayarlayabilirler.

## **Örnek Senaryo:**

* Bir fatura, bir ürünün her biri $20'dan 50 birimini listeler, toplam $1000. İlgili belgede 10 değerine sahip bir miktar alanı vardır. "Büyüktür" operatörünü kullanarak, kart birim fiyatın ($20) ve miktarın (10) birleşik değerini karşılaştırır, bu da $200'e eşittir. Kart, birleşik değerin $150'den (belirtilen değer) büyük olup olmadığını kontrol eder. $200'lik birleşik değer $150 eşiğinden büyük olduğundan, iş akışı belge için bir onay tetiklemeye devam eder.

## **Sonuç:**

"Unit Price Combined with Fields" iş akışı kartı, birim fiyatın ve belirtilen bir alanın birleşik değerini değerlendirerek fiyatlandırma koşullarının karşılanmasını sağlar. Bu karşılaştırmayı otomatikleştirerek, kuruluşlar tutarlılığı sağlayabilir ve onayla devam etmeden önce fiyatlandırma veya miktarlardaki tutarsızlıkları işaretleyebilir, bu da satınalma ve finansal süreçleri kolaylaştırmaya yardımcı olur.

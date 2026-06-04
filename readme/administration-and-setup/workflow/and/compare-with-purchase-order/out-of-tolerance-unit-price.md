# Out of Tolerance Unit Price

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, birim fiyatların ve belirtilen bir alanın birleşik değerinin tanımlanmış bir eşiği aşıp aşmadığını veya altında kalıp kalmadığını değerlendirmek için tasarlanmıştır. Birim fiyatların, diğer alanlarla birleştirildiğinde tolerans dışında olduğu herhangi bir tutarsızlığı belirlemeye yardımcı olur, fiyatlandırma koşullarının beklentileri karşılamasını sağlar ve herhangi bir sorunu inceleme veya başka eylem için işaretler.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name):**
   * **Açıklama**: Birim fiyatla birleştirilecek değeri içeren belge alanını belirtir.
   * **Ayrıntı**: Bu alandaki değer, karşılaştırma için toplam birleşik değeri oluşturmak üzere birim fiyatla birleştirilecektir.
2. **Operatör:**
   * **Açıklama**: Birim fiyatın ve alan değerinin birleşik değerini belirtilen değere karşı karşılaştırma koşulunu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerden farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değeri aşıp aşmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değere eşit veya ondan büyük olup olmadığını doğrular.
     * **Küçüktür (<)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değere eşit veya ondan küçük olup olmadığını doğrular.
3. **Değer:**
   * **Açıklama**: Birleşik birim fiyat ve alan değerinin karşılaştırılacağı değeri belirtir.
   * **Ayrıntı**: Bu sayısal değer, karşılaştırma için eşiği temsil eder. Birim fiyat ve alanın birleşik değeri bu değeri aşarsa veya altında kalırsa (seçilen operatöre göre), koşul belirtilen eylemleri tetikler.

## **İşlevsellik:**

* &#x20;**Koşul Değerlendirmesi:** Sistem, yapılandırmaya bağlı olarak birim fiyatı alan değeriyle çarparak veya toplayarak birleşik değeri hesaplar. Sonuç daha sonra seçilen operatör kullanılarak belirtilen değerle karşılaştırılır. Koşul karşılanırsa (yani birleşik değer tolerans dışındaysa), iş akışı onay, reddetme veya daha fazla inceleme olsun, bir sonraki adımla devam eder.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Karşılaştırma doğru sonuçlanırsa (yani birleşik değer koşulu karşılarsa), iş akışı doğru koşulla ilişkili eylemi tetikler (örn. onay veya bildirim).
  * **Yanlış Koşul**: Karşılaştırma yanlış sonuçlanırsa (yani birleşik değer koşulu karşılamazsa), iş akışı ilerlemez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, birim fiyatla birleştirilecek değeri içeren alanı seçer. Ardından, birleşik değerin belirtilen değere nasıl karşılaştırılacağını belirlemek için uygun operatörü seçerler. Son olarak, kullanıcı birleşik fiyatın karşılaştırılacağı değeri ayarlar.

## **Örnek Senaryo:**

* Bir fatura, bir ürünün her biri $30'dan 50 birimini listeler, toplam $1500. İlgili belgede 10 değerine sahip bir miktar alanı vardır. Birleşik fiyat, birim fiyatı ($30) ve miktarı (10) çarparak hesaplanır, sonuç $300 olur. Kart daha sonra bu birleşik değeri $250 eşiğiyle karşılaştırır. "Büyüktür" operatörünü kullanarak, kart $300'ün $250'den büyük olduğunu tanımlar ve belge için bir onay süreci tetikler.

## **Sonuç:**

"Out of Tolerance Unit Prices Combined with Fields" iş akışı kartı, fiyatlandırma ve alan değerlerinin iş kurallarıyla uyumlu olmasını sağlamaya yardımcı olur. Bu kontrolü otomatikleştirerek, kuruluşlar süreçte erken tutarsızlıkları belirleyebilir ve tolerans dışındaki herhangi bir birim fiyatın inceleme veya gerekli eylem için işaretlenmesini sağlayabilir.

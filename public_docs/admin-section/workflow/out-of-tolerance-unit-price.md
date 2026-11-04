# Tolerans Dışı Birim Fiyat

<figure><img src="../../../../.gitbook/assets/image (272).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, birim fiyatların ve belirtilen bir alanın birleşik değerinin tanımlanmış bir eşiği aşıp aşmadığını veya altında kalıp kalmadığını değerlendirmek için tasarlanmıştır. Birim fiyatların, diğer alanlarla birleştirildiğinde tolerans dışında olduğu tutarsızlıkları belirlemeye yardımcı olur, fiyatlandırma koşullarının beklentileri karşılamasını sağlar ve inceleme veya daha fazla eylem için sorunları işaretler.

## **Kartın Bileşenleri:**

1. **Alan Adı:**
   * **Açıklama**: Birim fiyatla birleştirilecek değeri içeren belge alanını belirtir.
   * **Detay**: Bu alandaki değer, karşılaştırma için toplam birleşik değeri oluşturmak üzere birim fiyatla birleştirilecektir.
2. **Operatör:**
   * **Açıklama**: Birim fiyatın ve alan değerinin birleşik değerini belirtilen değerle karşılaştırma koşulunu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerden farklı olmasını sağlar.
     * **Büyüktür (>)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değeri aşıp aşmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değere eşit veya ondan büyük olup olmadığını doğrular.
     * **Küçüktür (<)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birim fiyatın ve alanın birleşik değerinin belirtilen değere eşit veya ondan küçük olup olmadığını doğrular.
3. **Değer:**
   * **Açıklama**: Birleşik birim fiyat ve alan değerinin karşılaştırılacağı değeri belirtir.
   * **Detay**: Bu sayısal değer, karşılaştırma için eşiği temsil eder. Birim fiyatın ve alanın birleşik değeri bu değeri aşarsa veya altında kalırsa (seçilen operatöre göre), koşul belirtilen eylemleri tetikleyecektir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, yapılandırmaya bağlı olarak birim fiyatı alan değeriyle çarparak veya toplayarak birleşik değeri hesaplar. Sonuç daha sonra seçilen operatör kullanılarak belirtilen değerle karşılaştırılır. Koşul karşılanırsa (yani birleşik değer tolerans dışındaysa), iş akışı onay, reddetme veya daha fazla inceleme olsun bir sonraki adımla devam eder.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Karşılaştırma doğru sonuçlanırsa (yani birleşik değer koşulu karşılıyorsa), iş akışı doğru koşulla ilişkili eylemi (örneğin onay veya bildirim) tetikler.
  * **Yanlış Koşul**: Karşılaştırma yanlış sonuçlanırsa (yani birleşik değer koşulu karşılamıyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar birim fiyatla birleştirilecek değeri içeren alanı seçer. Ardından, birleşik değerin belirtilen değerle nasıl karşılaştırılacağını belirlemek için uygun operatörü seçerler. Son olarak kullanıcı, birleşik fiyatın karşılaştırılacağı değeri ayarlar.

## **Örnek Senaryo:**

* Bir fatura, her biri 30$ olan bir üründen 50 birim listeliyor ve toplam 1500$. İlgili belgede değeri 10 olan bir miktar alanı vardır. Birleşik fiyat, birim fiyat (30$) ve miktarın (10) çarpılmasıyla hesaplanır ve sonuç 300$ olur. Kart daha sonra bu birleşik değeri 250$ eşiğiyle karşılaştırır. “Büyüktür” operatörünü kullanan kart, 300$'ın 250$'dan büyük olduğunu tanımlar ve belge için bir onay sürecini tetikler.

## **Sonuç:**

"Alanlarla Birleştirilen Tolerans Dışı Birim Fiyatlar" iş akışı kartı, fiyatlandırma ve alan değerlerinin iş kurallarıyla uyumlu olmasını sağlamaya yardımcı olur. Bu kontrolü otomatikleştirerek kuruluşlar, tutarsızlıkları sürecin başlarında tanımlayabilir ve tolerans dışı birim fiyatların inceleme veya gerekli eylem için işaretlenmesini sağlayabilir.

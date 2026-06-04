# Compare Total Charges

<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belge alanındaki toplam ücretleri bir satınalma siparişindeki karşılık gelen ücretlerle karşılaştırır. Kart, belgedeki ücretlerin, belirtilen tolerans seviyelerini dikkate alarak satınalma siparişindekilerle uyumlu olmasını sağlamaya yardımcı olur. Tutarsızlıklar bulunursa karşılaştırma, tutarsızlıkları inceleme için işaretleme veya ücretleri buna göre ayarlama gibi eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name):**
   * **Açıklama**: Satınalma siparişindeki ücretlerle karşılaştırılacak toplam ücret değerlerini içeren belge alanını belirtir.
   * **Ayrıntı**: Bu alandaki değer, belgede (örn. fatura) uygulanan toplam ücretleri temsil eder ve satınalma siparişi ücretiyle karşılaştırılır.
2. **Operatör:**
   * **Açıklama**: Belgedeki toplam ücret ile satınalma siparişindeki ücret arasındaki karşılaştırmaya uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Belgedeki toplam ücretin satınalma siparişindeki ücretle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Belgedeki toplam ücretin satınalma siparişindeki ücretten farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Belgedeki toplam ücretin satınalma siparişindeki ücretten büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Belgedeki toplam ücretin satınalma siparişindeki ücrete eşit veya ondan büyük olup olmadığını doğrular.
     * **Küçüktür (<)**: Belgedeki toplam ücretin satınalma siparişindeki ücretten küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Belgedeki toplam ücretin satınalma siparişindeki ücrete eşit veya ondan küçük olup olmadığını doğrular.
3. **Tolerans Miktarı**
   * **Açıklama**: Toplam ücretleri karşılaştırmak için tolerans eşiğini belirtir.
   * **Ayrıntı**: Bu sayısal değer, belge ile satınalma siparişi arasındaki ücretlerde izin verilen sapmayı temsil eder.
4. **Tolerans Türü:**
   * **Açıklama**: Uygulanacak tolerans türünü belirtir.
   * **Seçenekler**:
     * **Yüzde**: Tolerans, satınalma siparişi ücretinin bir yüzdesi olarak uygulanır.
     * **Değer**: Tolerans, sabit bir sayısal tutar olarak uygulanır.
5. **Ayırıcı (Separator):**
   * **Açıklama**: Alan adının sonundaki Ücret Kimliğini ayırt etmek için kullanılan ayırıcıyı belirtir.
   * **Ayrıntı**: Ayırıcı, ücret alanını, belge ücretini satınalma siparişindeki karşılık gelen ücrete bağlamak için kullanılacak benzersiz Ücret Kimliğinden ayırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, operatöre ve toleransa dayanarak belge alanındaki toplam ücreti satınalma siparişindeki karşılık gelen ücretle karşılaştırır. Tolerans, iki ücret arasındaki farkın kabul edilebilir bir aralıkta olup olmadığını belirlemek için uygulanır.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Ücretler eşleşirse (tolerans dikkate alındığında) ve koşul doğruysa, iş akışı belge onayı veya daha fazla işleme gibi tanımlanan eylemle devam eder.
  * **Yanlış Koşul**: Koşul yanlışsa (yani ücretler tolerans içinde eşleşmezse), iş akışı devam etmez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, toplam ücret değerini içeren belge alanını seçerek başlar. Ardından, ücretin satınalma siparişi ücretiyle nasıl karşılaştırılacağını tanımlamak için operatörü seçerler. Sonra, kullanıcılar tolerans miktarını ve tolerans türünü (yüzde veya mutlak) ayarlar. Son olarak, karşılaştırma için kullanılacak ayırıcıyı ve Ücret Kimliğini belirtirler.

## **Örnek Senaryo:**

Bir fatura, "toplam ücretler" alanında $500'lik bir ücret listeler. Karşılık gelen satınalma siparişi ücreti $480'dir ve tolerans $20 (mutlak tolerans) olarak ayarlanmıştır. Kart, belge ücretini satınalma siparişi ücretine karşı karşılaştırır:

* Belgedeki toplam ücret satınalma siparişinin $20 toleransı içindedir ve iş akışı sorunsuz devam eder.
* Ücret toleransı aşarsa, iş akışı tutarsızlığı inceleme için işaretler.

## **Sonuç:**

"Compare Total Charges" iş akışı kartı, belirtilen tolerans seviyelerini dikkate alarak belgelerdeki ücretlerin satınalma siparişlerindekilerle uyumlu olmasını sağlar. Bu, kuruluşların doğrulama sürecini otomatikleştirmesine, tutarsızlıkları erken tanımlamasına ve ücretle ilgili süreçler üzerinde daha iyi kontrol sağlamasına yardımcı olur.

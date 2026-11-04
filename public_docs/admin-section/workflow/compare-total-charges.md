<figure><img src="../../../../.gitbook/assets/image (271).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belge alanındaki toplam ücretleri satın alma siparişindeki karşılık gelen ücretlerle karşılaştırır. Kart, belirtilen tolerans seviyelerini dikkate alarak belgedeki ücretlerin satın alma siparişindekilerle uyumlu olmasını sağlamaya yardımcı olur. Karşılaştırma, inceleme için tutarsızlıkları işaretlemek veya ücretleri buna göre ayarlamak gibi tutarsızlıklar bulunursa eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Alan Adı:**
   * **Açıklama**: Satın alma siparişindeki ücretlerle karşılaştırılacak toplam ücret değerlerini içeren belge alanını belirtir.
   * **Detay**: Bu alandaki değer, belgede (örneğin fatura) uygulanan toplam ücretleri temsil eder ve satın alma siparişi ücretiyle karşılaştırılacaktır.
2. **Operatör:**
   * **Açıklama**: Belgedeki toplam ücret ile satın alma siparişindeki ücret arasındaki karşılaştırmaya uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Belgedeki toplam ücretin satın alma siparişindeki ücretle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Belgedeki toplam ücretin satın alma siparişindeki ücretten farklı olmasını sağlar.
     * **Büyüktür (>)**: Belgedeki toplam ücretin satın alma siparişindeki ücretten büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Belgedeki toplam ücretin satın alma siparişindeki ücretten büyük veya ona eşit olup olmadığını doğrular.
     * **Küçüktür (<)**: Belgedeki toplam ücretin satın alma siparişindeki ücretten küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Belgedeki toplam ücretin satın alma siparişindeki ücretten küçük veya ona eşit olup olmadığını doğrular.
3. **Tolerans Tutarı**
   * **Açıklama**: Toplam ücretleri karşılaştırmak için tolerans eşiğini belirtir.
   * **Detay**: Bu sayısal değer, belge ile satın alma siparişi arasında ücretlerde izin verilen varyansı temsil eder.
4. **Tolerans Türü:**
   * **Açıklama**: Uygulanacak tolerans türünü belirtir.
   * **Seçenekler**:
     * **Yüzde**: Tolerans, satın alma siparişi ücretinin yüzdesi olarak uygulanır.
     * **Değer**: Tolerans, sabit bir sayısal tutar olarak uygulanır.
5. **Ayırıcı:**
   * **Açıklama**: Alan adının sonundaki Ücret Kimliğini (Charge ID) ayırt etmek için kullanılan ayırıcıyı belirtir.
   * **Detay**: Ayırıcı, ücret alanını, belge ücretini satın alma siparişindeki karşılık gelen ücrete bağlamak için kullanılacak benzersiz Ücret Kimliğinden ayırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, operatöre ve toleransa bağlı olarak belge alanındaki toplam ücreti satın alma siparişindeki karşılık gelen ücretle karşılaştırır. İki ücret arasındaki farkın kabul edilebilir bir aralıkta olup olmadığını belirlemek için tolerans uygulanır.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Ücretler eşleşirse (tolerans dikkate alınarak) ve koşul doğruysa, iş akışı belge onayı veya daha fazla işleme gibi tanımlanan eylemle devam edecektir.
  * **Yanlış Koşul**: Koşul yanlışsa (yani ücretler tolerans dahilinde eşleşmiyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, toplam ücret değerini içeren belge alanını seçerek başlar. Ardından, ücretin satın alma siparişi ücretiyle nasıl karşılaştırılacağını tanımlamak için operatörü seçerler. Daha sonra kullanıcılar tolerans tutarını ve tolerans türünü (yüzde veya mutlak) ayarlar. Son olarak, karşılaştırma için kullanılacak ayırıcıyı ve Ücret Kimliğini belirtirler.

## **Örnek Senaryo:**

Bir fatura, "toplam ücretler" alanında 500$ tutarında bir ücret listeliyor. Karşılık gelen satın alma siparişi ücreti 480$ ve tolerans 20$ (mutlak tolerans) olarak ayarlanmıştır. Kart, belge ücretini satın alma siparişi ücretine karşı karşılaştırır:

* Belgedeki toplam ücret, satın alma siparişinin 20$ toleransı içindedir ve iş akışı sorunsuz bir şekilde devam eder.
* Ücret toleransı aşarsa, iş akışı tutarsızlığı inceleme için işaretler.

## **Sonuç:**

"Toplam Ücretleri Karşılaştır" iş akışı kartı, belgelerdeki ücretlerin belirtilen tolerans seviyelerini dikkate alarak satın alma siparişlerindekilerle uyumlu olmasını sağlar. Bu, kuruluşların doğrulama sürecini otomatikleştirmesine, tutarsızlıkları erken tanımlamasına ve ücretle ilgili süreçler üzerinde daha iyi kontrol sağlamasına yardımcı olur.

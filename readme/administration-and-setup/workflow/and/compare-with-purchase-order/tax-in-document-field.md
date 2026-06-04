# Tax in document field

<figure><img src="../../../../.gitbook/assets/image (268).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, ücret kimliğine dayalı toleransları dikkate alarak bir belge alanındaki vergi değerinin bir satınalma siparişindeki vergi değeriyle eşleşip eşleşmediğini değerlendirmek için tasarlanmıştır. Kart, bu iki vergi değerini (biri belge alanından, biri satınalma siparişinden) karşılaştırır ve belirtilen bir koşulu (örn. eşittir, büyüktür, küçüktür vb.) karşılayıp karşılamadığını kontrol eder. Bu, vergi değerlerinin tutarlı olmasını sağlamaya ve satınalma iş akışlarında daha fazla inceleme veya onay için tutarsızlıkları işaretlemeye yardımcı olur.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama**: Satınalma siparişindeki vergi değeriyle karşılaştırılacak vergi değerini içeren belge alanını belirtir.
   * **Ayrıntı**: Bu alan, belgedeki vergi değeri için tam tanımlayıcıyla eşleşmelidir.
2. **Operatör**
   * **Açıklama**: Belgenin vergi değeri ile satınalma siparişinin vergi değeri arasındaki karşılaştırmaya uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Belge alanındaki verginin satınalma siparişindeki vergiyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Belge alanındaki verginin satınalma siparişindeki vergiyle eşleşmediğini garanti eder.
     * **Büyüktür (>)**: Belge alanındaki verginin satınalma siparişindeki vergiden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Belge alanındaki verginin satınalma siparişindeki vergiye eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<)**: Belge alanındaki verginin satınalma siparişindeki vergiden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Belge alanındaki verginin satınalma siparişindeki vergiye eşit veya ondan küçük olup olmadığını kontrol eder.
3. **Ana Veri Tablosu (Master Data Table)**
   * **Açıklama**: Ücret kimliği ve vergi değerleri dahil satınalma siparişi ayrıntılarını içeren tablo.
   * **Ayrıntı**: Bu tablo, satınalma siparişi vergi değeriyle ilişkili ücret kimliğine bir referansa sahip olmalıdır.
4. **Tolerans Miktarı**
   * **Açıklama**: Vergi değerlerinin değişebileceği eşik miktarı. Bu, vergi hesaplamalarındaki küçük tutarsızlıkları hesaba katmak için kullanılır.
   * **Ayrıntı**: Tolerans miktarı, vergi değerleri arasındaki izin verilen maksimum farkı tanımlayan sayısal bir değer olmalıdır.
5. **Tolerans Türü**
   * **Açıklama**: Uygulanan tolerans türünü, mutlak veya yüzde tabanlı olarak belirtir.
   * **Seçenekler**:
     * **Değer**: Tolerans sabit bir sayısal değerdir.
     * **Yüzde**: Tolerans, vergi değerinin bir yüzdesi olarak hesaplanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, belge alanındaki vergi değerinin, satınalma siparişindeki vergi değeriyle (ana veri tablosundan ücret kimliği referansıyla) karşılaştırıldığında belirtilen koşulu karşılayıp karşılamadığını değerlendirir. Vergi hesaplamalarındaki küçük farklara izin vermek için bu değerlendirmede tolerans miktarı ve türü dikkate alınır.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Belge alanındaki vergi, satınalma siparişinin vergisiyle karşılaştırıldığında koşulu karşılarsa (tolerans miktarı ve türü içinde), iş akışı devam eder.
  * **Yanlış Koşul**: Belge alanındaki vergi koşulu karşılamazsa (tolerans aralığı içinde değilse veya karşılaştırma başarısız olursa), iş akışı durur.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, karşılaştırılacak vergi değerini içeren belge alanını seçmelidir. Ardından, karşılaştırmanın nasıl yapılması gerektiği için operatörü (örn. eşittir, büyüktür) seçerler. Bunu takiben, kullanıcıların ana veri tablosu referansını belirtmesi ve küçük vergi tutarsızlıklarını hesaba katmak için tolerans miktarını ve türünü ayarlaması gerekir.

## **Örnek Senaryo:**

* Bir fatura $100'lik bir vergi tutarı listeler. Ana veri tablosunda bulunan karşılık gelen satınalma siparişi $95 vergi değeri belirtir. "Büyüktür" operatörünü kullanarak, sistem belgenin vergi değerini ($100) satınalma siparişi vergi değeriyle ($95) $10 tolerans (mutlak tolerans türü) ile karşılaştırır. $5'lik fark tolerans aralığında olduğundan, iş akışı herhangi bir uyarı tetiklemeden ilerler.

## **Sonuç:**

"Tax in Document Field Comparison" iş akışı kartı, belgelerdeki vergi değerlerinin satınalma siparişi ayrıntılarıyla uyumlu olmasını sağlar ve belirtilen toleranslara dayalı küçük tutarsızlıklara izin verir. Bu kontrolü otomatikleştirerek, kuruluşlar vergi hesaplamalarındaki hataları en aza indirebilir ve satınalma süreçlerini kolaylaştırabilir, manuel müdahale veya onaylara olan ihtiyacı azaltabilir.

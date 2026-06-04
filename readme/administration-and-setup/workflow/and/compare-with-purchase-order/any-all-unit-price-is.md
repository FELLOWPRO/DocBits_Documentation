# Any / All Unit Price is

<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belgedeki birim fiyatı bir satınalma siparişindeki birim fiyatla karşılaştırmak ve fiyatların tanımlanan tolerans seviyeleri içinde uyumlu olmasını sağlamak için kullanılır. Birim fiyat beklentileri karşılamazsa karşılaştırma eylemleri tetikleyebilir. **Sürüm 4**, kullanıcıların karşılaştırma için farklı varlıklar seçmesine olanak tanıyarak daha fazla esneklik ekler ve fiyatlandırma ve satınalma süreçleri üzerinde daha derin bir kontrol düzeyi sağlar.

## **Kartın Bileşenleri:**

1. **Any / All:**
   * **Açıklama**: Koşulun birim fiyatın karşılaştırıldığı herhangi bir veya tüm örneklere uygulanıp uygulanmayacağını tanımlar.
   * **Seçenekler**:
     * **Any**: Herhangi bir birim fiyat belirtilen karşılaştırma koşulunu karşılarsa koşul karşılanır.
     * **All**: Yalnızca tüm birim fiyatlar belirtilen karşılaştırma koşulunu karşılarsa koşul karşılanır.
2. **Operatör:**
   * **Açıklama**: Birim fiyatı belirtilen değere karşı karşılaştırma koşulunu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Birim fiyatın belirtilen değerle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Birim fiyatın belirtilen değerden farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Birim fiyatın belirtilen değerden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birim fiyatın belirtilen değere eşit veya ondan büyük olup olmadığını doğrular.
     * **Küçüktür (<)**: Birim fiyatın belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birim fiyatın belirtilen değere eşit veya ondan küçük olup olmadığını doğrular.

## **Sürüm 4'teki Ek Bileşenler:**

**Karşılaştırma Türü:**

* **Açıklama**: Kullanıcıların birim fiyata ek olarak hangi varlıkların karşılaştırılacağını seçmesine olanak tanır.
* **Seçenekler**:
  * **Satınalma Siparişinden Belgeye**: Satınalma siparişindeki birim fiyatı belgedeki birim fiyatla karşılaştırır.
  * **Teslim Alınandan Belgeye**: Teslim alınan miktarı belgedeki birim fiyatla karşılaştırır.
  * **Satınalma Siparişinden Teslim Alınana**: Satınalma siparişindeki birim fiyatı teslim alınan miktarla karşılaştırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre dayanarak belgedeki birim fiyatı satınalma siparişindeki birim fiyatla (veya Sürüm 4'te diğer seçili varlıkla) karşılaştırır. Karşılaştırma doğruysa, iş akışı sonraki adımlara göre devam eder ve ya onayı tetikler ya da süreci durdurur.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örn. belgedeki birim fiyat belirtilen değerden büyükse), iş akışı doğru eylemiyle devam eder (örn. onay, belge işleme).
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örn. belgedeki birim fiyat karşılaştırmayı karşılamazsa), iş akışı ilerlemez.

## **Kurulum ve Yapılandırma:**

* **Sürüm 3 Kurulumu:** Kullanıcılar, belgedeki birim fiyatı seçerek, birim fiyatın belirtilen değere nasıl karşılaştırılacağını tanımlamak için uygun operatörü seçerek ve karşılaştırılacak değeri ayarlayarak kartı yapılandırır. Ayrıca, kullanıcılar koşulun birim fiyat karşılaştırmasının herhangi bir veya tüm örneklerine uygulanıp uygulanmayacağını seçer.
* **Sürüm 4 Kurulumu:** Sürüm 4'te, kullanıcılar Karşılaştırma Türünü seçme ek seçeneğine sahiptir. Bu, Satınalma Siparişinden Belgeye, Teslim Alınandan Belgeye veya Satınalma Siparişinden Teslim Alınana gibi karşılaştırılacak varlıkları tanımlamalarına olanak tanır. Bu, kartın daha karmaşık senaryolarda birim fiyatları karşılaştırma esnekliğini artırır.

## **Örnek Senaryo:**

*   **Sürüm 3 Örneği:**&#x20;

    Bir fatura $50 birim fiyat gösterir. İlgili satınalma siparişinde $45 birim fiyat vardır. Kart, "Büyüktür" operatörünü kullanarak iki birim fiyatı karşılaştırır. Belgedeki birim fiyat ($50) satınalma siparişindeki birim fiyattan ($45) büyük olduğundan, iş akışı doğru koşulu tetikler (örn. belgeyi inceleme için gönder).
* **Sürüm 4 Örneği:**\
  Bir fatura $50 birim fiyat gösterir ve ilgili satınalma siparişi $45 birim fiyata yetki vermiştir. Ayrıca, teslim alınan miktar 60 birimdir. Kart, "Büyüktür" operatörünü kullanarak teslim alınan miktarı belgenin birim fiyatıyla karşılaştırır. Teslim alınan miktar (60) birim fiyattan ($50) büyük olduğundan, iş akışı doğru koşulu tetikler ve belge daha fazla inceleme için işaretlenir.

## **Sonuç:**

"Unit Price Comparison" iş akışı kartının Sürüm 3'ü, belgelerdeki birim fiyatların satınalma siparişlerindekilerle uyumlu olmasını sağlamak ve tanımlanan koşullara dayalı eylemleri tetiklemek için tasarlanmıştır. Sürüm 4, satınalma siparişlerini belgelerle, teslim alınan miktarları belgelerle ve satınalma siparişlerini teslim alınan miktarlarla karşılaştırma gibi daha karmaşık karşılaştırma seçenekleri sunarak bu işlevselliği genişletir. Bu eklenen esneklik, kuruluşların daha sofistike fiyatlandırma ve satınalma senaryolarını ele almasına olanak tanır ve iş akışlarında kontrolü ve doğruluğu artırır.

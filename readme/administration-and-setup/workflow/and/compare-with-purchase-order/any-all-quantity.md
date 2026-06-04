# Any / All Quantity

<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belgedeki miktarı satınalma siparişinde tanımlanan toleransa karşı karşılaştırmak için tasarlanmıştır. Kullanıcıların miktarın belirli koşulları karşılayıp karşılamadığını (örneğin eşitlik veya belirtilen toleransı aşma) değerlendirmesine olanak tanır. Sürüm 4'te, kart satınalma siparişi, teslim alınan miktarlar ve belge miktarları dahil olmak üzere birden fazla varlığı karşılaştırma özelliğini ekleyerek işlevselliği genişletir ve farklı senaryoları ele almada daha fazla esneklik sunar.

## **Kartın Bileşenleri:**

1. **Any / All:**
   * **Açıklama**: Karşılaştırmanın birden fazla öğe veya koşula nasıl uygulanacağını belirtir.
   * **Seçenekler**:
     * **Any**: Eylemin tetiklenmesi için koşullardan en az birinin doğru olması gerekir.
     * **All**: Eylemin devam etmesi için tüm koşulların doğru olması gerekir.
2. **Operatör:**
   * **Açıklama**: Belge miktarını belirtilen toleransa karşı karşılaştırmak için uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Miktarın belirtilen tolerans değeriyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Miktarın belirtilen tolerans değerinden farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Miktarın belirtilen toleranstan büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Miktarın belirtilen toleransa eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<)**: Miktarın belirtilen toleranstan küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Miktarın belirtilen toleransa eşit veya ondan küçük olup olmadığını kontrol eder.
3. **Tolerans Miktarı:**
   * **Açıklama**: Belge miktarının karşılaştırılacağı tolerans değerini belirtir.
   * **Ayrıntı**: Bu değer sayısaldır ve miktarda izin verilen sapmanın eşiğini temsil eder.
4. **Tolerans Türü:**
   * **Açıklama**: Uygulanacak tolerans türünü tanımlar.
   * **Seçenekler**:
     * **Yüzde**: Tolerans, satınalma siparişi miktarının bir yüzdesi olarak hesaplanır.
     * **Değer**: Tolerans, sabit bir sayısal değer olarak belirtilir.

## **Sürüm 4'teki Ek Bileşenler:**

* **Karşılaştırma Türü**: Karşılaştırılacak varlıkları seçer ve Sürüm 4'te miktarların nasıl değerlendirileceği konusunda daha fazla esneklik sağlar.
  * **Satınalma Siparişinden Belgeye**: Satınalma siparişindeki miktarı ilgili belgedeki miktarla karşılaştırır.
  * **Teslim Alınandan Belgeye**: Teslim alınan miktarı belgedeki miktarla karşılaştırır.
  * **Satınalma Siparişinden Teslim Alınana**: Satınalma siparişi miktarını teslim alınan miktarla karşılaştırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatör ve tolerans miktarı/türüne dayanarak belgedeki miktarı satınalma siparişindeki toleransa karşı karşılaştırır. Sürüm 4'te, **Karşılaştırma Türü**, satınalma siparişinden teslim alınana veya satınalma siparişinden belgeye gibi farklı miktarların karşılaştırılmasına olanak tanır ve daha dinamik bir karşılaştırma sağlar.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Karşılaştırma doğru sonuçlanırsa (örn. belge miktarı kabul edilebilir tolerans aralığında ise), iş akışı ilerler.
  * **Yanlış Koşul**: Karşılaştırma yanlış sonuçlanırsa (örn. miktar toleransı karşılamazsa), iş akışı ilerlemez.

## **Kurulum ve Yapılandırma:**

**Sürüm 3:**

* Kullanıcılar, belge miktarını seçerek, tolerans miktarını ve tolerans türünü tanımlayarak ve miktarı toleransa karşı karşılaştırmak için uygun operatörü seçerek kartı yapılandırır. Kart, miktarın tolerans eşiği içinde olup olmadığını değerlendirir ve sonuca göre "Doğru" veya "Yanlış" eylemiyle devam eder.

**Sürüm 4:**

* Sürüm 3'teki yapılandırmaya ek olarak, kullanıcılar aşağıdaki gibi farklı varlıklar arasında karşılaştırma yapmaya olanak tanıyan **Karşılaştırma Türü**'nü seçebilir:
  * **Satınalma Siparişinden Belgeye**
  * **Teslim Alınandan Belgeye**
  * **Satınalma Siparişinden Teslim Alınana**

## **Örnek Senaryo:**

Bir fatura 100 birimin teslim edildiğini gösterir, ancak satınalma siparişi yalnızca 90 birime yetki vermiştir. Tolerans miktarı 10 birim olarak ayarlanmıştır ve tolerans türü mutlaktır.

* **Sürüm 3**: Kart, belgedeki 100 birimi satınalma siparişinin 90 birim toleransına karşı karşılaştırır. Miktar toleransı aşarsa, kart daha fazla inceleme için tutarsızlığı işaretler.
* **Sürüm 4**: Kart, **satınalma siparişi miktarını** (90 birim) **teslim alınan miktarla** (100 birim) veya **belge miktarıyla** (100 birim) karşılaştırabilir. Seçilen **Karşılaştırma Türü**'ne bağlı olarak, iki varlık arasındaki farkın toleransı aşıp aşmadığını kontrol eder ve karşılık gelen eylemi tetikler.

## **Sonuç:**

* **Sürüm 3**: Bu iş akışı kartı, belge miktarını satınalma siparişi toleransıyla karşılaştırır ve miktardaki tutarsızlıkların işaretlenmesini ve uygun şekilde ele alınmasını sağlar.
* **Sürüm 4**: Kullanıcıların satınalma siparişinden teslim alınana veya satınalma siparişinden belgeye gibi farklı varlıkları karşılaştırmasına olanak tanıyarak bu işlevselliği genişletir ve daha karmaşık senaryoları ele almada daha fazla esneklik sağlar. Sürüm 4, satınalma ve teslim alma iş akışları üzerinde daha sıkı kontrol sağlar ve seçilen karşılaştırma türüne dayalı daha dinamik karşılaştırmalar ve eylemler sunar.

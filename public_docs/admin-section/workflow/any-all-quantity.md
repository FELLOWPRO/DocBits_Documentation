<figure><img src="../../../../.gitbook/assets/image (269).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (270).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belgedeki miktarı satın alma siparişinde tanımlanan toleransla karşılaştırmak için tasarlanmıştır. Kullanıcıların miktarın eşitlik veya belirtilen toleransı aşma gibi belirli koşulları karşılayıp karşılamadığını değerlendirmesine olanak tanır. Sürüm 4'te kart, satın alma siparişi, alınan miktarlar ve belge miktarları dahil olmak üzere birden fazla öğeyi karşılaştırma yeteneği ekleyerek işlevselliği genişletir ve farklı senaryoları ele almada daha fazla esneklik sunar.

## **Kartın Bileşenleri:**

1. **Herhangi biri / Tümü (Any / All):**
   * **Açıklama**: Karşılaştırmanın birden fazla öğe veya koşul arasında nasıl uygulanacağını belirtir.
   * **Seçenekler**:
     * **Herhangi biri (Any)**: Eylemin tetiklenmesi için koşullardan en az birinin doğru olması gerekir.
     * **Tümü (All)**: Eylemin devam etmesi için tüm koşulların doğru olması gerekir.
2. **Operatör:**
   * **Açıklama**: Belge miktarını belirtilen toleransla karşılaştırmak için uygulanacak koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Miktarın belirtilen tolerans değeriyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Miktarın belirtilen tolerans değerinden farklı olmasını sağlar.
     * **Büyüktür (>)**: Miktarın belirtilen toleranstan büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Miktarın belirtilen toleransa eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<)**: Miktarın belirtilen toleranstan küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Miktarın belirtilen toleransa eşit veya ondan küçük olup olmadığını kontrol eder.
3. **Tolerans Tutarı:**
   * **Açıklama**: Belge miktarının karşılaştırılacağı tolerans değerini belirtir.
   * **Detay**: Bu değer sayısaldır ve miktarda izin verilen varyans eşiğini temsil eder.
4. **Tolerans Türü:**
   * **Açıklama**: Uygulanacak tolerans türünü tanımlar.
   * **Seçenekler**:
     * **Yüzde**: Tolerans, satın alma siparişi miktarının yüzdesi olarak hesaplanır.
     * **Değer**: Tolerans, sabit bir sayısal değer olarak belirtilir.

## **Sürüm 4'teki Ek Bileşenler:**

* **Karşılaştırma Türü**: Karşılaştırılacak öğeleri seçer ve Sürüm 4'te miktarların nasıl değerlendirileceği konusunda daha fazla esneklik sağlar.
  * **Satın Alma Siparişinden Belgeye**: Satın alma siparişindeki miktarı ilgili belgedeki miktarla karşılaştırır.
  * **Alınandan Belgeye**: Alınan miktarı belgedeki miktarla karşılaştırır.
  * **Satın Alma Siparişinden Alınana**: Satın alma siparişi miktarını alınan miktarla karşılaştırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre ve tolerans tutarına/türüne bağlı olarak belgedeki miktarı satın alma siparişindeki toleransla karşılaştırır. Sürüm 4'te, **Karşılaştırma Türü**, satın alma siparişinden alınana veya satın alma siparişinden belgeye gibi farklı miktarların karşılaştırılmasına olanak tanıyarak daha dinamik bir karşılaştırma sağlar.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Karşılaştırma doğru sonuçlanırsa (örneğin, belge miktarı kabul edilebilir tolerans aralığı içindeyse), iş akışı devam edecektir.
  * **Yanlış Koşul**: Karşılaştırma yanlış sonuçlanırsa (örneğin, miktar toleransı karşılamıyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

**Sürüm 3:**

* Kullanıcılar, belge miktarını seçerek, tolerans tutarını ve tolerans türünü tanımlayarak ve miktarı toleransla karşılaştırmak için uygun operatörü seçerek kartı yapılandırır. Kart, miktarın tolerans eşiği içinde olup olmadığını değerlendirir ve sonuca göre "Doğru" veya "Yanlış" eylemiyle devam eder.

**Sürüm 4:**

* Sürüm 3'teki yapılandırmaya ek olarak, kullanıcılar aşağıdakiler gibi farklı öğeler arasında karşılaştırmalara olanak tanıyan **Karşılaştırma Türünü** seçebilirler:
  * **Satın Alma Siparişinden Belgeye**
  * **Alınandan Belgeye**
  * **Satın Alma Siparişinden Alınana**

## **Örnek Senaryo:**

Bir fatura 100 birimin teslim edildiğini gösteriyor, ancak satın alma siparişi yalnızca 90 birime izin veriyor. Tolerans tutarı 10 birim olarak ayarlanmış ve tolerans türü mutlaktır.

* **Sürüm 3**: Kart, belgedeki 100 birimi satın alma siparişinin 90 birimlik toleransıyla karşılaştırır. Miktar toleransı aşarsa, kart tutarsızlığı daha fazla inceleme için işaretler.
* **Sürüm 4**: Kart, **satın alma siparişi miktarını** (90 birim) **alınan miktarla** (100 birim) veya **belge miktarıyla** (100 birim) karşılaştırabilir. Seçilen **Karşılaştırma Türüne** bağlı olarak, iki öğe arasındaki farkın toleransı aşıp aşmadığını kontrol eder ve ilgili eylemi tetikler.

## **Sonuç:**

* **Sürüm 3**: Bu iş akışı kartı, belge miktarını satın alma siparişi toleransıyla karşılaştırarak miktardaki tutarsızlıkların işaretlenmesini ve uygun şekilde ele alınmasını sağlamaya yardımcı olur.
* **Sürüm 4**: Kullanıcıların satın alma siparişinden alınana veya satın alma siparişinden belgeye gibi farklı öğeleri karşılaştırmasına olanak tanıyarak bu işlevselliği genişletir ve daha karmaşık senaryoların ele alınmasında daha fazla esneklik sağlar. Sürüm 4, seçilen karşılaştırma türüne göre daha dinamik karşılaştırmalar ve eylemler sunarak satın alma ve alma iş akışları üzerinde daha sıkı kontrol sağlar.

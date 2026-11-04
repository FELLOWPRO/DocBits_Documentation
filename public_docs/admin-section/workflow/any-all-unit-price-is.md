<figure><img src="../../../../.gitbook/assets/image (274).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (273).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belgedeki birim fiyatı bir satın alma siparişindeki birim fiyatla karşılaştırmak için kullanılır ve fiyatların tanımlanan tolerans seviyeleri dahilinde hizalanmasını sağlar. Karşılaştırma, birim fiyat beklentileri karşılamıyorsa eylemleri tetikleyebilir. **Sürüm 4**, kullanıcıların karşılaştırma için farklı öğeler seçmesine olanak tanıyarak fiyatlandırma ve satın alma süreçleri üzerinde daha derin bir kontrol düzeyi sağlayarak daha fazla esneklik ekler.

## **Kartın Bileşenleri:**

1. **Herhangi biri / Tümü (Any / All):**
   * **Açıklama**: Koşulun birim fiyatın karşılaştırıldığı herhangi bir durum mu yoksa tüm durumlar için mi geçerli olduğunu tanımlar.
   * **Seçenekler**:
     * **Herhangi biri (Any)**: Herhangi bir birim fiyat belirtilen karşılaştırma koşulunu karşılıyorsa koşul karşılanır.
     * **Tümü (All)**: Koşul yalnızca tüm birim fiyatlar belirtilen karşılaştırma koşulunu karşılıyorsa karşılanır.
2. **Operatör:**
   * **Açıklama**: Birim fiyatı belirtilen değerle karşılaştırmak için koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Birim fiyatın belirtilen değerle eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Birim fiyatın belirtilen değerden farklı olmasını sağlar.
     * **Büyüktür (>)**: Birim fiyatın belirtilen değerden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birim fiyatın belirtilen değere eşit veya ondan büyük olup olmadığını doğrular.
     * **Küçüktür (<)**: Birim fiyatın belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birim fiyatın belirtilen değere eşit veya ondan küçük olup olmadığını doğrular.

## **Sürüm 4'teki Ek Bileşenler:**

**Karşılaştırma Türü:**

* **Açıklama**: Kullanıcıların birim fiyata ek olarak hangi öğelerin karşılaştırılacağını seçmesine olanak tanır.
* **Seçenekler**:
  * **Satın Alma Siparişinden Belgeye**: Satın alma siparişindeki birim fiyatı belgedeki birim fiyatla karşılaştırır.
  * **Alınandan Belgeye**: Alınan miktarı belgedeki birim fiyatla karşılaştırır.
  * **Satın Alma Siparişinden Alınana**: Satın alma siparişindeki birim fiyatı alınan miktarla karşılaştırır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, belgedeki birim fiyatı, seçilen operatöre göre satın alma siparişindeki (veya Sürüm 4'te seçilen diğer öğedeki) birim fiyatla karşılaştırır. Karşılaştırma doğruysa, iş akışı onayı tetikleyerek veya süreci durdurarak sonraki adımlara göre devam eder.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örneğin, belgedeki birim fiyat belirtilen değerden büyükse), iş akışı doğru eylemle (örneğin, onay, belge işleme) devam edecektir.
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örneğin, belgedeki birim fiyat karşılaştırmayı karşılamıyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

* **Sürüm 3 Kurulumu:** Kullanıcılar, belgedeki birim fiyatı seçerek, birim fiyatın belirtilen değerle nasıl karşılaştırılacağını tanımlamak için uygun operatörü seçerek ve karşılaştırılacak değeri ayarlayarak kartı yapılandırır. Ek olarak kullanıcılar, koşulun birim fiyat karşılaştırmasının herhangi bir durumuna mı yoksa tüm durumlarına mı uygulanacağını seçer.
* **Sürüm 4 Kurulumu:** Sürüm 4'te kullanıcılar Karşılaştırma Türünü seçmek için ek seçeneğe sahiptir. Bu, Satın Alma Siparişinden Belgeye, Alınandan Belgeye veya Satın Alma Siparişinden Alınana gibi karşılaştırılacak öğeleri tanımlamalarına olanak tanır. Bu, kartın daha karmaşık senaryolarda birim fiyatları karşılaştırma esnekliğini artırır.

## **Örnek Senaryo:**

*   **Sürüm 3 Örneği:**

    Bir fatura 50$ birim fiyat gösteriyor. İlgili satın alma siparişinin birim fiyatı 45$. Kart, "Büyüktür" operatörünü kullanarak iki birim fiyatı karşılaştırır. Belgedeki birim fiyat (50$), satın alma siparişindeki birim fiyattan (45$) büyük olduğu için iş akışı doğru koşulu tetikleyecektir (örneğin, belgeyi inceleme için gönder).
* **Sürüm 4 Örneği:**
  Bir fatura 50$ birim fiyat gösteriyor ve ilgili satın alma siparişi 45$ birim fiyata izin verdi. Ek olarak alınan miktar 60 birimdir. Kart, "Büyüktür" operatörünü kullanarak alınan miktarı belgenin birim fiyatıyla karşılaştırır. Alınan miktar (60), birim fiyattan (50$) büyük olduğu için iş akışı doğru koşulu tetikler ve belge daha fazla inceleme için işaretlenir.

## **Sonuç:**

"Birim Fiyat Karşılaştırması" iş akışı kartının Sürüm 3'ü, belgelerdeki birim fiyatların satın alma siparişlerindekilerle hizalanmasını sağlamak ve tanımlanan koşullara göre eylemleri tetiklemek için tasarlanmıştır. Sürüm 4, satın alma siparişlerini belgelerle, alınan miktarları belgelerle ve satın alma siparişlerini alınan miktarlarla karşılaştırmak gibi daha karmaşık karşılaştırma seçenekleri sunarak bu işlevselliği genişletir. Bu eklenen esneklik, kuruluşların daha gelişmiş fiyatlandırma ve satın alma senaryolarını ele almalarına olanak tanıyarak iş akışlarında kontrolü ve doğruluğu artırır.

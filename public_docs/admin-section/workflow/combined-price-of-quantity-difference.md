<figure><img src="../../../../.gitbook/assets/docbits_combined_price_card.png" alt="DocBits Combined Price Tarjeta" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/docbits_workflow_compare_two_fields.png" alt="Docbits Workflow Compare Two Fields" width="563"><figcaption></figcaption></figure>

## **Amaç**:

Bu iş akışı kartı, miktar farkının birleşik fiyatını değerlendirerek belirtilen bir değerle karşılaştırır. İlgili belgeler arasındaki fiyat ve miktar tutarsızlıklarına dayalı eylemleri otomatikleştirmeye yardımcı olur, satın alma ve alma iş akışlarını iyileştirir. **Sürüm 4**, satın alma siparişi, alınan miktarlar ve belgenin kendisi gibi farklı öğeler arasında karşılaştırmalara izin vererek bu işlevselliği genişletir ve iş akışına daha fazla esneklik ve kontrol ekler.

## **Kartın Bileşenleri**:

1. **Operatör**:
   * **Açıklama:** Birleşik fiyatı belirtilen bir değerle karşılaştırma koşulu.
   * **Seçenekler**:
     * **Eşittir (=)**: Birleşik fiyatın belirtilen değerle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Birleşik fiyatın belirtilen değerden farklı olmasını sağlar.
     * **Büyüktür (>)**: Birleşik fiyatın belirtilen değerden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birleşik fiyatın belirtilen değere eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<)**: Birleşik fiyatın belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birleşik fiyatın belirtilen değere eşit veya ondan küçük olup olmadığını kontrol eder.
2. **Değer**:
   * **Açıklama:** Miktar değerinin birleşik fiyatının karşılaştırılacağı değeri belirtir.
   * **Detay:** Değer sayısal bir değer olmalıdır.

## **Sürüm 4'teki Ek Bileşenler**:

* **Karşılaştırma Türü**: Karşılaştırılacak öğeleri seçer. Seçenekler şunlardır:
  * **Satın Alma Siparişinden Belgeye**: Satın alma siparişi ile ilgili belge arasındaki miktarları ve fiyatları karşılaştırır.
  * **Alınandan Belgeye**: Alınan miktarları belgedeki miktarlarla karşılaştırır.
  * **Satın Alma Siparişinden Alınana**: Satın alma siparişi miktarlarını alınan miktarlarla karşılaştırır.

## **İşlevsellik**:

* **Koşul Değerlendirmesi**: Miktar farkını birim fiyatla çarparak birleşik fiyatı hesaplar ve seçilen operatörü kullanarak belirtilen değerle karşılaştırır.
  **Sürüm 4**, kullanıcının yapılandırmasına bağlı olarak satın alma siparişinden alınana veya satın alma siparişinden belgeye gibi ek öğeleri karşılaştırma seçeneği ekler.
* **Eylem Yürütme**: Birleşik fiyatın belirtilen koşulu karşılayıp karşılamadığına bağlı olarak, iş akışı eylemleri tetiklemek veya iş akışını durdurmak için doğru veya yanlış koşullarıyla devam edecektir. **Sürüm 4** ayrıca, koşul türünün (örneğin satın alma siparişinden alınana) bir sonraki adımı etkilediği daha dinamik eylem yürütmesine olanak tanır.

## **Kurulum ve Yapılandırma**:

* **Sürüm 3**: Kullanıcılar, miktar farkı ve birim fiyat için belge alanlarını seçerek kartı yapılandırır. Ardından, birleşik fiyatın belirtilen değerle nasıl karşılaştırılacağını tanımlamak için operatör seçilir. Son olarak kullanıcılar, iş akışındaki bir sonraki adımı belirleyen devam koşulunu (doğru veya yanlış) ayarlar.
* **Sürüm 4**: **Sürüm 3**'teki yapılandırmaya ek olarak, kullanıcıların **Karşılaştırma Türünü** yapılandırmak için ek bir seçeneği vardır. Bu, **Satın Alma Siparişinden Belgeye**, **Alınandan Belgeye** veya **Satın Alma Siparişinden Alınana** gibi hangi öğelerin karşılaştırılacağını tanımlar.

## **Örnek Senaryo**:

* Bir fatura, her biri 100$ olan bir üründen 50 birim gösteriyor ve toplam 5000$. İlgili satın alma siparişi 45 birim için 4500$'lık bir satın almaya izin verdi. Miktar farkı 5 birimdir ve farkın birleşik fiyatı 500$'dır. Kart, satın alma siparişi miktarını (45 birim) alınan miktarla (50 birim) karşılaştırır ve birleşik fiyatın 400$'dan (belirtilen değer) büyük olup olmadığını kontrol eder. **Büyüktür (>)** operatörünü kullanarak kart, tutarsızlığı tanımlar ve finans ekibi tarafından incelenmesi için işaretler.

## **Sonuç**:

"Miktar Farkının Birleşik Fiyatı" iş akışı kartının **Sürüm 3**'ü, miktar tutarsızlıklarını karşılaştırmak ve fiyat eşiklerine dayalı eylemleri tetiklemek için doğrudan bir yaklaşım sunar.
**Sürüm 4**, farklı öğeler (satın alma siparişi, alınan, belge) arasında karşılaştırmalara izin vererek bu işlevselliği genişletir ve iş akışı üzerinde daha fazla esneklik ve kontrol sağlar. Kuruluşlar artık daha karmaşık senaryoları otomatikleştirebilir ve satın alma ve alma süreçleri üzerinde daha sıkı kontrol uygulayabilir.

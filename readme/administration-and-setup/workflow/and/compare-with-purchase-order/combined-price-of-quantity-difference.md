# Combined Price of Quantity Difference

<figure><img src="../../../../.gitbook/assets/image (17) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (21) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**:

Bu iş akışı kartı, bir miktar farkının birleşik fiyatını değerlendirir ve bunu belirtilen bir değere karşı karşılaştırır. İlgili belgeler arasındaki fiyat ve miktar tutarsızlıklarına dayalı eylemleri otomatikleştirmeye yardımcı olur ve satınalma ile teslim alma iş akışlarını iyileştirir. **Sürüm 4**, satınalma siparişi, teslim alınan miktarlar ve belgenin kendisi gibi farklı varlıklar arasında karşılaştırmalara olanak tanıyarak bu işlevselliği genişletir ve iş akışına daha fazla esneklik ve kontrol ekler.

## **Kartın Bileşenleri**:

1. **Operatör**:&#x20;
   * **Açıklama:** Birleşik fiyatı belirtilen bir değere karşı karşılaştırma koşulu.
   * **Seçenekler:**
     * **Eşittir (=)**: Birleşik fiyatın belirtilen değerle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠)**: Birleşik fiyatın belirtilen değerden farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Birleşik fiyatın belirtilen değerden büyük olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥)**: Birleşik fiyatın belirtilen değere eşit veya ondan büyük olup olmadığını kontrol eder.
     * **Küçüktür (<)**: Birleşik fiyatın belirtilen değerden küçük olup olmadığını doğrular.
     * **Küçük veya Eşittir (≤)**: Birleşik fiyatın belirtilen değere eşit veya ondan küçük olup olmadığını kontrol eder.
2. **Değer**:&#x20;
   * **Açıklama:** Miktar farkının birleşik fiyat değerinin karşılaştırılacağı değeri belirtir.
   * **Ayrıntı:** Değer sayısal bir değer olmalıdır.

## **Sürüm 4'teki Ek Bileşenler**:

* **Karşılaştırma Türü**: Karşılaştırılacak varlıkları seçer. Seçenekler şunları içerir:
  * **Satınalma Siparişinden Belgeye**: Satınalma siparişi ile ilgili belge arasındaki miktarları ve fiyatları karşılaştırır.
  * **Teslim Alınandan Belgeye**: Teslim alınan miktarları belgedeki miktarlarla karşılaştırır.
  * **Satınalma Siparişinden Teslim Alınana**: Satınalma siparişi miktarlarını teslim alınan miktarlarla karşılaştırır.

## **İşlevsellik**:

* **Koşul Değerlendirmesi**: Miktar farkını birim başına fiyatla çarparak birleşik fiyatı hesaplar ve seçilen operatörü kullanarak belirtilen değere karşı karşılaştırır.\
  **Sürüm 4**, satınalma siparişinden teslim alınana veya satınalma siparişinden belgeye gibi kullanıcının yapılandırmasına dayalı ek varlıkları karşılaştırma seçeneğini ekler.
* **Eylem Yürütme**: Birleşik fiyatın belirtilen koşulu karşılayıp karşılamadığına bağlı olarak, iş akışı eylemleri tetiklemek veya iş akışını durdurmak için doğru veya yanlış koşullarla devam eder. **Sürüm 4** ayrıca koşul türünün (örn. satınalma siparişinden teslim alınana) sonraki adımı etkilediği daha dinamik eylem yürütmesine olanak tanır.

## **Kurulum ve Yapılandırma**:

* **Sürüm 3**: Kullanıcılar, miktar farkı ve birim başına fiyat için belge alanlarını seçerek kartı yapılandırır. Ardından, birleşik fiyatın belirtilen değere nasıl karşılaştırılacağını tanımlamak için operatör seçilir. Son olarak, kullanıcılar iş akışındaki sonraki adımı belirleyen devam koşulunu (doğru veya yanlış) ayarlar.
* **Sürüm 4**: **Sürüm 3**'teki yapılandırmaya ek olarak, kullanıcılar **Karşılaştırma Türü**'nü yapılandırmak için ek bir seçeneğe sahiptir. Bu, **Satınalma Siparişinden Belgeye**, **Teslim Alınandan Belgeye** veya **Satınalma Siparişinden Teslim Alınana** gibi hangi varlıkların karşılaştırılacağını tanımlar.

## **Örnek Senaryo**:

* Bir fatura, bir ürünün her biri $100'dan 50 birimini gösterir, toplam $5000. İlgili satınalma siparişi, 45 birim için $4500'lik bir satın almaya yetki vermiştir. Miktar farkı 5 birimdir ve farkın birleşik fiyatı $500'dür. Kart, satınalma siparişi miktarını (45 birim) teslim alınan miktarla (50 birim) karşılaştırır ve birleşik fiyatın $400'den (belirtilen değer) büyük olup olmadığını kontrol eder. **Büyüktür (>)** operatörünü kullanarak, kart tutarsızlığı tanımlar ve finans ekibi tarafından inceleme için işaretler.

## **Sonuç**:

"Combined Price of Quantity Difference" iş akışı kartının **Sürüm 3**'ü, miktar tutarsızlıklarını karşılaştırmak ve fiyat eşiklerine dayalı eylemleri tetiklemek için basit bir yaklaşım sunar.\
**Sürüm 4**, farklı varlıklar (satınalma siparişi, teslim alınan, belge) arasında karşılaştırmalara olanak tanıyarak bu işlevselliği genişletir ve iş akışı üzerinde daha fazla esneklik ve kontrol sağlar. Kuruluşlar artık daha karmaşık senaryoları otomatikleştirebilir ve satınalma ile teslim alma süreçleri üzerinde daha sıkı kontrol uygulayabilir.

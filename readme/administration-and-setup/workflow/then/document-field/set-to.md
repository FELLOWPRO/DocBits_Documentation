# Set to

<figure><img src="../../../../.gitbook/assets/image (278).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, **"Where"** ve **"And Bölümleri"**nde tanımlanan koşullara göre belgedeki belirtilen bir alanı önceden tanımlanmış bir metin değerine otomatik olarak ayarlamak için tasarlanmıştır. Belirli ölçütler karşılandığında alanların tutarlı değerlerle doldurulmasını sağlayarak kullanıcıların veri girişini kolaylaştırmasına olanak tanır.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama**: Metin değeriyle güncellenecek alanı belirtir.&#x20;
   * **Ayrıntı**: Seçilen alan, **"Where"** ve **"And Bölümleri"**ndeki koşullar karşılanırsa belirtilen metin değeriyle güncellenir.
2. **Metin (Text)**
   * **Açıklama**: Koşullar doğru olarak değerlendirildiğinde hedef alana ayarlanacak metin değerini tanımlar.
   * **Ayrıntı**: Bu, kullanıcının alana yazmak istediği özel bir mesaj, durum veya önceden tanımlanmış bir değer olabilir. Metin, alanın beklenen giriş biçimiyle (örn. alfasayısal, tarih veya diğer metinsel bilgi türleri) uyumlu olmalıdır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, **"Where"** ve **"And Bölümleri"**ndeki koşulları değerlendirir:
  * **Her iki koşul da doğruysa**, **"Then Bölümü"**nde tanımlanan eylemler yürütülür. Özellikle, hedef alan (Alan Adı) belirtilen metinle doldurulur.
  * **"Where" veya "And" bölümünden biri yanlışsa**, hiçbir eylem gerçekleştirilmez ve alan değişmeden kalır. Koşullardan biri yanlışsa **Then Bölümü** eylemleri tamamen atlanır.
* **Eylem Yürütme**: **"Where"** ve **"And Bölümleri"**ndeki her iki koşul da karşılanırsa, sistem belirtilen alanı seçilen metin değeriyle otomatik olarak doldurur. Koşullar karşılanmazsa, alanda hiçbir değişiklik yapılmaz.

## **Kurulum ve Yapılandırma:**

Bu kartı kurmak için:

1. Metin değeriyle güncellenecek **alanı (Alan Adı) seçin**. Belgedeki kullanılabilir alanlar seçim için listelenir.
2. Koşullar doğru olduğunda hedef alana yazılacak **metin değerini belirtin**.
3. Eylem yalnızca hem **"Where"** hem de **"And Bölümleri"** koşulları doğru olarak değerlendirilirse yürütülür.

## **Sonuç:**

**"Set Field to Text"** iş akışı kartı, önceden tanımlanmış koşullara göre metin değerlerinin belirli belge alanlarına doldurulmasını otomatikleştirmek için basit bir yol sunar. Bu, manuel veri girişini azaltır ve belge işlemede tutarlılığı sağlar, iş akışlarını otomatikleştirmek ve verimliliği artırmak için yararlı bir araç haline getirir.

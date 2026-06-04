# Invert Checkbox

<figure><img src="../../../../.gitbook/assets/image (280).png" alt=""><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir onay kutusu alanının mevcut durumunu tersine çevirmek için tasarlanmıştır. Onay kutusu işaretliyse (true), işaretsiz hale getirilir (false) ve tam tersi. Tersine çevirme, **"Where"** ve **"And Bölümleri"**nde ayarlanan koşullara göre gerçekleşir. Bu kart, bir koşulun belirli ölçütlere göre bir onay kutusunu değiştirmeyi gerektirdiği iş akışlarını otomatikleştirmeye yardımcı olur.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama**: Tersine çevrilecek onay kutusu alanını belirtir.&#x20;
   * **Ayrıntı**: Seçilen onay kutusu alanının durumu, mevcut durumuna göre true'dan false'a veya false'dan true'ya değiştirilecektir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, **"Where"** ve **"And Bölümleri"**nde tanımlanan koşulları değerlendirir:
  * **Her iki koşul da doğruysa**, **"Then Bölümü"** eylemi yürütülür; bu durumda onay kutusu alanı değiştirilecektir.
  * **Koşullardan biri yanlışsa**, kart yürütülmez ve onay kutusu alanında hiçbir değişiklik yapılmaz.
* **Eylem Yürütme**: **"Where"** ve **"And Bölümleri"**ndeki koşullar doğru olarak değerlendirilirse, onay kutusu alanının durumu tersine çevrilir:
  * Onay kutusu işaretliyse (true), işaretsiz hale getirilir (false).
  * Onay kutusu işaretsizse (false), işaretli hale getirilir (true).

## **Kurulum ve Yapılandırma:**

Bu kartı yapılandırmak için, kullanıcıların şunları yapması gerekir:

1. Tersine çevrilecek **onay kutusu alanını (Alan Adı) seçin**. Belgedeki kullanılabilir onay kutusu alanları seçim için listelenir.
2. Onay kutusu alanı yalnızca hem **"Where"** hem de **"And Bölümleri"**ndeki koşullar doğruysa tersine çevrilir.

## **Sonuç:**

**"Invert checkbox \[Field Name]"** iş akışı kartı, belirli koşullara göre onay kutusu değerlerini değiştirmek için basit ama güçlü bir otomasyon aracı sunar. Manuel onay kutusu ayarlamalarına olan ihtiyacı azaltarak, bu kart belge işlemede verimliliği artırır ve iş akışları arasında tutarlılığı sağlar.

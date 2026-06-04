# Compare Order Confirmation with Purchase order

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

Bu DocBits kartı, bir sipariş onayı ile bir satınalma siparişi arasında miktar, indirim veya birim fiyat gibi belirli bir sipariş veri alanını karşılaştırmak için tasarlanmıştır. Aynı anda tek bir alanın odaklı karşılaştırmasına olanak tanıyarak, temel veri noktalarını doğrulamada hassasiyet sağlar ve sipariş doğruluğunu korur. **Sürüm 4**, satınalma siparişi, teslim alınan miktarlar ve belgenin kendisi gibi farklı varlıklar arasında karşılaştırmalara olanak tanıyarak bu işlevselliği genişletir ve iş akışına daha fazla esneklik ve kontrol ekler.

## Kartın Bileşenleri:

1. **Any/All**&#x20;
   * **Açıklama:** Koşulun sipariş onayındaki herhangi bir veya tüm satırlara uygulanıp uygulanmayacağını belirler.\
     **Seçenekler:**
     * **Any**: Sipariş onayının herhangi bir satırındaki seçili alan değeri satınalma siparişindeki karşılık gelen değerle eşleşirse karşılaştırma tetiklenir.
     * **All**: Yalnızca sipariş onayının tüm satırlarındaki seçili alan değeri satınalma siparişindeki karşılık gelen değerle eşleşirse karşılaştırma tetiklenir.
2. **Sipariş Veri Alanı**
   * **Açıklama**: Sipariş onayı ile satınalma siparişi arasında karşılaştırılacak veri alanını belirtir.
   * **Ayrıntı**: Kullanıcılar karşılaştırma için aşağıdaki alanlardan birini seçebilir:
     * **Miktar**: Sipariş edilen miktarı onaylanan miktarla karşılaştırır.
     * **İndirim**: Onaydaki indirimin satınalma siparişiyle eşleştiğini doğrular.
     * **Birim Fiyat**: Onaydaki birim fiyatın satınalma siparişiyle uyumlu olmasını sağlar.
3. **Operatör**
   * **Açıklama**: Seçilen veri alanının karşılaştırmasına uygulanan koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Değerin satınalma siparişiyle eşleştiğini onaylar.
     * **Eşit Değildir (≠)**: Değerin satınalma siparişinden farklı olduğunu garanti eder.
     * **Büyüktür (>)**: Değerin satınalma siparişinin değerini aştığını doğrular.
     * **Büyük veya Eşittir (≥)**: Değerin satınalma siparişinin değerine eşit veya onu aştığını onaylar.
     * **Küçüktür (<)**: Değerin satınalma siparişinin değerinin altında olduğunu kontrol eder.
     * **Küçük veya Eşittir (≤)**: Değerin satınalma siparişinin değerinin altında veya ona eşit olduğunu onaylar.

## **Sürüm 4'teki Ek Bileşenler**:

* **Karşılaştırma Türü**: Karşılaştırılacak varlıkları seçer. Seçenekler şunları içerir:
  * **Satınalma Siparişinden Belgeye**: Satınalma siparişi verisini ilgili belgeyle karşılaştırır.
  * **Teslim Alınandan Belgeye**: Teslim alınan veriyi (örn. teslim alınan miktarlar) belgeyle karşılaştırır.
  * **Satınalma Siparişinden Teslim Alınana**: Satınalma siparişi verisini teslim alınan miktarlarla karşılaştırır.

## İşlevsellik:

* **Alan Karşılaştırması**: Sistem, sipariş onayından seçilen sipariş veri alanını (Birim Fiyat, İndirim veya Miktar) satınalma siparişindeki karşılık gelen değerle karşılaştırır.
* **Eylem Yürütme**: Karşılaştırma sonucuna ve operatör koşuluna dayanarak, kart bildirimler veya uyarılar gibi takip eylemlerini tetikleyebilir.

## Örnek Senaryo:

* Bir sipariş onayı **$50 birim fiyat** belirtirken, satınalma siparişi $45 belirtir. "Büyüktür" operatörünü kullanarak, kart tutarsızlığı işaretler ve satınalma ekibinin işlemeden önce bunu ele almasına olanak tanır.

## Sonuç:

Bu kart, bireysel sipariş veri alanlarının doğrulanmasını basitleştirir ve satınalma siparişi koşullarına uyumu sağlar. Karşılaştırma için aynı anda tek bir alanı izole ederek, sipariş işlemede hedefli incelemeleri ve hata önlemeyi destekler.

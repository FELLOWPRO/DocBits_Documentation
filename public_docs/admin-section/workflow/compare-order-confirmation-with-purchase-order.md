<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

<figure><img src="../../../../.gitbook/assets/image (267).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

Bu DocBits kartı, bir sipariş onayı ile bir satın alma siparişi arasında miktar, indirim veya birim fiyat gibi belirli bir sipariş veri alanını karşılaştırmak için tasarlanmıştır. Bir seferde bir alanın odaklanmış bir karşılaştırmasına izin vererek, temel veri noktalarının doğrulanmasında hassasiyet sağlar ve sipariş doğruluğunu korur. **Sürüm 4**, satın alma siparişi, alınan miktarlar ve belgenin kendisi gibi farklı öğeler arasında karşılaştırmalara izin vererek bu işlevselliği genişletir ve iş akışına daha fazla esneklik ve kontrol ekler.

## Kartın Bileşenleri:

1. **Herhangi biri/Tümü (Any/All)**
   * **Açıklama:** Koşulun sipariş onayındaki herhangi bir satır mı yoksa tüm satırlar için mi geçerli olduğunu belirler.
     **Seçenekler:**
     * **Herhangi biri (Any)**: Sipariş onayındaki herhangi bir satırdaki seçilen alan değeri satın alma siparişindeki karşılık gelen değerle eşleşirse karşılaştırma tetiklenir.
     * **Tümü (All)**: Yalnızca sipariş onayındaki tüm satırlardaki seçilen alan değeri satın alma siparişindeki karşılık gelen değerle eşleşirse karşılaştırma tetiklenir.
2. **Sipariş Veri Alanı**
   * **Açıklama**: Sipariş onayı ile satın alma siparişi arasında karşılaştırılacak veri alanını belirtir.
   * **Detay**: Kullanıcılar karşılaştırma için aşağıdaki alanlardan birini seçebilir:
     * **Miktar**: Sipariş edilen miktarı onaylanan miktarla karşılaştırır.
     * **İndirim**: Onaydaki indirimin satın alma siparişiyle eşleştiğini doğrular.
     * **Birim Fiyat**: Onaydaki birim fiyatın satın alma siparişiyle uyumlu olmasını sağlar.
3. **Operatör**
   * **Açıklama**: Seçilen veri alanının karşılaştırmasına uygulanan koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Değerin satın alma siparişiyle eşleştiğini onaylar.
     * **Eşit Değildir (≠)**: Değerin satın alma siparişinden farklı olmasını sağlar.
     * **Büyüktür (>)**: Değerin satın alma siparişinin değerini aştığını doğrular.
     * **Büyük veya Eşittir (≥)**: Değerin satın alma siparişinin değerine eşit olduğunu veya onu aştığını onaylar.
     * **Küçüktür (<)**: Değerin satın alma siparişinin değerinin altında olduğunu kontrol eder.
     * **Küçük veya Eşittir (≤)**: Değerin satın alma siparişinin değerinin altında olduğunu veya ona eşit olduğunu onaylar.

## **Sürüm 4'teki Ek Bileşenler**:

* **Karşılaştırma Türü**: Karşılaştırılacak öğeleri seçer. Seçenekler şunlardır:
  * **Satın Alma Siparişinden Belgeye**: Satın alma siparişi verilerini ilgili belgeyle karşılaştırır.
  * **Alınandan Belgeye**: Alınan verileri (örneğin alınan miktarlar) belgeyle karşılaştırır.
  * **Satın Alma Siparişinden Alınana**: Satın alma siparişi verilerini alınan miktarlarla karşılaştırır.

## İşlevsellik:

* **Alan Karşılaştırması**: Sistem, sipariş onayından seçilen sipariş veri alanını (Birim Fiyat, İndirim veya Miktar) satın alma siparişindeki karşılık gelen değerle karşılaştırır.
* **Eylem Yürütme**: Karşılaştırma sonucuna ve operatör koşuluna bağlı olarak, kart bildirimler veya uyarılar gibi takip eylemlerini tetikleyebilir.

## Örnek Senaryo:

* Bir sipariş onayı 50$ bir **birim fiyat** belirtirken, satın alma siparişi 45$ belirtiyor. "Büyüktür" operatörünü kullanan kart, tutarsızlığı işaretleyerek satın alma ekibinin işlemeden önce bunu ele almasını sağlar.

## Sonuç:

Bu kart, bireysel sipariş veri alanlarının doğrulanmasını basitleştirerek satın alma siparişi şartlarına uyumu sağlar. Karşılaştırma için bir seferde bir alanı izole ederek, sipariş işlemede hedeflenen incelemeleri ve hata önlemeyi destekler.

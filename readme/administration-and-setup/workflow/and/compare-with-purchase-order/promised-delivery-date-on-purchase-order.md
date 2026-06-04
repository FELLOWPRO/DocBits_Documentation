# Promised Delivery Date on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu DocBits kartı, satınalma siparişlerindeki vaat edilen teslimat tarihlerinin bir tablodaki satır öğeleri için belirtilen teslimat tarihleriyle hassas bir şekilde karşılaştırılmasını kolaylaştırmak için tasarlanmıştır. Bir tolerans değerini entegre ederek, kart teslimat zaman çizelgelerini izlemede esneklik sağlar, envanter planlama doğruluğunu ve müşteri memnuniyetini korumaya yardımcı olur.

## **Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama:** Teslimat tarihlerini karşılaştırmak için uygulanan koşulu tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Satır öğesindeki vaat edilen teslimat tarihinin satınalma siparişinin teslimat tarihiyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠):** Satır öğesindeki vaat edilen teslimat tarihinin satınalma siparişindeki tarihle eşleşmediğini garanti eder.
     * **Büyüktür (>):** Satır öğesinin vaat edilen teslimat tarihinin satınalma siparişinin teslimat tarihinden sonra olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥):** Satır öğesinin vaat edilen teslimat tarihinin satınalma siparişinin teslimat tarihine eşit veya ondan sonra olup olmadığını kontrol eder.
     * **Küçüktür (<):** Satır öğesinin vaat edilen teslimat tarihinin satınalma siparişinin teslimat tarihinden önce olup olmadığını onaylar.
     * **Küçük veya Eşittir (≤):** Satır öğesinin vaat edilen teslimat tarihinin satınalma siparişinin teslimat tarihine eşit veya ondan önce olup olmadığını doğrular.
2. **Değer**
   * **Açıklama:** Teslimat tarihi karşılaştırmasında izin verilen bir hata payını belirtir.
   * **Ayrıntı:** Kullanıcılar, satır öğesi teslimat tarihinin vaat edilen teslimat tarihinden ne kadar gün farklı olabileceğini tanımlar.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**\
  Kart, satınalma siparişinin vaat edilen teslimat tarihi ile tablodaki satır öğeleri için teslimat tarihleri arasındaki farkı hesaplar. Ardından, koşulun karşılanıp karşılanmadığını belirlemek için seçilen operatör uygulanır.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Teslimat tarihi farkı tolerans aralığında ise ve operatör tarafından ayarlanan koşulla eşleşiyorsa, iş akışı ilerler.
  * **Yanlış Koşul:** Koşul karşılanmazsa, iş akışı devam etmez.

## **Kurulum ve Yapılandırma**

* İstenen karşılaştırma koşulunu (eşittir, büyüktür veya küçüktür gibi) tanımlamak için operatör seçilir. Son olarak, kullanıcılar gün cinsinden bir tolerans değeri belirtir; bu, uyarıları tetiklemeden karşılaştırmada küçük varyasyonlara olanak tanır.

## **Örnek Senaryo**

* Bir satınalma siparişi 1 Aralık vaat edilen teslimat tarihini belirtir. Tablodaki bir satır öğesinin vaat edilen teslimat tarihi 3 Aralıktır. Tolerans değeri 2 gün olarak ayarlanmış ve **Eşittir (≥)** operatörü seçilmişken, kart teslimat tarihini kabul edilebilir aralık içinde sayar. Hiçbir uyarı tetiklenmez, böylece küçük varyanslar operasyonları kesintiye uğratmadan tolere edilir.

## **Sonuç**

"Promised Delivery Date Comparison" kartı, teslimat zaman çizelgelerinin hassas izlenmesini mümkün kılarak tedarik zinciri operasyonlarını kolaylaştırmaya yardımcı olur. Toleransları ve esnek karşılaştırma operatörlerini dahil etme yeteneğiyle, küçük sapmalar için gereksiz uyarılardan kaçınırken teslimat beklentilerine bağlılığı sağlar. Bu, tedarikçi yönetimini ve genel iş akışı verimliliğini artırır.

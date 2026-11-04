# Satın Alma Siparişindeki Vaat Edilen Teslimat Tarihi

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu DocBits kartı, satın alma siparişlerindeki vaat edilen teslimat tarihlerinin bir tablodaki kalemler için belirtilen teslimat tarihleriyle hassas bir şekilde karşılaştırılmasını kolaylaştırmak üzere tasarlanmıştır. Bir tolerans değerini entegre ederek kart, teslimat zaman çizelgelerinin izlenmesinde esneklik sağlar, envanter planlama doğruluğunun ve müşteri memnuniyetinin korunmasına yardımcı olur.

## **Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama:** Teslimat tarihlerini karşılaştırmak için uygulanan koşulu tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Kalemdeki vaat edilen teslimat tarihinin satın alma siparişinin teslimat tarihiyle eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değil (≠):** Kalemdeki vaat edilen teslimat tarihinin satın alma siparişindeki tarihle eşleşmemesini sağlar.
     * **Büyüktür (>):** Kalemin vaat edilen teslimat tarihinin satın alma siparişinin teslimat tarihinden daha geç olup olmadığını doğrular.
     * **Büyük veya Eşittir (≥):** Kalemin vaat edilen teslimat tarihinin satın alma siparişinin teslimat tarihine eşit veya ondan daha geç olup olmadığını kontrol eder.
     * **Küçüktür (<):** Kalemin vaat edilen teslimat tarihinin satın alma siparişinin teslimat tarihinden daha erken olduğunu onaylar.
     * **Küçük veya Eşittir (≤):** Kalemin vaat edilen teslimat tarihinin satın alma siparişinin teslimat tarihine eşit veya ondan daha erken olup olmadığını doğrular.
2. **Değer**
   * **Açıklama:** Teslimat tarihi karşılaştırmasında izin verilebilir bir hata payı belirtir.
   * **Detay:** Kullanıcılar, kalem teslimat tarihinin vaat edilen teslimat tarihinden farklı olabileceği gün sayısını tanımlar.

## **İşlevsellik**

* **Koşul Değerlendirmesi:**
  Kart, satın alma siparişinin vaat edilen teslimat tarihi ile tablodaki kalemlerin teslimat tarihleri arasındaki farkı hesaplar. Ardından koşulun karşılanıp karşılanmadığını belirlemek için seçilen operatör uygulanır.
* **Eylem Yürütme:**
  * **Doğru Koşul:** Teslimat tarihi farkı tolerans aralığı içindeyse ve operatör tarafından belirlenen koşulla eşleşiyorsa iş akışı devam eder.
  * **Yanlış Koşul:** Koşul karşılanmazsa iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma**

* Eşittir, büyüktür veya küçüktür gibi istenen karşılaştırma koşulunu tanımlamak için operatör seçilir. Son olarak kullanıcılar, uyarıları tetiklemeden karşılaştırmada küçük varyasyonlara izin veren gün cinsinden bir tolerans değeri belirtir.

## **Örnek Senaryo**

* Bir satın alma siparişi 1 Aralık vaat edilen teslimat tarihini belirtiyor. Tablodaki bir kalem 3 Aralık vaat edilen teslimat tarihine sahip. Tolerans değeri 2 gün olarak ayarlandığında ve **Eşittir (≥)** operatörü seçildiğinde, kart teslimat tarihini kabul edilebilir aralıkta sayar. Herhangi bir uyarı tetiklenmez, böylece operasyonları aksatmadan küçük farklılıklara tolerans gösterilmesi sağlanır.

## **Sonuç**

"Vaat Edilen Teslimat Tarihi Karşılaştırması" kartı, teslimat zaman çizelgelerinin hassas bir şekilde izlenmesini sağlayarak tedarik zinciri operasyonlarını kolaylaştırmaya yardımcı olur. Toleransları ve esnek karşılaştırma operatörlerini dahil etme yeteneği ile, küçük sapmalar için gereksiz uyarılardan kaçınırken teslimat beklentilerine uyumu sağlar. Bu, tedarikçi yönetimini ve genel iş akışı verimliliğini artırır.

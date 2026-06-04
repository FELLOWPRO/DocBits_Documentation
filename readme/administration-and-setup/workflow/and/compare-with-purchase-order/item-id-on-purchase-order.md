# Item Id on Purchase Order

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, doğru öğelerin dahil edilmesini sağlamak için bir satınalma siparişi ile ilgili bir belge arasındaki öğe kimliklerini karşılaştırmak için tasarlanmıştır. Kart, satınalma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle eşleşip eşleşmediğini değerlendirir. Bu karşılaştırma, tutarsızlıklar bulunursa eylemleri tetikleyebilir ve belgedeki öğelerin satınalma siparişiyle uyumlu olmasını sağlar.

## **Kartın Bileşenleri:**

1. **Any / All:**
   * **Açıklama**: Koşulun öğe kimliği karşılaştırmalarının herhangi bir veya tüm örneklerine uygulanıp uygulanmayacağını tanımlar.
   * **Seçenekler**:
     * **Any**: Satınalma siparişindeki herhangi bir öğe kimliği belgedeki öğe kimliğiyle eşleşirse koşul karşılanır.
     * **All**: Yalnızca satınalma siparişindeki tüm öğe kimlikleri belgedeki öğe kimlikleriyle eşleşirse koşul karşılanır.
2. **Operatör:**
   * **Açıklama**: Satınalma siparişindeki öğe kimliğini belgedeki öğe kimliğine karşı karşılaştırma koşulunu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Satınalma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle tam olarak eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Satınalma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle eşleşmediğini garanti eder.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre dayanarak satınalma siparişindeki öğe kimliğini belgedeki öğe kimliğiyle karşılaştırır. Karşılaştırma koşulu doğruysa (örn. öğe kimlikleri eşleşir veya eşleşmez), iş akışı buna göre ilerler.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örn. satınalma siparişindeki öğe kimliği belgedeki öğe kimliğine eşitse), iş akışı doğru eylemiyle devam eder (örn. onay veya daha fazla işleme).
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örn. satınalma siparişindeki öğe kimliği belgedeki öğe kimliğiyle eşleşmezse), iş akışı ilerlemez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, hem satınalma siparişindeki hem de belgedeki öğe kimliğini seçerek kartı yapılandırır. Ardından, öğe kimliklerinin nasıl karşılaştırılacağını tanımlamak için uygun operatörü (Eşittir veya Eşit Değildir) seçerler. Son olarak, kullanıcılar koşulun karşılaştırmadaki öğe kimliklerinin herhangi birine veya tümüne uygulanıp uygulanmayacağını seçer.

## **Örnek Senaryo:**

* Bir fatura "ABC123" kimlikli bir öğe listeler ve ilgili satınalma siparişi de "ABC123" kimlikli bir öğe içerir. "Eşittir" operatörünü kullanarak, kart belgedeki öğe kimliğini satınalma siparişindeki öğe kimliğiyle karşılaştırır. Öğe kimlikleri eşleştiğinden, iş akışı sorunsuz devam eder.

## **Sonuç:**

"Item ID Comparison" iş akışı kartı, belgelerdeki öğe kimliklerinin satınalma siparişlerindekilerle uyumlu olmasını sağlar. Bu, öğe listelerindeki tutarsızlıkları önlemeye yardımcı olur ve doğru öğelerin satınalma siparişine göre işlenmesini sağlar. Herhangi bir veya tüm örneklere göre karşılaştırma yapabilme yeteneği, farklı kullanım durumlarında esneklik sağlar ve satınalma iş akışlarının doğruluğunu ve verimliliğini artırır.

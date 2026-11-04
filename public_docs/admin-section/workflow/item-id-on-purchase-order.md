# Satın Alma Siparişindeki Öğe Kimliği

<figure><img src="../../../../.gitbook/assets/image (275).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, doğru öğelerin dahil edildiğinden emin olmak için bir satın alma siparişi ile ilgili bir belge arasındaki öğe kimliklerini karşılaştırmak üzere tasarlanmıştır. Kart, satın alma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle eşleşip eşleşmediğini değerlendirir. Bu karşılaştırma, tutarsızlıklar bulunursa eylemleri tetikleyerek belgedeki öğelerin satın alma siparişiyle uyumlu olmasını sağlayabilir.

## **Kartın Bileşenleri:**

1. **Herhangi biri / Tümü (Any / All):**
   * **Açıklama**: Koşulun öğe kimliği karşılaştırmalarının herhangi bir durumu için mi yoksa tüm durumları için mi geçerli olduğunu tanımlar.
   * **Seçenekler**:
     * **Herhangi biri (Any)**: Satın alma siparişindeki herhangi bir öğe kimliği belgedeki öğe kimliğiyle eşleşirse koşul karşılanır.
     * **Tümü (All)**: Koşul yalnızca satın alma siparişindeki tüm öğe kimlikleri belgedeki öğe kimlikleriyle eşleşirse karşılanır.
2. **Operatör:**
   * **Açıklama**: Satın alma siparişindeki öğe kimliğini belgedeki öğe kimliğiyle karşılaştırmak için koşulu tanımlar.
   * **Seçenekler**:
     * **Eşittir (=)**: Satın alma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle tam olarak eşleşip eşleşmediğini doğrular.
     * **Eşit Değildir (≠)**: Satın alma siparişindeki öğe kimliğinin belgedeki öğe kimliğiyle eşleşmemesini sağlar.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre bağlı olarak satın alma siparişindeki öğe kimliğini belgedeki öğe kimliğiyle karşılaştırır. Karşılaştırma koşulu doğruysa (örneğin, öğe kimlikleri eşleşiyor veya gerektiği gibi eşleşmiyor), iş akışı buna göre devam edecektir.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örneğin, satın alma siparişindeki öğe kimliği belgedeki öğe kimliğine eşitse), iş akışı doğru eylemle (örneğin, onay veya daha fazla işleme) devam edecektir.
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örneğin, satın alma siparişindeki öğe kimliği belgedeki öğe kimliğiyle eşleşmiyorsa), iş akışı devam etmeyecektir.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, hem satın alma siparişindeki hem de belgedeki öğe kimliğini seçerek kartı yapılandırır. Ardından, öğe kimliklerinin nasıl karşılaştırılacağını tanımlamak için uygun operatörü (Eşittir veya Eşit Değildir) seçerler. Son olarak kullanıcılar, koşulun karşılaştırmadaki öğe kimliklerinin herhangi birine mi yoksa tümüne mi uygulanacağını seçer.

## **Örnek Senaryo:**

* Bir fatura "ABC123" kimliğine sahip bir öğeyi listeliyor ve ilgili satın alma siparişi de "ABC123" kimliğine sahip bir öğeyi içeriyor. "Eşittir" operatörünü kullanan kart, belgedeki öğe kimliğini satın alma siparişindeki öğe kimliğiyle karşılaştırır. Öğe kimlikleri eşleştiği için iş akışı sorunsuz devam eder.

## **Sonuç:**

"Öğe Kimliği Karşılaştırması" iş akışı kartı, belgelerdeki öğe kimliklerinin satın alma siparişlerindekilerle uyumlu olmasını sağlar. Bu, öğe listelerindeki tutarsızlıkların önlenmesine yardımcı olur ve doğru öğelerin satın alma siparişine göre işlenmesini sağlar. Herhangi bir veya tüm durumlara göre karşılaştırma yapabilme özelliği farklı kullanım durumlarında esneklik sağlayarak satın alma iş akışlarının doğruluğunu ve verimliliğini artırır.

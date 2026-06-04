# Supplier on Invoice

<figure><img src="../../../../.gitbook/assets/image (276).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir faturadaki tedarikçi bilgilerini ilgili satınalma siparişindeki tedarikçi bilgileriyle karşılaştırmak için tasarlanmıştır. Kart, faturadaki tedarikçinin satınalma siparişindeki tedarikçiyle eşleşmesini sağlar. Bu karşılaştırma, sipariş için doğru tedarikçinin fatura kestiğini doğrulamaya yardımcı olur ve herhangi bir tutarsızlığa dayalı eylemleri tetikleyebilir.

## **Kartın Bileşenleri:**

1. **Operatör:**
   * **Açıklama**: Faturadaki tedarikçiyi satınalma siparişindeki tedarikçiye karşı karşılaştırma koşulunu tanımlar.
   * **Seçenekler**:
     * **Is**: Faturadaki tedarikçinin satınalma siparişindeki tedarikçiyle eşleşip eşleşmediğini kontrol eder.
     * **Is Not**: Faturadaki tedarikçinin satınalma siparişindeki tedarikçiyle eşleşmediğini garanti eder.

## **İşlevsellik:**

* **Koşul Değerlendirmesi:** Sistem, seçilen operatöre dayanarak faturadaki tedarikçiyi satınalma siparişindeki tedarikçiyle karşılaştırır. Karşılaştırma koşulu doğruysa (örn. tedarikçi gerektiği gibi aynı veya farklı ise), iş akışı buna göre ilerler.
* **Eylem Yürütme:**
  * **Doğru Koşul**: Koşul doğru olarak değerlendirilirse (örn. faturadaki tedarikçi satınalma siparişindeki tedarikçiyle eşleşirse), iş akışı herhangi bir hata tetiklemeden devam eder.
  * **Yanlış Koşul**: Koşul yanlış olarak değerlendirilirse (örn. faturadaki tedarikçi satınalma siparişindeki tedarikçiyle eşleşmezse), iş akışı devam etmez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, tedarikçilerin nasıl karşılaştırılacağını tanımlamak için uygun operatörü ("Is" veya "Is Not") seçer.

## **Örnek Senaryo:**

* Bir fatura "SUP123" kimlikli bir tedarikçi listeler ve ilgili satınalma siparişi de "SUP123"ü tedarikçi olarak listeler. "Is" operatörünü kullanarak, kart tedarikçileri karşılaştırır ve aynı olduklarını bulur, böylece iş akışı sorunsuz devam eder.

## **Sonuç:**

"Supplier Comparison" iş akışı kartı, satınalma siparişi için doğru tedarikçinin fatura kestiğini sağlar ve satınalma sürecindeki tutarsızlıkları ve hataları önlemeye yardımcı olur. Tedarikçi bilgilerini otomatik olarak doğrulayarak, kuruluşlar fatura onay süreçlerini kolaylaştırabilir ve tedarikçi faturalandırmasında dolandırıcılık veya hata riskini azaltabilir.

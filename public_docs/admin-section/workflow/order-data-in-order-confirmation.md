# Sipariş Onayındaki Sipariş Verileri

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu iş akışı kartı, bir sipariş onayı ile bir satın alma siparişi arasındaki belirli alanları — **Birim Fiyat**, **İndirim** veya **Miktar** — karşılaştırmak için tasarlanmıştır. Kararlaştırılan şartlarla tutarlılığı ve uyumluluğu sağlar. Karşılaştırma sonucuna bağlı olarak kart, koşul **doğru** veya **yanlış** olarak değerlendirildiğinde kullanıcıların seçilen bir alana belirtilen metni yazmasına olanak tanıyarak belge işlemeyi kolaylaştırır ve manuel müdahaleyi azaltır.

## **Kartın Bileşenleri**

1. **Sipariş Verileri**
   * **Açıklama:** Sipariş onayı ile satın alma siparişi arasında karşılaştırılacak alanı belirtir.
   * **Seçenekler:**
     * **Birim Fiyat**: Her iki belgedeki birim fiyatı karşılaştırır.
     * **İndirim**: İndirim yüzdesini veya değerini karşılaştırır.
     * **Miktar**: Sipariş edilen miktarı karşılaştırır.
2. **Operatör**
   * **Açıklama:** Karşılaştırma sırasında uygulanan koşulu tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Seçilen alandaki değerin sipariş onayı ile satın alma siparişi arasında eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠):** Seçilen alandaki değerin iki belge arasında farklı olmasını sağlar.
3. **Metin**
   * **Açıklama:** Koşul değerlendirmesi üzerine hedef alana yazılacak metni belirtir.
   * **Detay:** Bu metin özel notlar, durum güncellemeleri veya önceden tanımlanmış değerler içerebilir.
4. **Alan Adı**
   * **Açıklama:** Metnin yazılacağı alanı belirtir.
   * **Detay:** Hedef alan, sistemdeki mevcut düzenlenebilir alanlar arasından seçilir.
5. **Koşul Sonucu**
   * **Açıklama:** Karşılaştırma sonucuna bağlı olarak metnin ne zaman yazılacağını belirler.
   * **Seçenekler:**
     * **Doğru:** Karşılaştırma koşulu karşılanırsa metni yazar.
     * **Yanlış:** Karşılaştırma koşulu karşılanmazsa metni yazar.

## **İşlevsellik**

* **Karşılaştırma Değerlendirmesi:** Sistem, belirtilen operatörü kullanarak sipariş onayı ile satın alma siparişi arasındaki seçilen alanı karşılaştırır.
* **Eylem Yürütme:** Koşul **doğru** veya **yanlış** olarak değerlendirilirse, belirtilen metin belirlenen alana yazılır.

## **Kurulum ve Yapılandırma**

* Bu kartı kurmak için kullanıcılar önce karşılaştırılacak alanı seçer — **Birim Fiyat**, **İndirim** veya **Miktar**. Ardından, **eşittir** veya **eşit değildir** gibi karşılaştırma koşulunu tanımlamak için bir operatör seçerler. Kullanıcılar bir hedef alana yazılacak metni belirtir ve koşul sonucuna (**doğru** veya **yanlış**) bağlı olarak bu eylemin ne zaman gerçekleşmesi gerektiğini seçerler.

## **Örnek Senaryo**

* Bir sipariş onayı bir ürün için 50$ birim fiyat listelerken, satın alma siparişi 45$ bir fiyat belirtiyor. **Eşit Değildir (≠)** operatörünü kullanan kart, tutarsızlığı tanımlar ve koşul **doğru** olarak değerlendirildiğinde belirlenen bir alana "Fiyat Uyuşmazlığı" metnini yazar.

## **Sonuç**

"Sipariş Onayında [Birim Fiyat/İndirim/Miktar]" iş akışı kartı, belge tutarlılığını sağlamak için pratik bir çözüm sunar. Tutarsızlıkları otomatik olarak işaretleyerek ve belirtilen alanlara ilgili metni yazarak, sipariş yönetimi süreçlerinde verimliliği artırır ve hataları azaltır.

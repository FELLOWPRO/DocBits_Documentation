# Order Data in Order Confirmation

<figure><img src="../../../../.gitbook/assets/image (265).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu iş akışı kartı, bir sipariş onayı ile bir satınalma siparişi arasında belirli alanları — **Birim Fiyat**, **İndirim** veya **Miktar** — karşılaştırmak için tasarlanmıştır. Tutarlılığı ve üzerinde anlaşılan koşullara uyumu sağlar. Karşılaştırma sonucuna dayanarak, kart, koşul **doğru** veya **yanlış** olarak değerlendirildiğinde kullanıcıların seçilen bir alana belirtilen metni yazmasına olanak tanır ve belge işlemeyi kolaylaştırır ve manuel müdahaleyi azaltır.

## **Kartın Bileşenleri**

1. **Sipariş Verisi (Order Data)**
   * **Açıklama:** Sipariş onayı ile satınalma siparişi arasında karşılaştırılacak alanı belirtir.
   * **Seçenekler:**
     * **Birim Fiyat**: Her iki belgedeki birim fiyatı karşılaştırır.
     * **İndirim**: İndirim yüzdesini veya değerini karşılaştırır.
     * **Miktar**: Sipariş edilen miktarı karşılaştırır.
2. **Operatör**
   * **Açıklama:** Karşılaştırma sırasında uygulanan koşulu tanımlar.
   * **Seçenekler:**
     * **Eşittir (=):** Seçilen alandaki değerin sipariş onayı ile satınalma siparişi arasında eşleşip eşleşmediğini kontrol eder.
     * **Eşit Değildir (≠):** Seçilen alandaki değerin iki belge arasında farklı olduğunu garanti eder.
3. **Metin (Text)**
   * **Açıklama:** Koşul değerlendirmesi üzerine hedef alana yazılacak metni belirtir.
   * **Ayrıntı:** Bu metin özel notlar, durum güncellemeleri veya önceden tanımlanmış değerler içerebilir.
4. **Alan Adı (Field Name)**
   * **Açıklama:** Metnin yazılacağı alanı belirtir.
   * **Ayrıntı:** Hedef alan, sistemdeki kullanılabilir düzenlenebilir alanlardan seçilir.
5. **Koşul Sonucu (Condition Result)**
   * **Açıklama:** Karşılaştırma sonucuna dayanarak metnin ne zaman yazılması gerektiğini belirler.
   * **Seçenekler:**
     * **True:** Karşılaştırma koşulu karşılanırsa metni yazar.
     * **False:** Karşılaştırma koşulu karşılanmazsa metni yazar.

## **İşlevsellik**

* **Karşılaştırma Değerlendirmesi:** Sistem, belirtilen operatörü kullanarak sipariş onayı ile satınalma siparişi arasındaki seçilen alanı karşılaştırır.
* **Eylem Yürütme:** Koşul **doğru** veya **yanlış** olarak değerlendirilirse, belirtilen metin belirlenen alana yazılır.

## **Kurulum ve Yapılandırma**

* Bu kartı kurmak için, kullanıcılar önce karşılaştırılacak alanı seçer — **Birim Fiyat**, **İndirim** veya **Miktar**. Ardından, **eşittir** veya **eşit değildir** gibi karşılaştırma koşulunu tanımlamak için bir operatör seçerler. Kullanıcılar hedef alana yazılacak metni belirtir ve koşul sonucuna (**doğru** veya **yanlış**) dayanarak bu eylemin ne zaman gerçekleşeceğini seçer.

## **Örnek Senaryo**

* Bir sipariş onayı bir ürün için $50 birim fiyat listelerken, satınalma siparişi $45 fiyat belirtir. **Eşit Değildir (≠)** operatörünü kullanarak, kart tutarsızlığı tanımlar ve koşul **doğru** olarak değerlendirildiğinde belirlenen bir alana "Price Mismatch" metnini yazar.

## **Sonuç**

"\[Birim Fiyat/İndirim/Miktar] in Order Confirmation" iş akışı kartı, belge tutarlılığını sağlamak için pratik bir çözüm sunar. Tutarsızlıkları otomatik olarak işaretleyerek ve belirtilen alanlara ilgili metni yazarak, sipariş yönetimi süreçlerinde verimliliği artırır ve hataları azaltır.

# AI Calculation for Cost Increase Surcharges

<figure><img src="../../../../.gitbook/assets/image (309).png" alt="" width="563"><figcaption></figcaption></figure>

## Amaç:

**"AI Calculation for Cost Increase Surcharges"** iş akışı kartı, maliyet artışlarına göre ek ücret tutarlarını otomatik olarak hesaplamak için yapay zekayı kullanır. Tutarlı ve doğru ek ücret hesaplamaları sağlar, iş akışlarını kolaylaştırır ve manuel çabayı azaltır.

## Kartın Bileşenleri:

* **Maliyet Artış Faktörü (Cost Increase Factor)**
  * **Açıklama:** Ek ücreti hesaplamak için temel maliyete uygulanan çarpan veya yüzde.
  * **Ayrıntı:** Maliyet artışına göre ek ücret tutarını belirler (örn. %10 artış için 1.10 faktörü).
* **Temel Maliyet Alanı (Base Cost Field)**
  * **Açıklama:** Ek ücret hesaplamasının temeli olarak kullanılan orijinal maliyet değerini içeren alan.
  * **Ayrıntı:** Hesaplama sırasında referans için otomatik olarak seçilir veya iş akışı içinde tanımlanır.
* **Ek Ücret Alanı (Surcharge Field)**
  * **Açıklama:** Yapay zeka tarafından hesaplanan ek ücret değerinin depolandığı alan.
  * **Ayrıntı:** Bu alan, hesaplanan ek ücreti yansıtır ve onu daha fazla işleme veya raporlama için kullanılabilir hale getirir.

## İşlevsellik:

**Koşul Değerlendirmesi:**

* Kart yalnızca hem **"Where"** hem de **"And Bölümleri"** koşulları doğru olarak değerlendirilirse etkinleşir.
* Koşullardan biri yanlış olarak değerlendirilirse, hiçbir ek ücret hesaplaması yapılmaz.

**Yapay Zeka Odaklı Hesaplama:**

* Sistem, ek ücreti hesaplamak için **Maliyet Artış Faktörü**'nü **Temel Maliyet Alanı**'na uygular.
* Sonuç **Ek Ücret Alanı**'nda depolanır ve sonraki iş akışı adımları için erişilebilirliği sağlar.

## Sonuç:

**"AI Calculation for Cost Increase Surcharges"** iş akışı kartı, maliyet artışlarına göre ek ücretlerin uygulanmasını otomatikleştirir. Hassasiyet ve tutarlılık için yapay zekadan yararlanarak, bu kart manuel hesaplamaları ortadan kaldırır, verimliliği artırır ve otomatik iş akışlarında doğru maliyet yönetimini destekler.

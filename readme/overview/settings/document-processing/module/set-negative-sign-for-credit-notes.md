# Kredi Notları İçin Negatif İşaret Ayarla

### Genel Bakış

**Kredi Notları İçin Negatif İşaret Ayarla** (Set Negative Sign for Credit Notes) ayarı, **kredi notlarının** **negatif tutarlarla** kaydedilmesini sağlar. Bir kredi notu, bir faturanın bir kısmını geri alır veya iade eder; bu nedenle muhasebede değerleri toplamları azaltmalı, yani negatif olmalıdır. Bu ayar açık olduğunda DocBits bu negatif işareti otomatik olarak uygular.

Bu ayar **varsayılan olarak etkindir**.

### Ne işe yarar?

Bir belge **kredi notu** olarak tanındığında, DocBits işleme sırasında tutarlarını otomatik olarak negatif değerlere dönüştürür. Bu, para alanlarını etkiler; bunlara net tutarlar, vergi tutarları ve toplamlar dahildir (örneğin net tutar, vergi tutarı, toplam vergi tutarı, toplam net tutar ve toplam tutar).

* **Etkin (varsayılan)** — Kredi notu tutarları negatif değerler olarak kaydedilir (örneğin `150,00`, `-150,00` olur). Normal faturalar etkilenmez.
* **Devre dışı** — Tutarlar, işaret değişikliği olmadan belgeden okunduğu gibi tam olarak korunur.

{% hint style="info" %}
Bu yalnızca **kredi notu** olarak tanımlanan belgeler için geçerlidir. Normal faturalar her zaman değiştirilmeden bırakılır.
{% endhint %}

### Avantajlar

* **Doğru muhasebe**: Kredi notları bakiyeleri azaltır, bu nedenle negatif değerler muhasebe ve ERP sistemlerinizin beklediği şeydir.
* **Manuel düzenleme yok**: Ekibinizin her kredi notunda işareti elle çevirmesi gerekmez.
* **Tutarlılık**: Her kredi notu, kuruluşunuz genelinde aynı şekilde işlenir.

### Nasıl kullanılır

1. **Ayarlar**'a gidin.
2. **Belge İşleme**'yi seçin.
3. **Modül**'ü seçin.
4. **Belge Türü** bölümünü açın.
5. **Kredi Notları İçin Negatif İşaret Ayarla** seçeneğini bulun ve anahtarı açın veya kapatın.

### Bu özellik ne zaman kullanılır

* Muhasebe veya ERP sisteminiz kredi notlarının negatif tutarlarla gelmesini bekliyorsa **etkin bırakın** (en yaygın kurulum budur).
* Yalnızca alt sisteminiz işareti zaten kendisi işliyorsa veya kredi notu tutarlarının pozitif kalmasını bekliyorsa **devre dışı bırakın**.

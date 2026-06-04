# Field is

<figure><img src="../../../../.gitbook/assets/image (7) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, bir belge içindeki belirtilen bir alanın varlığına veya durumuna göre eylemleri otomatikleştirmek için tasarlanmıştır. Alanın boş, eksik veya dolu olup olmadığını değerlendirerek, iş akışlarının belgeleri hassasiyet ve doğrulukla ele almasını sağlar.

## **Kartın Bileşenleri:**

1. **Alan Adı (Field Name)**
   * **Açıklama:** Değerlendirilecek alanın adını belirtir.
   * **Ayrıntı:** Doğru alan algılaması sağlamak için bu, belgede kullanılan tam tanımlayıcıyla eşleşmelidir.
2. **Operatörler**
   * **Açıklama**: Alanın varlığına veya durumuna göre iş akışını tetikleyen koşulu tanımlar.
   * **Seçenekler**:
     * **Boş/Belgede Değil (Empty/Not in Document):** Alan ya belgede eksikse ya da mevcut ama boşsa iş akışı tetiklenir.
     * **Belgede/Boş Değil (In Document/Not Empty):** Alan belgede mevcutsa ve bir değer içeriyorsa iş akışı tetiklenir.

## **İşlevsellik:**

* **Durum Algılama:** Kart, varlığını ve durumunu değerlendirmek için belirtilen alanı izler.
* **Koşul Değerlendirmesi:**
  * Sistem, belirtilen alanın seçilen operatör tarafından tanımlanan durumda (Boş/Belgede Değil veya Belgede/Boş Değil) olup olmadığını değerlendirir.
*

    **Eylem Yürütme:**

    * **Boş/Belgede Değil Koşulu:** Alanın durumu bu koşulla eşleşirse (yani alan ya belgeden yoksa ya da mevcut ama boşsa), sistem ilişkili eylemleri başlatır. Bunlar, uyarılar oluşturma, belgeyi inceleme için işaretleme veya iş akışını durdurma içerebilir.
    * **Belgede/Boş Değil Koşulu:** Alanın durumu bu koşulla eşleşirse (yani alan belgede mevcutsa ve bir değer içeriyorsa), sistem ilişkili eylemleri tetikler. Bunlar, sonraki iş akışı adımlarını etkinleştirme, kayıtları güncelleme veya bildirimleri tetikleme içerebilir.

## **Kurulum ve Yapılandırma:**&#x20;

* Kullanıcılar, kullanılabilir belge alanları listesinden alanı seçer. Operatör, "Boş/Belgede Değil" veya "Belgede/Boş Değil" için açık seçenekler sunan bir açılır menü aracılığıyla seçilir.

## **Sonuç:**

"Field Presence and State Validation" iş akışı kartı, eksik veya dolu alanların doğru ele alınmasını sağlayarak belge işleme iş akışları için kritik bir araçtır. Alan durumlarına dayalı eylemleri otomatikleştirerek, bu kart veri bütünlüğünü artırır, hataları azaltır ve iş akışlarının sorunsuz ve verimli çalışmasını sağlar.

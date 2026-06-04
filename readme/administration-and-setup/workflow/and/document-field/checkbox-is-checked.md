# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu iş akışı kartı, ERP sisteminizdeki bir onay kutusunun durumuna (işaretli veya işaretsiz) göre eylemleri otomatikleştirmek için tasarlanmıştır. Onay kutusunun koşulunu değerlendirerek, belirli süreçlerin tetiklenmesini veya uygulama içinde belirli kuralların uygulanmasını kolaylaştırır.

## **Kartın Bileşenleri:**

* **Alan Adı (Field Name)**
  * **Açıklama:** Değerlendirilecek onay kutusu alanının adını belirtir.
  * **Ayrıntı:** Bu, sistemde kullanılan tam alan tanımlayıcısıyla eşleşmelidir. Hangi onay kutusunun durumunun izlendiğini belirler.
* **Boolean**
  * **Açıklama:** İş akışını tetikleyen koşulu tanımlar.
  * **Seçenekler:**
    * **True:** Onay kutusu işaretliyse iş akışı tetiklenir.
    * **False:** Onay kutusu işaretsizse iş akışı tetiklenir.

#### **İşlevsellik:**

* **Durum Algılama:** Kart, belirtilen onay kutusu alanının durumunu sürekli olarak izler.
* **Koşul Değerlendirmesi:** Sistem, onay kutusunun Boolean koşulu tarafından belirtilen durumda (işaretli veya işaretsiz) olup olmadığını kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    Onay kutusunun durumu belirtilen Boolean koşuluyla eşleşirse (işaretli için true veya işaretsiz için false), sistem ilişkili eylemleri başlatır. Bunlar, form alanlarını etkinleştirme veya devre dışı bırakma, bildirimleri tetikleme, iş akışlarını başlatma veya kayıtları güncelleme içerebilir.
  * **Yanlış Koşul:**\
    Onay kutusunun durumu koşulla eşleşmezse, iş akışı kurulumuna bağlı olarak alternatif eylemler gerçekleştirilebilir veya hiçbir eylem gerçekleştirilmez.

## **Kurulum ve Yapılandırma:**

* Kullanıcılar, kullanılabilir alanlar listesinden onay kutusu alanını seçerek ve Boolean koşulunu ayarlayarak kartı yapılandırır.&#x20;

## Sonuç:

"Checkbox Field Condition" iş akışı kartı, kullanıcı girdilerinin sonraki veri süreçlerini belirleyebildiği bir ERP sistemi içinde dinamik formları ve belgeleri yönetmek için temel bir araçtır. Bir onay kutusunun durumuna göre eylemleri otomatikleştirerek, bu kart iş akışı verimliliğini artırır ve sistem davranışlarının kullanıcı girdileriyle uyumlu olmasını sağlar. Bu kartın net belgelenmesi, kullanıcıların onu operasyonları içinde etkili bir şekilde uygulamasına yardımcı olur ve form davranışları ile süreç otomasyonları üzerinde daha iyi kontrol sağlar.



**Not: Her müşteride onay kutusu bulunmaz, ancak istenirse eklenebilir.**

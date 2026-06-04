# Assign Sequentially to User

<figure><img src="../../../../.gitbook/assets/image (9) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign Sequentially to User**" iş akışı kartı, belgelerin seçilen bir kullanıcıya ardışık bir şekilde atanmasını otomatikleştirir. Öncelik değeri atama sırasını belirler; daha düşük sayılar daha yüksek önceliği temsil eder.

## **Kartın Bileşenleri**

1. **Kullanıcı (User)**
   * **Açıklama**: Seçilen kullanıcıya, iş akışı dizisine göre belge atanır.
   * **Ayrıntı**: Atama için tüm kullanılabilir kullanıcıları listeleyen bir açılır menü.
2. **Öncelik (Değer)**
   * **Açıklama**: Kullanıcı için öncelik düzeyinin ayarlanabileceği sayısal bir giriş alanı.
   * **Ayrıntı**: Daha düşük sayılar daha yüksek önceliği ifade eder. Belgeler kullanıcılara öncelik artan sırasında atanır.

## **İşlevsellik**

* **Belge Ataması**:\
  Kart, öncelik düzeyini dikkate alarak belgeleri seçilen kullanıcıya ardışık olarak atar.\
  Birden fazla kullanıcı aynı önceliğe sahipse, belgeler kullanıcıların açılır menüde göründüğü sırada atanır.

## **Kurulum ve Yapılandırma**

1. **Assign the Document Sequentially** kartını iş akışınıza ekleyin.
2. **Kullanıcı** alanını yapılandırın:
   * Açılır menüden bir kullanıcı seçin.
3. **Öncelik (Değer)** alanını yapılandırın:
   * Atama önceliğini ayarlamak için sayısal bir değer girin.
4. Yapılandırmayı uygulamak için iş akışını kaydedin ve etkinleştirin.

## **Sonuç**

"Assign the Document Sequentially to User" iş akışı kartı, belgeleri önceliklendirilmiş bir dizide atayarak düzenli belge dağıtımını sağlar. Bu, görev yönetimini artırır ve işlemedeki gecikmeleri azaltır.

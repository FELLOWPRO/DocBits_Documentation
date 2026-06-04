# Assign Sequentially to User/Group

<figure><img src="../../../../.gitbook/assets/image (11) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

"**Assign the Document Sequentially to User/Group Based on Decision Table**" iş akışı kartı, karar tablosunun değerlendirmesine bağlı olarak belgeleri dinamik olarak bir kullanıcıya veya bir gruba atar. Bu, belgelerin önceden tanımlanmış kurallara göre uygun şekilde yönlendirilmesini sağlar.

## **Kartın Bileşenleri**

1. **Öncelik (Değer)**
   * **Açıklama**: Atamalar için öncelik düzeyini belirtir; daha düşük sayılar daha yüksek önceliği temsil eder.
   * **Ayrıntı**: Atama sırasını kontrol etmek için öncelik değerinin ayarlanabileceği sayısal bir giriş alanı.

## **İşlevsellik**

* **Karar Tablosu Değerlendirmesi**:\
  Karar tablosu, belgenin bir kullanıcıya mı yoksa bir gruba mı atanacağına karar vermek için önceden tanımlanmış koşulları değerlendirir.
* **Belge Ataması**:
  * Karar tablosu bir kullanıcı döndürürse, belge doğrudan o kullanıcıya atanır.
  * Karar tablosu bir grup döndürürse, belge belirtilen öncelik değerine uyularak gruba ardışık olarak atanır.

## **Kurulum ve Yapılandırma**

1. **Assign the Document Sequentially** kartını iş akışınıza ekleyin.
2. **Öncelik (Değer)** alanını yapılandırın:
   * Atama önceliğini ayarlamak için sayısal bir değer girin.
3. Yapılandırmayı uygulamak için iş akışını kaydedin ve etkinleştirin.

## **Sonuç**

"**Assign the Document Sequentially to User/Group Based on Decision Table**" iş akışı kartı, verimli ve dinamik belge yönlendirmesini sağlar. Karar tablosu mantığından ve öncelik değerlerinden yararlanarak, kart bir kullanıcıya veya bir gruba doğru atamayı kolaylaştırır ve belge iş akışlarını kolaylaştırır.

# Document Type Operation one of

<figure><img src="../../../../.gitbook/assets/userlmn_14ab8ac5e693d9bbe68d178795d12a9f (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu kart, belgeler üzerindeki eylemleri türlerine bağlı olarak yönetmek için tasarlanmıştır ve belirli iş akışlarını ya tetiklemek ya da engellemek için basit koşullu mantık (is/is not) kullanır. Bu, ERP sistemi içinde farklı türdeki belgelerin nasıl işleneceği üzerinde hassas kontrol sağlar.

## **Kartın Bileşenleri:**

1. **Operatör**
   * **Açıklama**: Belge türlerine uygulanan koşullu mantığı belirler.
   * **Seçenekler**:
     * **is**: Belgenin türü listedeki belirtilen türlerden biriyle eşleşirse işlem tetiklenir.
     * **is not**: Belgenin türü listelenen türlerden hiçbiriyle eşleşmezse işlem tetiklenir.
2. **Belge Türleri Listesi**
   * **Açıklama**: Koşulun uygulanacağı belge türlerinin bir listesini belirtir.
   * **Ayrıntı**: Bu, koşulun (is/is not) değerlendirileceği "Invoice", "Purchase Order" vb. gibi çeşitli belge türlerini içerir.

## İşlevsellik:

* **Koşul Değerlendirmesi:** Sistem, belge türünün belirtilen belge türleri listesine karşı operatör koşuluyla (is veya is not) eşleşip eşleşmediğini kontrol eder.
* **Eylem Yürütme:**
  * **Doğru Koşul:**\
    Belge türü belirtilen koşulu karşılarsa (listede is veya is not), iş akışı devam eder. Bu, belge onayları, belirli doğrulamalar veya yönlendirme eylemleri gibi süreçleri tetikleyebilir.
  * **Yanlış Koşul:**\
    Belge türü koşulu karşılamazsa, belgeyi reddetme veya iş akışını durdurma gibi alternatif eylemler yürütülür.

## Kurulum ve Yapılandırma:

* Kullanıcılar, belge türü alanını seçerek ve operatörü (is veya is not) tanımlayarak kartı yapılandırır. Ardından, karşılaştırılacak belge türleri listesini belirtirler. Kurulum basittir; alan ve operatör seçimi için açılır menüler ve belge türleri listesini girmek için bir alan içerir.

## Sonuç:

"Document Type Condition" iş akışı kartı, belge tabanlı işlemleri hassasiyet ve esneklikle yönetmede çok önemli bir rol oynar. Basit koşullu mantık kullanarak, belgelerin uygun şekilde işlenmesini sağlamaya yardımcı olur, verimliliği ve uyumluluğu artırır. Bu kartı net bir şekilde belgelemek, kullanıcıların onu nasıl etkili bir şekilde uygulayacağını ve kullanacağını anlamasına yardımcı olur ve onu ERP sisteminizin belgelerinin değerli bir parçası haline getirir.

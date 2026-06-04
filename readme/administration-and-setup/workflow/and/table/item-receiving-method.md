# Item Receiving Method

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

Bu DocBits kartı, bir veri kümesindeki öğelerin belirtilen bir teslim alma yöntemine sahip olup olmadığını kontrol eder. Kullanıcılar, seçilen bir koşula dayanarak veri kümesindeki **herhangi bir** öğeyi veya **tüm** öğeleri doğrulamayı seçebilir, bu da onu tedarik zinciri yönetimi veya envanter izleme gibi iş akışlarının öğe teslim alma yöntemlerine bağlı olduğu senaryolar için uygun kılar.

## **İşlevsellik:**

* **Teslim Alma Yöntemi Doğrulaması:** Bu kart, öğelerin teslim alma yöntemini belirtilen bir koşula karşı doğrular. Kullanıcılar, veri kümesindeki **herhangi bir** öğe veya **tüm** öğeler arasından seçim yapabilir ve koşulu **eşittir** veya **eşit değildir** olarak ayarlayabilir.
* **Öğe Seçimi:** Kullanıcılar şunları belirtebilir:
  * **Herhangi Bir Öğe:** En az bir öğe belirtilen teslim alma yöntemi koşulunu karşılarsa kart tetiklenir.
  * **Tüm Öğeler:** Yalnızca tüm öğeler belirtilen teslim alma yöntemi koşulunu karşılarsa kart tetiklenir.
* **Operatörler:** Koşulu tanımlamak için aşağıdaki operatörler kullanılabilir:
  * **Eşittir (=):** Teslim alma yönteminin belirtilen değerle eşleşip eşleşmediğini kontrol eder.
  * **Eşit Değildir (≠):** Teslim alma yönteminin belirtilen değerle eşleşmediğini garanti eder.

## **Kullanım:**

Bu kart, işleme, depolama veya sevkiyat gibi başka eylemlere izin vermeden önce öğe teslim alma yöntemlerini doğrulaması gereken depo yöneticileri, envanter koordinatörleri veya lojistik personeli için idealdir.

## **Örnek Senaryo:**

* Bir kullanıcı, **tüm öğelerin** teslim alma yönteminin **"Direct Delivery" değerine eşit** olup olmadığını kontrol etmek için kartı yapılandırır. Her öğe bu koşulu karşılarsa, iş akışı ilerler ve tüm öğelerin doğrudan teslimat için tasarlandığını onaylar.

"Receiving Method Validation" kartını kullanarak kuruluşlar, teslim alma protokollerine uyumu sağlayabilir, lojistik iş akışlarını iyileştirebilir ve belirli teslim alma yöntemlerine dayalı öğe işlemede doğruluğu koruyabilir.

# When

<figure><img src="../../../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>

#### İş Akışı Yapılandırmalarında "When" Bölümünü Anlamak

**"When" Bölümünün Amacı**

* Bir iş akışı yapılandırmasındaki "When" bölümü, belirli bir iş akışı eylemini başlatan tetikleme koşullarını tanımlar. Bu koşullar, ERP sistemi içindeki belge özellikleri veya kullanıcı etkinlikleriyle ilgili belirtilen ölçütlere dayanır.

**Nasıl Çalışır**

* Arayüzünüzde "When", kullanıcıların farklı tetikleme kartları seçebileceği bir başlangıç noktası olarak görünür. Her kart, sonraki eylemlerin ("And" bölümünde tanımlanan) hangi koşullarda yürütüleceğini belirtir.

**Belge Türü Koşul Kartları**

* Ekran görüntüsünde belge simgesiyle gösterilen kartlar, işlenmekte olan belgenin türüne göre iş akışlarını tetiklemek için kullanılan "Document Type" koşullarının çeşitlemeleridir. İşte gösterilen her koşul kartı türünün bir dökümü:
  * **Document type (Operator) one of (Type)**: Bu kart, bir belgenin türü, bir listedeki belirtilen türlerden biriyle eşleştiğinde bir eylemi tetikler. Operatör, kapsayıcı veya dışlayıcı koşullara olanak tanıyan "is" veya "is not" gibi seçenekler içerebilir.
  * **Document type (Operator) (Type)**: Bu daha basit varyant, tek bir belge türü koşuluna göre tetiklenir. Genellikle belge türünün belirli bir tür "is" veya "is not" olup olmadığını, birden fazla tür arasından seçim yapma seçeneği olmadan kontrol eder.
  *

**Celery Beat**

* Ekran görüntüsündeki saat simgesine sahip kart, tarih ve saate göre iş akışlarını tetiklemek için kullanılan bir "Celery Beat" koşuludur.

#### Bir "When" Tetikleme Kartı Ayarlama

1. **Koşul Türünün Seçimi**: Kullanıcılar, otomatikleştirmek istedikleri iş akışıyla ilgili bir koşul türü seçerek başlar. Bu durumda odak noktası belge türleridir.
2. **Operatörü Tanımlama**: Kullanıcılar, gerçek belge türlerini tanımlanan koşullarla karşılaştırma temelini belirleyen mantıksal operatörü — "is" veya "is not" gibi — belirlemelidir.
3. **Belge Türlerini Belirtme**: Karta bağlı olarak, kullanıcılar bu türlerdeki belgeler işlendiğinde iş akışını tetikleyecek bir veya birden fazla belge türü seçebilir.
4. **Tetikleyiciyi Sonlandırma**: Koşul ayarlandıktan sonra, iş akışında tanımlanan belirli eylemleri tetiklemenin temeli haline gelir. Bir belge ayarlanan koşulu karşılarsa, tanımlanan eylemler otomatik olarak başlatılır.

#### Pratik Uygulama

Pratikte, bu tetikleme kartları onaylar, bildirimler veya işlenen belgenin türüne bağlı herhangi bir prosedür gibi süreçleri otomatikleştirmek için çok önemlidir. Örneğin, bir belge türü bir "Fatura" "is" ise ve "When" kartında ayarlanan koşullarla eşleşirse, iş akışı belgeyi otomatik olarak ödeme işlemesine yönlendirebilir.

Bu kurulum, iş akışlarının yalnızca verimli olmasını değil, aynı zamanda kuruluşun özel operasyonel ihtiyaçlarına göre uyarlanmasını sağlar, manuel denetimi azaltır ve belge işleme süreçlerini hızlandırır.

Özetle, iş akışı yapılandırmanızın "When" bölümü, belirli, önceden tanımlanmış koşullara dayalı otomatik eylemler için zemin hazırlamakla ilgilidir. ERP sisteminizin işin ihtiyaçlarına dinamik olarak tepki vermesini sağlayan, hem üretkenliği hem de belge yönetiminde doğruluğu artıran güçlü bir araçtır.

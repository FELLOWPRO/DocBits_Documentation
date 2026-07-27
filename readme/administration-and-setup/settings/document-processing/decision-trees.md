# Karar Ağaçları

{% embed url="https://youtu.be/omFWSkSjlL0" %}
DocBits'te Karar Ağacı Nasıl Oluşturulur (Koşullar, Politikalar, Test Etme ve Dışa Aktarma)
{% endembed %}

## Genel Bakış

Karar Ağaçları, önceden tanımlanmış kurallara dayalı olarak otomatik yönlendirme ve karar verme sürecine olanak tanıyan güçlü bir özelliktir. Bu özellik, fiyat atama, miktar belirleme veya belge yönlendirme gibi doğru eylem yolunu belirlemek için çeşitli koşulların değerlendirilmesi gereken karmaşık ortamlarda özellikle kullanışlıdır.

#### Temel Bileşenler

* **Karar Ağacı Listesi**: Mevcut tüm karar ağaçlarının listelendiği ana arayüzdür. Her karar ağacı, `INVOICE` veya `QUOTE` gibi belirli bir belge türüyle ilişkilendirilebilir.
* **Karar Ağacı Tasarımcısı**: Bu arayüz, belirli koşullar karşılandığında uygulanacak kuralları, operatörleri ve eylemleri tanımlayabileceğiniz karar ağaçlarının oluşturulmasına ve düzenlenmesine olanak tanır.

## Karar Ağacı Arayüzü

#### Karar Ağacı Listesi

Karar Ağacı listesi, yapılandırılmış tüm karar ağaçlarını gösterir. Listeyi **Settings → Document Processing → Decision Trees** yolundan açın.

<figure><img src="../../../.gitbook/assets/decision_trees.png" alt="Karar Ağaçları listesi"><figcaption><p>Karar Ağaçları listesi</p></figcaption></figure>

Her girdi şunları gösterir:

| Sütun | Açıklama |
|--------|-------------|
| **Name** | Karar ağacının adı. Tasarımcıyı açmak için üzerine tıklayın. |
| **Document Type** | Ağacın uygulandığı belge türü (ör. `INVOICE`, `QUOTE`). |
| **Last Modified By** | Ağacı en son düzenleyen kullanıcı. |
| **Last Modified At** | Son değişikliğin zaman damgası. |
| **Actions** | Ağacı düzenlemek, kopyalamak, dışa aktarmak veya silmek için üç noktalı menü. |

#### Karar Ağacı Oluşturma

1. Sağ üst köşedeki **+ Add Decision Tree** öğesine tıklayın.
2. Bir **Name** girin ve **Document Type** öğesini seçin.
3. Koşulları, politikaları ve sonuçları tanımlamak için Karar Ağacı Tasarımcısı'nı (aşağıda) kullanın.

#### Karar Ağacı İçe Aktarma

Daha önce dışa aktarılmış bir karar ağacı dosyasını (JSON formatında) yüklemek için **Import Decision Tree** öğesine tıklayın. Bu, bir ağacı kuruluşlar veya ortamlar arasında kopyalamak için kullanışlıdır.

## Karar Ağacı Tasarımcısı

Karar Ağacı Tasarımcısı, kararların nasıl verileceğini yöneten kuralları yapılandırmanıza olanak tanır.

### **Karar Ağacı Tasarımcısı'nın Bileşenleri**

* **Rules**: Her kural koşullardan ve eylemlerden oluşur.
* **Select Source**: Bu açılır menü, değerlendirilecek kaynak alanı belirlemenize olanak tanır.
* **Select Operator**: Kaynak alana uygulanacak mantık operatörünü (ör. `<=`, `>=`, `=`, `!=`) tanımlar.
* **Result**: Koşullar karşılandığında gerçekleştirilmesi gereken sonucu veya eylemi tanımlar.
* **Add New Row**: Karar ağacına ek kurallar eklemenize olanak tanır.

### Karar Ağacı Yapılandırması Örneği

Bu karar ağacı, **Total Amount** alanını değerlendirir ve önceden tanımlanmış koşullara göre farklı gruplara atar. Her kural, toplam tutarı belirli bir değerle karşılaştırır ve hangi koşulun doğru olduğuna bağlı olarak, ilgili **Group** döndürülür.

<figure><img src="../../../.gitbook/assets/decision_tree_example_total_amount.png" alt="Karar Ağacı Örneği Toplam Tutar"><figcaption></figcaption></figure>

Bu karar ağacı, hangi grubun atanacağını belirlemek için iki temel koşulu değerlendirir: **Total Amount** ve **Warehouse Status**. Ağaç, hangi grubun döndürüleceğini tanımlamak için toplam tutara dayalı eşik değerleri kullanır ve deponun "Warehouse Main", "Warehouse Sub" veya "Not Warehouse Main" olarak belirlenip belirlenmediğine dair ek bir ayrım yapar.

<figure><img src="../../../.gitbook/assets/decision_tree_example_warehouse_status.png" alt="Karar Ağacı Örneği Depo Durumu"><figcaption></figcaption></figure>

Her kural sırayla değerlendirilir.

## Karar Ağacı Politikası

Karar Ağacı Politikası, bir karar ağacındaki birden çok kuralın nasıl işleneceğini tanımlar. Çeşitli politikalar arasından seçim yapabilirsiniz:

* [Eşsiz](decision-trees/unique-policy.md)
* [Birinci](decision-trees/first-policy.md)
* [Öncelik](decision-trees/priority-policy.md)
* [Topla (Toplam)](decision-trees/collect-sum-policy.md)
* [Topla (Min/Maksimum/Say)](decision-trees/collect-min-max-count-policy.md)
* [Kural Sırası](decision-trees/rule-order-policy.md)
* [Herhangi](decision-trees/any-policy.md)
* [Birinci ve Bitişik](decision-trees/first-and-adjacent-policy.md)

## **Karar Ağacını Test Etme**

**Genel Bakış:**
Karar ağacı tasarımcısı, yapılandırılan kuralların mantığını doğrulamak için bir test özelliği içerir. Bu özellik, kullanıcıların seçili alanlar için belirli girdi değerleri sağlayarak karar ağacını test etmesine olanak tanır.

**Test Özelliğini Kullanma Adımları:**

1.  **Test Düğmesini Bulun:**

    * Karar ağacı tasarımcısında **Test** düğmesini bulun.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_button.png" alt="Karar Ağacı Test Düğmesi" width="563"><figcaption></figcaption></figure>
2.  **Test Açılır Penceresini Açın:**

    * **Test** düğmesine tıklayın.
    * Karar ağacında kullanılan ölçütlere karşılık gelen girdi alanları sağlayan bir açılır pencere görünür.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_popup.png" alt="Karar Ağacı Test Açılır Penceresi" width="421"><figcaption></figcaption></figure>
3. **Girdi Değerleri Sağlayın:**
   *   Gerçek dünya senaryosunu simüle etmek için girdi alanlarına değerler girin.

       <figure><img src="../../../.gitbook/assets/decision_tree_test_input.png" alt="Karar Ağacı Test Girdisi" width="428"><figcaption></figcaption></figure>
4.  **Sonuçları Değerlendirin:**

    * Girdileri girdikten sonra, ağaç bunları seçilen politikaya göre işler.
    * Sistem, sağlanan girdilerle eşleşen kuralı/kuralları vurgular.

    <figure><img src="../../../.gitbook/assets/decision_tree_test_result.png" alt="Karar Ağacı Test Sonucu" width="563"><figcaption></figcaption></figure>
5. **Eşleşme Olmaması Durumunda Geri Bildirimi İnceleyin:**
   * Hiçbir kural vurgulanmazsa, sistem hiçbir kuralın neden eşleşmediğini açıklayan geri bildirim görüntüler.
   * Girdileri ayarlamak veya ağacın yapılandırmasını olası sorunlar açısından gözden geçirmek için bu geri bildirimi kullanın.

## Dışa Aktarma ve Kaydetme

* **Save**: Karar ağacının mevcut yapılandırmasını kaydeder.
* **Export**: Karar ağacı yapılandırmasını dışa aktarmanıza olanak tanır; bu yapılandırma daha sonra başka bir ortama içe aktarılabilir veya yedekleme amacıyla kullanılabilir.

## Kullanım Senaryoları

* **Onay iş akışları** — faturaları tutar eşiklerine göre farklı onaylayıcılara yönlendirin (örneğin, 10.000'in üzerindeki tutarlar yönetici onayı gerektirir).
* **Doğrulama kuralları** — alan değerlerini otomatik olarak doğrulayın ve yapılandırılmış ölçütleri karşılamayan belgeleri işaretleyin.
* **Sıralı atama** — koşullara göre belgeleri belirli bir sırada kullanıcılara atayın.

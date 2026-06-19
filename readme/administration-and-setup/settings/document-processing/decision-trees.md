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

### **1. Benzersiz Politika (Unique Policy)**

Yalnızca tek bir kuralın eşleşmesini sağlar. Birden çok kural eşleşirse, karar ağacı false döndürür.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)
* **Kural 3**: Total Amount <= 5000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 3000 (eşleşir)

Birden çok kural eşleştiği için (**Kural 2**, **Kural 3**, **Kural 4**, **Kural 5**), karar ağacı **false** döndürür çünkü **Benzersiz** politika yalnızca bir kuralın eşleşebilmesini sağlar.

### **2. İlk Politika (First Policy)**

İlk eşleşen kural uygulanır ve sonraki kurallar değerlendirilmez.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir) → Karar ağacı sonraki kuralları değerlendirmeyi durdurur ve **GROUP_2** uygular.

### **3. Öncelik Politikası (Priority Policy)**

Bu seçeneği seçmek, her kural için öncelikler belirlemenize olanak tanır. Seçilen sayı ne kadar düşükse, öncelik o kadar yüksektir (yani öncelik 1 en yüksek önceliğe sahiptir). Kurallar öncelik sıralarına göre değerlendirilir. En yüksek öncelikli eşleşen kural uygulanır.

**Örnek:**

<table><thead><tr><th width="137">Kural</th><th width="110">Öncelik</th><th width="268">Koşul</th><th>Döndürülen Grup</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

Öncelik **5, 4, 3, 2, 1** sırasına göre uygulandığından, en yüksek öncelikli eşleşen kural **Kural 5** (**GROUP_5**) olur. Karar ağacı **GROUP_5** döndürür çünkü **Kural 5** en yüksek önceliğe (öncelik 1) sahiptir.

### **4. Topla (sum) Politikası (Collect (sum) Policy)**

Bu politika, eşleşen tüm kuralları toplar ve sonuçları toplamaya alır. Yalnızca **Return Type Value** için çalışır.

**Örnek:**

| Kural | Koşul                | Döndürülen Değer |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

**Total Amount = 3500** girdi değeri için, kuralların değerlendirmesi şu şekilde olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir, Döndürülen Değer = 3)
* **Kural 4**: Total Amount <= 4000 (eşleşir, Döndürülen Değer = 4)
* **Kural 5**: Total Amount <= 5000 (eşleşir, Döndürülen Değer = 5)

**Topla (sum)** politikası uygulandığından, eşleşen kuralların **Döndürülen Değerlerini** toplarız; bunlar **3, 4, 5** değerleridir.

**Bu değerleri toplamak** şunu verir:

* 5 + 4 + 3 = **12**

Böylece karar ağacı tarafından döndürülen sonuç, eşleşen tüm döndürülen değerlerin toplamı olan **12** olur.

### **5. Topla (min/maks/sayım) Politikası (Collect (min/max/count) Policy)**

Bu politika, eşleşen tüm kuralları toplar ve ya **minimum**, **maksimum** seçer ya da oluşumları **sayar**. Yalnızca **Return Type Value** için çalışır.

**Örnek:**

| Kural | Koşul                | Döndürülen Değer |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. **Topla (min)** seçeneği seçilirse, sonuç eşleşen kuralların **Döndürülen Değerlerinin** **minimumunu** döndürür.
   * **Total Amount = 3500** girdi değeri için, kuralların değerlendirmesi şu şekilde olur:
     * **Kural 1**: Total Amount <= 1000 (eşleşmez)
     * **Kural 2**: Total Amount <= 2000 (eşleşmez)
     * **Kural 3**: Total Amount <= 3000 (eşleşir, Döndürülen Değer = 3)
     * **Kural 4**: Total Amount <= 4000 (eşleşir, Döndürülen Değer = 4)
     * **Kural 5**: Total Amount <= 5000 (eşleşir, Döndürülen Değer = 5)
   * **Eşleşen kurallar** Kural 3, Kural 4 ve Kural 5 olup, **Döndürülen Değerleri** **3, 4 ve 5**'tir.
   * **Topla (min)** politikası uygulandığından, sonuç **minimum değer** olan **3** olur.
   * **Sonuç**: **3**
2. **Topla (maks)** seçeneği seçilirse, sonuç eşleşen kuralların **Döndürülen Değerlerinin** **maksimumunu** döndürür.
   * Yukarıdaki aynı değerlendirme için sonuç şu olur:
   * **Sonuç**: **5**
3. **Topla (sayım)** seçeneği seçilirse, sonuç **eşleşen kuralların sayısını** sayar.
   * Yukarıdaki aynı değerlendirme için sonuç şu olur:
   * **Sonuç**: **3** (3 kural eşleştiği için).

### **6. Kural Sırası Politikası (Rule Order Policy)**

Bu politika, kuralları karar ağacında göründükleri sırayla uygular ve ilk eşleşen kuralın sonucunu döndürür.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Girdi değerinin **Total Amount = 3500** olduğu göz önüne alındığında, kuralların değerlendirmesi şu şekilde olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

**Kural Sırası** altında, ağaç kuralları listelendikleri sırayla işler. Dolayısıyla eşleşen kurallar şunlar olur:

* **Kural 3**: GROUP_3
* **Kural 4**: GROUP_4
* **Kural 5**: GROUP_5

**Sonuç**: **GROUP_3**, **GROUP_4**, **GROUP_5**

### **7. Herhangi Politika (Any Policy)**

Birden çok kural doğru olabilir, ancak bu kuralların sonucu aynı olmalıdır.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Toplam tutar **2500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

**Herhangi** politikasının uygulanması için, eşleşen tüm kuralların aynı **Döndürülen Grup** değerini döndürmesi gerekir. Gruplar farklı kurallar arasında eşleşmediğinden, sonuç **false** olur.

### **8. İlk ve Bitişik Politika (First & Adjacent Policy)**

Doğru olan ilk kurala bitişik olan kuralın sonucunu seçer.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)

**Kural 2** eşleşen ilk kural olduğundan, **İlk ve Bitişik** politikası **Kural 3**'ün sonucunu uygular: **GROUP_3**.

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

# Barkod Atama

### Genel Bakış

**Barkod Atama** (Barcode Assignment) ayarı, **belge doğrulama ekranına** bir barkod aracı ekler. Bir belgede bulunan barkodları ve QR kodlarını okur ve **değerlerini belgenin alanlarına atamanıza** olanak tanır — örneğin bir sipariş, referans veya irsaliye numarasını yazmak yerine bir barkoddan doldurmak gibi.

Bu ayar **varsayılan olarak devre dışıdır**.

### Etkinleştirdiğinizde ne elde edersiniz

Ayar etkinleştirildiğinde, **doğrulama ekranının** (`/field_validation_v1/…`) sağ tarafındaki araç çubuğunda yeni bir **barkod düğmesi** (QR kod simgesi) görünür. Bu düğme, tüm özelliğin giriş noktasıdır — ayar olmadan simge gizli kalır.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_icon.png" alt="Doğrulama araç çubuğundaki barkod (QR kod) simgesi"><figcaption><p>Ayar etkinleştirildiğinde, barkod simgesi doğrulama araç çubuğunda görünür.</p></figcaption></figure>

İşte simge, doğrulama ekranında, incelenen belgenin yanındaki bağlamıyla:

<figure><img src="../../../../.gitbook/assets/barcode_assignment_validation_screen.png" alt="Barkod simgesinin bulunduğu doğrulama ekranı"><figcaption><p>Doğrulama ekranı — barkod simgesi (vurgulanmış, sağdaki araç çubuğu) yalnızca Barkod Atama etkinleştirildiğinde gösterilir.</p></figcaption></figure>

### Barkodlar nasıl okunur

DocBits, barkodları belge işleme sırasında algılar ve kodu çözülmüş değerlerini atama için sunar. Tek bir belge birden çok barkod türü taşıyabilir — örneğin bir **QR kod**, bir **Code 128** ve bir **EAN-13** — her biri sipariş numarası, fatura numarası veya tedarikçi GLN'si gibi farklı bir değer kodlar.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_demo_invoice.png" alt="Birden çok barkod türü taşıyan örnek fatura"><figcaption><p>Üç barkod türü taşıyan örnek bir DocBits demo faturası (QR kod → sipariş numarası, Code 128 → fatura numarası, EAN-13 → tedarikçi GLN'si), her biri bir alana atayabileceğiniz bir değeri kodlar.</p></figcaption></figure>

{% hint style="info" %}
Hangi barkod türlerinin algılanacağı, **Bar-Code / QR Code Extraction** (`Barcode Extraction Types`) ayarıyla denetlenir. İletişim kutusunda *“no barcodes extracted found”* görünüyorsa, barkod çıkarımının etkin olduğundan ve beklenen türlerin (ör. `QRCODE`, `CODE128`, `EAN13`) seçili olduğundan emin olun.
{% endhint %}

### Barkod Atama iletişim kutusunu kullanma

1. **Doğrulama ekranında** bir belge açın.
2. Sağdaki araç çubuğunda **barkod simgesine** tıklayın.
3. **Barkod Atama** iletişim kutusu, DocBits'in belgede algıladığı her barkodu `Barcode <n> : <değer>` biçiminde listeler.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_dialog.png" alt="Algılanan barkodları listeleyen Barkod Atama iletişim kutusu"><figcaption><p>Barkod Atama iletişim kutusu, algılanan her barkodu hedef alanı seçmek için bir açılır listeyle birlikte listeler.</p></figcaption></figure>

4. Her barkod için açılır listesini açın ve değerin gideceği alanı seçin.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_options.png" alt="Bir barkod için hedef alanın seçilmesi"><figcaption><p>Her barkod herhangi bir belge alanına atanabilir — ör. Sipariş numarası, Fatura numarası, Tedarikçi kimliği.</p></figcaption></figure>

5. Bir alan seçer seçmez, o alan barkodun değeriyle doldurulur.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_field_mapped.png" alt="Sipariş numarası alanına atanmış barkod"><figcaption><p>Bir alan seçtikten sonra (burada Sipariş numarası), alan barkod değeriyle doldurulur.</p></figcaption></figure>

### Nasıl etkinleştirilir

1. **Ayarlar**'a gidin.
2. **Belge İşleme**'yi seçin.
3. **Modül**'ü seçin.
4. **Belge Türü** bölümünü açın.
5. **Barkod Atama** seçeneğini bulun ve anahtarı açın.

<figure><img src="../../../../.gitbook/assets/barcode_assignment_toggle.png" alt="Barkod Atama anahtarı"><figcaption><p>Ayarlar → Belge İşleme → Modül altındaki Barkod Atama anahtarı.</p></figcaption></figure>

### Avantajlar

* **Daha hızlı, hatasız giriş**: Değerleri elle okuyup yazmak yerine doğrudan bir barkoddan alın.
* **Daha az yazım hatası**: Taranan bir değer, barkodda kodlanmış olanla tamamen aynıdır.
* **Kontrol sizde**: Doğrulama sırasında hangi barkodun hangi alana gideceğine siz karar verirsiniz.

### Bu özellik ne zaman kullanılır

* **Barkodlu belgeler**: Belgeleriniz, değerleri belirli alanlara ait olan barkodlar/QR kodları içerdiğinde (ör. sipariş veya referans numaraları).
* **Manuel doğrulama akışları**: Bir kişi belgeleri incelediğinde ve alanları barkodlardan hızlıca doldurmak istediğinde.
* Belgelerinizde kullanılabilir barkod yoksa veya yalnızca otomatik barkod/QR **çıkarımına** ihtiyacınız varsa **devre dışı bırakın**.

{% hint style="info" %}
**Bu, bir barkod/QR değerini okumak ve doğrulama sırasında bir alana atamak içindir.** Ödeme kodlarından (Swiss QR Bill veya GiroCode gibi) yapılandırılmış verilerin otomatik olarak çıkarılması — ve çok sayfalı bir dosyanın barkod ayırıcı sayfalarda bölünmesi — **farklı** bir ayar olan **Bar-Code / QR Code Extraction** tarafından yönetilir.
{% endhint %}

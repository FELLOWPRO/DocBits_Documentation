# Barkod Atama

### Genel Bakış

**Barkod Atama** (Barcode Assignment) ayarı, **belge doğrulama ekranına** bir barkod aracı ekler. Bir belgede bulunan barkodları ve QR kodlarını okur ve **değerlerini belgenin alanlarına atamanıza** olanak tanır — örneğin bir referans, sipariş veya irsaliye numarasını yazmak yerine bir barkoddan doldurmak gibi.

Bu ayar **varsayılan olarak devre dışıdır**.

### Ne işe yarar?

Bu ayar etkinleştirildiğinde, bir belgeyi doğrularken araç çubuğunda küçük bir **barkod düğmesi** (QR kod simgesi) görünür. Buna tıklamak, DocBits'in belgede bulduğu barkodları gösterir ve her birini bir alana eşleyebilirsiniz. Alan daha sonra barkoddan okunan değerle doldurulur.

* **Etkin** — Barkod düğmesi doğrulama ekranında gösterilir. Belgedeki barkodları okuyabilir ve değerlerini alanlara atayabilirsiniz.
* **Devre dışı** — Düğme gizlenir ve doğrulama sırasında barkod değerleri atama için sunulmaz.

{% hint style="info" %}
**Bu, bir barkod/QR değerini okumak ve doğrulama sırasında bir alana atamak içindir.** Ödeme kodlarından (Swiss QR Bill veya GiroCode gibi) yapılandırılmış verilerin otomatik olarak çıkarılması — ve çok sayfalı bir dosyanın barkod ayırıcı sayfalarda bölünmesi — **farklı** bir ayar olan **Bar-Code / QR Code Extraction** tarafından yönetilir.
{% endhint %}

### Avantajlar

* **Daha hızlı, hatasız giriş**: Değerleri elle okuyup yazmak yerine doğrudan bir barkoddan alın.
* **Daha az yazım hatası**: Taranan bir değer, barkodda kodlanmış olanla tamamen aynıdır.
* **Kontrol sizde**: Doğrulama sırasında hangi barkodun hangi alana gideceğine siz karar verirsiniz.

### Nasıl kullanılır

1. **Ayarlar**'a gidin.
2. **Belge İşleme**'yi seçin.
3. **Modül**'ü seçin.
4. **Belge Türü** bölümünü açın.
5. **Barkod Atama** seçeneğini bulun ve anahtarı açın.
6. Ardından bir belgeyi doğrularken araç çubuğundaki **barkod düğmesine** tıklayın ve algılanan barkod değerlerini ilgili alanlara atayın.

### Bu özellik ne zaman kullanılır

* **Barkodlu belgeler**: Belgeleriniz, değerleri belirli alanlara ait olan barkodlar/QR kodları içerdiğinde (ör. sipariş veya referans numaraları).
* **Manuel doğrulama akışları**: Bir kişi belgeleri incelediğinde ve alanları barkodlardan hızlıca doldurmak istediğinde.
* Belgelerinizde kullanılabilir barkod yoksa veya yalnızca otomatik barkod/QR **çıkarımına** ihtiyacınız varsa **devre dışı bırakın**.

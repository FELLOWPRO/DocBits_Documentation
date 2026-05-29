# Barkod Atama

### Genel Bakış

**Barkod Atama** (Barcode Assignment) ayarı, DocBits'in **bir dosyayı tek tek belgelere ayırmak için içindeki barkodları kullanmasına** olanak tanır. Bu, birden çok belge tek bir büyük PDF'e birlikte taranırken ve bir barkod bir belgenin nerede bitip diğerinin nerede başladığını işaretlerken kullanışlıdır.

Bu ayar **varsayılan olarak devre dışıdır**.

### Ne işe yarar?

Bu ayar etkinleştirildiğinde, DocBits gelen çok sayfalı bir dosyada barkodları arar ve dosyayı işaretlenen konumlarda ayrı belgelere böler. Ortaya çıkan her belge daha sonra ayrı ayrı işlenir.

* **Etkin** — DocBits barkodları algılar ve birleştirilmiş bir dosyayı bunlara göre otomatik olarak tek tek belgelere ayırır.
* **Devre dışı** — Dosya tek bir belge olarak işlenir; barkodlar bölmek için kullanılmaz.

{% hint style="info" %}
Burada söz konusu olan, barkodlara göre sayfaların **bölünmesi ve atanmasıdır**. Bir barkodta kodlanmış verilerin okunması (örneğin ödeme QR kodları için) ayrı olarak **Bar-Code / QR Code Extraction** altında ele alınır.
{% endhint %}

### Avantajlar

* **Daha hızlı toplu tarama**: Her belgeyi tek tek taramak yerine, aralarına barkod sayfaları koyarak bütün bir belge yığınını tek seferde tarayın.
* **Daha az manuel ayıklama**: DocBits tek tek belgeleri sizin için oluşturur, böylece kimsenin PDF'i elle bölmesi gerekmez.
* **Daha az hata**: Belgeler her seferinde tam olarak işaretlenen konumlarda ayrılır.

### Nasıl kullanılır

1. **Ayarlar**'a gidin.
2. **Belge İşleme**'yi seçin.
3. **Modül**'ü seçin.
4. **Belge Türü** bölümünü açın.
5. **Barkod Atama** seçeneğini bulun ve anahtarı açın.

### Bu özellik ne zaman kullanılır

* **Yüksek hacimli tarama**: Birçok belgeyi birlikte tararken ve aralarında barkodlu ayırıcı sayfalar kullanırken.
* **Karma yığınlar**: Tek bir gelen dosya, ayrı ayrı işlenmesi gereken birden çok farklı belge içerdiğinde.
* Belgeleriniz her zaman ayrı dosyalar olarak geliyorsa **devre dışı bırakın** — bu durumda bölme gerekmez.

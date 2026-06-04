# Düğümler

Gelişmiş İş Akışı, kenarlarla birbirine bağlanan **düğümlerden** oluşan bir grafiktir. Düğümleri **+ Add** menüsünden (veya tuvale sağ tıklayarak) eklersiniz ve yürütme akışını tanımlamak için bunları birbirine bağlarsınız.

<figure><img src="../../../.gitbook/assets/workflow_advanced_add_menu.png" alt="Kullanılabilir düğüm türlerini gösteren düğüm ekleme menüsü"><figcaption><p><strong>+ Add</strong> düğüm menüsü — kullanılabilir düğüm türleri.</p></figcaption></figure>

## Düğüm türleri

- **Start** — iş akışının giriş noktası. Otomatik olarak eklenir; her akış buradan başlar.
- **When** — bir tetikleyici kartı, Standart oluşturucudakiyle aynıdır.
- **And** — bir koşul kartı. Doğru veya yanlış olarak değerlendirilir ve akışı dallandırabilir.
- **Then** — iş yapan bir eylem kartı (alanları ayarla, görevler oluştur, API'leri çağır, …).
- **Wait ALL** — devam etmeden önce *tüm* gelen dalların tamamlanmasını bekler.
- **Wait ANY** — *herhangi* bir gelen dal tamamlanır tamamlanmaz devam eder.
- **OR** — akışı alternatif yollara dallandırır.
- **Note** — tuval üzerinde serbest metin açıklaması; yürütmeyi etkilemez.

**When / And / Then** düğümleri, [Kartlar](../cards-overview.md) bölümünde açıklanan kartların tam olarak aynısını kullanır.

## Düğümleri bağlama

Düğümler **renkli kenarlarla** birbirine bağlanır. Bir bağlantı oluşturmak için bir düğümün **sağ** tarafındaki bir tutamaçtan, başka bir düğümün **sol** tarafındaki giriş tutamacına sürükleyin. Her renk farklı bir yürütme sonucunu gösterir:

- **Success** (mavi) — bir düğüm başarıyla tamamlandığında izlenen varsayılan yol. Tüm düğüm türlerinde kullanılabilir.
- **Failed Condition** (turuncu) — bir koşul yanlış olarak değerlendirildiğinde izlenir. **And** (koşul) düğümlerinde kullanılabilir.
- **Error** (kırmızı) — bir düğüm yürütme sırasında bir hatayla karşılaştığında izlenir. **And** ve **Then** (eylem) düğümlerinde kullanılabilir.

## Yürütme yolu vurgulama

Yürütme yolunu görmek için herhangi bir düğüme tıklayın. Ona giden tüm düğümler ve ondan sonra gelen tüm düğümler vurgulanır — diğer her şey soluklaştırılır. **Wait ALL** düğümleri için, geçidin devam etmeden önce tam olarak neyi beklediğini görebilmeniz için her gelen dal gösterilir.

## Sonraki adımlar

- [Değişkenler](variables.md) ile düğümler arasında veri aktarın.
- Akışınızı [Doğrulama ve Test](validation-and-testing.md) ile kontrol edin ve çalıştırın.

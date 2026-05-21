# Tam Metin Arama Ayarları

<figure><img src="../../../.gitbook/assets/fulltext_search_settings.png" alt="Tam Metin Arama Ayarları"><figcaption><p>Tam Metin Arama Ayarları — „Modül Gerekli" Diyaloğu</p></figcaption></figure>

Tam Metin Arama Ayarları, DocBits'in neyi indekslediğini ve bu içeriğin belgeler, ERP ana verileri ve şablonlar arasında nasıl aranabilir hale geldiğini kontrol eder. Ayarlar sayfası yalnızca **Tam Metin Arama modülü** etkin olduğunda açılır — kullanıcıya yönelik sorgu dili için [Tam Metin Arama](../document-processing/module/fulltext-search.md)'ya bakın.

## Önkoşullar

Tam Metin Arama modülü, **Ayarlar → Belge İşleme → Modül → Panolar → Tam metin arama**'da etkinleştirilmelidir. Modül etkin değilse, bir diyalog şunları sunar:

* **Modüllere git** — Yapılandırmayı incelemek için Modül ayarları sayfasını açın.
* **Şimdi etkinleştir** — Tam Metin Arama modülünü doğrudan etkinleştirin (bir DocSearch aboneliği başlatır).

Ayarlar sayfasının kendisi, modül etkin olduğunda erişilebilir hale gelir.

## Sayfa düzeni

Ayarlar sayfası, her biri Tam Metin Arama'nın indeksleyebileceği farklı bir içerik türünü kapsayan üç sekmeye ayrılmıştır.

### „Belgeler" sekmesi

Belgeler sekmesi, işlenmiş belgelerin indekslenmesiyle ilgili her şeyi kapsar:

* **İndeksleme istatistikleri** — indekslenmiş ve bekleyen belgelerin toplamları, isteğe bağlı yenilenir.
* **Vektör tercihleri** — belgeler için vektör indekslemenin metin indeksiyle paralel çalışıp çalışmayacağına karar veren kuruluş düzeyinde üç anahtar. Vektör indeksleme, `vector:` sorgu modunu ve „Benzerleri bul" özelliğini besler.
* **Yeniden indeksleme eylemleri** — tam veya artımlı bir yeniden indeksleme başlatın. Yeniden indeksleme çalışırken canlı ilerlemeyi (dakikada belge, tahmini kalan süre), mevcut akış durumunu ve son hatayı (varsa) görürsünüz.
* **Senkronizasyon tanılama** — indeksin altta yatan belge deposundan senkronize görünmediği durumlar için isteğe bağlı tanılama.

<mark>Yeniden indeksleme yıkıcı değildir — yeni indeks oluşturulurken mevcut arama çalışmaya devam eder.</mark>

### „ERP" sekmesi

ERP sekmesi, ERP ana verilerinin — tedarikçiler, müşteriler, ürünler ve benzer varlıklar — indekslenmesini kontrol eder. Her varlığın kendi anahtarı vardır:

* **İndeksleme** — varlığı metinsel olarak indeksler, böylece panodan aranabilir.
* **Vektör** — varlığı vektörel olarak indeksler, böylece semantik sorgularla eşleştirilebilir.

Aynı açık/kapalı durumu tüm varlıklara aynı anda uygulamak için listenin üst kısmındaki **Tümünü aç/kapat** eylemini kullanın. İndeksleme arka planda başlar; her satırdaki bir gösterge devam ettiğinde gösterir.

### „Şablonlar" sekmesi

Şablonlar sekmesi, Tam Metin indeksinin bildiği şablon sürümlerini listeler. Yeniden dağıtımdan sonra bağımlı olduğunuz şablon sürümlerinin indekste bulunduğunu doğrulamak için bu görünümü kullanın.

## Neler indekslenir

Etkinleştirildikten ve yapılandırıldıktan sonra Tam Metin Arama, kullanıcıların şunları yapmasını sağlar:

* Tüm belge içeriğinde arama (yalnızca meta veri alanlarında değil).
* Yüklenen dosyalarda yer alan metne göre belge bulma.
* Hassas sorgular için gelişmiş arama operatörleri kullanma.
* Arama sonuçlarına doğrudan panodan erişme.
* Vektör indeksleme o içerik türü için etkin olduğunda semantik arama kullanma (`vector:` öneki).

Sorgu dilinin tam referansı — aralık sorguları, akıllı filtreler ve AI arama modu dahil — için [Tam Metin Arama](../document-processing/module/fulltext-search.md) modül sayfasına bakın.

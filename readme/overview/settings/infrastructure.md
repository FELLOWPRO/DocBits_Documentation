# Altyapı

**Altyapı** sayfası, yöneticilere DocBits'in her parçasının nerede çalıştığı (AB veya ABD), bir belgenin sistem içinde nasıl aktığı ve arka plan işlemenin sağlıklı olup olmadığı hakkında canlı bir görünüm sunar. Sayfa salt okunurdur — burada hiçbir şey yapılandırılmaz; şu soruyu yanıtlar: *„her şey çalışıyor mu ve verilerim kendi bölgemde mi kalıyor?"*

> **Erişim:** Altyapı yalnızca yöneticilere özel bir sayfadır. **Ayarlar → Organizasyon ve Erişim → Altyapı** yolunu açın.

<figure><img src="../../.gitbook/assets/infrastructure_overview.png" alt="Topoloji sekmesi açık Altyapı sayfası"><figcaption><p>Altyapı sayfası, Topoloji sekmesi</p></figcaption></figure>

Sayfa üç sekmeye ayrılmıştır:

| Sekme | Yanıtladığı soru |
|-------|------------------|
| **Topoloji** | Her bileşen nerede çalışıyor ve hepsi benim bölgemde mi? |
| **İşleme** | İşleme adımları (OCR, çıkarma, PO eşleştirme …) çalışıyor ve güncel mi? |
| **Zamanlanmış görevler** | Yinelenen arka plan işleri planlandığı gibi çalışıyor mu? |

## Topoloji

Topoloji sekmesi, tüm DocBits platformunu katmanlara gruplanmış bir diyagram olarak çizer — **Edge / Web**, **Core API**, **İçe Aktarma**, **Arka Plan Servisleri**, **Veri Depoları** ve **Kimlik Doğrulama**. Her kutu bir bileşendir (Web Uygulaması/CDN, API ağ geçidi, OCR worker, veritabanı vb.).

<figure><img src="../../.gitbook/assets/infrastructure_topology.png" alt="Bölge rozetleriyle topoloji diyagramı"><figcaption><p>Her bileşen, çalıştığı bölge ile etiketlenir</p></figcaption></figure>

### Bölge şeffaflığı

Her bileşen bir bölge rozeti taşır; böylece verilerinizin nerede bulunduğunu bir bakışta doğrulayabilirsiniz:

| Rozet | Anlamı |
|-------|--------|
| **AB ✓** / **US ✓** | Bileşen, organizasyonunuzun bölgesinde çalışır. |
| **SHARED** | Tek bir bölgesi olmayan küresel bir bileşen (örneğin CDN) — bu beklenen bir durumdur ve sorun değildir. |
| **Bölge uyuşmazlığı** | Bileşen, organizasyonunuzdan *farklı* bir bölgede çalışır. Desteğe bildirebilmeniz için vurgulanır. |

Üstteki afiş sonucu özetler: her şey eşleştiğinde **„Tüm bileşenler sizin bölgenizde (AB) çalışıyor"**, veya kritik bir bileşen başka bir bölgedeyse bir uyarı.

### Mimari vs. Süreci oynat

Görünümü değiştirmek için diyagramın üzerindeki anahtarı kullanın:

- **Mimari** — tüm bileşenlerin ve nasıl bağlandıklarının statik haritası.
- **Süreci oynat** — bir belgenin sistemdeki yolculuğunu adım adım canlandırır; böylece bileşenlerin hangi sırayla devreye girdiğini görürsünüz.

**● live** göstergesi, diyagramdaki durum bilgisinin sistemin güncel durumunu yansıttığını gösterir.

### İsteğe bağlı modüller

İsteğe bağlı bir modüle ait bileşenler (Tam metin arama, DocFlow, Auto-Accounting, DocNet, PO Eşleştirme) bir **etkin** veya **devre dışı** rozeti gösterir. Devre dışı bir modüle tıklamak sizi doğrudan onu açabileceğiniz sayfaya götürür — çoğu modül için **Ayarlar → Modül**, veya PO Eşleştirme için (belge türü başına etkinleştirilen) **Belge Türleri**.

## İşleme

İşleme sekmesi, **organizasyonunuza** ait belge işleme hattını gösterir — her adımın en son ne zaman çalıştığını ve işin akıp akmadığını veya birikip birikmediğini.

<figure><img src="../../.gitbook/assets/infrastructure_processing.png" alt="Durum rozetleriyle işleme tablosu"><figcaption><p>Organizasyonunuz için adım bazında işleme durumu</p></figcaption></figure>

| Sütun | Açıklama |
|-------|----------|
| **Süreç** | İşleme adımı — Belge İşleme, OCR, TR-OCR, Barkod Bölme, Barkod Çıkarma, Çıkarma, PO Eşleştirme. |
| **Son Çalışma** | Adımın en son ne kadar süre önce çalıştığı. Tam zaman damgası için üzerine gelin. *„Hiç çalışmadı"*, henüz hiçbir belgenin bu adıma ulaşmadığı anlamına gelir. |
| **Durum** | Trafik ışığı türünde bir rozet (aşağıya bakın). |

Durum rozetleri:

| Rozet | Anlamı |
|-------|--------|
| **OK** (yeşil) | Son zamanlarda hata yok ve bekleyen bir şey yok — adım sağlıklı. |
| **Devam ediyor (N)** (sarı) | `N` belge şu anda bu adımda işleniyor. |
| **Hata (N)** (kırmızı) | `N` belge bu adımda yakın zamanda başarısız oldu. |

Hatalar ve *devam ediyor* bağımsız sinyallerdir, bu nedenle bir adım her iki rozeti aynı anda gösterebilir — böylece başka iş sürerken bile bir hatayı görürsünüz. En güncel sayıları almak için **Yenile**'yi (sağ üst) kullanın.

## Zamanlanmış görevler

Zamanlanmış görevler sekmesi, DocBits'i çalışır durumda tutan yinelenen arka plan işlerini listeler (önbellek yenilemeleri, durum uyarıları, belge zaman aşımları, giden senkronizasyonlar ve daha fazlası) ve her birinin zamanında tetiklendiğini doğrular.

<figure><img src="../../.gitbook/assets/infrastructure_scheduled.png" alt="Zamanlanmış görevler tablosu"><figcaption><p>Yinelenen arka plan işleri ve zamanlama durumları</p></figcaption></figure>

| Sütun | Açıklama |
|-------|----------|
| **Görev** | Zamanlanmış işin adı. |
| **Son Çalışma** | En son ne kadar süre önce çalıştığı. Tam zaman damgası için üzerine gelin; *„Hiç çalışmadı"*, henüz tetiklenmediği anlamına gelir. |
| **Durum** | Zamanlama durumu (aşağıya bakın). |

Durum değerleri:

| Rozet | Anlamı |
|-------|--------|
| **Planlandığı gibi** (yeşil) | Görev beklenen aralıkta çalışıyor. |
| **Gecikti** (kırmızı) | Görev beklendiği zaman çalışmadı — incelemeye veya desteğe bildirmeye değer. |
| **Bilinmiyor** (gri) | Zamanlama durumu belirlenemedi. |

Zamanlama durumunu istediğiniz zaman yeniden kontrol etmek için **Yenile**'yi kullanın.

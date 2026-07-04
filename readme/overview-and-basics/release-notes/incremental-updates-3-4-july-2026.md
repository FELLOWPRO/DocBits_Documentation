# DocBits Sürüm Notları — 3–4 Temmuz 2026

_Bu production yükseltmesinin sade bir dille neler sağladığı. Her hizmet, şu anda
production ortamında canlı olan sürümü gösterir. Listelenmeyen hizmetlerde bu
dönemde müşteriye yönelik bir değişiklik olmamıştır._

---

## Öne Çıkanlar

- **Filo genelinde daha temiz dağıtımlar.** Birkaç temel hizmet (API, Auto
  Accounting, Docflow, Extraction, OCR, PO Match) artık bir sürüm sırasında
  doğru şekilde kapanıyor, böylece devam eden bir dağıtım artık zaten işlemde
  olan bir isteği kesme riski taşımıyor.
- **E-fatura dışa aktarma iyileştirmeleri.** Bir belgeyi aynı anda birden fazla
  dışa aktarma yapılandırmasına aktarmak artık daha güvenilir — yinelenen dışa
  aktarma kontrolleri öğe başına değil, toplu iş başına bir kez çalışıyor ve
  yeni bir dışa aktarma uç noktası, birkaç dışa aktarma birlikte tetiklendiğinde
  dışa aktarma durumunun titremesini önlüyor. XRechnung/ZUGFeRD belgeleri de
  daha tutarlı alan eşlemesi kazanıyor.
- **Daha kararlı belge işleme.** Tek bir sayfanın başarısız olması durumunda
  tüm bir OCR belgesini çökertebilen bir hata düzeltildi, Satın Alma Siparişi
  teslimat senkronizasyonunun yalnızca ilk 100 kaydı getirmesi sorunu
  düzeltildi ve birkaç hizmet kısa süreli veritabanı bağlantı kesintilerine
  karşı güçlendirildi.
- **E-posta ekleri kurtarıldı.** Gelen içe aktarma sırasında e-posta eklerinin
  bozuk veya eksik bayt olarak gelebildiği bir durum düzeltildi.
- **İş akışı güvenilirliği.** Doğru şekilde temizlenmeyen bir kilit nedeniyle
  iş akışlarının takılı kalması düzeltildi ve atlanan iş akışı adımlarının
  doğru şekilde işlenip günlüğe kaydedilmesi için yeniden zamanlama mantığı
  düzeltildi.
- **Yeni: Ideas Service.** Yeni bir arka uç hizmeti (Ideas, v0.3.0) production
  filosuna katıldı.

---

## API Service — canlı: `12.52.4`

- **OCR güvenilirliği:** tek bir sayfadaki çökme artık tüm belgeyi
  başarısız kılmıyor.
- **Dışa aktarma:** yinelenen dışa aktarma kontrolleri artık öğe başına
  değil, toplu iş başına bir kez çalışıyor; yeni bir dışa aktarma uç noktası,
  birden fazla dışa aktarma aynı anda çalıştığında dışa aktarma durumunun
  titremesini önlüyor; XRechnung/ZUGFeRD belgeleri daha tutarlı kurallı alan
  eşlemesi kazanıyor.
- **Satın Alma Siparişleri:** sipariş başına teslimat senkronizasyonunun
  yalnızca ilk 100 kaydı getirmesi sorunu düzeltildi.
- **Etkinlik Günlükleri:** "İleri" sayfa düğmesinin ilgisiz bir zaman
  aralığına atlaması düzeltildi.
- **Ana Veri Arama:** bir sunucu hatası (HTTP 500) düzeltildi.
- **Arama indeksleme:** belgelerin tam metin aramaya güvenilir şekilde
  kuyruğa alınması için bir teslimat kanıtı işareti ve yeniden deneme
  eklendi.
- Birkaç tekrarlayan arka plan hatasını çözen genel kararlılık düzeltmeleri.

## Auth Service — canlı: `1.68.7`

- Bu dönemde yalnızca dahili güvenilirlik ve bakım.

## Auto Accounting — canlı: `1.18.8`

- Dağıtımlar sırasında **daha temiz kapanmalar**, işlemdeki isteklerin
  kesilmesini önleyerek.

## Barcode Service — canlı: `1.15.8`

- Bu dönemde yalnızca dahili dağıtım yapılandırması düzeltmesi.

## Docflow Service — canlı: `2.5.3`

- Bir belgeyi aynı anda birden fazla dışa aktarma yapılandırmasına
  göndermek için **yeni dışa aktarma seçeneği**.
- Durumdan bağımsız olarak doğru şekilde temizlenmeyen bir kilit nedeniyle
  **iş akışlarının takılı kalması düzeltildi**.
- Atlanan adımların sessizce göz ardı edilmek yerine doğru şekilde işlenip
  günlüğe kaydedilmesi için **iş akışı yeniden zamanlaması düzeltildi**.
- **Daha hızlı başlangıç:** veritabanları artık arka planda önceden ısıtılıyor.
- Kısa süreli veritabanı bağlantı kesintilerine karşı daha dayanıklı.
- İş akışı kartları için geliştirilmiş tarih alanı ayrıştırması.

## Email Service — canlı: `1.37.9`

- **Gelen ekler düzeltildi**, bozuk veya eksik bayt olarak gelebiliyordu.
- Bir posta kutusu klasörü getirilemediğinde genel bir hata yerine **daha
  net hatalar**.

## Extraction Service — canlı: `1.49.6`

- Tanınmayan bir belge türüne sahip belgelerde ve olağandışı/hatalı
  biçimli tablolarda **çökmeler düzeltildi**.
- Sorgu sırasında kısa süreli veritabanı bağlantı kesintilerine karşı daha
  dayanıklı.

## FTP Service — canlı: `1.30.3`

- Bu dönemde yalnızca dahili framework yükseltmesi.

## Fulltext Service — canlı: `1.36.3`

- **Arama indeksleme:** periyodik bir tarama artık herhangi bir kuruluş
  için arama indeksine ulaşamayan belgeleri onarıyor.
- **ERP senkronizasyonu:** başarısız bir yeniden deneme sonrasında ERP
  senkronizasyonunu engelleyebilen takılı bir kilit düzeltildi.

## OCR Service — canlı: `1.7.8`

- **OCR kimlik doğrulaması düzeltildi**, böylece kuruluş API anahtarları
  yeniden doğru şekilde çalışıyor.
- Dağıtımlar sırasında daha temiz kapanmalar.

## Operator Service — canlı: `1.39.7`

- Bu dönemde yalnızca dahili dağıtım güvenilirliği düzeltmeleri.

## PO Match Service — canlı: `1.56.0`

- Boş değerler içeren PO Match miktarları sıralanırken oluşan **bir çökme
  düzeltildi**.
- Dağıtımlar sırasında daha temiz kapanmalar.

## Web App — canlı: `10.36.9`

- Başka bir ekrandan Alan Doğrulamaya geri dönüldüğünde oluşan **bir hata
  düzeltildi**.
- **"Scripts" düğmesinin** 404 sayfasına yönlendirmesi düzeltildi.
- **Etkinlik Günlükleri:** yanlış bir "Page 2 of 1" görüntüsü düzeltildi ve
  WARN önem düzeyi filtresinin hiçbir şeyle eşleşmemesi sorunu düzeltildi.

---

## Bu dönemde müşteriye yönelik değişiklik yok

Auth Service, Barcode Service, FTP Service, Operator Service ve Docnet
Service (`1.54.6`, değişmedi) bu dönemde yalnızca dahili veya dağıtım
yapılandırması bakımı aldı.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT and NEU version-bump commits supplied by the
     user, per service). Window ~2026-07-01 → 2026-07-04. -->

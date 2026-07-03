# DocBits Sürüm Notları — 30 Haziran – 3 Temmuz 2026

_Bu production yükseltmesinin sade bir dille neler sağladığı. Her hizmet, şu anda
production ortamında canlı olan sürümü gösterir. Listelenmeyen hizmetlerde bu
dönemde müşteriye yönelik bir değişiklik olmamıştır._

---

## Öne Çıkanlar

- **Etkinlik Günlüklerinde AI sohbeti.** Etkinlik Günlükleri sayfasındaki yeni bir
  AI sohbet paneli, ham kayıtları karıştırmadan günlük etkinliği hakkında doğrudan
  soru sormanıza olanak tanıyor.
- **Giden e-posta içe aktarma takibi.** İçe Aktarma Günlüğü artık gelen e-postaların
  yanında giden postayı da kaydediyor; Hatalar / Gelen / Giden hızlı filtre
  etiketleriyle birlikte — tekrarlanan hatalardan sonra sorunlu posta kutuları
  otomatik olarak devre dışı bırakılıyor, yöneticiler içe aktarma hatasında e-posta
  ile bilgilendirilebiliyor ve yeniden denemeler artık pes etmeden önce yaklaşık 5
  saat boyunca 15 kez tekrarlanıyor.
- **Daha net e-posta içe aktarma hataları.** Oturum açma hataları artık gerçek
  temel nedeni gösteriyor; geçersiz bir sertifika veya yanlış bir Gmail uygulama
  şifresi için özel mesajlarla birlikte.
- **Oturum açma döngüsü düzeltildi.** Bazı kullanıcılar token yenileme sırasında
  tekrarlanan bir oturum açma döngüsüne takılabiliyordu — çözüldü.
- **Daha kararlı belge işleme.** Yuvarlanmamış koordinat değerlerinden kaynaklanan
  veri çıkarma sırasındaki bir çökme düzeltildi, barkod okuma artık kurtarılabilir
  hatalarda sessizce pes etmek yerine yeniden deniyor ve bir belgenin aynı anda iki
  kez dışa aktarılabildiği nadir bir durum giderildi.
- **Doğrulama ekranı iyileştirmeleri.** Belgelere artık daha fazla yakınlaştırma
  yapabiliyorsunuz, alanlar değeri gerçekte değişmediğinde scriptler tarafından
  artık boşaltılmıyor ve pano geri döndüğünüzde sayfa konumunuzu hatırlıyor.

---

## Web App — canlı: `10.35.7`

- **AI sohbet paneli**, Etkinlik Günlükleri sayfasına eklendi (#15512).
- **İçe Aktarma Günlüğü:** yeni Hatalar / Gelen / Giden hızlı filtre etiketleri;
  gelen e-posta ayarları için hata bildirimi alıcıları anahtarı ve alanı.
- **Doğrulama ekranı:** belge yakınlaştırması artık önceki varsayılan boyutun
  ötesine geçiyor; doğrulama scriptleri tarafından boşaltılan alanlar, script aynı
  değeri döndürdüğünde artık değerlerini doğru şekilde koruyor.
- **Pano:** tabloya geri dönüldüğünde sayfa konumu korunuyor; sütun yeniden
  boyutlandırma tutamacı artık tablo başlığının dışına taşmıyor.
- **Otomatik Muhasebe ekranı:** bir doğrulama hatası düzeltildi.
- **DocBits Görevleri:** bir izin sorunu düzeltildi.
- **Watchdog günlükleri:** bir zaman aralığı filtresi ve ayarlanabilir bir
  sayfa başına satır sayısı seçici eklendi.
- **Düzeltmeler:** Panolar sayfasında bir grafik hatası ("Element not found");
  Etkinlik Günlüklerinde bozuk bir dışa aktarma silme bağlantısı; Düzen Oluşturucu
  ekranında düzen düzeltmeleri; Etkinlik Günlükleri zaman aralığı filtresinde
  eksik bir çeviri.
- **Otomatik güncelleme:** otomatik uygulama güncelleme mekanizmasının daha da
  sağlamlaştırılması (daha hızlı önyükleme temizliği, daha güvenilir sürüm tespiti,
  kurtarma yeniden yüklemesinden önce önbellek temizliği).

## API Service — canlı: `12.48.1`

- **Daha hızlı belge script yükleme:** doğrulama scriptleri artık her seferinde
  yeniden alınmak yerine sunucu tarafında önbelleğe alınıyor (6 saatlik önbellek).
- **Daha doğru tutar güven skoru:** güven skorlaması artık farklı ondalık ayırıcı
  kurallarını kullanan belgeleri de hesaba katıyor.
- **Güvenilirlik:** belge doğrulaması her zaman tek etkin script sürümünü
  çalıştırıyor ve hangi sürümün çalıştığı artık günlüğe kaydediliyor; bir belgenin
  aynı anda iki kez dışa aktarılabildiği nadir bir durum giderildi; zorunlu bir
  yeniden OCR sonrasında tedarikçiye özel çıkarma kuralları artık yeniden doğru
  şekilde uygulanıyor.
- **E-posta içe aktarma:** giden posta günlüğü ve hata bildirimi e-postaları için
  arka uç desteği eklendi (bkz. Email Service, aşağıda).

## Auth Service — canlı: `1.68.5`

- **Oturum açma döngüsü düzeltildi**, bazı kullanıcıların oturum token'ı
  yenilenirken takılabildiği bir sorun.
- **Daha hızlı kuruluş yönetici ekranları:** kullanıcı ve abonelik verileri artık
  tek tek değil toplu olarak yükleniyor.
- **Nadir bir veritabanı çakışması düzeltildi**, bir kullanıcıyı bir kuruluşa
  bağlarken.

## Email Service — canlı: `1.37.4`

- **İçe Aktarma Günlüğü artık gelen postanın yanında giden postayı da izliyor**,
  yalnızca gelen, giden veya başarısız içe aktarmaları gösteren bir filtreyle
  birlikte.
- **Tekrarlanan hatalardan sonra sorunlu posta kutuları artık otomatik olarak
  devre dışı bırakılıyor** ve bir içe aktarma başarısız olduğunda yöneticiler
  e-posta ile bilgilendirilebiliyor; yeniden denemeler artık pes etmeden önce
  yaklaşık 5 saat boyunca 15 kez tekrarlanıyor.
- **Daha net oturum açma hatası mesajları:** gerçek temel nedeni gösteriyor,
  geçersiz bir sertifika için özel bir mesaj ve yanlış bir Gmail uygulama şifresi
  için özel bir mesaj sunuyor.
- **Gelen yönlendirme düzeltildi**, AB bölgesi hesapları için sunucu adreslerini
  yanlış şekilde yeniden yazan sorun.
- Kısa süreli Redis bağlantı kesintilerine karşı daha dayanıklı.

## Extraction Service — canlı: `1.49.0`

- **Çıkarma sırasında bir çökme düzeltildi**, yuvarlanmamış koordinat değerlerinden
  kaynaklanan.
- Karışık ondalık ayırıcı biçimlerine sahip belgeler için **daha doğru tutar güven
  skoru**; küçük vergi toplamı yuvarlama farkları artık bir eşleşmeyi engellemiyor.

## Docflow Service — canlı: `2.4.2`

- **Gelişmiş (Celery tabanlı) iş akışları için kimlik doğrulama yeniden
  düzenlendi**, başarısız bir kimlik doğrulama kontrolünün artık bir iş akışı
  çalıştırmasını çökertemeyeceğini garanti eden korumalarla birlikte.
- Artık var olmayan bir iş akışına karşı çalıştırılmaya çalışılan bir iş akışı
  adımında **daha net bir yanıt** sunuluyor.

## Barcode Service — canlı: `1.15.7`

- **Barkod okuma artık kurtarılabilir hatalarda otomatik olarak yeniden
  deniyor**, sessizce pes etmek yerine.

## OCR Service — canlı: `1.7.3`

- **Bir Redis ana bilgisayar adı arama sorunundan kaynaklanan bir OCR hatası
  düzeltildi.**
- Sağlık kontrolü Redis bağlantı kesintileri artık hata olarak günlüğe
  kaydedilmiyor, bu da yanlış uyarıları azaltıyor.

## PO Match Service — canlı: `1.55.8`

- **PO Match kayıtlarında notların görünmemesi sorunu düzeltildi.**

---

## Bu dönemde müşteriye yönelik değişiklik yok

30 Haziran – 3 Temmuz arasında kararlı, kayda değer ürün değişikliği yok: Auto
Accounting (`1.18.7`), Docnet (`1.54.6`), FTP (`1.30.2`), Fulltext (`1.35.7`),
Operator (`1.39.5`). Auto Accounting yalnızca dahili dağıtım yapılandırması
bakımı aldı. Ideas Service, bu dönemde sürüm kontrolü için erişilemedi.

<!-- Generated by the docbits-changelog skill (version-boundary mode, resolved
     from the prod version table supplied by the user). Window 2026-06-30 →
     2026-07-03. -->

# DocBits Sürüm Notları — 4–14 Temmuz 2026

_Bu DocBits sürümüyle sizin için nelerin değiştiğine dair bir özet. Aşağıdaki her
hizmet, şu anda kullanıma sunulmakta olan sürümü ve ardından sade bir dille
açıklanmış yenilikleri veya düzeltmeleri gösterir — bilet numaraları veya
mühendislik jargonu olmadan. Listelenmeyen hizmetlerde bu dönemde müşteriye
yönelik bir değişiklik olmamıştır._

---

## Öne Çıkanlar

- **Çoklu kuruluş girişi.** Birden fazla kuruluşa üye olan kullanıcılar artık
  girişte gerçek bir kuruluş seçim ekranı, üst çubukta bir kuruluş değiştirici
  ve varsayılan kuruluş ayarı ile karşılanıyor. Oturumlar aynı anda güvenli bir
  şekilde tek bir kuruluşa bağlanıyor ve uygulama, etkin kuruluşun bölgesini
  otomatik olarak izliyor. Yanlış bölgeye yapılan girişler artık başarısız
  olmak yerine doğru bölgede otomatik olarak yeniden deneniyor.
- **Sürüm kanalları (frozen / latest).** Kuruluşlar artık kararlı ("frozen")
  bir sürüme sabitlenebilirken diğerleri en güncel güncellemeleri alabiliyor —
  böylece kontrollü dağıtımlar mümkün oluyor. Hizmet Sürümleri iletişim
  kutusunda yeni bir *Release* sütunu gösteriliyor ve yöneticiler kanalı
  Şirket Bilgileri üzerinden yönetiyor. Bu dönemde bazı hizmetlerin daha büyük
  sürüm sıçramaları göstermesi tamamen yeni kanal sürüm numaralandırmasından
  kaynaklanıyor — bu sıçramalar herhangi bir işlevsel değişiklik içermiyor.
- **Yapılandırılabilir kural motorları.** API'ye üç yeni kural sistemi geliyor
  (her biri varsayılan olarak kapalı, kuruluş bazında etkinleştiriliyor):
  çıkarılan değerleri denetleyip başarısızlıkları doğrudan belge üzerinde
  işaretleyen **doğrulama kuralları**, çıkarılan alan ve tablo değerlerini
  otomatik olarak temizleyen veya yeniden yazan **dönüştürme kuralları** ve
  doğru belge düzenini belgenin geldiği yere göre değil kurallara göre seçen
  **kural tabanlı düzen seçimi**.
- **E-posta içe aktarmada şeffaflık.** E-posta içe aktarma günlüğü artık her
  ek için genişletilebilir bir satır gösteriyor, hangi belgelerin
  oluşturulduğunu söylüyor (panoda doğrudan ilgili belgeye götüren düğmelerle),
  atlanan ve bölünen öğeleri işaretliyor ve orijinal e-postayı `.eml` dosyası
  olarak indirmenize olanak tanıyor.
- **Yapay zeka ile tablo çıkarımı.** Tablolar için yeni bir yapılandırılmış
  yapay zeka çıkarım modu; Belge Türü ayarlarında tablo ve sütun bazında
  "Use AI" onay kutusuyla.
- **Web App kararlılığı.** Süresi dolan bir oturum sonrasında oluşan sonsuz
  yeniden yükleme döngüsü düzeltildi, bozuk Layout Builder onarıldı ve çıkarım
  tablolarına sürüklenebilir bir yükseklik boyutlandırıcısı eklendi.
- **Yeni: Auth Bridge Service.** Yeni bir hizmet, oturum açma verilerini AB ve
  ABD bölgeleri arasında sürekli olarak eşitliyor; kendi kendini onarma ve
  izleme yerleşik olarak geliyor.

---

## API Service — canlı: `12.57.8`

- **Doğrulama kuralları (yeni, kuruluş bazında):** yönetici tarafından
  yapılandırılabilen bir kural motoru, çıkarılan değerleri (toplamlar, zorunlu
  alanlar ve daha fazlası) denetliyor ve hangi kuralın tetiklendiği bilgisiyle
  birlikte başarısızlıkları doğrudan belge üzerinde işaretliyor. Kurallar
  etkinleştirilmeden önce deneme çalıştırmasıyla test edilebiliyor, belge türü
  bazında açılabiliyor ve başlangıç için varsayılan kurallardan oluşan bir
  katalogla geliyor (siz etkinleştirene kadar tümü devre dışı).
- **Dönüştürme kuralları (yeni, kuruluş bazında):** işleme sırasında çıkarılan
  alan ve tablo değerlerini otomatik olarak temizliyor veya yeniden yazıyor —
  belge türü bazında veya tüm kuruluş için yapılandırılabiliyor.
- **Kural tabanlı düzen seçimi (yeni):** belge düzenleri artık belgenin
  kaynağına bağlı olmak yerine yapılandırılabilir kurallarla seçilebiliyor.
  Mevcut kaynak tabanlı davranış otomatik olarak taşınıyor, düzen şablonları
  yeniden adlandırılabiliyor ve yinelenen düzen başlıkları engelleniyor.
- **Daha hızlı pano dışa aktarmaları:** panodan tetiklenen dışa aktarmalar
  artık bir yoklama döngüsünü beklemek yerine ayrılmış bir arka plan
  işleyicisine gönderiliyor, böylece hemen başlıyor.
- **Yinelenen Belge Algılama dışa aktarma bloğu düzeltildi:** şüpheli
  yinelenenler için dışa aktarma bloğu yeniden çalışıyor.
- **Kaydedilmeyen ayarlar:** aynı ayarın daha önce silinmiş eski bir kopyası
  bulunduğunda kaydedilen tercihlerin ara sıra kalıcı olmaması düzeltildi.
- **Olağandışı karakterler içeren belgeler:** çıkarılan verilerdeki görünmez
  NUL karakterlerinin neden olduğu kaydetme hataları düzeltildi.
- **Doğru "Güncelleyen" bilgisi:** e-belge olarak otomatik yüklenen belgeler
  artık son düzenleyen olarak bir sistem kullanıcısı göstermiyor — bir kişi
  gerçekten düzenleme yapana kadar alan boş kalıyor.
- **İyi bir metin katmanına sahip taranmış PDF'ler:** yeni bir seçenek,
  DocBits'in OCR'yi yeniden çalıştırmak yerine taranmış sayfada zaten gömülü
  olan metne güvenmesine olanak tanıyor — daha hızlı ve çoğu zaman daha
  isabetli.
- **E-faturalar:** orijinal dosyanın yeniden denetlenmesi gerektiğinde gömülü
  XML'in daha sağlam algılanması.
- **Görevler:** yönetici olmayan kullanıcıların görev listesinde "Tümü"
  filtresini kullanmasına olanak tanıyan yeni bir kuruluş ayarı.
- **Satır kalemi eşleştirme:** bulanık eşleştirme davranışı artık satır
  bazında yapılandırılabiliyor.
- **Kararlılık:** WebSocket bağlantıları hata durumunda sunucu istisnaları
  oluşturmak yerine temiz bir şekilde kapanıyor; izin önbelleği eşitlemesi
  kendini doğrulayıp onarıyor; hizmet sürümü artık sağlık uç noktasında
  görülebiliyor.

## Auth Service — canlı: `1.71.1`

- **Çoklu kuruluş girişi:** kullanıcı birden fazla kuruluşa üye olduğunda
  giriş artık hangi kuruluşa girileceğini soruyor, oturumlar o kuruluşa
  bağlanıyor ve yeni uç noktalar kuruluş seçmeyi, kuruluş değiştirmeyi ve
  varsayılan kuruluş belirlemeyi destekliyor. Yinelenen veya çakışan kuruluş
  üyelikleri temizlendi ve artık veritabanı düzeyinde engelleniyor; üyelik
  sorguları da hızlandırıldı.
- **Varsayılan kuruluş düzeltmeleri:** giriş yapıldığında (rastgele bir
  kuruluş değil) varsayılan kuruluşunuz otomatik olarak seçiliyor ve
  varsayılanı değiştirmek eski profil verileri göstermek yerine hemen etkili
  oluyor.
- **Çıkış düzeltildi:** çıkışta oluşan bir sunucu hatası (HTTP 500) giderildi
  ve belirteç iptal uç noktası geri getirildi.
- **Belirteç güvenliği:** belirteç doğrulama ve önbellekleme artık belirtecin
  hangi kuruluş için verildiğini dikkate alıyor ve belirteç iptali
  merkezileştirildi.
- **Sürüm kanalları:** kuruluşun sürüm kanalı burada saklanıyor, kuruluş
  yöneticileri tarafından yönetilebiliyor ve uygulamaya ve yönlendirme
  katmanına sunuluyor.

## Auth Bridge Service — canlı: `0.2.4.2` _(yeni hizmet)_

- **Nedir:** kimlik doğrulama verilerini AB ve ABD bölgeleri arasında sürekli
  olarak çoğaltan yeni bir hizmet; böylece hesaplar ve oturum açma bilgileri
  bölgeler arasında tutarlı kalıyor.
- **Kendi kendini onarma:** bölgeler arasındaki veri kaymalarını algılayıp
  onarıyor — silme işlemlerinin yayılmasını sağlamak dahil — ve bağlantı
  kopmalarında veri kaybetmek yerine otomatik olarak toparlanıyor.
- **Güvenlik ve izleme:** daha önce oluşan çift yönlü bir çoğaltma döngüsü
  durduruldu ve artık etkin olarak algılanıp engelleniyor; hata izleme ve
  uyarı mekanizmaları devreye alındı; hizmet, sürümünü Hizmet Sürümleri
  iletişim kutusunda bildiriyor.

## Docflow Service — canlı: `2.6.1`

- **İş akışı kartları boş değerleri kabul ediyor:** onay kutusu ve iş ortağı
  kartları, bir alan meşru olarak boş olduğunda artık başarısız olmuyor; kart
  türü denetimleri daha katı ve daha öngörülebilir.
- **İş akışları gerçek değişikliklerde yeniden çalışıyor:** iş akışı kilidi
  yeniden tetikleyicideki belge durumunu dikkate alıyor ve artık belge
  sürümünü de izliyor — böylece verisi gerçekten değişen bir belge aynı
  durumla bile iş akışından yeniden geçebiliyor, gerçek yinelenenler ise
  engellenmeye devam ediyor.
- **Daha büyük gelişmiş iş akışları:** iş akışı düğüm sınırı yükseltildi ve
  artık ortam bazında yapılandırılabiliyor.
- **Alternatif dışa aktarma:** iş akışıyla tetiklenen alternatif dışa
  aktarmalar artık bu şekilde etiketleniyor, böylece alt sistemler bunları
  ayırt edebiliyor.
- **Dayanıklılık:** hizmet, kullanım sırasında kopan bir veritabanı
  bağlantısında otomatik olarak yeniden bağlanıyor, yavaşlayan bir mesaj
  aracısını başarısız olmak yerine tolere ediyor ve başarısız API istekleri
  artık tam bağlam ve izlenebilir yürütme kimlikleriyle günlüğe kaydediliyor.

## Email Service — canlı: `1.38.4`

- **İzlenebilirlik için yeniden yapılandırılan içe aktarma günlüğü:** içe
  aktarılan her e-posta artık kendisinden hangi belgelerin oluşturulduğunu,
  ek bazında ayrıntı satırlarıyla birlikte kaydediyor.
- **Orijinal e-posta indirme:** orijinal ileti, doğrudan içe aktarma
  günlüğünden `.eml` dosyası olarak indirilebiliyor.
- **Ek kurtarma:** bozulma kurtarma yolu artık düz metin iletileri de
  işleyebiliyor, böylece hasarlı gelen e-postaların daha fazlası atlanmak
  yerine kurtarılıyor.

## Extraction Service — canlı: `1.51.6`

- **Vergi/net artık yer değiştirmiyor:** ABD belgelerinde, birden fazla aday
  çift bulunduğunda vergi tutarının net tutardan büyük olacak şekilde
  atanabildiği bir durum düzeltildi.
- **Tedarikçi başına birden fazla vergi oranı:** çıkarım artık faturalarında
  tek belgede farklı vergi oranları bulunan tedarikçileri işleyebiliyor.
- **Yapay zeka ile tablo çıkarımı (yeni, isteğe bağlı):** tablolar için
  yapılandırılmış yapay zeka çıkarım uç noktaları, kuruluş bazında özellik
  bayrağıyla etkinleştiriliyor.
- **Daha hızlı yapay zeka çağrıları:** gereksiz işleme süresini önlemek için
  çıkarım sırasında kullanılan yapay zeka modeli yapılandırması iyileştirildi.
- **Çökme düzeltmesi:** çıkarım sırasında boş aday listesi üreten belgelerde
  oluşan bir hata giderildi.

## Fulltext Service — canlı: `1.37.2`

- **Arama indeksi taşımaları onarıldı:** kaymış olan taşıma tanımları geri
  yüklendi; böylece arama indeksi yükseltmeleri güvenilir kalıyor.
- Yeni sürüm kanalı altyapısı için dahili yönlendirme çalışması.

## PO Match Service — canlı: `1.58.2`

- **Daha toleranslı eşleştirme:** PO eşleştirme artık olağandışı verilerde
  başarısız olmuyor — metin olmayan kalem numaraları, eksik miktarlar ve
  metin olmayan tutar değerleri artık hataya yol açmak yerine sorunsuz
  şekilde işleniyor.

## Web App — canlı: `10.41.8`

- **Çoklu kuruluş deneyimi:** girişte yeni kuruluş seçim sayfası, üst çubukta
  özel bir kuruluş değiştirme simgesi, varsayılan kuruluş ayarları ve etkin
  kuruluşunuzun bölgesini izleyen uygulama. Yanlış bölgeye yapılan girişler
  sessizce doğru bölgede yeniden deneniyor ve gerektiğinde sizi kuruluş seçim
  ekranına yönlendiriyor.
- **Sonsuz yeniden yüklemeler sona erdi:** sunucu, saklanan bir oturum
  belirtecini reddettiğinde oluşabilen sonsuz yeniden yükleme döngüsü
  düzeltildi — uygulama artık sonsuza kadar yeniden yüklemek yerine gerçek
  bir belirteç yenilemesi yapıyor.
- **Layout Builder düzeltildi:** Layout Builder yeniden çalışıyor ve düzen
  seçimi belgenin kaynağından ayrıldı (API'deki yeni kural tabanlı seçimle
  uyumlu).
- **Çıkarım tabloları:** satır kalemi tablolarında artık sürüklenebilir bir
  boyutlandırma tutamacı var; böylece doğrulama sırasında tabloya daha fazla
  alan verebilirsiniz.
- **E-posta içe aktarma günlüğü:** yeni "atlandı" durumu ve bölünme rozetleri,
  ek bazında genişletilebilir satırlar, orijinal e-posta indirme ve panoyu
  doğrudan ilgili belgeye göre filtrelenmiş olarak açan belge kimliği
  düğmeleri.
- **Pano araması:** sorgu değeri açılır listesi artık değer listesi alanları
  için yerelleştirilmiş etiketi gösteriyor ve arama yardımı örnekleri yeniden
  düzenlendi.
- **Ayar güvenilirliği:** SSO ile oturum açarken kullanıcı tercihleri artık
  güvenilir şekilde yükleniyor ve kaydetme onayı yalnızca kaydetme gerçekten
  başarılı olduğunda gösteriliyor.
- **Görevler:** "Tümü" filtresi, yeni bir kuruluş ayarıyla yönetici olmayan
  kullanıcılar için yeniden etkinleştirilebiliyor.
- **Watchdog günlükleri:** artık 10.000 kayıtla sınırlı değil; ayrıca genel
  kullanılabilirlik iyileştirmeleri.
- **Destek talepleri:** destek formu, e-posta adresinizi profilinizden
  önceden dolduruyor.
- **Belge Türü ayarları:** yapay zeka destekli tablo çıkarımını kontrol etmek
  için tablolarda ve sütunlarda yeni "Use AI" onay kutusu.
- **Hizmet Sürümleri iletişim kutusu:** her hizmetin kanalını (frozen/latest)
  gösteren yeni *Release* sütunu; sabitlenmiş kuruluşlar için hızlı kalacak
  şekilde yönlendiriliyor.
- **Alan Doğrulama:** başka bir ekrandan Alan Doğrulamaya geri dönüldüğünde
  oluşan bir hata düzeltildi ve "Scripts" düğmesi artık 404 sayfasına
  yönlendirmiyor.

---

## Yalnızca sürüm yeniden numaralandırması (işlevsel değişiklik yok)

**Auto Accounting** (`1.20.1`), **Barcode Service** (`1.17.1`), **OCR
Service** (`1.9.1`), **FTP Service** (`1.31.1`), **Operator Service**
(`1.40.2`) ve **Ideas Service** (`0.3.1`), yeni sürüm kanalı altyapısının bir
parçası olarak yeniden numaralandırıldı. Bu dönemde büyük görünen sürüm
sıçramaları herhangi bir özellik veya davranış değişikliği içermiyor.
**Docnet Service** (`1.54.6`) 19 Haziran'dan bu yana değişmedi.

<!-- Generated by the docbits-changelog skill (version-boundary mode: exact
     git ranges between the ALT (2026-07-03/04) and NEU (2026-07-09..14)
     version-bump commits supplied by the user, per service). -->

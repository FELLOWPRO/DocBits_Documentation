# DocBits Sürüm Notları — 14–29 Temmuz 2026

_29 Temmuz 2026'daki DocBits üretim yükseltmesinde (Nova kanal güncellemesi)
nelerin değiştiği — 14 Temmuz sürümünden bu yana yapılan her şeyi kapsıyor.
Her hizmet önce şu anda canlıda olan sürümü, ardından yenilikleri veya
düzeltmeleri sade bir dille listeliyor. Listelenmeyen hizmetlerde müşteriye
yönelik bir değişiklik olmadı._

---

## Öne Çıkanlar

- **İki faktörlü kimlik doğrulama.** DocBits hesapları artık ikinci bir
  faktörle korunabiliyor: bir kimlik doğrulayıcı uygulama (TOTP), e-posta ile
  gelen tek kullanımlık kod veya Touch ID, Windows Hello, YubiKey ve benzeri
  yollarla bir geçiş anahtarı. Yedek kodlar cihazın kaybolduğu durumu
  kapsıyor ve güvenilir olarak işaretlenen bir cihaz ikinci faktörü bir süre
  atlayabiliyor. Her kullanıcı bunu kendisi için açabilir; yöneticiler ise
  tüm kuruluş için zorunlu kılabilir. Bkz.
  [İki Faktörlü Kimlik Doğrulama kılavuzu](../two-factor-authentication.md).
- **Hata ekranından destek talebi.** Bir şeyler ters gittiğinde artık
  doğrudan hata kaydından destek talebi açabilirsiniz. Talep teknik bağlamı
  zaten içeriyor; sizin anlatmanız gerekmiyor.
- **Bölgeye uygun gelen e-posta.** ABD kuruluşları kendi bölgelerinde gelen
  içe aktarma adresleri alıyor ve ulusal bulut kiracılarındaki (GCC, 21Vianet
  ve benzeri) Microsoft 365 posta kutuları artık bir Cloud Instance seçimiyle
  yapılandırılabiliyor.
- **Daha net PO eşleştirme durumu.** Satır kalemi tablosu eşlenemeyen
  faturalar eskiden "satınalma siparişi bulunamadı" olarak etiketleniyor ve
  insanları yanlış sorunun peşine düşürüyordu. Artık hangi sütunun
  eşlenmediğini gösteren ayrıntılarla birlikte kendi "tablo eksik"
  durumlarını alıyorlar.
- **E-belgeler için vergi kodu eşleme.** Yeni bir ayarlar sayfası, elektronik
  belgeler için ERP vergi kodlarınızı eşliyor; dışa aktarmalar da eşlemeyi
  ERP'de başarısız olmak yerine en baştan denetliyor.
- **Turbo yapay zeka katmanı emekliye ayrıldı.** Turbo modeli kullanım
  ömrünün sonuna ulaştı. Bu modeli seçmiş olan herkes otomatik olarak Fast'e
  taşındı; yapmanız gereken bir şey yok.

---

## Web App — canlı: `10.46.2`

### Oturum açma

- **İki faktörlü kimlik doğrulama:** profilinizden bir kimlik doğrulayıcı
  uygulama, e-posta kodları veya bir geçiş anahtarı kurun, yedek kodları
  yazdırın ve bir cihazı güvenilir olarak işaretleyerek her seferinde
  sorulmasını önleyin. Geçiş anahtarı kullananlar tamamen parolasız giriş
  yapabiliyor. Kuruluş yöneticileri bir zorunlu kılma anahtarının yanı sıra
  kimlerin kaydolduğunu gösteren bir benimseme özeti elde ediyor.
- **Silinen hesaplar:** silinmiş bir hesapla giriş yapmak, genel bir hatayla
  başarısız olmak yerine bunu açıkça söylüyor.
- **SSO:** farklı bir bölge seçiliyken oturum açarken oluşan bir hata
  düzeltildi. SSO oturumları artık sabit bir yerel zamanlayıcıya göre değil,
  kimlik sağlayıcının belirttiği anda sona eriyor.

### Belgelerle çalışma

- **Silinen belgeler:** bu arada silinmiş bir belgeyi açmak, betik hataları
  yerine düzgün bir mesaj gösteriyor.
- **Alan Doğrulama:** sayfa numarası girişi daha geniş ve Enter'a
  basıldığında ilgili sayfaya atlıyor. Bir betikle salt okunur yapılan alan,
  alan bağlantısını göstermeye devam ediyor. Ham JavaScript yazdıran bir
  uyarı penceresi artık gerçek mesajı gösteriyor ve uzun e-belge satır kalemi
  tabloları içeren belgelerde ekran artık donmuyor.
- **Tablo çıkarımı:** bir sütunu silmek adını yeniden kullanılabilir hale
  getiriyor ve silinen başlıklar kaydedilen tabloda yeniden ortaya çıkmıyor.
- **Onaylar:** yeni beklemeye alınmış bir belgeyi açmak doğru onay ekranına
  götürüyor. Kullanıcılar artık gruplarının yetkisi olmayan bir Sales Tax
  adımını onaylayamıyor ve onay geçmişi yeniden tüm kayıtları gösteriyor.
  Geçmiş ayrıca onayı fiilen veren kişiyi de adıyla gösteriyor; bir
  yöneticinin atanan kişi adına verdiği onaylar buna dahil.
- **Tedarikçiler:** Muhasebe sayfası artık asılsız bir "Supplier is missing"
  (tedarikçi eksik) uyarısı göstermiyor ve yalnızca çıkarımdan var olan bir
  tedarikçiyi silmek artık iletişim kutusunu askıda bırakmıyor.
- **Ana veriler:** ana veriler sayfasındaki tablolar yeniden
  kaydırılabiliyor.
- **Görevler ve bildirimler:** bir görevi silmek artık yalnızca yöneticilere
  özel değil. Yönetici olmayan kullanıcıların kendi görevlerini silip
  silemeyeceği artık bir kuruluş ayarı ve açamadıkları bir belgede görevi
  olan kullanıcılar hata yerine yalnızca göreve özel bir görünüm alıyor.

### Pano ve arama

- **Dışa aktarma:** dışa aktarmalar seçili olan panoyu kullanıyor ve
  kaydedilmemiş değişiklikleri olan bir panoyu dışa aktarmadan önce uygulama
  sizi uyarıyor.
- **Arama:** Invoice Type, değer listesiyle birlikte arama alanı olarak
  kullanılabiliyor. Bir sonuç kümesi panonun gösterebileceği pencereden büyük
  olduğunda, sayı rozeti artık sessizce kırpmak yerine bunu belirtiyor.
- **İçe aktarma günlüğü:** bölünmüş belgeler üst belgeleri üzerinden
  bulunabiliyor ve Failed Filenames sütunu yalnızca gerçekten başarısız olan
  veya atlanan dosyaları listeliyor.

### Ayarlar ve yönetim

- **Destek talepleri:** doğrudan bir hata kaydından talep oluşturun. Talepler
  ortam ve sürüm kanalı bilgisini taşıyor; ekran görüntüsü yakalama da artık
  takılmıyor.
- **Gruplar ve yetkiler:** sınıflandırılmamış belgeler, diğer belge türleri
  gibi bir yetki olarak verilebiliyor.
- **Workflow Builder:** yeni oluşturulan veya yeniden adlandırılan kartlar,
  e-posta şablonları ve diğer açılır liste öğeleri sayfayı yeniden yüklemeye
  gerek kalmadan hemen görünüyor.
- **Karar Ağaçları:** tasarımcıdaki belge alanı etiketleri, her zaman
  İngilizce adı göstermek yerine arayüz dilini izliyor.
- **Belge Türleri:** çıkarım bölümünde yeni Structured Extraction ayarı.
- **E-Belge vergi kodları:** elektronik belgeler için ERP vergi kodlarınızı
  eşleyen yeni ayarlar sayfası (bkz. Öne Çıkanlar).
- **Auto Accounting:** boyutlar aralıklı olarak değil, güvenilir şekilde
  görünüyor.
- **Yapay zeka modeli seçimi:** emekliye ayrılan Turbo katmanı açılır
  listeden kaldırıldı; mevcut seçimler Fast olarak görünüyor.
- **Hizmet Sürümleri iletişim kutusu:** artık kaydırılabiliyor, Auth Bridge
  hizmetini içeriyor ve Vesta ile Nova sürüm kanalı adlarını gösteriyor.
- **İçe aktarma sayfası:** abonelik kaydı boş olan kuruluşlarda artık
  çökmüyor.

### Küçük düzeltmeler

Boş bildirim mesajları bastırılıyor, yeni/düzenle fikir iletişim kutusu
kaydırılabiliyor, alan ayarlarındaki kaymış onay kutuları yeniden hizalandı,
engellenen belge silme işlemleri nedenini açıklıyor ve E-Belge ayarları
Default'tan Custom'a geçişi sorunsuz ele alıyor.

## API Service — canlı: `12.68.1`

- **İki faktörlü kimlik doğrulama:** parola tabanlı tüm giriş yolları ikinci
  faktör denetiminden geçiyor; böylece hiçbir entegrasyon yolu bunu
  atlamıyor.
- **E-Belge vergi kodları:** elektronik belgeler için ERP vergi kodu
  eşlemesi; eksik kodların erkenden ortaya çıkması için dışa aktarmadan
  önce merkezi bir denetim yapılıyor.
- **Erişim denetimi:** yöneticiler, yönetici olmayan kullanıcılara
  sınıflandırılmamış belgeleri görme yetkisi verebiliyor.
- **Silme denetim izi:** belgeler, kimin ne zaman sildiğini kaydediyor.
- **Kişisel panolar:** kaydedilmeyen paylaşım ayarları düzeltildi.
- **Pano araması:** Invoice Type genişletilmiş arama alanlarına katıldı ve
  barkod veya QR bölmesiyle oluşturulan belgeler üst belgeleri üzerinden
  bulunabiliyor.
- **Pano güncelliği:** bir tabloyu yenilemek veya bir belgeyi yeniden
  işlemek pano önbelleğini temizliyor; böylece liste artık değişiklik
  öncesindeki değerleri göstermiyor.
- **Yüklemeler:** ağ yeniden denemesi sırasında aynı dosyanın tekrar tekrar
  yüklenmesi artık yinelenen belgeler oluşturmuyor.
- **Tedarikçi araması:** sonuçlar sabit bir bekleme süresi sonunda değil,
  veri hazır olur olmaz geliyor.
- **Infor dışa aktarma:** birim fiyatlar dört ondalık basamağı koruyor. M3
  dışa aktarmaları sıfır tutarlı satır masraflarını içerebiliyor ve negatif
  LN maliyet satırları pozitif alacak kayıtları olarak gönderiliyor. Dışa
  aktarma ayrıca iş akışının ortasında çalışmak yerine bekleyen bir iş
  akışının tamamlanmasını bekliyor.
- **Onaylar:** bir onay, yalnızca onaylayan kişi ilgili onay talebinin
  atanmış kişisi olduğunda o taleple ilişkilendiriliyor. Bir iş akışının
  kendi başına yaptığı değişiklikler, belgeye en son dokunan kişiye değil,
  System kullanıcısına atfediliyor.
- **Giriş kararlılığı:** token doğrulamasındaki geçici bir hata artık
  kullanıcıların oturumunu kapatmıyor; uygulama bunun yerine yeniden
  deniyor. Belgeler de aynı şekilde ele alınıyor ve kısa süreli bir kimlik
  doğrulama aksaklığında doğrudan başarısız olmuyor.
- **Sınıflandırma:** kaynak kuralları artık sabit konumlar yerine tüm belge
  kaynak alanlarıyla eşleştiriliyor.
- **Doğrulama kararlılığı:** adı olmayan bir alan artık belge doğrulamasını
  çökertmiyor.
- **Yapay zeka modelleri:** emekliye ayrılan Turbo katmanı, ince ayarlı
  varyantlar dahil her yerde Fast'e yeniden eşlendi; ayrıca emekli bir
  modelin asla çalıştırılamamasını sağlayan bir koruma eklendi.
- **Arka plan işleri:** takılan bir zamanlayıcı tespit edilip yeniden
  başlatılıyor; böylece yinelenen işler sessizce durmuyor.

## Auth Service — canlı: `1.75.3`

- **İki faktörlü kimlik doğrulama:** Öne Çıkanlar bölümündeki maddenin
  arkasındaki altyapı. Kimlik doğrulayıcı uygulamalar, e-posta ile tek
  kullanımlık kodlar, geçiş anahtarları ve güvenilir cihazların yanı sıra
  yedek kodlar, kuruluş bazında zorunlu kılma ve parolasız geçiş anahtarı
  girişi. Kaydolmak diğer oturumlarınızı kapatıyor, parolanızı değiştirmek
  güvenilir cihazları iptal ediyor ve doğrulama uç noktaları kilitlemeli hız
  sınırlaması ile yeniden kullanılan kodlara karşı bir tekrar koruması
  içeriyor.
- **Giriş geçmişi:** SSO/SAML üzerinden yapılan oturum açmalar artık giriş
  geçmişinde görünüyor ve son giriş zaman damgası her giriş türü için
  güvenilir şekilde kaydediliyor. Başka bir kullanıcının giriş geçmişini
  görüntülemek uygun yönetici düzeyini gerektiriyor.
- **Eski hesaplar:** eski tip bir kullanıcı hesabını silmek, sessizce hiçbir
  şey yapmamak yerine yeniden çalışıyor.
- **Toplu kullanıcı yönetimi:** mevcut kullanıcıları, e-posta adresine göre
  eşleştirilen CSV ile alt kuruluşlara ve gruplara toplu olarak ekleyin.
  Ayrıca düzensiz doldurulmuş CSV satırlarında oluşan bir çökme ile aynı
  anda iki veya daha fazla yeni kullanıcı eklerken oluşan bir sunucu hatası
  düzeltildi.
- **Üye listeleri:** silinen kullanıcılar artık alt kuruluş üye listelerinde
  görünmüyor.
- **Tek oturum açma:** bir dizi sağlamlaştırma düzeltmesi. Süresi dolan
  token'lar artık temiz bir "süresi doldu" yanıtı döndürüyor, SAML
  yapılandırması olmayan kuruluşlar yanlış bir giriş akışı yerine düzgün bir
  bulunamadı yanıtı alıyor, oturum kapatma isteği doğrulanamasa bile çıkış
  her zaman tamamlanıyor ve eksik kimlik sağlayıcı yapılandırması etrafındaki
  birkaç çökme giderildi. Sağlayıcının döndürdüğü token ömrü uygulamaya
  aktarılıyor.
- **Oturum token'ları:** süresi dolmamış olmasına rağmen kısa ömürlü oturum
  token'larının geçersiz diye reddedilmesi düzeltildi.
- **Yönetim araçları:** kuruluş bölgesi yönetim API'sinde görünüyor, bir
  kuruluşun sistem kullanıcısı yeniden atanabiliyor ve plan ile kullanım
  yönetimi özel uç noktalar kazandı. Bu değişiklikler müşteri uygulamasını
  değil, DocBits personel araçlarını etkiliyor.

## Email Service — canlı: `1.40.2`

- **Bölgeye uygun içe aktarma:** gelen e-posta alan adları artık her bölge
  için ayrı ayrı mevcut ve yanlış bölgeye ulaşan postalar doğru bölgeye
  yönlendiriliyor. ABD kuruluşları artık AB gelen posta yoluna bağımlı
  değil.
- **Microsoft 365:** ulusal bulut kiracıları bir Cloud Instance seçimiyle
  yapılandırılıyor; bu, ABD müşterileri için O365 içe aktarmalarını
  düzeltiyor. Geçersiz bir kiracı artık sunucu hatası yerine net bir giriş
  hatası üretiyor ve eksik kiracı kimlik bilgileri sessizce başarısız olmak
  yerine hemen bir mesajla başarısız oluyor.
- **Bağlantı testi:** yanıt vermeyen bir IMAP posta kutusunu test etmek, bir
  ağ geçidi zaman aşımına takılmak yerine birkaç saniye içinde bir zaman
  aşımı mesajıyla başarısız oluyor.
- **Gelen kutusu düzeni:** eki olmayan e-postalar gelen kutusunda birikmek
  yerine dışarı taşınıyor.
- **Yeniden denemede yineleme yok:** belge API'sine yapılan yüklemeler bir
  idempotency anahtarı taşıyor; böylece yeniden denenen bir teslimat aynı
  belgeyi iki kez oluşturamıyor.
- **Kaynak adlandırması:** klasör yapılandırılmış O365 kaynakları adlarında
  hesap e-postasını içeriyor; böylece benzer kaynaklar birbirinden ayırt
  edilebiliyor. Posta kutusu adresi, elle yazılan bir alandan değil, kimliği
  doğrulanmış hesaptan okunuyor.
- **İçe aktarma günlüğü temizliği:** içe aktarma günlüğü kayıtları 90 gün
  saklanıyor ve bu sürenin sonunda otomatik olarak temizleniyor.

## PO Match Service — canlı: `1.59.3`

- **"Tablo eksik" durumu:** satır kalemi tablosu eşlenemeyen faturalar,
  yanıltıcı "satınalma siparişi bulunamadı" yerine kendi durumlarını alıyor
  (bkz. Öne Çıkanlar). Pano bunu eşleşmedi simgesiyle gösteriyor.
- **Daha iyi hata ayrıntısı:** tablo eşleme hataları, eşlenemeyen sütunu
  adıyla belirtiyor.
- **Büyük faturalarda daha hızlı:** kurallara dayalı eşleştirme, adayları
  kalem numarasına göre gruplandırıyor ve tolerans ayarlarını her satır için
  değil, kuruluş başına bir kez okuyor.
- **Daha temiz API davranışı:** var olmayan PO kuralları için yapılan
  istekler düzgün bir bulunamadı yanıtı döndürüyor ve bozuk önbellek
  kayıtları tekrarlanan hatalara yol açmak yerine atılıyor.
- **Toplam üzerinden eşleştirme:** satınalma siparişi toplamıyla
  eşleştirmedeki bir hata düzeltildi.

## Fulltext Service — canlı: `1.39.1`

- **Avrupa sayı biçimleri:** ondalık virgülle yazılan tutarlar (`1.234,56`)
  dizinlemeden önce normalleştiriliyor; böylece tutar aramaları ve filtreler
  sayı biçiminden bağımsız çalışıyor.
- **Dürüst sonuç sayıları:** bir arama, panonun döndürdüğü pencereden daha
  fazla belgeyle eşleştiğinde, yanıt kırpılmış bir listeyi eksiksizmiş gibi
  sunmak yerine bunu belirtiyor.
- **ERP sayıları:** panodaki canlı sayım akışını kesebilen bir token hatası
  düzeltildi.
- **Dizinleme dayanıklılığı:** dizinleme artık geçici veritabanı ve kimlik
  doğrulama hizmeti aksaklıklarını atlatıyor (otomatik yeniden deneme,
  birincil veritabanına geri dönüş) ve hatalı biçimli kuyruk mesajlarını
  sonsuza kadar yeniden denemek yerine atıyor.

## OCR Service — canlı: `1.10.3`

- **Kararlı okuma sırası:** metin belirlenimci bir sırayla okunuyor; böylece
  aynı belge her seferinde aynı şekilde çıkarılıyor.
- **Büyük belgeler:** OCR süre bütçesi belge boyutuyla ölçekleniyor; çok
  büyük dosyalar artık zaman aşımıyla başarısız olmuyor.
- **Olağandışı karakterler:** bir temizleyici, OCR motorunun temsil
  edemediği karakterleri ayıklıyor; egzotik semboller içeren belgelerdeki
  hatalar giderildi.
- **Daha az geçici hata:** geçici depolama bağlantı hataları otomatik olarak
  yeniden deneniyor ve takılan bir işleyici, gerçekten iş tüketip
  tüketmediğine bakılarak tespit ediliyor.

## Extraction Service — canlı: `1.53.3`

- **Sıfır vergili ABD faturaları:** vergi tutarı sıfır olduğunda doğru
  net/vergi çiftinin atlandığı bir durum düzeltildi.
- **Tablo çıkarımı:** yapılandırılan eşleme belgenin sunduğundan daha fazla
  sütun beklediğinde tablolar düzenlenebilir kalıyor; ayrıca olağandışı
  satır verilerinde oluşan bir çökme düzeltildi.
- **Kararlı okuma sırası:** yukarıdaki OCR değişikliğini yansıtıyor; böylece
  çıkarım, OCR'ın ürettiği token sırasının aynısını görüyor.
- **Yapay zeka modelleri:** Turbo katmanının emekliye ayrılması, API
  Service'ten yansıtıldı.

## Docflow Service — canlı: `2.7.3`

- **İş akışlarında PO eşleştirme:** eksik karşılaştırma değerleri,
  uyuşmazlık yerine eksik veri olarak ele alınıyor.
- **Sipariş onayı kartları:** alıcı ve sorumlu kişi güvenilir şekilde
  çözümleniyor.
- **Teklif kartları:** günlük artık, teklif edilen bir fiyat var olduğu halde
  izin verilen tarih aralığının dışında kaldığında bunu kaydediyor; bu durum
  eskiden eksik veri gibi görünüyordu.
- **Navlun masrafları:** iki tarafta da masraf yoksa durum takılıp kalmak
  yerine operatör kartıyla çözülüyor.
- **Güvenlik:** iş akışı API token'ları ait oldukları kuruluşa göre
  doğrulanıyor.
- **Daha hızlı tetikleme:** etkin iş akışı denetimi önbelleğe alınıyor ve
  arka plan işleyicileri, arkalarında takılmış süreçler bırakmak yerine
  temiz bir şekilde yeniden başlıyor.

## Barcode Service — canlı: `1.18.1`

- **Uzun süren bölmeler:** uzun barkod işleri sırasında görev kuyruğu
  bağlantısı canlı tutuluyor; böylece büyük yığınları bölme işlemi artık
  sona doğru takılmıyor.

## FTP Service — canlı: `1.31.2`

- **İçe aktarma günlüğü temizliği:** Email Service ile aynı 90 günlük
  saklama süresi ve otomatik temizlik.

## Auth Bridge Service — canlı: `0.4.1`

- **Doğru çoğaltma uyarıları:** AB/ABD hesap çoğaltma köprüsü, bir takılmayı
  ilk hatadan değil son gerçek ilerlemeden itibaren ölçüyor ve yalnızca
  gerçek çoğaltma hareketini ilerleme olarak sayıyor. Gecelik asılsız "köprü
  takıldı" uyarıları ortadan kalktı. Uygulamada hiçbir şey değişmiyor.

## Operator Service — canlı: `1.42.1`

- **İşleyici kararlılığı:** takılan bir işleyici, iş tüketip tüketmediğine
  bakılarak tespit ediliyor ve işleyiciler arasındaki boş trafik kapatıldı.

---

## Bu sürümde değişmeyenler

**Auto Accounting** (`1.21.1`) müşteriye yönelik hiçbir değişiklik olmadan
yeniden derlendi. **Docnet** (`1.55.1`) ve **Ideas** (`0.3.1`) bu dönemde
herhangi bir değişiklik içermiyor.

<!-- Generated by the docbits-changelog skill. Boundary: versions live in the
     prod namespace on 28 Jul 2026 (Web App 10.41.8, API 12.57.8, Auth 1.71.1)
     up to the versions live in the sandbox namespace the same day, which is
     what the 29 July upgrade promotes. Re-check the version headers on the
     morning of the upgrade in case anything else lands on sandbox first.
     Manage Layouts and Custom Validation Rules stay excluded: DOCB-13719 gates
     both behind a beta query parameter, so they are not generally available in
     10.46.2. The hourly password for script changes (DOCB-13673) was added and
     then reverted inside this window, so it must not be announced. -->

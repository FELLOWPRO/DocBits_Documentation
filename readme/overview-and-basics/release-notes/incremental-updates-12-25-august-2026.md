# DocBits Sürüm Notları — 12–25 Ağustos 2026

_25 Ağustos 2026'daki DocBits üretim yükseltmesinde nelerin değiştiği —
12 Ağustos sürümünden bu yana yapılan her şeyi kapsıyor. Her hizmet önce
dağıtılan sürümü, ardından yenilikleri veya düzeltmeleri sade bir dille
listeliyor. Listelenmeyen hizmetlerde müşteriye yönelik bir değişiklik
olmadı._

---

## Öne Çıkanlar

- **Daha sıkı kuruluş izolasyonu.** Bir güvenlik taraması, bir kuruluşun
  verilerinin başka bir kuruluştan okunabildiği veya yazılabildiği birkaç
  noktayı kapattı: belge betikleri, alt kuruluş kullanıcı listeleri, grup
  üyelikleri ve bir belgenin işlem hattı boyunca taşıdığı işleme belirteci
  artık tamamı çağıranın kuruluşuna göre denetleniyor. Onaylar da dört göz
  ilkesini gerektiği gibi uyguluyor: ikinci onaylayan, birinciden farklı bir
  kişi olmak zorunda.
- **Belgeler artık takılı kalmıyor.** Belgelerin sonsuza kadar askıda
  kalmasına yol açan dört ayrı neden düzeltildi: reddedildikten sonra "Dışa
  aktarılıyor" durumunda kalan dışa aktarmalar, bir işleme adımı çöktüğünde
  donan yeniden başlatmalar, hiç geri bildirmeyen barkod bölmeleri ve
  "Hazırlanıyor…" üzerinde asılı kalan muhasebe ekranı. Her durumda belge
  artık ya tamamlanıyor ya da üzerine gidebileceğiniz gerçek bir hata
  gösteriyor.
- **Alacak dekontları alacak dekontu olarak tanınıyor.** CII sözdizimindeki
  XRechnung 3.0, 3.0.1 ve 3.0.2 alacak dekontları, saf CII alacak dekontları
  ve ZUGFeRD 2.4 / Factur-X 1.08 belgeleri artık doğru sınıflandırılıyor ve
  toplam doğru alandan okunuyor. Hem "fatura" hem "alacak dekontu" ifadesi
  geçen taranmış belgeler, hangi anahtar kelimenin belge türüne daha yakın
  durduğuna göre çözümleniyor; bir alacak dekontunu yeniden fatura olarak
  sınıflandırdığınızda tutarlar tekrar pozitife dönüyor.
- **PO eşleştirme güvenebileceğiniz bir aritmetik kullanıyor.** Toleranslar
  kayan noktalı değerler yerine tam ondalık sayılar olarak karşılaştırılıyor,
  satın alma siparişi değerini temel alıyor ve birden çok satın alma
  siparişine atıfta bulunan faturalar bunların tümüyle eşleştiriliyor. Hiç
  eşlemediğiniz sütunlar artık satır tutarı denetimini bozmuyor ve zorunlu
  sütunlar eksik olduğunda hata bunların adını veriyor.
- **İş akışı çalıştırmaları yaptıkları işi koruyor.** Bir alan değeri yazan
  iş akışı, bu değeri belgeye artık sonraki bir dışa aktarmanın sessizce geri
  alamayacağı şekilde yazıyor. Yeniden denenen tetikleyiciler çalıştırmanın o
  ana kadar yaptıklarını artık atmıyor ve aynı belgeye denk gelen iki
  tetikleyici birbirinin kilidini çalmak yerine sıraya giriyor.
- **Parola sıfırlama e-postaları yeniden gönderiliyor.** E-postalar sunucudan
  sessizce hiç çıkmıyordu. Sıfırlama formu da gönderimden sonra gerçek bir
  geri bildirim gösteriyor ve yanıt artık bir hesabın var olup olmadığını
  açık etmiyor.

---

## Web App — `10.55.0`

### Oturum açma ve hesaplar

- Parola sıfırlama yeniden uçtan uca çalışıyor: e-posta ulaşıyor, form
  gönderimi onaylıyor ve yanıt, adresin bir hesabı olup olmamasından
  bağımsız olarak aynı.
- Bir tarayıcı sekmesinde oturumu kapatmak diğer sekmelerin oturumunu da
  kapatıyor; sekmeler oturum konusunda anlaşamadığında beliren hata
  bildirimleri de artık yok.
- Kuruluşunuz iki faktörlü kayıt zorunlu tutuyorsa, oturum açma ekranı artık
  mesajsız başarısız olmak yerine bunu söylüyor. Bölgeler arası geçiş
  anahtarıyla oturum açma çevrilmiş hata mesajları gösteriyor ve gönder
  düğmesi görünür durumda.
- Yöneticiler, oturum açma kaydı kullanıma sunulmadan kuruluş genelinde MFA
  zorunluluğunu artık açamıyor; bu daha önce insanların dışarıda kalmasına
  yol açabiliyordu.

### Doğrulama ekranı

- Yakınlaştırma kaydırıcısı artık %150'ye kadar çıkıyor (eskiden %80'de
  duruyordu) ve bir tabloyu yakınlaştırmak, hiçbir şey yapmamak yerine
  kapsayıcı genişliğinin ötesinde de çalışıyor.
- Boş tutar alanları hata bildirimi üretmek yerine 0 sayılıyor ve hiçbir
  alan seçili değilken belge görüntüsüne çift tıklama yok sayılıyor.
- Belge kilidi başka bir oturumdayken gösterilen bandın hiç metni yoktu;
  artık kendini açıklıyor. Bir tabloyu etiketlemek, kendi değişikliğiniz
  hakkında yanlış bir "belge dışarıdan değiştirildi" uyarısını artık
  tetiklemiyor.
- Yapay zeka tablosunda, başka bir sütunun eşlemesini kaldıracak bir sütun
  yeniden eşlemesi önce onay istiyor; AMOUNT ve NUMBER sütunlarında sayı
  olmayan değerler işaretleniyor.
- "Çıkarılan tablo" sekmesi boş olduğunda yeniden elle tablo eğitimine
  bağlantı veriyor ve halihazırda bir yapay zeka tablosu varken artık
  sonsuza kadar dönmüyor.
- Karşılaştırma satır kalemi tablosundaki kalem numaraları tutarlar gibi
  yuvarlanmıyor, tanımlayıcı olarak gösteriliyor.
- Onaylayan alanları kullanıcı ve grup kimliklerini adlara çözümlüyor;
  böylece asla ham bir kimlik göstermiyor ya da boş kalmıyorlar. Görev son
  tarihleri UTC'ye duyarlı tek bir yoldan dönüştürülüyor, dolayısıyla her
  görüntüleyen aynı tarihi görüyor.
- Doğrulamaya geri gönderilen belgeler hazırlanırken ölü bir ekran yerine
  yükleme göstergesi gösteriyor.
- Büyük tedarikçi faturalarını açmak belirgin şekilde daha hızlı.

### Muhasebe

- Bölünmüş satır kalemleri Enter'a basıldıktan sonra % işaretini koruyor ve
  %0 bir değer olarak kabul ediliyor.
- Hesap filtresinde Enter, hiçbir şey yapmamak yerine eşleşen ilk hesabı
  seçiyor.
- Flexdimension karakterleri boyut kimliğine göre eşleniyor; böylece sıra
  farklı olsa bile boyutlar doğru sütuna düşüyor.
- Başarısız bir muhasebe hazırlığı, sonsuza kadar "Hazırlanıyor…" üzerinde
  asılı kalmak yerine bir hata mesajıyla toparlanıyor ve bir belgeyi yeniden
  açmak artık bir önceki belgenin bayat verisini sunmuyor.

### PO eşleştirme

- PO Eşleştirme'yi tüm zorunlu sütunlar eşlenmeden açmak yeniden mümkün;
  gerekli bir şey eksik olduğunda mesaj, eksik sütunları tek tek
  adlandırıyor.
- Hiçbir şeye eşlenmemiş sütunlar, size bir kez sorulduktan sonra ekran
  açılırken gizleniyor ve artık satır tutarı hesaplamasına karışmıyor.
- Eşleşen miktar kaydettikten sonra yenileniyor ve eksik sütun penceresi
  sizi sorunu düzeltebileceğiniz Alan Doğrulama sayfasına yönlendiriyor.

### Pano ve arama

- Açılır listeye dayalı sütunlar (fatura türü, durum ve benzerleri) ham
  saklanan değer yerine etiketlerini arayüz dilinizde gösteriyor.
- Serbest metin araması parantezleri düz metin olarak kabul ediyor; eskiden
  sorguyu reddediyordu. "Eşit değil" filtre işleci seçili kalıyor ve bir
  filtreyi elle düzenlemek artık alan adını bozmuyor.
- Hızlı aramada bir alt kuruluş seçmek uuid'sini değil adını ekliyor ve alt
  kuruluş otomatik tamamlaması artık yinelenen kayıtlar listelemiyor.
- Pano artık arama penceresi başına 10.000 belgeye kadar getirebiliyor;
  böylece büyük sonuç kümeleri doğru sayfalanıyor.
- Yinelenen belge paneli ana listeyle aynı çözümlenmiş sütunları gösteriyor
  ve birden çok kelimeden oluşan tedarikçi filtre değerleri Enter'a basınca
  kaybolmuyor.
- Kenar çubuğundaki açık görev sayacı, o sırada hangi belge açıksa onun
  bağlamını değil, sizin alt kuruluş bağlamınızdaki görevleri sayıyor.

### Görevler

- Kanban sütunları siz kaydırdıkça sayfalanıyor; böylece çok görevli panolar
  hızla yükleniyor.
- Atama e-postası bir görev atandığında ve yalnızca bir kez gönderiliyor.
  Bir görevi düzenlemek veya tamamlandı olarak işaretlemek e-postayı artık
  yeniden göndermiyor ve "atanma tarihi" atamanın yapıldığı tarih olarak
  kalıyor. Görev e-postaları Outlook'ta da düzgün görüntüleniyor.

### Workflow Builder

- İş akışı listesi, bir iş akışını açıp geri döndüğünüzde — gezinme yolu
  (breadcrumb) üzerinden dönüşler dahil — aramanızı, sıralama düzeninizi,
  sayfanızı ve sayfa boyutunuzu koruyor. Sayfa varsayılan olarak Liste
  sekmesinde açılıyor.
- Yerleşim oluşturucudaki "değişiklikte iş akışını çalıştır" anahtarı artık
  çalıştırmayı gerçekten denetliyor ve etkinleştirmek bir iş akışı seçmeyi
  gerektiriyor.

### Ayarlar ve yönetim

- WatchDog indirme bağlantısı ve kurulum komutu her zaman üretim ortamına
  değil, içinde bulunduğunuz ortama işaret ediyor.
- Karar Ağaçları: seçici yeniden açıldığında seçili belge alanı vurgulu
  kalıyor, kısaltılan etiketler araç ipucu alıyor ve satır eklerken ham
  kimlikler yerine kullanıcı adları gösteriliyor.
- Bir kullanıcıyı düzenlerken Sistem Yöneticisi onay kutusu düzenlenebilir.
- Ana Veri sayfası bir sıralama yarışı yüzünden artık boş gelmiyor ve
  rozetlere göre sıralamak sayfayı artık çökertmiyor.
- "İptal ediliyor" durumundaki bir abonelik sürdürülebiliyor.
- XSLT ayrıntı sayfası hiçbir şey göstermemek yerine yükleme hatalarını
  bildiriyor; e-posta bildirim ayarları çalışan bir günlük bölmesiyle tam
  sayfa genişliğini kullanıyor.
- Çok kuruluşlu kullanıcılar için kuruluş seçicinin satır düzeni,
  boyutlandırması ve tema renkleri doğru.
- Analitik: Core Web Vitals gerçek ölçüm verisinden çiziliyor, günlük
  hizmeti görünümü çalışıyor ve başarısız bir metrik isteği sıfırlar
  göstermek yerine bir hata durumu gösteriyor.
- Yerleşim yöneticisindeki "Varsayılan Şablonu Kullan" varsayılan yerleşimi
  amaçlandığı gibi kopyalıyor; eskiden çöküyor ya da varsayılan olmadığını
  iddia ediyordu.
- Özel alan etiketleri standart alanların hazır çevirilerini artık ezmiyor;
  Agent Wizard dahil DocNet (AI Workforce) ekranları çevrildi.
- Tedarikçi portalı teklifleri: izin verilen listenin dışında bir REF1
  değeriyle teklif göndermek engelleniyor, yönetilen ölçü birimleri satır
  kalemi tablosunda görünüyor ve onay biçimlendirmesi yalnızca sözleşme
  tekliflerine uygulanıyor.
- MediOrder, doğrulama ekranına yinelenen belge algılama özelliği kazanıyor.

## API Service — `12.82.3`

### Güvenlik ve kuruluş izolasyonu

- Etkin kuruluşu değiştirme isteği gerçek üyeliğinize göre doğrulanıyor ve
  doğrulanamazsa reddediliyor; kuruluşlar arasında geçiş için kötüye
  kullanılabilecek dahili bir test uç noktası kapatıldı.
- Belge betikleri artık kuruluşlar arasında okunamıyor veya üzerine
  yazılamıyor — ne belgeye uygulama çağrısıyla ne de kaydetme sırasında
  yabancı bir sürüm kimliğiyle.
- Alt kuruluş kullanıcı listeleri ve grup üyesi listeleri yalnızca çağıranın
  kuruluşundaki kişileri döndürüyor; bir gruba aynı anda birden çok kullanıcı
  eklemek artık ilki dışındakileri düşürmüyor.
- Yanlış kuruluştan bir kimlik bilgisi, bir belgenin işleme belirteci
  olmadan önce reddediliyor ve tam metin arama sorguları bir hizmet
  kimliğiyle değil, çağıran kullanıcı olarak çalışıyor.
- Dört göz onayı uygulanıyor: ikinci onaylayan, ilk onayı veren kişiden
  farklı olmak zorunda.
- Canlı PO Panosu listesi kullanıcının alt kuruluşlarıyla sınırlandırılıyor.

### Belge işleme hattı

- Dışa aktarımı reddedilen belgeler artık sonsuza kadar "Dışa aktarılıyor"
  durumunda beklemiyor ve dışa aktarma hataları boş bir mesaj yerine her
  zaman gerçek bir mesaj taşıyor.
- Bir işleme adımı çöktüğünde belge, çıkışı olmayan "yeniden başlatma
  sürüyor" durumunda takılmak yerine hata durumuna geçiyor.
- Başarısız olan veya zaman aşımına uğrayan bir barkod bölme, sessizce
  "Çalışıyor" göstermek yerine belgeyi Hata olarak işaretliyor; hiç alt
  belge üretmeyen bir bölme, her şeyi silmek yerine ana belgeyi koruyup
  işaretliyor.
- Başarısız bir yeniden deneme, bu arada işlenmesi tamamlanmış bir belgenin
  üzerine artık yazamıyor.
- Kullanıcı etkileşimi olmadan yeniden başlatılan belgeler ve bölme sonucu
  oluşan alt belgeler artık kalıcı bir kuruluş belirteciyle çalışıyor;
  böylece uzun süren işlemler süresi dolan bir oturum yüzünden ölmüyor.
- Boş bir yerleşim şablonu yanıtı artık altı saat boyunca önbelleğe
  alınmıyor; bu, önbellek süresi dolana kadar yerleşimlerin kaybolmasına yol
  açıyordu.

### Veri çıkarma ve e-belgeler

- Sonda eksi işaretiyle yazılan tutarlar ("100,00-") atılmak yerine negatif
  olarak ayrıştırılıyor.
- İsviçre belgeleri, Almanya kurallarına varsayılan olarak düşmek yerine
  İsviçre belgesi olarak algılanıyor (CHF, CHE KDV numaraları, CH
  IBAN'ları) ve tipografik tirelerle yazılmış tarihler doğru ayrıştırılıyor.
- CII sözdizimindeki XRechnung 3.0, 3.0.1 ve 3.0.2 alacak dekontları,
  toplamları genel toplam alanından okunarak alacak dekontu olarak
  sınıflandırılıyor; aynısı saf CII alacak dekontları için de geçerli.
  Bildirilen bir ZUGFeRD 2.4 / Factur-X 1.08 sürümü genel profil
  tanımlayıcısına üstün geliyor ve yalın XRechnung türleri başarısız olmak
  yerine UBL veya CII karşılığına çözümleniyor.
- Vergi Ülkesi ve Vergi Kodu gibi açılır liste (değer listesi) alanları,
  alan dönüşümü boyunca değerlerini koruyor; eskiden boşaltılıyorlardı.
- Tablo çıkarma: yalnızca sayılardan oluşan bir sütundaki hata tüm tabloyu
  öldürmek yerine o sütunla sınırlı kalıyor, yapay zeka tablo çıkarma çok
  partili çalıştırmalarda da geçerliliğini koruyan bir zaman aşımı kazanıyor
  ve alışılmadık tablo biçimlerinde (sayfa konumu olmayan satırlar, düzensiz
  sütun sayıları) yaşanan iki çökme düzeltildi.
- Kaynak kuralı desenleri büyük/küçük harfe duyarsız eşleşiyor.

### Dışa aktarma

- Dışa aktarma önizlemesi sırasında başarısız olan bir vergi denetimi, her
  iki önizleme uç noktasında da sunucu hatası yerine okunabilir bir hata
  döndürüyor.
- SFTP dışa aktarma, dönüştürülmüş belgenin yanında orijinal belgeyi de
  gönderebiliyor.
- Dışa aktarma yapılandırmaları birden çok düzeyde bulunduğunda, en özel
  olan tutarlı biçimde kazanıyor.
- BOD dışa aktarmaları, eşleme üzerinden sütun türü öznitelikleri
  taşıyabiliyor.

### İçe aktarma ve ana veriler

- E-posta İçe Aktarma Günlüğü eksiksiz: reddedilen ve başarısız olan gelen
  e-postalar her zaman doğru bir nedenle günlük satırı alıyor. Sessiz
  kayıplar bitti.
- Satın alma siparişi BOD içe aktarmaları alt satırları doğru satıra bağlı
  tutuyor; devralınan bir bayrak onları eskiden yanlış satıra bağlıyordu.
- Birden çok yeni tedarikçi içeren bir CSV'yi içe aktarmak çalışıyor
  (üretilen kimlikleri artık çakışmıyor), nakit iskonto koşulu takma adları
  içe aktarılıyor ve "çakışma durumunda" ayarına uyuyor; çakışma durumundaki
  IGNORE seçimi tedarikçilerin ötesinde de uygulanıyor.
- Tedarikçi önerisi (TF-IDF), bir tercih güncellendiğinde tedarikçi
  kimliğini koruyor; böylece öneriler artık boşluğu işaret etmiyor.

### Diğer düzeltmeler

- Pano satırları, isteği bloklamadan açılır liste etiketlerini kullanıcının
  dilinde çözümlüyor.
- Alanlar düzenlendikten sonra PO eşleştirme durumu, düzenleme öncesi durumu
  göstermek yerine güncelleniyor.
- Satın Alma Siparişi Değişikliği belgeleri, Satın Alma Siparişi ile
  eşdeğer beş alan ve varsayılan bir alan doğrulama yerleşimi kazanıyor.
- 152 uç noktadaki hata yanıtları ham istisna nesneleri yerine okunabilir
  mesajlar döndürüyor ve günlük analitiği sayfası, günlük dizini olmayan
  kuruluşlar için artık 502 ile yanıt vermiyor.

## Auth Service — `1.77.9`

- Parola sıfırlama e-postaları sessizce hiç gönderilmiyordu; altında yatan
  iş parçacığı güvenliği sorunuyla birlikte düzeltildi.
- Yeniden oynatılan bir yenileme belirteci (refresh token) reddediliyor:
  yetkili veritabanı denetimi, önbellek isabetinde atlanmak yerine artık
  her seferinde çalışıyor.
- İki faktörlü kimlik doğrulama: e-posta kodlarının yanına bir kimlik
  doğrulayıcı uygulama kaydedilebiliyor; son geçiş anahtarını kaldırmak veya
  yedek kodları yeniden üretmek önce taze bir ikinci faktör gerektiriyor.
- Geçerli bir alt kuruluş kimliği artık "Organization not found" hatasıyla
  reddedilmiyor ve bir alt kuruluşta oluşturulan API anahtarı, teknik
  kullanıcısını o alt kuruluştan çözümlüyor.
- Bir kuruluşu düzenlemek iş ortağı kimliğini doğruluyor ve yan etki olarak
  kuruluş türünü artık sıfırlamıyor.
- Abonelik görünümündeki "Kalan token" değeri takvim yılına değil, sözleşme
  yılına bağlı.

## Auth Bridge Service — `0.5.7`

- AB ve ABD bölgeleri arasındaki hesap çoğaltması kendi kendine
  toparlanıyor. Kopan bir çoğaltma akışı yerinde yeniden bağlanıyor, bir
  mutabakat çalışırken çoğaltma akmaya devam ediyor ve mutabakat belleği
  sınırlandığı için hizmet büyük tablolarda artık çökme döngüsüne girmiyor.

## Barcode Service — `1.18.7`

- Barkod okuma bir süre sınırı altında çalışıyor ve asılı kalmak yerine
  zaman aşımı bildiriyor; bu durum eskiden belgeyi işlemede takılı
  bırakıyordu.

## Docflow Service — `2.9.8`

- Bir iş akışı kartının yazdığı alan değerleri, belgeye saklanan her iki
  gösterimde de işleniyor; böylece sonraki bir dışa aktarma bunları artık
  geri almıyor.
- Yeniden denenen bir tetikleyici, çalıştırmanın o ana kadar yaptığı işi
  koruyor; aynı belge üzerinde çekişen tetikleyiciler kilidi çalmak yerine
  sıraya giriyor ve yükseltilen bir yeniden deneme kuyrukta öne alınıyor.
- Satın alma siparişi karşılaştırma kartları: toleranslar tam ondalık
  sayılar olarak karşılaştırılıyor ve satın alma siparişi değerini temel
  alıyor, ters karşılaştırma yönleri seçenek olarak sunuluyor, grup ataması
  bir kullanıcı kimliği karşılaştırmasında başarısız olmak yerine grup
  olarak raporlanıyor, atama kimlikleri UUID olarak doğru karşılaştırılıyor,
  boş sayısal değerli satırlar atlanıyor ve hiç teslim alma verisi olmayan
  bir "teslim alınan" karşılaştırması eşleşmiş gibi yapmak yerine eksik
  veri bildiriyor.
- Apply Decision Table (Karar Tablosu Uygula) kartı emekliye ayrıldı.

## Email Service — `1.41.0`

- Gmail içe aktarmaları her eki tam olarak bir kez alıyor; çakışan
  getirmelerden kaynaklanan yinelenenler ortadan kalktı.
- İçe aktarma okuma imleci yalnızca bir içe aktarma onaylandıktan sonra
  ilerliyor; böylece içe aktarmanın ortasındaki bir çökme artık e-posta
  atlanmasına yol açamıyor.
- Benzeri bulunduğu için devre dışı bırakılan bir içe aktarma
  yapılandırmasında bu devre dışı bırakma artık sessiz değil; görünür ve
  bildiriliyor.

## Extraction Service — `1.54.5`

- Bir belgenin alacak dekontu mu yoksa fatura mı olduğu, "ilk eşleşen
  kazanır" yerine hangi anahtar kelimenin belge türü ifadesine daha yakın
  durduğuna göre çözümleniyor.
- Birden çok vergi yorumu tolerans içinde kaldığında, kıl payı tutan yerine
  tam tutan mutabakat tercih ediliyor.
- Zorunlu bir yeniden OCR'dan sonra belge türü ve yerel ayar geri
  yükleniyor; böylece yeniden OCR'lanan belgelerde tablo çıkarma ve eğitim
  yeniden çalışıyor.
- Belge türü olmayan belgeler tablo kuralı aramasını artık çökertmiyor.

## FTP Service — `1.32.8`

- Klasör tarama, sınırlı bir derinlikle klasör başına tek listeleme
  gidiş-dönüşü yapıyor; böylece büyük FTP dizinlerinden içe aktarmalar çok
  daha hızlı ve artık zaman aşımına uğramıyor.

## Fulltext Service — `1.42.3`

- Saklanan arama verisinde çıkarılmış alan bulunmayan belgeler veritabanından
  yeniden dizinleniyor; böylece pano aramasında yeniden görünüyorlar.
- Pano arama penceresi 10.000 belgeye kadar destekliyor.
- Anlamsal arama etkinken faset aramaları artık başarısız olmuyor.

## OCR Service — `1.10.7`

- OCR süre bütçesi gerçek sayfa başına maliyete göre boyutlandırılıyor;
  böylece uzun belgeler işlem hattı sınırına takılmak yerine tamamlanıyor.

## PO Match Service — `1.59.8`

- Miktarı sıfır olan tablo satırları, yanlış uyuşmazlıklar üretmek yerine
  uyuşmazlık denetimlerinde atlanıyor.
- Gerekli PO eşleştirme sütunları eksik olduğunda sonuç bunların adını
  veriyor.

# DocBits Sürüm Notları — 15 Eylül 2026

_15 Eylül 2026'daki DocBits üretim hotfixinde (R1.0.13 sürümü) nelerin
değiştiği — 1 Eylül sürümünden bu yana yapılan her şeyi kapsıyor. Her hizmet
önce dağıtılan sürümü, ardından yenilikleri veya düzeltmeleri sade bir dille
listeliyor. Listelenmeyen hizmetlerde müşteriye yönelik bir değişiklik
olmadı._

---

## Öne Çıkanlar

- **Pano araması için tek bir kural seti.** `field=value` artık her arama
  motorunda tam olarak bu değer anlamına geliyor, `field:value` içerir
  anlamına geliyor (ile başlar ve ile biter için `value*` ve `*value`),
  `field!=value` ise hiç değeri olmayan belgeleri de döndürüyor. Etiketsiz
  bir arama, satın alma siparişi numaraları, barkodlar ve talep numaraları
  dahil her alanda alt dize araması yapıyor. Sonuç sayısı, durum kutucukları
  ve sayfalama aynı belge kümesini tanımlıyor; sonuç penceresine takılan ya
  da tam metin dizini olmadan çalışan bir arama "tamamlandı" demek yerine
  bunu belirtiyor. Panonun kendi arama bağlantısı (WebSocket) daha önce tam
  metin dizinine hiç ulaşmıyordu; artık ulaşıyor.
- **Tedarikçiler daha sık tanınıyor.** Bir arama alanı (vergi numarası,
  IBAN, tedarikçi numarası) tam olarak bir tedarikçiyle eşleştiğinde, ad
  gibi geniş bir alan birden çok tedarikçiyle eşleşse bile o tedarikçi
  kullanılıyor. XRechnung CII ve Facturae belgeleri tedarikçi alanlarını
  yeniden taşıyor. Ana verilerin çıkarılan bir değerin yerine geçtiği
  durumlarda doğrulama ekranı bunu belirtiyor ve orijinali geri yüklemenize
  izin veriyor.
- **Satın alma siparişi eşleştirme kendini açıklıyor.** Ekran neden eşleşme
  olmadığını söylüyor, uyuşmazlık ipucu başarısız olan sütunu adlandırıyor,
  eşleştirme geçmişi çalışan dönüşüm kurallarını listeliyor ve satın alma
  siparişi birim fiyatları net tutardan türetiliyor. Yedek kuralı olmayan
  kuruluşlarda elle eşleştirme yeniden çalışıyor, kaldırılan satın alma
  siparişleri kaldırılmış kalıyor ve sonlandırılan bir eşleştirme görevi
  belgeyi sonsuza kadar "Kuyruk"ta bırakmak yerine başarısız olarak
  işaretliyor.
- **Takılan belgeler ve yanlış hatalar.** Sürekli yükleme yapan kuruluşların
  belgeleri, mesai saatlerinde hiç hizmet verilmeyen bir kuyruk önceliğine
  düşürülüyordu (bir müşteride 866 belge "yeni" durumunda takılı kaldı).
  Bir yeniden deneme tarayıcısı, başarıyla dışa aktarılmış bir belgenin
  üzerine saatler sonra "hata" yazabiliyor ve bunun için dışa aktarma hatası
  e-postasını gönderebiliyordu. Bu yol kapatıldı.
- **Touchless Intelligence.** Kaç belgenin DocBits'ten insan dokunuşu
  olmadan geçtiğini ölçen Analitik sekmesi ilk tam sürümüne kavuşuyor: yapay
  zeka tavsiyeli sorun kümeleri, toplu analiz, önizleme, uygulama ve geri
  alma içeren değişiklik önerileri, eğilim ve örnekler içeren bir tedarikçi
  sayfası, belge başına işlem hattı akış diyagramı ve bir belgenin neden
  geçmediğini söyleyen bir satın alma siparişi kural seti diyagramı.
- **Büyük verilerde daha hızlı.** Soğuk oturum açmalar 33 sn'ye kadar süren
  kredi defteri toplamını atlıyor, muhasebe açılır listesi 2.000'den fazla
  hesabı olan kuruluşlarda çalışıyor, E-Belgeler kurallar sayfası 1.600
  kuralını tarayıcıyı dondurmak yerine sunucuda sayfalıyor ve satın alma
  siparişi panosundaki Yenile, önbelleğe alınmış bir liste yerine taze veri
  döndürüyor.
- **Güvenlik.** Ön yüz kaynak haritaları artık her dağıtımla birlikte
  gönderilmiyor, ana veri arama filtreleri sorguya eklenmek yerine SQL
  parametresi olarak bağlanıyor, süresi dolmuş bir belirteç önbellek
  isabetinde bile reddediliyor ve işleme belirtecindeki kuruluş denetimi
  önündeki katmandan bağımsız olarak uygulanıyor.

---

## Web App — `10.66.3`

### Oturum açma ve hesaplar

- Oturum açma daha hızlı. Oturum açmadaki abonelik denetimi, milyonlarca
  defter satırını toplayan ve çoğu zaman istemcinin 10 sn zaman aşımını aşan
  tam kredi bakiyesini istiyordu. Oturum açma artık yalnızca bir aboneliğin
  var olup olmadığını soruyor; bakiyeler Ayarlar → Abonelik sayfasında
  hesaplanmaya devam ediyor.
- Bölge değiştirmek (AB ↔ ABD) oturumunuzu açık tutuyor. Hedef bölge, oturum
  çoğaltılana kadar birkaç saniye boyunca "geçersiz belirteç" yanıtı veriyor
  ve iki kod yolu bunu ölü bir oturum olarak okuyordu.
- Sandbox'ta sonsuza kadar yeniden yükleme yapan "Updating DocBits
  v10.59.3.1 → v10.59.3.1" katmanı düzeltildi. Aynı sürüme yeniden yükleme
  artık katmanı göstermiyor, döngü sekme başına sınırlandırıldı ve tekrar
  olursa bir bant elle kurtarma seçeneği sunuyor.
- Yöneticiler Analitik Panosu sekmesini belirli rollere verebiliyor ve rol
  değişiklikleri güvenilir biçimde kaydediliyor.
- Sistem Yöneticisi onay kutusu mevcut bir kullanıcıda işaretlenebiliyor. Ön
  yüzden sistem yöneticisi oluşturmak artık etkili oluyor; bir eşitleme işi
  bayrağı her çalışmada sıfırlıyordu.
- Ayarlar → Roller: sunucu hatayla yanıt verdiğinde üye listesi bir
  yükleyicinin arkasında asılı kalmak yerine görüntüleniyor.
- DocBits MCP sunucusunda oturum açmak iki faktörlü kimlik doğrulamayı ve
  tek kullanımlık onayı zorunlu kılıyor.

### Pano ve arama

- Arama yardımı açılır penceresinde de açıklanan yeni işleç kuralları: `=`
  tam olarak bu değer (büyük/küçük harfe duyarsız), `:` içerir, `: value*`
  ile başlar, `: *value` ile biter, `!=` değeri olmayan belgeler dahil tam
  olarak bu değer olmayan her şey. Tırnak işaretleri yalnızca boşluk içeren
  bir değeri gruplar.
- `"Johnson and Johnson"` gibi tırnak içindeki bir ifade tek bir ifade
  olarak aranıyor. Tırnak içindeki "and" ve "or" artık bağlaç olarak
  okunmuyor.
- Etiketsiz bir arama hiçbir şey bulamadığında pano kuralı açıklıyor ve tek
  tıklamalık etiketler sunuyor (`Invoice number : <term>`,
  `Purchase order : <term>`, `Supplier ID : <term>`).
- Sıfır sonuçlu bir arama sayfalayıcıyı ve sayfadaki her sayacı sıfırlıyor.
  Daha önce sayfalama, önceki aramanın sayısını koruyordu.
- Satın alma siparişi numaraları, sipariş numaraları, barkodlar, fatura
  türleri ve talep numaraları etiket olmadan bulunabiliyor.

### Doğrulama ekranı

- Ana verilerin yerine geçtiği değerler işaretleniyor. Kehribar renkli bir
  rozet orijinal ve geçerli değeri, veri kümesini ve nasıl eşleştiğini
  gösteriyor; bir düğme çıkarılan değeri geri yüklüyor. Ana verilerle
  doğrulanan veya satın alma siparişinden doldurulan değerler kendi
  etiketlerini alıyor. Daha önce hepsi "Kaydedilmiş kurallarla çıkarıldı"
  rozetini taşıyordu.
- Onay damgası, sayfa zaten başka bir ek açıklama taşısa bile kaydediliyor.
  Bu durumda indirilen açıklamalı belgelerde damga eksikti.
- "Eşlenmemiş sütunları gizle", elle eğittiğiniz sütunları (örneğin Kalem
  Numarası ve Satın Alma Siparişi) koruyor.
- Bir sayfa numarası yazıp ardından bir alan için kutu çizdikten sonra
  çıkarma kurallarını kaydetmek çalışıyor. Bu sıralama eskiden kaydetmeyi
  çökertiyordu.
- Yapılandırılmış çıkarma tedarikçi başına açılabiliyor: doğrulama ekranının
  tfidf açılır penceresinde ve Ayarlar → Sınıflandırma ve Çıkarma sayfasında
  salt okunur bir sütun olarak.
- Train Model (Modeli Eğit) arka planda çalışıyor. Ekran "eğitim başladı"
  gösteriyor, sonucu yokluyor ve başarı ya da başarısızlığı bildiriyor.
  Büyük kuruluşlar, eğitim sunucu tarafında devam ederken ağ geçidi hatası
  alıyordu.
- Karanlık mod: bölme ekranındaki makas imleci ve Auto Accounting
  ekranındaki mod anahtarı yeniden okunabiliyor.

### Satın alma siparişi eşleştirme

[8 Eylül 2026 Hotfixleri](incremental-updates-8-september-2026.md)
sayfasında duyurulan değişiklikler bu sürümle üretime ulaşıyor: eşleşme
kaydetmeden sonra korunuyor, satın alma siparişi numarası düzeltildiğinde
eşleştirme yeniden çalışıyor, ekran neden eşleşme olmadığını ve bir
eşleşmenin neden tutulmadığını söylüyor, eşleştirme geçmişi dönüşüm
kurallarını gösteriyor ve satın alma siparişi birim fiyatı net tutardan
hesaplanıyor. Buna ek olarak:

- Uyuşmazlık ipucu eşleşmeyen sütunu adlandırıyor. Yalnızca eşleşen sütunlar
  kaydedildiği için eskiden boştu ve ekran yalnızca "Mismatched"
  diyebiliyordu.
- "PO Auto Match and Export" açıkken Auto Match düğmesi belgeyi de dışa
  aktarıyor. Daha önce dışa aktarma yalnızca belge panodan "PO Match" ile
  açıldığında gerçekleşiyordu.
- Miktar/birim fiyat tolerans açılır penceresi, sunucu kaydetmeyi
  reddettiğinde açık kalıyor; böylece girilen değerler kaybolmuyor.
- Satın alma siparişi panosundaki Yenile düğmesi yeniden yüklemeden önce
  sunucu tarafı önbelleği temizliyor. ERP'den içe aktarılan bir satın alma
  siparişi ancak yedi-sekiz dakika sonra görünüyordu.
- PO eşleştirme kuralları sayfası kural setini bir akış şeması olarak
  çiziyor ve eşleştirme geçmişi eylem araç çubuğuna taşındı.

### Otomatik muhasebe

- 2.000'den fazla hesabı olan kuruluşlar hesap listesini sunucuda arıyor.
  Bu tür kuruluşlarda açılır liste sandbox'ta boştu ve sayfa yüklemeleri
  beş saniye sürüyordu.
- Bir belgenin atıfta bulunduğu hesaplar toplu olarak çözümleniyor: satır
  başına iki bölme içeren 100 satırlık bir belge 403 yerine 4 istek
  gerektiriyor.
- Auto Accounting ve PO tablolarının başlıkları sabit kodlanmış bir metin
  yerine yerleşim oluşturucuda ayarlanan etiketi izliyor.

### Ayarlar

- Ayarlar → E-Belgeler → Kurallar, 1.600 kurallık kataloğu sunucuda
  sayfalıyor, arıyor ve sıralıyor. Sekme eskiden her kuralı aynı anda
  işliyor ve tarayıcıyı donduruyordu. "Tümünü sıfırla" kural başına bir
  çağrı yerine tek çağrı.
- Belge türü Gelişmiş Ayarları her anahtarın kayıtlı durumunu gösteriyor.
  Kaydedilmiş bir `false`, `0` tolerans veya boş bir seçim varsayılanla
  değiştiriliyordu ve belge türleri arasında geçiş yapmak önceki türün
  değerlerini geride bırakıyordu.
- Dönüşüm kuralları: bir "Değer ata" (Set value) eylemi kaydediliyor.
  Düzenleyici bunu sunucunun reddettiği bir adla gönderiyordu.
- Değer Listesi: kenar çubuğu yeni bir listeyi yeniden yükleme olmadan
  gösteriyor ve silinen bir listeyi düşürüyor; önceki bir listeden gelen geç
  yanıtlar artık geçerli listenin üzerine yazmıyor.
- Belge alt türleri bağlantısı standart belge türlerinde gösteriliyor.
- SMB dışa aktarmasının JPL eşlemesi `.properties` olarak indiriliyor;
  böylece dosya yeniden yüklenebiliyor. Dosya `.xml` olarak adlandırılıyor
  ve geri yüklenirken reddediliyordu.

### İş akışları

- Bir iş akışını yeniden adlandırmak aynı oturumda yapılan kart
  değişikliklerini koruyor. Yeni iş akışları tek bir kaydetme isteğiyle
  oluşturuluyor ve şablon yeniden adlandırmaları kalıcı hale getiriliyor.
- Dışa aktarılan bir iş akışı dosyası tüm dışa aktarma zarfını (sürüm, ad,
  açıklama) içeriyor. Gelişmiş iş akışları yeniden içe aktarılabiliyor; daha
  önce dosya sürümünü kaybediyor, standart iş akışı olarak okunuyor ve
  reddediliyordu.
- İş akışı listesindeki sütun filtreleri VE ile birleşiyor. Bir ad ve bir
  tarih filtresi etkinken yalnızca ada uyan satırlar sonuca sızıyordu.
- Görev son tarihleri listede, panoda ve ayrıntı görünümünde kullanıcı
  ayarlarınızdaki tarih biçimini kullanıyor.

### Analitik: Touchless Intelligence

Touchless sekmesi (Analitik → Touchless), kaç belgenin DocBits'ten bir kişi
dokunmadan geçtiğini ve diğerlerinin neden geçmediğini ölçüyor. Bu sürüm onu
tamamlıyor:

- **Kanıtlı sorun kümeleri.** Dokunuş gerektiren belgeler nedene göre
  gruplanıyor. Her küme kartı başarısız olduğu alanları, doğrulama kodlarını
  ve hata mesajlarını, ayrıca tedarikçisini adlandırıyor ya da tedarikçi
  olmadığını söylüyor. DocBits'in düzeltebileceği kümeler (bir kural, bir
  alan ayarı) yalnızca tedarikçinin düzeltebileceklerinden ayrılıyor ve
  yapay zeka analiz bütçesi önce düzeltilebilir olanlara gidiyor.
- **Yapay zeka analizi, öyle olduğu belirtilerek.** Bir küme kartı,
  tavsiyeyi bir dil modelinin mi yoksa bir kuralın mı yazdığını, analizin
  neyi saydığını ve ne zaman geçerliliğini yitirdiğini, bir tıklamanın
  önbelleğe alınmış bir analizi yeniden kullanıp kullanmayacağını söylüyor.
  Yapay zeka danışmanı bu ortamda çalışamıyorsa sekme nedenini belirtiyor.
- **Toplu analiz.** Birçok kümeyi tek çalıştırmada analiz edin,
  çalıştırmanın küme küme ne yaptığını görün ve sonuçları sonradan bulun.
  Sonuç listesi gezinme ve yeniden yüklemeden sonra da kalıyor ve
  çalıştırma bir alt kuruluş görünümünde artık "Running · 0/6 done"
  üzerinde asılı kalmıyor.
- **Değişiklik önerileri.** Bir tavsiye, üzerinde işlem yapabileceğiniz bir
  şeye dönüşüyor: kart önerilen değişikliği dört soruyla açıklıyor,
  ayarlamanıza izin veriyor, ne yapacağını önizliyor (hiçbir şey
  kaydedilmez), uyguluyor, etkiyi ölçüyor ve geri alabiliyor. Düzeltme
  adımları, adlandırdıkları ayarlar sayfasına belge türü, alan veya kurala
  göre önceden filtrelenmiş derin bağlantı veriyor.
- **Tedarikçi sayfası.** Sekmeden bir tedarikçi seçin veya fırsat kuyruğunda
  ada ya da numaraya göre arayın. Sayfa tedarikçinin zaman içindeki
  Touchless oranını (30 günden 1 yıla), sorunlu belgelerini ve iyi giden
  belgeleri gösteriyor ve tedarikçi başına yapay zeka teşhisi sunuyor. En
  fazla beş tedarikçi yan yana karşılaştırılabiliyor. Dahili bir karma
  değeri yerine tedarikçi numarası gösteriliyor.
- **İşlem hattı akışı.** Belge başına ve küme başına bir diyagram; alım,
  sınıflandırma, e-belge denetimi, tedarikçi, OCR, çıkarma, doğrulama, PO
  eşleştirme, onay ve dışa aktarma boyunca izlenen yolu ve belgeyi durduran
  aşamayı gösteriyor.
- **Satın alma siparişi eşleştirme, açıklanmış.** PO kural seti ayarlar
  sayfasında ve Touchless'ta bir akış şeması olarak çiziliyor; bir belgenin
  izlediği yol ve neden geçmediğine dair sade bir dille yazılmış neden de
  gösteriliyor. Neden kodları "satın alma siparişi bulunamadı"yı "satır
  uyuşmazlığı" ve "zorunlu alan eksik"ten ayırıyor.
- **Bölümleme.** KPI'lar, kümeler ve öneriler bir belge alanına göre
  bölünebiliyor; örneğin Sipariş Türü = Doğrudan / Dolaylı.
- **Doğru sayılar.** KPI kutucukları alt kuruluş filtresine uyuyor ve
  yalnızca ayrıntı görünümünün listeleyebildiği belgeleri sayıyor.
  Kuruluşun sistem kullanıcısının tarayıcı oturumu insan sayılıyor; böylece
  elle düzeltilen belgeler artık dokunmasız olarak dosyalanmıyor.
- Raporun araç çubuğu geniş ekranlarda denetimlerini sığdırıyor ve karanlık
  mod renkleri temadan geliyor.

### DocNet

- Etkinlikler akışı, Son Etkinlik pencere öğesi ve görev (mission) zaman
  çizelgesi çevrildi. Denetim özetleri 22 dilin tümünde İngilizceydi.
- Ajanlar, belge türünün tanımladığı ancak çıkarmanın boş bıraktığı alanları
  görüyor. Eskiden bu tür alanların var olmadığı sonucuna varıyor ve yazma
  denemesi yapmadan zorunlu güncellemeleri atlıyorlardı.

### Güvenlik

- Ön yüz kaynak haritaları her dağıtımdan çıkarılıyor. Üretim dahil her
  ortam bunları sunuyordu.

---

## API Service — `12.83.156`

### Tedarikçi tanıma ve ana veriler

- Bir arama alanı benzersiz olduğunda tedarikçi tanımlanıyor. Birden çok
  aranabilir alanda sonuçlar birleşim olarak birleştiriliyordu; bu yüzden
  dört tedarikçiyle eşleşen geniş bir ad eşleşmesi, tam olarak bir
  tedarikçiyle eşleşen vergi numarasını bastırıyordu. Hiçbir şeyle
  eşleşmeyen alanlar artık eşleşen alanları veto etmiyor. Alanların birlikte
  nasıl çalıştığı için bkz.
  [Ana Veri Ayarları](../../administration-and-setup/settings/global-settings/document-types/fields/master-data-settings.md).
- Ana veri değiştirmeleri kökenleriyle birlikte kaydediliyor: veri kümesi,
  yapılandırma, kaynak alan, işleç ve eşleşme türü. Doğrulama ekranı bunu
  gösteriyor ve çıkarılan değeri geri yükleyebiliyor.
- Nakit İskonto Koşulu tedarikçi BOD'undan içe aktarılıyor; ERP ile
  eşitlenen tedarikçilerde boştu. Tam kod olarak girilen bir İskonto Koşulu
  Geçersiz Kılma ("143", "012", "X08") uygulanıyor; daha önce yalnızca yüzde
  ön ekine bakılıyordu.
- Ana veri aramaları sayfa başına 1.000 satırla sınırlandırılıyor ve SQL'de
  pivotlanıyor. 19.000 kayıtlık bir arama çağrı başına beş saniye sürüyor
  ve API'yi engelliyordu.
- Ana veri aramasındaki filtre özellik adları ve veri türleri SQL
  parametresi olarak bağlanıyor. Sorguya doğrudan ekleniyorlardı.

### Belge işleme

- Sürekli yükleme yapan bir kuruluşun belgeleri, kuyruğun yalnızca daha
  yüksek öncelikli her şey boşken hizmet verdiği 9 önceliğine
  düşürülüyordu. Düşürme artık 3 ile sınırlı. Takılan belgeleri yeniden
  kuyruğa alması gereken mutabakatçının üretimde çalışan kimlik bilgileri
  yoktu; artık var.
- Tamamlanmış, dışa aktarılmış bir belgenin üzerine asla "hata" yazılmıyor.
  Hiç temizlenmeyen bir iş akışı bayrağı, yeniden deneme tarayıcısının
  başarıyla dışa aktarılmış bir belgeyi dakikada bir almasına yol açıyordu;
  ta ki yeniden deneme sınırı, dışa aktarmadan 2 sa 17 dk sonra belgeye
  "hata" damgası vurup müşterinin dışa aktarma hatası e-postasını gönderene
  kadar.
- Birleştirme ve ekleme `.PDF` ve `.Pdf` dosyalarını kabul ediyor.
  `SCAN0001.PDF` adlı tarayıcı çıktısı "Only PDF files are allowed."
  hatasıyla reddediliyordu.
- Önbellek geçersiz kılma anahtar alanını iki kez yerine bir kez tarıyor ve
  yalnızca bir BOD'un değiştirdiği arama veri türlerini temizliyor. Her BOD
  eskiden kuruluşun tüm arama önbelleğini siliyor ve herkesin anahtarlarını
  gezerken API'yi engelliyordu.
- Model yeniden eğitimi arka plan görevi olarak çalışıyor ve arayüzün
  yokladığı bir durumla hemen dönüyor.
- Başka bir kuruluştan gelen işleme belirteci, önündeki alt kuruluş üyelik
  denetiminden bağımsız olarak reddediliyor.
- Kullanıcı eşitlemesi sistem kullanıcısı bayrağını her çalışmada
  sıfırlamak yerine olduğu gibi bırakıyor.

### Dışa aktarma

- M3 teslim alma satırları dışa aktarılan birim fiyatı fatura satırının
  kendi fiyat temeliyle eşliyor. Fiyat, satın alma siparişi satırının
  böleniyle gidiyor ve ERP satırı faturalanan tutarın 1.000 katıyla yeniden
  fiyatlandırıyordu.
- Tablo dışa aktarması, satın alma siparişi kaldırılmış bir satırı da
  atlatıyor; satır fiyat temeli olmadan dışa aktarılıyor.
- IDM dışa aktarması: sayısal bir alana (örneğin miktar) eşlenen çok değerli
  bir alan dışa aktarma yükünü çökertiyordu. Değer önce metne
  dönüştürülüyor.

### E-belgeler

- Ön ödenmiş bir tutar toplamı dengelediği için ödenecek tutarı 0,00 olan
  XRechnung CII faturaları genel toplamı (BT-112) toplam tutar olarak
  gösteriyor. Müşteri "toplam tutar 0,00" görüyordu.
- XRechnung CII ve Facturae belgeleri tedarikçi alanlarını yeniden sağlıyor.
  Bayat kuruluş düzeyi geçersiz kılmalar doğru varsayılan eşlemeyi
  gölgeliyordu; bu yüzden tedarikçi tanıma hiçbir zaman eşleşemiyordu.
- Doğrulama kuralları kataloğu sunucuda sayfalanıyor, aranıyor ve
  sıralanıyor; filtre çubuğu için fasetler var.

### Sınıflandırma

- İsviçre belgeleri içeriklerine göre (CHF tutarları, CHE KDV numaraları, CH
  IBAN) `de_CH`, `fr_CH` veya `it_CH` olarak sınıflandırılıyor. Yerel ayar
  kuruluş varsayılanından alınıyor ve İsviçre belgeleri `de_DE` alıyordu.

### Pano araması

- Postgres ve ClickHouse'da tek işleç semantiği: `=` tam eşleşme, `:` kenar
  joker karakterleriyle içerir, `!=` boş değerler dahil tümleyen. Postgres'te
  `=` eskiden ön ek eşleşmesiydi; bu yüzden `invoice_id=911892112`
  911892112333'ü de döndürüyordu.
- Etiketsiz bir arama, iş tanımlayıcıları dahil her alanda alt dize
  araması. Satın alma siparişi, sipariş numarası, barkod, fatura türü,
  fatura alt türü ve talep numarasının hiç düz metin kolu yoktu.
- Fatura numarası etiketi, dizinde zaten olduğu gibi Postgres'te de tam
  eşleşme. Baştaki sıfırlar, ondalık biçimler ve büyük/küçük harf serbest
  metinde ve etiketlerde aynı şekilde ele alınıyor.
- Panonun WebSocket araması çağıranın kimlik bilgisini tam metin hizmetine
  taşıyor. Daha önce her yetki devri reddediliyordu; bu yüzden pano sessizce
  yalnızca Postgres'te arıyor ve yanıtı tam olarak sunuyordu.
- Durum kutucukları, sonuç sayısı ve sonuç listesi tek bir koşul kümesi
  üzerinde çalışıyor. Kutucuklar eskiden herhangi bir arama sırasında tüm
  kuruluşu tanımlıyordu.
- Alt kuruluş ve belge türü izinleri sonuç penceresinden önce uygulanıyor;
  böylece izin verilen belgeler artık 500 / 10.000 sınırının dışına
  düşmüyor.
- Vektör araması gerçek sonuç penceresiyle sınırlanıyor ve "(50)" ifadesini
  kesin toplam olarak göstermek yerine sınırı bildiriyor.
- Tam metin dizini olmadan çalışan bir arama (dizin eksik, dizin dakikalarca
  geride, yetenek sorgusu başarısız, alan çözümlemesi düşük kaliteli)
  "tamamlandı" yerine pencere durumunu bildiriyor.
- Kesilmiş bir aramanın pano dışa aktarmaları CSV/XLSX dosyasında ve bildirim
  e-postasında bir uyarı satırı taşıyor.
- Tam metin aramasını çağıran belge betikleri doğru kimlik doğruluyor ve
  boş sonuç döndürmek yerine hataları gösteriyor.

### Satın alma siparişi eşleştirme (süreç içi eşleştirici)

PO Match Service yerine API'de eşleştirme yapan kuruluşlar için:

- Birim fiyat ve miktar dahil her sütun karşılaştırması kaydediliyor;
  böylece uyuşmazlık ipucu başarısız olan sütunu adlandırabiliyor.
- Kullanıcının kaldırdığı satın alma siparişleri otomatik eşleştirmede
  kaldırılmış kalıyor.
- Düzeltilen bir satın alma siparişi numarası, onu düzelten kaydetme
  işleminde eşleştiriliyor.

### Analitik

- Touchless: yukarıdaki Web App bölümünün arkasındaki tüm arka uç
  değişiklikleri; her işlem hattı aşamasının kaydettiği aşama kanıtı, PO
  eşleştirme izi, önizleme, uygulama ve geri alma içeren değişiklik
  önerileri, bölümleme, tik başına tek çağrıda toplu durum ve herhangi bir
  pencereyi ve bir tedarikçiyi kabul eden eğilim uç noktası dahil.
- Zamanlanmış her çalıştırmada başarısız olan üç analitik arka plan görevi
  düzeltildi.

---

## PO Match Service — `1.59.34`

- Satın alma siparişi satırının birim fiyatı vergili toplamından değil net
  tutarından türetiliyor ve bir belgenin satın alma siparişi anlık görüntüsü
  birim fiyatlarını eşleştirme anında yeniden türetiyor.
- Hizmet, her satın alma siparişi numarası adayının nereden geldiğini ve bir
  çalıştırmanın hangi numaralara baktığını kaydediyor. Bir belgenin kendi
  fatura numarası asla satın alma siparişi adayı olmuyor. Düşürülen bir
  eşleşme, ekran için nedenini belgede bırakıyor.
- Eşleşmeyen sütun kaydediliyor ve bir yedek kuralın kaldırdığı sütunlar
  ölçülüyor.
- Kullanıcının kaldırdığı satın alma siparişlerine uyuluyor ve son
  dışlamadan sonra bayat arka plan eşleşmeleri temizleniyor.
- Kuralları `is_fallback` bayrağı taşımayan kuruluşlarda elle eşleştirme
  çalışıyor. Kullanıcılar satırları seçip eşleştirmeye basıyor ve hiçbir şey
  dönmüyordu.
- "Kuyruk"ta yetim kalan belge yok: veritabanı ifade zaman aşımları, canlı
  tutma sinyalleri ve açık bir yumuşak süre sınırı işleyicisi, iz bırakmayan
  bir sonlandırmaya güvenmek yerine görevi başarısız olarak işaretliyor.
- İki üretim hatası (`NaN` birim fiyat, miktarsız bir grup) artık
  eşleştirmenin tamamını başarısız kılmıyor.
- Tolerans değişiklikleri eşleştirme isteği başına okunuyor; böylece az önce
  kaydedilen bir tolerans bir sonraki eşleştirmede kullanılıyor.
- Beş aşamalı karar izi Touchless için belge başına kalıcı olarak
  saklanıyor.

---

## Auth Service — `1.78.27`

- `/organisation/subscriptions` kredi bakiyesini atlayabiliyor ve kredi
  hesaplaması, pencere başına bir sorgu (en büyük kuruluş için her biri
  yaklaşık 700 ms süren 32 sorgu) yerine tüm sözleşme yılı pencerelerini tek
  bir ifadede çalıştırıyor. Daha sonra kullanılmak üzere günlük bir kullanım
  özeti hazırlandı.
- Kuruluş okuyucularındaki kalan belirteç rakamları sözleşme yılı başına
  hesaplanıyor.
- Belirteç süresi önbellek isabetlerinde de uygulanıyor. Önbellekteki bir
  kayıt, belirtecin süresi dolduktan sonra dokuz saate kadar kimlik
  doğrulayabiliyordu.
- Belirteç doğrulaması, değişmemiş bir `org_id` değerini her istekte
  kullanıcı satırına geri yazmayı bırakıyor; bu, çağrı başına bir UPDATE
  üretiyordu.
- Sağlık denetimleri Redis G/Ç işlemlerini atlıyor ve Redis istemcisi
  havuzlanıyor. Otomatik ölçeklendiriciyi en yüksek kopya sayısına iten bir
  bellek sızıntısı düzeltildi ve hizmet yeniden iki çalışana döndü.
- Yinelenen bir tedarikçi kaydı (sihirli bağlantının iki kez açılması),
  yinelenen anahtar hatasıyla başarısız olmak yerine mevcut üyeliği yeniden
  kullanıyor.
- Parola sıfırlama e-posta iş parçacığı kayıtlı tek Flask uygulamasını
  kullanıyor; sıfırlama 25 Ağustos'tan beri "current Flask app is not
  registered" hatasıyla başarısız oluyordu.
- Sistem kullanıcısı bayrağı, başka hiçbir üye taşımıyorken mevcut bir
  kullanıcıda değiştirilebiliyor.
- MCP oturum açma: işleme bağlı MFA, tek kullanımlık onay ve tarayıcı iki
  oturum kimliği taşıdığında zorunlu hesap seçimi.

---

## Auth Bridge Service — `0.5.7`

AB ↔ ABD kimlik doğrulama çoğaltması:

- Periyodik mutabakat çoğaltma akışını canlı tutuyor. Gönderici zaman aşımı
  60 sn iken yaklaşık 95 sn sürüyordu; bu yüzden altı saatte bir yapılan her
  mutabakat akışı planlı olarak düşürüyordu.
- Akış öldüğünde çoğaltma yuvası, köprüyü yeniden kurup tam başlangıç
  mutabakatını yeniden çalıştırmak yerine yerinde yeniden bağlanıyor.
- Mutabakat, her iki tarafı belleğe yüklemek yerine birincil anahtarları
  sayfa sayfa karşılaştırıyor; belirteç tablosu çoğaltmaya katıldığından
  beri her iki taraf belleğe sığmıyor.
- Mevcut bir çoğaltma kaynağı bozulma değil başarı olarak ele alınıyor.

---

## Extraction Service — `1.55.33`

- Yapılandırılmış çıkarma tedarikçi başına çözümleniyor: eğitilmiş bir
  yerleşimin ayarı, tıpkı yapay zeka modelinde olduğu gibi kuruluş
  tercihine baskın geliyor.
- Öğrenilmiş bir sütun eşlemesi faturanın sahip olduğu sütunları
  yasaklayamıyor.
- Yapay zeka tablo çıkarma: tutar sütunları açıklamalı sayı olarak
  tipleniyor ve tutar sütunlarındaki uydurma sayısal olmayan değerler (komşu
  hücreden birim fiyat başına alanına kopyalanan bir "St.") saklanmak yerine
  atılıyor.
- ABD faturaları: net tutar zaten toplama eşitken vergi, çıkarılmış sahte
  bir vergiyi korumak yerine 0 olarak çözümleniyor. Sent altı kayan nokta
  gürültüsü artık aday net/vergi çiftleri arasında karar vermiyor (268,28 +
  22,13; net = toplam, vergi = 0 karşısında kaybediyordu).
- Başlık satırı hiç gerçek adlara eşlenmemiş bir tablo tümüyle başarısız
  olmak yerine çıkarılıyor.

---

## Fulltext Service — `1.42.35`

- Arama sonucu önbelleği her ortamda açık; üretim, sandbox ve stage, etkin
  ortam dosyaları oluşturulduğundan beri onsuz çalışıyordu. Yükleme ve silme
  önbelleği geçersiz kılıyor; böylece yüklemeden sonraki bir arama yeni
  belgeyi görüyor.
- Dinamik bir metin alanında tam `=` yalnızca değerin tamamını
  karşılaştırıyor. Analiz edilen yoldaki bir joker karakter,
  `note_field=53173` ifadesinin "PO 53173 / 2024" ile eşleşmesine yol
  açıyordu.
- `2026-003` gibi yalın tireli bir tanımlayıcı, belirteç torbası değil tek
  bir sabit değer.
- Satın alma siparişi numaraları, tam eşleşme koşulu sessizce düşürülen
  yalnızca rakamlardan oluşan tanımlayıcılar dahil her depolama biçiminde
  bulunuyor.
- Okuma yolları okudukları dizini oluşturmayı bırakıyor. Eksik veya boş bir
  dizin "tamamlandı, 0 sonuç" bildiriyordu; sıfır isabetli her yanıt artık
  bir pencere durumu ve nedeni taşıyor.
- Yazılı para birimi değerleri, eski boolean eşlemeleri, tarihler ve vergi
  bayrakları küçültülmüş dizin yeniden oluşturmasını atlatıyor; alanı
  olmayan dizin girdileri tespit edilip çıkarmadan kurtarılıyor.

---

## Docflow Service — `2.10.11`

- Gelişmiş iş akışı içe aktarmaları kuruluşun yetkisine bağlı ve bir toplu
  iş herhangi bir şey yazılmadan önce denetleniyor. Gelişmiş modülü olmayan
  bir kuruluş, sonradan açmanın hiçbir yolu olmayan gelişmiş bir iş akışını
  içe aktarabiliyordu.
- İş akışı yeniden adlandırması kaydetmeyle birlikte gidiyor ve şablon
  yeniden adlandırmaları kalıcı hale getiriliyor.
- "Bekleyen iş akışı yürütmesi" güncellemesi düşen bağlantılarda yeniden
  deneniyor. Tek bir başarısız istek bayrağı değiştirmeden bırakıyor ve biri
  belgeyi yeniden başlatana kadar belgeyi dışa aktarmanın dışında tutuyordu.

---

## Docnet Service — `1.56.12`

- Alan keşfi, yerleşimin tanımladığı her başlık alanını dolu olsun olmasın
  döndürüyor ve yazma korumasının denetlediğiyle örtüşüyor. Boş alanlar yok
  gibi göründüğü için ajanlar zorunlu alan güncellemelerini atlıyordu.
- Kimlikler API'nin kullandığı aynı kuruluş kapsamlı anahtar altında
  önbelleğe alınıyor; böylece kuruluş API anahtarı sınırı her iki hizmette
  de korunuyor.

---

## Email Service — `1.41.6`

- Ondan fazla alt klasörü olan paylaşılan Office 365 posta kutuları her
  klasörü çözümlüyor. Microsoft Graph klasörleri onar onar sayfalıyor; 11. ve
  sonraki yapılandırmalar her yoklamada "unable to find the selected Folder"
  hatasıyla başarısız oluyordu.

---

## FTP Service — `1.32.18`

- SFTP zamanlayıcısı çatallamadan önce değil, her çalışan süreçte başlıyor.
  Periyodik SFTP içe aktarmaları bozuk bir zamanlayıcı durumuyla sessizce
  başarısız olurken taze bir süreç sorunsuz çalışıyordu.

---

## Auto Accounting `1.21.7`, Barcode `1.18.14`, OCR `1.10.11`, Operator `1.42.12`, Ideas `0.3.6`

Yalnızca derleme ve dağıtım değişiklikleri (temel imaj güncellemesi, CI
kimlik bilgileri). Davranışta değişiklik yok.

<!-- Release R1.0.13. Everything in the prod->sandbox code delta is announced.
     Held back because Jira "Release No." names the later release R1.1:
     DRFS-778 (discount due dates on import), DRFS-712, MEF-165, MEF-166,
     DOCB-14389. Announce them with R1.1. -->

# DocBits Sürüm Notları — 14 Ekim 2026

_14 Ekim 2026'daki DocBits üretim hotfixinde (R1.0.15 sürümü) nelerin
değiştiği — [15 Eylül hotfixinden](incremental-updates-15-september-2026.md)
bu yana yapılan her şeyi kapsıyor. Her hizmet önce dağıtılan sürümü, ardından
yenilikleri veya düzeltmeleri sade bir dille listeliyor. Listelenmeyen
hizmetlerde müşteriye yönelik bir değişiklik olmadı._

{% embed url="https://docbits-videos.fra1.cdn.digitaloceanspaces.com/release-notes/2026-10-14/tr.mp4" %}

---

## Öne Çıkanlar

- **Ayarlar Asistanı.** Her ayar sayfasındaki bir sohbet çubuğu, kuruluşunuzun
  yapılandırmasıyla ilgili soruları sizin dilinizde ve DocBits belgelerinden
  yanıtlıyor. Ayarlarınızın güncel durumunu okuyup açıklıyor (grup izinleri,
  içe aktarma kanalları, satın alma siparişi anahtarları, muhasebe). Bir şeyi
  açmasını veya kapatmasını istediğinizde önce bir önizleme gösteriyor,
  onayınızı bekliyor ve geri alma imkânı sunuyor. "Ayarı aç" doğrudan ilgili
  ayara gidiyor, kapalı bir bölümün içinde bile, ve ayarı vurguluyor.
  Kuruluş yöneticileri asistanı Şirket Bilgileri sayfasından açıp kapatıyor.
  Yalnızca DocBits sorularını yanıtlıyor ve onay olmadan hiçbir şeyi
  değiştirmiyor.
- **Yeni yapay zeka kademeleri.** Fast ve Full kademeleri yeni modeller
  üzerinde çalışıyor. Yeni bir Auto kademesi belge başına Fast veya Full'u
  seçiyor ve Nexus Flash, Nexus'a katılıyor. Bir görsel mod (hibrit veya
  otomatik), sayfa görüntüsünün ne zaman birlikte gönderileceğine karar
  veriyor. Kayıtlı yapay zeka model tercihleri yeni kademelere kendiliğinden
  geçiyor ve ekranlarda yalnızca kademe adları görünüyor. "Yapay zeka kullan"
  bir açılır liste (Standart, Evet, Hayır) ve yapılandırılmış çıkarmanın neyi
  isteyeceğinin önizlemesini içeriyor.
- **Başlık alanı denetimi.** Doğrulama ekranında Kaydet düğmesinin yanında bir
  "Başlık alanı denetimi" düğmesi bulunuyor. Raporu, her başlık alanını
  değerin nereden geldiğiyle (yapay zeka, kural, betik veya ana veri) birlikte
  listeliyor; kaynak filtresi, arama ve sıralama içeren kompakt bir tablo ile
  doğrulama ekranıyla aynı alan etiketlerini kullanıyor. Köken açılır penceresi
  her değerin kaynağını tek bir şeritte gösteriyor.
- **Oturum açma ve kuruluş güvenliği.** Bir MFA doğrulaması her oturum açma
  yolunda yalnızca bir kez kullanılabiliyor ve bir kimlik doğrulama uygulaması
  kaydetmek için e-posta kodu gerekiyor. Kuruluşlar doğrulanmış e-posta
  alanlarından oluşan bir listeye sahip; sosyal giriş (örneğin Microsoft),
  alanı listeleyen kuruluşa katılıyor ve kendi başına hiçbir zaman kuruluş,
  kullanıcı veya abonelik oluşturmuyor. Kuruluş tercihlerini yalnızca kuruluş
  yöneticileri değiştirebiliyor ve satın alma siparişi eşleştirme kurallarını
  yalnızca onlar yazabiliyor veya onaylayabiliyor. Önbelleğe alınmış yanıtlar
  artık kuruluşlar arasında sızamıyor.
- **Satın alma siparişi eşleştirmesi ve ücretler.** Satın alma siparişinin sıfır
  olarak beklediği ücretler için mutlak bir alt sınır var, ücret toleransı
  siparişin bütçelemediği ücretler için de geçerli ve tek bir alan, tutarları
  satın alma siparişiyle orantılı olarak bölünen birden çok maliyet unsurunu
  listeleyebiliyor. Bir eşleştirme sütunu "uyuşmazlığa izin ver" bayrağı
  taşıyabiliyor. İş akışı kartları ücretleri liste başına karşılaştırıyor ve
  iş akışı yürütme sınırı 30'dan 50'ye çıkıyor.
- **Daha az yanlış sayı.** Tutarlar her kullanıcının kişisel biçiminde
  gösteriliyor (İsviçre ve Slovenya dahil), yalnızca tarih içeren değerler her
  saat diliminde takvim gününü koruyor, ABD toplam denklemi ek tutarları ve
  çok vergili faturaları hesaba katıyor ve başlık tutarları 0,00 olan
  belgeler artık yanlış aday geçişine düşmüyor.

---

## Bu sürümde ayrıca düzeltilenler

- Bir yarış durumu alt kuruluş filtresini kuruluş kimliğine ayarlayıp her
  belgeyi dışarıda bıraktığında pano artık boş kalmıyor.
- Boyut değerleri her kullanıcı için yeniden seçilebiliyor.
- Bir müşteri tarafından bildirilen yükleme hatası düzeltildi.
- "Toplamda eşleştir", faturası tek satırlı tedarikçiler için ve bunu bildiren
  tedarikçi kurulumları için çalışıyor.
- SPS e-belgeleri: 810 ücretleri ayarlandı, 855 ücret yerleşimi güncellendi ve
  e-belge önizlemesindeki müşteri logosu düzeltildi.

---

## Web App — `10.78.9.4`

**Ayarlar Asistanı**
- Tüm ayar sayfalarında bir anahtarla açılan, sağ taraftaki bir sohbet paneli
  bulunuyor. Konuşma sayfa değişikliklerinde korunuyor, 20 mesajla
  sınırlandırılmış ve uyguladığı değişiklikleri geri alma seçeneğiyle
  gösteriyor.
- Sizi geçerli ayar sayfasına uygun sorularla karşılıyor ve açma/kapatma
  anahtarlı ayar kartları gösteriyor. Esc önce menüleri kapatıyor, Durdur
  çalışan bir yanıtı iptal ediyor ve yanıtlardaki ekran görüntüleri bir
  ışık kutusunda açılıyor.
- Bir değişikliği uygulamak; önizleme, onay ve geri alma içeren bir iletişim
  kutusu açıyor.
- Her ayar kenar çubuğundan aranabiliyor ve bulunan ayar farklı bir renkle
  vurgulanıyor. "Ayarı aç", kapalı bir akordeonun içindeki hedefe kaydırıyor.
- Şirket Bilgileri sayfasında asistan için bir kuruluş yöneticisi anahtarı
  bulunuyor.
- Yapay zeka tavsiyeleri Nova'ya atfediliyor ve yalnızca kademe adları
  görünüyor, model kimlikleri hiçbir zaman görünmüyor.

**Doğrulama ekranı ve belge işleme**
- Rapor, alan başına köken ve yardım sayfası içeren yeni "Başlık alanı
  denetimi" düğmesi (bkz. Öne Çıkanlar). Kaynak etiketleri ve durum çipleri
  hücrelerinin içinde kalıyor.
- Alan etiketlerinin yanındaki "ana veriden" metin rozetleri kaldırıldı; bu
  bilgiyi artık köken açılır penceresi taşıyor.
- Her yerde tek bir ortak alan doğrulaması çalışıyor; bu, Auto Accounting
  sonrasındaki genel "Bir veya daha fazla alanın doğrulanması gerekiyor"
  hatasını ortadan kaldırıyor.
- Alan açılır penceresindeki düğmelerin (Sil, Temizle, Onayla) araç ipuçları,
  tıklamadan önce her birinin ne yaptığını söylüyor.
- İyimser bir satır artık yazılanı değil, saklananı gösteriyor. Bir sütun
  yeniden eşleştirmesi, yalnızca görünür bir sütun eşlemesini kaybettiğinde
  onay istiyor.
- OCR sayfa sınırını aşan sayfalar salt okunur ve işaretli; Auto Accounting
  görüntüleyicisinde de böyle. Eski içe aktarma sayfa kısıtlaması paneli
  kaldırıldı.
- Çoklu satın alma siparişi başlık alanındaki her satın alma siparişi numarası
  için bir satın alma siparişi tablosu görünüyor ve Layout Builder, satın alma
  siparişi sekmelerini satın alma siparişi tablo anahtarından etiketliyor;
  satın alma siparişi tablosu açıkken artık modülün devre dışı olduğunu
  bildirmiyor.
- Öneri kartı `[object Object]` yerine toleransı gösteriyor ve Onay karşılaştırma
  ekranı, yapılandırılmış karşılaştırma sütunlarını (kalem numaraları)
  yuvarlamayı bırakıyor.

**Hesaplar, ayarlar ve hatalar**
- Her hata bildirimi ve oturum açma hatası, başarısız isteğin izleme kimliğini
  gösteriyor; böylece destek ekibi onu bulabiliyor. Pano WebSocket hataları
  yalnızca adını verdikleri isteği reddediyor.
- Şirket Bilgileri, kuruluşun e-posta alanlarını listeliyor.
- Yöneticiler, kullanıcı sayfasından "Parolanızı belirleyin" e-postasını yeniden
  gönderebiliyor.
- Genel yöneticiler sözleşme başlangıcını abonelik tablosunda belirliyor.
- Kuruluş yöneticileri Yönetici Panosu sekmesini ve XSLT ekleme ve silme
  düğmelerini görüyor. Üyeler yerleşimleri kendi tercihleri olarak kaydediyor.
- Kuruluşsuz bir oturum, boş bir pano yerine net bir hata ve kuruluş seçici
  alıyor.
- Tutarlar kullanıcının kişisel sayı biçimini izliyor ve yalnızca tarih içeren
  değerler her saat diliminde gününü koruyor.
- Ana veri, alt kuruluş kimliklerini yalnızca kuruluş kimliğinden farklı
  olduklarında gönderiyor ve özel ana veri üstbilgileri üstbilgi olarak
  gidiyor.
- Tablolar maskesi artık "Yapay zeka kullan" açılır listesini kırpmıyor, yapay
  zeka ipucu metni eğitim satırını artık örtmüyor ve yapay zeka tablosu,
  yalnızca simgeli bir başlık denetimi ve bir lisans mesajıyla birlikte doğrudan
  Uygula düğmesini koruyor.
- Eski simge yazı tipi kaldırıldıktan sonra tablo çıkarma simgeleri yeniden
  görüntüleniyor.

**Görev panosu**
- Pano ilk sayfasını daha az yinelenen istekle yüklüyor, Enter aramayı hemen
  çalıştırıyor, geç gelen yanıtlar doğru aramayla eşleştiriliyor, alt bilgi
  sayfa kapasitesi yerine gerçek isabet sayısını gösteriyor ve bir kuruluşta
  başlatılan silme işlemi, kuruluş değiştirdiğinizde gönderilmeden önce
  iptal ediliyor.

---

## API Service — `12.83.293`

**Ayarlar Asistanı ve MCP**
- Korkuluklara sahip sohbet uç noktası: yalnızca DocBits soruları, onay
  olmadan değişiklik yok, belirsiz veya meta sorular ret yerine yardım alıyor
  ve yanıtlar önce kartları, sonra metni akıtıyor.
- Her ayar alanı için salt okunur yapı taşları (grup izinleri, içe aktarma
  kanalları, satın alma siparişi eşleştirmesi, muhasebe, e-posta alanları),
  ayar bulma aracı içeren bir derin bağlantı kataloğu ve DocBits belgelerinden
  görsellerle belge araması.
- 1. dalga uygulama akışı: desteklenen ayarlar için önizleme, onay ve geri
  alma; üçü için tek bir kapsam kuralı, çifte onaya ve süre aşımına karşı
  güvenli.
- MCP araçları uzak modda sunucudan hiçbir zaman dosya okumuyor; fixture ve
  lab araçları yalnızca dev ortamında çalışıyor.

**Yapay zeka**
- Fast ve Full kademelerinin, Auto kademesinin, Nexus Flash'ın ve görsel mod
  tercihinin arkasında yeni modeller. Kayıtlı `AI_MODEL` tercihleri yeni
  kademelere taşınıyor.
- "Yapay zeka kullan", yapılandırılmış çıkarmanın neyi istediğini belgeliyor.

**Güvenlik ve yalıtım**
- Kuruluş tercihlerini yalnızca kuruluş yöneticileri değiştiriyor.
- `/accounting/rebuild` çağrısı yalnızca çağıranın kuruluşunu eğitiyor,
  başarısız bir kuruluş aramasında erişimi reddediyor ve hatalı bir kimlik için
  400 yanıtı veriyor.
- XSLT, XML ve PDF oluşturma dosya ve ağ erişimini reddediyor, harici
  include'ları çözmüyor ve fatura baytları dönüştürücüye ulaşmadan önce
  temizleniyor. Oluşturulan PDF önizlemeleri yalnızca güvenilir görsel
  sunucularına izin veriyor.
- Önbellek anahtarları kuruluşu taşıyor ve aynı tanımlayıcı her zaman aynı
  anahtarı veriyor; böylece yabancı bir kuruluş kimliği artık önbelleğe alınmış
  verileri okuyamıyor. Her belge değişikliğinde kuruluş genelinde pano önbelleği
  temizleme kaldırıldı.
- Kuruluşun e-posta alanı listesi Auth'a iletiliyor.

**Satın alma siparişi eşleştirmesi ve dışa aktarma**
- Bir alan, tutarları satın alma siparişiyle orantılı olarak bölünen birden çok
  maliyet unsurunu listeleyebiliyor.
- Onay vekilleri etkin onay talebine bağlanıyor, onarılmış onay kayıtları artık
  engellemiyor ve onay bekleyen bir belge dışa aktarma için reddediliyor.
- PDF/A ek açıklaması katalogu ve gömülü XML'i koruyor; böylece e-faturalar
  ek açıklamadan sonra XML'lerini koruyor. Yalın EN 16931 CustomizationID'ye
  sahip UBL faturaları sınıflandırılıyor (e-fatura ağı).
- GRPR, M3'ün kabul ettiği 6 ondalığa yuvarlıyor. Temel ölçü birimi dönüşüm
  katsayıları dondurulmuş satıra ekleniyor.
- Geçici olarak silinmiş eğitimlere ve biçimlendirme kurallarına saygı
  gösteriliyor ve MCP `update_document_fields` artık kaybettiği bir yazmayı
  onaylamıyor. `get_table_rules` türlendirilmiş bir ıskalama yanıtı veriyor ve
  boş bir çeviri yükü kendi yedeğini kullanıyor.
- Slovence tutarlar `sl_SI` kullanıyor ve kayıtlı tercihler taşınıyor. UUID
  kimlikleri olarak gönderilen özel sınıflandırma etiketleri çözümleniyor.
  Paylaşılan panolar, güncellemede `created_by` ve paylaşım listesini koruyor.
- Pano hata çerçeveleri isteğin `request_id` değerini taşıyor ve başarısız
  her JSON yanıtı bir izleme kimliği taşıyor.
- Sistem tüm API filosu yerine yalnızca sağlıksız çalışanları yeniden
  başlatıyor ve kayıtlı görev listesini doğru denetliyor. Takılma izleme kuyruğu
  yeniden tüketiliyor.

---

## Auth Service — `1.78.49`

- Çok faktörlü bir doğrulama yalnızca MCP akışında değil, her oturum açma
  yolunda tek kullanımlık. Kayıt için e-posta kodu gerekiyor, ortak parolayla
  oturum açıldıktan sonra kayıt belirteci verilmiyor ve bir faktör
  kaydedildiğinde kullanıcılara bildirim gidiyor.
- Kuruluşlar her biri yalnızca bir kez atanabilen bir e-posta alanı listesine
  sahip. Sosyal giriş, doğrulanmış alanı listeleyen kuruluşa katılıyor, hiçbir
  zaman kuruluş, kullanıcı veya abonelik uydurmuyor ve kimseyi adlandırmadan
  reddediyor; bunun yerine yöneticilere bilgi veriliyor. Microsoft'un
  döndürdüğü alanlar ele alınıyor.
- Reddedilen her oturum açma bir izleme kimliği taşıyor. Yöneticiler "Parolanızı
  belirleyin" e-postasını yeniden gönderebiliyor. Sözleşme bakiyesi işaretli ve
  sözleşme başlangıcı denetleniyor.

## Auth Bridge — `0.5.7`

- AB ve ABD hesap çoğaltması, mutabakat sırasında bağlantısını besli tutuyor,
  kopan bir çoğaltma yuvasını kendiliğinden yeniden bağlıyor, sınırlı bellek
  kullanıyor ve mevcut bir çoğaltma kaynağını başarı olarak ele alıyor.
  Bölgeler arası oturum açma daha güvenilir.

## Docflow Service — `2.10.22`

- Ayrı birim fiyat kartı, ücretler için kuruluşun varsayılan alan
  tanımlarını okuyor ve bir alanın listelediği her maliyet unsurunu
  karşılaştırıyor.
- İş akışı yürütme sınırı 30'dan 50'ye çıkıyor ve iş akışı günlük aramaları
  UUID olmayan bir kimliği reddediyor.

## Docnet Service — `1.56.15`

- `list_document_fields`, boş olanlar dahil yapılandırılmış her tablo
  sütununu bildiriyor.

## Extraction Service — `1.56.0.1`

- Kademeler: Fast ve Full'un arkasında yeni modeller, Auto, Nexus Flash ve bir
  görsel mod. Çıkarım ana bilgisayarına giden görsel istekleri, onun boyut
  sınırının altında kalıyor.
- Nexus ile tablo çıkarma sayfaları gruplar halinde (grup başına iki)
  işliyor, grupları ölçülmüş bir zaman aşımıyla paralel çalıştırıyor, geçici
  hataları yeniden deniyor ve zaman aşımına uğrayan bir grubu bölüyor. Başlık
  alanları tüm gruplardan okunuyor.
- ABD toplamları: ek tutarlar toplam denkleminin parçası, 1. çift 2. çift
  korumasında sayılıyor, vergiler sıfır olmadığında düşük puanlı adaylar
  atlanıyor ve "üstünde" ile "altında" çok kelimeli etiketlerle eşleşiyor.
- Tanımlayıcı alanlar gerçekten oluşan karakterleri onarıyor ve görünmez
  karakterler anlamlarına göre işleniyor; böylece bir "O" artık garip bir
  karaktere dönüşmüyor.

## Fulltext Service — `1.42.41`

- DocBits belgeleri için yeni bir dizin; alım ve arama uç noktaları, yanıtlarda
  görseller ve tüm arama için bir son süre içeriyor. Ayarlar Asistanı'nı
  besliyor.

## PO Match Service — `1.59.48`

- Satın alma siparişinin sıfır olarak beklediği ücretler için mutlak alt sınır
  ve siparişin bütçelemediği ücretler için ücret toleransı.
- Bir sütun "uyuşmazlığa izin ver" bayrağı taşıyabiliyor. Alan başına birden
  çok maliyet unsuru orantılı olarak bölünüyor.
- Eşleştirme kurallarını yalnızca kuruluş yöneticileri yazıyor veya
  onaylıyor ve kural koşulları yalnızca beyaz listeye alınmış bir ifade
  dilbilgisini kabul ediyor.
- Kural değişiklikleri, Touchless değişiklik önerileri için yazmadan, bir
  geçersiz kılma kural kümesine karşı simüle edilebiliyor. Eşleştirilecek
  satın alma siparişi ek sütunları belge türü özniteliğinden okunuyor ve eski
  tercih taşınıyor.

---

_Bu sürümden etkilenmeyenler: Auto Accounting, Barcode, E-Mail, FTP, Ideas,
OCR, Operator. FTP ve Operator yalnızca dahili bakım içeriyor._

<!-- Release R1.0.15 (sandbox 02-10-26, planned prod 14-10-26, deployed Wednesday 14 Oct 2026).
Versions on prod before this deploy: API 12.83.222, Auth 1.78.38, Auth Bridge 0.4.2,
Docflow 2.10.18, Docnet 1.56.13, Extraction 1.55.50.1, Fulltext 1.42.38, PO Match 1.59.39,
Web App 10.70.6.
Held back (Release No. names a later release; announce with that release):
R1.1: CORE-6145, CORE-6148 (import failure notice and card per channel), CORE-6127 and
CORE-6136 (run transformation rules after master data lookup), CORE-6117, CORE-6072, CORE-6071,
CORE-2452, CORE-2444, DRFS-779, CORE-554 (rule execution logs from the dashboard), CORE-550, CORE-6278,
CORE-6180, CORE-6168, DMB-431, OBO-160, DRFS-806 (date tolerance for PO matching and approval).
R1.0.16: CORE-6103 (assistant drafts transformation rules), DRFS-822 (charge cards use only
matched POs, trigger status filter), DPG-170 (cost invoice export gate), OBO-159 (the "x" on a
field stores "leave empty" on its own; field suppression).
R1.2 / R1.4: DRFS-535 (receipt availability flag), DOP-53 (UOM conversion).
Added from the Ready for Production Release list: DRFS-742, DU-220, MAR-67, DRFS-708, DRFS-820,
DRFS-723, DRFS-724, DRFS-726. Not on the page (no matching code in the delta, check by hand):
MEF-169 (S/MIME invoices from one supplier not arriving, Email Service version unchanged), DMB-391.
Shipped although Release No. is empty or stale: OBO-156, CORE-6102, CORE-6154, CORE-6155,
CORE-6150, CORE-6169, CORE-6181, CORE-6183, CORE-6185, CORE-6187, CORE-2606, CORE-2461,
CORE-2457, CORE-6092 (R1.0.14 labels). -->

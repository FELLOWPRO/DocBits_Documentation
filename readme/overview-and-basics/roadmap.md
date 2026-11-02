# DocBits Yol Haritası

_7 Ekim 2026 itibarıyla planlama durumu. Her sürüm, planlanan sandbox
tarihini (müşterilerin test edebileceği tarih) ve planlanan üretim tarihini
listeliyor. Temalar sürüm için planlananları anlatıyor, halihazırda
yayınlananları değil; kapsam ve tarihler değişebilir. Sürümler arasındaki
hotfixler [Sürüm Notları](release-notes/README.md) sayfasında belgeleniyor._

| Sürüm | Sandbox | Üretim |
|---|---|---|
| R1.1 | 16 Ekim 2026 | 4 Kasım 2026 |
| R1.2 | 16 Şubat 2027 | 3 Mart 2027 |
| R1.3 | 1 Haziran 2027 | 16 Haziran 2027 |
| R1.4 | 5 Ekim 2027 | 20 Ekim 2027 |

---

## R1.1 — Sandbox 16 Ekim 2026 · Üretim 4 Kasım 2026

**Dönüşüm kuralları ve yerleşimler**

- Çıkarılan alan ve sütun değerleri için bir kural motoru: iç içe koşul
  gruplarıyla değer atayın, değiştirin veya türetin; kuralları yönetmek için
  bir ayarlar ekranı. "Şunlardan biridir" koşulu birden çok değer alıyor,
  kural listesinde kural kimliğine göre arama yapılabiliyor ve kurallar ana
  veri aramasından sonra da çalışıyor.
- Yerleşim seçim kuralları aynı iç içe koşulları ve isteğe bağlı bir çalıştırma
  günlüğünü kazanıyor. Yerleşim seçimi, belgenin nereden geldiğinden bağımsız
  çalışıyor.
- Yerleşimleri Yönet, Özel Doğrulama Kuralları ve Dönüşüm Kuralları artık beta
  anahtarı gerektirmiyor.
- Başlık alanları ve tablo sütunlarındaki alan etiketleri için net öncelik
  kuralları. Kullanıcılar alan ayarları ve tablo sütunları için kendi çeviri
  anahtarlarını oluşturabiliyor.
- Silinen bir tablo sütunu yeniden atanabiliyor ve tedarikçi kalem fiyat
  tablosu tüm sütunlarını gösteriyor.

**Onay ve doğrulama ekranları**

- Onay ekranındaki üç satır kalemi tablosu (fatura satırları, karşılaştırma
  satırları, satın alma siparişi eşleştirmesi) tek bir stili paylaşıyor.
- Son açılan yan panel (etkinlik akışı veya onay geçmişi) kullanıcı başına
  hatırlanıyor.
- Belgeler, onay ekranından belge yükleyiciyle birleştirilebiliyor.
- Özel doğrulama kuralları nakliye maliyetlerini genel biçimde ele alıyor,
  zorunlu bir alan boş olduğunda genel bir hata yerine alan mesajı gösteriyor
  ve yanlış negatif bildiren kurallar düzeltildi. Sistem varsayılan kuralları
  çoğaltılabiliyor.
- Yapay zekayla çıkarılan bir tabloda miktar ile net tutar arasındaki
  uyuşmazlık bildiriliyor, eşleşen bir satın alma siparişi olan fatura artık
  masraf faturası olarak sınıflandırılmıyor ve bir kuralın yeniden
  biçimlendirdiği tarih kabul ediliyor.
- Onaylama veya reddetmeden sonra yükleme katmanında takılı kalan onay ekranı
  düzeltildi. Sade yükleme simgesinin yerini bir yükleme çubuğu alıyor ve sayfa
  URL'leri daha anlaşılır.
- Oturum süresi dolduktan sonra bir belge bağlantısını açmak 404 yerine oturum
  açma sayfasına yönlendiriyor.

**Yinelenen belge algılama**

- Özel alanlar yinelenen belge algılama sonucunda görünüyor ve yinelenen
  belge ayarlarında arama yapılabiliyor.
- "Yinelenen Belge Dışa Aktarımını Engelle" seçeneği, algılanan bir yinelenen
  belgenin dışa aktarılmasını engelliyor.

**İş akışları ve görevler**

- Bir "Yeni iş akışı" düğmesi, gelişmiş iş akışları için günlükler, daha
  anlaşılır bir watchdog günlük ekranı; bir alanı veya onay kutusunu
  değiştiren iş akışı adımları güvenilir biçimde uygulanıyor.
- Bir karar ağacına satır eklemek, kimlikleri göstermek yerine kullanıcı
  adlarını koruyor.
- Bir belgenin her durum değişikliği günlüğe kaydediliyor.
- Yeni bir e-posta şablonu oluşturmak yeniden çalışıyor.
- Görev listesi ilk yüklemede görevlerini gösteriyor.

**İçe aktarma**

- E-posta içe aktarma, bir postayı yalnızca yükleme onaylandıktan sonra gelen
  kutusundan çıkarıyor, yeniden teslim edilen bir iletmeyi tek teslimat
  olarak ele alıyor, son kaydeden kişiyi kaydediyor ve başarısız olan bir eki
  hata nedeniyle birlikte yalnızca bir kez listeliyor.
- FTP ve SFTP içe aktarma, taşıma ve arşivlemenin yanına gerçek bir içe aktarma
  sonrası silme seçeneği kazanıyor. Bir yapılandırma düzenlendiğinde parolalar
  artık bozulmuyor, bağlantı testi yeni SFTP bağlantıları için çalışıyor ve
  başarısız bir SFTP bağlantısı ya da yanlış oturum açma bilgisi genel bir hata
  yerine belirli bir mesaj gösteriyor.
- Yapılandırılmış bir FTP veya e-posta içe aktarma çalışmayı bıraktığında
  yöneticilere Ayarlar Asistanı'nda bildiriliyor.
- Tarayıcı uygulamasından yükleme yeniden çalışıyor.
- ABD bölgesinde yüklenen satın alma siparişi BOD dosyaları ABD bölgesinde
  kalıyor.

**Belge işleme ve çıkarma**

- Barkod hizmeti takıldığında belge, süresiz olarak "İşleniyor" durumunda
  kalmak yerine hatayı gösteriyor.
- Çıkarma için yeni, daha ucuz bir yapay zeka model kademesi ("Eco").
- Yapılandırılmış yapay zeka çıkarmasında eğitilmiş tedarikçi kalem
  numaraları eğitilmiş kalıyor; kalem numarası ile tedarikçi kalem numarası
  artık yer değiştirmiyor.
- UBL e-belge şablonları uyarlandı; belirli tedarikçi yerleşimlerinde
  tutarlar, vergi oranları, birim fiyatlar ve satın alma siparişi numaraları
  için çıkarma düzeltmeleri.
- Ek tarih biçimleri tanınıyor.
- İki KDV oranına sahip bir masraf faturası her iki muhasebe satırını da
  koruyor.

**Satın alma siparişi eşleştirmesi**

- Eşleştirme bir miktar sütunu gerektiriyor, temel birim miktarı başına
  fiyatı kullanıyor ve son satır yedek kuralı müşteri başına açılıp
  kapatılabiliyor.
- İrsaliye satırları tek tek seçilebiliyor.
- E-belge ekranı 250'den fazla satırı olan faturalarda artık donmuyor.

**Touchless Intelligence**

- Touchless raporunda daha fazla ayrıntı; Touchless onay kutusu kaydedilen
  ayarı yansıtıyor.

**Pano, hesaplar ve abonelik**

- Pano arama başına 10.000 belgeye kadar tutabiliyor ve özel tarih filtresi
  doğru uygulanıyor.
- İskonto vade tarihi ve fatura vade tarihi yerleşim alanı olarak
  kullanılabiliyor ve içe aktarmada dolduruluyor.
- Bir pano kaydedildiğinde paylaşılan pano kullanıcıları korunuyor ve
  "Güncelleyen" doğru kişiyi gösteriyor.
- Arşivlenen belgeler "Arşivlendi" durumundan geri çıkarılabiliyor.
- Kullanıcılar parola sıfırlamadan sonra yeniden oturum açabiliyor.
- Abonelik planı sayfası plan ve özellikleri için kullanımı gösteriyor.

**Dışa aktarma ve EDI**

- Ek fatura bilgileri için ilave bir Infor M3 dışa aktarma adımı.
- Birden çok konteyner numarası içeren bir çeki listesi, konteyner başına bir
  kayıt olarak dışa aktarılıyor.
- Bir mal kabul teslimatını yeniden içe aktarmak artık yinelenen anahtar
  nedeniyle başarısız olmuyor ve mal kabul teslimatı BOD'ları doğru sırada
  uygulanıyor.
- Fatura, satın alma siparişi ve sipariş onayı için EDI eşlemeleri
  güncellendi.
- Yeni bir Infor IDM veya Infor LN dışa aktarma yapılandırmasının bağlantı
  testi çalışıyor.

**Güvenlik**

- API anahtarları için kuruluş denetimi her ortamda uygulanıyor.

---

## R1.2 — Sandbox 16 Şubat 2027 · Üretim 3 Mart 2027

**Onay ve satın alma siparişi eşleştirmesi**

- Bir "Girdi bekleniyor" durumu, iş akışını veya denetim geçmişini bozmadan
  belgeyi biri yanıt verene kadar duraklatıyor; onaylayanlar onay akışını
  kesintiye uğratmadan soru sorabiliyor.
- Bir belge başka bir kullanıcıya yeniden atanabiliyor (ilk aşama).
- Ön ödeme faturaları, "Alınan miktar üzerinden eşleştir" etkin kalırken mal
  kabulünden önce eşleştirilebiliyor.
- Eşleştirme ekranı yalnızca uygun satın alma siparişi satırlarını sunuyor ve
  fiyat karşılaştırmasını atlayan çok satırlı eşleşmeler onay ekranında yine de
  birim fiyatı gösteriyor.
- Bir mal kabul uygunluk bayrağı faturalanan ve alınan miktarları
  karşılaştırıyor.
- Sipariş onayları: onay beklenirken maliyet unsurları gösteriliyor, satın
  alma siparişi eşleştirmesinde renk kodlu ek ücret pozisyonları ve fatura
  satır kalemlerinde kalem numarası sütunu.
- Tedarikçi RMA satırları ele alınıyor.

**İçe aktarma ve sınıflandırma**

- Tedarikçi türü satır kalemlerinden türetiliyor.
- Destek talebi formu ek kabul ediyor ve kuruluşu otomatik olarak bağlıyor.

**Ayarlar ve otomasyon**

- "Alt kuruluş ata" betiği bir dönüşüm kuralına dönüşüyor.
- Standart sütunlar bir belge türünden kaldırılabiliyor.

**Dışa aktarma**

- Dışa aktarma geçmişi dışa aktarılan belgeleri yeniden listeliyor.
- Navlun faturaları Infor LN'ye dışa aktarılıyor.
- Dışa aktarma dosya adları yapılandırılabiliyor.
- Genişletilmiş Vertex vergi entegrasyonu.

---

## R1.3 — Sandbox 1 Haziran 2027 · Üretim 16 Haziran 2027

**Auto Accounting Rule Manager**

- Kurallar, alt kuruluş ve belge türü başına kapsamlanmış olarak hesapları ve
  boyutları otomatik atıyor; hangi kuralın tetiklendiğini gösteren bir
  denetim ekranı eşlik ediyor.
- Bir kural ana verileri arayıp birden çok alanı tek seferde atayabiliyor veya
  bir tablo satırı sütunundan değer doldurabiliyor.
- Alanlar ve boyutlar tek tek temizlenebiliyor, satır kalemleri (tutarı
  olmayan satırlar dahil) silinebiliyor ve kurallar metinden açılır listeye
  dönüştürülen alanlarda çalışmaya devam ediyor.
- Tahminler birden çok vergi kodunu ve boyutu, fişleri ve kayıt referanslarını
  destekliyor. Auto Accounting ekranları birden çok dilde.

**Satın alma siparişi eşleştirmesi**

- Eşleşme simgesi, birden çoğa eşleşmeler dahil sekmeler arasında gezinip
  kaydırıyor ve vurguluyor.
- Takma adlarla birim dönüşümü (örneğin KG ve TO), yuvarlama hesabı olan
  yapılandırılabilir bir yuvarlama sapması ve dört ondalıkla yapılıp üç
  ondalıkla gösterilen hesaplamalar.

**Kullanılabilirlik**

- Belge betiklerinin yürütme sırası ön yüzde görünüyor.
- Enter ve Tab tuşları klavyeden alanlar arasında geçiş sağlıyor.

**Dışa aktarma**

- Başarısız bir dışa aktarmanın ardından Infor LN'deki eksik belge siliniyor.
- Veritabanı bağlayıcısı ilgili tüm tabloları içeriyor.

---

## R1.4 — Sandbox 5 Ekim 2027 · Üretim 20 Ekim 2027

**Onay ekranında Auto Accounting**

- Onaylayanlar, Auto Accounting ile doğrudan onay ekranında çalışabiliyor.
- Onay, hesap kodu veya ülke gibi muhasebe alanlarına bağlanabiliyor; bir
  belge geri gönderildiğinde borç hesaplarında bir düzeltme yapılıyor.
- Birden çok vergi satırı kurmadan Auto Accounting'de bir vergi kodu açılır
  listesi.
- Boyutlar, büyük boyut kümelerinin daha hızlı yüklenmesi için yeni bir
  yapıda saklanıyor ve Rule Manager için bir geri bildirim turu yapılıyor.

**Onay**

- İyileştirilmiş bir onay akışı, onay sırasında başka bir kullanıcıya devretme
  ve bir "Dışa Aktar ve Sonraki" düğmesi.

**Satın alma siparişi eşleştirmesi ve dışa aktarma korumaları**

- Faturalanan miktarın alınan miktarı aştığı fazla eşleşmiş faturalar
  eşleştirme ekranında tanınıyor ve fatura eşleştirmesi sırasında ölçü
  birimleri dönüştürülüyor.
- Ücret kodları (geçiş ücreti, taşıma, enerji) tanınıyor ve maliyetleri
  dağıtılıyor.
- Eşleşen miktar alınan miktarı aştığında ya da ondan çok saptığında veya
  kayıt tarihi ambar giriş tarihinden önce olduğunda dışa aktarma bir uyarıyla
  engelleniyor.

**İçe aktarma ve ayarlar**

- FTP, e-posta ve gelen e-posta içe aktarma için otomatik ve elle yeniden
  işleme içeren bir yeniden deneme mekanizması; gönderen adresi e-posta içe
  aktarmadan kullanılabiliyor.
- Ayarlarda tüm anahtarlar ve alt sayfalar genelinde arama yapılabiliyor.
- E-posta sunucusu kurulumu, süresi dolan bir OAuth veya istemci gizli
  anahtarını posta kutusunu yeniden kurmadan değiştirmenize olanak tanıyor.
- Tedarikçi kalem numarası eşlemesi (kalem numarası dönüşüm tablosu) bir CSV
  içe aktarmasıyla doldurulabiliyor.
- Onay geçmişi SFTP dışa aktarma ile dışa aktarılabiliyor.

**DocNet Agents**

- Sipariş alımı: bir müşteri siparişi Infor M3 veya Infor LN'de satış
  siparişine dönüşüyor (ilk sürüm, metin belgeleri).

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-10-07 by the
     docbits-roadmap skill. Releases up to R1.4 only; R1.5 and later are not
     published yet. Themes only; ticket keys, customer names and internal work
     are deliberately left out. Rerun the skill to refresh. -->

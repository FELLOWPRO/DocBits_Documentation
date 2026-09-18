# DocBits Yol Haritası

_18 Eylül 2026 itibarıyla planlama durumu. Her sürüm, planlanan sandbox
tarihini (müşterilerin test edebileceği tarih) ve planlanan üretim tarihini
listeliyor. Temalar sürüm için planlananları anlatıyor, halihazırda
yayınlananları değil; kapsam ve tarihler değişebilir. Sürümler arasındaki
hotfixler [Sürüm Notları](release-notes/README.md) sayfasında belgeleniyor._

| Sürüm | Sandbox | Üretim |
|---|---|---|
| R1.1 | 5 Ekim 2026 | 14 Ekim 2026 |
| R1.2 | 23 Kasım 2026 | 2 Aralık 2026 |
| R1.3 | 8 Şubat 2027 | 17 Şubat 2027 |
| R1.4 | 7 Nisan 2027 | 15 Nisan 2027 |
| R1.5 | 18 Mayıs 2027 | 27 Mayıs 2027 |
| R1.6 | 6 Temmuz 2027 | 15 Temmuz 2027 |
| R1.7 | 21 Eylül 2027 | 30 Eylül 2027 |
| R2.0 | daha sonra duyurulacak | daha sonra duyurulacak |

---

## R1.1 — Sandbox 5 Ekim 2026 · Üretim 14 Ekim 2026

**Dönüşüm kuralları ve yerleşimler**

- Çıkarılan alan ve sütun değerleri için bir kural motoru: iç içe koşul
  gruplarıyla değer atayın, değiştirin veya türetin; kuralları yönetmek için
  bir ayarlar ekranı. Yerleşim seçim kuralları da aynı iç içe koşulları
  kazanıyor.
- Yerleşim seçimi, belgenin nereden geldiğinden bağımsız çalışıyor.
- Başlık alanları ve tablo sütunlarındaki alan etiketleri için net öncelik
  kuralları.
- Silinen bir tablo sütunu yeniden atanabiliyor ve tedarikçi kalem fiyat
  tablosu tüm sütunlarını gösteriyor.

**Onay ve doğrulama ekranları**

- Onay ekranındaki üç satır kalemi tablosu (fatura satırları, karşılaştırma
  satırları, satın alma siparişi eşleştirmesi) tek bir stili paylaşıyor ve
  karşılaştırma görünümü satıra ait kalem numarasını gösteriyor.
- Son açılan yan panel (etkinlik akışı veya onay geçmişi) kullanıcı başına
  hatırlanıyor.
- Belgeler, onay ekranından belge yükleyiciyle birleştirilebiliyor.
- Özel doğrulama kuralları nakliye maliyetlerini genel biçimde ele alıyor ve
  yanlış negatif bildiren kurallar düzeltildi.
- Sade yükleme simgesinin yerini bir yükleme çubuğu alıyor; daha anlaşılır
  sayfa URL'leri.

**Yinelenen belge algılama**

- Özel alanlar yinelenen belge algılama sonucunda görünüyor ve yinelenen
  belge ayarlarında arama yapılabiliyor.

**İş akışları ve görevler**

- Bir "Yeni iş akışı" düğmesi, gelişmiş iş akışları için günlükler, daha
  anlaşılır bir watchdog günlük ekranı; bir alanı veya onay kutusunu
  değiştiren iş akışı adımları güvenilir biçimde uygulanıyor.
- Bir karar ağacına satır eklemek, kimlikleri göstermek yerine kullanıcı
  adlarını koruyor.
- Bir belgenin her durum değişikliği günlüğe kaydediliyor.
- Yeni bir e-posta şablonu oluşturmak yeniden çalışıyor.

**İçe aktarma**

- E-posta içe aktarma, bir postayı yalnızca yükleme onaylandıktan sonra gelen
  kutusundan çıkarıyor, yeniden teslim edilen bir iletmeyi tek teslimat
  olarak ele alıyor, son kaydeden kişiyi kaydediyor ve S/MIME imzalı
  postaları kabul ediyor.
- FTP içe aktarma, taşıma ve arşivlemenin yanına gerçek bir içe aktarma
  sonrası silme seçeneği kazanıyor.
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

**Satın alma siparişi eşleştirmesi**

- Eşleştirme bir miktar sütunu gerektiriyor, temel birim miktarı başına
  fiyatı kullanıyor ve son satır yedek kuralı müşteri başına açılıp
  kapatılabiliyor.
- İrsaliye satırları tek tek seçilebiliyor.
- E-belge ekranı 250'den fazla satırı olan faturalarda artık donmuyor.

**Touchless Intelligence**

- Touchless raporunda daha fazla ayrıntı; Touchless onay kutusu kaydedilen
  ayarı yansıtıyor.

**Pano**

- Pano arama başına 10.000 belgeye kadar tutabiliyor.
- İskonto vade tarihi ve fatura vade tarihi yerleşim alanı olarak
  kullanılabiliyor ve içe aktarmada dolduruluyor.
- Bir pano kaydedildiğinde paylaşılan pano kullanıcıları korunuyor ve
  "Güncelleyen" doğru kişiyi gösteriyor.
- Arşivlenen belgeler "Arşivlendi" durumundan geri çıkarılabiliyor.

**Dışa aktarma ve EDI**

- Ek fatura bilgileri için ilave bir Infor M3 dışa aktarma adımı.
- Birden çok konteyner numarası içeren bir çeki listesi, konteyner başına bir
  kayıt olarak dışa aktarılıyor.
- Bir mal kabul teslimatını yeniden içe aktarmak artık yinelenen anahtar
  nedeniyle başarısız olmuyor ve mal kabul teslimatı BOD'ları doğru sırada
  uygulanıyor.
- Fatura, satın alma siparişi ve sipariş onayı için EDI eşlemeleri
  güncellendi.

**Güvenlik**

- API anahtarları için kuruluş denetimi her ortamda uygulanıyor.

---

## R1.2 — Sandbox 23 Kasım 2026 · Üretim 2 Aralık 2026

**Onay ve satın alma siparişi eşleştirmesi**

- Bir "Girdi bekleniyor" durumu, iş akışını veya denetim geçmişini bozmadan
  belgeyi biri yanıt verene kadar duraklatıyor; onaylayanlar onay akışını
  kesintiye uğratmadan soru sorabiliyor.
- Ön ödeme faturaları, "Alınan miktar üzerinden eşleştir" etkin kalırken mal
  kabulünden önce eşleştirilebiliyor.
- Bir mal kabul uygunluk bayrağı faturalanan ve alınan miktarları
  karşılaştırıyor.
- Sipariş onayları: onay beklenirken maliyet unsurları gösteriliyor, satın
  alma siparişi eşleştirmesinde renk kodlu ek ücret pozisyonları ve fatura
  satır kalemlerinde kalem numarası sütunu.
- Eşlenmemiş sütunlar artık tablo tutarı hesaplamasına katılmıyor.
- Tedarikçi RMA satırları ele alınıyor.

**İçe aktarma ve sınıflandırma**

- Gönderen adresi e-posta içe aktarmadan kullanılabiliyor.
- Tedarikçi türü satır kalemlerinden türetiliyor.

**Ayarlar ve otomasyon**

- "Alt kuruluş ata" betiği bir dönüşüm kuralına dönüşüyor.
- Standart sütunlar bir belge türünden kaldırılabiliyor.

**Dışa aktarma**

- Dışa aktarma geçmişi dışa aktarılan belgeleri yeniden listeliyor.
- Navlun faturaları Infor LN'ye dışa aktarılıyor.

---

## R1.3 — Sandbox 8 Şubat 2027 · Üretim 17 Şubat 2027

**Auto Accounting Rule Manager**

- Kurallar, alt kuruluş ve belge türü başına kapsamlanmış olarak hesapları ve
  boyutları otomatik atıyor; hangi kuralın tetiklendiğini gösteren bir
  denetim ekranı eşlik ediyor.
- Bir kural, bir tablo satırı sütunundan değer doldurabiliyor.
- Alanlar ve boyutlar tek tek temizlenebiliyor, satır kalemleri (tutarı
  olmayan satırlar dahil) silinebiliyor ve kurallar metinden açılır listeye
  dönüştürülen alanlarda çalışmaya devam ediyor.

**Satın alma siparişi eşleştirmesi**

- Eşleşme simgesi, birden çoğa eşleşmeler dahil sekmeler arasında gezinip
  kaydırıyor ve vurguluyor.
- Takma adlarla birim dönüşümü (örneğin KG ve TO), yuvarlama hesabı olan
  yapılandırılabilir bir yuvarlama sapması ve dört ondalıkla yapılıp üç
  ondalıkla gösterilen hesaplamalar.

**Dışa aktarma**

- Yapılandırılabilir dışa aktarma dosya adları.
- Başarısız bir dışa aktarmanın ardından Infor LN'deki eksik belge siliniyor.
- Veritabanı bağlayıcısı ilgili tüm tabloları içeriyor.

---

## R1.4 — Sandbox 7 Nisan 2027 · Üretim 15 Nisan 2027

**İçe aktarma**

- FTP, e-posta ve gelen e-posta içe aktarma için otomatik ve elle yeniden
  işleme içeren bir yeniden deneme mekanizması.

**DocNet Agents**

- Sipariş alımı: bir müşteri siparişi Infor M3 veya Infor LN'de satış
  siparişine dönüşüyor (ilk sürüm, metin belgeleri).

**Onay**

- İyileştirilmiş bir onay akışı, onay sırasında başka bir kullanıcıya devretme
  ve bir "Dışa Aktar ve Sonraki" düğmesi.

**Satın alma siparişi eşleştirmesi**

- Eşleştirme ekranında yalnızca uygun satın alma siparişi satırları
  sunuluyor.
- Faturalanan miktarın alınan miktarı aştığı fazla eşleşmiş faturalar
  eşleştirme ekranında tanınıyor ve fatura eşleştirmesi sırasında ölçü
  birimleri dönüştürülüyor.

**Diğer**

- Rule Manager için geri bildirim turu.
- Destek talebi formu ek kabul ediyor ve kuruluşu otomatik olarak bağlıyor.
- Genişletilmiş Vertex vergi entegrasyonu.

---

## R1.5 — Sandbox 18 Mayıs 2027 · Üretim 27 Mayıs 2027

**Auto Accounting**

- Rule Manager arama eylemi: ana verileri eşleştirip birden çok alanı tek
  seferde atayın.
- Tahminler birden çok vergi kodunu ve boyutu, fişleri ve kayıt referanslarını
  destekliyor.
- Auto Accounting ekranları birden çok dilde.

**Onay ve satın alma siparişi eşleştirmesi**

- Bir belgeyi başka bir kullanıcıya yeniden atayın.
- Satın alma siparişi eşleştirme ekranındaki sütun sırası kullanıcı başına
  kaydediliyor.
- Ücret kodları (geçiş ücreti, taşıma, enerji) tanınıyor ve maliyetleri
  dağıtılıyor.

**Dışa aktarma korumaları**

- Eşleşen miktar alınan miktarı aştığında ya da ondan çok saptığında veya
  kayıt tarihi ambar giriş tarihinden önce olduğunda dışa aktarma bir uyarıyla
  engelleniyor.

**Kullanılabilirlik**

- Belge betiklerinin yürütme sırası ön yüzde görünüyor.
- Enter ve Tab tuşları klavyeden alanlar arasında geçiş sağlıyor.

---

## R1.6 — Sandbox 6 Temmuz 2027 · Üretim 15 Temmuz 2027

**Ayarlar**

- Ayarlarda tüm anahtarlar ve alt sayfalar genelinde arama yapılabiliyor.
- E-posta sunucusu kurulumu, süresi dolan bir OAuth veya istemci gizli
  anahtarını posta kutusunu yeniden kurmadan değiştirmenize olanak tanıyor.
- Tedarikçi kalem numarası eşlemesi (kalem numarası dönüşüm tablosu) bir CSV
  içe aktarmasıyla doldurulabiliyor.

**Auto Accounting**

- Boyutlar, büyük boyut kümelerinin daha hızlı yüklenmesi için yeni bir
  yapıda saklanıyor.

---

## R1.7 — Sandbox 21 Eylül 2027 · Üretim 30 Eylül 2027

**Onay ekranında Auto Accounting**

- Onaylayanlar, Auto Accounting ile doğrudan onay ekranında çalışabiliyor.
- Onay, hesap kodu veya ülke gibi muhasebe alanlarına bağlanabiliyor; bir
  belge geri gönderildiğinde borç hesaplarında bir düzeltme yapılıyor.
- Birden çok vergi satırı kurmadan Auto Accounting'de bir vergi kodu açılır
  listesi.

---

## R2.0 — Sandbox daha sonra duyurulacak · Üretim daha sonra duyurulacak

**Auto Accounting**

- Bir listeye dayanan alanlar serbest metin de kabul ediyor.
- Zorunlu alanlar doğrulanıyor.
- Model tahminleri muhasebe alanlarını otomatik dolduruyor (eğitilmiş tahmin
  modeliyle hibrit mod); modelin neyi doldurduğuna dair bir denetim izi
  tutuluyor.

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-18 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->

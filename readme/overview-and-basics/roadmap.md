# DocBits Yol Haritası

_15 Eylül 2026 itibarıyla planlama durumu. Her sürüm, planlanan sandbox
tarihini (müşterilerin test edebileceği tarih) ve planlanan üretim tarihini
listeliyor. Temalar sürüm için planlananları anlatıyor, halihazırda
yayınlananları değil; kapsam ve tarihler değişebilir. Sürümler arasındaki
hotfixler [Sürüm Notları](release-notes/README.md) sayfasında belgeleniyor._

| Sürüm | Sandbox | Üretim |
|---|---|---|
| R1.1 | 16 Eylül 2026 | 23 Eylül 2026 |
| R1.2 | 21 Ekim 2026 | 28 Ekim 2026 |
| R1.3 | 25 Kasım 2026 | 2 Aralık 2026 |
| R1.4 | 27 Ocak 2027 | 3 Şubat 2027 |
| R1.5 | 10 Mart 2027 | 17 Mart 2027 |

---

## R1.1 — Sandbox 16 Eylül 2026 · Üretim 23 Eylül 2026

**Dönüşüm kuralları ve yerleşimler**

- Çıkarılan alan ve sütun değerleri için bir kural motoru: iç içe koşul
  gruplarıyla değer atayın, değiştirin veya türetin; kuralları yönetmek için
  bir ayarlar ekranı. Yerleşim seçim kuralları da aynı iç içe koşulları
  kazanıyor.
- Yerleşim seçimi, belgenin nereden geldiğinden bağımsız çalışıyor.
- Başlık alanları ve tablo sütunlarındaki alan etiketleri için net öncelik
  kuralları.

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

- Bir "Yeni iş akışı" düğmesi, gelişmiş iş akışları için günlükler; bir alanı
  veya onay kutusunu değiştiren iş akışı adımları güvenilir biçimde
  uygulanıyor.
- Satın alma faturası iş akışlarında onay e-postaları atanan onaylayanlara
  ulaşıyor.
- Bir belgenin her durum değişikliği günlüğe kaydediliyor.

**İçe aktarma**

- E-posta içe aktarma, bir postayı yalnızca yükleme onaylandıktan sonra gelen
  kutusundan çıkarıyor, yeniden teslim edilen bir iletmeyi tek teslimat
  olarak ele alıyor, son kaydeden kişiyi kaydediyor ve S/MIME imzalı
  postaları kabul ediyor.
- FTP içe aktarma, taşıma ve arşivlemenin yanına gerçek bir içe aktarma
  sonrası silme seçeneği kazanıyor.
- Tarayıcı uygulamasından yükleme yeniden çalışıyor.

**Belge işleme ve çıkarma**

- Barkod hizmeti takıldığında belge, süresiz olarak "İşleniyor" durumunda
  kalmak yerine hatayı gösteriyor.
- "Sayfalarla sınırla" yalnızca OCR'ı ve sayfa sayımını sınırlıyor; artık
  belgeden sayfa kesmiyor.
- Bir belgeyi kaydetmek ilgisiz verilere dokunmuyor.
- Çıkarma için yeni, daha ucuz bir yapay zeka model kademesi ("Eco") ve yapay
  zeka tablosunda tablo etiketleri uygulamak yeniden çalışıyor.
- Bir ZUGFeRD PDF'ini başka bir PDF ile birleştirmek e-fatura verisini
  koruyor; UBL e-belge şablonları uyarlandı; belirli tedarikçi
  yerleşimlerinde tutarlar, vergi oranları ve satın alma siparişi numaraları
  için çıkarma düzeltmeleri.
- Ek tarih biçimleri tanınıyor.

**Satın alma siparişi eşleştirmesi**

- Eşleştirme bir miktar sütunu gerektiriyor, temel birim miktarı başına
  fiyatı kullanıyor ve son satır yedek kuralı müşteri başına açılıp
  kapatılabiliyor.
- E-belge ekranı 250'den fazla satırı olan faturalarda artık donmuyor.
- Tanılama, satın alma siparişi satırının fiyatı olmasa bile miktarı ölçüyor.

**Touchless Intelligence**

- Touchless raporunda daha fazla ayrıntı; bir satın alma siparişi engeli,
  alan doğrulama hatası olarak değil olduğu gibi bildiriliyor.

**Pano**

- Pano arama başına 10.000 belgeye kadar tutabiliyor.
- İskonto vade tarihi ve fatura vade tarihi yerleşim alanı olarak
  kullanılabiliyor ve içe aktarmada dolduruluyor.
- Bir pano kaydedildiğinde paylaşılan pano kullanıcıları korunuyor; "Atanan"
  ve "Güncelleyen" doğru kişiyi gösteriyor.
- Belge izinleri tam metin dizininde de uygulanıyor.

**Dışa aktarma ve EDI**

- BOD dışa aktarma 30 karakterden uzun tablo sütun değerlerini koruyor.
- Ek fatura bilgileri için ilave bir Infor M3 dışa aktarma adımı ve satır
  türü 5 dışa aktarmalarında birim fiyatlar.
- Bir mal kabul teslimatını yeniden içe aktarmak artık yinelenen anahtar
  nedeniyle başarısız olmuyor.
- Fatura (810), satın alma siparişi (850), sipariş onayı (855), sevkiyat
  bildirimi (856, WMS dışa aktarma dahil) ve değişiklik siparişi (860) için
  EDI X12 eşlemeleri güncellendi.

**Güvenlik**

- Tedarikçi hesap planı eşlemeleri bağlı SQL parametreleriyle saklanıyor ve
  API anahtarları için kuruluş denetimi her ortamda uygulanıyor.

---

## R1.2 — Sandbox 21 Ekim 2026 · Üretim 28 Ekim 2026

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
- Bir satın alma siparişi değişiklik talebi akışı ve Infor dışa aktarma
  eşlemesinde belge sahibi.

**Dışa aktarma**

- Dışa aktarma geçmişi dışa aktarılan belgeleri yeniden listeliyor.
- Navlun faturaları Infor LN'ye dışa aktarılıyor.

---

## R1.3 — Sandbox 25 Kasım 2026 · Üretim 2 Aralık 2026

**Auto Accounting Rule Manager**

- Kurallar, alt kuruluş ve belge türü başına kapsamlanmış olarak hesapları ve
  boyutları otomatik atıyor; hangi kuralın tetiklendiğini gösteren bir
  denetim ekranı eşlik ediyor.
- Bir kural, bir tablo satırı sütunundan değer doldurabiliyor.
- Alanlar ve boyutlar tek tek temizlenebiliyor, tutarı olmayan satırlar
  silinebiliyor ve kurallar metinden açılır listeye dönüştürülen alanlarda
  çalışmaya devam ediyor.

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

## R1.4 — Sandbox 27 Ocak 2027 · Üretim 3 Şubat 2027

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
- Birden çok ambar girişi tek bir fatura satırıyla eşleşebiliyor ve fatura
  eşleştirmesi sırasında ölçü birimleri dönüştürülüyor.

**Diğer**

- Rule Manager için geri bildirim turu.
- Destek talebi formu ek kabul ediyor ve kuruluşu otomatik olarak bağlıyor.
- Genişletilmiş Vertex vergi entegrasyonu.

---

## R1.5 — Sandbox 10 Mart 2027 · Üretim 17 Mart 2027

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

<!-- Generated from Jira "Release No." (customfield_10392) on 2026-09-15 by the
     docbits-roadmap skill. Themes only; ticket keys, customer names and
     internal work are deliberately left out. Rerun the skill to refresh. -->

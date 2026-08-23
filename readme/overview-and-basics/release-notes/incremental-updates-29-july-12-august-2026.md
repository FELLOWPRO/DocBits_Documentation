# DocBits Sürüm Notları — 29 Temmuz – 12 Ağustos 2026

_10–12 Ağustos 2026'da devreye alınan DocBits üretim yükseltmesinde nelerin
değiştiği — 29 Temmuz sürümünden bu yana yapılan her şeyi kapsıyor. Her hizmet
önce canlıya alınan sürümü, ardından yenilikleri veya düzeltmeleri sade bir
dille listeliyor. Listelenmeyen hizmetlerde (Auto Accounting `1.21.1`, Ideas
`0.3.1`, OCR `1.10.3`, Operator `1.42.1`, PO Match `1.59.3`, FTP `1.32.4`)
müşteriye yönelik bir değişiklik olmadı._

---

## Öne Çıkanlar

- **FacturaE desteği.** İspanyol FacturaE 3.1 e-faturaları kutudan çıktığı
  haliyle sınıflandırılıyor ve çıkarılıyor; alan eşlemeleri eksiksiz. Aynı
  dalgada ebInterface (Avusturya) eşlemeleri sürüme sadık hale geldi, Factur-X
  ve ZUGFeRD varsayılanları şirket adı yolunu kazandı ve iskontolar, KDV ve
  birim fiyatlar için birkaç hatalı varsayılan eşleme düzeltildi.
- **Pano araması ve sıralaması onarıldı.** Sıralama artık hangi sütunların
  görünür olduğuna bağlı değil, bir aralık veya eşitlikle birleştirilen OR
  filtresi artık arama ifadelerini silmiyor, tedarikçi adları hızlı aramada
  yeniden görünüyor ve ISO biçimli tarihler doğru okunuyor.
- **Yapay zeka çıkarımı kendini düzeltiyor.** Yapay zekanın yaptığı
  kanıtlanabilir bir net/toplam tutar takası otomatik olarak geri alınıyor,
  yapay zekayla taranan alanlar bir belge yeniden başlatıldıktan sonra artık
  yanlış dönmüyor ve yapay zeka tablo çıkarma belgeleri sayfa partileri
  halinde işlediği için uzun tablolar eksiksiz geliyor.
- **İş akışları bir kimlik doğrulama aksamasını atlatıyor.** Kısa süreliğine
  erişilemeyen kimlik doğrulama hizmeti çalıştırmayı başarısız saymak yerine
  yeniden deneniyor ve kimlik doğrulayamayan bir iş akışı tetikleyicisi
  belgeyi takılı bırakmak yerine hatayı bildiriyor.
- **Zor okunan PDF'ler yeniden çıkarılıyor.** Standart PDF metin çözücüsü bir
  sayfayı okuyamadığında (Ghostscript ile üretilmiş dosyalarda yaygın), veri
  çıkarma hiçbir şey döndürmemek yerine ikinci bir motora geçiyor.
- **MFA bölgeler arasında çalışıyor.** İki faktörlü kayıt verileri AB ve ABD
  bölgeleri arasında çoğaltılıyor; böylece bir bölgede kurulan ikinci faktör
  diğerinde de tanınıyor.

---

## Web App — `10.49.4`

### Oturum açma ve hesaplar

- Bir tarayıcı sekmesinde oturumu kapatmak diğer sekmelerin oturumunu da
  kapatıyor; sekmeler oturum konusunda anlaşamadığında beliren hata
  bildirimleri de artık yok.
- Profilde kendi parolanızı değiştirmek özel self-servis uç noktası üzerinden
  gidiyor; böylece yönetici yetkileri olmadan da çalışıyor.
- Ana bölge dışından geçiş anahtarıyla oturum açma çevrilmiş hata mesajları
  gösteriyor ve gönder düğmesi görünür durumda.

### Doğrulama ekranı

- "Çıkarılan tablo" sekmesi, halihazırda bir yapay zeka tablosu varken artık
  sonsuza kadar dönmüyor.
- Barkod verisi eksik olan belgeler barkod atama görünümünü artık bozmuyor.
- M3 çoklu vergi satırları, vergi kodunu serbest metin alanı yerine değer
  listesinden beslenen bir açılır liste olarak sunuyor.
- Büyük tedarikçi faturalarını açmak belirgin şekilde daha hızlı.

### Görevler

- Kanban sütunları siz kaydırdıkça sayfalanıyor; böylece çok görevli panolar
  hızla yükleniyor.
- Kenar çubuğundaki açık görev sayacı, o sırada hangi belge açıksa onun
  bağlamını değil, sizin alt kuruluş bağlamınızdaki görevleri sayıyor.

### Workflow Builder

- İş akışı listesi, bir iş akışını açıp geri döndüğünüzde — gezinme yolu
  (breadcrumb) üzerinden dönüşler dahil — aramanızı, sıralama düzeninizi,
  sayfanızı ve sayfa boyutunuzu koruyor. Sayfa varsayılan olarak Liste
  sekmesinde açılıyor.

### Ayarlar ve yönetim

- Ana Veri sayfası bir sıralama yarışı yüzünden artık boş gelmiyor ve
  rozetlere göre sıralamak sayfayı artık çökertmiyor.
- "İptal ediliyor" durumundaki bir abonelik sürdürülebiliyor.
- XSLT ayrıntı sayfası hiçbir şey göstermemek yerine yükleme hatalarını
  bildiriyor; e-posta bildirim ayarları çalışan bir günlük bölmesiyle tam
  sayfa genişliğini kullanıyor.
- Çok kuruluşlu kullanıcılar için kuruluş seçicinin satır düzeni,
  boyutlandırması ve tema renkleri doğru; seçici düzgün kaydırılıyor ve çok
  sayıda kuruluşu olan hesaplar için bir filtre sunuyor.
- Analitik: başarısız bir metrik isteği sıfırlar göstermek yerine bir hata
  durumu gösteriyor ve kullanım bileşenleri, ölçüm verisi olmadığında bunu
  dürüstçe bildiriyor.
- Önbellek yönetimi sayfasından kullanımdan kalkmış önbellek seçenekleri
  kaldırıldı; Kullanıcılar ve Gruplar sayfalarındaki iç içe çift kaydırma
  çubukları da gitti.
- Yerleşim yöneticisindeki "Varsayılan Şablonu Kullan" artık çökmüyor ya da
  tepkisiz kalmıyor; varsayılan yerleşim olmadığını iddia etmeyi de bıraktı.
- Seçim kuralları, bir kural yeniden açıldığında metin eşleme, varlık ve
  düzenli ifade (regex) işleçlerini koruyor.
- Belge Türleri tür başına dönüşüm kurallarını destekliyor ve kural listesi
  arayüzü bir sabit değer atama eylemi kazandı.
- Satın alma siparişi durum rozetleri, ERP'nin büyük/küçük harf düzenindeki
  durum değerleri için doğru eşleniyor.
- Agent Wizard dahil DocNet (AI Workforce) ekranları çevrildi ve yeni/düzenle
  fikir iletişim kutusu yatay kaydırılabiliyor.
- Tedarikçi portalı teklifleri: yönetilen ölçü birimleri satır kalemi
  tablosunda görünüyor, onay biçimlendirmesi yalnızca sözleşme tekliflerine
  uygulanıyor ve her iki değer aynı olduğunda karşılaştırma satırı artık
  görünmüyor.
- Hata sayfasının JSON yedek görünümü karanlık modda okunabiliyor ve raporlar
  başıboş bir "7" yerine düzgün bir "son 7 gün" etiketi kullanıyor.

## API Service — `12.74.0`

### Pano ve arama

- Sıralama hangi sütunların görünür olduğundan bağımsız çalışıyor ve aramanın
  tam metne devrettiği bir anahtar kelime artık arkasında bozuk bir SQL
  parçası bırakmıyor.
- Tam metin dizini olmayan kuruluşlarda tedarikçi adları hızlı aramada yeniden
  görünüyor.
- ISO biçimli tarihler (2026-08-12) gün-önce tarih normalleştiricisi
  tarafından artık yanlış okunmuyor.
- Pano dışa aktarmaları, fatura numarası gibi yalın metin değerlerini doğru
  sütuna yönlendiriyor.

### E-faturalar

- FacturaE 3.1 (İspanya): sınıflandırma kuralı ve eksiksiz alan eşlemeleri.
- XRechnung sınıflandırma kuralları kendi sözdizimi ailesine sabitlendi;
  böylece bir UBL belgesi artık CII kurallarıyla eşleşmiyor, tersi de geçerli.
- Kabul edilen "3.0" sürümü tüm yama ailesini (3.0.1, 3.0.2) kapsıyor.
- CII faturaları tedarikçinin yasal adını alıyor; ticari ad yalnızca yedek
  olarak kullanılıyor.
- ebInterface (Avusturya) eşlemeleri sürüme sadık; genel yakalama kuralı
  düzeltildi ve test örnekleri yeniden oluşturuldu.
- Factur-X ve ZUGFeRD varsayılanları şirket adı çıkarma yolunu kazandı; vergi
  oranı, fatura türü ve üçüncü kademe alanlar için varsayılan başlık
  dönüşümleri, aile genelindeki iskonto, KDV ve birim fiyat semantiğiyle
  birlikte düzeltildi.
- Kaynak vergi kategorisi kodları artık körlemesine ERP kodlarınıza
  eşlenmiyor.
- Hem "fatura" hem "alacak dekontu" ifadesi geçen belgeler alacak dekontu
  sınıflandırmasını tercih ediyor.

### Belgeler ve veri çıkarma

- Standart PDF çözücüsü bir sayfanın gömülü metnini okuyamadığında veri
  çıkarma ikinci bir motora geçiyor; böylece etkilenen PDF'ler boş dönmek
  yerine çıkarılıyor.
- Barkod ana anahtarı artık `BARCODE_EXTRACTION`; eski QR kodu ayarı takma ad
  olarak çalışmaya devam ediyor.
- Arka plan zamanlayıcısındaki bir bellek sızıntısı kapatıldı; günler süren
  çalışma boyunca işlemeyi yavaş yavaş bozuyordu.
- Ülke bilgisi olmadan içe aktarılan tedarikçiler Almanya'ya varsayılan olarak
  düşmek yerine boş kalıyor.

### Dışa aktarma ve ana veriler

- Save Rules (Kuralları Kaydet), hiçbir şey yazmadığında başarı iddia etmek
  yerine başarısızlık bildiriyor.
- Sıfır tutarlı satırlar otomatik muhasebe dışa aktarmalarından artık
  düşürülmüyor ve her kovaya eşleşen bir filtre düzeltildi.
- M3 dışa aktarmaları ek bilgi son işleme kancalarını (post-hook) destekliyor.
- Başarısız tek bir veri kümesi denetimi artık tüm Ana Veri ekranını
  boşaltmıyor.
- ERP bir satın alma siparişinin durumunu güncellediğinde PO önbellekleri
  geçersiz kılınıyor; böylece pano bayat durumu göstermeyi bırakıyor.

### Yönetim

- Her tercih, onu en son hangi kullanıcının değiştirdiğini gösteriyor.
- Çıkarma kuralları yeni uç noktalar üzerinden tedarikçiye göre silinebiliyor
  ve kopyalanabiliyor.
- Durum uyarısı e-posta alıcıları NULL'a karşı güvenli biçimde
  karşılaştırılıyor; bu, bildirim gönderimindeki bir çökmeyi düzeltiyor.

## Auth Service — `1.75.9`

- İlgisiz bir kuruluşa karşı kullanılan kuruluş API anahtarı reddediliyor.
- Kuruluş oluşturma, satırı aslında kaydettiği halde hata döndürüyordu; artık
  doğru yanıt veriyor.
- Hiç geçiş anahtarı kayıtlı değilken geçiş anahtarıyla oturum açmak kendi
  hata kodunu döndürüyor; böylece oturum açma ekranı neyin yanlış olduğunu
  söyleyebiliyor.

## Auth Bridge Service — `0.4.2`

- İki faktörlü kayıt tabloları AB ve ABD bölgeleri arasında çoğaltılıyor ve
  satırlar gerçek birincil anahtarlarıyla tanımlanıyor.

## Docflow Service — `2.8.7`

- Kimlik doğrulayamayan bir iş akışı tetikleyicisi belgeyi takılı bırakmak
  yerine hatayı bildiriyor ve kısa süreliğine erişilemeyen kimlik doğrulama
  hizmeti geçersiz belirteç sayılmak yerine yeniden deneniyor.
- Teklif karşılaştırma kartları: kalem numaraları yalnızca kalem fiyat
  matrisinin tanımladığı satırlar için karşılaştırılıyor; ölçü birimi veya
  fiyatı olmayan satırlar karşılaştırmayı başarısız kılmak yerine atlanıyor.
- Sözleşmeli fiyat karşılaştırma kartı bir herhangi biri/tümü işleç seçeneği
  kazandı ve kart önbellekleri geçişlerden (migration) ve kod
  güncellemelerinden sonra doğru biçimde geçersiz kılınıyor.
- Kopan SSL bağlantıları geçici sayılıyor ve çalıştırmayı başarısız kılmak
  yerine yeniden deneniyor.

## Docnet Service — `1.56.4`

- Sağlık ve sürüm uç noktaları artık canlı denetimlerde bloklanmıyor; bu,
  eskiden Hizmet Sürümleri iletişim kutusunun asılı kalmasına yol açıyordu.

## Email Service — `1.40.6`

- Gelen bir e-posta atlandığında nedeni, sessiz kalmak yerine içe aktarma
  olay satırında gösteriliyor.
- Ekli `.eml` kapsayıcı dosyaları artık belge olarak içe aktarılmıyor.
- Başarısız bir Microsoft Office oturum açması okunabilir bir hata mesajı
  üretiyor ve yapay zeka hizmetinden gelen bir iletim hatası ret yerine
  "belirsiz" sayılıyor.

## Extraction Service — `1.53.8`

- Yapay zekanın yaptığı kanıtlanabilir bir net/toplam tutar takası alan
  çıkarımından sonra geri alınıyor ve koruma denetimi hataları sessizce
  geçmek yerine günlüğe kaydediliyor.
- Yapay zekayla taranan alanlar bir belge yeniden başlatıldıktan sonra artık
  yanlış dönmüyor.
- Yapay zeka tablo çıkarma sayfalara göre partiliyor ve tüm partileri
  biriktiriyor; böylece uzun tablolar eksiksiz geliyor.
- Hem "fatura" hem "alacak dekontu" ifadesi geçen belgeler alacak dekontu
  sınıflandırmasını tercih ediyor.
- Yinelenen üstbilgi/altbilgi temizliği önbelleğe alınıyor; bu, çok sayfalı
  belgelerde çıkarımı hızlandırıyor.

## Fulltext Service — `1.41.7`

- Bir aralık veya eşitlik koşuluyla birleştirilen OR filtresi artık arama
  ifadelerini silmiyor.
- Sıralama doğru dizin yollarını kullanıyor ve arama arka ucu bir sorguyu
  reddettiğinde gerçek nedeni gösteriyor; ham sorgu aramasını tamamen bozan
  bir sıralama gerilemesi ortaya çıktığı hafta içinde düzeltildi.
- Belge aramaları, metin eşlemeli eski dizinlerde de çalışıyor.
- Belirteç önbelleği belirteç ve kuruluş çiftine göre kapsamlandı; böylece
  kuruluş değiştirmek önceki bağlam altında sonuç sunamıyor.

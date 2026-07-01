# DocBits Sürüm Notları — 26–30 Haziran 2026

_Bu production yükseltmesinin sade bir dille neler sağladığı. Her hizmet, şu anda
production ortamında canlı olan sürümü gösterir. Listelenmeyen hizmetlerde bu
dönemde müşteriye yönelik bir değişiklik olmamıştır._

---

## Öne Çıkanlar

- **AI asistanları için tek bağlantı ([DocBits MCP](https://docs.docbits.com/advanced-functions-and-tools/docbits-mcp)).** Tek ve birleşik bir ağ geçidi
  artık tüm DocBits araçlarını — DocFlow dahil — ana API üzerinden sunuyor; böylece
  AI asistanları (Claude, Gemini CLI, Codex) birkaç uç nokta yerine tek ve güvenilir
  bir uç nokta üzerinden bağlanıyor.
- **Daha akıllı çok dilli pano araması.** Arama bağlaçları (**AND / OR**) artık
  kendi dilinizde renkli vurgulamayla görünüyor, fatura alt türleri bir değer açılır
  listesi sunuyor ve arama sözdizimi mesajları yerelleştiriliyor — baştan sona daha
  akıcı klavye işlemesiyle.
- **Daha akıcı onaylar ve izinler.** Sipariş onayından gelen ambalaj birimi boş
  olduğunda onay artık tetiklenmiyor, normal kullanıcılar erişim denetimi geçişinden
  sonra maliyet öğelerini yeniden onaylayabiliyor ve bir tablo sütunu zaten mevcut
  olsa bile belge düzeyindeki izinler doğru şekilde uygulanıyor.
- **Uygulama kendini güncelliyor.** Yeni bir sürüm yayınlandığında DocBits, sizi bir
  "Şimdi Yenile" açılır penceresiyle kesintiye uğratmak yerine artık otomatik olarak
  yenileniyor.
- **Daha sağlam satın alma siparişi eşleştirme.** Sütun değeri dönüşümleri, fiyatı
  veya miktarı eksik satırlar için çökme korumaları ve kopan veritabanı
  bağlantılarında otomatik yeniden deneme eşleştirmeyi daha kararlı hale getiriyor.
- **Genelinde daha az hata.** Panolarda, tedarikçi faturalarında, PO kayıtlarında ve
  OCR işlerinde görülen birçok nadir sunucu hatası tespit edilip düzeltildi.

---

## Web App — canlı: `10.34.4`

- **Pano hızlı araması:** renkli sözdizimi vurgulamalı yerelleştirilmiş **AND / OR**
  bağlaçları (de/fr); fatura alt türü değer açılır listesi; yerelleştirilmiş arama
  sözdizimi hata mesajları; daha akıcı klavye deneyimi; "tam metin gerekli" uyarısı
  artık satır içinde görüntüleniyor, böylece düzen artık kaymıyor.
- **Onaylar ve izinler:** sipariş onayından gelen ambalaj birimi boş olduğunda
  yanlışlıkla tetiklenen onay düzeltildi; normal kullanıcılar erişim denetimi
  geçişinden sonra maliyet öğelerini yeniden onaylayabiliyor; bir tablo sütunu zaten
  mevcut olduğunda belge düzeyindeki izinler artık uygulanıyor.
- **Otomatik güncelleme:** uygulama, yeni bir sürümde "Şimdi Yenile" açılır
  penceresi göstermek yerine otomatik olarak yenileniyor; eski sürüm bilgisi
  diyaloğu kaldırıldı.
- **Gelen e-posta ayarları:** yeni hata bildirimi alıcıları anahtarı ve alanı; içe
  aktarma günlüğü artık giden etkinliği ve hata nedenini gösteriyor; gelen adres
  güvenilir şekilde kopyalanıyor.
- **Belge bölme:** Belge Bölme ekranı artık kaydırılabiliyor.
- **Karanlık mod:** tablo çıkarma, görev sayacı ve panodaki kapatılmış belge
  işaretleyicileri için düzeltmeler.
- **Kullanılabilirlik ve kararlılık:** pano dışa aktarma arayüzü düzeltmeleri;
  yapışkan tablo başlıkları artık diyalogların arkasından görünmüyor; DocNet panosu
  artık başarısız bir istatistik isteğinde çökmüyor; alan scriptleri boşaltılan
  alanları artık eski değerlerine geri döndürmüyor; PO ayarları onay kutuları ve
  düzen düzeltmeleri; sınıflandırma listesi görüntüleme düzeltmeleri.
- **Tedarikçiler:** tedarikçi kuruluşları artık magic link ile kayıt olabiliyor.

## API Service — canlı: `12.46.8`

- **DocBits MCP ağ geçidi:** birleşik bir ağ geçidi artık DocFlow araçlarını ana API
  üzerinden proxy'liyor; böylece AI asistanları her DocBits aracına tek bir uç nokta
  üzerinden ulaşıyor; MCP uç noktası, bağlantıları bozabilecek bir yönlendirme
  olmadan sunuluyor.
- **Muhasebe:** muhasebe kimliği için maliyet merkezi doğrulaması eklendi.
- **OCR yönlendirmesi:** tedarikçi e-metni kapatıldığında belgeler tam bir yeniden
  OCR için gönderiliyor, böylece metin güvenilir kalıyor.
- **Infor ERP / SAP:** ERP, masrafı zaten sıfır tutarında tuttuğunda ek masraflar
  doğru şekilde yönlendiriliyor.
- **Güvenilirlik (daha az sunucu hatası):** pano, tedarikçi faturası, PO kaydı ve
  görev yöneticisi sorguları güçlendirildi, böylece artık nadir 500 hataları
  döndürmüyorlar; daha dayanıklı kuruluş önbelleği senkronizasyonu ve saklanan dosya
  temizliği.
- **Daha temiz pano filtreleri:** gereksiz fatura numarası filtre alanı kaldırıldı;
  PO ile eşleştirilen miktar düzeltildi.
- **Geliştirici API belgeleri:** Swagger arayüzü artık DocBits markasıyla bir
  spesifikasyon açılır listesi sunuyor (OpenAPI 3.0 ve Infor Swagger 2.0 görünümü).

## Auth Service — canlı: `1.68.0`

- **Daha hızlı oturum kapatma / token iptali:** toplu token iptali artık dakikalarca
  sürüp bağlantıyı düşürmüyor.
- **Parola belirleme e-postaları düzeltildi**, böylece doğru şekilde görüntüleniyor.
- **Tedarikçiler:** tedarikçi kuruluşları magic link ile kayıt olabiliyor.
- **Oturum açma kararlılığı:** geçici bir kuruluş araması hatasında bir üye artık
  kilitlenmiyor ve geçersiz bir kuruluş kimliği artık bir hata yerine anlaşılır bir
  mesaj döndürüyor.

## Docflow Service — canlı: `2.4.1`

- **Güvenilir AI ağ geçidi:** DocFlow MCP uç noktasındaki takılmalar ve zaman
  aşımları düzeltildi (el sıkışma, istemci bağlantı kesilmeleri, yinelenen yanıtlar)
  — birleşik DocBits MCP ağ geçidinin DocFlow tarafı.

## OCR Service — canlı: `1.7.1`

- **Daha kararlı OCR işleme:** arka plan yanıt kuyrukları otomatik olarak sona eriyor
  ve geçici bağlantı hataları yeniden deneniyor, böylece daha az OCR işi takılıyor.

## PO Match Service — canlı: `1.55.7`

- Kural eşleştirmesi sırasında ürün kimliği, birim kodu ve statik değer sütunlarında
  artık **değer dönüşümleri** uygulanıyor.
- **Çökme korumaları:** fiyatı veya miktarı eksik bir satır, olağandışı bir ağırlıklı
  anahtar kombinasyonu ya da imkansız bir bölme işlemi artık eşleştirmeyi
  çökertmiyor.
- **Güvenilirlik:** veritabanı yazma işlemleri, kopan veya SSL ile kapatılan
  bağlantılarda otomatik olarak yeniden deneniyor.
- **Infor ERP / SAP:** ERP, masrafı sıfır tutarında tuttuğunda ek masraflar doğru
  şekilde yönlendiriliyor.

## Fulltext Service — canlı: `1.35.6`

- **Daha hızlı yeniden indeksleme:** tüm senkronizasyon aşamaları artık
  paralelleşiyor, böylece otomatik ölçeklendirme devreye giriyor; bu da yavaş seri
  yeniden indekslemeyi ve %0'da takılan ilerleme aracını düzeltiyor.
- **Daha kararlı istatistikler:** bölgeler arası belge istatistiği istekleri
  sınırlandırıldı, böylece artık zaman aşımına uğramıyor.

---

## Bu dönemde müşteriye yönelik değişiklik yok

26–30 Haziran arasında kararlı, kayda değer ürün değişikliği yok: Auto Accounting
(`1.18.6`), Barcode (`1.15.6`), Docnet (`1.54.6`), Email (`1.36.4`), Extraction
(`1.48.7`), FTP (`1.30.1`), Operator (`1.39.5`). Auto Accounting ve FTP yalnızca
dahili bakım aldı.

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-26 → 2026-06-30. -->

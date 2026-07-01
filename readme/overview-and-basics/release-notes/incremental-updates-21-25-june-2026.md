# DocBits Sürüm Notları — 21–25 Haziran 2026

_Bu production yükseltmesinin sade bir dille neler sağladığı. Her hizmet, şu anda
production ortamında canlı olan sürümü gösterir. Listelenmeyen hizmetlerde bu
dönemde müşteriye yönelik bir değişiklik olmamıştır._

---

## Öne Çıkanlar

- **Daha akıllı pano araması.** Belgeleri tutarlara ve sayılara göre güvenilir
  şekilde arayın — belirli bir değerin üzerindeki faturaları bulun veya **talep
  numarasına** göre arayın — metni değil gerçek sayıları karşılaştıran tutar
  aralıklarıyla. Fatura alt türleri, çevrilmiş adlarıyla aranabilir.
- **Güvenilir e-posta bildirimleri.** Durum değişikliği uyarıları artık her durum
  için gönderiliyor (sessizce düşen e-postalar yok) ve gelen içe aktarma alındıları
  ile hata bildirimleri artık alıcı bazında denetimlerle düzgün şekilde DocBits
  markasını taşıyor.
- **Bölgeler arası daha akıcı oturum açma (EU/US).** Bölge değiştirme artık tam
  ekran bir kesinti yerine küçük bir bilgi çubuğu şeklinde, tek oturum açma doğru
  bölgeye yönlendiriyor ve birden fazla tarayıcı sekmesinde oturumun açık kalması
  daha güvenilir.
- **İzin düzeltmeleri.** Kullanıcılar, gruplarının kendilerine verdiği erişimi
  alıyor — grup ve izinler daha az yaygın şekillerde yapılandırılmış olsa bile
  belgeleri açma, düzenleme, onaylama ve yeniden başlatma artık doğru çalışıyor.
- **Daha kararlı belge işleme.** Daha önce yüklemeden sonra takılıp kalan belgeler
  otomatik olarak yeniden işleme alınıyor ve bir müşteriden gelen ani yoğunluk
  artık diğerlerini yavaşlatmıyor.

---

## Web App — canlı: `10.32.4`

- **E-Fatura Doğrulama** ayarına doğrudan **hızlı arama sıçraması (Cmd/Ctrl + K)**.
- **Bölge ve oturum açma:** bölge değişimi, engelleyici bir ekran yerine kalıcı bir
  bilgi çubuğu olarak gösteriliyor; tek oturum açma artık doğru bölgeye (EU/US)
  yönlendiriyor; birden fazla sekmede oturumun açık kalması daha güvenilir.
- **İzinler:** kullanıcıların doğru grup izinlerine sahip olmalarına rağmen
  belgeleri **onaylayamadığı**, **düzenleyemediği**, **açamadığı** veya **yeniden
  başlatamadığı** durumlar düzeltildi.
- **Gelen e-posta ayarları:** yeni "Göndereni bilgilendir" ve "Alındığında göndereni
  yanıtla" anahtarları.
- **Kullanılabilirlik:** yinelenen belge uyarısının artık devam etmeden önce
  kapatılması gerekiyor; "arka uç kullanılamıyor" bilgi çubuğu yalnızca gerçek
  kesintilerde görünüyor; görev sayaçları görevler tamamlandığında anında
  güncelleniyor; AI tablo doğrulama ekranında karanlık mod düzeltmesi.
- **Performans:** alan doğrulaması ve PO eşleştirmesi sırasında e-belge ekranındaki
  bir donma düzeltildi.
- **Fatura alt türlerini çevrilmiş adlarıyla arayın.**

## API Service — canlı: `12.41.9`

- **Pano araması elden geçirildi:** talep numarası ve talep eden artık aranabilir;
  tutar ve sayı aramaları doğru sonuçlar döndürüyor (gerçek sayısal karşılaştırma);
  toplam net tutar ve hesaplanan sütunlar doğru görüntüleniyor.
- Herhangi bir belge durumu için **güvenilir durum uyarısı e-postaları**; gönderim
  hataları artık gizlenmiyor.
- **İzinler:** grubu olmayan kullanıcılar kendi belgelerini açıp onaylayabiliyor;
  grubu olmayan kullanıcılar için belge görünürlüğü geri getirildi.
- **Belge işleme güvenilirliği:** "yeni" durumunda takılan belgeler otomatik olarak
  yeniden kuyruğa alınıyor; adil paylaşımlı işleme sayesinde bir kuruluştan gelen
  büyük bir ani yoğunluk diğerlerini aç bırakmıyor; nadir görülen veritabanı sıra
  (sequence) sorunları için kendi kendini onarma.
- **Bozuk metin katmanına sahip taranmış PDF'ler**, güvenilmez metin üretmek yerine
  **OCR'a yönlendiriliyor**.
- **Çıkarma ve PO doğruluğu:** tedarikçi adı, bağlı satın alma siparişinden
  dolduruluyor; yinelenen ürün numarası sütunları kaldırıldı; özel (bölünmez)
  boşlukların daha iyi işlenmesi.
- **Infor ERP / SAP dışa aktarımı:** SFTP dışa aktarma kimlik doğrulaması
  düzeltildi.
- **E-faturalama:** ZUGFeRD / e-belge çıkarma yolu iyileştirmeleri.

## Auth Service — canlı: `1.66.0`

- Bazı kullanıcılar için **eksik kuruluş ataması düzeltildi** (boş org id).

## Docflow Service — canlı: `2.3.4`

- **İş akışı tetikleyici bekleme süresi** artık ortam bazında yapılandırılabilir.

## Email Service — canlı: `1.35.9`

- **Markalı e-postalar:** gelen içe aktarma alındıları ve hata bildirimleri artık
  gerçek DocBits logosunu ve renklerini kullanıyor.
- **Kuruluş bazında denetimler:** alındığında onay e-postası, hata durumunda
  "göndereni bilgilendir" ve göndereni yanıtla seçenekleri.
- **Daha güvenilir gelen içe aktarma:** içe aktarma sonuçları doğru şekilde
  kaydediliyor, kısmi hatalar (sessiz başarılar olarak değil) hata olarak
  raporlanıyor ve e-posta gövdelerindeki sorunlu karakterler artık içe aktarmayı
  bozmuyor.
- **EU/US yönlendirmesi:** kuruluş bazında doğru bölgesel API'ye yönlendirme.

## Fulltext Service — canlı: `1.34.5`

- **Tutarlara ve sayılara göre arama** artık binlik ayırıcılar ve tutar aralıkları
  dahil güvenilir şekilde çalışıyor (pano araması elden geçirmesinin arkasındaki
  motor).
- **Daha kararlı arama altyapısı:** sahipsiz kalan arka plan kuyrukları
  temizleniyor, böylece artık paylaşılan kaynakları meşgul etmiyor.

## PO Match Service — canlı: `1.54.7`

- **Daha sağlam satın alma siparişi eşleştirme:** metin tabanlı ambalaj/paketleme
  birimi kodları artık bir eşleşmeyi engellemiyor ve manuel satır eşleştirme boş
  sonuçları güvenli şekilde işliyor.

---

## Bu dönemde müşteriye yönelik değişiklik yok

21–25 Haziran arasında kararlı, kayda değer ürün değişikliği yok: Auto Accounting
(`1.18.5`), Barcode (`1.15.6`), Docnet (`1.54.6`), Extraction (`1.48.6`), FTP
(`1.30.0`), OCR (`1.6.8`), Operator (`1.39.5`).

<!-- Generated by the docbits-changelog skill (prod-delta mode). Versions read live
     from prod (do-fra1-polydocs/prod); window 2026-06-21 → 2026-06-25. -->

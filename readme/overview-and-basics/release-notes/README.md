# Sürüm Notları

> **En yeni hotfix sürümü:** [Güncellemeler — 14–29 Temmuz 2026](incremental-updates-14-29-july-2026.md): 29 Temmuz 2026 üretim yükseltmesiyle nelerin değiştiği — iki faktörlü kimlik doğrulamadan bölgeye uygun gelen e-postaya kadar. Tüm hotfix sayfaları gezinmede Sürüm Notları altında yer alır.

## **Release R1.0 13/14 Haziran 2026**

> **Sandbox Kullanılabilirliği:** 28 Nisan 2026

### Yeni Özellikler:

* **Etkinlik Günlüğü / Erişim Denetimi:**\
  Uyumluluk ve izleme amacıyla uygulama genelinde ayrıntılı etkinlik günlüğü ve erişim denetim izi. Tüm mikroservisler için ve zaman aralığına dayalı olarak farklı günlükleme türleri.

* **Genel Hızlı Arama:**\
  Uygulamanın herhangi bir yerinden Cmd+K / Ctrl+K tuşlarına basarak 200'den fazla rota ve 40'tan fazla sayfa içi özellik arasında arama yapın. Bulanık eşleştirme, ok tuşuyla gezinme ve tam Uygulama Dizini Sayfasına bağlantılarla birlikte en iyi 8 sonucu gösterir.

* **Site Haritası (Uygulama Dizini Sayfası):**\
  DocBits genelindeki her gezilebilir sayfayı ve sayfa içi özelliği (diyaloglar, kenar çubukları, paneller) kataloglayan aranabilir dizin sayfası. 18 kategoride düzenlenmiş olup tür filtreleri, kategori etiketleri, URL ile senkronize arama ve yönetici olmayan kullanıcılara kilitli olarak gösterilen izin korumalı girişler içerir.

* **Analiz Panosu:**\
  Yönetici Genel Bakış, API Metrikleri, Kalite Metrikleri, İşleme Performansı, Belge Akışı Analizi, Etkinlik Günlüğü, Olay Günlüğü ve Denetim İzi ile kapsamlı belge işleme analizi.

* **Pano Dışa Aktarma İşlevi:**\
  CSV veya XLSX formatlarında liste dışa aktarımına olanak tanıyan yeni pano dışa aktarma işlevi.

* **Tam Metin Arama / DocSearch:**\
  Gerçek zamanlı tedarikçi filtreleme, "Benzerlerini Bul" özelliği ve yapılandırılabilir indeksleme ayarlarıyla indekslenen tüm belgeler arasında AI destekli vektör araması.

* **Tedarikçi Teslimat İstatistikleri:**\
  Tedarikçi ile ilgili belge işleme metriklerine dair içgörü sağlayan yeni görünümler.

* **Hata Ayıklama Toplayıcısı:**\
  Ctrl+Shift+P tuşlarına basarak API çağrıları, WebSocket durumu, hatalar, konsol günlükleri, performans metrikleri ve ortam bilgileri dahil olmak üzere tam bir hata ayıklama anlık görüntüsü yakalayın. Anlık görüntüler panoya kopyalanabilir veya HTML formatlı bir rapor ve ekli JSON dosyasıyla doğrudan destek talebi olarak gönderilebilir.

* **AI Ajanları (DocNet):**\
  Gelen e-postaları otomatik olarak işleyen — belgeleri sınıflandıran, çıkaran ve yönlendiren — manuel müdahale olmadan çalışan otonom arka plan ajanları. Ajanlar atanmış görevleri bağımsız olarak yürütür ve insan yargısı gerektiğinde onay talepleri aracılığıyla kullanıcılara yükseltir. Etkinliği ve performansı izlemek için özel bir ajan panosu içerir.

* **Yeni E-Belgeler:**\
  XRechnung 3.0.2, ZUGFeRD 2.2/2.3.2, Factur-X çeşitleri ve Asya-Pasifik PINT Alacak Dekontları dahil olmak üzere 80'den fazla yeni küresel e-fatura türü ve 40'tan fazla yeni format. %100 sınıflandırma ve çıkarma kapsamı.

* **AI Script Sohbeti:**\
  Gerçek zamanlı akış yanıtlarıyla temel script geliştirme için AI destekli sohbet asistanı.

* **Script Sürümleme:**\
  Değişiklik takibi, karşılaştırma ve geri yükleme özellikleriyle scriptler için tam sürüm geçmişi. E-Belgelerin sürümlerinin korunma şekline benzer şekilde scriptlere sürüm yönetimi sağlar.

* **Pano Eylemlerinde Dışa Aktarma Geçmişi:**\
  Bir belgenin dışa aktarma geçmişine doğrudan pano eylem menüsünden erişin.

* **Genel API Dışa Aktarıcısı (APS450, GLS840):**\
  Harici sistemlerle esnek entegrasyon için bir Eşleme-Dosyası yapılandırması aracılığıyla yapılandırılabilir genel API dışa aktarma hedefi. APS450 ve GLS840 için destek uygulandı.

* **Birden Çok Dışa Aktarma Yapılandırması:**\
  Belge türü başına birden çok etkin dışa aktarma yapılandırması için yürütme sıralaması ve başarısız adımdan yeniden denemek için bir yeniden dışa aktarma düğmesi desteği.

* **Yeni Watchdog Sürümü:**\
  WatchDog Ayarları sayfasının tamamen yeniden çalışılması. Mevcut WatchDog Durumu, kurulum için kılavuz ve komutlar, XSLT şablonu yapılandırması ve otomatik güncelleme ayarı dahil olmak üzere yeni yaşam kalitesi özellikleri eklendi. Ayrıca WatchDog'un aynı anda birden çok yapılandırmayı işleme işlevi de uygulandı.

* **Vertex Entegrasyonu:**\
  Belge işleme sırasında otomatik vergi hesaplaması ve uyumluluk için Vertex aracılığıyla Tüketici Kullanım Vergisi entegrasyonu.

* **Arayüz Yeniden Tasarımı ve Ayarların Yenilenmesi:**\
  Uygulama genelinde kapsamlı arayüz yenileme. Yeniden tasarlanmış giriş ve kimlik doğrulama sayfaları. Daraltılabilir kenar çubuğu, düzenlenmiş alt kategoriler, çıpa tabanlı gezinme, bağlam yardım paneli ve durum takip rozetleriyle yeniden tasarlanmış ayarlar alanı. Belge scriptleri arayüz değişiklikleri. Belge akışı için yeni arayüz. Geliştirilmiş Değer Listesi arayüzü.

* **Fikir Panosu:**\
  Kullanıcıların yeni özellikler, iyileştirmeler, gerekli hata düzeltmeleri vb. göndermesi, tartışması ve oy vermesi için zengin metin editörü ve görsel desteğiyle özellik istek panosu.

* **API Anahtarı Yönetimi:**\
  Birden çok API anahtarı oluşturmak, görüntülemek ve yönetmek için özel ayarlar sayfası.

* **Ana Veri Arama İşlevi:**\
  Seçilen alanlara göre uygun arama seçenekleri sağlayarak geliştirilmiş Ana Veri arama yeteneği.

* **Kullanıcı Etkinliği Grafiği:**\
  Kullanıcı etkinlik kalıplarını ve etkileşim metriklerini gösteren görsel grafik. Trend karşılaştırma grafikleri, günlük/haftalık toplama ve GeoLite2 tabanlı coğrafi konum ile giriş etkinliği panosu.

* **Kullanıcı Giriş Geçmişi:**\
  Giriş geçmişi olan Kullanıcı Ayrıntı Görünümü.

* **Özelleştirilebilir Kenar Çubuğu:**\
  Kenar çubuğu menü öğeleri için sürükle-bırak ile yeniden sıralama, göster/gizle geçişi ve en üste sabitleme. Tercihler her kullanıcı için "Varsayılana sıfırla" seçeneğiyle kalıcı hale getirilir. Özellik bayraklarına uyar.

* **Video Karuseli:**\
  Kısa animasyonlu ürün ipucu videoları (Genel Arama, Klavye Kısayolları, Belge Yükleme, Tablo Özelleştirme) gösteren, prepare-dashboard sayfasında otomatik oynatılan video karuseli. Solda videolar ve sağda pano hazırlığı ile iki sütunlu düzen. Kullanıcılar videolara göz atarken otomatik yönlendirme duraklatılır.

* **Gelişmiş Workflow Tasarımcısı:**\
  Çok adımlı işleme kanalları için sürükle-bırak tuvaliyle görsel, düğüm tabanlı otomasyon oluşturucusu. Bekleme adımlarını, paralel yolları, yeniden kullanılabilir şablonları, Or koşul kartlarını, manuel test/çalıştır düğmesini, "Buradan Test Et" kısmi yürütmesini ve tam olarak hangi düğümlerin yürütüldüğünü gösteren görsel akış vurgulamasıyla düğüm başına yürütme günlüklerini destekler.

* **Workflow KPI Panosu:**\
  Workflow yürütmesini izlemek için temel metrik panosu.

* **Workflow Partner Kartı SDK'sı:**\
  Üçüncü taraf geliştiricilerin özel workflow kartları oluşturması için AI destekli inceleme, korumalı alanda doğrulama ve başlangıç dokümantasyonuyla SDK.

* **Workflow Test Yöneticisi:**\
  Yöneticilerin testleri tek tek veya toplu olarak oluşturup çalıştırmasına olanak tanıyan workflow'lar için otomatik test yöneticisi.

### İyileştirmeler:

* **Veritabanı (Tüm Modüller) — ID Sütunlarının Taşınması:**\
  Tüm DocBits "ID" veritabanı sütunları dahili olarak dizelerden özel ID türüne (UUID7) taşındı. Bu iyileştirmeyi desteklemek için temel Postgres veritabanı V18'e taşındı.

* **Belge İşleme — Ek İyileştirmeler:**\
  Dikkate alınacak maksimum sayfa sayısıyla ilgili dışa aktarma mantığı değiştiriliyor — artık belgenin tamamı dışa aktarılacak. Belge doğrulaması sırasında kullanıcı, bu belirli belge için varsayılan maksimum sayfa sınırını geçersiz kılma seçeneğine sahip olacak. Bekleyen Belge Sayacının hesaplanması geliştirildi.

* **Servis Sürümleri, Durumu ve Dağıtım Tarihi:**\
  "Servis Sürümleri" açılır penceresinde sağlanan servis kullanılabilirlik durumu.

* **Dil Genişletme:**\
  Güncellenmiş dil seçiciyle desteği 22 dile genişletildi.

* **Alan Düzeyinde Erişim Kontrolü Tasarımı:**\
  Daha net etkinleştirme durumu, alan düzeyinde erişim, tutarlı kural işleme ve basitleştirilmiş grup tabanlı izinlerle yeniden tasarlanmış/geliştirilmiş erişim kontrolü. Erişim Kontrolü ile Görüntüleme İzinleri arasındaki çakışan kuralları düzeltir, içe aktarma sahibini arayüzde gösterir ve erişim kontrolünü alan doğrulaması, AI ile çıkarılan tablolar ve tüm görünümlerde tutarlı bir şekilde uygular.

* **Tüm Ekranlar için Etkinlik Akışı:**\
  Etkinlik akışı artık yalnızca Onay Bekliyor'da değil, tüm belge işleme ekranlarında (Doğrulamaya Hazır, PO Eşleştirme, Muhasebe, Teklif Ayrıntıları, Reddet) mevcut. Tüm ekranlarda tutarlı bir sağ panel konumuna taşındı.

* **Belge Akışı Sayfası:**\
  Belge işleme akışını görselleştirmek ve izlemek, durum geçişlerini ve kanal boyunca ilerlemeyi göstermek için özel sayfa.

* **Çift Monitör Modu (Genel Kullanıcı Ayarı):**\
  Çift monitör modu, oturumlar arasında kalıcı olacak şekilde genel kullanıcı ayarına taşındı.

* **Layout Builder İyileştirmeleri:**\
  Görsel göstergelerle gizli ve salt okunur alanlar, yeniden boyutlandırılabilir panel ayırıcı ve alan uzunluğu ayarları desteği. Varsayılan Layout'u her birini tek tek ziyaret etmeden birden çok kaynağa uygulayın.

## **Release HotFix 3 16 Nisan 2026**

### DocBits İyileştirmeleri:

* **Polonya Faturaları için QR Kod Çıkarma:**\
  DocBits artık özellikle Polonya faturaları için QR kod çıkarmayı destekleyerek, Polonya kaynaklı belgeler için otomatik veri yakalamayı iyileştiriyor.

### Hata Düzeltmeleri:

* PO eşleştirme zaten gerçekleşmiş ancak satın alma siparişi belgeyle ilişkilendirilmemişken otomatik dışa aktarmanın başarısız olduğu bir sorun düzeltildi.
* Ambalaj birimleri (Verpackungseinheiten / VPE) olan faturalarda birim fiyatların yanlış yuvarlandığı bir sorun düzeltildi.
* ION/MEC'ten gelen dışa aktarma hata mesajlarının (ör. Acknowledge.PurchaseOrder hataları) DocBits'te görüntülenmediği ve dışa aktarma başarısız olmasına rağmen "Dışa Aktarıldı" durumunu gösterdiği bir sorun düzeltildi.
* AI tablo çıkarma kullanıldığında onay ekranındaki birim fiyatın yanlış olduğu bir sorun düzeltildi.
* Toplam Eşleştirme scriptinin doğrulama ekranında bir hata verdiği bir sorun düzeltildi.
* Belge işlemenin bir hatayla başarısız olduğu bir sorun düzeltildi ("UserAuthentication object has no setter for 'org_id'").
* Belirli tedarikçiler için tablo eğitiminin çalışmadığı, sütunların eşlenen alanlar yerine gizli sütunlara düştüğü bir sorun düzeltildi.
* Çok parçalı istek boyutu sınırının aşılması nedeniyle büyük faturalarda (10+ sayfa) PO eşleştirmenin başarısız olduğu bir sorun düzeltildi.
* Script ile doldurulan sütun değerlerinin belge yeniden başlatıldıktan sonra kalıcı olmadığı bir sorun düzeltildi.
* "Tablo Doğrulamasını Yoksay" geçişinin arayüzde etkin (yeşil) olarak göründüğü ancak arka planda aslında devre dışı olduğu bir sorun düzeltildi.
* İçe aktarmadan sonra belge kalitesinin önemli ölçüde düştüğü bir sorun düzeltildi.
* Tam bir dağıtım gönderiminden sonra uygulamada görüntülenen mikroservis sürümlerinin ve dağıtım tarihlerinin ortamlar arasında tutarsız olduğu bir sorun düzeltildi.
* Görev verilerinden kullanıcı kimlik doğrulama nesnesi oluştururken oluşan bir hata nedeniyle barkod çıkarmanın başarısız olduğu bir sorun düzeltildi.
* Tedarikçi portalında kaydederken tedarikçi iletişim bilgilerinin boşaltıldığı bir sorun düzeltildi.
* Belgelerin dışa aktarma sırasında bir NoneType hatasıyla karşılaştığı bir sorun düzeltildi.
* İlk ekli dosya bir PNG veya JPEG görseli olduğunda e-posta gövdesinin dahil edilmediği bir sorun düzeltildi.
* Birkaç belge için e-posta gövdesinin eksik olduğu bir sorun düzeltildi.
* DocBits Operator "ai-exporting"in hedef sistemlerde (LN/D3) dışa aktarma sonuçları üretmediği bir sorun düzeltildi.

## **Release HotFix 2 31 Mart 2026**

### DocBits İyileştirmeleri:

* **Hibrit PDF İşleme — Kullanıcı Kontrollü XML Çıkarma:**\
  Bir PDF, gömülü XML verisi içerdiğinde, kullanıcılar artık DocBits'in çıkarma için gömülü XML'i mi kullanacağını yoksa belgeyi standart bir PDF olarak mı işleyeceğini seçebilir. Bu, kuruluşlara hibrit belgelerin nasıl işleneceği üzerinde tam kontrol sağlar ve iş akışlarına en uygun çıkarma yönteminin uygulanmasını garanti eder.

* **Onay Ekranında AP Atama Kodu:**\
  AP Yöneticisi Onay sayfası artık Infor M3 CRS620 ile entegre bir AP Atama Kodu alanı içeriyor. Bu, onaylayanların harici sistemlere geçmeden doğrudan onay süreci sırasında atama kodlarını gözden geçirip onaylamasına olanak tanır.

* **Belge Toplamıyla PO Toplam Eşleştirme:**\
  DocBits artık satın alma siparişi toplamını belgedeki toplamla eşleştirmeyi destekleyerek, tutarsızlıkları süreçte daha erken yakalamak için PO eşleştirme sırasında ek bir doğrulama katmanı sağlıyor.

* **Tedarikçi Ürün Numarası ve VPE Güncellemesi:**\
  DocBits artık belge işleme sırasında Tedarikçi Ürün Numarası ve VPE (Verpackungseinheit / ambalaj birimi) alanlarını güncellemeyi destekliyor; değerler dışa aktarma sırasında M3'e geri senkronize ediliyor.

* **Geliştirilmiş Belge Düzeni Sınıflandırması:**\
  Belge düzeni kimliği (tfidf_id) artık altbilgi metni hariç yalnızca başlık metnine göre oluşturuluyor. Bu, altbilgi içeriğinin belge türü algılamasını etkilemesini önleyerek sınıflandırma doğruluğunu artırır.

* **Dışa Aktar ve Sonraki Düğmesi:**\
  Kullanıcıların mevcut belgeyi dışa aktarmasına ve hemen kuyruktaki bir sonrakine geçmesine olanak tanıyan yeni bir "Dışa Aktar ve Sonraki" düğmesi eklendi ve inceleme ile dışa aktarma iş akışı basitleştirildi.

* **Maliyet Faturaları için Onay Süreci:**\
  Maliyet faturaları için onay süreci, geliştirilmiş yönlendirme ve doğrulama mantığıyla iyileştirildi.

### Hata Düzeltmeleri:

* Yanlış bir kitaplık komutu nedeniyle Infor SFTP dışa aktarmasının bir hatayla başarısız olduğu bir sorun düzeltildi.
* Onay ekranında boole onay kutularının görüntülenemediği bir sorun düzeltildi.
* Satın alma biriminde uyumsuzluk olmamasına rağmen UNMU mesajlarının gönderildiği bir sorun düzeltildi.
* PO Eşleştirme ekranında satış vergisinin yanlışlıkla bir masraf olarak sınıflandırıldığı ve negatif bir ödenmemiş tutara yol açtığı bir sorun düzeltildi.
* Satın alma birimi sipariş onayında ayarlanmamış ancak satın alma siparişinde mevcut olduğunda dışa aktarmanın başarısız olduğu bir sorun düzeltildi.
* Birkaç belge için e-posta gövdesinin eksik olduğu bir sorun düzeltildi.
* Tedarikçi Ürün Numarasının onay ekranında görünmediği ve güncellemelerin M3'e gönderilmediği bir sorun düzeltildi.
* Tedarikçinin Infor'a dışa aktarımının bir hata döndürdüğü bir sorun düzeltildi.
* PO Eşleştirmenin işleme sırasında hatalar ürettiği bir sorun düzeltildi.
* `findAll` işlevinin belge scriptlerinde doğru çalışmadığı bir sorun düzeltildi.
* Watchdog "Güncelleyen" sütununun gerçek kullanıcı yerine yanlışlıkla Fellow Admin kullanıcısını gösterdiği bir sorun düzeltildi.
* BOD-Eşlemesinin Watchdog arayüzünde yapılandırılamadığı bir sorun düzeltildi.
* Masrafların masraf olarak görüntülenmek yerine yanlışlıkla ödenmemiş tutar olarak gösterildiği bir sorun düzeltildi.
* Bir eşleştirme yapılandırması mevcut olmasına rağmen çok satırlı faturalar için otomatik eşleştirmenin çalışmadığı bir sorun düzeltildi.
* Ürün numarasındaki bir tirenin ("-") satın alma siparişi için PO eşleştirme sırasında dikkate alındığı ancak faturada göz ardı edildiği ve yanlış bir uyumsuzluğa neden olduğu bir sorun düzeltildi.
* "PDF Dışa Aktar" geçişi devre dışı bırakıldığında bile hem PDF hem de XML dosyalarının dışa aktarma klasörüne yüklendiği bir sorun düzeltildi.
* Workflow kartındaki eksik bir durumun belgelerin workflow boyunca ilerlemesini engellediği bir sorun düzeltildi.
* İçe aktarmadan sonra belge kalitesinin önemli ölçüde düştüğü bir sorun düzeltildi.
* PO Eşleştirme ekranının bir hata verdiği bir sorun düzeltildi ("Cannot read properties of null").
* Varsayılan değer listesinin düzenlenemediği bir sorun düzeltildi.
* Workflow'un alan durumunu düzgün okuyamadığı ve yanlış yönlendirmeye neden olduğu bir sorun düzeltildi.
* Gelen e-posta içe aktarmalarının bir hatayla başarısız olduğu bir sorun düzeltildi.
* Dışa aktarma sırasında eksik satırların M3'e doğru bir şekilde ulaşmadığı bir sorun düzeltildi.
* Kodlanmış ve onaylanmış faturaların APS110 API aracılığıyla M3'te ara sıra "onaylandı" durumuna güncellenmediği bir sorun düzeltildi.
* Çok Bankalı yapılandırmanın doğru çalışmamasıyla ilgili bir sorun düzeltildi.
* Paylaşılan pano görüntüleme ve kaydetme davranışıyla ilgili birden çok sorun düzeltildi.
* Tedarikçi Ürün Numarası alanının 30 karakterle sınırlı olduğu ve daha uzun değerlerin saklanmasını engellediği bir sorun düzeltildi.
* Birim fiyat ve birim fiyat değerlerinin dışa aktarma sırasında bir hataya neden olduğu bir sorun düzeltildi.
* Dışlanmış bir duruma (ör. "Kapalı") sahip PO satırlarının, eşleştirme kuralları tarafından dışlanmalarına rağmen PO Eşleştirme ekranında yine de sürüklenip eşleştirilebildiği bir sorun düzeltildi.

### Yapılandırma Değişiklikleri:

* "Göreve Git" düğmesini kaldırmak için e-posta şablonları güncellendi.
* Maliyet öğelerindeki scriptler ve zorunlu alan ayarları düzenlendi.

## **Release HotFix 1 16 Mart 2026**

### DocBits İyileştirmeleri:

* **SFTP Dışa Aktarmada Belge Geçmişi:**\
  DocBits artık SFTP'ye dışa aktarırken, dışa aktarılan XML yükünün bir parçası olarak tam belge geçmişini dahil etmeyi destekliyor. Bu özellik Dışa Aktarma Ayarları aracılığıyla yapılandırılabilir ve alt sistemlere, DocBits içindeki bir belgede yapılan her durum değişikliği ve eylemin tam bir denetim izini sağlar — değişikliği kimin yaptığı, ne zaman gerçekleştiği ve önceki ile mevcut durumların ne olduğu dahil. Bu, özellikle uyumluluk, izlenebilirlik ve operasyonel analiz için değerlidir.
* **Infor On Premise için Sipariş Onayında Masraf Güncellemesi:**\
  Infor On Premise müşterileri artık masraf içeren Sipariş Onaylarını doğrudan DocBits içinde işleyebilir. Masraflar dışa aktarma yoluyla tamamen güncellenir, bu da uçtan uca Sipariş Onayı sürecini sorunsuz hale getirir ve alt sistemde manuel ayarlama ihtiyacını ortadan kaldırır.
*   **Varsayılan Layout'u Tüm Kaynaklara Uygula:**\
    Layout yapılandırma ekranında yeni bir **Varsayılan Layout'u Kaynaklara Uygula** düğmesi tanıtıldı. Yöneticiler artık bir kuruluş içindeki tüm kaynaklara Varsayılan layout'u tek bir eylemde uygulayabilir, böylece layout JSON'unu her kaynağa tek tek kopyalayıp yapıştırmanın zaman alıcı manuel sürecini ortadan kaldırır. Bu, birden çok kaynağın tutarlı bir şekilde yapılandırılması gereken yeni müşteri katılımı sırasında özellikle yararlıdır.

    <figure><img src="../../.gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>
*   **FTP İçe Aktarma için Belge Türü Seçimi:**\
    FTP içe aktarma yapılandırmaları artık klasör başına belge türü atamasını destekliyor. Bir FTP içe aktarma yapılandırırken, kullanıcılar o klasörden içe aktarılan tüm belgelere hangi belge türünün — Fatura veya Sipariş Onayı gibi — uygulanacağını belirtebilir. Belgeler içe aktarma sırasında otomatik olarak sınıflandırılır ve alım sonrası manuel belge türü atamasına ihtiyaç ortadan kalkar. Bu, farklı alt kuruluşlar ve klasörler arasında birden çok belge türünü yöneten kuruluşları destekler.

    <figure><img src="../../.gitbook/assets/image (4).png" alt=""><figcaption></figcaption></figure>
* **Infor On Premise için GLS840'a Dışa Aktarma**:\
  DocBits artık Infor On Premise müşterileri için belgeleri GLS840 programına dışa aktarmayı destekleyerek, şirket içi ortamlar için desteklenen dışa aktarma hedeflerinin kapsamını genişletiyor.
*   **Watchdog ve Dışa Aktarma Yapılandırması için Arayüz İyileştirmeleri:**\
    Watchdog yapılandırması ve Dışa Aktarma yapılandırması ekranları, bu ayarları yöneten yöneticiler için daha temiz bir düzen ve daha sezgisel bir deneyim sunan geliştirilmiş bir kullanıcı arayüzüyle yenilendi.

    <figure><img src="../../.gitbook/assets/image (1).png" alt=""><figcaption></figcaption></figure>



    <figure><img src="../../.gitbook/assets/image (2).png" alt=""><figcaption></figcaption></figure>

### Hata Düzeltmeleri:

* Geçerli görüntüleme haklarına sahip kullanıcıların belgeleri görüntüleyememesiyle ilgili bir sorun düzeltildi — izin mantığı, önceki grup tabanlı filtreleme yaklaşımının yerini alan bir erişim düzeyi kontrolüyle yeniden düzenlendi.
* Daha fazla kararlılık için uygulamanın birden çok alanında istisna işleme iyileştirildi.
* Alan çıkarma sırasında boole türü sütunların doğru işlenmediği bir sorun çözüldü.
* Dosya yükleme uç noktasındaki bir asenkron kimlik doğrulama sorunu düzeltildi.
* Doğrulama ekranındaki PO tablosu için arayüz görüntüleme sorunları çözüldü.
* Daha iyi denetlenebilirlik için değişiklik takibi yorumlarını içerecek şekilde script şablonu güncellendi.
* Doğrulama ekranında açılır menü alanlarının doğru davranmamasıyla ilgili bir sorun düzeltildi.
* Panodan belge atamaları güncellenirken alt kuruluş alanının önceden doldurulmadığı bir sorun düzeltildi.

## **Release Winter Summit 10 Aralık 2025**

### DocBits İyileştirmeleri:

*   **Geliştirilmiş PO Eşleştirme Kuralı Özelleştirmesi:**\
    DocBits artık satın alma siparişi eşleştirme kuralları üzerinde daha ayrıntılı ve özelleştirilebilir kontrol sağlıyor. Yöneticiler, her belge türü için eşleştirme süreci sırasında hangi sütunların değerlendirileceğini tam olarak yapılandırabilir ve yalnızca en ilgili alanların dikkate alınmasını sağlayabilir. Ayrıca, toleranslar sütun düzeyinde tanımlanabilir ve küçük tutarsızlıkları ele alırken daha fazla esneklik sağlar. Her kural ayrıca manuel eşleştirmeye, otomatik eşleştirmeye veya her ikisine de uygulanacak şekilde yapılandırılabilir ve ekiplere eşleştirme iş akışını tam operasyonel gereksinimlerine göre uyarlama olanağı verir. Bu iyileştirmeler, satın alma siparişi eşleştirme sürecinin uyarlanabilirliğini ve hassasiyetini önemli ölçüde artırır.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_3.png" alt=""><figcaption></figcaption></figure>
*   **Birden Çok Tedarikçi Finansal Hesabı Desteği:**\
    DocBits artık Infor tarafından sağlanan RemitToPartyMaster BOD aracılığıyla tedarikçiler için birden çok finansal hesabı yönetmeyi destekliyor. Bu iyileştirme, kuruluşların tek bir tedarikçi için birden çok ödeme hesabı kaydı tutmasına olanak tanıyarak ödeme işlemede esneklik ve doğruluğu artırır. Bu yeteneği etkinleştirmek veya devre dışı bırakmak için yeni bir yapılandırma ayarı tanıtıldı ve yöneticilerin özelliği operasyonel ihtiyaçlarına göre etkinleştirmesine olanak tanınır.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_1.png" alt=""><figcaption></figcaption></figure>
*   **OCR Çıkarma Sonuçlarına Kullanıcı Erişimi Ekleme:**\
    Alan Doğrulama ekranındaki **OCR Görünümü** düğmesi artık yalnızca yöneticilerle sınırlı olmak yerine, doğrulama erişimi olan tüm kullanıcılara sunuluyor. Bu güncellemeyle, yetkili herhangi bir kullanıcı OCR çıkarma sonuçlarını doğrudan gözden geçirebilir, bu da veri doğruluğunu doğrulamayı ve genel OCR performansını izlemeyi kolaylaştırır. Bu iyileştirme daha fazla şeffaflığı teşvik eder ve doğrulama iş akışının verimliliğini artırır.

    <figure><img src="../../.gitbook/assets/release_notes_12_2025_2.png" alt=""><figcaption></figcaption></figure>
* **Onay Ekranlarında Dinamik Sütun Oluşturma:**\
  Onay görünümleri, yalnızca her kuruluşun veritabanı tercihlerinde karşılaştırma için yapılandırılan sütunları dinamik olarak görüntüleyecek şekilde geliştirildi. Önceden, karşılaştırma için yapılandırılmadığında bazı kuruluşa özgü sütunlar boş görünür ve karışıklığa neden olurdu. Artık onay görünümleri yalnızca etkin olarak karşılaştırılan alanları gösteriyor. Bu, boş veya alakasız sütunlar olmadan daha net, kuruluşa özgü onay ekranları sağlar.
* **Ana Veri Aramasına Sipariş Türü Alanı Eklendi**:\
  Satın alma siparişi başlık listesi artık ana veri aramasında bir "Sipariş Türü" sütunu içeriyor ve ek kategorizasyon yetenekleri sağlıyor.
* **Özel Filtre Panosu İyileştirmeleri:**\
  Pano paylaşım işlevi, paylaşılan kullanıcılara daha fazla esneklik sağlamak için geliştirildi. Kendileriyle pano paylaşılan kişiler artık pano filtrelerini ayarlayıp düzenleyebilir ve görüntülenen bilgileri özel ihtiyaçlarına göre uyarlayabilir. Bu iyileştirme, daha kişiselleştirilmiş ve etkileşimli bir görüntüleme deneyimini destekler ve kullanıcıların görevleriyle en alakalı veri içgörülerini kolayca hassaslaştırmasını sağlar.
* **Onay Ekranı Sütunları için Özelleştirilebilir Önekler:**\
  Onay ekranlarında belge sütunlarından önce önekleri görüntülemek için yeni bir yapılandırılabilir seçenek tanıtıldı. Bu özellik doğrudan layout builder içinde yönetilebilir ve yöneticilere öneklerin gösterilip gösterilmeyeceği ve hangi belge türlerine uygulanacağı üzerinde tam kontrol verir. Bu seçeneği etkinleştirerek, kullanıcılar onay süreci sırasında belgeleri incelerken daha net bağlam ve gelişmiş okunabilirlik kazanır.

### Genel İyileştirmeler

* Tablo çıkarmada yetersiz eğitilmiş tablolar için hata günlüğü iyileştirildi.
* Panolar için en fazla 10 kullanıcı veya 5 grupla sınırlı bir paylaşım limiti ve limite ulaşıldığında net bir hata mesajı eklendi.
* Bir kullanıcı zaten var olan bir adla pano oluşturmaya çalıştığında özel panolar için hata işleme iyileştirildi.

### Hata Düzeltmeleri:

* E-postaların Tedarikçi Ayrıntıları bölümünden başarıyla gönderilmiş göründüğü ancak alıcılara teslim edilmediği bir sorun düzeltildi.
* Onay/reddetme ekranlarına eklenen Açılır menü alanlarının görüntülenmediği bir sorun düzeltildi.
* Dışa aktarılan tüm belgelerin yanlış kullanıcı tarafından son güncellenmiş olarak işaretlendiği bir sorun düzeltildi.
* Belgelerin "Workflow Devam Ediyor" durumunu gösterdiği ancak hiçbir workflow'un yürütülmediği ve günlüğün boş kaldığı bir sorun düzeltildi.
* Üzerinde herhangi bir iş yapmadan dışa aktarma sırasında belgelere alakasız kullanıcıların atandığı bir sorun düzeltildi.
* Doğru izinlere sahip kullanıcıların atanmış belgeleri reddedemediği ve hata aldığı bir sorun düzeltildi.
* Bazı kuruluşlar için belge akışı simgelerinin görüntülenmediği bir sorun düzeltildi.
* Belgeleri sürükle-bırak ile panoya yüklerken bir açılır pencerenin göründüğü bir sorun düzeltildi.
* API yanıtı tüm değerleri false olarak göstermesine rağmen E-TEXT bayraklarının arayüzde etkin olarak göründüğü bir sorun düzeltildi.
* Boş sayfalar içeren belgeler yüklenirken bir hata oluştuğu bir sorun düzeltildi.
* E-posta bildirimlerindeki görev bağlantılarının kullanıcıları doğru onay ekranına yönlendirmediği bir sorun çözüldü.
* Çapraz alt kuruluşun seçilmesinin Ana Veri Aramasının hiçbir tedarikçi göstermemesine neden olduğu bir sorun çözüldü. Kullanıcılar artık çapraz kuruluş tedarikçi verilerini doğru şekilde görüntüleyebilir.

## Release Autumn Summit 22 Ekim 2025

### DocBits iyileştirmeleri:

*   **E-posta Şablonu Tasarım İyileştirmeleri:**

    E-posta şablonu editörü, daha net bir yapı ve daha sorunsuz bir deneyim sağlamak için yeniden tasarlandı. Belge alanlarını seçmek artık daha sezgisel ve ekler doğrudan şablonlara dahil edilebilir. Bu iyileştirmeler, profesyonel, özelleştirilmiş e-postalar oluşturmayı daha hızlı ve kolay hale getirir.

    <figure><img src="../../.gitbook/assets/image (310).png" alt=""><figcaption></figcaption></figure>
*   **Pano İyileştirmeleri:**

    Pano, gezinme ve özelleştirmeyi iyileştirmek için genişletildi. Yeni sekmelerle kullanıcılar farklı belge türleri arasında daha hızlı geçiş yapabilir ve doğru görünümü ararken harcanan süreyi azaltabilir.

    <figure><img src="../../.gitbook/assets/image (474) (1).png" alt=""><figcaption></figcaption></figure>
*   **Özel Filtre Panoları:**\
    Ayrıca, panolar artık bireysel tercihlere göre özelleştirilebilir ve filtrelenebilir. Bu özel panolar meslektaşlarla da paylaşılabilir, bu da\
    ekip genelinde tutarlı raporlama görünümleri oluşturmayı kolaylaştırır.

    <figure><img src="../../.gitbook/assets/image (477).png" alt=""><figcaption></figcaption></figure>
*   **E-posta Bildirim Günlükleri:**

    Tüm e-posta bildirimleri için yeni bir günlükleme özelliği mevcut. Kullanıcılar artık gönderilen bildirimlerin geçmişini gözden geçirebilir, bu da teslimatları doğrulamayı ve e-postalar alınmadığında sorunları gidermeyi kolaylaştırır.
*   **E-Fatura Desteği: e-SLOG 1.6 ve 2.0:**

    Ek e-fatura formatları için destek tanıtıldı. Sistem artık e-SLOG sürümleri 1.6 ve 2.0'ı işleyebilir ve oluşturabilir, böylece iş ortakları ve mevzuat gereksinimleriyle uyumluluk genişletilir.
*   **Yinelenen Belge Tespiti İyileştirmeleri:**

    Yinelenen belge tespiti, iki güçlü yapılandırma seçeneğiyle yükseltildi. **Yinelenen Tespit Aralığı**, yinelenenleri daha kesin kontrol etmek için bir zaman aralığı tanımlamanıza olanak tanırken, **Yinelenenlerin Dışa Aktarımını Engelle** ayarı, yinelenen olarak tespit edilen belgelerin dışa aktarılmasını otomatik olarak önler. Bu iyileştirmeler birlikte daha fazla kontrol sağlar ve daha yüksek veri doğruluğu garanti eder.

    <figure><img src="../../.gitbook/assets/image (478).png" alt=""><figcaption></figcaption></figure>
*   **Karar Ağacı İyileştirmeleri:**

    Karar ağaçları artık belge alan değerlerini döndürme yeteneğiyle daha çok yönlü. Bu, daha gelişmiş otomasyon mantığına olanak tanır ve workflow'ların gerçek belge verilerine dayalı kararlar almasını sağlar.
*   **Yeni Workflow Kartları:**

    İki yeni workflow kartı otomasyon yeteneklerini genişletir. İlki, bir belgenin belirli bir alt kuruluşa ait olup olmadığını kontrol etmenize olanak tanır ve çok kuruluşlu kurulumları yönetmeyi kolaylaştırır. İkincisi, teslimat gereksinimlerini daha etkili bir şekilde yönetmeye ve uygulamaya yardımcı olmak için teslimat tarihlerini iş günü cinsinden mevcut tarihle karşılaştıran bir teslimat tarihi tolerans kontrolü tanıtır.
*   **CSV Dışa Aktarma İyileştirmeleri:**

    CSV dışa aktarma özelliği önemli ölçüde iyileştirildi. Sistem artık yalnızca geçerli sayfada görüntülenen belgeleri dışa aktarmak yerine, bir veri setindeki tüm belgeleri dışa aktarıyor. Her dışa aktarma bir günlük girişi oluşturur ve ortaya çıkan CSV otomatik olarak e-posta ile gönderilir, böylece daha eksiksiz ve güvenilir bir dışa aktarma süreci sağlanır.
*   **Satın Alma Siparişi Silme Zaman Aralığı:**

    Yeni bir yapılandırma seçeneği, yöneticilerin satın alma siparişi silme için bir zaman aralığı tanımlamasına olanak tanır. Bu iyileştirme, veri saklama politikaları üzerinde esneklik ve kontrol ekler ve satın alma siparişlerinin yalnızca uygun olduğunda kaldırılmasını sağlar.

### Hata Düzeltmeleri

* Belgeler dışa aktarılırken eski verilerin dahil edildiği bir sorun düzeltildi.
* Daha önce diğer durumları da gösteren Dışa Aktarma Hataları filtresi düzeltildi.
* Değerler doğru olmasına rağmen "Birim Fiyat"ın hata tetiklediği ancak "Birim Fiyat Başına"nın tetiklemediği bir tablo doğrulama uyumsuzluğu çözüldü.
* Panoya yeni bir sütun eklemenin başarısız olduğu bir sorun düzeltildi.
* Görevlerin pano görev sütununda görünmediği bir sorun düzeltildi.
* Listelerin artık tutarlı bir sıralamaya uyması için rastgele sıralama davranışı düzeltildi.
* Sütun boyutunu değiştirmenin durdurulamadığı bir sorun çözüldü.
* PO Eşleştirme ekranında manuel satır eşleştirmeyi engelleyen bir hata düzeltildi.
* Kaydettikten sonra e-posta eki seçeneğinin sıfırlandığı bir sorun düzeltildi.
* Otomatik muhasebenin ilk açıldığında başlangıçta veritabanı kimliklerini görüntülediği bir sorun düzeltildi.
* Değerlerin artık yanlış şekilde üzerine yazılmaması için bulanık alan davranışı düzeltildi.
* İçerik silindikten sonra otomatik hesaptaki alanların kaybolduğu bir sorun düzeltildi.
* Kullanıcının ayarlar açılır penceresinde "Ad" ve "Soyadı"nı yeniden adlandıramadığı bir hata düzeltildi.
* Belgelerin "workflow devam ediyor" durumunda takılabildiği bir sorun çözüldü.
* Seçilen kuruluş renklerinin doğru uygulanmadığı bir menü simgesi rengi sorunu düzeltildi.
* QR kodlarının bazen tanınmadığı bir sorun düzeltildi.
* Farklı bir hesap girmek için hesapların geri tuşuyla kaldırılamadığı bir sorun düzeltildi.
* Üretim gönderiminin ardından giriş yaptıktan sonra oluşan bir dil karışıklığı çözüldü.

## Release **Summer Bloom** Temmuz 2025

### DocBits iyileştirmeleri:

* **E-posta İçe Aktarma Günlüğü için Filtre Seçeneği:**\
  Kullanıcılar artık daha net, daha verimli bir genel bakış için içe aktarma günlüklerini filtreleme ve tabloyu sıralama olanağına sahip. Bu iyileştirme, e-posta girişlerini tanımlama ve yönetme sürecini basitleştirir, sorun giderme ve genel günlük yönetimini iyileştirir.
*   **Değer Listesi için Çok Dilli Destek:**\
    Çok dilli yetenekleri Değer Listesi özelliğine genişlettik. Yöneticiler artık etiketleri birden çok dilde tanımlayabilir ve doğru etiketin kullanıcının sistem dili ayarlarına göre otomatik olarak görüntülenmesini sağlayabilir. Bu iyileştirme daha fazla erişilebilirlik ve yerelleştirmeyi teşvik eder ve dünya çapındaki kullanıcıların platformla kendi ana dillerinde etkileşim kurmasını kolaylaştırır.

    <figure><img src="../../.gitbook/assets/image (13) (1) (1) (1) (2).png" alt=""><figcaption></figcaption></figure>
* **Ayarlarda Kullanıcı Ayrıntısı İyileştirmeleri:**\
  Ayarlar arayüzü artık kapsamlı kullanıcı bilgilerini görüntülüyor. Yöneticiler grup üyeliklerini, alt kuruluş ayrıntılarını ve ek anahtar verileri kolayca görüntüleyebilir, böylece kullanıcı rollerinin daha iyi yönetilmesini ve ekip yapılarının daha net anlaşılmasını sağlar. Ayrıca Yöneticiler artık Kuruluş için bir Sistem Yöneticisi oluşturabilir.
* **Onay Ekranında Otomatik Muhasebe Bilgileri:**\
  Onay ekranı artık fatura bilgileriyle birlikte otomatik muhasebe ayrıntılarını sunuyor. Bu iyileştirme, işlem verilerine daha derin içgörü sağlar, daha sorunsuz inceleme süreçlerini ve faturalarla ilgili daha bilinçli karar vermeyi kolaylaştırır.
* **Pano Görünümünde Belgeler için Görev Sayacı:**\
  Panodaki belgeler artık kendileriyle ilişkili açık görevleri gösterebilir ve bekleyen görevlerin toplam sayısını görüntüleyebilir. Bu özellik, kullanıcılara bekleyen eylemlere hızlı bir genel bakış sağlar, görev yönetimini ve iş akışı verimliliğini iyileştirir.
* **Tedarikçi Tabanlı AI Modeli Seçimi:**\
  Kullanıcılar artık veri çıkarma için kullanılan AI modelini tedarikçi bazında seçebilir. Bu iyileştirme, ince ayarlı optimizasyona olanak tanır ve farklı tedarikçiler için daha iyi çıkarma doğruluğu sağlayarak genel veri işleme sonuçlarını iyileştirir. [Daha fazla bilgi](https://docs.docbits.com/end-user-and-partner-section/end-user-section/validation-screen#supplier-based-ai-model)
* **Karar Ağacı Kartları için Geliştirilmiş Workflow Günlükleri:**\
  Günlükler artık karar ağacının çıktısını görüntülüyor, bu da workflow'lar içinde kararların nasıl verildiğini izlemeyi ve anlamayı kolaylaştırır.
*   **Sistem İşlevselliğini ve Kararlılığını Artırmak için Yeni Otomatik Test Kurulumunun Tanıtımı:**

    Platformumuzun genel işlevselliğini ve güvenilirliğini iyileştirmek için tasarlanmış yeni bir otomatik test sistemi uygulamasını duyurmaktan heyecan duyuyoruz. Bu yeni kurulum, deneyiminizi etkilemeden önce herhangi bir sorunu tespit etmek için sistemimizde tutarlı, kapsamlı kontroller yürütecektir. Bu testleri otomatikleştirerek, olası sorunlara daha hızlı yanıt verebilir ve sistemimiz için en yüksek kalite standartlarını koruyabiliriz.
* **Mikroservis Mimarisi Uygulaması:**\
  Temel bileşenleri özel mikroservislere bölerek platformu yeniden yapılandırdık. Bu mimari değişim ölçeklenebilirliği artırır, sistem performansını iyileştirir ve daha hızlı, daha modüler geliştirme ve dağıtım döngülerine olanak tanır.
*   **Kılavuzlu Tanıtım:**\
    Kullanıcıların uygulamanın farklı bölümlerinde daha kolay gezinmesine ve bunları anlamasına yardımcı olmak için artık kılavuzlu bir tanıtım mevcut. Bu, özellikle yeni kullanıcıların katılımı veya tanıdık olmayan özelliklerin keşfedilmesi için yararlıdır.

    <figure><img src="../../.gitbook/assets/image (430) (1).png" alt=""><figcaption></figcaption></figure>
* **Karar Ağacı İyileştirmeleri:**\
  Karar ağacı arayüzünde, bakım ve düzenlemeyi basitleştirmek için artık ağacın en üstünde yer alan daha sezgisel bir satır ekleme özelliği dahil olmak üzere iyileştirmeler yapıldı.
* **DocOperator**\
  DocOperator gibi yeni AI destekli araçlar, tekrarlayan görevleri otomatikleştirmeye yardımcı olur, verimliliği artırır ve belge iş akışlarında manuel çabayı azaltır.
*   **Elektronik Belge Önizleme Seçeneği:**\
    Elektronik belgeler (eDocs) için bir önizleme özelliği eklendi ve kullanıcıların değişiklikleri dağıtmadan önce doğrudan ayarlar içinde test edip görüntülemesine olanak tanındı.\\

    <figure><img src="../../.gitbook/assets/image (3) (1) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **Yeni Dil Desteği – Çince:**\
  DocBits artık Çince'yi destekliyor ve küresel pazarlardaki kullanıcılar için erişilebilirlik ve yerelleştirme seçeneklerini genişletiyor.
* **Geliştirilmiş Görev Panosu:**\
  Görev panosu, aynı anda daha fazla sayıda görev görüntüleyecek şekilde geliştirildi ve kullanıcılara daha net bir genel bakış sağlayarak görev takibini iyileştirdi.
*   **PO Eşleştirme İyileştirmeleri:**

    Farklı eşleştirme durumları için görsel göstergeler eklendi

    Belge türü başına zaten eşleştirilmiş PO satırlarını yoksaymak için yeni ayar

    Tutarlılığı sağlamak için PO güncellemeleri için otomatik kontrol iyileştirildi
* **Layout Builder İyileştirmeleri:**\
  Artık hem alan adlarını hem de alan başlıklarını arayabilirsiniz, bu da layout bileşenlerini yapılandırmayı ve bulmayı daha hızlı ve kolay hale getirir.
* **Onay Ekranında Dışa Aktar ve Sonraki Düğmesi:**\
  Onay ekranına, kullanıcıların bir belgeyi dışa aktarmasına ve otomatik olarak "Doğrulamaya Hazır" kuyruğundaki bir sonrakine geçmesine olanak tanıyan yeni bir düğme eklendi.
* **Yeni Workflow Kartları:**\
  Yeni satın alma siparişleri ve teklifle ilgili olaylar üzerinde workflow'lar çalıştırmak için olanlar dahil olmak üzere yeni workflow kartları tanıtıldı. Bunlar daha fazla otomasyon seçeneği sağlar.
*   **Watchdog İyileştirmeleri:**\
    Watchdog yapılandırması ana uygulama arayüzüne taşındı ve yönetimi kolaylaştırıldı. Ayrıca daha iyi izleme ve kontrol için ek işlevler tanıtıldı.\\

    <figure><img src="../../.gitbook/assets/image (4) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **Satır Reddetme İyileştirmeleri:**\
  Bir satır öğesinin reddedilmesi artık kullanıcıların bir neden belirtmesini gerektiriyor, bu da inceleme iş akışlarında daha iyi izlenebilirlik ve hesap verebilirlik sağlıyor.
* **Ayarlarda Tedarikçi AI Modeli Listesi:**\
  Yeni bir ayarlar görünümü, belirli tedarikçilere atanan AI modellerini ve bunları sıfırlama seçeneğini görüntüler. Bu, tedarikçi tabanlı AI yapılandırmalarının şeffaflığını ve yönetilebilirliğini iyileştirir.
*   **Belge Günlüğü İyileştirmeleri:**\
    Belge günlükleri artık daha iyi denetim ve sorun gidermeyi desteklemek için daha ayrıntılı bilgi içeriyor.

    <figure><img src="../../.gitbook/assets/image (5) (1) (1) (1) (1).png" alt=""><figcaption></figcaption></figure>
* **PNG ve JPG Desteği:**\
  Artık PNG ve JPG dosyalarını yükleyebilirsiniz; bunlar işlenmek üzere otomatik olarak PDF formatına dönüştürülür.
* **IDM Dışa Aktarma Belge Formatı Yapılandırması:**\
  IDM'deki PDF'lerin dışa aktarma formatı artık yapılandırılabilir, bu da kullanıcılara belgelerin nasıl oluşturulduğu üzerinde daha fazla kontrol sağlar.
* **Yeni eDoc Türü – EDIFACT INVOIC02:**\
  Artık EDIFACT INVOIC02 elektronik belge türünü destekliyoruz ve standartlaştırılmış fatura formatlarıyla uyumluluğu genişletiyoruz.
*   **E-posta Bildirimi ve Şablon Seçenekleri**

    DocBits artık e-posta bildirimleri üzerinde geliştirilmiş kontrol sunuyor:

    * **Zamanlanmış Yeniden Gönderme:** Herhangi bir işlem yapılmazsa belirli bir süre sonra bildirim e-postalarını otomatik olarak yeniden gönderin, böylece görevlerin kaçırılmamasını sağlayın.
    * **Yeniden Atamada Yeniden Gönderme:** Görevler yeniden atandığında da bildirimler tetiklenebilir, böylece kullanıcılar sorumluluk değişikliklerinden haberdar tutulur.
    * **Özel E-posta Şablonları:** Yöneticiler artık konu satırlarını, mesaj içeriğini ve biçimlendirmeyi özelleştirmek için e-posta şablonları oluşturabilir ve yönetebilir. Bu, kuruluşunuzun iletişim tarzına uygun kişiselleştirilmiş, bağlama duyarlı bildirimlere olanak tanır.

    Bu eklemeler iletişim verimliliğini artırır ve belge işleme iş akışlarındaki gecikmeleri azaltır.
*   **Panoda PO Durumu**

    Pano artık **bağlantılı satın alma siparişlerinin (PO'lar) durumunu** doğrudan belge genel bakışlarında görüntüleme seçeneği içeriyor. Bu iyileştirme, kullanıcılara alındı veya faturalandı gibi PO ilerlemesine anında içgörü sağlar, daha hızlı karar vermeyi ve belgeler ile satın alma süreçleri arasında daha iyi uyumu mümkün kılar.

### Hata Düzeltmeleri

* Görevlerin doğrulama/onay ekranında görünmediği bir sorun çözüldü.
* Sonraki/Önceki düğmesinin sabit kalması için konumlandırması düzeltildi.
* Script ve karar ağacı görünümlerindeki kaydırma sorunları düzeltildi ve eylem düğmelerinin kaydırma sırasında sabit kalması sağlandı.
* E-faturalardan menşe ülke alanı kaldırıldı.
* Görev sayacının yanlış sayıda görev görüntülemesiyle ilgili bir sorun düzeltildi.
* Eksik çeviriler eklendi.
* Özel alanlar, kimlikler yerine açıklayıcı adları görüntüleyecek şekilde düzeltildi.
* Belgelerin yanlış dosya adıyla indirildiği bir sorun çözüldü.
* PO eşleştirmedeki fatura satırı tablosunda sıralama tutarsızlıkları düzeltildi.
* Görev oluşturma işlevini etkileyen bir sorun düzeltildi.
* PO eşleştirmede bir satır eşleştirilirken fatura tablosu sıralamasının sıfırlandığı bir sorun düzeltildi.
* Bir tutar bölündüğünde muhasebe referanslarının doğru şekilde bölünmesi sağlanarak otomatik muhasebe sorunları çözüldü.
* ClickHouse ana bilgisayar bilgileri güncellendi.
* Yinelenen belgelerin yinelenen olarak tanınmadığı bir sorun çözüldü.
* Çok uzun muhasebe referanslarının neden olduğu dışa aktarma sorunları düzeltildi.
* Otomatik muhasebe için verilen tahminler düzeltildi.
* Salt okunur onay kutularının salt okunur olmadığı bir sorun çözüldü.
* Kullanıcıların bir alt kuruluşa iki kez eklenebildiği bir sorun düzeltildi.
* Bir belge için alt kuruluşun değiştirilmesinin atanan kullanıcıyı veya grubu sıfırlamasına neden olduğu bir sorun düzeltildi.
* auto.accounting Ekranıyla ilgili bazı sorunlar çözüldü.
* Kullanıcıların FTP yapılandırması ekleyemediği bir sorun düzeltildi.
* SSO girişiyle ilgili bir sorun düzeltildi.
* Gelen E-postalarla ilgili bazı sorunlar düzeltildi.
* Belgeler indirilirken yanlış ad almasıyla ilgili bir sorun düzeltildi.
* Karar ağacının yanlış sonuç döndürdüğü bir sorun düzeltildi.

## Release Hot Fix Winter Frost 10 Nisan 2025

### DocBits iyileştirmeleri:

* **Geliştirilmiş `set_column_date_value` Script İşlevi:**\
  `set_column_date_value` işlevi artık `skip_weekend` seçeneği için destek içeriyor ve uygulandığında tarih değerlerinin hafta sonlarını otomatik olarak atlamasına olanak tanıyor.
* **Geliştirilmiş Dosya Yükleme Desteği:**\
  PNG ve JPEG dosyaları artık doğrudan yüklenebilir ve basitleştirilmiş belge işleme için otomatik olarak PDF formatına dönüştürülür.
* **Watchdog İşlevsellik Yükseltmeleri:**
  * Daha iyi sistem entegrasyonu için artık **Enaio**'ya dışa aktarmayı destekliyor.
  * `Sync.ContentDocument` XML yapılarından bilgi çıkarmak için geliştirilmiş ayrıştırma yetenekleri, daha verimli veri işlemeye olanak tanır.

### Hata Düzeltmeleri

* Bir script işlevindeki bir sorun düzeltildi.
* Satın alma siparişlerinin güncellendikten sonra yanlış bir duruma sahip olduğu bir sorun çözüldü.

## Release Hot Fix Winter Frost 17 Mart 2025

### Hata Düzeltmeleri

* Kısayollar iyileştirildi.

## Release Hot Fix Winter Frost 11 Mart 2025

### DocBits iyileştirmeleri:

* **Geliştirilmiş Veri Çıkarma:** **Satın Alma Siparişini** veya **Ürün Numarasını** üstteki veya alttaki bir satırdan çıkarma seçeneği eklendi.
* **Genişletilmiş Çapraz Alt Kuruluş Erişimi:** Yönetici olmayan kullanıcılar artık **Çapraz Alt Kuruluşlar** özelliğine de erişebilir. [Daha fazla bilgi](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

### **Hata Düzeltmeleri:**

* Kullanıcıların bir gruba eklenemediği bir sorun düzeltildi.
* E-posta içe aktarma hatalarıyla ilgili bir sorun düzeltildi.
* Birden fazla sayfaya sahip belgelerde alan eğitimiyle ilgili bir sorun çözüldü.
* Scriptlerin düzgün çalışmadığı bir sorun düzeltildi.
* Belge verilerinin doğru görüntülenmediği bir sorun çözüldü.
* Otomatik güncelleme satın alma siparişi ayarıyla ilgili bir sorun düzeltildi.
* Abonelik tokenlarının yanlış görüntülendiği bir sorun düzeltildi.
* Görev ekranının güncel olmayan bir belge sürümünü görüntülediği bir sorun çözüldü.
* Belgelerin durumlarını değiştirmemesine neden olan bir sorun düzeltildi.

## Release Hot Fix Winter Frost 3 Şubat 2025

### **DocBits İyileştirmeleri:**

* **ZUGFeRD için ISO-8859-1 Desteği:** ISO-8859-1 karakter kodlaması kullanan faturalar için uyumluluk iyileştirildi.
* **Optimize Edilmiş Günlükleme Sistemi:** Daha hızlı sorun tanımlama ve çözümü için geliştirilmiş izleme ve tanılama.

## Release Winter Frost 22 Ocak 2025

#### Yeni Özellikler

### ZUGFeRD 2.1 ve Daha Yeni Sürümler için Destek

DocBits artık ZUGFeRD 2.1 ve üzeri sürümler için tam destek içeriyor ve ZUGFeRD uyumlu elektronik faturaların sorunsuz bir şekilde işlenmesini ve yönetilmesini sağlıyor. Entegrasyon şunları garanti eder:

* **Uyumluluk**: DocBits, ZUGFeRD faturalarını hem yapılandırılmış (XML) hem de yapılandırılmamış (PDF) formatlarında yönetebilir ve e-faturalama için EN 16931 gibi AB standartlarıyla uyumluluğu korur.
* **Verimlilik**: Kullanıcılar ZUGFeRD e-faturalarından verileri zahmetsizce içe aktarabilir, doğrulayabilir ve çıkarabilir, böylece manuel veri girişi en aza indirilir ve işleme süresi azaltılır.
* **Esneklik**: ZUGFeRD standardı içinde temel, konfor veya genişletilmiş profillerle çalışıyor olsanız da, DocBits her düzeydeki fatura karmaşıklığını yönetmek için araçlar sağlar.
* **Geleceğe Hazırlık**: Daha yeni sürümler için destekle DocBits, işletmelerin AB üye devletleri ve ötesindeki gelişen e-faturalama düzenlemeleriyle uyumlu kalmasını sağlar.

ZUGFeRD 2.1 ve daha yeni standartları dahil ederek, DocBits sınır ötesi işlemleri basitleştirir ve modern iş ihtiyaçlarıyla uyumlu hale gelir, bu da onu dijital dönüşüme ve mevzuata uyumluluğa öncelik veren kuruluşlar için önemli bir araç yapar. [Daha fazla bilgi](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/edi/zugferd-1.0-2.1-and-2.3)

### Geliştirilmiş Belge İşleme için Harici API Entegrasyonu

DocBits, belge işleme sırasında harici API'lerden yararlanmak için gelişmiş bir yetenek sunuyor ve çıkarılan verilerin eksiksizliğini ve doğruluğunu artırıyor. Bu özellik, güvenilir kaynaklardan gerçek zamanlı olarak alınan doğru, güncel bilgilerle eksik alanları doldurarak manuel girişi önemli ölçüde azaltır. Belgelerin daha hızlı ve daha tutarlı bir şekilde işlenmesini sağlar.

### Çapraz Alt Kuruluş Erişimi

Birden çok alt kuruluşun etkinleştirildiği kuruluşlar için, DocBits artık Çapraz Alt Kuruluşlar özelliğini sunuyor. Bu iyileştirme, yönetici kullanıcıları tek bir çatı altındaki tüm alt kuruluşlar arasında belge yönetimini basitleştirme gücüyle donatır. Yönetici kullanıcılar artık alt kuruluş değiştirmeden her alt kuruluştan tüm belgelere erişebilir ve bunları görüntüleyebilir. Bu merkezi görünürlük, yöneticilerin tüm alt kuruluşlar için tüm belgeleri görmesine olanak tanır, bir kuşbakışı görünümü korurken belirli dosyaları bulmayı kolaylaştırır. [Daha fazla bilgi](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/sub-organizations#cross-sub-organisations-access)

<figure><img src="../../.gitbook/assets/CrossSubOrganisations.png" alt=""><figcaption></figcaption></figure>

### Grup İzinlerine Dayalı Belge Görünürlüğü

DocBits, grup tabanlı izinler aracılığıyla yönetici olmayan kullanıcılar için daha hassas erişim yönetimi sağlayan geliştirilmiş belge görünürlüğü kontrolleri sunuyor. Bu özellik, yöneticilerin hangi belgelerin belirli kullanıcılara veya gruplara görünür olduğunu tanımlamasına olanak tanır, böylece basitleştirilmiş iş akışları ve gelişmiş veri güvenliği sağlar. Yönetici kullanıcılar belgeleri belirli gruplara atayabilir ve görünürlüğü yalnızca o gruplardaki kullanıcılara verebilir. Bu, kullanıcıların yalnızca rolleri veya ekipleriyle ilgili belgeleri görmesini sağlar, karmaşayı azaltır ve odaklanmayı artırır. [Daha fazla bilgi](https://docs.docbits.com/administration-and-setup/settings/global-settings/groups-users-and-permissions/groups-and-permissions)

<figure><img src="../../.gitbook/assets/Group Based Permission.png" alt=""><figcaption></figcaption></figure>

### Sıralı Workflow ve Onay Geçmişi

DocBits, belge işleme verimliliğini ve hesap verebilirliğini artırmak için tasarlanmış güçlü bir Sıralı Workflow ve Onay Geçmişi özelliği sunuyor. Belgelerin önceden tanımlanmış bir karar ağacını takip etmesine olanak tanıyarak, bu özellik yapılan eylemlerin eksiksiz bir kaydını korurken düzenli inceleme ve onayı garanti eder. Sıralı Workflow Yönetimi:

* Belgeler önceden tanımlanmış bir sırayla birden çok kullanıcıya atanabilir, böylece her inceleme veya doğrulama aşamasının doğru sırada gerçekleşmesi sağlanır.
* Workflow'daki her kullanıcı, belge üzerinde işlem yapma sırası geldiğinde bilgilendirilir, böylece karışıklık ve gecikmeler azalır.
* Workflow'lar belirli iş süreçlerine uyacak şekilde özelleştirilebilir

**Onay Geçmişi:**

* Belge üzerinde yapılan tüm eylemlerin eksiksiz bir günlüğü Doğrulama ve Onay görünümlerinde mevcuttur. Bu şunları içerir:
  * Kullanıcı eylemleri (ör. "onaylandı" "reddedildi")
  * Her eylem için zaman damgaları
  * İnceleme sırasında kullanıcılar tarafından eklenen yorumlar veya notlar
* Geçmiş şeffaflığı garanti eder ve uyumluluk ile sorun giderme için bir denetim izi sağlar. [Daha fazla bilgi](https://docs.docbits.com/administration-and-setup/settings/global-settings/document-types/more-settings/approval-history)

<figure><img src="../../.gitbook/assets/Approval History.png" alt=""><figcaption></figcaption></figure>

### SFTP/FTP Belgeleri Arşivi İyileştirmesi

DocBits'teki SFTP/FTP Belgeleri Arşivi iyileştirmesi, mevcut içe aktarma işlevselliği üzerine inşa edilir ve dosyaları işlendikten sonra arşivlemek için sorunsuz bir yöntem sunar. FTP içe aktarma yapılandırmasındaki yeni bir ayar, kullanıcıların dosya arşivlemeyi etkinleştirmesine veya devre dışı bırakmasına olanak tanır. Dosyalar DocBits'te başarıyla alındıktan ve işlendikten sonra, seçenek etkinse SFTP/FTP sunucusundaki belirlenmiş bir klasöre otomatik olarak arşivlenir. Bu, işlenen dosyaların, aktif içe aktarma dizinlerini karıştırmadan kayıt tutma amacıyla korunmasını sağlar. [Daha fazla bilgi](https://docs.docbits.com/end-user-and-partner-section/end-user-section/how-to-import-documents/ftp)

<figure><img src="../../.gitbook/assets/SFTPArchieve.png" alt=""><figcaption></figcaption></figure>

### Vergi Türü için Birden Çok Vergi Bölümü ve LN'ye Dışa Aktarma

Bu özellik, vergi bilgilerinin ayrıntılı sınıflandırılmasını ve Infor LN'ye dışa aktarılmasını sağlayarak (Tam Vergi, İndirimli Vergi, Vergisiz) vergi işleme yeteneklerini geliştirir. Bu, karmaşık vergi yapılarıyla daha iyi uyum sağlar ve muhasebe sistemleriyle sorunsuz entegrasyonu garanti eder.

**Tür Başına Birden Çok Vergi Bölümü**:

* DocBits artık her vergi türü altında birden çok vergi bölümü eklemeyi destekliyor, örneğin:
  * Tam Vergi: Standart VAT veya satış vergisi oranları.
  * İndirimli Vergi: Belirli mal veya hizmetler için daha düşük oranlar (ör. temel ürünler).
  * Vergisiz: Uygun işlemler için muafiyetler.
* Bu bölümler, vergi tutarlarının hassas kategorizasyonuna olanak tanır ve vergi düzenlemeleri ile muhasebe standartlarına uyumu garanti eder.

**Dinamik Otomatik Muhasebe Entegrasyonu**:

* Belge işleme sırasında çıkarılan verilere dayanarak, ilgili vergi bölümleri Otomatik Muhasebe Ekranında otomatik olarak görüntülenir.
* Bu, kullanıcıların vergi girişlerini manuel hesaplama veya yeniden giriş olmadan hızlıca doğrulamasını ve ayarlamasını sağlar, böylece iş akışı basitleştirilir.

**Infor LN'ye Dışa Aktarma**:

* Tüm ilgili bölümler ve sınıflandırmalar dahil olmak üzere vergi verileri, DocBits'teki belge işleme ile kurumsal kaynak planlama (ERP) sistemi arasında tutarlılık sağlayarak Infor LN'ye sorunsuz bir şekilde dışa aktarılır.
* Dışa aktarılan veriler, Infor LN'deki ilgili maliyet satırlarına bağlanır, böylece net izlenebilirlik ve doğru finansal raporlama korunur.

<figure><img src="../../.gitbook/assets/MultipleTaxLInes.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../../.gitbook/assets/MultipleTaxLineAuto Accounting.png" alt=""><figcaption></figcaption></figure>

### Pano İyileştirmeleri

DocBits, kullanılabilirlik, verimlilik ve gelişmiş veri görünürlüğüne odaklanarak panoya önemli güncellemeler getirdi. Bu iyileştirmeler, kullanıcıların belgeleriyle etkileşim kurmasını ve bunları yönetmesini kolaylaştıran yeni bir "Gruba Atandı" filtresi ve Belge Günlükleri için optimize edilmiş bir arayüz içerir.

### PO Eşleştirme İyileştirmeleri

DocBits, satın alma siparişi (PO) satırlarını faturalarla eşleştirme sürecini basitleştirmek için tasarlanmış PO Eşleştirme Ekranına çeşitli kullanılabilirlik iyileştirmeleri sunuyor. Bu iyileştirmeler, çok satırlı seçim için daha sezgisel kontroller sunar ve güncel olmayan PO verilerini işlemek için net görsel göstergeler sağlar.

**Bireysel Satır Seçimi için Ctrl + Tıklama**:

* Kullanıcılar artık Ctrl tuşunu basılı tutabilir ve PO eşleştirme ekranında birden çok, bitişik olmayan satır seçmek için belirli satırlara tıklayabilir.

**Aralık Seçimi için Shift + Tıklama**:

* Kullanıcılar Shift tuşunu basılı tutarak, ilk satıra tıklayarak ve ardından son satıra tıklayarak bir satır aralığı seçebilir. İlk ve son seçim arasındaki tüm satırlar otomatik olarak seçilir.

**Otomatik Güncel Olmayan Veri Tespiti**:

* Bir faturayla ilişkili PO verisi eskiyse (sistem ayarlarına göre), kullanıcıyı bilgilendirmek için bir simge görüntülenir. Bu görsel gösterge, kullanıcıların satın alma siparişindeki en son güncellemeleri yansıtmayabilecek eski verilerden haberdar olmasını sağlar.

### Hata Düzeltmeleri

* Otomatik muhasebe süreçleri sırasında tüm olası değerlerin doğru şekilde görüntülenmesini sağlamak için bir sorun çözüldü.
* Gezinme ve kullanılabilirliği daha sezgisel hale getirmek için Workflow Günlüklerinin kullanıcı arayüzü iyileştirildi.
* Belge alanları, gerekli ve gizli bayraklar gibi ek bilgileri doğrudan kullanıcı arayüzünde görüntüleyecek şekilde güncellendi.
* Grup ayarlarında grup açıklamalarının görünürlüğü eklendi.
* Hataları önlemek için oluşturma sırasında grup adları için uzunluk kısıtlamaları görüntülendi.
* Karar ağacı test işlevindeki sorunlar giderildi ve çeviri tutarsızlıkları çözüldü.
* Daha doğru ve etkili arama sonuçları için Workflow Günlüklerindeki arama işlevi iyileştirildi.
* Kullanıcıların e-belge taslaklarını yanlışlıkla silmesini önlemek için bir sorun düzeltildi.
* Sorunsuz entegrasyon ve veri işleme sağlamak için e-posta içe aktarma sürecindeki hatalar çözüldü.
* Tutarlı veri saklamayı sağlayarak AI ile oluşturulan etiketlerin kaydedilmesiyle ilgili sorunlar düzeltildi.
* Panonun farklı sayfalarında sıralama uygulanırken oluşan bir sıralama sorunu düzeltildi.
* DocBits tarafından işlenen belge sayısını doğru şekilde görüntülemek için belge sayacı geliştirildi.
* Farklı diller için kullanılabilirliği artırmak amacıyla uygulama genelinde çeviriler iyileştirildi.

## Release Hot Fix Feast 17 Aralık 2024

### **DocBits İyileştirmeleri:**

#### E-posta İçe Aktarma İyileştirmeleri

* Kullanıcılar artık E-posta İçe Aktarma özelliği aracılığıyla XML ve EDI dosyalarını sorunsuz bir şekilde içe aktarabilir.

## Release Hot Fix Feast 27 Kasım 2024

### DocBits İyileştirmeleri:

#### Geliştirilmiş PO Optimizasyonu

* **Optimize Edilmiş Kaydetme Mekanizması**: Kaydetme süreci yalnızca kullanıcı eşleştirmeyi tamamladıktan sonra gerçekleşecek şekilde basitleştirildi, böylece gereksiz kaydetmeler azaltıldı ve verimlilik artırıldı.
* **Geliştirilmiş Asenkron Dışa Aktarma**: Dışa aktarma işlevi artık asenkron olarak çalışıyor, böylece daha sorunsuz işlemler ve gelişmiş bir genel kullanıcı deneyimi sağlanıyor.

#### Workflow İyileştirmeleri

Workflow işlevselliği daha iyi bir kullanıcı deneyimi sağlamak için yükseltildi:

* **Geliştirilmiş Günlükler**: Workflow günlükleri artık daha temiz, daha sezgisel bir arayüze sahip, bu da süreç ayrıntılarını incelemeyi ve anlamayı kolaylaştırıyor.
* **Geliştirilmiş Yanıt Verme**: Workflow yürütme süreçleri daha hızlı ve daha güvenilir performans için optimize edildi, böylece daha hızlı görev tamamlama ve azaltılmış gecikmeler sağlandı.

#### Geliştirilmiş Uygulama Önbelleğe Alma

Veri alımını optimize etmek ve yükleme sürelerini azaltmak için uygulama genelinde gelişmiş önbelleğe alma stratejileri uyguladık. Bu iyileştirmeler, özellikle sık erişilen özellikler için daha sorunsuz gezinme ve daha duyarlı bir kullanıcı deneyimi sağlayarak genel kullanılabilirliği artırır.

#### Pano ve Arayüz Yükseltmeleri

* **Pano İyileştirmeleri**: Pano, gezinmeyi basitleştirmek ve temel metriklerin görünürlüğünü artırmak için geliştirilmiş bir düzen ve ek özelliklerle yenilendi.
* **Arayüz İyileştirmeleri**: Uygulama genelindeki kullanıcı arayüzü, kullanıcıların görevlerini minimum çabayla gerçekleştirmesini kolaylaştıran daha modern, sezgisel ve kullanıcı dostu bir deneyim için iyileştirildi.

### Hata Düzeltmeleri:

1. Çıkarma sonrası daha doğru ve güvenilir veri doldurma sağlamak için bulanık mantık geliştirildi.
2. Gruplar ve izinleri etkileyen bilinen hatalar düzeltildi, böylece sorunsuz erişim yönetimi ve rol işlevselliği sağlandı.
3. Uygulama genelindeki çeviri tutarsızlıkları giderildi, netlik ve yerelleştirme iyileştirildi.
4. Düzenle ilgili sorunlar çözüldü, tüm yapılandırmalarda tutarlı ve optimize edilmiş bir kullanıcı arayüzü sağlandı.
5. Ana veri arama işlevselliğindeki hatalar düzeltildi, doğru ve güvenilir veri alımı sağlandı.
6. Mevcut tüm seçenekler arasında e-posta içe aktarma işlevselliğiyle ilgili sorunlar çözüldü, sorunsuz ve hatasız işlemler sağlandı.

## Release Feast 4 Kasım 2024

### Yeni Özellikler:

#### E-posta İçe Aktarma İyileştirmeleri

İçe aktarma sonuçları için otomatik olarak bildirim göndermek üzere IMAP e-posta ayarları yapılandırıldı. Başarılı içe aktarma bildirimleri işlenen dosyaları onaylayacak, başarısızlık uyarıları ise hızlı sorun giderme için dosya adlarını ve belirli hata ayrıntılarını içerecektir.

<figure><img src="../../.gitbook/assets/EmailImport.png" alt=""><figcaption><p>E-posta İçe Aktarma Yapılandırmaları</p></figcaption></figure>

#### Ana Veri Arama Yenilenmesi

Ana veri arama ayarları, çeşitli ana veri türlerinin daha hızlı ve daha kesin alınmasını sağlayan iyileştirilmiş kategorizasyonla yenilendi. Bu iyileştirme, ana verileri farklı kategorilere düzenleyerek veri erişimini basitleştirir ve arama verimliliğini ve doğruluğunu önemli ölçüde artırır. Kullanıcılar artık ilgili verileri daha hızlı bulabilir, böylece uygulama genelinde üretkenlik ve karar verme geliştirilir

<figure><img src="../../.gitbook/assets/MasterDataLookup.png" alt=""><figcaption><p>Ana Veri</p></figcaption></figure>

#### Performans İyileştirmeleri

Özellikle yüksek istek yükleri altında uygulama performansını önemli ölçüde artırmak için sağlam bir önbelleğe alma mekanizması uygulandı. Bu iyileştirme, sık erişilen verileri geçici olarak depolayarak sunucu işleme süresini azaltır, böylece daha hızlı yanıt süreleri ve daha sorunsuz bir kullanıcı deneyimi sağlar. Yeni önbelleğe alma sistemi, artan trafiği verimli bir şekilde yönetir ve yoğun kullanım dönemlerinde bile güvenilir ve ölçeklenebilir performans sağlar

#### Belge Kilitleme Özelliği İyileştirmesi

Eşzamanlı düzenlemeleri önlemek için belge kilitleme işlevselliği yükseltildi, böylece veri bütünlüğü sağlandı ve çakışmalar en aza indirildi. Artık belgeler aktif düzenleme sırasında otomatik olarak kilitlenir ve kullanıcılara bir belgenin kullanımda olduğuna dair net göstergeler sağlar ve düzenleme oturumu tamamlanana kadar başkalarının değişiklik yapmasını önler. Bu iyileştirme işbirlikçi iş akışlarını basitleştirir ve veri üzerine yazma riskini azaltır.

#### Gezinme ve Kullanıcı Deneyimi İyileştirmeleri

* **Ekmek Kırıntısı Gezinme**: Gezinmeyi geliştirmek için uygulama sayfalarında ekmek kırıntısı izleri eklendi, böylece kullanıcıların daha sezgisel bir tarama deneyimi için önceki bölümleri kolayca takip etmesi ve bunlara geri dönmesi sağlandı.
* **Basitleştirilmiş Kullanıcı Arayüzü**: Daha sorunsuz, kesintisiz bir iş akışı oluşturmak için "yeni sürüm" açılır bildirimi kaldırıldı, böylece dikkat dağıtıcı unsurlar azaltıldı ve genel kullanılabilirlik iyileştirildi.

### Hata Düzeltmeleri:

* Şifreli veya imzalı e-postalardan ek hataları gibi kullanıcıya özgü sorunlar çözüldü.
* Kart görüntüleme ve akış sorunları düzeltildi.
* Sonraki/Önceki düğmeleriyle ilgili yönlendirme sorunları düzeltildi.
* Karar ağacı tablolarıyla ilgili hatalar giderildi.
* Kullanılabilirliği artırmak için parola alanı arayüzü güncellendi.
* Görev sayacının doğru görüntülenmemesiyle ilgili sorunlar düzeltildi.
* AI tablosuyla ilgili bir kullanıcı arayüzü sorunu düzeltildi.
* Tablo eğitimi sırasında belge çıkarmayla ilgili hatalar çözüldü.
* Yeniden biçimlendirme sırasında bir PO eşleştirildiğinde bir uyarı eklendi ve eşleştirilen satırların kaldırılması sağlandı.
* Tarih biçimlendirme düzeltildi, verilerin gün ve hafta filtrelerine göre doğru yüklenmesi sağlandı ve belge türlerinin düzgün görüntülenmesi sağlandı.
* Belgelerin çift monitörde görüntülenmesi düzeltildi.
* Bir PO satırının bağlantısının kaldırılmasının tüm satırları kaldırdığı bir sorun düzeltildi.
* Uygulama genelindeki yanlış çeviriler çözüldü.
* Kural yönetimindeki uzun açıklamaların listede kaydırmaya neden olduğu sorun düzeltildi.
* Yönetici olmayan kullanıcılar için eksik "Ata" işlevselliği geri yüklendi.

## Release Harvest 9 Eylül 2024

#### Yeni Özellikler

### Yinelenen Fatura İşleme

Bu özellik, kullanıcıların belgelerin sistemleri genelinde yinelenip yinelenmediğini belirlemesine olanak tanır. Bu özellik, kullanıcı tarafından yapılandırılabilen belge alanlarını analiz ederek çalışır. Belirli alanları seçerek, kullanıcılar tespit kriterlerini ihtiyaçlarına uyacak şekilde özelleştirebilir ve yalnızca ilgili yinelenenlerin işaretlenmesini sağlayabilir. Bu, veri bütünlüğünü korumaya yardımcı olur ve gereksiz belgelerin karmaşasını azaltır, böylece belge yönetim süreçleri basitleştirilir.

{% embed url="https://youtu.be/8CdBu7HN47I" %}

### Karar Ağacı

Karar ağacı, seçenekleri ve sonuçlarını haritalayarak bir workflow'da karar vermeyi otomatikleştirmek için kullanılan bir araçtır. Karar ağaçlarını entegre ederek, belirli kriterlere dayalı tutarlı kararlar sağlayabilir, süreçleri basitleştirebilir ve hataları azaltabilirsiniz. Bu yaklaşım, workflow içindeki karmaşık karar noktalarını otomatikleştirerek verimliliği artırır.

{% embed url="https://youtu.be/E7cx8BDGTI0" %}

### AI Modelleri Seçme

DocBits artık kullanıcıların ihtiyaçlarına daha iyi uyacak şekilde farklı AI modelleri arasında geçiş yapmasına olanak tanıyor. Belge analizi, veri çıkarma veya metin sınıflandırma için olsun, özel kullanım durumunuza en uygun AI modelini seçebilirsiniz. Bu esneklik, performansı optimize etmenize ve daha doğru sonuçlar elde etmenize olanak tanır, böylece AI'nin yeteneklerini kuruluşunuzun benzersiz gereksinimlerine göre uyarlar.

{% embed url="https://youtu.be/YvgEVagPepY" %}

### OCR Sürümü Seçme

DocBits artık platform içinde kullanılan OCR (Optik Karakter Tanıma) sürümünü değiştirme yeteneği sunuyor. Kullanıcılar özel ihtiyaçlarına göre farklı OCR sürümleri seçebilir, böylece çeşitli belge türleriyle daha iyi doğruluk ve uyumluluk sağlanır. Bu özellik, görsellerden ve taranmış belgelerden daha hassas metin çıkarmaya olanak tanır, böylece genel veri kalitesi ve iş akışı verimliliği iyileştirilir.

{% embed url="https://youtu.be/zkW8zj0H5Ko" %}

## Release Sunset 12 Ağustos 2024

### Yeni Özellikler:

## Kural Yöneticisi

[rule-manager](../../administration-and-setup/settings/document-processing/rule-manager/ "mention"), DocBits faturalama sistemi için özel olarak hazırlanmış çakışma çözümü kuralları oluşturma ve düzenleme esnekliği sağlar. Bu kurallar, fatura ayrıntıları ile satın alma siparişi (PO) verileri arasındaki tutarsızlıkları otomatik olarak ele almak için tasarlanmıştır ve doğru finansal mutabakat sağlar. Sistem, bu kuralları fatura satırlarını, masrafları ve vergileri işlemek için uygular ve gerektiğinde uygun ayarlamalar veya notlar oluşturur.

<figure><img src="../../.gitbook/assets/RuleManager.png" alt=""><figcaption><p>Kural Yöneticisi</p></figcaption></figure>

### Stream Kullanarak Veri Senkronizasyonu

Infor'dan BOD senkronizasyonu, gerçek zamanlı veri işleme için AWS Stream kullanır, böylece verimliliği artırır ve veri senkronizasyon süresini önemli ölçüde azaltır.

### XRechnung

DocBits artık XRechnung'u (elektronik faturalar) önce kullanıcı dostu bir PDF oluşturarak sorunsuz bir şekilde işliyor, böylece fatura işleme iş akışını basitleştiriyor ve kolaylaştırıyor.

<figure><img src="../../.gitbook/assets/XRECHNUNG.png" alt=""><figcaption></figcaption></figure>

### Hata Düzeltmeleri:

1. PO Eşleştir Düğmesi Görünürlüğü\
   Sorun: Tablo olmadığında veya tablo silindiğinde PO Eşleştir düğmesi kullanılabilir.\
   Durum: Alan doğrulamasında, tablo yoksa veya tablo silinmişse PO Eşleştir gizlenecek
2. Tablo Sürükle ve Bırak Sıralaması\
   Sorun: Tüm Listelerde/Panolarda sıralama için Tablo Sürükle ve Bırak\
   Çözüm: Kullanıcı artık tabloyu sıralamak için sürükleyip bırakabilir
3. Doğrulama Ekranı Araç Çubuğu\
   Sorun: Doğrulama ekranı: araç çubuğu sağ tarafı kaydırılamıyor\
   Çözüm: Düzeltildi
4. Yatay Kaydırma\
   Sorun: Onay Ekranında Yatay Kaydırma\
   Çözüm: Düzeltildi
5. Onay Ekranı Karar Temizleme\
   Sorun: Onay ekranında onayla/reddet kararını temizleme yeteneği\
   Çözüm: Düzeltildi
6. Onay Ekranında Görev Görüntüleme\
   Sorun: Onay Ekranında gösterilen Görev\
   Çözüm: Açık/devam eden görevlerin sayısını gösteren araç çubuğu mevcut
7. PO Eşleştir Tablo Boyutu\
   Sorun: PO Eşleştir tablosu bir satır eşleştirildikten sonra küçülüyor\
   Çözüm: Düzeltildi
8. Ürün Satın Alma Grubuna Dayalı Görev Ataması\
   Sorun: Satın alma grubu ataması için çeviri\
   Çözüm: Düzeltildi
9. Görev Oluşturmada Tedarikçi Adı ve Kimliği\
   Sorun: Görev oluşturmada Tedarikçi Adı ve Kimliği ekleme\
   Çözüm: Tedarikçi Adı ve Kimliği belgeden alınacak
10. Belge Alt Türü Kopyalama\
    Sorun: Alt belge türü ayarından Belge Alt Türünü Kopyala'ya tıklama çalışmıyordu\
    Çözüm: Düzeltildi
11. Yeni Etiket Alanı\
    Sorun: Değer ve eş anlamlıyla birlikte etiket eklemek için değer listesinde Yeni Etiket alanı\
    Çözüm: Düzeltildi
12. Workflow'da Menşe Ülke Kartı\
    Sorun: Bir tedarikçinin menşe ülkesini kontrol eden ve buna göre bir görev oluşturan veya belge işlemeye devam eden workflow'da Yeni Kart\
    Çözüm: Düzeltildi
13. Ayarlar arama çubuğunda Karanlık Mod Düzeltmesi\
    Sorun: Bu sorun daha önce tespit edilmişti\
    Çözüm: Düzeltildi
14. Çıkarılan Tablo Sütun Görünürlüğü Göstergesi\
    Sorun: Alan doğrulamasında çıkarılan tabloda Sütunların gizli olup olmadığına dair gösterge\
    Çözüm: Düzeltildi
15. Yöneticiler için Pano Ataması\
    Sorun: Panodaki Ata'yı yalnızca yöneticiler için yapma\
    Çözüm: Düzeltildi
16. Belge Bölme Görünürlüğü\
    Sorun: Belge bölmeyi yalnızca daha fazla sayfa olduğunda göster\
    Çözüm: Düzeltildi
17. Fatura Panosu Sütunları\
    Sorun: Fatura panosunda ek sütunlar\
    Çözüm: Düzeltildi
18. Alan Doğrulama Script Devre Dışı Bırakma\
    Sorun: Alan Doğrulama- Scripti devre dışı bırakma doğru çalışmıyordu\
    Çözüm: Düzeltildi
19. Onay Layout Düğmesi Özelleştirmesi\
    Sorun: Onay layout builder'da düğme türü ve stili değiştirilemiyor\
    Çözüm: Düzeltildi
20. Veri Senkronizasyon Tablosu\
    Sorun: Ayarlarda Veri Senkronizasyon Tablosu\
    Çözüm: Düzeltildi
21. Pano Analizi Toplam Görüntüleme\
    Sorun: Pano Analizi- yanlış toplam sayı görüntüleme\
    Çözüm: Düzeltildi

## Release Firework Juli 8th, 2024

### Yeni Özellikler

**Satır Masraflarının M3'e Dışa Aktarılması**

• Satır masraflarını iş ihtiyaçlarınıza uygun maliyet öğeleriyle M3'e dışa aktarın.

**PO ve Fatura Tutarsızlık İşleme**

• Miktar, fiyat, masraf ve vergideki tutarsızlıkların akıllı işlenmesi.

### Temel Hata Çözümleri

#### 1. PO Arama İşlevselliği

• Sorun: PO araması çalışmıyordu.

• Durum: Bu sorun tespit edildi ve bu sürümde ele alınmayacak.

#### 2. PO Eşleştirme Bağlantısı

• Sorun: PO eşleştirme bağlantısı beklendiği gibi kaldırılmıyordu.

• Çözüm: Sorunsuz PO eşleştirme işlemlerini sağlamak için düzeltildi.

#### 3. Dışa Aktarılan Belge Uyarıları

• Sorun: Dışa aktarılan belgeler, sistem bunun için kurulmamış olsa bile maliyet öğeleri için uyarılara sahipti.

• Çözüm: Gereksiz uyarıları önlemek için düzeltildi, böylece doğru belge dışa aktarımı sağlandı.

#### 4. İhbarlı Sevkiyat EDI Görünümü

• Sorun: İhbarlı sevkiyat EDI görünümü başlıkta kimlikleri gösteriyordu.

• Çözüm: Başlıklar artık doğru şekilde görüntüleniyor, böylece veri okunabilirliği iyileştirildi.

#### 5. Toplama Göre Bölmede Hesaplama Hataları Sorunu

• Sorun: Satırlar daha fazla bölündüğünde hesaplama hataları oluştu.

• Çözüm: Tüm senaryolarda doğru hesaplamaları sağlamak için düzeltildi.

#### 6. PO Ekranı Tablo Görüntüleme

• Sorun: PO ekranında tablo görünmüyordu.

• Çözüm: Tabloların doğru görünmesini sağlamak için görüntüleme sorunu çözüldü.

#### 7. Sipariş Onayında Otomatik Dışa Aktarma

• Sorun: Otomatik dışa aktarma çalışmıyordu.

• Çözüm: Otomatik dışa aktarmaların sorunsuz çalışmasını sağlamak için işlevsellik geri yüklendi.

#### 8. PO'da Uyumsuzluk Sorunu

• Sorun: Teslimat Notunda her şey aynı olmasına rağmen PO'da uyumsuzluk sorunu gösteriliyordu.

• Çözüm: Doğru uyumsuzluk tespitini sağlamak için çözüldü.

#### 9. Rapor İndirme Sorunları

• Sorun: Raporlar indirilmiyordu.

• Çözüm: Sorunsuz rapor indirmelerini sağlamak için düzeltildi.

#### 10. Yanlış Toplam ve Net Tutarlar

• Sorun: Toplam ve Net tutarlar yanlış değerler gösteriyordu.

• Çözüm: Finansal doğruluğu sağlamak için değerler düzeltildi.

#### 11. Panoda Fatura Tarihi Formatı

• Sorun: Fatura Tarihi sütununun yanlış format değerleri vardı.

• Çözüm: Tarihler artık doğru formatta görüntüleniyor, böylece kullanılabilirlik artırıldı.

#### 12. "Doğrulamaya Hazır"da Workflow Gecikmeleri

• Sorun: Doc2flow'dan geri bildirim gelene kadar "Doğrulamaya Hazır"da workflow gecikmeleri oluşuyordu.

• Çözüm: Daha hızlı doğrulama süreçleri için workflow zamanlaması iyileştirildi.

## Next Release Firework Juli 8th, 2024

### Sorun:

Mevcut sistem, fatura masraflarını satın alma siparişlerine (PO'lar) karşı doğru bir şekilde eşleştirmek ve işlemek için otomatik kurallardan yoksundur. Bu manuel süreç, ekran görüntülerinde gösterildiği gibi, fatura masrafları ve PO'ların doğru faturalama için mutabakat gerektirdiği tutarsızlıklara yol açabilir.

<div><figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.37.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-06-07 um 17.11.46.png" alt=""><figcaption><p>Rule Manager DocBits</p></figcaption></figure></div>

### Çözüm:

Temmuz'da piyasaya sürülecek DocBits'teki yeni Kural Yöneticisi ile bu süreci otomatikleştirebilirsiniz:

#### 1. Kurallar Oluşturun:

Fatura satır öğeleri için kriterleri (ör. Miktar > PO Miktarı) tanımlayın.

#### 2. Eylemleri Ayarlayın:

Verileri sorunsuz bir şekilde Infor'a dışa aktarmak için alanları ve eylemleri eşleyin.

#### 3. Kuralları Test Edin:

Doğruluğu sağlamak için kuralları örnek verilerle doğrulayın.

## Junebug Release Notes - June 10th, 2024

Bu güncelleme, Junebug'a heyecan verici yeni özellikler ve hata düzeltmeleri getiriyor:

**Yeni Özellikler:**

* **Otomatik Masraf Çıkarma:** Junebug artık Docbit belgeleriniz içindeki masrafları otomatik olarak çıkarır ve eşler. Bu, manuel veri girişini ortadan kaldırır ve iş akışınızı basitleştirir.
* **Infor IDM'ye Portal Dışa Aktarımı:** Yeni Portal, tedarikçi belgelerini doğrudan Infor IDM'ye zahmetsizce dışa aktarmanıza olanak tanır. Bu, sevkiyat işlemesini basitleştirir ve manuel müdahaleyi azaltır.
* **Menşe Tanımlama (AI):** Junebug, belgelerin menşeini otomatik olarak öğrenen güçlü bir AI özelliği sunar. Bu, belge sınıflandırmasında zaman ve emekten tasarruf sağlar.
*

```
<div><figure><img src="../../.gitbook/assets/POShipmentTable.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/ApprovalScreen2.png" alt=""><figcaption></figcaption></figure> <figure><img src="../../.gitbook/assets/ApprovalScreen1.png" alt=""><figcaption></figcaption></figure></div>
```

**Hata Düzeltmeleri:**

* **QR Kod Düzeltmesi:** Daha önce QR kod işlemesiyle ilgili sorunlara neden olan bir sorun çözüldü.
* **EDI Olmayan Belge İşleme:** Junebug artık EDI olmayan belgeleri daha etkili bir şekilde işliyor.

<figure><img src="../../.gitbook/assets/EDI810-Invoice.png" alt=""><figcaption></figcaption></figure>

Hotfix - 5 Juni [**Öncelik Sistemi**](../../end-user-and-partner-section/end-user-section/our-document-priority-system.md)

## Next Release - Junebug Release 10th June 2024

Sandbox Freeze - 3th June 2024

<figure><img src="../../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.37.35.png" alt=""><figcaption></figcaption></figure>

Yaklaşan sürümde, özellikle belgeler içindeki tablo satırlarını hedefleyen sınıflandırma ve çıkarma yeteneklerinde önemli bir iyileştirme tanıtılacaktır. Bu yeni özellik, kullanıcıların bir tablodaki bir satırın bir masrafı temsil edip etmediğini tanımlamasına olanak tanır. Bu işlevsellik, doğru işleme ve kayıt tutma için farklı işlem türleri arasında — masraflar, vergiler veya ücretler gibi — ayrım yapmanın çok önemli olduğu faturalar gibi ayrıntılı finansal belgelerde özellikle yararlıdır.

**Sürüm Notları için Temel Noktalar:**

* **Geliştirilmiş Tablo Satırı Sınıflandırması**: Kullanıcılar artık bir belge tablosundaki belirli bir satırın bir masraf olup olmadığını belirtebilir, böylece veri çıkarmanın doğruluğu ve ayrıntı düzeyi artırılır.

## Maypole Release 5.55.8.10 - ( 17th May )

### Release Notes - Web App

#### Yeni Özellikler:

▪ Workflow Kartı Çevirisi: Daha iyi yerelleştirme desteği için kart çevirisi dahil olmak üzere workflow'da iyileştirmeler.

▪ E-posta İçe Aktarma Günlüğü: Sorun giderme ve izlemeyi geliştirmek için e-posta içe aktarmaları için ayrıntılı günlükleme eklendi.

▪ Bozuk Bulanık Ekran Düzeltmesi: Çeşitli arayüzlerde bozuk bulanık ekran görüntülemesiyle ilgili bir sorun çözüldü.

▪ Muhasebe Güncellemeleri: Güncel olmayan muhasebe yöntemlerini kaldırarak ve masrafları daha verimli bir şekilde entegre ederek muhasebe süreci geliştirildi.

#### İyileştirmeler:

▪ Ruiz Workflow İyileştirmeleri: Özellikle gizli adımları içeren workflow gezinmesiyle ilgili hatalar düzeltildi.

▪ Kullanıcı Arayüzü Ayarlamaları: Daha iyi netlik ve kullanıcı deneyimi için ödeme koşulları altındaki nakit iskonto koşulları gibi kullanıcı arayüzü öğeleri iyileştirildi.

▪ Performans İyileştirmeleri: Sistem performansını ve kararlılığını artırmak için çeşitli arka uç iyileştirmeleri.

#### Hata Düzeltmeleri:

▪ Onay Damgası Sorunu: Uyumluluğu ve doğru işlevselliği sağlamak için onay damgası sürecini çevreleyen kritik sorunlar düzeltildi.

▪ Anahtar Ekleme: Veri bütünlüğünü ve sistem işlevselliğini sağlamak için gerekli anahtarlar sisteme geri eklendi.

▪ Ana Veri Alanı Ayarlaması: Kullanıcı gereksinimleriyle uyum sağlamak için ana veri alanındaki bir sorun ele alındı.

#### Teknik:

▪ Sürüm Güncellemeleri: Mevcut standartlar ve teknolojilerle uyum sağlamak için çeşitli sistem bileşenlerine rutin güncellemeler.

▪ Birleştirme Etkinlikleri: Birden çok geliştirme dalından özellikleri, düzeltmeleri ve iyileştirmeleri ana dala entegre etmek için çok sayıda birleştirme.

### What's New - API

▪ Önbellek Yönetimi İyileştirmeleri: Performansı ve güvenilirliği artırmak için get\_receive\_delivery\_cache güncellendi.

▪ Satış Siparişleri için Yeni Özellikler: Sipariş verilerinin görselleştirilmesini ve yönetimini geliştiren, satış siparişleri için bir önizleme özelliği tanıtıldı.

▪ Belge İşleme İyileştirmeleri: Sağlamlığı sağlamak için demotesting ve sandbox ortamları için otomatik test işleri eklendi.

▪ Geliştirilmiş Önbellek İşlevselliği: Önbelleğe alma mekanizmalarını daha da geliştirmek için field\_id eklendi.

#### Düzeltmeler ve İyileştirmeler

▪ Office E-posta İçe Aktarma Ayarlamaları: İşlevselliği geliştirmek için Office E-posta İçe Aktarma özelliğinde gerekli ayarlamalar yapıldı.

▪ Geliştirme İyileştirmeleri: Ortamlar arasında senkronizasyon ve kararlılık sağlamak için dev'den ana dallara birden çok birleştirme.

#### Çeşitli

▪ Yapılandırma Güncellemeleri: Sistem kurulumunu ve parametrelerini iyileştiren yapılandırma dosyalarına çeşitli güncellemeler.

### Release Notes - Workflow

#### İyileştirmeler:

▪ Artık içe aktarma sırasında etkinleştirilebilen yeni bir workflow testi uygulandı ve daha esnek test senaryolarına olanak tanındı.

▪ Hata ayıklama ve izlemeyi daha verimli hale getirerek eylem kartları için günlükleme işlevselliği geliştirildi.

▪ Alan karşılaştırma kartları için tarih ve enum türleriyle uyumluluk iyileştirildi, böylece daha sorunsuz karşılaştırmalar ve doğrulamalar sağlandı.

▪ Vergi kartı güncellendi ve işlemleri basitleştirmek için eylem kartları için iade süreçleri değiştirildi.

#### Düzeltmeler:

▪ Belge durumu güncellemeleriyle ilgili sorunlar ele alındı, böylece sistemde doğru şekilde yansıtılmaları sağlandı.

▪ Tutarsızlıkları doğru şekilde işlemek için birim fiyat ve miktarı içeren karşılaştırma kartının hesaplaması düzeltildi.

▪ Birden çok küçük hata çözüldü ve kararlılık iyileştirmeleri yapıldı.

#### Operasyonel Değişiklikler:

▪ Birden çok geliştirme aşaması sandbox ve stage dallarına birleştirildi, bu da yeni özelliklerin ve düzeltmelerin önemli bir entegrasyonunu yansıtıyor.

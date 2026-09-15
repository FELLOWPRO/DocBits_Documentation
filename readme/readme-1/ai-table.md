# Yapay Zeka Tablosu

Yapay Zeka Çıkarılan Tablo, bir tedarikçinin eğitilmiş tablo kuralları olmadığında DocBits'in yapay zeka ile okuduğu satır kalemi tablosudur. Doğrulama ekranında başlık alanlarının altında görünür. Bu sayfa, tabloyu ne zaman aldığınızı, nasıl yeniden çalıştıracağınızı ve çıkardığı veriyi nasıl şekillendireceğinizi açıklar.

## Yapay zeka tablosunu ne zaman alırsınız

* Bir yönetici **Yapay Zeka Tablo Çıkarma**'yı açmıştır (Ayarlar → Belge İşleme → Sınıflandırma ve Çıkarma). Kapalıysa tablo alanında *AI Table will display here. Enable in …* mesajı görünür.
* Tedarikçinin **kaydedilmiş kuralı yoktur**. Biri tedarikçinin tablosunu eğitip *Kuralları Kaydet*'e tıkladığı anda kaydedilen kurallar o tedarikçi için yapay zeka tablosunun yerini alır; satırlar artık *Yapay Zeka Çıkarılan Tablo* sekmesi yerine *Çıkarılan tablo* sekmesinde görünür.
* İstisna: tablo sütunu ayarlarında **Yapay Zeka Kullan** olarak işaretlenen sütunlar, kaydedilmiş kuralları olan tedarikçiler için bile yapay zeka tarafından doldurulur, bkz. aşağıdaki **Sütun başına yapay zeka kullanımı** bölümü.

Tabloyu hangi yapay zeka katmanının okuyacağı (Fast, Full, Nexus) kuruluş başına ayarlanır ve doğrulama ekranındaki *Daha fazla ayar* altında tedarikçi başına geçersiz kılınabilir.

## Yapay zeka tablosunu yeniden çıkarma

Satırlar eksik olduğunda veya bir sütun kaymış olduğunda ve yapay zekanın yeniden denemesini istediğinizde, örneğin bir etiket ekledikten sonra bunu kullanın:

1. Tablonun altındaki alana etiket ekleyin veya etiketleri değiştirin ve **Uygula**'ya tıklayın. Yapay zeka, etiketleriniz ve sütun değişikliklerinizle tabloyu bu belge için yeniden oluşturur; tedarikçi için henüz hiçbir şey saklanmaz. Belgede PO ile eşleşmiş satırlar varsa DocBits, yeniden oluşturmanın eşleşmeleri kaldıracağı konusunda uyarır.
2. Sonuçtan memnun musunuz? Bu tedarikçinin bir sonraki belgesinin aynı şekilde çıkarılması için **Kaydet**'e (*Kuralları Kaydet*) tıklayın.
3. Baştan başlamak için **Sil**'e (*Kuralları Sil*) tıklayın: DocBits *Rules has been deleted successfully* mesajıyla onaylar ve yapay zeka çıkarmasını kaydedilmiş etiket veya biçimlendirme olmadan yeniden çalıştırır.

*Kuralları Sil*, bu tedarikçi için kaydedilen etiketleri ve biçimlendirme kurallarını kaldırır, tablo sütunu yapılandırmasını değil. Bir yönetici ayarları veya sütunları değiştirdikten sonra belgenin tamamını (başlık ve tablo) yeniden çıkarmak için bunun yerine panodaki belge menüsünde *Yeniden Başlat*'ı kullanın.

## Sütun başına yapay zeka kullanımı

Her tablo sütununun bir **Yapay Zeka Kullan** işareti vardır (Ayarlar → Genel Ayarlar → Belge Türleri → [Tablo Sütunları](../admin-section/settings/global-settings/document-types/table-columns.md)). İşaret açıkken, tedarikçinin kaydedilmiş kuralları olsa bile o sütunu yapay zeka doldurur; diğer sütunlar kurallardan gelmeye devam eder. Tipik kullanım: eğitilmiş kuralların kötü yakaladığı bir serbest metin açıklama sütunu veya sayfada yer değiştiren bir değer.

Yapay zekanın o sütunu satırın tamamından tahmin ettiğini unutmayın. Oraya sürekli yanlış değeri koyuyorsa (örneğin satır toplamını *Masraflar* sütununa) satır toplamı kontrolü her satırda başarısız olur. Bu durumda o sütun için *Yapay Zeka Kullan*'ı kapatın veya yapay zekaya sütunun ne olduğunu söyleyen bir etiket ekleyin.

## Yapılandırılmış çıkarma

Kuruluş ayarlarında **Yapılandırılmış Çıkarma Kullan (Yapay Zeka)** etkinken yapay zeka, tedarikçinin sütun başlıklarını kopyalamak yerine tabloyu, yapılandırılmış tablo sütunlarına doğrudan eşlenen sabit bir yapıda döndürür. Sütun adları böylece her zaman yapılandırmanızla eşleşir; tedarikçinin yazdırdığı ancak sizin yapılandırmadığınız bir sütun çıkarılmaz. Tedarikçi başlıkları çok değişkenlik gösterdiğinde ve yeniden eşlemeye zaman harcadığınızda yöneticinizden bunu açmasını isteyin.

## Çıkarılan tabloyla çalışma

İşte temel yetenekler ve kullanım talimatları:

* **Sütunları Silme**: Çıkarılan tablodaki belirli sütunlar gerekli değilse, kullanıcılar sütun başlığının yanındaki "Sütunu Sil" simgesine (üç dikey nokta ile temsil edilir) tıklayarak bunları kolayca kaldırabilir. Bu, tabloyu sadeleştirir ve yalnızca ilgili bilgilere odaklanmayı sağlar.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.48.56 (1).png" alt=""><figcaption></figcaption></figure>

* **Para Birimi Formatını Değiştirme**: Para birimi formatı, "Para Birimi" alanının yanındaki açılır menüden istenen formata seçilerek değiştirilebilir. Bu, para birimi değerlerinin tercih edilen formatta görüntülenmesini sağlayarak finansal verileri yorumlamayı ve analiz etmeyi kolaylaştırır.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.49.15 (2).png" alt=""><figcaption></figcaption></figure>

* **Eşlenmemiş Sütunları Gösterme/Gizleme**: Varsayılan olarak, tabloda yalnızca eşlenmiş sütunlar (çıkarılan veri içeren sütunlar) görünür. Ancak, kullanıcılar tablonun altındaki "Eşlenmemiş sütunları gizle" veya "Eşlenmemiş sütunları göster" düğmesine tıklayarak eşlenmemiş sütunları göstermeyi veya gizlemeyi seçebilir. Bu özellik, kullanıcılar veriler şu anda veri içermese bile tüm mevcut sütunları incelemek istediklerinde faydalıdır.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.49.26 (2).png" alt=""><figcaption></figcaption></figure>

* **Tablo Başlıklarını Değiştirme**: Tablo başlıkları (sütun adları), başlığa tıklayarak ve istenen adı girdiğinizde değiştirilebilir. Bu özellik, kullanıcıların sütun adlarını kendi terimleri veya tercihleriyle daha iyi uyumlu hale getirmelerine olanak tanır, verileri daha okunabilir ve anlaşılır hale getirir.

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-08 um 20.48.43.png" alt=""><figcaption></figcaption></figure>

* **Değişikliklerinizi kaydetme**: Etiketlerin yanındaki **Kaydet** (ipucu *Kuralları Kaydet*), mevcut sütun eşlemesini, gizli sütunları ve etiketleri bu tedarikçi için saklar. Tedarikçinin bir sonraki belgesi bunlarla çıkarılır.

Bu özellikler size çıkarılan veriler üzerinde kontrol sağlar. Aynı tedarikçi her seferinde aynı düzeltmelere ihtiyaç duyuyorsa, bunun yerine tabloyu bir kez eğitin, bkz. [Eğitim Satır Alanları / Tablo Eğitimi](../admin-section/setup/document-training/training-line-fields-table-training/README.md); yapay zeka tablosu o tedarikçi için artık kullanılmaz.

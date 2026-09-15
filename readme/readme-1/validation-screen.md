# Doğrulama Ekranı

## Genel Bakış

<div data-full-width="false">

<figure><img src="../.gitbook/assets/docbits_validation_screen_overview_nl.png" alt="Docbits Validation Screen Overview Nl"><figcaption></figcaption></figure>

</div>

### Belge Kökeni (Document Origin)

{% embed url="https://youtu.be/-m45XGiIeig" %}
DocBits Origin Setting Explained: Country Standards for Dates & Number Formats
{% endembed %}

## **Kaydet Düğmesi:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 08.40.49 (2).png" alt=""><figcaption></figcaption></figure>

* **Kaydet Düğmesi:**
* **Amaç:** Üzerinde çalışılan belgenin veya betiğin mevcut durumunu kaydeder.
* **Kullanım Senaryosu:** Bir belgeye değişiklikler veya notlar ekledikten sonra, tüm değişikliklerin kaydedildiğinden emin olmak için bu düğmeyi kullanın.

### **Özel Kurallar Ekle:**

<figure><img src="../.gitbook/assets/docbits_add_special_rules.png" alt="Docbits Add Special Rules"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/docbits_add_script_rule.png" alt="Docbits Add Script Rule"><figcaption></figcaption></figure>

* **Özel Kurallar Ekle / DocBits'te Betik Ekle:**
* **Amaç:** Belgelerin nasıl işlendiğini özelleştiren belirli kuralları veya betikleri uygulamak için kullanıcılara izin verir.
* **Kullanım Senaryosu:** Veri çıkarma veya format doğrulama gibi görevleri otomatikleştirmek için bu özelliği kullanın, iş akışı verimliliğini artırır.

{% hint style="info" %}
Buradan [DocBits'te Betik Ekle](../admin-section/setup/scripting-in-docbits/) bakabilirsiniz.
{% endhint %}

### **Bulanık Alanlar:**

<figure><img src="../.gitbook/assets/docbits_fuzzy_fields_nl.png" alt="Docbits Fuzzy Fields Nl"><figcaption></figcaption></figure>

*   **Bulanık Alanlar:**

* **Amaç:** Verilerin tam olarak eşleşmeyebileceği ancak yeterince yakın olduğu alanları tanımlamada ve düzeltmede yardımcı olur.
* **Kullanım Senaryosu:** Tam eşleşmelerin her zaman mümkün olmadığı veri doğrulama süreçlerinde faydalıdır, örneğin hafif yanlış yazılmış isimler veya adresler.

## Çıkarılan tablo (satır kalemleri)

<figure><img src="../.gitbook/assets/validation_screen_line_items_table.png" alt="Doğrulama ekranında tablo araç çubuğuyla birlikte satır kalemi tablosu"><figcaption><p>Başlık alanlarının altındaki çıkarılan tablo</p></figcaption></figure>

Başlık alanlarının altında DocBits, belgenin satır kalemi tablosunu gösterir: her fatura satırı için bir satır, belge türü için yapılandırılan her [tablo sütunu](../admin-section/settings/global-settings/document-types/table-columns.md) için bir sütun. Bir belge türünün birden fazla tablosu olduğunda (örneğin kalemler ve masraflar), her tablonun ızgaranın üstünde kendi sekmesi bulunur.

### Tablo nereden gelir

Izgaranın üstünde, kuruluşun açtığı her çıkarma yolu için bir sekme bulunur:

| Sekme | Anlamı |
|---|---|
| **Çıkarılan tablo** | Kural tabanlı çıkarma (*Tablo Çıkarma* ayarı). Eğitilmiş tablosu olan bir tedarikçide bu satırlar kaydedilmiş kurallardan gelir ve o tedarikçinin her belgesinde aynı şekilde çıkarılır; eğitilmemiş bir tedarikçide sekme boş olabilir. |
| **Yapay Zeka Çıkarılan Tablo** | Yapay zeka tablo çıkarma (*Yapay Zeka Tablo Çıkarma* ayarı). Tedarikçinin kaydedilmiş kuralı olmadığında ve kurallar olsa bile *Yapay Zeka Kullan* olarak işaretlenen sütunlar için doldurulur. Sekmedeki *AI table not found* ipucu, yapay zekanın bu belge için hiçbir sonuç döndürmediği anlamına gelir. |
| **PO Tabloları** | Yalnızca düzen oluşturucuda: eşleştirme için kullanılan satın alma siparişi satırları. |

Hiçbir sekme görünmüyorsa, kuruluş için her iki tablo ayarı da kapalıdır (Ayarlar → Belge İşleme → Sınıflandırma ve Çıkarma). Tabloyu hangi yapay zeka katmanının okuyacağı kuruluş başına ayarlanır ve doğrulama ekranındaki *Daha fazla ayar* altında tedarikçi başına geçersiz kılınabilir.

### Tabloda çalışma

* **Bir hücreyi düzenleme**: hücreye tıklayın ve yazın. Tutar, sayı ve tarih sütunları siz yazarken doğrulanır.
* **Yeni tablo satırı ekle**: sona boş bir satır ekler. Bir satır tanınmadığında kullanın.
* **Bir satırı silme**: satırın sonundaki çöp kutusu simgesi.
* **Boş eşlenmiş sütunları ekle**: yapay zekanın boş bıraktığı yapılandırılmış sütunları gösterir, böylece elle doldurabilirsiniz.
* **Tablo Sütununu Geri Yükle**: bu belge için görünümden kaldırdığınız bir sütunu geri getirir.
* **Tabloyu sil**: bu belgedeki bu tablonun tüm satırlarını temizler. Yapılandırmaya dokunulmaz.
* **Yeni tablo sütunu ekle** (yöneticiler): belgeden ayrılmadan, tablo sütunu ayarlarındakiyle aynı iletişim kutusu.
* **Etiketler** (yalnızca yapay zeka tablosu): yapay zeka için kısa metin ipuçları, örneğin *"son sütun net tutardır"*. Bkz. [Yapay Zeka Tablosu](ai-table.md).
* Etiketlerin yanındaki **Uygula** / **Kaydet** / **Sil**: *Uygula*, yaptığınız etiket ve sütun değişiklikleriyle yapay zeka tablosunu bu belge için yeniden çalıştırır, hiçbir şey kaydetmez (belgede PO ile eşleşmiş satırlar varsa DocBits eşleşmelerin kaldırılacağı konusunda uyarır); *Kuralları Kaydet*, mevcut sütun eşlemesini ve etiketleri bu tedarikçi için saklar; *Kuralları Sil* bunları kaldırır ve bu belge için yapay zeka çıkarmasını yeniden çalıştırır.
* **Dışa aktar**: tabloyu CSV dosyası olarak indirir.
* **Tablo çıkarma görünümüne git**: bu belge için tablo eğitimini açar. Aynı tedarikçi sürekli yanlış çıkıyorsa kullanın: tabloyu bir kez çizin, sütunları eşleyin ve *Kuralları Kaydet*'e tıklayın; bundan sonra satırlar *Çıkarılan tablo* sekmesinde görünür. Bkz. [Eğitim Satır Alanları / Tablo Eğitimi](../admin-section/setup/document-training/training-line-fields-table-training/README.md).

{% hint style="info" %}
Tablo yapay zeka tarafından çıkarılmışsa ve tablo eğitimini açarsanız DocBits *Table is already extracted by AI. Do you want to train manually?* diye sorar. Kuralları kaydettikten sonra bu tedarikçi için yapay zeka tablosu artık kullanılmaz.
{% endhint %}

### Tabloyu yeniden çıkarma

* **Aynı belge, yapay zeka tablosu:** etiketleri ekleyin veya değiştirin ve **Uygula**'ya tıklayın; yapay zeka tablosu yalnızca bu belge için yeniden oluşturulur. Tedarikçinin kaydedilmiş etiketlerini ve biçimlendirmesini de kaldırmak için **Sil**'e (*Kuralları Sil*) tıklayın: DocBits *Rules has been deleted successfully* mesajıyla onaylar ve yapay zeka çıkarmasını yeniden çalıştırır.
* **Aynı belge, eğitilmiş kurallar:** *Tablo çıkarma görünümüne git*'i açın, tabloyu düzeltin ve *Kaydet ve yeniden çıkar*'a tıklayın.
* **Belgenin tamamı yeniden (başlık ve tablo):** Pano → belge menüsü → *Yeniden Başlat*. Bir yönetici tablo sütunlarını veya çıkarma ayarlarını değiştirdikten sonra gereklidir.

### Onayı ne engeller

Tablo, kaydettiğinizde veya onayladığınızda kontrol edilir. Kırmızı bir hücre veya tablonun altındaki bir mesaj şunlardan birini gösterir:

| Mesaj | Neden | Ne yapmalı |
|---|---|---|
| Zorunlu sütun boş | *Zorunlu* olarak işaretlenen bir sütunun bu satırda değeri yok. | Hücreyi doldurun veya sütunun zorunlu olması gerekip gerekmediğini bir yöneticiye sorun. |
| *Line total does not match quantity x unit price (expected …, got …)* | `miktar × birim fiyat + masraflar − indirim`, satır toplamından 0,02'den fazla farklı. Çoğunlukla dört değerden biri yanlış sütuna okunmuştur. | Belgede yanlış olan değeri düzeltin; *Masraflar* gibi bir sütun sürekli yanlış değerle dolduruluyorsa yöneticinize bildirin (bkz. [Tablo Sütunları: Sorun giderme](../admin-section/settings/global-settings/document-types/table-columns.md)). |
| *Line items add up to … but the net total is …* | Satır toplamlarının toplamı, başlıktaki net tutardan farklı. | Eksik veya yinelenen bir satır ya da yanlış okunmuş bir başlık tutarı olup olmadığını kontrol edin. |
| *Line Item Table is missing Mandatory column for PO* | PO eşleştirme kalem numarası, birim fiyat, miktar ve toplam tutara ihtiyaç duyar; bunlardan biri gizli. | Yönetici: sütunun gizliliğini Tablo Sütunları altında kaldırın. |

Bir yönetici, *Tablo doğrulamasını yok say* ile (Belge Türleri → Daha Fazla Ayarlar) bir belge türü için tüm tablo kontrollerini kapatabilir; satır uyuşmazlıkları ve boş zorunlu sütunlar o zaman bildirilmez.

Kontroller hakkında daha fazla bilgi: [Tablo Sütunları](../admin-section/settings/global-settings/document-types/table-columns.md) sayfasındaki Sorun giderme bölümü.

### **Büyüteç:**

<figure><img src="../.gitbook/assets/docbits_magnifying_glass_tool.png" alt="Docbits Magnifying Glass Tool" width="118"><figcaption></figcaption></figure>

* **Büyüteç (Magnify Glass):**
* **Amaç:** Belgenin seçilen bir alanının yakınlaştırılmış bir görünümünü sağlar.
* **Kullanım Senaryosu:** Belgelerde ince detayları veya küçük metinleri incelemeye yardımcı olur, veri girişinde veya gözden geçirmede doğruluğu sağlar.

<figure><img src="../.gitbook/assets/docbits_open_new_window_usage.png" alt="Docbits Open New Window Usage"><figcaption></figcaption></figure>

### **Yeni pencere aç:**

<figure><img src="../.gitbook/assets/docbits_open_new_window_tool.png" alt="Docbits Open New Window Tool" width="130"><figcaption></figcaption></figure>

* **Yeni Pencere Aç:**
* **Amaç:** Belge karşılaştırması veya çoklu görev yaparken yan yana yeni bir pencere açar.
* **Kullanım Senaryosu:** İki belgeyi karşılaştırırken veya mevcut belgeden ayrılmadan ek bilgilere başvururken faydalıdır.

### **Klavye kısayolları:**

<figure><img src="../.gitbook/assets/docbits_shortcuts_tool.png" alt="Docbits Shortcuts Tool" width="145"><figcaption></figcaption></figure>

1. **Klavye Kısayolları:**
* **Amaç:** Kullanıcıların klavye kısayol kombinasyonlarını kullanarak hızlı bir şekilde işlemler gerçekleştirmesine olanak tanır.
* **Kullanım Senaryosu:** Fare gezinmesine olan bağımlılığı en aza indirerek belge gezinme ve işleme hızını ve verimliliğini artırır.

<figure><img src="../.gitbook/assets/docbits_shortcuts_usage.png" alt="Docbits Shortcuts Usage"><figcaption><p>Klavye </p></figcaption></figure>

### **Görevler:**

<figure><img src="../.gitbook/assets/docbits_tasks_tool.png" alt="Docbits Tasks Tool" width="55"><figcaption></figcaption></figure>

Dahili bilgileri paylaşmak için görevler oluşturabilir ve bunları şirket içinde belirli bir çalışana veya gruba atayabilirsiniz.

* **Görevler:**
* **Amaç:** Belgelerle ilgili görevler oluşturmayı ve bunları takım üyelerine atamayı sağlar.
* **Kullanım Senaryosu:** Takımlar içinde işbirliğini ve görev yönetimini kolaylaştırır, herkesin sorumluluklarını bilmesini sağlar.

<figure><img src="../.gitbook/assets/docbits_annotation_mode_usage.png" alt="Docbits Annotation Mode Usage" width="218"><figcaption></figcaption></figure>

### **Not Modu:**

<figure><img src="../.gitbook/assets/docbits_annotation_mode_tool.png" alt="Docbits Annotation Mode Tool" width="187"><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (35).png" alt=""><figcaption></figcaption></figure>

Belge üzerine notlar bırakabilirsiniz. Bu, belgeyi daha sonra düzenleyecek diğer kullanıcılara bilgi bırakmak için faydalı olabilir.

* **Not Modu:**
* **Amaç:** Kullanıcıların belge üzerinde doğrudan notlar veya açıklamalar bırakmasını sağlar.
* **Kullanım Senaryosu:** Diğer takım üyelerine geri bildirim, talimat veya önemli notlar sağlamak için faydalıdır.

### **Birleştirme:**

<figure><img src="../.gitbook/assets/docbits_merge_tool.png" alt="Docbits Merge Tool" width="60"><figcaption></figcaption></figure>

Belgeler burada birleştirilebilir, örneğin bir fatura sayfası eksikse, bu sayfalar tüm belgenin silinmesi veya yeniden yüklenmesi gerekmeden daha sonra birleştirilebilir.

* **Belgeleri Birleştirme:**
* **Amaç:** Birden fazla belgeyi tek bir dosyada birleştirir.
* **Kullanım Senaryosu:** Belgenin parçaları ayrı ayrı tarandığında ve birleştirilmesi gerektiğinde kullanışlıdır.

### **OCR görünümü:**

<figure><img src="../.gitbook/assets/docbits_ocr_view_tool.png" alt="Docbits Ocr View Tool" width="77"><figcaption></figcaption></figure>

OCR görünümünde, metin belgeden otomatik olarak filtrelenir. Bu, posta kodu, sözleşme numarası, fatura numarası ve bir belgenin sıralanması gibi ilgili özellikleri tanımak için kullanılır.

* **OCR Görünümü:**
* **Amaç:** Optik Karakter Tanıma teknolojisini kullanarak belgeler içindeki metni otomatik olarak tanır.
* **Kullanım Senaryosu:** Basılı veya el yazısı metinlerin dijitalleştirme sürecini hızlandırır, aranabilir ve düzenlenebilir hale getirir.

<figure><img src="../.gitbook/assets/docbits_ocr_usage.png" alt="Docbits Ocr Usage"><figcaption><p>OCR</p></figcaption></figure>

### **Talep Oluştur:**

<figure><img src="../.gitbook/assets/docbits_create_ticket_tool.png" alt="Docbits Create Ticket Tool" width="97"><figcaption></figcaption></figure>

Şirket içinde iletilen görevlerin aksine, bu destek talebi, hataları ve/veya tutarsızlıkları hemen bildirmek ve uygun belge ile birlikte hemen bir hata göndermek için önemlidir. Bu süreci çok daha kolay hale getirir çünkü hatayı hemen uygun belge ile gönderebilirsiniz. Ayrıca öncelik belirleme, belgenin ekran görüntüsünü almak veya yüklemek gibi seçenekler de bulunmaktadır.

* **Talep Oluştur:**
* **Amaç:** Kullanıcıların destek talebi oluşturarak sorunları veya tutarsızlıkları bildirmesine olanak tanır.
* **Kullanım Senaryosu:** Sorunların ve hataların hızlı çözümü için temel oluşturur, sistemin bütünlüğünü ve sorunsuz işleyişini sağlamaya yardımcı olur.

<figure><img src="../.gitbook/assets/docbits_script_logs_usage.png" alt="Docbits Script Logs Usage" width="237"><figcaption></figcaption></figure>
### **Belge skript Günlükleri:**

<figure><img src="../.gitbook/assets/docbits_script_logs_tool.png" alt="Docbits Script Logs Tool" width="160"><figcaption></figcaption></figure>

Skriptler Belge Türleri altında oluşturulabilir; bu bilgiler daha sonra burada görüntülenecektir.

* **Belge Skript Günlükleri:**
* **Amaç:** Farklı belge türleri için uygulanan skriptlerle ilgili günlükleri gösterir.
* **Kullanım Senaryosu:** Belgelerdeki skript işlemlerini izlemek ve hata ayıklamak için kullanışlıdır, kullanıcıların otomatik işlemleri anlamalarına ve herhangi bir sorunu düzeltmelerine yardımcı olur.

<figure><img src="../.gitbook/assets/image (34).png" alt=""><figcaption></figcaption></figure>



### **Daha fazla ayar:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 09.04.13.png" alt="" width="239"><figcaption></figcaption></figure>

### **Belgeyi bölmek:**

* Burada belgeyi bölebilir ve ihtiyaç duyulmayan sayfaları kesip silebilirsiniz.
* **Belgeyi Bölme:**
* **Amaç:** Kullanıcılara belgeyi ayrı parçalara bölmelerine, gerekli olmayan sayfaları kaldırmalarına veya izole etmelerine olanak tanır.
* **Kullanım Senaryosu:** Yalnızca belirli bölümlerin işlenmesi veya gözden geçirilmesi gereken çok sayfalı belgelerle uğraşırken idealdir.

### **Belgeyi İyileştir:**

* Belge yeniden başlatılacaktır
* **Belgeyi İyileştir:**
* **Amaç:** Belgeyi başlangıç durumuna sıfırlar, yeniden değerlendirme veya daha fazla değişiklik için.
* **Kullanım Senaryosu:** İlk değişikliklerin geri alınması gerektiğinde veya belgenin başka bir düzenleme turu için yenilenmesi gerektiğinde kullanışlıdır. Burada belge kalitesini iyileştirmek için ek ML Vision'a ihtiyacımız var.&#x20;

### **Belge Akışı:**

Burada belge akışını bulacaksınız

* **Amaç:** Sistem içinde belge işleme sürecinin sırasını ve ilerlemesini gösterir.
* **Kullanım Senaryosu:** Belge durumunu farklı aşamalarda izlemede yardımcı olur, gerekli tüm işlemlerin takip edildiğinden emin olur.

### **Düzen Şablonuna Git:**

* Bu seçenekle yönlendirilecek ve düzeninizi düzenleyebilecek veya varsayılan şablonu kullanabileceksiniz
* **Düzen Şablonuna Git:**
* **Amaç:** Kullanıcıları mevcut şablonları değiştirmelerine veya varsayılan bir tane uygulamalarına olanak tanıyan bir düzen editörüne yönlendirir.
* **Kullanım Senaryosu:** Belge düzenlerini özelleştirmeyi ve belgeyi şirket standartlarıyla görsel ve işlevsel olarak uyumlu hale getirmeyi sağlayarak belge düzenlerinin belirli iş gereksinimlerini veya tercihleri karşılamasını sağlar.

### **Gerekli alanlar:**

<figure><img src="../.gitbook/assets/docbits_mandatory_fields.png" alt="Docbits Mandatory Fields"><figcaption></figcaption></figure>

Daha fazla düzenleme için gereken alanlar vardır, bunlar ayarlarda düzenlenebilir.

Araç ipucunu kullanarak şunları öğrenin:&#x20;

* Zorunlu bir alan mı (gereklidir)
* Doğrulama gereklidir&#x20;
* Düşük güven
* Tam vergi tutarı uyuşmazlığı
* **Gerekli Alanlar:**
* **Amaç:** Doldurulması veya düzeltilmesi gereken belgelerdeki zorunlu alanları tanımlar.
* **Kullanım Senaryosu:** Temel verilerin doğru bir şekilde yakalanmasını sağlayarak veri bütünlüğünü korur ve iş kurallarına uyumu sağlar.

### **Tablo çıkarma görünümüne git:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.37.png" alt=""><figcaption></figcaption></figure>

Burada tablo çıkarma görünümüne gelir ve devam etmek için daha fazla seçeneğiniz vardır. Örneğin, eğitim modunda tabloyu öğrenme.

* **Tablo Çıkarma Görünümüne Git:**
* **Amaç:** Kullanıcıların belgelerden tablo verilerini çıkarmalarına ve manipüle etmelerine olanak tanıyan bir arayüze yönlendirir.
* **Kullanım Senaryosu:** Tablolar içeren karmaşık belgeler için kullanışlıdır, hassas veri çıkarma ve zamanla tanımayı iyileştirmek için.

### **Eşlenmemiş sütunlar ekle:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.49.png" alt=""><figcaption></figcaption></figure>

Atanmamış sütunları eklemek için buraya tıklayın ve tabloda istediğiniz sütunları seçin veya gereksiz olanları kaldırın.

<figure><img src="../.gitbook/assets/image (37).png" alt="" width="375"><figcaption></figcaption></figure>

### **Eşlenmemiş sütunları göster / Eşlenmemiş sütunları gizle:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.35.58.png" alt=""><figcaption></figcaption></figure>

* **Eşlenmemiş Sütunları Göster/Gizle:**
* **Amaç:** Bilinen alanlara otomatik olarak eşlenmeyen sütunların tabloda görünürlüğünü değiştirir.
* **Kullanım Senaryosu:** Gereksiz sütunları gizleyerek veya potansiyel olarak dahil etmek için gözden geçirerek kullanıcıların ilgili verilere odaklanmasını sağlar.

<figure><img src="../.gitbook/assets/image (38).png" alt=""><figcaption></figcaption></figure>

### **Bu tedarikçi için tablo çıkarmayı engelle:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.06.png" alt=""><figcaption></figcaption></figure>

* **Bu Tedarikçi İçin Tablo Çıkarmayı Engelle:**
* **Amaç:** Belirli tedarikçilerden gelen belgeler için tablo çıkarma işlemlerini engeller.
* **Kullanım Senaryosu:** Tedarikçi belgelerinin sürekli olarak doğru bir şekilde çıkarılamadığı veya çıkarılmasına gerek olmayan senaryolarda kullanışlıdır.

### **Tabloyu Sil:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.14.png" alt=""><figcaption></figcaption></figure>

* **Tabloyu Sil:**
* **Amaç:** Bir belgeden bir tabloyu tamamen kaldırır.
* **Kullanım Senaryosu:** Bir tablo yanlışlıkla dahil edildiğinde veya belgenin amacı için artık gerekli olmadığında kullanışlıdır.

### **Yeni tablo sütunu ekle:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.21.png" alt=""><figcaption></figcaption></figure>

<figure><img src="../.gitbook/assets/image (36).png" alt="" width="375"><figcaption></figcaption></figure>

Eksik bir sütun varsa, burada yeni bir sütun oluşturabilirsiniz. Başlığı belirtin, zorunlu bir alan olup olmamasına karar verin ve sütun türünü belirleyin (bu, doğru biçim için önemlidir)

* **Yeni Tablo Sütunu Ekle:**
* **Amaç:** Mevcut bir tabloya yeni bir sütun oluşturur, başlık, gereklilik ve tür için özelliklerle.
* **Kullanım Senaryosu:** Belirli veri gereksinimlerine uyacak şekilde özel sütun oluşturarak veri yakalamanın esnekliğini ve doğruluğunu artırır.



### **Tablo doğrulamasını yok say:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.29.png" alt=""><figcaption></figcaption></figure>

* **Tablo Doğrulamasını Yok Say:**
* **Amaç:** Belirli tablolar için doğrulama kurallarını atlamak için kullanıcılara olanak tanır.
* **Kullanım Senaryosu:** Bilinen veri anormallikleri iş akışını engelleyecek ve doğrulamaya ısrar etmek iş akışını engelleyecek durumlarda kullanışlıdır.

### **Tablo sütununu geri yükle:**

<figure><img src="../.gitbook/assets/Bildschirmfoto 2024-05-10 um 11.36.37.png" alt=""><figcaption></figcaption></figure>

* **Tablo Sütununu Geri Yükle:**
* **Amaç:** Bir tablodaki daha önce silinmiş veya değiştirilmiş bir sütunu yeniden yükler.
* **Kullanım Senaryosu:** Yanlışlıkla kaldırılan veya değiştirilen verileri kurtarmak için faydalıdır, veri bütünlüğünü sağlar.

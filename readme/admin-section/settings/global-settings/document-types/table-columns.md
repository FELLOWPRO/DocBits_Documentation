# Tablo Sütunları

Tablo sütunları, bir belge türünün satır kalemi tablosunda hangi sütunların bulunduğunu tanımlar: DocBits'in her sütuna hangi veriyi çıkardığını, kullanıcının doğrulama ekranında neyi gördüğünü ve dışa aktarmada ERP'ye neyin gönderildiğini.

**Nerede:** Ayarlar → Genel Ayarlar → Belge Türleri → Tablo Sütunları

<figure><img src="../../../../.gitbook/assets/table-columns_list.png" alt="Sütun başına Zorunlu, Salt Okunur, Gizli ve Yapay Zeka Kullan işaretlerini gösteren Tablo Sütunları listesi"><figcaption><p>Tablo Sütunları: her sütun için bir satır, işaretler doğrudan listede değiştirilir</p></figcaption></figure>

## Ne görürsünüz

Her satır, bir tablonun bir sütunudur. Liste şunları gösterir:

| Sütun | Anlamı |
|---|---|
| **Sütun adı** | Başlıktan türetilen teknik ad (büyük harf, alt çizgi). Scriptlerde, dışa aktarma eşlemelerinde ve API'de kullanılır. Sonradan değiştirilemez. |
| **Başlık** | Doğrulama ekranında gösterilen etiket. *İşlemler* sütunundaki çeviri simgesiyle (*Çeviri anahtarını güncelle*) değiştirilir. |
| **Sütun Türü** | `AMOUNT`, `STRING`, `DATE`, `NUMBER`, `BOOLEAN` veya `CURRENCY`. Doğrulamayı ve biçimlendirmeyi belirler. |
| **Tablo adı** | Sütunun ait olduğu tablo, örneğin `INVOICE_TABLE`. |
| **Zorunlu** | Bu sütun herhangi bir satırda boşken belge onaylanamaz. |
| **Salt Okunur** | Kullanıcılar değeri görür ancak düzenleyemez. |
| **Gizli** | Sütun ne gösterilir ne de dışa aktarılır. İhtiyaç duymadığınız varsayılan sütunları kapatmak için kullanılır. |
| **Yapay Zeka Kullan** | Tedarikçinin eğitilmiş kuralları olsa bile bu sütunu yapay zeka tablo çıkarma doldurur. |
| **İşlemler** | Çeviri simgesi: başlığı yeniden adlandırır. Bilgi simgesi: gösterilen etiketin nereden geldiğini gösterir (sizin çeviriniz, varsayılan, anahtar). Üç nokta menüsü: *Sil*, yalnızca kuruluşunuzun oluşturduğu sütunlar için; varsayılan sütunlar yalnızca gizlenebilir. |

Listenin üstünde iki düğme bulunur:

* **Yeni tablo oluştur**: belge türü için ikinci bir satır kalemi tablosu (örneğin kalem tablosunun yanında bir masraf tablosu).
* **Yeni tablo sütunu ekle**: aşağıdaki **Yeni sütun ekleme** bölümünde açıklanan iletişim kutusunu açar.

## Varsayılan sütunlar ve kendi sütunlarınız

Her belge türü bir dizi varsayılan sütunla gelir (faturalar için: kalem numarası, açıklama, miktar, birim fiyat, toplam tutar, vergi, …). Bunlar kuruluşunuza değil DocBits'e aittir, bu nedenle silinemez; bunun yerine gizleyin. Kendi eklediğiniz sütunlar kuruluşunuza aittir ve silinebilir.

{% hint style="info" %}
**Değişiklikler yalnızca yeni belgeler için geçerlidir.** Eklediğiniz, gizlediğiniz veya sildiğiniz bir sütun, değişiklikten sonra yüklenen veya yeniden başlatılan belgelerde görünür. Panoda zaten bulunan belgeler tablolarını çıkarıldığı haliyle korur. Yeni yapılandırmanın uygulanması için belgeyi yeniden başlatın.
{% endhint %}

## Amaç ve kullanım

Bir tablo sütunu, satır kalemi tablosunun bir alanıdır. DocBits'in bir tabloyla yaptığı her şey (çıkarma, doğrulama, PO eşleştirme, dışa aktarma) burada yapılandırılan sütunlar üzerinde çalışır.

### Bir sütunun göründüğü yerler

| Yer | Sütunun orada üstlendiği görev |
|---|---|
| **Doğrulama ekranı** | Satır kalemi tablosunda bir sütun. *Başlık* sütun başlığıdır, *Sütun Türü* düzenleyiciyi belirler (tutar, tarih, metin, evet/hayır). Gizli sütunlar gösterilmez. |
| **Tablo eğitimi** | Bir tedarikçinin tablosunu eğitirken, algılanan her tablo sütununu burada yapılandırılan sütunlardan birine eşlersiniz. Yalnızca yapılandırılmış sütunlar eşlenebilir. |
| **Yapay zeka tablo çıkarma** | Yapay zeka, yapılandırılmış sütunları doldurur. *Yapay Zeka Kullan* olarak işaretlenen bir sütun, eğitilmiş kuralları olan tedarikçiler için bile yapay zeka tarafından doldurulur. |
| **Doğrulama kuralları** | *miktar × birim fiyat = satır toplamı* gibi satır kalemi kontrolleri, `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `CHARGES`, `DISCOUNT` varsayılan sütunları üzerinde çalışır. |
| **PO eşleştirme** | Kalem numarası, birim fiyat, miktar ve toplam tutar varsayılan sütunlarına ihtiyaç duyar. Bunlar olmadan belge *Line Item Table is missing Mandatory column for PO* mesajını gösterir. |
| **Dışa aktarma** | Gizli olmayan her sütun, ERP'ye gönderilen satır kalemi verilerinin bir parçasıdır. Dışa aktarma eşlemesi *Sütun adı*na başvurur. |
| **Scriptler** | Scriptler sütunları *Sütun adı* ile okur ve yazar, örneğin `row["TOTAL_AMOUNT"]`. |

### Kapsam

* Tablo sütunları **tablo başına** yapılandırılır ve bir tablo bir **belge türüne** aittir. Fatura sütunları irsaliyeleri etkilemez.
* Yapılandırma **kuruluş başınadır**. Alt kuruluşlar bunu devralır.
* Belirli bir tedarikçi için hangi sütunların *doldurulacağına* o tedarikçinin eğitimi veya yapay zeka karar verir; sütun yapılandırması yalnızca hangi sütunların var olduğunu belirler.

### Yapılandırmayı değiştirmenin tipik nedenleri

* Müşteriye özel bir değerin satır başına yakalanması gerekiyor (masraf yeri, proje numarası, dahili ürün numarası) → sütun ekleyin.
* Bir varsayılan sütun hiç kullanılmıyor ve doğrulama ekranını kalabalıklaştırıyor → gizleyin.
* Bir sütun dışa aktarmadan önce her zaman dolu olmalı → *Zorunlu* olarak işaretleyin.
* Bir değer ERP aramasından geliyor ve kullanıcılar tarafından düzenlenmemeli → *Salt Okunur* olarak işaretleyin.
* Yapay zeka bir sütunu eğitilmiş kurallardan daha iyi yakalıyor (örneğin serbest metin açıklamalar) → *Yapay Zeka Kullan* olarak işaretleyin.

## Yeni sütun ekleme

Varsayılan sütunların kapsamadığı bir değerin satır kalemi başına yakalanması gerektiğinde bir sütun ekleyin: masraf yeri, proje numarası, dahili ürün numarası.

### Başlamadan önce

* Sütunun hangi **tabloya** ait olacağına karar verin. Çoğu belge türünün tek tablosu vardır (örneğin `INVOICE_TABLE`). Liste boşsa önce **Yeni tablo oluştur**'a tıklayın; iletişim kutusu yalnızca bir tablo adı sorar.
* **Türe** karar verin: para tutarları için `AMOUNT`, miktarlar için `NUMBER`, tarihler için `DATE`, evet/hayır için `BOOLEAN`, ISO para birimi kodu için `CURRENCY`, diğer her şey için `STRING`. Tür kaydedildikten sonra değiştirilemez.
* Aynı anlama gelen ancak gizli olan bir **varsayılan sütunun** zaten var olup olmadığını kontrol edin. Gizli sütunlar listede *Gizli* işareti ayarlı olarak görünür; kopya oluşturmak yerine gizliliğini kaldırın.

### Adımlar

1. **Ayarlar → Genel Ayarlar → Belge Türleri → Tablo Sütunları**'nı açın.
2. **Yeni tablo sütunu ekle**'ye tıklayın.

<figure><img src="../../../../.gitbook/assets/table-columns_add-dialog.png" alt="Başlık, Sütun zorunlu mu, Sütun türünü seçin ve Tablo seçin alanlarıyla Yeni tablo sütunu ekle iletişim kutusu"><figcaption><p>Yeni tablo sütunu ekle</p></figcaption></figure>

3. İletişim kutusunu doldurun:

| Alan | Ne girilir |
|---|---|
| **Başlık** | Kullanıcının doğrulama ekranında gördüğü etiket, örneğin `Cost Centre`. Yalnızca harf ve rakam. DocBits teknik *Sütun adı*nı bundan türetir (`COST_CENTRE`). |
| **Sütun zorunlu mu?** | Sütun herhangi bir satırda boşken belgenin onaylanmaması gerekiyorsa işaretleyin. |
| **Sütun türünü seçin** | Yukarıdaki tür listesine bakın. |
| **Tablo seçin** | Sütunun ekleneceği tablo. |

4. **Devam**'a tıklayın. Sütun listede *Salt Okunur*, *Gizli* ve *Yapay Zeka Kullan* işaretleri kapalı olarak görünür. Gerekirse bu işaretleri listede değiştirin, aşağıdaki **Sütunları düzenleme ve silme** bölümüne bakın.

### Ekledikten sonra

* Sütun **mevcut belgelerde boştur**. Değişiklikten sonra yüklenen veya yeniden başlatılan belgelerde doldurulur.
* **Eğitilmiş kuralları** olan tedarikçiler için, tedarikçinin belgelerinden birini tablo eğitiminde açın ve yeni sütunu eşleyin; aksi halde sütun o tedarikçi için boş kalır. Bkz. [Tabloları ve Sütunları Tanımlama](../../../setup/document-training/training-line-fields-table-training/defining-tables-and-columns.md).
* **Yapay zeka tablo çıkarma** ile, değer belgede tanınabiliyorsa yapay zeka sütunu doldurur. Tedarikçinin eğitilmiş kuralları varsa ancak bu sütunun yine de yapay zekadan gelmesi gerekiyorsa sütunu *Yapay Zeka Kullan* olarak işaretleyin.
* ERP'nin sütunu alması gerekiyorsa sütunu **dışa aktarma eşlemesine** ekleyin, bkz. [Dışa Aktar](../../../../administration-and-setup/settings/document-processing/export.md).

### Mesajlar

| Mesaj | Anlamı |
|---|---|
| *Column name already exists* | Bu teknik ada sahip bir sütun tabloda zaten var. Farklı bir başlık seçin. |
| *Column name already exists – Please activate it in Table Column settings* | Gizli bir varsayılan sütun bu ada sahip. Yeni bir sütun oluşturmak yerine onun *Gizli* işaretini kaldırın. |
| *No table exists. Please create table before creating columns.* | Belge türünün henüz tablosu yok: önce **Yeni tablo oluştur**'a tıklayın. |

## Sütunları düzenleme ve silme

Başlık dışındaki her şey doğrudan listede değiştirilir; ayrı bir düzenleme iletişim kutusu yoktur.

**Nerede:** Ayarlar → Genel Ayarlar → Belge Türleri → Tablo Sütunları

### Bir işareti değiştirme

Satırdaki onay kutusunu işaretleyin veya işaretini kaldırın. Değişiklik hemen kaydedilir (*Successfully saved*).

| İşaret | Açık | Kapalı |
|---|---|---|
| **Zorunlu** | Sütun herhangi bir satırda boşken onay engellenir; doğrulama ekranı hücreyi işaretler. | Boş hücrelere izin verilir. |
| **Salt Okunur** | Değer gösterilir ancak üzerine yazılamaz. Bir aramadan veya scriptten gelen değerler için kullanın. | Kullanıcılar hücreyi düzenleyebilir. |
| **Gizli** | Sütun doğrulama ekranından ve dışa aktarmadan kaldırılır. Verisi korunur. | Sütun gösterilir ve dışa aktarılır. |
| **Yapay Zeka Kullan** | Yapay zeka tablo çıkarma bu sütunu, eğitilmiş kuralları olan tedarikçiler için de doldurur. | Sütun eğitilmiş kurallar tarafından, kural yoksa yapay zeka tarafından doldurulur. |

{% hint style="info" %}
İşaretler, değişiklikten **sonra** yüklenen veya yeniden başlatılan belgelerde geçerli olur. Açık belgeler yeniden başlatılana kadar mevcut tablolarını korur.
{% endhint %}

### Başlığı yeniden adlandırma

*İşlemler* sütunundaki çeviri simgesine (*Çeviri anahtarını güncelle*) tıklayın, yeni etiketi girin ve onaylayın. Yanındaki bilgi simgesi, şu anda hangi etiketin geçerli olduğunu ve nereden geldiğini gösterir. Yalnızca etiket değişir; teknik *Sütun adı* aynı kalır, böylece scriptler, dışa aktarma eşlemeleri ve eğitilmiş kurallar çalışmaya devam eder.

### Türü veya tabloyu değiştirme

Mümkün değildir. Sütunu gizleyin (veya kendi sütununuzsa silin) ve doğru türde yeni bir sütun ekleyin.

### Bir sütunu silme

Silme işlemi yalnızca kuruluşunuzun oluşturduğu sütunlar için sunulur. Varsayılan sütunlar silinemez; bunları gizleyin.

1. *İşlemler* sütunundaki üç nokta menüsünü açın ve **Sil**'i seçin. Varsayılan sütunlarda bu seçenek bulunmaz.
2. Onaylayın.

Ne olur:

* Sütun yapılandırmadan kaldırılır. **Bundan sonra** işlenen belgelerde artık bulunmaz.
* Zaten çıkarılmış belgeler, yeniden başlatılana kadar sütunu ve değerlerini korur.
* Bu sütunu eşleyen eğitilmiş kurallar diğer sütunlar için çalışmaya devam eder; silinen sütunun eşlemesi yok sayılır.
* Sütuna bir dışa aktarma eşlemesinde veya scriptte başvuruluyorsa bu başvuruyu kaldırın; aksi halde dışa aktarma veya script eksik sütun hatasıyla başarısız olur.

### Bir silme işlemini geri alma

Silinen bir sütun listeden geri yüklenemez. Aynı başlıkla yeniden ekleyin: teknik ad başlıktan türetildiği için aynı başlıkla oluşturulan sütun aynı *Sütun adı*nı alır ve mevcut eşlemeler yeniden eşleşir.

## En iyi uygulamalar

### Tutarlar ve miktarlar için varsayılan sütunları koruyun

Satır kalemi kontrolleri (*miktar × birim fiyat = satır toplamı*) ve PO eşleştirme, `QUANTITY`, `UNIT_PRICE`, `TOTAL_AMOUNT`, `ITEM_NUMBER` varsayılan sütunlarını arar. Bu değerler için bunların yerine kendi sütunlarınızı oluşturursanız kontroller çalışmaz ve PO eşleştirme eksik zorunlu sütun bildirir. İfade size uymuyorsa *başlığı* yeniden adlandırın; sütunu koruyun.

### Silmeyin, gizleyin

İhtiyaç duymadığınız varsayılan sütunlar silinmez, gizlenir; zaten silinemezler. Kendi sütunlarınız için de, bir scriptin veya dışa aktarma eşlemesinin sütuna hâlâ başvurup başvurmadığından emin değilseniz gizlemek daha güvenli seçenektir.

### Yalnızca dışa aktarmayı engelleyen değerleri zorunlu yapın

Her zorunlu sütunun, kullanıcı belgeyi onaylayabilmeden önce her satırda doldurulması gerekir. Bunu, eksik olduğunda ERP'nin reddettiği değerler için kullanın (örneğin bir muhasebe dışa aktarmasındaki masraf yeri), yalnızca faydalı olan değerler için değil.

### Aranan değerler için *Salt Okunur* kullanın

Bir scriptin veya ana veri aramasının tabloya yazdığı değerler (ürün ana verisinden ürün açıklaması, tedarikçiden vergi kodu) salt okunur olmalıdır; böylece kullanıcılar kopyayı değil kaynağı düzeltir.

### Yapay zekayı tedarikçi başına değil, sütun başına kullanın

Eğitilmiş kuralları olan bir tedarikçide çoğu sütun kurallardan doğru gelir. Bir sütun güvenilir değilse (satır kaydıran uzun açıklamalar, bazen farklı bir yerde duran bir indirim), *Yapay Zeka Kullan*'ı yalnızca o sütunda ayarlayın. Gerisini kurallar üstlenir.

### Sütunları belgeye göre değil, ERP'ye göre adlandırın

*Sütun adı* dışa aktarma eşlemelerinde ve scriptlerde kullanılır. `COST_CENTRE`, `KST`'den daha kolay eşlenir ve bir tedarikçi bunu farklı yazdırdığında değişmez.

### Yeniden başlatılmış bir belgede test edin

Bir değişiklikten sonra belge türünün mevcut bir belgesini yeniden başlatın ve açın: yeni sütun görünür, gizlenen sütun kaybolmuştur, zorunlu hücreler işaretlidir. Ancak bundan sonra kullanıcılara sunun.

### Her satır kalemi yapısı için tek tablo

Yalnızca bir belge türü gerçekten iki bağımsız tabloya sahip olduğunda (örneğin kalem satırları ve ayrı bir masraf tablosu) ikinci bir tablo oluşturun. Fazladan boş tablolar, o türün her belgesinde görünür.

## Sorun giderme

### Yeni sütun doğrulama ekranında görünmüyor

* Belge, sütun eklenmeden önce işlendi. Değişiklikler sonradan yüklenen veya yeniden başlatılan belgeler için geçerlidir; **belgeyi yeniden başlatın** (Pano → belge menüsü → Yeniden Başlat).
* Sütun **Gizli**. Tablo Sütunları listesindeki işareti kontrol edin.
* Sütun, gösterilenden **farklı bir tabloya** eklendi. Doğrulama ekranı belge türünün tablolarını gösterir; *Tablo adı* sütununu karşılaştırın.
* Belge, yapılandırdığınız belge türünden değil.

### Sütun var ama her zaman boş

* Tedarikçinin **eğitilmiş kuralları** var ve yeni sütun bunlarda eşlenmemiş. Tedarikçinin belgelerinden birini tablo eğitiminde açın ve sütunu eşleyin veya sütunda *Yapay Zeka Kullan*'ı ayarlayın.
* Yapay zeka çıkarmasında değer belgede tanınamıyor (başlık yok, kısaltılmış, farklı bir dilde). Sütunu adlandıran bir yapay zeka tablo etiketi ekleyin veya sütunu eğitimde eşleyin.

### "Column name already exists"

Aynı teknik ada sahip bir sütun tabloda zaten var. Listede görünmüyorsa gizli bir varsayılan sütundur: mesaj *Please activate it in Table Column settings* der. Yeni bir sütun oluşturmak yerine o sütunun *Gizli* işaretini kaldırın.

### Onay, zorunlu bir sütun tarafından engelleniyor

Tablodaki mesaj sütunu adlandırır. Ya hücreyi her satırda doldurun ya da (değer bu belgede yoksa) sütunun *Zorunlu* işaretini kaldırın, belgeyi yeniden başlatın ve tekrar deneyin. Sütunun gerçekten zorunlu olması gerekip gerekmediğini değerlendirin (yukarıdaki **En iyi uygulamalar** bölümüne bakın).

### Yapay zeka bir sütunu yanlış değerle dolduruyor

Tipik durum: `CHARGES` satır toplamını alır ve masraflar `miktar × birim fiyat + masraflar` formülünün parçası olduğundan her satır *Line total does not match quantity x unit price (expected …, got …)* mesajıyla satır toplamı kontrolünde başarısız olur.

* Eğitilmiş kurallar sütunu doğru yakalıyorsa sütunda *Yapay Zeka Kullan* işaretini kaldırın.
* Tedarikçinin kuralı yoksa, sütunun doğru konuma bağlanması için tabloyu bir kez eğitin (Tablo eğitimi) veya tedarikçi bu değeri hiç yazdırmıyorsa sütunu gizleyin.
* Son çare olarak, belge türünün Daha Fazla Ayarlar bölümündeki *Tablo doğrulamasını yok say* seçeneği tüm belge türü için her tablo kontrolünü kapatır; uyuşmazlık artık yakalanmaz, boş zorunlu sütunlar da yakalanmaz.

### PO eşleştirme: "Line Item Table is missing Mandatory column"

PO eşleştirme, kalem numarası, birim fiyat, miktar ve toplam tutar varsayılan sütunlarına ihtiyaç duyar. Bunlardan biri gizli veya özel bir sütunla değiştirilmiş. Varsayılan sütunun gizliliğini kaldırın veya tablo eğitiminde değeri ona eşleyin.

### Bir sütun silindikten sonra script veya dışa aktarma başarısız oluyor

Script veya dışa aktarma eşlemesi hâlâ silinen *Sütun adı*na başvuruyor. Başvuruyu kaldırın veya sütunu aynı başlıkla yeniden ekleyin; teknik ad başlıktan türetilir ve yeniden eşleşir.

### Daha fazla bilgi

* [Eğitim Satır Alanları / Tablo Eğitimi](../../../setup/document-training/training-line-fields-table-training/README.md): DocBits'e bir tedarikçinin tablosunun nerede olduğunu öğretin
* [Yapay Zeka Tablosu](../../../../readme-1/ai-table.md): kullanıcının doğrulama ekranında gördükleri
* [Doğrulama Ekranı](../../../../readme-1/validation-screen.md): çıkarılan tablo ve onayı engelleyen kontroller

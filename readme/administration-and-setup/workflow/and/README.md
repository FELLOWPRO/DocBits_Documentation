# And: bir koşul kartı seçin

İş akışının **Ne zaman** tetikleyicisinden sonra devam edip etmeyeceğine karar vermek için bir **Ve** kartı kullanın. **Daha sonra** eyleminden önce ihtiyaç duyduğunuz kontrolleri ekleyin. Her kart, **Operatör**, **Alan Adı** veya **Değer** gibi doldurulacak alanlar gösterir; ekran görüntüleri tamamlanmış kuralları değil, kullanılabilir kart şablonlarını gösterir.

**İş Akışı Oluşturucu** bölümünde **Ve....** altındaki **Kart Ekle** seçeneğini seçin. Soldan bir kategori seçin veya **Arama Kartı** alanına bir kart adı yazın. İş akışına eklemek için bir kart önizlemesi seçin. Daha fazla kart görmek için önizleme listesini kaydırabilirsiniz. Başka bir kart seçmeden seçiciyi kapatmak için **×** kullanın. Kartları yapılandırdıktan sonra iş akışını kaydedin. Çevreleyen **Ne zaman**, **Ve** ve **Daha sonra** adımları için [İş Akışı](../README.md) sayfasına bakın.

## Satınalma Siparişi ile Karşılaştır

Sipariş veya fatura verilerini bir satınalma siparişiyle karşılaştırmak için bu kartları kullanın; örneğin birim fiyat, vaat edilen teslimat tarihi, masraflar veya miktar. Seçilen kartın istediği alanları, operatörü ve varsa toleransı seçin. Tek tek kartlar için [Satınalma Siparişi ile Karşılaştır](compare-with-purchase-order/README.md) sayfasına bakın.

<figure><img src="../../../.gitbook/assets/and-category-po-comparison-tr-20261008.png" alt="Türkçe And kart seçicisi, Satınalma Siparişi ile Karşılaştır seçili; görünen önizlemeler birim fiyatı, teslimat tarihi, masraflar ve miktar karşılaştırmalarını içerir."><figcaption><p>Türkçe Sandbox'ta Satınalma Siparişi ile Karşılaştır kategorisi.</p></figcaption></figure>

## Belge Alanı

Bir onay kutusunu veya alan durumunu denetlemek, bir alanı bir değerle karşılaştırmak ya da iki alanı karşılaştırmak için bu kategoriyi seçin. Seçilen kartta **Alan Adı** ve **Operatör** yer tutucularını doldurun. Bazı karşılaştırmalar ayrıca bir tolerans ister. Bkz. [Belge Alanı](document-field/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-field-tr-20261008.png" alt="Türkçe And kart seçicisi, Belge Alanı seçili; görünen önizlemeler bir onay kutusunu, alan durumunu, alan değerlerini ve iki alan karşılaştırmasını denetler."><figcaption><p>Belge Alanı kontrolleri geçerli belgedeki değerleri kullanır.</p></figcaption></figure>

## Tarih ve Saat

Bir tarih veya saati bir aralıkla karşılaştırmak ya da **Bugün** ile seçilen bir tarihi karşılaştırmak için **Tarih ve Saat** kullanın. Kartta **Operatör** ve tarih değerlerini seçin. Bkz. [Tarih ve Saat](date-and-time/README.md).

<figure><img src="../../../.gitbook/assets/and-category-date-time-tr-20261008.png" alt="Türkçe And kart seçicisi, Tarih ve Saat seçili; iki önizleme bir tarih veya saati bir aralıkla karşılaştırır ve Bugün ile bir Tarihi karşılaştırır."><figcaption><p>Tarih ve Saat bir aralık kontrolü ve bugüne göre bir kontrol sunar.</p></figcaption></figure>

## Belge

Bir iş akışı **belge türüne** veya **alt kuruluşa** bağlı olması gerektiğinde bu kartları kullanın. Kartta adı geçen türü veya kuruluşu seçin. Bkz. [Belge](document/README.md).

<figure><img src="../../../.gitbook/assets/and-category-document-tr-20261008.png" alt="Türkçe And kart seçicisi, Belge seçili; önizlemeler belge türünü ve bir alt kuruluşa üyeliği denetler."><figcaption><p>Belge koşulları türü veya alt kuruluşu denetler.</p></figcaption></figure>

## Mantık

Bu kategori karar tablosu, bir HTTPS yanıtı, modül kullanılabilirliği, teklif edilen bir ürün fiyatı, bir şans değeri veya iki değer kullanan kontrolleri içerir. İlgili kartı açın ve adlandırılmış yer tutucularını doldurun; örneğin HTTPS kartı URL, yöntem ve kabul edilen durum kodunu sorar. Bkz. [Mantık](logic/README.md).

<figure><img src="../../../.gitbook/assets/and-category-logic-tr-20261008.png" alt="Türkçe And kart seçicisi, Mantık seçili; önizlemeler karar tablosu, HTTPS isteği, etkin modül, teklif edilen fiyat, şans ve değer karşılaştırma kartlarını içerir."><figcaption><p>Mantık birkaç farklı koşul türü sunar; kuralınıza uyanı seçin.</p></figcaption></figure>

## Durum

Bir belgenin seçilen bir duruma sahip olup olmadığını veya durumunun seçili bir küme içinde olup olmadığını denetlemek için **Durum** kullanın. Kartta **Operatör** ve **Durum** seçin. Bkz. [Durum](status/README.md).

<figure><img src="../../../.gitbook/assets/and-category-status-tr-20261008.png" alt="Türkçe And kart seçicisi, Durum seçili; iki önizleme Belge durumunu bir Durumla veya bir durum kümesiyle karşılaştırır."><figcaption><p>Durum koşulları belgenin geçerli durumunu denetler.</p></figcaption></figure>

## Masa

Bu kartlar belge tablosu satırlarını inceler. Görünen seçenekler tarih kontrollerini, metin kalıplarını, raf ömrünü ve sütunlar arası karşılaştırmaları içerir. Bir operatör veya kalıp seçmeden önce **Tablo adı** ve **Sütun Adı** seçin. Bkz. [Masa](table/README.md).

<figure><img src="../../../.gitbook/assets/and-category-table-tr-20261008.png" alt="Türkçe And kart seçicisi, Masa seçili; görünen önizlemeler tarih, regex kalıbı, raf ömrü ve tablo sütunu karşılaştırmalarını içerir."><figcaption><p>Masa koşulları bir belge tablosunun satırlarını ve sütunlarını kullanır.</p></figcaption></figure>

## Teklif Fiyatı ile Karşılaştır

Bir ürünü teklif fiyatı verileriyle karşılaştırmak için bu kartları kullanın. Görünen seçenekler ürün kimliği, tedarikçi türü, tedarikçi ürün kimliği, birim fiyat ve ölçü birimini kapsar. **Operatör** ve veri yer tutucuları seçtiğiniz karta bağlıdır.

<figure><img src="../../../.gitbook/assets/and-category-quote-price-tr-20261008.png" alt="Türkçe And kart seçicisi, Teklif Fiyatı ile Karşılaştır seçili; beş önizleme ürün kimliği, tedarikçi türü, tedarikçi ürün kimliği, birim fiyat ve ölçü birimini kapsar."><figcaption><p>Teklif Fiyatı ile Karşılaştır, geçerli kart seçicide ayrı bir kategoridir.</p></figcaption></figure>

## Atanan kişi

Koşul atanan kullanıcıya veya gruba bağlı olduğunda **Atanan kişi** kullanın. Tek bir kullanıcı ya da grupla mı yoksa seçili bir kümeyle mi karşılaştırılacağını seçin. Bkz. [Atanan kişi](assignee/README.md).

<figure><img src="../../../.gitbook/assets/and-category-assignee-tr-20261008.png" alt="Türkçe And kart seçicisi, Atanan kişi seçili; önizlemeler atanan kullanıcıyı veya grubu bir ya da birkaç seçenekle karşılaştırır."><figcaption><p>Atanan kişi koşulları belgeye atanan kullanıcıyı veya grubu denetler.</p></figcaption></figure>

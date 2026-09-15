# Dışa Aktarmada Satır Kalemleri

Bir belge onaylanıp dışa aktarıldığında satır kalemi tablosuna ne olacağı, dışa aktarma yöntemine bağlıdır. Bu sayfa, hangi sütunların DocBits'ten çıktığını, hangilerinin zorunlu olduğunu ve bir dışa aktarmanın neden doğrulama ekranından daha az satır gösterebileceğini açıklar.

## İki tür dışa aktarma

| Dışa aktarma yöntemi | Tablo için ne gönderilir |
|---|---|
| **webhook**, **watcher**, **sftp**, **infor_sftp** (JSON / XML) | Tablo doğrulama ekranındaki haliyle: her satırın gizli olmayan her [tablo sütunu](../../../admin-section/settings/global-settings/document-types/table-columns.md), değer, biçimlendirilmiş değer ve güven puanıyla birlikte. |
| **infor-m3-cloud**, **infor-m3-toml-cloud**, **infor-idm-***, **infor-gls840-onpremise**, **infor-m3-oc-charges-onpremise** (Infor ERP / SAP BOD'ları) | Ham tablo değil. DocBits bundan **teslim alma satırları** ve **maliyet satırları** oluşturur (aşağıya bakın) ve bunları [INFOR'a Aktarma](../../../admin-section/setup/exporting-in-docbits/exporting-to-infor/README.md) altında yapılandırılan eşlemeyle BOD alanlarına eşler. |

## Teslim alma satırları ve maliyet satırları (Infor dışa aktarmaları)

Bir ERP fatura satırı ya bir **teslim alma satırıdır** (receipt line), yani bir satın alma siparişi teslim alımını kapatır, ya da bir **maliyet satırıdır** (cost line), yani bir tutarı boyutlarıyla birlikte bir defter hesabına kaydeder. DocBits fatura satırı başına karar verir:

* **Teslim alma satırları** **PO eşleştirmeden** gelir. Bir PO satırıyla eşleştirilen her fatura satırı (Pano → PO Eşleştirme veya *PO otomatik eşleştirme* ile otomatik olarak), PO numarasını, PO satırını, teslim alma satırını ve eşleşen miktar ile tutarı taşıyan bir teslim alma satırı olur. PO eşleşmesi olmayan bir faturanın **teslim alma satırı yoktur**; dışa aktarma önizlemesi bu durumda `receipt_lines: []` gösterir, bu doğrudur, bir hata değildir.
* **Maliyet satırları**, maliyet muhasebesi adımının (veya Otomatik Muhasebe'nin) oluşturduğu **muhasebe kaydından** gelir: satır başına defter hesabı, boyutlar, tutar, miktar. Muhasebe kaydı olmayan bir faturanın maliyet satırı yoktur.
* **Vergi satırları** tablodan değil, başlıktaki vergi tutarlarından oluşturulur.

Dolayısıyla Infor dışa aktarmalarında satır kalemi tablosu, PO eşleştirme ve muhasebenin *girdisidir*; ERP'nin aldığı şey bu iki adımın sonucudur. Ne PO ile eşleşen ne de muhasebeleştirilen bir satır ERP'ye ulaşmaz.

{% hint style="warning" %}
PO eşleştirmenin çalışması için tabloda **kalem numarası, birim fiyat, miktar ve toplam tutar** varsayılan sütunları bulunmalıdır. Bunlardan biri gizliyse doğrulama ekranı *Line Item Table is missing Mandatory column for PO* mesajını gösterir ve hiçbir teslim alma satırı oluşturulamaz.
{% endhint %}

## Zorunlu sütunlar ve onay iletişim kutusu

Bir belge onaylanabilmeden önce DocBits tabloyu kontrol eder:

1. **Zorunlu** olarak işaretlenen her sütunun (Ayarlar → Belge Türleri → Tablo Sütunları) her satırda bir değeri olmalıdır.
2. Her satır **satır toplamı kontrolünden** geçmelidir: `toplam = miktar × birim fiyat + masraflar − indirim`, 0,02 tolerans dahilinde. Başarısız satırlar işaretlenir; mesaj beklenen ve gerçek değeri belirtir.
3. **Satır toplamlarının toplamı**, başlıktaki net tutarla karşılaştırılır. Bir fark uyarıdır ve onayı engellemez.

Onay iletişim kutusu hâlâ eksik olanları listeler. Bir yönetici, **Tablo doğrulamasını yok say** ile (Belge Türleri → Daha Fazla Ayarlar) her tablo kontrolünü belge türü başına kapatabilir; satır toplamları ve zorunlu sütunlar o zaman artık kontrol edilmez, başlık kontrolleri devam eder.

Mesajların ayrıntıları: [Doğrulama Ekranı](../../../readme-1/validation-screen.md) sayfasındaki "Onayı ne engeller" bölümü.

## Boş tablo

* **JSON / XML dışa aktarmaları** belgeyi `tables: []` ile (veya sıfır satırlı tabloyla) gönderir. Alıcı sistem boş bir tabloyu işleyebilmelidir.
* Teslim alma satırı ve maliyet satırı olmayan **Infor dışa aktarmaları** yalnızca başlık ve vergi satırlarını gönderir. Çoğu ERP satırsız bir faturayı reddeder; bu tür belge türleri için Otomatik Muhasebe veya varsayılan bir maliyet satırı yapılandırın ya da bunları farklı bir dışa aktarmaya yönlendirin.
* **Tablosu olmayan** bir belge türü (yapılandırılmış tablo yok) hiçbir zaman satır verisi göndermez; başlık düzeyinde eşleştirilen sipariş onayları gibi belge türleri için bu beklenen davranıştır.

## Onaylamadan önce kontrol etme

API veya MCP erişimi olan iş ortakları ve destek ekibi, bir belgenin dışa aktarma yükünü gönderilmeden önce isteyebilir: MCP aracı `get_export_preview(doc_id)`, dışa aktarmanın göndereceği şeyi tam olarak döndürür: Infor dışa aktarmaları için `receipt_lines`, `cost_lines` ve `tax_lines`, JSON dışa aktarmaları için `tables`. ERP eksik satır bildirdiğinde kullanın: `receipt_lines` boşsa fatura PO ile eşleştirilmemiştir; `cost_lines` boşsa muhasebe kaydı yoktur.

## İlgili sayfalar

* [Dışa Aktar](export.md): dışa aktarma yapılandırmaları ve yöntemleri
* [Tablo Sütunları](../../../admin-section/settings/global-settings/document-types/table-columns.md)
* [INFOR'a Aktarma](../../../admin-section/setup/exporting-in-docbits/exporting-to-infor/README.md): teslim alma, maliyet ve vergi satırları için BOD alan eşlemeleri

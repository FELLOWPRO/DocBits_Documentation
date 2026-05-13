# Supplier BOD Eşleme

Bu sayfa, DocBits'in Infor M3'ten tedarikçi ana verilerini `SyncSupplierPartyMaster` ve `SyncRemitToPartyMaster` BOD'ları aracılığıyla nasıl içe aktardığını belgeler. Her iki BOD da DocBits'te aynı `SUPPLIER` ana veri tablosunu doldurur.

{% file src="../../../../.gitbook/assets/Sync.SupplierPartyMaster.pdf" %}
SupplierPartyMaster — Orijinal BOD eşleme referansı (PDF)
{% endfile %}

{% file src="../../../../.gitbook/assets/Sync.RemitToPartyMaster.pdf" %}
RemitToPartyMaster — Orijinal BOD eşleme referansı (PDF)
{% endfile %}

## Temel ilkeler

- **CONO + SUNO eşleştirme anahtarıdır.** DocBits'teki bir `supplier_header` satırı, `(customer_number = sharedCONO, supplier_number = sharedSUNO)` ile benzersiz olarak tanımlanır. Bu, tek bir DocBits organizasyonunun birden fazla M3 şirketini birleştirmesine olanak tanır.
- **`variationID`, sıra dışı BOD'lara karşı koruma sağlar.** M3, aynı ana veri kaydını arka arkaya hızlıca birden çok kez yayabilir; gelen `variationID`, güncellemenin kabul edilmesi için saklı değerden büyük olmalıdır. Her iki BOD da kendi `variationID`'lerini bağımsız olarak takip eder (`variation_id_supplier_bod`, `variation_id_remit_to_party`).
- **Sessiz üzerine yazma yoktur.** SupplierPartyMaster ve RemitToPartyMaster birkaç alanı paylaşır (ad, telefon, KDV, banka, durum). Her BOD yalnızca sahip olduğu alanları günceller ve yalnızca `variationID`'si ilerlerse. Paylaşılan kümede, en son alınan BOD (BOD türü başına) kazanır.
- **Çoklu banka senkronizasyonu tercih kontrolüne tabidir.** Varsayılan davranış: son `FinancialParty`, başlıktaki `bank_id` alanına yazılır. `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` tercihi etkinleştirildiğinde, her `FinancialParty` girişi `supplier_account` içine kaydedilir (IBAN, hesap kimliği, para birimi kodu, tercih göstergesi).
- **İsteğe bağlı CONO son eki kesimi.** Bazı M3 kurulumları şirket numarasına bir bölüm soneki ekler (örn. `100_01`). `EXCLUDE_DIVISION_FOR_CUSTOMER_NUMBER` tercihi, DocBits anahtarlarının tutarlı kalması için `_*` soneklerini keser.

## Sync.SupplierPartyMaster

→ DocBits Ana Veri Tablosu: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//SupplierPartyMaster/PartyIDs/ID",
            "variationID": "//SupplierPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//SupplierPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//SupplierPartyMaster/PartyIDs/TaxID",
            "paymentTermId": "//SupplierPartyMaster/PaymentTermID",
            "paymentMethodCode": "//SupplierPartyMaster/PaymentMethodCode",
            "buyerPersonReferenceId": "//SupplierPartyMaster/BuyerPersonReference/IDs/ID",
            "buyerPersonReference": "//SupplierPartyMaster/BuyerPersonReference/Name",
            "supplier_category": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Categories']",
            "supplier_group": "//SupplierPartyMaster/Classification/Codes/Code[@listID='Supplier Group']",
            "discount_terms_description": "//SupplierPartyMaster/UserArea/Property/NameValue[@name='eam.UDFCHAR06']",
            "status": "//SupplierPartyMaster/Status/Code",
            "bank_id": "//SupplierPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
        }
```

### Alan referansı

| DocBits alanı | M3 kaynağı | Açıklama |
|---|---|---|
| `sharedCONO` | M3 şirket numarası | `supplier_header` içinde `customer_number` ile eşleşir. Eşleştirme anahtarının parçası. |
| `sharedSUNO` | `CIDMAS.IDSUNO` | M3 tedarikçi numarası. Eşleştirme anahtarının parçası. |
| `variationID` | BOD özniteliği | `variation_id_supplier_bod` olarak saklanır. Gelen BOD'lar yalnızca `variationID` değerleri saklı değeri aşarsa kabul edilir. Eksik bir öznitelik `0` olarak ele alınır (force-update). |
| `supplierName` | `CIDMAS.IDSUNM` | Tedarikçi görüntüleme adı. |
| `phone` | `CIDMAS.PHNO/PHN2/IDTFNO` | `Phone` iletişim kanalından telefon numarası. |
| `vatNo` | `CIDMAS.IDVRNO` | KDV tanımlayıcısı. `PartyIDs/TaxID` üzerinden okunur (M3 içe aktarma yolunda `@schemeName` filtresi yok). |
| `paymentTermId` | `CIDVEN.IITEPY` | Ödeme koşulları tanımlayıcısı. |
| `paymentMethodCode` | — | Sağlandığında ödeme yöntemi kodu. |
| `buyerPersonReferenceId` / `buyerPersonReference` | `CIDVEN.IIBUYE` / `CSYUSR.CRRENM` | Atanmış alıcı (M3 kullanıcı referansı ve görüntüleme adı). |
| `supplier_category` | — | `Classification/Codes/Code[@listID='Supplier Categories']` üzerinden okunur. Müşteriye özgü UserArea uzantısı; standart M3 kurulumlarında NULL. |
| `supplier_group` | `CIDVEN.IISUCL` | Tedarikçi sınıflandırma grubu. |
| `discount_terms_description` | — | DocBits'in iskonto tarihi hesaplayıcısı tarafından kullanılan müşteriye özgü UserArea uzantısı (`eam.UDFCHAR06`). Tedarikçi burada iskonto günü değeri verdiğinde, DocBits onu fatura tarihiyle birleştirerek AP ekibi için bir iskonto vade tarihi üretir. |
| `status` | `CIDMAS.IDSTAT` | Tedarikçi aktif/pasif durumu, `SupplierPartyMaster/Status/Code` üzerinden. |
| `bank_id` | `CBANAC.BCBKNO` | Varsayılan banka hesabı, *son* `FinancialParty` üzerinden. Her `FinancialParty`'yi `supplier_account` tablosuna senkronize etmek için `ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` özelliğini etkinleştirin. |

## Sync.RemitToPartyMaster

→ DocBits Ana Veri Tablosu: **SUPPLIER**

```python
header_mappings = {
            "sharedCONO": "//DataArea/Sync/AccountingEntityID",
            "sharedSUNO": "//RemitToPartyMaster/PartyIDs/ID",
            "variationID": "//RemitToPartyMaster/PartyIDs/ID/@variationID",
            "supplierName": "//RemitToPartyMaster/Name",
            "phone": '//Communication[ChannelCode="Phone"]/DialNumber',
            "vatNo": "//RemitToPartyMaster/PartyIDs/TaxID",
            "bank_id": "//RemitToPartyMaster/FinancialParty[last()]/FinancialAccount/ID",
            "status": "//RemitToPartyMaster/Status/Code",
        }
```

### Alan referansı

| DocBits alanı | M3 kaynağı | Açıklama |
|---|---|---|
| `sharedCONO` / `sharedSUNO` | M3 şirketi / `CIDMAS.IDSUNO` | `SupplierPartyMaster` ile aynı semantik. Aynı `supplier_header` satırına bağlanır. |
| `variationID` | BOD özniteliği | `variation_id_remit_to_party` olarak saklanır — SupplierPartyMaster `variationID`'sinden bağımsız olarak izlenir. |
| `supplierName` | `CIDMAS.IDSUNM` | Remit-to tarafının görüntüleme adı. Paylaşılan `supplier_name` sütununa yazar. |
| `phone` | `CIDREF.IRPHNO` | Remit-to iletişim bloğundan telefon numarası. |
| `vatNo` | `CIDMAS.IDCORG` | Remit-to tarafının KDV tanımlayıcısı. |
| `bank_id` | `CBANAC.BCBKNO` | Remit-to banka hesabı (`FinancialParty[last()]`). Aynı çoklu banka tercihi geçerlidir. |
| `status` | `CIDMAS.IDSTAT` | Remit-to tarafının aktif/pasif durumu. |

## İki BOD'un paylaşılan `SUPPLIER` tablosunda nasıl etkileşimde bulunduğu

Her iki BOD da aynı `supplier_header` satırını doldurur. Paylaştıkları alanlar için (`supplierName`, `phone`, `vatNo`, `bank_id`, `status`), DocBits aşağıdaki kuralları uygular:

1. Satırı `(customer_number = sharedCONO, supplier_number = sharedSUNO)` üzerinden bul.
2. Gelen `variationID` değerini *aynı BOD türü için* saklı `variationID` ile karşılaştır.
3. Gelen `variationID` daha büyükse (veya `0`, force-update), o BOD'a ait alanları güncelle. Aksi takdirde BOD'u at.
4. Diğer BOD türünün `variationID`'sine dokunulmaz; daha önce saklanmış değerleri yerinde kalır.

Tedarikçiyle ilişkili `supplier_address` ve `supplier_account` satırları güncellemede silinir ve yeniden eklenir; böylece ikincil tablolar her zaman en son BOD'u yansıtır.

## Sık sorulan sorular

### Tüm tedarikçilerim tek bir M3 şirketinden geliyorsa DocBits CONO'yu neden takip ediyor?

CONO yönlendirmesi zorunludur çünkü DocBits tasarım gereği multi-tenant'tır: Bir organizasyon birden fazla M3 şirketinden BOD alabilir. CONO eşleştirme anahtarının bir parçasıdır; böylece farklı şirketlerden tedarikçiler çakışmaz. Tek şirketiniz varsa değeri yok sayabilirsiniz; ancak anahtar sütunu yine de doldurulur.

### Her iki BOD da aynı tedarikçi satırına yazıyor — son BOD her şeyin üzerine mi yazıyor?

Hayır. Her BOD türü yalnızca gönderdiği alanlara sahiptir ve güncellemeler bağımsız bir `variationID` ile yönetilir. Yalnızca tedarikçi adını değiştiren bir SupplierPartyMaster, sonraki bir RemitToPartyMaster'ın yazmış olduğu telefon numarasını geri almaz.

### `Supplier Categories` ve `eam.UDFCHAR06` M3'üm tarafından hiç teslim edilmiyor — ne yapmalıyım?

Her ikisi de müşteriye özel UserArea uzantılarıdır. Uzantı olmadan sütunlar NULL kalır ve hiçbir DocBits özelliği bunlara bağlı değildir. İskonto tarihi mantığını yalnızca M3'ünüz `eam.UDFCHAR06` yayacak şekilde yapılandırıldığında etkinleştirin.

### `vatNo`, `schemeName='TaxIdentificationNumber'` üzerinde filtrelemeli mi?

M3 BOD içe aktarma yolu şu anda `PartyIDs/TaxID` değerini `schemeName` filtresi olmadan okur. Filtre, e-fatura XSLT yollarında (Facturae, XRechnung, KSeF) kullanılır, M3 içe aktarmasında değil. M3'ünüz farklı `schemeName` öznitelikleriyle birden fazla TaxID öğesi yayıyorsa, filtresiz davranışa güvenmeden önce bir örnek BOD ile bizimle iletişime geçin.

### Sadece sonuncusunu değil, her tedarikçi banka hesabını senkronize etmek istiyorum. Nasıl?

`ALLOW_MULTIPLE_SUPPLIER_ACCOUNTS_SYNC` tercihini etkinleştirin. Bayrak etkinken, BOD'daki her `FinancialParty`, `supplier_account` tablosuna kaydedilir (IBAN, finansal hesap kimliği, para birimi kodu, tercih göstergesi). Başlıktaki eski `bank_id` sütunu, geriye dönük uyumluluk için son girişi tutmaya devam eder.

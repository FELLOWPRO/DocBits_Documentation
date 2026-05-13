# Purchase Order BOD Eşleme

Bu sayfa, DocBits'in Infor M3 `SyncPurchaseOrder` BOD'larını nasıl içe aktardığını ve alanları dahili `PURCHASE_ORDER_HEADER` ve Purchase Order Line tablolarına nasıl eşlediğini belgeler.

{% file src="../../../../.gitbook/assets/Sync.PurchaseOrder.pdf" %}
Orijinal BOD eşleme referansı (PDF)
{% endfile %}

## Temel ilkeler

- **DocBits'te para birimi dönüşümü yoktur.** Tutarlar, M3 tarafından BOD'da iletildiği şekliyle, kendi `@currencyID`'leriyle birlikte saklanır. Üç başlık tutarı mevcuttur: `ExtendedAmount` (işlem para birimi), `ExtendedBaseAmount` (şirket temel para birimi), `ExtendedReportAmount` (raporlama para birimi).
- **DocBits'te ölçü birimi dönüşümü yoktur.** Miktarlar kendi `@unitCode` değerleriyle saklanır. `ReceivedBaseUOMQuantity`, M3 tarafından önceden hesaplanmış temel UoM değeridir — DocBits onu olduğu gibi saklar.
- **Başlık durumu mevcut olduğunda SXE aşamasından alınır.** DocBits `UserArea/Property[@name='poeh.stagecd']` özelliğini okur (değerler `1..8` → Ordered / Entered / Released / Allocated / Picked / Delivered / Invoiced / Cancelled) ve bunu otoriter başlık durumu olarak kullanır. Standart `Status/Code` da referans olarak saklanır.
- **Kısmi miktar için otomatik durum mantığı yoktur.** DocBits, alınan vs. sipariş edilen miktarlardan bir durum çıkarmaz; M3 tarafından iletilen durum 1:1 alınır.
- **`CONO`/`AccountingEntityID` PurchaseOrder BOD'unun bir parçası değildir.** Şirket numarası yönlendirmesi tedarikçi ana verilerine uygulanır (bkz. [Supplier BOD Eşleme](supplier-bod-mapping.md)); satın alma siparişleri `LocationID` üzerinden atanır.

## Başlık Eşleme

→ DocBits Ana Veri Tablosu: **PURCHASE\_ORDER\_HEADER**

```python
header_mappings = {
            "purchase_order_number": "//DataArea/PurchaseOrder/PurchaseOrderHeader/DocumentID/ID",
            "warehouse_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ShipToParty/Location[@type='Warehouse']/ID",
            "location_id": "//DataArea/Sync/LocationID",
            "status": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Status/Code",
            "supplier_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/PartyIDs/ID",
            "supplier_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/SupplierParty/Name",
            "order_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/OrderDateTime",
            "requested_shipment_date": "//DataArea/PurchaseOrder/PurchaseOrderHeader/RequiredDeliveryDateTime",
            "total_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "buyer_contact_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/ID",
            "buyer_contact_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CustomerParty/BuyerContact/Name",
            "order_last_modified_by": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationPerson/IDs/ID",
            "order_last_modified_on": "//DataArea/PurchaseOrder/PurchaseOrderHeader/LastModificationDateTime",
            "disponent_id": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/IDs/ID",
            "disponent_name": "//DataArea/PurchaseOrder/PurchaseOrderHeader/PlannerReference/Name",
            "extended_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedAmount",
            "extended_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedBaseAmount",
            "extended_report_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/ExtendedReportAmount",
            "canceled_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledAmount",
            "canceled_base_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledBaseAmount",
            "canceled_reporting_amount": "//DataArea/PurchaseOrder/PurchaseOrderHeader/CanceledReportingAmount",
            "type_code": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification/Codes/Code[@listID='Purchase Order Types']",
            "type_description": "//DataArea/PurchaseOrder/PurchaseOrderHeader/Classification[Codes/Code[@listID='Purchase Order Types']]/Description",
            "sxe_stage": "//DataArea/PurchaseOrder/PurchaseOrderHeader/UserArea/Property/NameValue[@name='poeh.stagecd']/text()",
        }
```

### Başlık alan referansı

| DocBits alanı | M3 kaynağı | Açıklama |
|---|---|---|
| `purchase_order_number` | `MPHEAD.IAPUNO` | M3 satın alma sipariş numarası, birincil anahtar. |
| `warehouse_id` | — | `ShipToParty/Location[@type='Warehouse']/ID` değerini okur. `@type='Warehouse'` özniteliği M3 tarafından nadiren ayarlanır; bu durumda alan NULL kalır. M3 yerel deposu için `location_id` kullanın. |
| `location_id` | `MPHEAD.IAFACI` | BOD'un oluşturulduğu M3 bölümü/tesisi (depo). DocBits içinde organizasyon/tesis yönlendirmesi için kullanılır, fatura tesisleriyle eşleştirme dahil. |
| `status` | `MPHEAD.IAPUSL` | BOD'dan ham `Status/Code`. `sxe_stage` boş olduğunda yedek olarak kullanılır. |
| `sxe_stage` | `MPHEAD.IAPUSL` | UserArea özelliği `poeh.stagecd` üzerinden okunan otoriter başlık durumu. M3 SXE aşama kodları 1..8 → Ordered, Entered, Released, Allocated, Picked, Delivered, Invoiced, Cancelled olarak eşler. Ayarlandığında, iş akışı kararları için `status` üzerinde önceliklidir. `UPDATE_DOCUMENT_PURCHASE_ORDER_STATUS` tercihi etkinleştirildiğinde, DocBits bu durumu bağlı faturalara yayar. |
| `supplier_id` | `MPHEAD.IASUNO` | Satın alma siparişindeki tedarikçi numarası. |
| `supplier_name` | `CIDMAS.IDSUNM` | Tedarikçi görüntüleme adı. |
| `order_date` | `MPHEAD.IAPUDT` | Satın alma siparişinin M3'te oluşturulma tarihi. |
| `requested_shipment_date` | — | Mevcutsa başlık seviyesindeki `RequiredDeliveryDateTime` değerinden okunur. Çoğu M3 kurulumu bunu yalnızca satırda tutar; bu durumda satır seviyesindeki `requested_ship_date` kullanın. |
| `total_amount` | `MPHEAD.IAOURR` | İşlem para biriminde sipariş toplamı. `ExtendedAmount`'tan 1:1 saklanır. |
| `extended_amount` | `MPHEAD.IAOURR` | `total_amount` ile aynı kaynak. İzlenebilirlik ve kanonik BOD yolunu bekleyen aşağı akış tüketicileri için ayrı bir ham sütun olarak tutulur. |
| `extended_base_amount` | `MPHEAD.IAOUVA` | Şirket temel para birimi cinsinden toplam. M3 mevcut olduğunda doldurur. |
| `extended_report_amount` | `MPHEAD.IAOUVB` | Şirket raporlama para birimi cinsinden toplam. |
| `canceled_amount` / `canceled_base_amount` / `canceled_reporting_amount` | — | İşlem/temel/raporlama para birimlerinde iptal tutarları. M3 yalnızca iptal olaylarından sonra doldurur. |
| `type_code` / `type_description` | — | `Classification/Codes/Code[@listID='Purchase Order Types']` (ve `Description`) üzerinden satın alma siparişi türü. Örnekler: `P10` normal PO, `P20` stok ikmal PO. Yalnızca görüntüleme için saklanır — filtreleme mantığı yok. |
| `buyer_contact_id` / `buyer_contact_name` | `MPHEAD.IABUYE` / bağlı kullanıcı | PO'ya atanmış alıcı. |
| `order_last_modified_by` / `order_last_modified_on` | `MPHEAD.IACHID` / `MPHEAD.IALMDT` | Denetim alanları. |
| `disponent_id` / `disponent_name` | `MPHEAD.IARESP` / bağlı kullanıcı | Planlayıcı referansı. |

## Satır Eşleme

→ DocBits Ana Veri Tablosu: **Purchase Order**

```python
line_mappings = {
        "sub_line_number": "SubLineNumber",
        "item_id": [
            "Item/ItemID/ID[not(@schemeName)]",
            "Item/ItemID/ID[@schemeName='NonStock']",
        ],
        "supplier_item_id": [
            "Item/ItemID/ID[@schemeName='Supplier']",
            "Item/Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']",
            "Item/SupplierItemID/ID",
        ],
        "schedule_line_number ": "DocumentReference/ScheduleLineNumber",
        "description": "Item/Description",
        "note": "Note",
        "quantity": "Quantity",
        "open_quantity": "OpenQuantity",
        "confirmed_quantity": "BackOrderedQuantity",
        "received_quantity": "ReceivedQuantity",
        "received_base_mou_quantity": "ReceivedBaseUOMQuantity",
        "unit_of_measure": "Quantity/@unitCode",
        "unit_price": "UnitPrice/Amount",
        "unit_price_per": "UnitPrice/PerQuantity",
        "unit_code_price": "UnitPrice/PerQuantity/@unitCode",
        "total_amount": ["TotalAmount", "ExtendedAmount"],
        "extended_amount": "ExtendedAmount",
        "currency": ["TotalAmount/@currencyID", "ExtendedAmount/@currencyID"],
        "buyer_id": "BuyerParty/PartyIDs/ID",
        "buyer_name": "BuyerParty/Name",
        "status": "Status/Code",
        "geo_code": "UserArea/Property/NameValue[@name='GeoCode']",
        "delivery_method": "UserArea/Property/NameValue[@name='m3.DeliveryMethod']",
        "order_multiple": "Classification/Codes/Code[@listID='Order multiple']",
        "standard_quantity": "UserArea/Property/NameValue[@name='StandardQuantity']",
        "promised_delivery_date": "PromisedDeliveryDateTime",
        "requested_ship_date": "RequiredDeliveryDateTime",
    }
```

### Satır alan referansı

| DocBits alanı | M3 kaynağı | Açıklama |
|---|---|---|
| `item_id` | `MPLINE.IBITNO` | M3 madde numarası. Stok dışı maddeler için `@schemeName='NonStock'` yedeklemesi. |
| `supplier_item_id` | `MPLINE.IBSITE` / Classification | Tedarikçi tarafı madde numarası. Sırayla üç yedekleme ile çözülür: `ID[@schemeName='Supplier']` → `Classification[@type='Supplier Item Code']/Codes/Code[@listID='Supplier Item Code']` → `Item/SupplierItemID/ID`. |
| `description` | `MPLINE.IBPITT` | Satır madde açıklaması. |
| `note` | `MSYTXL.TLTX60` | Satır not metni. |
| `quantity` | `MPLINE.IBORQA` | Sipariş edilen miktar. `unit_of_measure` ile saklanır (dönüşüm yok). |
| `open_quantity` | `CFQA - RVQA` | Hâlâ açık olan miktar (sipariş - alınan). Aynı `unit_of_measure`. |
| `confirmed_quantity` | — | Tedarikçi tarafından onaylanan miktar. M3 boş bırakır; `BackOrderedQuantity` yayan ERP'ler tarafından doldurulur. |
| `received_quantity` | `MPLINE.IBRVQA` | Mal kabul miktarı. |
| `received_base_mou_quantity` | `MPLINE.IBRVQA` (temel UoM) | M3'ün kendisi tarafından temel ölçü birimine dönüştürülmüş alınan miktar. DocBits hesaplamaz — M3'ün gönderdiğini saklar. Stok muhasebesi için yararlı. |
| `unit_of_measure` | `MPLINE.IBPUUN` | İşlem UoM. `quantity`, `open_quantity`, `received_quantity` için geçerli. |
| `unit_price` | `MPLINE.IBPUPR` | İşlem para biriminde birim fiyat. |
| `unit_price_per` / `unit_code_price` | `MPLINE.IBCPUC` / `MPLINE.IBPPUN` | Birim başına fiyat ve birim kodu (fiyat değiştirici, örn. 100 PCS başına fiyat). |
| `total_amount` | `LNAM + EXEP` | Satır toplamı. `[TotalAmount, ExtendedAmount]` yedeklemesiyle çözülür — `TotalAmount` yoksa `total_amount`, `extended_amount`'a eşittir. İkisi de mevcutsa, `TotalAmount` vergi/iskonto içerebilir; `extended_amount` ise `quantity × unit_price` değeridir. |
| `extended_amount` | `LNAM` / `LNA2` | Ham `ExtendedAmount` (vergisiz/iskontosuz satır ara toplamı). |
| `currency` | `MPHEAD.IACUCD` | İşlem para birimi. `TotalAmount/@currencyID` üzerinden, yedek olarak `ExtendedAmount/@currencyID`. |
| `status` | `MPLINE.IBPUST` | Satır durumu. Raporlama için saklanır; hiçbir DocBits iş akışı bundan türetilmez. |
| `buyer_id` / `buyer_name` | `MPLINE.IBBUYE` / bağlı kullanıcı | Satır düzeyinde alıcı. `buyer_name` satırda M3 tarafından nadiren doldurulur; tedarikçi alıcı referansı [Supplier BOD Eşleme](supplier-bod-mapping.md) içindedir. |
| `geo_code` | — | US/CA vergi motorları için coğrafi kod. Yalnızca onu yayan ERP'ler tarafından doldurulur. |
| `delivery_method` | `MPLINE.IBMODL` | Satır teslimat yöntemi (M3 `MODL` kodu). |
| `promised_delivery_date` | `CODT, DWDT/TIHM` | Tedarikçi tarafından onaylanan teslimat tarihi. |
| `requested_ship_date` | `MPLINE.IBDWDT` | Satırdaki talep edilen sevkiyat tarihi — operasyonel olarak ilgili istenen teslim tarihi. |
| `sub_line_number` | — | İsteğe bağlı alt satır tanımlayıcısı. Mevcutsa saklanır; M3 genellikle boş bırakır. |
| `schedule_line_number` | — | Planlı teslimatlı PO'lar için isteğe bağlı çizelge satırı referansı. |
| `order_multiple` / `standard_quantity` | `MPLINE.IBOMUL` / UserArea | Satır sipariş katı (minimum sipariş miktarı) ve standart ambalaj miktarı. |

## Sık sorulan sorular

### DocBits yabancı para biriminde satın alma siparişlerini nasıl ele alır?

DocBits para birimlerini dönüştürmez. İşlem tutarı (`total_amount`, `extended_amount`, `unit_price`) kendi `@currencyID`'siyle birlikte saklanır. Şirket farklı bir temel veya raporlama para birimi kullandığında, M3 önceden dönüştürülmüş değerleri `extended_base_amount` ve `extended_report_amount` üzerinden sağlar — bunlar başlıkta ek sütunlar olarak saklanır.

### DocBits kısmi alındı durumunu nasıl türetir?

Türetmez. Başlık durumu, BOD yayınlandığı andaki M3 SXE aşamasını (`poeh.stagecd`) yansıtır. Kısmi alındı göstergesi gerekiyorsa, satır tablosunda `open_quantity` vs. `quantity` üzerinden türetin.

### Satırda `total_amount` ile `extended_amount` arasındaki fark nedir?

Her iki sütun da tarihsel/UI uyumluluk için bulunur. `total_amount`, `[TotalAmount, ExtendedAmount]` üzerinden çözülür; yani `TotalAmount` yoksa `extended_amount`'a eşittir. M3 ikisini de yaydığında, `TotalAmount`, `extended_amount`'ta tutulan `quantity × unit_price` değerinin üzerine vergi veya iskonto ekleyebilir.

### Depo neden iki farklı yola eşleniyor?

`warehouse_id`, çoğu M3 kurulumunun boş bıraktığı `ShipToParty/Location[@type='Warehouse']/ID` değerini okur (`@type` özniteliği nadiren ayarlanır). `location_id`, M3 tarafından her zaman doldurulan ve PO'nun ait olduğu bölüm/tesisi temsil eden `DataArea/Sync/LocationID` değerini okur. `location_id`'yi M3 yerel depo tanımlayıcısı olarak değerlendirin.

### Bazı alanlar belgeli ama her zaman boş (`buyer_name`, `geo_code`, `confirmed_quantity`, `sub_line_number`, …). Neden eşleniyor?

Bu eşlemeler savunma amaçlıdır: BOD şeması alanlara izin verir ve diğer ERP'ler veya özelleştirilmiş M3 uzantıları bunları doldurabilir. M3 onları boş bıraktığında, sütunlar DocBits'te basitçe NULL olur.

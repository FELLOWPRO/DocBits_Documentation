# Ana Veri Arama

{% embed url="https://youtu.be/hn_bkeUMxJg" %}
{% endembed %}

**Ana Veri Arama** (kenar çubuğu: **Lookup Master Data**), DocBits'in belgelerden çıkarılan verileri ERP sisteminizle doğrulamak için kullandığı ana verileri görüntülemenizi ve yönetmenizi sağlar. Doğru PO matching, tedarikçi doğrulaması ve alanların otomatik tamamlanması için gereklidir. **Ayarlar → Belge İşleme → Lookup Master Data** üzerinden açın.

<figure><img src="../../../.gitbook/assets/master_data_lookup_overview.png" alt="Ana Veri Arama"><figcaption><p>Ana Veri Arama sayfası – veri kaynakları ve veri tablosu</p></figcaption></figure>

## Veri Kaynakları

Sol panel dört veri kaynağı kategorisini listeler:

| Kaynak | Açıklama |
|--------|----------|
| **BOD Input Data** | Infor BOD (Business Object Document) mesajları aracılığıyla alınan veriler. |
| **ERP API Data** | ERP sisteminizden bir API aracılığıyla doğrudan alınan veriler. API bağlantısını yapılandırmak için dişli simgesine tıklayın. |
| **Imported** | Manuel olarak içe aktarılan veriler (örneğin CSV yükleme yoluyla). Yeni veri eklemek için **+** simgesine tıklayın. |
| **DocBits Master Data** | DocBits içinde yönetilen dahili ana veriler. |

## Veri Tablosu

Bir veri kaynağı seçildiğinde, verileri sağ tarafta aranabilir ve sıralanabilir bir tabloda açılır:

* **Sekmeler** – her sekme bir ana veri türüdür (örneğin Tedarikçi, Satınalma Siparişi, Kalem).
* **Arama** – sütuna göre filtreleyin (**Search by column**) veya metne göre arayın (**Search String**).
* **Eylemler** – sütun etiketlerini güncelleyin, boş sütunları gizleyin, takma adları güncelleyin veya verileri CSV olarak indirin.
* **Sayfalama** – sayfa denetimleriyle büyük veri kümelerinde gezinin.

Tedarikçi ve Satınalma Siparişi tabloları; Tedarikçi Kimliği, Tedarikçi Adı, Adres, Bank Id, PO Numarası, Kalem Kimliği, Açıklama, Miktar, Birim Fiyat, Toplam Tutar, Para Birimi ve Durum gibi sütunların yanı sıra özel alanları da içerir.

## Ayarlar

Ana veri ayarlarını açmak için veri kaynakları panelinin sol alt köşesindeki **Settings** (dişli simgesi) öğesine tıklayın.

<figure><img src="../../../.gitbook/assets/master_data_lookup_settings.png" alt="Ana Veri Arama ayarları"><figcaption><p>Supplier BOD ve satınalma siparişi silme ayarları</p></figcaption></figure>

### Supplier BOD

**Allow Multiple Supplier Accounts Sync**

* **Etkin**: tek bir tedarikçinin BOD'da birden fazla `<FinancialParty>` öğesi olabilir (genellikle birden fazla IBAN veya finansal hesap nedeniyle). Tüm `<FinancialParty>` girişleri çıkarılır ve tedarikçi tablosuna kaydedilir, böylece birden fazla finansal öznitelik saklanabilir.
* **Devre dışı**: tedarikçi için bulunan yalnızca son `<FinancialParty>` öğesi çıkarılır. Önceki finansal öznitelikler (örneğin ek IBAN'lar) yok sayılır ve yalnızca son oluşumun verileri kaydedilir.

### Purchase Order Deletion Assistant

**Delete Purchase Order After** – kapatılmış satınalma siparişlerinin ne zaman kaldırılacağını seçin. Seçilen süre sonunda kayıtlar otomatik olarak silinir.

{% hint style="info" %}
DocBits'e ana verilerin nasıl yükleneceğini öğrenmek için bkz. [Ana verileri içe aktarma](../../../infor-integration-and-configuration/importing-customer-master-data/).
{% endhint %}

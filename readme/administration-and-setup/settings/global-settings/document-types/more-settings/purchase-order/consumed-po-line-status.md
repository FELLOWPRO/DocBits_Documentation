# Consumed PO Line Status

Bu ayar, bir fatura satırının bir Satın Alma Siparişi (PO) satırına eşleştirilip eşleştirilmediğini gösteren **Eşleşen Miktar** değerinin, PO satırının durumunu güncelleyip güncellemeyeceğini belirler.

<figure><img src="../../../../../../.gitbook/assets/consumed-po-line-status-settings-tr.png" alt="Satın alma emri ayarları bölümünde Tüketilen PO satır durumu anahtarı" width="750"><figcaption><p>Satın alma emri ayarlarında <strong>Tüketilen PO satır durumu</strong> anahtarı</p></figcaption></figure>

Kapalıyken (varsayılan), PO satırının durumu eşleştirmeden etkilenmez.

<figure><img src="../../../../../../.gitbook/assets/consumed-po-line-status-toggle-tr.png" alt="Açık konumdaki Tüketilen PO satır durumu anahtarı" width="750"><figcaption><p>Tüketilen PO satır durumu açıkken</p></figcaption></figure>

Açıkken, bir fatura satırı bir PO satırına eşleştirildiğinde ve **Eşleşen Miktar** PO miktarına ulaştığında, PO satırının durumu otomatik olarak **Consumed** olarak güncellenir.

PO Eşleştirme ekranındaki **Eşleşen Miktar** sütunu, bir PO satırına eşleştirilen miktarı gösterir. Ayar açıkken bu değer PO miktarına ulaştığında satır **Consumed** olarak işaretlenir.

## Etki alanı

Bu ayar yalnızca PO satırlarının durumunu etkiler. Fatura durumunu, PO eşleştirme sonuçlarını ve PO satırının durumunu elle değiştirmenizi etkilemez.

## İlgili ayarlar

* [Purchase Order Matching Rules](purchase-order-matching-rules.md)
* [Calculate PO Unit Price](calculate-po-unit-price.md)

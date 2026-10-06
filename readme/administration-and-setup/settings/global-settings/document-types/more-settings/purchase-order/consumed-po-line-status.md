# Consumed PO Line Status

Bu ayar, bir fatura satırının bir Satın Alma Siparişi (PO) satırına eşleştirilip eşleştirilmediğini gösteren **Eşleşen Miktar** değerinin, PO satırının durumunu güncelleyip güncellemeyeceğini belirler.

<figure><img src="../../../../../../.gitbook/assets/consumed-po-line-status-off-tr-20261006.png" alt="Daha fazla ayar bölümünde Tüketilen PO satır durumu anahtarı kapalı" width="375"><figcaption><p>Tüketilen PO satır durumu kapalıyken</p></figcaption></figure>

Kapalıyken (varsayılan), PO satırının durumu eşleştirmeden etkilenmez.

<figure><img src="../../../../../../.gitbook/assets/consumed-po-line-status-on-tr-20261006.png" alt="Daha fazla ayar bölümünde Tüketilen PO satır durumu anahtarı açık" width="375"><figcaption><p>Tüketilen PO satır durumu açıkken</p></figcaption></figure>

Açıkken, bir fatura satırı bir PO satırına eşleştirildiğinde ve **Eşleşen Miktar** PO miktarına ulaştığında, PO satırının durumu otomatik olarak **Consumed** olarak güncellenir.

<figure><img src="../../../../../../.gitbook/assets/consumed-po-line-status-matching-tr-20261006.png" alt="PO Eşleştirme ekranında Eşleşen Miktar sütunu" width="750"><figcaption><p>PO Eşleştirme ekranındaki <strong>Eşleşen Miktar</strong> sütunu</p></figcaption></figure>

PO Eşleştirme ekranındaki **Eşleşen Miktar** sütunu, bir PO satırına eşleştirilen miktarı gösterir. Ayar açıkken bu değer PO miktarına ulaştığında satır **Consumed** olarak işaretlenir.

## Etki alanı

Bu ayar yalnızca PO satırlarının durumunu etkiler. Fatura durumunu, PO eşleştirme sonuçlarını ve PO satırının durumunu elle değiştirmenizi etkilemez.

## İlgili ayarlar

* [Purchase Order Matching Rules](purchase-order-matching-rules.md)
* [Calculate PO Unit Price](calculate-po-unit-price.md)

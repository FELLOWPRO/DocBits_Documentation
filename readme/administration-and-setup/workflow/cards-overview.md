# Cards

Kartlar, her iş akışının yapı taşlarıdır. Bir iş akışının ne zaman çalışacağını ve ne yapacağını tanımlamak için onları **When / And / Then** gruplarında birleştirirsiniz. Bu bölüm, kullanılabilir kartları ve her birinin ne yaptığını açıklar.

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — kartlar kategoriye göre gruplandırılmıştır.</p></figcaption></figure>

## Kart grupları

- **When** — bir iş akışını başlatan tetikleyici kartlar (örn. document type, document type one of).
- **And** — eylemler çalışmadan önce ayrıca doğru olması gereken koşul kartları. Bunlar *Compare with Purchase Order* (PO eşleştirme), *Document Field* karşılaştırmaları, *Date & Time*, *Logic*, *Status*, *Table* ve *Assignee* koşullarını içerir.
- **Then** — işi yapan eylem kartları: alanları ayarlama, onaylama/reddetme, durum değiştirme, dışa aktarma, görev oluşturma, belge atama, tabloları işleme ve eylemleri çalıştırma (Call API, Send HTTPS request, Run Workflow, AI hesaplamaları).

## Kart referans kılavuzları

Her kartın ve seçeneklerinin eksiksiz bir referansı için, bu bölümdeki *complete guide* sayfalarına bakın (Condition Cards, PO Matching Cards, Assignment & User Cards, Task Cards, Field & Table Cards ve Action kartları).

## Kartları birleştirme

Yaygın iş senaryolarını çözen kanıtlanmış kart kombinasyonlarını görmek için **Workflow Pattern Guides**'a bakın.

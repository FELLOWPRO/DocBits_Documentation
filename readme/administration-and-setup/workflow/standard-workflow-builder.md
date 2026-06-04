# Standard Workflow

**Standard Workflow** oluşturucusu, belge işlemeyi otomatikleştirmek için doğrusal, kart tabanlı bir düzenleyicidir. Bir iş akışı üç kart grubundan oluşur — **When** (tetikleyici), **And** (ek koşullar) ve **Then** (çalıştırılacak eylemler). Bir belge When/And koşullarıyla eşleştiğinde, Then eylemleri otomatik olarak çalışır.

## Nasıl erişilir

**Workflow Dashboard → Workflow List**'i açın, ardından yeni bir Standard iş akışı oluşturmak için **Add Workflow**'a tıklayın veya düzenlemek için mevcut bir iş akışına tıklayın.

<figure><img src="../../.gitbook/assets/workflow_list.png" alt="Tür, yürütme sırası ve tetikleyiciyle Workflow List"><figcaption><p>Workflow List — her satır, açıp kapatabileceğiniz veya düzenleyebileceğiniz bir iş akışıdır.</p></figcaption></figure>

## When / And / Then modeli

<figure><img src="../../.gitbook/assets/workflow_designer_cards.png" alt="When, And ve Then kartlarıyla Standard Workflow tuvali"><figcaption><p>Standard Workflow tuvali. Bu örnek, bir alt kuruluştaki faturalarda tetiklenir ve onları bir kullanıcıya atar.</p></figcaption></figure>

- **When** — iş akışını başlatan tetikleyici (örn. *Document type is Invoice*).
- **And** — ayrıca doğru olması gereken ek koşullar (örn. *Document is part of sub-organization*). When kartının her eşleşmesinde çalıştırmak için boş bırakın.
- **Then** — gerçekleştirilecek eylemler (örn. *Assign the document to the user*, bir görev oluşturma, bir API çağırma, bir e-posta gönderme).

## Kart ekleme

Kart kütüphanesini açmak için herhangi bir grupta **Add Card**'a tıklayın. Kartlar kategoriye göre düzenlenmiştir, böylece ihtiyacınız olan yapı taşını bulabilirsiniz:

<figure><img src="../../.gitbook/assets/workflow_add_card_picker.png" alt="Kategoriye göre gruplandırılmış Add Card kütüphanesi"><figcaption><p><strong>Add Card</strong> kütüphanesi — koşul kartları, karşılaştırma kartları, eylem kartları ve daha fazlası, kategoriye göre gruplandırılmıştır.</p></figcaption></figure>

**Save Workflow** ile kaydedin veya düzeni **Save Template** ile yeniden kullanılabilir bir şablon olarak kaydedin.

## Sonraki adımlar

- Her kartın ne yaptığını **Cards** bölümünde görün.
- Kartları **Workflow Pattern Guides** ile kanıtlanmış çözümler halinde birleştirin.
- Paralel yollu dallanan akışlar (Wait ALL / Wait ANY / OR) için **Advanced Workflow** oluşturucusunu kullanın.

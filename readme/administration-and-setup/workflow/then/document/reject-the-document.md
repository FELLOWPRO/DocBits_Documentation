# Reject the Document

<figure><img src="../../../../.gitbook/assets/image (282).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Reject the Document"** iş akışı kartı, bir iş akışı içinde bir belgeyi reddedilmiş olarak işaretlemek için kullanılır. Bu eylem, belgenin ilerlemesini durdurur ve iş akışındaki bir sonraki aşamaya geçmesini engeller. Gerekli koşulları veya ölçütleri karşılamayan belgelerin işaretlenmesini ve daha fazla işlenmesinin engellenmesini sağlar.

## **Kartın Bileşenleri:**

1. **Reddetme Durumu (Rejection Status)**
   * **Açıklama**: Bu bileşen belgeyi reddedilmiş olarak işaretler ve onay için gerekli koşulları karşılamadığını gösterir.
   * **Ayrıntı**: Tetiklendiğinde, bu kart belgenin durumunu "reddedildi" olarak günceller. Bu karar, **"Where"** ve **"And Bölümleri"**nde ayarlanan koşullara göre verilir.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, **"Where"** ve **"And Bölümleri"**nde ayarlanan koşulları değerlendirir.
  * **Her iki koşul da doğruysa**, belge reddedilir.
  * **Koşullardan biri yanlışsa**, kart yürütülmez ve belgenin durumu değişmeden kalır.
* **Eylem Yürütme**: Koşullar karşılandığında, belge reddedilmiş olarak işaretlenir. Bu eylem, yalnızca belirli ölçütleri karşılayan belgelerin ilerlemesini sağlarken, diğerlerinin inceleme veya düzeltme için işaretlenmesini ve durdurulmasını sağlar.

## **Sonuç:**

**"Reject the Document"** iş akışı kartı, otomatik süreçlerde belge akışını kontrol etmek için temel bir araçtır. Uyumlu olmayan belgelerin reddedilmesine izin vererek, yalnızca geçerli ve doğru belgelerin iş akışından devam etmesini sağlar, belge yönetiminde verimliliği ve doğruluğu artırır.

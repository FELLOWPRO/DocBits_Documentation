# Confirmed Delivery Date

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu iş akışı kartı, faturalar veya sevkiyat belgelerindeki onaylanmış teslimat tarihlerinin bir ana veri arama tablosunda tanımlanan kabul edilen teslimat tarihleriyle uyumlu olmasını doğrulamak için tasarlanmıştır. Bu tarihleri karşılaştırarak, üzerinde anlaşılan teslimat programlarına uyumu sağlamaya yardımcı olur ve tedarik zinciri güvenilirliğini artırır.

## **Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama:** Onaylanmış teslimat tarihini kabul edilen teslimat tarihiyle karşılaştırma koşulunu tanımlar.
   * **Seçenekler:**
     * **Is:** Teslimat tarihinin ana verideki kabul edilen teslimat tarihiyle eşleştiğini onaylar.
     * **Is Not:** Teslimat tarihinin ana verideki kabul edilen teslimat tarihiyle eşleşmediğini garanti eder.
2. **Ana Veri Tablosu Araması**
   * **Açıklama:** Karşılaştırma için kabul edilen teslimat tarihlerini içeren referans tablosunu belirtir.
   * **Ayrıntı:** Tablo, **Ana Veri Tablosu (Master Data Table)** parametresiyle tanımlanır ve sipariş numaraları veya teslimat bölgeleri gibi ek meta veriler içerebilir.



## **İşlevsellik**

* **Tarih Karşılaştırması:** Sistem, fatura veya sevkiyat belgesindeki onaylanmış teslimat tarihini belirtilen ana veri arama tablosundaki kabul edilen teslimat tarihiyle karşılaştırır.
* **Eylem Yürütme:** Karşılaştırma sonucuna dayanarak, kart bildirimler gibi takip eylemlerini tetikleyebilir.

## **Kurulum ve Yapılandırma**

* Bu kartı yapılandırmak için, kullanıcılar belgedeki onaylanmış teslimat tarihini temsil eden alanı seçer ve kabul edilen teslimat tarihlerini içeren ana veri arama tablosunu belirtir. Ardından, iki tarihin nasıl karşılaştırılması gerektiğini tanımlamak için bir operatör seçilir (örn. **Is** veya **Is Not**).

## **Örnek Senaryo**

* Bir fatura 10 Haziran onaylanmış teslimat tarihini listelerken, ana veri arama tablosu 15 Haziran kabul edilen teslimat tarihini belirtir. **Is Not** operatörünü kullanarak, kart tutarsızlığı inceleme için işaretler ve lojistik ekibinin nedeni araştırmasına ve programları buna göre ayarlamasına olanak tanır.

## **Sonuç**

**"Confirmed Delivery Date vs. Accepted Delivery Date"** iş akışı kartı, onaylanmış ve kabul edilen teslimat tarihlerinin karşılaştırmasını otomatikleştirerek kuruluşların üzerinde anlaşılan teslimat programlarına bağlılığı korumasına yardımcı olur. Teslimat yönetimine yönelik bu proaktif yaklaşım, operasyonel verimliliği artırır, gecikmeleri azaltır ve tedarik zinciri boyunca daha iyi işbirliğini teşvik eder.

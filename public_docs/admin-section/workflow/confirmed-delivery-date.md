# Onaylanmış Teslimat Tarihi

<figure><img src="../../../../.gitbook/assets/image (266).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç**

Bu iş akışı kartı, faturalar veya sevkiyat belgeleri üzerindeki onaylanmış teslimat tarihlerinin ana veri arama tablosunda tanımlanan kabul edilen teslimat tarihleriyle uyumlu olduğunu doğrulamak için tasarlanmıştır. Bu tarihleri karşılaştırarak, üzerinde anlaşılan teslimat programlarına uyumu sağlamaya yardımcı olur ve tedarik zinciri güvenilirliğini artırır.

## **Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama:** Onaylanmış teslimat tarihini kabul edilen teslimat tarihiyle karşılaştırma koşulunu tanımlar.
   * **Seçenekler:**
     * **DIR:** Teslimat tarihinin ana verilerdeki kabul edilen teslimat tarihiyle eşleştiğini onaylar.
     * **DEĞİLDİR:** Teslimat tarihinin ana verilerdeki kabul edilen teslimat tarihiyle eşleşmediğini sağlar.
2. **Ana Veri Tablosu Araması**
   * **Açıklama:** Karşılaştırma için kabul edilen teslimat tarihlerini içeren referans tabloyu belirtir.
   * **Detay:** Tablo, **Ana Veri Tablosu** parametresi tarafından tanımlanır ve sipariş numaraları veya teslimat bölgeleri gibi ek meta veriler içerebilir.



## **İşlevsellik**

* **Tarih Karşılaştırması:** Sistem, faturadan veya sevkiyat belgesinden alınan onaylanmış teslimat tarihini belirtilen ana veri arama tablosundaki kabul edilen teslimat tarihiyle karşılaştırır.
* **Eylem Yürütme:** Karşılaştırma sonucuna bağlı olarak kart, bildirimler gibi takip eylemlerini tetikleyebilir.

## **Kurulum ve Yapılandırma**

* Bu kartı yapılandırmak için kullanıcılar belgedeki onaylanmış teslimat tarihini temsil eden alanı seçer ve kabul edilen teslimat tarihlerini içeren ana veri arama tablosunu belirtir. Ardından, iki tarihin nasıl karşılaştırılacağını tanımlamak için bir operatör seçilir (örneğin, **DIR** veya **DEĞİLDİR**).

## **Örnek Senaryo**

* Bir fatura 10 Haziran onaylanmış teslimat tarihini listelerken, ana veri arama tablosu 15 Haziran kabul edilen teslimat tarihini belirtiyor. **DEĞİLDİR** operatörünü kullanan kart, tutarsızlığı inceleme için işaretleyerek lojistik ekibinin nedeni araştırmasına ve programları buna göre ayarlamasına olanak tanır.

## **Sonuç**

**"Onaylanmış Teslimat Tarihi - Kabul Edilen Teslimat Tarihi"** iş akışı kartı, onaylanmış ve kabul edilen teslimat tarihlerinin karşılaştırılmasını otomatikleştirerek kuruluşların üzerinde anlaşılan teslimat programlarına bağlı kalmasına yardımcı olur. Teslimat yönetimine yönelik bu proaktif yaklaşım operasyonel verimliliği artırır, gecikmeleri azaltır ve tedarik zinciri boyunca daha iyi iş birliğini teşvik eder.

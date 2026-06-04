# Start Export

<figure><img src="../../../../.gitbook/assets/image (285).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Start Export"** iş akışı kartı, bir belge için dışa aktarma sürecini başlatmak için tasarlanmıştır. Bu kart, önceki bölümlerdeki koşullar karşılandığında dışa aktarma işlemini sorunsuz bir şekilde başlatmak için iş akışı içinde bir tetikleyici olarak işlev görür.

## **Kartın Bileşenleri:**

1. **Eylem (Action)**
   1. **Açıklama**: Belge için dışa aktarma sürecini başlatır.
   2. **Ayrıntı**: Kart, belgeyi işlemek ve dışa aktarmak için sistemde yapılandırılmış dışa aktarma ayarlarını kullanır.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, iş akışının **"Where"** ve **"And Bölümleri"**nde ayarlanan koşulları değerlendirir. Tüm koşullar doğruysa, dışa aktarma süreci başlar.
* **Belge Dışa Aktarma**: Belge, varsayılan veya önceden tanımlanmış dışa aktarma yapılandırması kullanılarak işlenir ve dışa aktarılır.

## **Kurulum ve Yapılandırma:**

Bu kart, sistemde zaten tanımlanmış dışa aktarma ayarlarını kullandığından özel bir yapılandırma gerektirmez. Kullanıcıların şunlardan emin olması gerekir:

1. Kart yalnızca bu koşullar doğru olarak değerlendirilirse yürütüldüğünden, **"Where"** ve **"And Bölümleri"** koşullarının doğru yapılandırıldığından.
2. Sistemde belgeyle ilişkili geçerli bir dışa aktarma yapılandırmasının olduğundan.

## **Sonuç:**

**"Start Export"** iş akışı kartı, dışa aktarma sürecini tetiklemek için kolaylaştırılmış ve otomatik bir yol sunar. Önceden yapılandırılmış ayarlara ve koşullu değerlendirmelere dayanarak, verimli ve doğru belge işlemeyi sağlar.

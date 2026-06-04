# Export with Export Configuration

<figure><img src="../../../../.gitbook/assets/image (284).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Export Document with Export Configuration"** iş akışı kartı, bir belgeyi belirtilen bir dışa aktarma yapılandırması kullanarak dışa aktarmak için tasarlanmıştır. Belgeyle ilişkili bekleyen görevleri yok sayma esnekliği sunar ve belgenin mevcut durumundan bağımsız olarak sorunsuz bir dışa aktarma süreci sağlar.

## **Kartın Bileşenleri:**

1. **Dışa Aktarma Yapılandırması (Export Configuration)**
   * **Açıklama**: Belgeyi işlemek için kullanılacak dışa aktarma yapılandırmasını belirtir.
   * **Ayrıntı**: Bu yapılandırma, dışa aktarılan belgenin biçimini, yapısını ve hedefini belirler.
2. **Bekleyen Görevleri Yok Say (Ignore Pending Tasks)**
   * **Açıklama**: Dışa aktarma süreci sırasında belgeye bağlı bekleyen görevlerin göz ardı edilip edilmeyeceğini belirler.
   * **Seçenekler**:
     * **True**: Belgeyi bekleyen görevlerden bağımsız olarak dışa aktarır.
     * **False**: Dışa aktarmadan önce bekleyen görevlerin tamamlanmasını sağlar.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, iş akışının **"Where"** ve **"And Bölümleri"**nde ayarlanan koşulları değerlendirir. Her iki koşul da doğruysa, dışa aktarma süreci başlatılır.
* **Belge Dışa Aktarma**: Belirtilen **Dışa Aktarma Yapılandırması** kullanılarak, belge tanımlanan biçim ve hedefte işlenir ve dışa aktarılır.
* **Bekleyen Görevleri Yönetme**: **Ignore Pending Tasks** **True** olarak ayarlanırsa, dışa aktarma süreci belgeye bağlı bekleyen görevleri atlar. **False** olarak ayarlanırsa, tüm görevler çözülene kadar dışa aktarma ertelenir.

## **Kurulum ve Yapılandırma:**

Bu kartı yapılandırmak için, kullanıcıların şunları yapması gerekir:

1. Belgenin nasıl dışa aktarılacağını tanımlamak için istenen **Dışa Aktarma Yapılandırması**nı seçin.
2. Değeri **True** veya **False** olarak ayarlayarak **Bekleyen Görevleri Yok Sayıp** saymayacağınızı seçin.
3. Kart, eylemini yalnızca bu koşullar doğru olduğunda yürüttüğünden, **"Where"** ve **"And Bölümleri"**ndeki koşulların doğru ayarlandığından emin olun.

## **Sonuç:**

**"Export Document with Export Configuration"** iş akışı kartı, belgelerin verimli ve önceden tanımlanmış yapılandırmalara göre dışa aktarılmasını sağlar. Bekleyen görevleri yok sayma yeteneğiyle, bu kart belgeleri çeşitli aşamalarda işlemede esneklik sunar, gecikmeleri azaltır ve dışa aktarma sürecini kolaylaştırır.

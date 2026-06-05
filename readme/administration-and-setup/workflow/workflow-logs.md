# Workflow Logs

## **Genel Bakış**

**Workflow Logs**, kullanıcıların bir belge için hangi iş akışlarının yürütüldüğünü analiz etmesine, yürütme sonuçlarını anlamasına ve hata ayıklama veya doğrulama için koşul düzeyindeki ayrıntılara inmesine olanak tanır.

## **Workflow Logs'a Erişim**

Workflow Logs'a erişmek için:

1. **Dashboard**'a gidin.
2. İlgili belgenin yanındaki **Eylemler menüsünü** (üç nokta simgesi) tıklayın.
3. Menüden **Workflow Logs**'u seçin.
   * <mark style="color:red;">**Not**</mark>: Bu seçeneğe erişmek için Workflow özelliğinin etkinleştirilmiş olması gerekir.
4.  Yürütülen iş akışlarının bir özetini gösteren bir **yan panel** açılır.\\

    <div align="left"><figure><img src="../../.gitbook/assets/image (8).png" alt="" width="563"><figcaption></figcaption></figure></div>

## **Workflow Logs Panelinin Bileşenleri**

#### **1. İş Akışı Özet Sayaçları**

Günlük panelinin üst kısmında yer alır:

* **Mavi**: Yürütülen toplam iş akışı sayısı.
* **Kırmızı**: **Hatayla** sonuçlanan iş akışları.
* **Sarı**: Koşul uyuşmazlıkları nedeniyle **tamamlanmayan** iş akışları.
* **Yeşil**: Başarıyla **yürütülen** iş akışları.

#### **2. İş Akışı Yürütme Tablosu**

Tablodaki her satır bir iş akışı yürütmesini temsil eder ve şunları içerir:

* **İş Akışı Adı**
* **Zaman Damgası** (Oluşturulma Tarihi)
* **Çalışma Süresi** (saniye cinsinden)
* **Sonuç Simgesi**:
  * Yeşil onay işareti: İş akışı başarıyla yürütüldü.
  * Kırmızı çarpı: İş akışı bir hatayla yürütüldü.
  * Turuncu çizgi: Bir koşul karşılanmadığı için yürütme durduruldu.

Her satırın solundaki **oku** tıklamak, **iş akışı ayrıntı görünümünü** genişletir.

<div align="left"><figure><img src="../../.gitbook/assets/workflow_test9_match_check_overview.png" alt="" width="563"><figcaption></figcaption></figure></div>

### **İş Akışı Ayrıntı Görünümü**

Belirli bir iş akışı satırını tıklamak, aşağıdakileri gösteren ayrıntılı **yürütme günlüğünü** açar:

#### **Koşul Değerlendirmesi**

* **When...** bloğu: İlk koşul.
* **And...** bloğu/blokları: Ek koşullar.
* **Then...** bloğu/blokları: Tüm koşullar karşılandığında gerçekleştirilen eylemler.

Her koşul satırı şunları gösterir:

* **Yeşil onay**: Koşul karşılandı.
* **Turuncu çizgi**: Koşul karşılanmadı.
* **Kırmızı çarpı**: Koşul **bir hata nedeniyle** başarısız oldu.

### **Önemli Davranış Notu**

Bir iş akışındaki bir koşul **karşılanmazsa**, sistem o iş akışı içindeki **daha fazla iş akışı kartını değerlendirmeyi durdurur**. Bu davranış gereksiz işlemeyi önler.\
Görsel bir gösterge olarak, **koşulunu karşılamayan** kart **gri** olarak gösterilir ve aynı iş akışındaki tüm **sonraki kartlar** da **gri** görünerek **yürütülmediklerini** belirtir.

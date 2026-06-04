# Document Status Condition List

<figure><img src="../../../../.gitbook/assets/userlmn_e9d6da331deceed4f330358635d6b605 (1).png" alt="" width="521"><figcaption></figcaption></figure>

**Amaç**

Bu kart, bir belgenin mevcut durumuna göre iş akışı eylemlerini kontrol etmek için tasarlanmıştır ve belirli süreçleri ya tetiklemek ya da kısıtlamak için koşullu mantık kullanır. Belgelerin yalnızca önceden tanımlanmış durum ölçütlerini karşıladıklarında iş akışlarından ilerlemesini sağlar.

**Kartın Bileşenleri**

1. **Operatör**
   * **Açıklama**: Belge durumunun belirtilen bir koşula karşı nasıl değerlendirileceğini belirler.
   * **Seçenekler**:
     * **is**: Belgenin mevcut durumu belirtilen durumlardan biriyle eşleşirse ilişkili eylemleri tetikler.
     * **is not**: Belgenin durumu belirtilen durumlardan hiçbiriyle eşleşmezse eylemleri tetikler.
2. **Durum ( Liste )**
   * **Açıklama**: Belgenin mevcut durumunun karşılaştırılacağı belirli durumları listeler.
   * **Örnekler**: "Error", "Export Error", "Ready in Validation", "Ready in Review", "Pending Approval", "Pending Second Approval". Bunlar, bir belgenin bir iş akışı süreci içinde bulunabileceği farklı aşamaları veya koşulları temsil eder.

**İşlevsellik**

* **Durum Tanımlama**: ERP sisteminin iş akışında ilerlerken bir belgenin mevcut durumunu otomatik olarak tanımlar.
* **Koşul Değerlendirmesi**: Belgenin durumuna seçilen operatörü (is veya is not) listelenen durumlarla karşılaştırarak uygular:
  * **is** ise, belgenin durumunun listedeki herhangi bir durumla eşleşip eşleşmediğini kontrol eder.
  * **is not** ise, belgenin durumunun listede görünmediğini kontrol eder.
* **Eylem Yürütme**: Koşul değerlendirmesinin sonucuna bağlı olarak:
  * **Doğru**: Koşul karşılanırsa önceden tanımlanmış eylemleri veya iş akışlarını yürütür.
  * **Yanlış**: Koşul karşılanmazsa atlar veya alternatif iş akışları tetikler.
* **İş Akışı Entegrasyonu**: Diğer iş akışı bileşenleriyle sorunsuz entegre olur ve belge işlemenin sistem genelinde koordine edilmesini sağlar.

**Kullanıcı Etkileşimleri**

* **Kurulum ve Yapılandırma**: Kullanıcılar, operatörü seçerek ve ilgili durumları belirterek kartı yapılandırır. Bu kurulum, durumları ve operatörleri seçmek için basit açılır menüler veya onay kutuları içerebilir.
* **İzleme ve Yönetim**: Kullanıcılar, izlenen durum koşulları ve bu koşullara göre gerçekleştirilen eylemler hakkında öngörüler sağlayan bir gösterge paneli aracılığıyla kartın etkinliğini izleyebilir.
* **Hata Yönetimi ve Uyarılar**: Süreç hataları veya beklenen belge durumlarındaki uyuşmazlıklar için uyarılar ayarlamayı destekler ve operasyonel sorunlara hızlı yanıt verilmesini sağlar.

#### Sonuç

"Document Status Condition" iş akışı kartı, belgelerin mevcut durumlarına göre doğru şekilde işlenmesini sağlamak için hayati öneme sahiptir ve ERP sistemi içinde kontrol ve verimliliği artırır. Bu kartı sistemin kılavuzunda net bir şekilde belgelemek, kullanıcıların onu etkili bir şekilde uygulamasına ve yönetmesine yardımcı olur ve sorunsuz ve uyumlu belge iş akışlarını sürdürmek için işlevselliğinden yararlanır. Bu kart, özellikle belge yaşam döngülerini yönetmede ve yalnızca belirli ölçütleri karşılayan belgelerin iş süreçlerinin sonraki aşamalarına ilerlemesini sağlamada yararlıdır.

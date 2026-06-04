# Change Status to

<figure><img src="../../../../.gitbook/assets/image (283).png" alt="" width="563"><figcaption></figcaption></figure>

## **Amaç:**

**"Change Status"** iş akışı kartı, bir belgenin durumunu önceden tanımlanmış durumlardan birine — **Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval** — değiştirmek ve isteğe bağlı olarak durum değişikliğine göre ilişkili iş akışlarını tetiklemek için kullanılır. Bu kart, durum güncellemeleri ve iş akışı tetikleyicileri sürecini otomatikleştirir ve verimli belge yönetimi ile hata yönetimi sağlar.

## **Kartın Bileşenleri:**

1. **Durum (Status)**
   * **Açıklama**: Belgeye uygulanacak yeni durumu belirtir.
   * **Seçenekler**:
     * **Error**: Belgeyi bir hatayla karşılaşmış olarak işaretler.
     * **Rejected**: Belgenin reddedildiğini ve daha ileri gitmeyeceğini gösterir.
     * **Ready for Validation**: Belgeyi bir sonraki kullanıcı veya sistem süreci tarafından incelenecek ve doğrulanacak şekilde ayarlar.
     * **Pending Approval**: Belgeyi onay için beklemede durumuna alır.
     * **Pending Second Approval**: Geçerliyse, belgeyi ikinci düzeyde onay için bekletir.
2. **İş Akışlarını Tetikle (Trigger Workflows)**
   * **Açıklama**: Durum değişikliğinden sonra herhangi bir sonraki iş akışının tetiklenip tetiklenmeyeceğini belirler.
   * **Seçenekler**:
     * **True**: Durum değişikliğine göre ilgili iş akışlarını başlatır.
     * **False**: Durum değişikliğinden sonra iş akışı yürütülmesini önler.

## **İşlevsellik:**

* **Koşul Değerlendirmesi**: Sistem, **"Where"** ve **"And Bölümleri"**nde ayarlanan koşulları değerlendirir. Bu koşullar doğruysa, kart belgenin durumunu seçilen değere değiştirmeye devam eder.
* **Durum Güncellemesi**: Koşullar karşılandığında, belgenin durumu kullanıcının seçimine bağlı olarak önceden tanımlanmış seçeneklerden birine (Error, Rejected, Ready for Validation, Pending Approval, Pending Second Approval) güncellenir.
* **İş Akışı Tetikleme Eylemi**: **Trigger Workflows** **True** olarak ayarlanırsa, sistem durum güncellemesinin ardından ilişkili herhangi bir iş akışını otomatik olarak başlatır. **False** olarak ayarlanırsa, ek iş akışı tetiklenmez ve süreç durum değişikliğiyle sona erer.

## **Kurulum ve Yapılandırma:**

Bu kartı yapılandırmak için, kullanıcıların şunları yapması gerekir:

1. Koşul değerlendirmesi üzerine belgenin ayarlanacağı istenen **Durum**u belirtin (Error, Rejected, Ready for Validation, Pending Approval veya Pending Second Approval).
2. **True** veya **False** seçerek durum değişikliğinden sonra **İş Akışlarını Tetikleyip** tetiklemeyeceğinizi seçin.
3. Kart, eylemini yalnızca **"Where"** ve **"And Bölümleri"**ndeki her iki koşul da doğru olarak değerlendirilirse yürütür.

## **Sonuç:**

**"Change Status"** iş akışı kartı, belge durumlarını yönetmek ve ilgili iş akışlarını tetiklemek için kolaylaştırılmış bir yaklaşım sunar. Belgelerin otomatik olarak doğru duruma yönlendirilmesini ve durum değişikliğine bağlı olarak gerekli eylemlerin gerçekleştirilmesini sağlar. Yürütme için açık koşullar belirleyerek, manuel çabayı azaltır ve iş akışı verimliliğini artırır.

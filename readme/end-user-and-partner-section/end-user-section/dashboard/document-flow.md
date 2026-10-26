---
description: DocBits Belge Akışı Kılavuzu
---

# Belge Akışı

**Belge Akışı**, bir belgenin işleme adımlarını gösterir. Hangi adımların tamamlandığını, hangisinin beklediğini ve işlemenin ne kadar sürdüğünü görmek için kullanın. Aşağıdaki örnekte İngilizce Sandbox ortamındaki sentetik bir fatura kullanılmıştır.

## Gösterge Panosundan açma

[Gösterge Paneli](../../../overview/dashboard/README.md) üzerinde belgeyi bulun. **Eylemler** sütunundaki üç noktayı seçin ve ardından **Belge akışı**'nı tıklayın. Bu seçenek o belgenin akışını açar; belgenin kendisini değiştirmez.

<figure><img src="../../../.gitbook/assets/document-flow-dashboard-menu-tr-20261008.png" alt="Sentetik bir faturanın Eylemler menüsü açıkken Türkçe Gösterge Paneli; Belge akışı, Atamak seçeneğinin altında listelenir."><figcaption>Belgenin Eylemler menüsünden Belge akışı'nı seçin.</figcaption></figure>

## Alan Doğrulamasından açma

Belgeyi açın. [Doğrulama Ekranı](../../../readme-1/validation-screen.md) üzerinde, sağdaki eylem çubuğundaki üç noktayı seçin ve ardından **Daha fazla seçenek** altında **Belge Akışı**'nı tıklayın.

<figure><img src="../../../.gitbook/assets/document-flow-validation-menu-tr-20261008.png" alt="Sentetik bir fatura yanında Daha fazla seçenek menüsünü ve Belge Akışı öğesini gösteren Türkçe Alan Doğrulaması ekranı."><figcaption>Aynı akışa belge görünümünden de ulaşılır.</figcaption></figure>

## Akışı okuma

Soldaki **Process Statistics** paneli adım sayısını, tamamlanan ve bekleyen adımları, yeniden başlatmaları, toplam süreyi, geçerli durumu ve genel ilerlemeyi özetler. Her numaralı kart bir işleme adımını ve o anki durumunu gösterir. Sonraki adımları görmek için aşağı kaydırın.

<figure><img src="../../../.gitbook/assets/document-flow-overview-tr-20261008.png" alt="Solda Process Statistics paneli ve ilk numaralı adım kartlarını gösteren Türkçe Belge Akışı görünümü: İTHAL, OCR_COMPLETED ve SINIFLANDIRILMIŞ."><figcaption>Sentetik bir faturanın akışındaki ilk adımlar.</figcaption></figure>

<figure><img src="../../../.gitbook/assets/document-flow-later-steps-tr-20261008.png" alt="Aşağı kaydırıldıktan sonraki Türkçe Belge Akışı görünümü; sonraki kartlar FIELDS_EXTRACTED, TABLES_EXTRACTED, TRANSFORMED, METADATA_POPULATED, LOOKUP_COMPLETED ve QUEUED durumundaki son adımı içerir."><figcaption>Sırayı sonraki adımlara kadar takip etmek için kaydırın.</figcaption></figure>

Bir adım kartını seçerek solda **Step Details** panelini açın. Bu panel modülü ve durumunu gösterir. Sağda bir **Task Logs** paneli de açılabilir; günlük ayrıntıları o görev için neyin mevcut olduğuna bağlıdır. Step Details panelini kapatmak için **×** simgesini seçin.

<figure><img src="../../../.gitbook/assets/document-flow-step-details-tr-20261008.png" alt="OCR kartının seçili olduğu Türkçe Belge Akışı görünümü; Process Statistics altındaki Step Details paneli ocr_completed modülünü ve Completed durumunu gösterir."><figcaption>Step Details, seçili modülün durumunu açıklar.</figcaption></figure>

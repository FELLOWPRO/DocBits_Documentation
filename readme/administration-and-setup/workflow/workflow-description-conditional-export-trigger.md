# Workflow Example: Conditional Export Trigger

<figure><img src="../../.gitbook/assets/image (3) (2) (2).png" alt=""><figcaption></figcaption></figure>

Bu iş akışı, bir dışa aktarma işleminin hangi koşullar altında başlatılması gerektiğini ana hatlarıyla belirtir. Yalnızca belirtilen tüm ölçütleri karşılayan belgelerin dışa aktarım için işlenmesini sağlayarak veri bütünlüğünü ve iş kurallarıyla uyumu artırır.

### When:

* Sistemdeki bir belge, dışa aktarma uygunluğu açısından değerlendirilir.

### Logic:

1. **Belge Türü Kontrolü**
   * Belge belirli bir türde olmalıdır (örneğin, "Fatura" veya "Makbuz"). Dışa aktarma işlemi için uygun olan belge türünü belirtin.
2. **Durum Doğrulaması**
   * Belgenin mevcut durumu, daha fazla işleme hazır olduğunu gösteren önceden tanımlanmış ölçütleri karşılamalıdır (örneğin, "Onaylandı" veya "Dışa Aktarmaya Hazır").
3. **Bağlamsal Koşullar**
   * Belgenin ayrıntılarının belirli gereksinimlerle uyumlu olduğundan emin olmak için ek kontroller gerçekleştirilir. Bu kontroller, sipariş onaylarındaki veya satın alma siparişlerindeki bilgilerin doğrulanmasını içerebilir. Karşılanması gereken belirli koşulları belirtin. Örneğin:
     * Sipariş onayında listelenen tüm kalemler, satın alma siparişindekilerle eşleşir.
     * Sipariş onayındaki toplam tutar, satın alma siparişindeki toplam tutarla eşleşir.
     * Sipariş onayında belirtilen teslimat tarihleri, satın alma siparişindekilerle uyumludur.

### Then:

#### Action:

* **Dışa Aktarmayı Başlat**
  * Yukarıdaki tüm koşullar karşılanırsa, sistem belge için dışa aktarma işlemini otomatik olarak başlatır.
  * Bu, bir dışa aktarma dosyası oluşturmayı, harici bir sisteme veri göndermeyi veya başka bir uygulamada bir iş akışını tetiklemeyi içerebilir.

#### Implementation Example:

```yaml
rules:
  - description: "Conditional Export Trigger"
    conditions:
      - type: "DocumentType"
        criteria: "<SpecifyDocumentType>"
      - type: "Status"
        criteria: "<SpecifyStatus>"
      - type: "DetailMatch"
        criteria:
          - "ItemMatch"
          - "AmountMatch"
          - "DateMatch"
    actions:
      - operation: "StartExport"
```

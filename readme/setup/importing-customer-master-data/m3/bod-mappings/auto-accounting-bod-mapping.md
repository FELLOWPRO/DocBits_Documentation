# Auto Accounting BOD Eşleme

DocBits Auto-Accounting iş akışı, gider faturalarını geçerli muhasebe boyutlarıyla zenginleştirmek için Infor M3'ten iki BOD tüketir:

- **`Sync.CodeDefinition`** — muhasebe boyutu başına geçerli değerler listesini sağlar (maliyet merkezi, proje, hesap grubu, …).
- **`Sync.ChartOfAccounts`** — her hesaba bağlı boyut profili ile birlikte hesap planını sağlar.

{% file src="../../../../.gitbook/assets/Sync.CodeDefinition.pdf" %}
CodeDefinition — Orijinal BOD eşleme referansı (PDF)
{% endfile %}

## Sync.CodeDefinition

→ DocBits Ana Veri Tablosu: **m3flexdimension**

#### Durum 1: Aynı ID birden fazla boyutta geçiyor

```json
{
    "ID": "concat(substring(//DataArea/CodeDefinition/CodeValue/@listID,21),'_',//DataArea/CodeDefinition/DocumentID/ID)",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

#### Durum 2: ID tek bir boyutta geçiyor

```json
{
    "ID": "//DataArea/CodeDefinition/DocumentID/ID",
    "Dimension": "substring(//DataArea/CodeDefinition/CodeValue/@listID,21)",
    "ListID": "//DataArea/CodeDefinition/ListID",
    "CodeValue": "//DataArea/CodeDefinition/CodeValue",
    "Description": "//DataArea/CodeDefinition/Description"
}
```

### Alan referansı

| DocBits alanı | Açıklama |
|---|---|
| `ID` | `m3flexdimension` içindeki birincil anahtar. **Durum 1**'de, aynı kod farklı boyutlarda göründüğünde girişleri benzersiz tutmak için boyut kodu M3 `DocumentID/ID`'nin önüne eklenir; **Durum 2** ham M3 ID'sini kullanır. |
| `Dimension` | Boyut adı (örn. maliyet merkezi, proje). `CodeValue/@listID` değerinden `substring(..., 21)` ile çıkarılır — aşağıdaki nota bakın. |
| `ListID` | Tam, kesilmemiş `ListID` değeri. Orijinal ad alanı önekinin denetim ve aşağı akış araçları için kullanılabilir olması amacıyla `Dimension` ile birlikte saklanır. |
| `CodeValue` | Gerçek boyut kod değeri (örn. maliyet merkezi numarası `1000`). |
| `Description` | Kodun okunabilir açıklaması (örn. "Pazarlama"). |

### `substring(..., 21)` ifadesi hakkında

XPath `substring()` fonksiyonunun ikinci argümanı 1 tabanlı bir başlangıç konumudur. M3, `@listID` değerini 20 karakter uzunluğunda ad alanı benzeri bir önekle yayınlar (örneğin `lng.m3.dimension.D1`), bu nedenle `substring(value, 21)` o önekten sonraki boyut kodunu döndürür (örnekte `D1`). M3'ünüz farklı uzunlukta bir önek yayıyorsa, ofsetin ayarlanması gerekir — standart olmayan bir kiracıya karşı Auto-Accounting'i yapılandırmadan önce lütfen örnek bir BOD ile iletişime geçin.

### Boyutlar gider faturalarına nasıl beslenir

Bir fatura gider faturası olarak sınıflandırıldığında, DocBits hesap planına göre muhasebe satırları önerir (aşağıya bakın). Önerilen nominal hesabın gerektirdiği her boyut için, kullanıcı arayüzü `m3flexdimension`'da saklanan değerleri sunar — en son `Sync.CodeDefinition` BOD'larından önceden doldurulmuş. AP kullanıcısı doğru değeri seçer veya otomatik öneriyi kabul eder ve sonuç, ilgili `Sync.SupplierInvoice` BOD'u ile M3'e geri verilir.

## Sync.ChartOfAccounts

→ DocBits Ana Veri Tablosu: **ChartOfAccounts**

```json
{
    "ID": "//DataArea/ChartOfAccounts/IDs/ID",
    "NominalAccount": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/GLNominalAccount",
    "AccountType": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/AccountType",
    "Description": "//DataArea/ChartOfAccounts/BaseChartOfAccounts/Description",
    "DimensionProfile": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/ID",
    "Dimension1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/ListID",
    "Usage1": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[0]/Usage",
    "Dimension2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/ListID",
    "Usage2": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[1]/Usage",
    "Dimension3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/ListID",
    "Usage3": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[2]/Usage",
    "Dimension4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/ListID",
    "Usage4": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[3]/Usage",
    "Dimension5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/ListID",
    "Usage5": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[4]/Usage",
    "Dimension6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/ListID",
    "Usage6": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[5]/Usage",
    "Dimension7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/ListID",
    "Usage7": "//DataArea/ChartOfAccounts/DimensionProfileSet/DimensionProfile/DimensionUsage[6]/Usage"
}
```

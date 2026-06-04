---
hidden: true
---

# In Order Confirmation Purchase Order

### Satınalma Siparişiyle Karşılaştır:

**In Order Confirmation Purchase Order**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Mantık Kartı: Miktar veya Birim Fiyat veya İndirim Eşleşmesi

Bu mantık kartı, bir sipariş onayında ayrıntılı olarak belirtilen miktarın, birim fiyatın veya indirimin satınalma siparişindeki karşılık gelen rakamlarla eşleştiğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilenler ile tedarikçinin teslim etmeyi onayladığı şeyler arasında tutarlılık ve doğruluk sağlar.

#### Tetikleme Koşulu

Mantık, bir sipariş onayında orijinal satınalma siparişine göre aşağıdaki koşullardan herhangi biri karşılandığında etkinleştirilir:

* **Miktar**: Sipariş edilen öğelerin miktarı tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Üzerinde anlaşılan öğe başına fiyat, tedarikçinin onayıyla eşleşir.
* **İndirim**: Uygulanan herhangi bir indirim, satınalma siparişi ile sipariş onayı arasında tutarlıdır.

#### Sonuçlar

* **Eşittir**: Sipariş onayının miktarı, birim fiyatı veya indirimi satınalma siparişiyle tam olarak eşleşirse, sistem onayı geçerli sayar ve satınalma sürecindeki sonraki adımlarla devam eder.
* **Eşit Değildir**: Miktarda, birim fiyatta veya indirimde bir tutarsızlık varsa, sistem sipariş onayını manuel inceleme için işaretler. Bu, herhangi bir uyuşmazlığın ilerlemeden önce çözülmesini sağlar.

#### Faydalar

* **Doğruluk ve Tutarlılık**: Satınalma sürecinde doğruluğu korur ve ödemelerin ve teslimatların doğru rakamlara göre yapılmasını sağlar.
* **Verimlilik**: Doğrulama sürecini otomatikleştirir, manuel kontrollere olan ihtiyacı azaltır ve sipariş işlemeyi hızlandırır.
* **Maliyet Kontrolü**: Süreçte erken tutarsızlıkları yakalayarak fazla ödemeleri veya yanlış teslimatları önlemeye yardımcı olur.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Karşılaştırma Parametrelerini Tanımla**: Mantık kartının bir eşleşme için kontrol edeceği belirli alanları (miktar, birim fiyat, indirim) ayarlayın.
2. **Doğrulamayı Otomatikleştir**: Sistemi, bir sipariş onayı alındığında bu ayrıntıları otomatik olarak karşılaştıracak şekilde yapılandırın.
3. **Uyarıları Özelleştir**: Manuel inceleme için uyarıların özelleştirilmesi dahil, tutarsızlıkları ele alma iş akışına karar verin.

Bu mantık kartı, bir sipariş onayının ayrıntılarının orijinal satınalma siparişiyle uyumlu olmasını sağlamak için hayati öneme sahiptir ve satınalma döngüsünün bütünlüğünü korur. \`\`

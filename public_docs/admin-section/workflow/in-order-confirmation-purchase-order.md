---
hidden: true
---

# Sipariş Onayında Satın Alma Siparişi

### Satın Alma Siparişi ile Karşılaştır:

**Sipariş Onayında Satın Alma Siparişi**

<figure><img src="https://lh7-us.googleusercontent.com/glQHETatKah-1YugeLqBb7Jim6lNJxuarRv-KEMv4NPzFfcjSm6mVhTMdI30nxdJ0SHXZ55Oup6KH7K-J6IxjUOiG0wxUX8toAaCopgBJwPyr94CPjoKuauNTmoHGGhg6f3gwHD39W7gpvijg4LQVJ4" alt="" width="563"><figcaption></figcaption></figure>

#### Mantık Kartı: Miktar veya Birim Fiyat veya İndirim Eşleşmesi

Bu mantık kartı, bir sipariş onayında ayrıntıları verilen miktar, birim fiyat veya indirimin satın alma siparişindeki karşılık gelen rakamlarla eşleştiğini otomatik olarak doğrulamak için tasarlanmıştır. Bu doğrulama, sipariş edilen ile tedarikçinin teslim etmeyi onayladığı arasında tutarlılık ve doğruluk sağlar.

#### Tetikleme Koşulu

Mantık, orijinal satın alma siparişine göre bir sipariş onayında aşağıdaki koşullardan herhangi biri karşılandığında etkinleşir:

* **Miktar**: Sipariş edilen kalemlerin miktarı, tedarikçi tarafından onaylanan miktarla eşleşir.
* **Birim Fiyat**: Kararlaştırılan kalem başına fiyat, tedarikçinin onayıyla eşleşir.
* **İndirim**: Uygulanan tüm indirimler, satın alma siparişi ile sipariş onayı arasında tutarlıdır.

#### Sonuçlar

* **Eşittir**: Sipariş onayının miktarı, birim fiyatı veya indirimi satın alma siparişiyle tam olarak eşleşirse, sistem onayı geçerli sayar ve tedarik sürecindeki sonraki adımlara geçer.
* **Eşit Değildir**: Miktarda, birim fiyatta veya indirimde bir tutarsızlık varsa, sistem sipariş onayını manuel inceleme için işaretler. Bu, ilerlemeden önce herhangi bir uyumsuzluğun giderilmesini sağlar.

#### Faydalar

* **Doğruluk ve Tutarlılık**: Tedarik sürecinde doğruluğu koruyarak ödemelerin ve teslimatların doğru rakamlara dayanarak yapılmasını sağlar.
* **Verimlilik**: Doğrulama sürecini otomatikleştirerek manuel kontrol ihtiyacını azaltır ve sipariş işlemeyi hızlandırır.
* **Maliyet Kontrolü**: Sürecin başlarında tutarsızlıkları yakalayarak fazla ödemelerin veya yanlış teslimatların önlenmesine yardımcı olur.

<figure><img src="https://lh7-us.googleusercontent.com/DRTMJxJ9XLeC5zWSU8QuZwPLkqHzmCUm9RwiUZIkcc8pVxMZsxLv56dX9spzqr7KeDkTigbeBX2DvAZRe-6MdqOgAnrO-QPnCbi4e6hP4--P_O0A0DSoQJxjGeefOS1p6GuXHs1YXv-A73DXYaE8qlI" alt="" width="563"><figcaption></figcaption></figure>

1. **Karşılaştırma Parametrelerini Tanımlayın**: Mantık kartının eşleşme için kontrol edeceği belirli alanları (miktar, birim fiyat, indirim) ayarlayın.
2. **Doğrulamayı Otomatikleştirin**: Sistemi, bir sipariş onayı alındığında bu ayrıntıları otomatik olarak karşılaştıracak şekilde yapılandırın.
3. **Uyarıları Özelleştirin**: Manuel inceleme için uyarıların özelleştirilmesi dahil olmak üzere tutarsızlıkları işlemek için iş akışına karar verin.

Bu mantık kartı, bir sipariş onayının ayrıntılarının orijinal satın alma siparişiyle uyumlu olmasını sağlayarak tedarik döngüsünün bütünlüğünü korumak için hayati öneme sahiptir.

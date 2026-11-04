# Ana Konsept: Tolerans Penceresi

Operatörlere bakmadan önce, tolerans penceresinin nasıl hesaplandığını anlamak önemlidir.

## Tolerans penceresi nedir?

Tolerans penceresi, satın alma siparişi vaat edilen teslimat tarihi etrafındaki kabul edilebilir tarih aralığını tanımlar.

**Örnek:**

* Satın Alma Siparişi Tarihi: **9 Ocak**
* Tolerans Günleri: **3**
* Tolerans Penceresi: **6 Ocak → 12 Ocak**

> <mark style="color:red;">Bu pencere hesaplanırken yalnızca seçilen</mark> <mark style="color:red;"></mark><mark style="color:red;">**İzin Verilen Tolerans Günleri**</mark> <mark style="color:red;"></mark><mark style="color:red;">(haftanın günleri) sayılır.</mark>

### Görsel Zaman Çizelgesi Örneği

```
← Geçmiş                           Gelecek →
|-----|-----|-----|-----|-----|-----|-----|
     6 Oca      9 Oca      12 Oca
   (Başlangıç) (SS Tarihi)    (Bitiş)
```

### Örneklerle Açıklanan Operatör Davranışı

* **Eşittir (=)**
  * **Anlamı:**
Kalem teslimat tarihi tolerans penceresi _içine_ düşmelidir.
  * **Geçerli Tarihler:**
    * **6 Ocak ile 12 Ocak** arasındaki herhangi bir tarih (dahil)
  * **Geçersiz Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
    * **12 Ocak'tan sonraki** herhangi bir tarih
* **Eşit Değildir (≠)**
  * **Anlamı:**
Kalem teslimat tarihi tolerans penceresinin _dışına_ düşmelidir.
  * **Geçerli Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
    * **12 Ocak'tan sonraki** herhangi bir tarih
  * **Geçersiz Tarihler:**
    * **6 Ocak ile 12 Ocak** arasındaki tarihler
* **Büyük veya Eşittir (≥)**
  * **Anlamı:**
Kalem teslimat tarihi, **tolerans penceresinin başlangıcında** veya sonrasında olmalıdır.
  * **Geçerli Tarihler:**
    * **6 Ocak → herhangi bir gelecek tarih**
  * **Geçersiz Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
  * <mark style="color:red;">**Önemli:**</mark>
Bu operatör, tolerans penceresi _içindeki_ **ve ötesindeki** tarihlere izin verir.
* **Küçük veya Eşittir (≤)**
  * **Anlamı:**
Kalem teslimat tarihi, **tolerans penceresinin sonunda** veya öncesinde olmalıdır.
  * **Geçerli Tarihler:**
    * **12 Ocak'a kadar** olan herhangi bir geçmiş tarih
  * **Geçersiz Tarihler:**
    * **12 Ocak'tan sonraki** herhangi bir tarih
* **Büyüktür (>)**
  * **Anlamı:**
Kalem teslimat tarihi _kesinlikle_ tolerans penceresinden sonra olmalıdır.
  * **Geçerli Tarihler:**
    * **13 Ocak → herhangi bir gelecek tarih**
  * **Geçersiz Tarihler:**
    * **12 Ocak ve öncesindeki** herhangi bir tarih
* **Küçüktür (<)**
  * **Anlamı:**
Kalem teslimat tarihi _kesinlikle_ tolerans penceresinden önce olmalıdır.
  * **Geçerli Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
  * **Geçersiz Tarihler:**
    * **6 Ocak ve sonrasındaki** herhangi bir tarih

## “İzin Verilen Tolerans Günleri” Tolerans Penceresini Nasıl Etkiler?

Tolerans penceresi hesaplanırken, **yalnızca seçilen haftanın günleri sayılır**.
Seçilmeyen günler (hafta sonları veya hariç tutulan haftanın günleri gibi) **tamamen atlanır**

#### Örnek: Haftanın Günü Bazlı Tolerans Hesaplaması

**Yapılandırma:**

* Satın Alma Siparişi Tarihi: **9 Ocak Çarşamba**
* Tolerans Günleri: **3**
* İzin Verilen Tolerans Günleri: **Pazartesi, Salı, Çarşamba, Perşembe, Cuma**
* Hafta Sonları (Cumartesi, Pazar): **Seçilmedi**

#### Adım Adım Hesaplama

SS tarihinden başlayarak (**9 Ocak**):

**Geriye doğru sayma (3 tolerans günü):**

* 8 Ocak Salı → **1. Gün**
* 7 Ocak Pazartesi → **2. Gün**
* 6 Ocak Pazar → _Atlandı (izin verilmiyor)_
* 5 Ocak Cumartesi → _Atlandı (izin verilmiyor)_
* 4 Ocak Cuma → **3. Gün**

➡ **Tolerans başlangıç tarihi: 4 Ocak Cuma**

**İleriye doğru sayma (3 tolerans günü):**

* 10 Ocak Perşembe → **1. Gün**
* 11 Ocak Cuma → **2. Gün**
* 12 Ocak Cumartesi → _Atlandı_
* 13 Ocak Pazar → _Atlandı_
* 14 Ocak Pazartesi → **3. Gün**

➡ **Tolerans bitiş tarihi: 14 Ocak Pazartesi**

#### Sonuç Tolerans Penceresi

```
4 Ocak  →  14 Ocak
```

#### Bu Neden Önemlidir?

İzin Verilen Tolerans Günleri yanlış yapılandırılırsa:

* Teslimat tarihleri **beklenmedik şekilde geçerli veya geçersiz** görünebilir
* Erken veya geç teslimatlar doğru algılanmayabilir

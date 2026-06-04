# Key Concept: Tolerance Window

Operatörlere bakmadan önce, tolerans penceresinin nasıl hesaplandığını anlamak önemlidir.

## Tolerans penceresi nedir?

Tolerans penceresi, satınalma siparişi vaat edilen teslimat tarihi etrafında kabul edilebilir bir tarih aralığını tanımlar.

**Örnek:**

* Satınalma Siparişi Tarihi: **9 Ocak**
* Tolerans Günleri: **3**
* Tolerans Penceresi: **6 Ocak → 12 Ocak**

> <mark style="color:red;">Bu pencere hesaplanırken yalnızca seçilen</mark> <mark style="color:red;"></mark><mark style="color:red;">**İzin Verilen Tolerans Günleri**</mark> <mark style="color:red;"></mark><mark style="color:red;">(hafta içi günler) sayılır.</mark>

### Görsel Zaman Çizelgesi Örneği

```
← Past                           Future →
|-----|-----|-----|-----|-----|-----|-----|
     6 Jan      9 Jan      12 Jan
   (Start)    (PO Date)     (End)
```

### Örneklerle Açıklanan Operatör Davranışı

* **Eşittir (=)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi tolerans penceresinin _içine_ düşmelidir.
  * **Geçerli Tarihler:**
    * **6 Ocak ile 12 Ocak** arasındaki herhangi bir tarih (dahil)
  * **Geçersiz Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
    * **12 Ocak'tan sonraki** herhangi bir tarih
* **Eşit Değildir (≠)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi tolerans penceresinin _dışına_ düşmelidir.
  * **Geçerli Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
    * **12 Ocak'tan sonraki** herhangi bir tarih
  * **Geçersiz Tarihler:**
    * **6 Ocak ile 12 Ocak** arasındaki tarihler
* **Büyük veya Eşittir (≥)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi **tolerans penceresinin başlangıcında** veya sonrasında olmalıdır.
  * **Geçerli Tarihler:**
    * **6 Ocak → herhangi bir gelecekteki tarih**
  * **Geçersiz Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
  * <mark style="color:red;">**Önemli:**</mark>\
    Bu operatör tolerans penceresinin _içindeki_ tarihlere **ve ötesindeki** tarihlere izin verir.
* **Küçük veya Eşittir (≤)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi **tolerans penceresinin sonunda** veya öncesinde olmalıdır.
  * **Geçerli Tarihler:**
    * **12 Ocak'a** kadar herhangi bir geçmiş tarih
  * **Geçersiz Tarihler:**
    * **12 Ocak'tan sonraki** herhangi bir tarih
* **Büyüktür (>)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi tolerans penceresinden _kesinlikle sonra_ olmalıdır.
  * **Geçerli Tarihler:**
    * **13 Ocak → herhangi bir gelecekteki tarih**
  * **Geçersiz Tarihler:**
    * **12 Ocak'ta veya öncesinde** herhangi bir tarih
* **Küçüktür (<)**
  * **Anlam:**\
    Satır öğesi teslimat tarihi tolerans penceresinden _kesinlikle önce_ olmalıdır.
  * **Geçerli Tarihler:**
    * **6 Ocak'tan önceki** herhangi bir tarih
  * **Geçersiz Tarihler:**
    * **6 Ocak'ta veya sonrasında** herhangi bir tarih

## "İzin Verilen Tolerans Günleri" Tolerans Penceresini Nasıl Etkiler

Tolerans penceresi hesaplanırken **yalnızca seçilen hafta içi günler sayılır**.\
Seçilmeyen günler (hafta sonları veya hariç tutulan hafta içi günler gibi) **tamamen atlanır**

#### Örnek: Hafta İçi Tabanlı Tolerans Hesaplaması

**Yapılandırma:**

* Satınalma Siparişi Tarihi: **Çarşamba, 9 Ocak**
* Tolerans Günleri: **3**
* İzin Verilen Tolerans Günleri: **Pazartesi, Salı, Çarşamba, Perşembe, Cuma**
* Hafta sonları (Cumartesi, Pazar): **Seçili değil**

#### Adım Adım Hesaplama

PO tarihinden (**9 Ocak**) başlayarak:

**Geriye doğru sayma (3 tolerans günü):**

* Salı, 8 Ocak → **Gün 1**
* Pazartesi, 7 Ocak → **Gün 2**
* Pazar, 6 Ocak → _Atlandı (izin verilmiyor)_
* Cumartesi, 5 Ocak → _Atlandı (izin verilmiyor)_
* Cuma, 4 Ocak → **Gün 3**

➡ **Tolerans başlangıç tarihi: Cuma, 4 Ocak**

**İleriye doğru sayma (3 tolerans günü):**

* Perşembe, 10 Ocak → **Gün 1**
* Cuma, 11 Ocak → **Gün 2**
* Cumartesi, 12 Ocak → _Atlandı_
* Pazar, 13 Ocak → _Atlandı_
* Pazartesi, 14 Ocak → **Gün 3**

➡ **Tolerans bitiş tarihi: Pazartesi, 14 Ocak**

#### Ortaya Çıkan Tolerans Penceresi

```
4 January  →  14 January
```

#### Bu Neden Önemli

İzin Verilen Tolerans Günleri yanlış yapılandırılırsa:

* Teslimat tarihleri **beklenmedik şekilde geçerli veya geçersiz** görünebilir
* Erken veya geç teslimatlar doğru şekilde algılanmayabilir

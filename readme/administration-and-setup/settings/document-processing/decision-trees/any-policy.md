# Herhangi

Birden çok kural doğru olabilir, ancak bu kuralların sonucu aynı olmalıdır.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Toplam tutar **2500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

**Herhangi** politikasının uygulanması için, eşleşen tüm kuralların aynı **Döndürülen Grup** değerini döndürmesi gerekir. Gruplar farklı kurallar arasında eşleşmediğinden, sonuç **false** olur.

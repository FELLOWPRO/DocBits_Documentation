# Eşsiz

Yalnızca tek bir kuralın eşleşmesini sağlar. Birden çok kural eşleşirse, karar ağacı false döndürür.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)
* **Kural 3**: Total Amount <= 5000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 3000 (eşleşir)

Birden çok kural eşleştiği için (**Kural 2**, **Kural 3**, **Kural 4**, **Kural 5**), karar ağacı **false** döndürür çünkü **Benzersiz** politika yalnızca bir kuralın eşleşebilmesini sağlar.

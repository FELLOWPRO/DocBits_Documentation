# Kural Sırası

Bu politika, kuralları karar ağacında göründükleri sırayla uygular ve ilk eşleşen kuralın sonucunu döndürür.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Girdi değerinin **Total Amount = 2500** olduğu göz önüne alındığında, kuralların değerlendirmesi şu şekilde olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

**Kural Sırası** altında, ağaç kuralları listelendikleri sırayla işler. Dolayısıyla eşleşen kurallar şunlar olur:

* **Kural 3**: GROUP_3
* **Kural 4**: GROUP_4
* **Kural 5**: GROUP_5

**Sonuç**: **GROUP_3**, **GROUP_4**, **GROUP_5**

# Kolejność reguł

Ta polityka stosuje reguły w kolejności, w jakiej pojawiają się w drzewie decyzyjnym, i zwraca wynik reguły, która zostanie dopasowana jako pierwsza.

**Przykład:**

| Reguła | Warunek              | Zwracana grupa |
| ------ | -------------------- | -------------- |
| 1      | Total Amount <= 1000 | GROUP\_1       |
| 2      | Total Amount <= 2000 | GROUP\_2       |
| 3      | Total Amount <= 3000 | GROUP\_3       |
| 4      | Total Amount <= 4000 | GROUP\_4       |
| 5      | Total Amount <= 5000 | GROUP\_5       |

Zakładając, że wartością wejściową jest **Total Amount = 2500**, ocena reguł wyglądałaby następująco:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

W ramach polityki **Kolejność reguł** drzewo przetwarza reguły w kolejności, w jakiej są wymienione. Dopasowanymi regułami będą zatem:

* **Reguła 3**: GROUP\_3
* **Reguła 4**: GROUP\_4
* **Reguła 5**: GROUP\_5

**Wynik**: **GROUP\_3**, **GROUP\_4**, **GROUP\_5**

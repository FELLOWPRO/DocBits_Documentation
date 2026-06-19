# Polityka kolejności reguł (Rule Order)

Ta polityka stosuje reguły w kolejności, w jakiej pojawiają się w drzewie decyzyjnym, i zwraca wynik reguły, która zostanie dopasowana jako pierwsza.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Zakładając, że wartością wejściową jest **Total Amount = 3500**, ocena reguł wyglądałaby następująco:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

W ramach polityki **Rule Order** drzewo przetwarza reguły w kolejności, w jakiej są wymienione. Dopasowanymi regułami będą zatem:

* **Reguła 3**: GROUP_3
* **Reguła 4**: GROUP_4
* **Reguła 5**: GROUP_5

**Wynik**: **GROUP_3**, **GROUP_4**, **GROUP_5**

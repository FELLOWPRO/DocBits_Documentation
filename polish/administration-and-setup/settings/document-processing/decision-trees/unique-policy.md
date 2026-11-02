# Unikalny

Zapewnia dopasowanie tylko jednej reguły. Jeśli dopasowanych zostanie wiele reguł, drzewo decyzyjne zwróci wartość false.

**Przykład:**

| Reguła | Warunek            | Zwracana grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie)
* **Reguła 3**: Total Amount <= 5000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 3000 (dopasowanie)

Ponieważ dopasowano wiele reguł (**Reguła 2**, **Reguła 3**, **Reguła 4**, **Reguła 5**), drzewo decyzyjne zwróci wartość **false**, ponieważ polityka **unikalności** zapewnia, że dopasowana może być tylko jedna reguła.

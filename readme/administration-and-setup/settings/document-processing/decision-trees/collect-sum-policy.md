# Polityka zbierania – suma (Collect – sum)

Ta polityka zbiera wszystkie dopasowane reguły i sumuje wyniki. Działa tylko dla **Return Type Value**.

**Przykład:**

| Reguła | Warunek            | Zwracana wartość |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Dla wartości wejściowej **Total Amount = 3500** ocena reguł wyglądałaby następująco:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie, Return Value = 3)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie, Return Value = 4)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie, Return Value = 5)

Ponieważ stosowana jest polityka **zbierania (suma)**, sumujemy **Return Values** dopasowanych reguł, czyli **3, 4, 5**.

**Zsumowanie tych wartości** daje:

* 5 + 4 + 3 = **12**

Zatem wynikiem zwróconym przez drzewo decyzyjne będzie **12**, czyli suma wszystkich dopasowanych wartości zwracanych.

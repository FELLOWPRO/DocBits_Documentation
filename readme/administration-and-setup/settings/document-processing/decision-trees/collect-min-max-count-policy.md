# Polityka zbierania – min/max/zliczanie (Collect – min/max/count)

Ta polityka zbiera wszystkie dopasowane reguły i wybiera wartość **minimalną**, **maksymalną** lub **zlicza** wystąpienia. Działa tylko dla **Return Type Value**.

**Przykład:**

| Reguła | Warunek            | Zwracana wartość |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Jeśli wybrana zostanie opcja **Collect (min)**, wynikiem będzie wartość **minimalna** spośród **Return Values** dopasowanych reguł.
   * Dla wartości wejściowej **Total Amount = 2500** ocena reguł wyglądałaby następująco:
     * **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
     * **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
     * **Reguła 3**: Total Amount <= 3000 (dopasowanie, Return Value = 3)
     * **Reguła 4**: Total Amount <= 4000 (dopasowanie, Return Value = 4)
     * **Reguła 5**: Total Amount <= 5000 (dopasowanie, Return Value = 5)
   * **Dopasowane reguły** to Reguła 3, Reguła 4 i Reguła 5, z **Return Values** wynoszącymi **3, 4 i 5**.
   * Ponieważ stosowana jest polityka **Collect (min)**, wynikiem będzie **wartość minimalna**, czyli **3**.
   * **Wynik**: **3**
2. Jeśli wybrana zostanie opcja **Collect (max)**, wynikiem będzie wartość **maksymalna** spośród **Return Values** dopasowanych reguł.
   * Dla tej samej oceny co powyżej wynikiem będzie:
   * **Wynik**: **5**
3. Jeśli wybrana zostanie opcja **Collect (count)**, wynik zliczy **liczbę dopasowanych reguł**.
   * Dla tej samej oceny co powyżej wynikiem będzie:
   * **Wynik**: **3** (ponieważ dopasowano 3 reguły).

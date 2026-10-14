# Pierwszy

Stosowana jest pierwsza dopasowana reguła, a kolejne reguły nie są już oceniane.

**Przykład:**

| Reguła | Warunek              | Zwracana grupa |
| ------ | -------------------- | -------------- |
| 1      | Total Amount <= 1000 | GROUP\_1       |
| 2      | Total Amount <= 2000 | GROUP\_2       |
| 3      | Total Amount <= 5000 | GROUP\_5       |
| 4      | Total Amount <= 4000 | GROUP\_4       |
| 5      | Total Amount <= 3000 | GROUP\_3       |

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie) → Drzewo decyzyjne przerywa ocenę kolejnych reguł i stosuje **GROUP\_2**.

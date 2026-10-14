# Każdy

Wiele reguł może być prawdziwych, ale wynik tych reguł musi być taki sam.

**Przykład:**

| Reguła | Warunek              | Zwracana grupa |
| ------ | -------------------- | -------------- |
| 1      | Total Amount <= 1000 | GROUP\_1       |
| 2      | Total Amount <= 2000 | GROUP\_2       |
| 3      | Total Amount <= 3000 | GROUP\_3       |
| 4      | Total Amount <= 4000 | GROUP\_4       |
| 5      | Total Amount <= 5000 | GROUP\_5       |

Jeśli kwota całkowita wynosi **2500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (brak dopasowania)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

Aby polityka **Każdy** została zastosowana, wszystkie dopasowane reguły muszą zwracać tę samą **Return Group**. Ponieważ grupy nie są zgodne w poszczególnych regułach, wynikiem będzie **false**.

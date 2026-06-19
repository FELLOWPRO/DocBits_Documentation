# Polityka priorytetu (Priority)

Wybór tej opcji umożliwia ustawienie priorytetów dla każdej reguły. Im niższa wybrana liczba, tym wyższy priorytet (tzn. priorytet 1 ma najwyższy priorytet). Reguły są oceniane na podstawie kolejności ich priorytetów. Zastosowana zostanie dopasowana reguła o najwyższym priorytecie.

**Przykład:**

<table><thead><tr><th width="137">Reguła</th><th width="110">Priorytet</th><th width="268">Warunek</th><th>Zwracana grupa</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Jeśli kwota całkowita wynosi **1500**, ocenione reguły będą następujące:

* **Reguła 1**: Total Amount <= 1000 (brak dopasowania)
* **Reguła 2**: Total Amount <= 2000 (dopasowanie)
* **Reguła 3**: Total Amount <= 3000 (dopasowanie)
* **Reguła 4**: Total Amount <= 4000 (dopasowanie)
* **Reguła 5**: Total Amount <= 5000 (dopasowanie)

Ponieważ priorytet jest stosowany w kolejności **5, 4, 3, 2, 1**, dopasowaną regułą o najwyższym priorytecie będzie **Reguła 5** (**GROUP_5**). Drzewo decyzyjne zwróci **GROUP_5**, ponieważ **Reguła 5** ma najwyższy priorytet (priorytet 1).

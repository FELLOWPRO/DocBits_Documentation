# Politika prioriteta (Priority)

Izbor ove opcije vam omogućava da postavite prioritete za svako pravilo. Što je izabrani broj niži, to je prioritet viši (tj. prioritet 1 ima najviši prioritet). Pravila se procenjuju na osnovu redosleda prioriteta. Primeniće se pravilo sa najvišim prioritetom koje se podudara.

**Primer:**

<table><thead><tr><th width="137">Pravilo</th><th width="110">Prioritet</th><th width="268">Uslov</th><th>Vraćena grupa</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Pošto se prioritet primenjuje redosledom **5, 4, 3, 2, 1**, pravilo sa najvišim prioritetom koje se podudara biće **Pravilo 5** (**GROUP_5**). Stablo odlučivanja će vratiti **GROUP_5** jer **Pravilo 5** ima najviši prioritet (prioritet 1).

# Öncelik

Bu seçeneği seçmek, her kural için öncelikler belirlemenize olanak tanır. Seçilen sayı ne kadar düşükse, öncelik o kadar yüksektir (yani öncelik 1 en yüksek önceliğe sahiptir). Kurallar öncelik sıralarına göre değerlendirilir. En yüksek öncelikli eşleşen kural uygulanır.

**Örnek:**

<table><thead><tr><th width="137">Kural</th><th width="110">Öncelik</th><th width="268">Koşul</th><th>Döndürülen Grup</th></tr></thead><tbody><tr><td>1</td><td>5</td><td>Total Amount &#x3C;= 1000</td><td>GROUP_1</td></tr><tr><td>2</td><td>4</td><td>Total Amount &#x3C;= 2000</td><td>GROUP_2</td></tr><tr><td>3</td><td>3</td><td>Total Amount &#x3C;= 3000</td><td>GROUP_3</td></tr><tr><td>4</td><td>2</td><td>Total Amount &#x3C;= 4000</td><td>GROUP_4</td></tr><tr><td>5</td><td>1</td><td>Total Amount &#x3C;= 5000</td><td>GROUP_5</td></tr></tbody></table>

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)
* **Kural 3**: Total Amount <= 3000 (eşleşir)
* **Kural 4**: Total Amount <= 4000 (eşleşir)
* **Kural 5**: Total Amount <= 5000 (eşleşir)

Öncelik **5, 4, 3, 2, 1** sırasına göre uygulandığından, en yüksek öncelikli eşleşen kural **Kural 5** (**GROUP_5**) olur. Karar ağacı **GROUP_5** döndürür çünkü **Kural 5** en yüksek önceliğe (öncelik 1) sahiptir.

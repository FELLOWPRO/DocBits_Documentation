# Topla (sum) Politikası (Collect (sum) Policy)

Bu politika, eşleşen tüm kuralları toplar ve sonuçları toplamaya alır. Yalnızca **Return Type Value** için çalışır.

**Örnek:**

| Kural | Koşul                | Döndürülen Değer |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

**Total Amount = 2500** girdi değeri için, kuralların değerlendirmesi şu şekilde olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşmez)
* **Kural 3**: Total Amount <= 3000 (eşleşir, Döndürülen Değer = 3)
* **Kural 4**: Total Amount <= 4000 (eşleşir, Döndürülen Değer = 4)
* **Kural 5**: Total Amount <= 5000 (eşleşir, Döndürülen Değer = 5)

**Topla (sum)** politikası uygulandığından, eşleşen kuralların **Döndürülen Değerlerini** toplarız; bunlar **3, 4, 5** değerleridir.

**Bu değerleri toplamak** şunu verir:

* 5 + 4 + 3 = **12**

Böylece karar ağacı tarafından döndürülen sonuç, eşleşen tüm döndürülen değerlerin toplamı olan **12** olur.

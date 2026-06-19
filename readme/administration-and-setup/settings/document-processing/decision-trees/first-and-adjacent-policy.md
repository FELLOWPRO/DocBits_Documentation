# İlk ve Bitişik Politika (First & Adjacent Policy)

Doğru olan ilk kurala bitişik olan kuralın sonucunu seçer.

**Örnek:**

| Kural | Koşul                | Döndürülen Grup |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Toplam tutar **1500** ise, değerlendirilen kurallar şunlar olur:

* **Kural 1**: Total Amount <= 1000 (eşleşmez)
* **Kural 2**: Total Amount <= 2000 (eşleşir)

**Kural 2** eşleşen ilk kural olduğundan, **İlk ve Bitişik** politikası **Kural 3**'ün sonucunu uygular: **GROUP_3**.

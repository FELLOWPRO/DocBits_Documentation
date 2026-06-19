# Politika prvog i susednog (First & Adjacent)

Bira rezultat pravila koje je susedno prvom pravilu koje je tačno.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se)

Pošto je **Pravilo 2** prvo pravilo koje se podudara, politika **First & Adjacent** bi primenila rezultat **Pravila 3**: **GROUP_3**.

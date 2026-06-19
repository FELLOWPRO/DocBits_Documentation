# Politika prvog (First)

Primenjuje se prvo pravilo koje se podudara, a dalja pravila se ne procenjuju.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 5000 | GROUP_5     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 3000 | GROUP_3     |

Ako je ukupan iznos **1500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (podudara se) → Stablo odlučivanja prestaje da procenjuje dalja pravila i primenjuje **GROUP_2**.

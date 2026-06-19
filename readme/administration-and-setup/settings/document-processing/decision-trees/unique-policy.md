# Politika jedinstvenosti (Unique)

Obezbeđuje da se podudara samo jedno pravilo. Ako se podudari više pravila, stablo odlučivanja će vratiti false.

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
* **Pravilo 2**: Total Amount <= 2000 (podudara se)
* **Pravilo 3**: Total Amount <= 5000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 3000 (podudara se)

Pošto se podudara više pravila (**Pravilo 2**, **Pravilo 3**, **Pravilo 4**, **Pravilo 5**), stablo odlučivanja će vratiti **false** jer politika **jedinstvenosti (Unique)** obezbeđuje da se može podudariti samo jedno pravilo.

# Politika bilo kog (Any)

Više pravila može biti tačno, ali rezultat tih pravila mora biti isti.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

Ako je ukupan iznos **2500**, procenjena pravila će biti:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Da bi se politika **Any** primenila, sva pravila koja se podudaraju moraju vratiti istu **vraćenu grupu**. Pošto se grupe ne podudaraju kroz različita pravila, rezultat bi bio **false**.

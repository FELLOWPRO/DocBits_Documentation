# Politika prikupljanja sume (Collect – sum)

Ova politika prikuplja sva pravila koja se podudaraju i sabira rezultate. Radi samo za **Return Type Value**.

**Primer:**

| Pravilo | Uslov            | Vraćena vrednost |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

Za ulaznu vrednost **Total Amount = 3500**, procena pravila bila bi:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se, Return Value = 3)
* **Pravilo 4**: Total Amount <= 4000 (podudara se, Return Value = 4)
* **Pravilo 5**: Total Amount <= 5000 (podudara se, Return Value = 5)

Pošto se primenjuje politika **prikupljanja sume (Collect – sum)**, sabiramo **vraćene vrednosti** pravila koja se podudaraju, a to su **3, 4, 5**.

**Sabiranjem ovih vrednosti** dobijamo:

* 5 + 4 + 3 = **12**

Dakle, rezultat koji vraća stablo odlučivanja bio bi **12**, što je zbir svih vraćenih vrednosti koje se podudaraju.

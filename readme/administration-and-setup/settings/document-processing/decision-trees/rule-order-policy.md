# Politika redosleda pravila (Rule Order)

Ova politika primenjuje pravila redosledom kojim se pojavljuju u stablu odlučivanja i vraća rezultat pravila koje se prvo podudari.

**Primer:**

| Pravilo | Uslov            | Vraćena grupa |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | GROUP_1     |
| 2    | Total Amount <= 2000 | GROUP_2     |
| 3    | Total Amount <= 3000 | GROUP_3     |
| 4    | Total Amount <= 4000 | GROUP_4     |
| 5    | Total Amount <= 5000 | GROUP_5     |

S obzirom na to da je ulazna vrednost **Total Amount = 2500**, procena pravila bila bi:

* **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
* **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
* **Pravilo 3**: Total Amount <= 3000 (podudara se)
* **Pravilo 4**: Total Amount <= 4000 (podudara se)
* **Pravilo 5**: Total Amount <= 5000 (podudara se)

Pod politikom **Rule Order**, stablo će obraditi pravila redosledom kojim su navedena. Dakle, pravila koja se podudaraju biće:

* **Pravilo 3**: GROUP_3
* **Pravilo 4**: GROUP_4
* **Pravilo 5**: GROUP_5

**Rezultat**: **GROUP_3**, **GROUP_4**, **GROUP_5**

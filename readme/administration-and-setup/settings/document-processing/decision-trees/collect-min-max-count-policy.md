# Politika prikupljanja (Collect – min/max/count)

Ova politika prikuplja sva pravila koja se podudaraju i bira **minimum**, **maksimum** ili **broji** pojavljivanja. Radi samo za **Return Type Value**.

**Primer:**

| Pravilo | Uslov            | Vraćena vrednost |
| ---- | -------------------- | ------------ |
| 1    | Total Amount <= 1000 | 1            |
| 2    | Total Amount <= 2000 | 2            |
| 3    | Total Amount <= 3000 | 3            |
| 4    | Total Amount <= 4000 | 4            |
| 5    | Total Amount <= 5000 | 5            |

1. Ako je izabrana opcija **Collect (min)**, rezultat će vratiti **minimum** **vraćenih vrednosti** za pravila koja se podudaraju.
   * Za ulaznu vrednost **Total Amount = 3500**, procena pravila bila bi:
     * **Pravilo 1**: Total Amount <= 1000 (ne podudara se)
     * **Pravilo 2**: Total Amount <= 2000 (ne podudara se)
     * **Pravilo 3**: Total Amount <= 3000 (podudara se, Return Value = 3)
     * **Pravilo 4**: Total Amount <= 4000 (podudara se, Return Value = 4)
     * **Pravilo 5**: Total Amount <= 5000 (podudara se, Return Value = 5)
   * **Pravila koja se podudaraju** su Pravilo 3, Pravilo 4 i Pravilo 5, sa **vraćenim vrednostima** **3, 4 i 5**.
   * Pošto se primenjuje politika **Collect (min)**, rezultat će biti **minimalna vrednost**, koja iznosi **3**.
   * **Rezultat**: **3**
2. Ako je izabrana opcija **Collect (max)**, rezultat će vratiti **maksimum** **vraćenih vrednosti** za pravila koja se podudaraju.
   * Za istu procenu kao gore, rezultat će biti:
   * **Rezultat**: **5**
3. Ako je izabrana opcija **Collect (count)**, rezultat će prebrojati **broj pravila koja se podudaraju**.
   * Za istu procenu kao gore, rezultat će biti:
   * **Rezultat**: **3** (pošto su se podudarila 3 pravila).

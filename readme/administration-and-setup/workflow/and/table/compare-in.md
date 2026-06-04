# Compare In

<figure><img src="../../../../.gitbook/assets/image (43).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica vrši poređenje između dve kolone u navedenoj tabeli, omogućavajući korisnicima da postave uslove na osnovu vrednosti u svakoj koloni. Pored toga, ova kartica uključuje funkciju zavisnosti, gde će se poređenje izvršiti samo ako se vrednost u trećoj koloni poklapa sa navedenim Python regex obrascem. Ovo podešavanje je korisno za uslovne provere koje zavise od više tačaka podataka unutar skupa podataka.

## **Funkcionalnost:**

* **Poređenje kolona sa zavisnošću:** Ova kartica upoređuje vrednosti u dve navedene kolone na osnovu postavljenog uslova, koji se primenjuje samo ako se vrednost u trećoj koloni "zavisnosti" poklapa sa definisanim Python regex obrascem.
* **Operatori:** Korisnici mogu izabrati sledeće operatore za poređenje kolona:
  * **Equals (=):** Proverava da li su vrednosti u dve kolone tačno jednake.
  * **Not Equals (≠):** Obezbeđuje da vrednosti u dve kolone nisu jednake.
  * **Greater Than (>):** Potvrđuje da su vrednosti u prvoj koloni veće od onih u drugoj koloni.
  * **Greater or Equals (≥):** Obezbeđuje da su vrednosti u prvoj koloni veće ili jednake onima u drugoj koloni.
  * **Lesser Than (<):** Proverava da li su vrednosti u prvoj koloni manje od onih u drugoj koloni.
  * **Less or Equals (≤):** Obezbeđuje da su vrednosti u prvoj koloni manje ili jednake onima u drugoj koloni.
* **Regex zavisnost:** Ova kartica uključuje funkciju zavisnosti koja omogućava korisnicima da definišu regex obrazac za treću kolonu. Uslov poređenja se primenjuje samo ako se najmanje jedna vrednost u koloni zavisnosti poklapa sa regex obrascem.

## **Upotreba:**

Ova kartica je posebno korisna u scenarijima gde je potrebna složena uslovna logika, kao što su provere kvaliteta koje zavise od odnosa između tačaka podataka, sa dodatnim uslovima zasnovanim na formatiranju podataka ili određenim obrascima.

***

## **Primer scenarija:**

* Korisnik konfiguriše karticu da uporedi kolone "Quantity" i "Threshold" u tabeli "Stock" sa uslovom **Quantity ≥ Threshold**. Ovo poređenje se izvršava samo ako se kolona "Item Code" poklapa sa regex obrascem za određene formate kodova, kao što je **^A\d{3}$** (što ukazuje na kod stavke koji počinje sa "A" praćen sa tri cifre).

Korišćenjem kartice "Conditional Column Comparison", organizacije mogu kreirati napredna poređenja zavisna od obrazaca unutar skupova podataka, omogućavajući precizno podešenu obradu podataka i poboljšanu tačnost u uslovnim radnim tokovima.

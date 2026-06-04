# Compare values in table

<figure><img src="../../../../.gitbook/assets/image (48).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica vrši poređenje između vrednosti u dve navedene kolone unutar tabele, na osnovu izabranog uslova. Korisna je za scenarije koji zahtevaju validaciju odnosa između tačaka podataka, kao što su kontrola kvaliteta, provere doslednosti podataka ili verifikacija usklađenosti.

## **Funkcionalnost:**

* **Poređenje kolona:** Ova kartica omogućava korisnicima da postave uslove za poređenje vrednosti između dve kolone u istoj tabeli.
* **Operatori:** Sledeći operatori su dostupni za definisanje poređenja:
  * **Equals (=):** Proverava da li su vrednosti u dve kolone tačno jednake.
  * **Not Equals (≠):** Obezbeđuje da vrednosti u dve kolone nisu jednake.
  * **Greater Than (>):** Potvrđuje da su vrednosti u prvoj koloni veće od onih u drugoj koloni.
  * **Greater or Equals (≥):** Obezbeđuje da su vrednosti u prvoj koloni veće ili jednake onima u drugoj koloni.
  * **Lesser Than (<):** Proverava da li su vrednosti u prvoj koloni manje od onih u drugoj koloni.
  * **Less or Equals (≤):** Obezbeđuje da su vrednosti u prvoj koloni manje ili jednake onima u drugoj koloni.
* **Izbor tabele i kolone:** Korisnici navode tabelu i dve kolone koje žele da uporede.

## **Upotreba:**

Ova kartica je idealna za analitičare podataka, timove za kontrolu kvaliteta ili službenike za usklađenost kojima je potrebno da obezbede da se vrednosti u jednoj koloni odnose na vrednosti u drugoj u skladu sa određenim pravilima, omogućavajući naprednu validaciju podataka.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da proveri da li su vrednosti u koloni "Current Stock" **veće ili jednake (≥)** vrednostima u koloni "Minimum Stock Level" u tabeli "Inventory". Ako sve vrednosti ispunjavaju ovaj uslov, radni tok se nastavlja, potvrđujući da su nivoi zaliha adekvatni.

Korišćenjem kartice "Column Value Comparison", organizacije mogu obezbediti doslednost podataka, održati standarde kvaliteta i proveriti odnose podataka unutar tabela.

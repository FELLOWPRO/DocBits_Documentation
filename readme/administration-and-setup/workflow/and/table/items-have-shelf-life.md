# Items Have Shelf Life

<figure><img src="../../../../.gitbook/assets/image (44).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica proverava da li stavke u skupu podataka ispunjavaju navedene uslove na osnovu svog roka trajanja. Kartica omogućava korisnicima da biraju između "bilo koje" ili "svih" stavki za validaciju i podržava različite operatore poređenja. Ovo je idealno za scenarije gde odluke radnog toka zavise od roka trajanja stavki, kao što su kontrola kvaliteta, upravljanje zalihama ili provere usklađenosti

## **Funkcionalnost:**

* **Validacija roka trajanja:** Ova kartica proverava rok trajanja stavki u odnosu na navedeni uslov. Korisnici mogu odabrati da provere **bilo koju** stavku ili **sve** stavke u skupu podataka i primeniti različite operatore poređenja za definisanje uslova.
* **Izbor stavki:** Korisnici mogu birati između:
  * **Any Item:** Kartica se pokreće ako najmanje jedna stavka ispunjava navedeni uslov roka trajanja.
  * **All Items:** Kartica se pokreće samo ako sve stavke ispunjavaju navedeni uslov roka trajanja.
* **Operatori:** Sledeći operatori su dostupni za postavljanje uslova roka trajanja:
  * **Equals (=):** Proverava da li je rok trajanja tačno jednak navedenoj vrednosti.
  * **Not Equals (≠):** Obezbeđuje da rok trajanja nije jednak navedenoj vrednosti.
  * **Greater Than (>):** Potvrđuje da je rok trajanja veći od navedene vrednosti.
  * **Greater or Equals (≥):** Obezbeđuje da je rok trajanja veći ili jednak navedenoj vrednosti.
  * **Less Than (<):** Proverava da li je rok trajanja manji od navedene vrednosti.
  * **Less or Equals (≤):** Obezbeđuje da je rok trajanja manji ili jednak navedenoj vrednosti.



## **Upotreba:**

Ova kartica je pogodna za timove za kontrolu kvaliteta, menadžere zaliha ili službenike za usklađenost kojima je potrebno da obezbede da stavke ispunjavaju određene zahteve roka trajanja pre nastavka sa daljim akcijama ili radnim tokovima.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da proveri da li **sve stavke** imaju rok trajanja **veći ili jednak 30 dana**. Ako svaka stavka ispunjava ovaj uslov, radni tok se nastavlja, potvrđujući da sve stavke imaju dovoljan rok trajanja za prodaju ili distribuciju.

Korišćenjem kartice "Shelf Life Validation", organizacije mogu sprovoditi standarde roka trajanja, održavati kvalitet proizvoda i obezbediti tačnost radnog toka na osnovu uslova roka trajanja stavki.

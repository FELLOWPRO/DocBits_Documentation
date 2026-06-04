# Item Receiving Method

<figure><img src="../../../../.gitbook/assets/image (47).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica proverava da li stavke u skupu podataka imaju navedeni metod prijema. Korisnici mogu odabrati da provere **bilo koju** stavku ili **sve** stavke u skupu podataka na osnovu izabranog uslova, što je čini pogodnom za scenarije gde radni tokovi zavise od metoda prijema stavki, kao što su upravljanje lancem snabdevanja ili praćenje zaliha.

## **Funkcionalnost:**

* **Validacija metoda prijema:** Ova kartica proverava metod prijema stavki u odnosu na navedeni uslov. Korisnici mogu birati između **bilo koje** stavke ili **svih** stavki u skupu podataka i postaviti uslov kao **equals** ili **not equals**.
* **Izbor stavki:** Korisnici mogu navesti:
  * **Any Item:** Kartica se pokreće ako najmanje jedna stavka ispunjava navedeni uslov metoda prijema.
  * **All Items:** Kartica se pokreće samo ako sve stavke ispunjavaju navedeni uslov metoda prijema.
* **Operatori:** Sledeći operatori su dostupni za definisanje uslova:
  * **Equals (=):** Proverava da li se metod prijema poklapa sa navedenom vrednošću.
  * **Not Equals (≠):** Obezbeđuje da se metod prijema ne poklapa sa navedenom vrednošću.

## **Upotreba:**

Ova kartica je idealna za menadžere skladišta, koordinatore zaliha ili logističko osoblje kojima je potrebno da provere metode prijema stavki pre nego što dozvole dalje akcije, kao što su obrada, skladištenje ili otprema.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da proveri da li **sve stavke** imaju metod prijema **jednak "Direct Delivery"**. Ako svaka stavka ispunjava ovaj uslov, radni tok se nastavlja, potvrđujući da su sve stavke namenjene za direktnu isporuku.

Korišćenjem kartice "Receiving Method Validation", organizacije mogu obezbediti usklađenost sa protokolima prijema, poboljšati logističke radne tokove i održati tačnost u rukovanju stavkama na osnovu određenih metoda prijema.

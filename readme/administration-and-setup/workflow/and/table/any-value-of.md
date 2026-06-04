# Any Value of

<figure><img src="../../../../.gitbook/assets/image (46).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica se koristi za proveru da li se bilo koja vrednost u određenoj koloni tabele poklapa sa datim regex obrascem. Ako se bilo koji pojedinačni unos u koloni poklapa sa obrascem, radni tok će se nastaviti, što je čini idealnom za slučajeve upotrebe gde identifikacija čak i jednog poklapanja pokreće sledeće korake u procesu.

## **Funkcionalnost:**

* **Validacija regex obrasca:** Ova kartica proverava da li se bilo koja vrednost u datoj koloni tabele poklapa sa datim obrascem regularnog izraza. Kartica će se pokrenuti i omogućiti nastavak radnog toka ako najmanje jedan unos u koloni ispunjava uslov.
* **Operator:** Korisnici definišu kolonu i navode regex obrazac. Dostupni uslov uključuje:
  * **Matches Regex Pattern:** Proverava da li se najmanje jedna vrednost u navedenoj koloni poklapa sa regex obrascem.
* **Izbor tabele i kolone:** Korisnici navode tabelu i kolonu koje žele da provere za poklapanja sa regex obrascem.

## **Upotreba:**

Ova kartica je posebno korisna za scenarije gde tabela sadrži podatke koji mogu zahtevati određena poklapanja, kao što su validacija e-adresa, brojeva faktura ili ID-ova proizvoda. Obezbeđuje da se radni tokovi nastave kada se bilo koji relevantan unos poklapa sa definisanim obrascem, bez potrebe za proverom svakog unosa.

## **Primer scenarija:**

* Korisnik podešava karticu da proveri unose u koloni "Email Address" u tabeli "Customers", koristeći regex obrazac za validne formate e-pošte. Ako se najmanje jedna e-adresa u koloni poklapa sa obrascem, kartica će pokrenuti sledeći korak radnog toka, obezbeđujući da sistem obradi validan unos.

Korišćenjem kartice "Regex Pattern Matching", organizacije mogu automatizovati radne tokove na osnovu dinamičkih validacija zasnovanih na obrascima, pojednostavljujući procese i obezbeđujući da samo relevantni unosi pokreću dalje akcije.

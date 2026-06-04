# All Value of

<figure><img src="../../../../.gitbook/assets/image (45).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica se koristi za proveru da li se **sve vrednosti** u određenoj koloni tabele poklapaju sa datim regex obrascem. Da bi se radni tok nastavio, svaki unos u koloni mora ispunjavati uslov, što ovu karticu čini idealnom za obezbeđivanje doslednosti i integriteta podataka u svim unosima.

## **Funkcionalnost:**

* **Validacija regex obrasca:** Ova kartica proverava da li se **sve vrednosti** u navedenoj koloni tabele poklapaju sa datim obrascem regularnog izraza. Radni tok će se nastaviti samo ako svaki unos u koloni ispunjava uslov.
* **Operator:** Korisnici definišu kolonu i navode regex obrazac. Dostupni uslov uključuje:
  * **Matches Regex Pattern:** Proverava da li se svaka vrednost u navedenoj koloni poklapa sa regex obrascem.
* **Izbor tabele i kolone:** Korisnici navode tabelu i kolonu koje žele da provere za potpuna poklapanja sa regex obrascem.

## **Upotreba:**

Ova kartica je idealna za slučajeve gde je potrebna ujednačenost podataka, kao što je obezbeđivanje da svi brojevi telefona, ID-ovi proizvoda ili drugi unosi polja budu u skladu sa određenim formatom. Obezbeđuje da se radni tokovi nastave samo kada je svaki relevantan unos usklađen sa obrascem.

## **Primer scenarija:**

* Korisnik podešava karticu da proveri kolonu "Phone Number" u tabeli "Contacts", koristeći regex obrazac za validaciju formata brojeva telefona. Ako se svaki unos broja telefona u koloni poklapa sa obrascem, kartica će pokrenuti sledeći korak u radnom toku, potvrđujući ujednačeno formatiranje podataka.

Korišćenjem kartice "All Values Regex Pattern Matching", organizacije mogu sprovoditi stroge standarde podataka i poboljšati tačnost radnog toka, obezbeđujući da svaki unos u navedenoj koloni ispunjava traženi format pre nastavka.

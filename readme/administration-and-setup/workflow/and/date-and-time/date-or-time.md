# Date or Time

<figure><img src="../../../../.gitbook/assets/image (5) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica proverava da li navedena vrednost datuma/vremena pada unutar definisanog opsega. Omogućava radnim tokovima da se nastave ili zaustave na osnovu toga da li je uslov ispunjen, što je čini pogodnom za vremenski osetljive operacije ili planiranje radnih tokova.

## **Funkcionalnost:**

* **Validacija datuma/vremena:** Ova kartica procenjuje da li je dati datum/vreme unutar navedenog opsega koristeći sledeće uslove:
  * **Is:** Proverava da li je datum/vreme unutar definisanog opsega početka i kraja (uključujući).
  * **Is Not:** Obezbeđuje da datum/vreme pada izvan definisanog opsega.

**Opseg datuma/vremena:** Korisnici navode vrednosti datuma/vremena početka i kraja da definišu opseg za poređenje.

## **Upotreba:**

Ova kartica je idealna za planiranje, provere usklađenosti ili validaciju uslova zasnovanih na vremenu u radnim tokovima. Na primer, može se koristiti da bi se obezbedilo da se zadaci izvršavaju samo tokom unapred definisanih vremenskih okvira ili da bi se proverili rokovi.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da proveri da li je **datum podnošenja** fakture **između** **"2024-11-01"** i **"2024-11-30"**. Ako datum podnošenja pada unutar ovog opsega, radni tok se nastavlja na obradu plaćanja. Ako ne, radni tok pokreće obaveštenje za dalji pregled.

Korišćenjem kartice "Date/Time Range Validation", organizacije mogu obezbediti tačno planiranje, poboljšati usklađenost i pojednostaviti radne tokove pridržavanjem unapred definisanih vremenskih ograničenja.

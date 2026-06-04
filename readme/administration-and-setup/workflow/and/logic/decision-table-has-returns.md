# Decision Table has Returns

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (1) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova DocBits kartica proverava da li navedena tabela odlučivanja ima povratne vrednosti za dati dokument i određuje da li vraćene podatke treba koristiti u narednim koracima radnog toka. Obezbeđuje da se radni tokovi mogu dinamično prilagoditi na osnovu ishoda tabele odlučivanja.

## **Funkcionalnost:**

* **Validacija tabele odlučivanja:** Ova kartica proverava da li izabrana tabela odlučivanja pruža povratne vrednosti za dokument koji se obrađuje.
* **Izbor tabele odlučivanja:** Korisnici navode ime tabele odlučivanja koju treba proveriti.
* **Korišćenje povratnih podataka:** Korisnici mogu navesti da li će koristiti povratne podatke u kasnijim karticama pomoću **Boolean** postavke:
  * **True:** Povratni podaci su dostupni i biće korišćeni u narednim koracima radnog toka.
  * **False:** Povratni podaci se neće koristiti, i radni tok se nastavlja bez njih.

## **Upotreba:**

Ova kartica je idealna za radne tokove koji uključuju uslovnu logiku ili donošenje odluka na osnovu unapred definisanih pravila u tabeli odlučivanja. Obezbeđuje neometanu integraciju izlaza tabele odlučivanja u procese radnog toka.

## **Primer scenarija:**

* Korisnik konfiguriše karticu da proveri tabelu odlučivanja **"Invoice Processing Rules"** za povratne vrednosti. **Boolean** je postavljen na **True**, što ukazuje da će se povratni podaci (npr. zahtevi za odobrenje) koristiti u kasnijim karticama da bi se vodile odluke radnog toka.

Korišćenjem kartice "Decision Table Check", organizacije mogu poboljšati fleksibilnost radnog toka, pojednostaviti obradu zasnovanu na pravilima i obezbediti doslednost u donošenju odluka u automatizovanim radnim tokovima.

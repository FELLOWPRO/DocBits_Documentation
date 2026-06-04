# Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_5e16e9b23626ec1211c753fec5333513 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka upravlja izvršavanjem operacija na osnovu toga da li je zadatak ili dokument dodeljen određenom korisniku ili skupu korisnika. Koristi uslovnu logiku da pokrene ili spreči određene akcije, što je čini idealnom za radne tokove koji zahtevaju rukovanje specifično za korisnika.

**Komponente kartice**

1. **Operator**
   * **Opis**: Definiše logički uslov koji se primenjuje na dodelu korisnika.
   * **Opcije**:
     * **IS**: Pokreće operaciju ako se dodeljeni korisnik dokumenta ili zadatka poklapa sa bilo kojim korisnikom u navedenoj listi.
     * **IS NOT**: Pokreće operaciju ako se dodeljeni korisnik dokumenta ili zadatka ne poklapa ni sa jednim korisnikom u navedenoj listi.
2. **Lista korisnika**
   * **Opis**: Lista ili izbor korisnika za poređenje sa dodeljenim korisnikom.
   * **Detalj**: Ova lista može uključivati jednog ili više korisnika, omogućavajući kartici da efikasno rukuje i pojedinačnim i višestrukim uslovima korisnika. Izbor se može vršiti pomoću polja za potvrdu, padajuće liste sa višestrukim izborom ili sličnih elemenata korisničkog interfejsa.

**Funkcionalnost**

* **Identifikacija dodele korisnika**: Automatski identifikuje korisnika ili korisnike dodeljene određenom zadatku ili dokumentu u ERP sistemu.
* **Procena uslova**:
  * Koristeći operator **IS**, kartica proverava da li je dodeljeni korisnik među onima navedenim u Listi korisnika.
  * Koristeći operator **IS NOT**, kartica obezbeđuje da dodeljeni korisnik nije među navedenima.
* **Izvršavanje akcije**:
  * **Tačan uslov**: Ako dodela korisnika ispunjava uslov (bilo IS ili IS NOT), pokreću se relevantne akcije, kao što su obaveštenja, pokretanja zadataka, odobrenja ili drugi koraci radnog toka.
  * **Netačan uslov**: Ako uslov nije ispunjen, radni tok se neće nastaviti.

**Korisničke interakcije**

* **Podešavanje i konfiguracija**: Korisnici konfigurišu karticu izborom operatora i navođenjem relevantnih korisnika iz Liste korisnika. Podešavanje treba da bude jednostavno za korišćenje i intuitivno kako bi se prilagodilo izborima iz potencijalno velikih baza korisnika.
* **Praćenje i izveštavanje**: ERP sistem treba da pruži funkcionalnost za praćenje i izveštavanje o operacijama pokrenutim ovom karticom, nudeći uvid u tačnost dodela i efikasnost procesa.
* **Rukovanje greškama i obaveštenja**: Korisnici treba da imaju opcije da primaju upozorenja ili obaveštenja ako postoje problemi sa dodelama, kao što su nedodeljeni zadaci ili greške u izboru korisnika.

#### Zaključak

Kartica radnog toka "Assigned User Condition" je ključni alat za upravljanje radnim tokovima dokumenata i zadataka koji zavise od dodela korisnika. Omogućavajući uslove zasnovane na tome da li je zadatak ili dokument dodeljen određenim korisnicima, ona obezbeđuje da radne tokove pokreću samo odgovarajuće interakcije korisnika, poboljšavajući i odgovornost i usklađenost zadataka unutar timova. Jasno dokumentovanje ove kartice pomoći će korisnicima da razumeju njen značaj i da je efikasno integrišu u svoje radne tokove, obezbeđujući neometano i efikasno poslovanje prilagođeno ulogama i odgovornostima korisnika.

# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/userlmn_77e991cee96598023f9a3ac7ad230e50 (1).png" alt="" width="552"><figcaption></figcaption></figure>

**Svrha**

Ova kartica radnog toka olakšava operacije zasnovane na dodeli zadatka ili dokumenta jednom, određenom korisniku. Koristeći direktan pristup uslovnoj logici, ona upravlja radnim tokovima koji zahtevaju ciljano angažovanje korisnika, obezbeđujući preciznost u rukovanju zadacima zasnovanom na korisnicima.

**Komponente kartice**

1. **Operator**
   * **Opis**: Navodi logiku koja se primenjuje na dodelu korisnika.
   * **Opcije**:
     * **IS**: Pokreće operaciju ako se dodeljeni korisnik dokumenta ili zadatka poklapa sa navedenim korisnikom.
     * **IS NOT**: Pokreće operaciju ako se dodeljeni korisnik ne poklapa sa navedenim korisnikom.
2. **Korisnik**
   * **Opis**: Omogućava izbor jednog korisnika sa kojim će se uporediti dodeljeni korisnik.
   * **Detalj**: Ovo uključuje jednostavno padajuće polje ili polje sa automatskim dovršavanjem gde se može izabrati jedan korisnik istovremeno.

**Funkcionalnost**

* **Identifikacija dodele korisnika**: Identifikuje korisnika trenutno dodeljenog određenom zadatku ili dokumentu.
* **Procena uslova**:
  * Za operator **IS**, kartica proverava da li je dodeljeni korisnik isti kao izabrani korisnik.
  * Za operator **IS NOT**, ona proverava da li se dodeljeni korisnik razlikuje od izabranog korisnika.
* **Izvršavanje akcije**:
  * **Tačan uslov**: Ako dodela ispunjava zadati uslov (IS ili IS NOT), pokreću se unapred definisane akcije, koje mogu uključivati nastavak sa odobrenjima, pokretanje daljih zadataka, slanje obaveštenja ili druge povezane radne tokove.
  * **Netačan uslov**: Ako uslov nije ispunjen, radni tok se neće nastaviti.

**Korisničke interakcije**

* **Podešavanje i konfiguracija**: Korisnici podešavaju karticu izborom operatora i izborom korisnika iz polja korisnika. Ovo podešavanje treba da bude jednostavno, obezbeđujući lak izbor korisnika i konfiguraciju.
* **Praćenje i izveštavanje**: Nudi alate za praćenje performansi kartice, kao što je praćenje koji se zadaci pokreću određenim dodelama korisnika i ishodi tih pokretanja.
* **Rukovanje greškama i obaveštenja**: Pruža mehanizme za upozoravanje korisnika ako su zadaci pogrešno dodeljeni ili ako dođe do operativnih grešaka usled problema sa dodelama.

#### Zaključak

Kartica radnog toka "Single Assigned User Condition" je od suštinskog značaja za precizno upravljanje dokumentima i zadacima specifično za korisnika unutar ERP sistema. Ona pojednostavljuje radne tokove fokusirajući se na pojedinačne dodele korisnika, čime obezbeđuje da se akcije izvršavaju samo kada je to prikladno, na osnovu uloge i odgovornosti korisnika. Jasno dokumentovanje ove kartice pomoći će korisnicima da razumeju njenu primenu, omogućavajući im da je efikasno implementiraju i njome upravljaju u svom svakodnevnom poslovanju. Ova dokumentacija obezbeđuje da svi potencijalni korisnici lako shvate svrhu kartice i da je neometano integrišu u svoje radne tokove.

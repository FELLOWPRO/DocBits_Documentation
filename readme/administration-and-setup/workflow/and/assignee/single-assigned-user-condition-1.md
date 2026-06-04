# Single Assigned User Condition

<figure><img src="../../../../.gitbook/assets/image (16) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Svrha:**\
Ova kartica radnog toka izvršava operacije na osnovu toga da li je zadatak ili dokument dodeljen određenoj grupi. Koristi jednostavan uslov za pokretanje ili sprečavanje akcija na osnovu dodele grupe.

**Komponente kartice:**

1. **Operator**
   * **Opis:** Definiše logički uslov koji se primenjuje na dodelu grupe.
   * **Opcije:**
     * **IS:** Pokreće operaciju ako se dodeljena grupa dokumenta ili zadatka poklapa sa navedenom grupom.
     * **IS NOT:** Pokreće operaciju ako se dodeljena grupa dokumenta ili zadatka ne poklapa sa navedenom grupom.
2. **Grupa**
   * **Opis:** Navodi grupu za poređenje sa dodeljenom grupom.
   * **Detalj:** Ovo polje vam omogućava da izaberete jednu grupu za poređenje dodele.

**Funkcionalnost:**

* **Identifikacija dodele grupe:** Automatski identifikuje grupu dodeljenu određenom zadatku ili dokumentu.
* **Procena uslova:**
  * Koristeći operator **IS**, kartica proverava da li se dodeljena grupa poklapa sa navedenom grupom.
  * Koristeći operator **IS NOT**, kartica obezbeđuje da se dodeljena grupa ne poklapa sa navedenom grupom.
* **Izvršavanje akcije:**
  * **Tačan uslov:** Ako dodela grupe ispunjava uslov (bilo **IS** ili **IS NOT**), pokreću se relevantne akcije, kao što su obaveštenja, pokretanja zadataka, odobrenja ili drugi koraci radnog toka.
  * **Netačan uslov:** Ako uslov nije ispunjen, dokument ili zadatak mogu proći kroz drugačije usmeravanje, ili se mogu navesti alternativne akcije.

**Korisničke interakcije:**

* **Podešavanje i konfiguracija:**\
  Korisnici konfigurišu karticu izborom operatora i navođenjem relevantne grupe. Podešavanje treba da bude jednostavno i intuitivno.
* **Praćenje i izveštavanje:**\
  Sistem treba da pruži funkcionalnost za praćenje i izveštavanje o operacijama pokrenutim ovom karticom, nudeći uvid u tačnost dodela i efikasnost procesa.
* **Rukovanje greškama i obaveštenja:**\
  Korisnici treba da imaju opcije da primaju upozorenja ili obaveštenja ako postoje problemi sa dodelama, kao što su nedodeljeni zadaci ili greške u izboru grupe.

**Zaključak:**\
Kartica radnog toka "Assigned Group Condition" je od suštinskog značaja za upravljanje radnim tokovima dokumenata i zadataka zasnovanim na dodelama grupa. Omogućavajući uslove zasnovane na tome da li je zadatak ili dokument dodeljen određenoj grupi, ona obezbeđuje da radne tokove pokreću samo odgovarajuće interakcije grupa, poboljšavajući upravljanje zadacima i efikasnost radnog toka.

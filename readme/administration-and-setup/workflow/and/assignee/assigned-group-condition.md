# Assigned Group Condition

<figure><img src="../../../../.gitbook/assets/image (15) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

**Svrha:**

Ova kartica radnog toka izvršava operacije na osnovu toga da li je zadatak ili dokument dodeljen određenoj grupi ili skupu grupa. Koristi uslovnu logiku da pokrene ili spreči određene akcije u zavisnosti od dodele grupe, što je čini idealnom za radne tokove koji zahtevaju rukovanje specifično za grupu.

**Komponente kartice:**

1. **Operator**
   * **Opis:** Definiše logički uslov koji se primenjuje na dodelu grupe.
   * **Opcije:**
     * **IS:** Pokreće operaciju ako se dodeljena grupa dokumenta ili zadatka poklapa sa jednom od grupa u navedenoj listi.
     * **IS NOT:** Pokreće operaciju ako se dodeljena grupa dokumenta ili zadatka ne poklapa ni sa jednom od grupa u navedenoj listi.
2. **Lista grupa**
   * **Opis:** Lista ili izbor grupa za poređenje sa dodeljenom grupom.
   * **Detalj:** Ova lista može uključivati jednu ili više grupa, omogućavajući kartici da efikasno rukuje i pojedinačnim i višestrukim uslovima grupa.

**Funkcionalnost:**

* **Identifikacija dodele grupe:** Automatski identifikuje grupu ili grupe dodeljene određenom zadatku ili dokumentu u sistemu.
* **Procena uslova:**
  * Koristeći operator **IS**, kartica proverava da li je dodeljena grupa jedna od grupa navedenih u Listi grupa.
  * Koristeći operator **IS NOT**, kartica obezbeđuje da dodeljena grupa nije deo navedenih grupa.
* **Izvršavanje akcije:**
  * **Tačan uslov:** Ako dodela grupe ispunjava uslov (bilo **IS** ili **IS NOT**), pokreću se relevantne akcije, kao što su obaveštenja, pokretanja zadataka, odobrenja ili drugi koraci radnog toka.
  * **Netačan uslov:** Ako uslov nije ispunjen, radni tok se neće nastaviti.

**Korisničke interakcije:**

* **Podešavanje i konfiguracija:** Korisnici konfigurišu karticu izborom operatora i navođenjem relevantnih grupa iz Liste grupa. Podešavanje treba da bude jednostavno za korišćenje i intuitivno kako bi se prilagodilo izborima iz potencijalno velikih baza grupa.
* **Praćenje i izveštavanje:**\
  Sistem treba da pruži funkcionalnost za praćenje i izveštavanje o operacijama pokrenutim ovom karticom, nudeći uvid u tačnost dodela i efikasnost procesa.
* **Rukovanje greškama i obaveštenja:**\
  Korisnici treba da imaju opcije da primaju upozorenja ili obaveštenja ako postoje problemi sa dodelama, kao što su nedodeljeni zadaci ili greške u izboru grupe.

**Zaključak:**\
Kartica radnog toka "Assigned Group Condition" je od suštinskog značaja za upravljanje radnim tokovima dokumenata i zadataka koji zavise od dodela grupa. Omogućavajući uslove zasnovane na tome da li je zadatak ili dokument dodeljen određenim grupama, ona obezbeđuje da radne tokove pokreću samo odgovarajuće interakcije grupa, poboljšavajući odgovornost i upravljanje zadacima među timovima.

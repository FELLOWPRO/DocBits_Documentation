# Checkbox is checked

<figure><img src="../../../../.gitbook/assets/image (20) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije na osnovu stanja (označeno ili neoznačeno) polja za potvrdu unutar vašeg ERP sistema. Procenom uslova polja za potvrdu, ona olakšava pokretanje određenih procesa ili sprovođenje određenih pravila unutar aplikacije.

## **Komponente kartice:**

* **Field Name**
  * **Opis:** Navodi ime polja za potvrdu koje će se proceniti.
  * **Detalj:** Ovo treba da se poklapa sa tačnim identifikatorom polja koji se koristi u sistemu. Određuje stanje kog polja za potvrdu se prati.
* **Boolean**
  * **Opis:** Definiše uslov koji pokreće radni tok.
  * **Opcije:**
    * **True:** Radni tok se pokreće ako je polje za potvrdu označeno.
    * **False:** Radni tok se pokreće ako polje za potvrdu nije označeno.

#### **Funkcionalnost:**

* **Detekcija stanja:** Kartica neprekidno prati stanje navedenog polja za potvrdu.
* **Procena uslova:** Sistem proverava da li je polje za potvrdu u stanju (označeno ili neoznačeno) navedenom Boolean uslovom.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako se stanje polja za potvrdu poklapa sa navedenim Boolean uslovom (bilo true za označeno ili false za neoznačeno), sistem pokreće povezane akcije. One mogu uključivati omogućavanje ili onemogućavanje polja formulara, pokretanje obaveštenja, pokretanje radnih tokova ili ažuriranje zapisa.
  * **Netačan uslov:**\
    Ako se stanje polja za potvrdu ne poklapa sa uslovom, mogu se preduzeti alternativne akcije ili nikakve akcije, u zavisnosti od podešavanja radnog toka.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom polja za potvrdu iz liste dostupnih polja i postavljanjem Boolean uslova.&#x20;

## Zaključak:

Kartica radnog toka "Checkbox Field Condition" je osnovni alat za upravljanje dinamičkim formularima i dokumentima unutar ERP sistema, gde korisnički unosi mogu diktirati naredne procese podataka. Automatizacijom akcija na osnovu stanja polja za potvrdu, ova kartica poboljšava efikasnost radnog toka i obezbeđuje da ponašanja sistema budu usklađena sa korisničkim unosima. Jasna dokumentacija ove kartice pomoći će korisnicima da je efikasno implementiraju u svoje poslovanje, omogućavajući bolju kontrolu nad ponašanjem formulara i automatizacijom procesa.



**Napomena: Nemaju svi korisnici polje za potvrdu, ali se ono može dodati ako se želi.**

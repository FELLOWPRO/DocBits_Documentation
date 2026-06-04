# If Country in Field is One of

<figure><img src="../../../../.gitbook/assets/image (14) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Ova kartica radnog toka je dizajnirana da proceni da li je navedena zemlja, smeštena u određenom polju, deo unapred definisane liste zemalja. Na osnovu ove procene, radni tok se može nastaviti sa tačnim ili netačnim uslovom. Pomaže u automatizaciji procesa gde akcije zavise od toga da li je zemlja navedena među skupom dozvoljenih ili ograničenih zemalja.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi polje dokumenta u kojem je sačuvano ime ili kod zemlje.
   * **Detalj:** Ovo treba da se poklapa sa tačnim identifikatorom polja podataka o zemlji unutar dokumenta.&#x20;
2. **Operator**
   * **Opis:** Definiše da li zemlja u polju mora biti deo unapred definisane liste zemalja.
   * **Opcije:**
     * **Is:** Zemlja mora biti uključena u listu navedenih zemalja da bi uslov bio tačan.
     * **Is Not:** Zemlja ne sme biti uključena u listu navedenih zemalja da bi uslov bio tačan.
3. **Countries**
   * **Opis:** Navodi listu zemalja sa kojima će se uporediti izabrana zemlja.
   * **Detalj:** Ovo je lista zemalja razdvojenih zarezima. Poređenje proverava da li je zemlja u polju uključena u ovu listu.
4. **Continue Condition**
   * **Opis:** Definiše rezultat poređenja. Ako zemlja ispunjava uslov, radni tok se nastavlja sa navedenom Boolean vrednošću.
   * **Opcije:**
     * **True:** Radni tok se nastavlja ako se uslov poklapa.
     * **False:** Radni tok se nastavlja ako se uslov ne poklapa.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje da li je zemlja navedena u polju deo liste unapred definisanih zemalja. Ova procena proverava ime ili kod zemlje u odnosu na datu listu.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako je zemlja u polju deo navedene liste zemalja, radni tok se nastavlja sa tačnim uslovom. Ovo može pokrenuti dalje akcije, kao što su usmeravanje dokumenata odgovarajućem odeljenju, primena određenih pravila obrade ili omogućavanje funkcija specifičnih za region.
  * **Netačan uslov:**\
    Ako se zemlja ne poklapa sa listom, radni tok se nastavlja sa netačnim uslovom. Ovo omogućava izvršavanje alternativnih akcija ili zaustavljanje radnog toka na osnovu podešavanja sistema.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom polja dokumenta koje sadrži zemlju i navođenjem liste zemalja za proveru. Operator se zatim bira iz padajuće liste da definiše da li zemlja mora biti deo ili ne deo navedene liste zemalja. Na kraju, korisnici postavljaju uslov za nastavak (tačan ili netačan), koji određuje sledeći korak u radnom toku.

## **Zaključak:**

Kartica radnog toka "Country in Field Comparison with List" je vredan alat za automatizaciju akcija na osnovu toga da li je zemlja deo unapred definisane grupe. Poređenjem podataka o zemlji sa listom dozvoljenih ili ograničenih zemalja, ova kartica poboljšava efikasnost radnog toka i obezbeđuje da sistemski procesi prate ispravna geografska pravila.

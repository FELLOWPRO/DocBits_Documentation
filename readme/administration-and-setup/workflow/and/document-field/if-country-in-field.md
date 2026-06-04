# If Country in Field

<figure><img src="../../../../.gitbook/assets/image (13) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da proceni da li je navedena zemlja, smeštena u određenom polju, deo određene trgovinske ili političke oblasti (Evropska unija, Šengenska zona ili NAFTA). Na osnovu ove procene, radni tok se može nastaviti sa tačnim ili netačnim uslovom, omogućavajući dalje akcije unutar sistema. Posebno je korisna za automatizaciju poslovnih pravila specifičnih za region, obezbeđivanje usklađenosti ili pokretanje određenih radnih tokova na osnovu geografskih pripadnosti.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi polje dokumenta u kojem je sačuvano ime ili kod zemlje.
   * **Detalj:** Ovo treba da se poklapa sa tačnim identifikatorom polja podataka o zemlji unutar dokumenta.&#x20;
2. **Operator**
   * **Opis:** Navodi da li zemlja u izabranom polju treba ili ne treba da se poklapa sa izabranim regionom ili sporazumom.
   * **Opcije:**
     * **Is:** Zemlja mora biti deo izabranog sporazuma (EU, Šengen ili NAFTA) da bi uslov bio tačan.
     * **Is Not:** Zemlja ne sme biti deo izabranog sporazuma da bi uslov bio tačan.
3. **Poređenje zemalja**
   * **Opis:** Definiše da li se zemlja u polju proverava u odnosu na određeni politički ili trgovinski sporazum.
   * **Opcije:**
     * **European Union:** Kartica proverava da li je zemlja članica Evropske unije.
     * **Schengen Area:** Kartica proverava da li je zemlja deo Šengenske zone.
     * **NAFTA:** Kartica proverava da li je zemlja članica NAFTA sporazuma.
4. **Boolean**
   * **Opis:** Definiše rezultat poređenja. Ako zemlja ispunjava uslov, radni tok se nastavlja sa navedenom Boolean vrednošću.
   * **Opcije:**
     * **True:** Radni tok se nastavlja ako se uslov poklapa.
     * **False:** Radni tok se nastavlja ako se uslov ne poklapa.

## **Funkcionalnost:**

* **Procena uslova:**
  * Sistem procenjuje da li je zemlja navedena u polju deo izabranog regiona ili sporazuma (EU, Šengenska zona ili NAFTA) na osnovu izabranog operatora. Ova procena proverava ime ili kod zemlje u odnosu na unapred definisanu listu zemalja koje pripadaju svakoj odgovarajućoj grupi.
* **Izvršavanje akcije:**
  * **Tačan uslov:** Ako se zemlja u polju poklapa sa izabranim regionom (prema operatoru), radni tok se nastavlja sa navedenim tačnim uslovom. Ovo može pokrenuti dalje akcije, kao što su usmeravanje dokumenata, primena posebnih pravila obrade ili omogućavanje funkcija specifičnih za region.
  * **Netačan uslov:** Ako se zemlja ne poklapa sa izabranim regionom (prema operatoru), radni tok se nastavlja sa navedenim netačnim uslovom, omogućavajući izvršavanje alternativnih akcija ili završetak radnog toka na osnovu podešavanja sistema.

## **Podešavanje i konfiguracija:**&#x20;

* Korisnici konfigurišu karticu izborom polja dokumenta koje sadrži zemlju i navođenjem regiona (Evropska unija, Šengenska zona ili NAFTA). Operator se zatim bira iz padajuće liste da definiše da li zemlja mora biti deo ili ne deo izabranog regiona. Na kraju, korisnici postavljaju uslov za nastavak (tačan ili netačan), koji određuje sledeći korak u radnom toku.

## **Zaključak:**

Kartica radnog toka "Country in Field Comparison" je ključni alat za automatizaciju procesa koji zavise od geografskih pravila, kao što su usklađenost sa trgovinskim sporazumima ili političke pripadnosti. Poređenjem podataka o zemlji sa određenim regionima kao što su Evropska unija, Šengenska zona ili NAFTA, ova kartica obezbeđuje da sistem primeni ispravnu logiku obrade, poboljšavajući efikasnost i obezbeđujući tačno izvršavanje radnog toka na osnovu geografskih uslova.

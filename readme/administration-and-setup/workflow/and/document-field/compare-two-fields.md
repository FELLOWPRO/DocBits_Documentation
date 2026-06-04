# Compare two Fields

<figure><img src="../../../../.gitbook/assets/image (11) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije poređenjem vrednosti dva navedena polja dokumenta. Omogućava dinamičko donošenje odluka na osnovu podataka polja i obezbeđuje da se radni tokovi izvršavaju na osnovu poređenja između različitih vrednosti dokumenta.

## **Komponente kartice:**

1. **Field Name (1)**
   * **Opis:** Navodi prvo polje dokumenta koje treba uporediti.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom prvog polja unutar dokumenta.
2. **Operator**
   * **Opis:** Definiše tip poređenja koji treba izvršiti između dva polja.
   * **Opcije:**
     * **Equals (=):** Proverava da li su vrednosti dva polja jednake.
     * **Not Equals (≠):** Obezbeđuje da su vrednosti dva polja različite.
     * **Greater Than (>):** Potvrđuje da je vrednost prvog polja veća od drugog polja.
     * **Greater or Equals (≥):** Proverava da li je vrednost prvog polja jednaka ili veća od drugog polja.
     * **Lesser Than (<):** Proverava da li je vrednost prvog polja manja od drugog polja.
     * **Less or Equals (≤):** Obezbeđuje da je vrednost prvog polja manja ili jednaka drugom polju.
3. **Field Name (2)**
   * **Opis:** Navodi drugo polje dokumenta koje treba uporediti sa prvim poljem.
   * **Detalj:** Ovo treba da se poklapa sa tačnim identifikatorom drugog polja unutar dokumenta.

## **Funkcionalnost:**

**Procena uslova:** Sistem procenjuje da li vrednosti u dva navedena polja zadovoljavaju uslov poređenja definisan operatorom.

**Izvršavanje akcije:**

* **Tačan uslov:**\
  Ako vrednosti dva polja odgovaraju uslovu poređenja, sistem pokreće povezane akcije. Ove akcije mogu uključivati ažuriranje zapisa ili pokretanje upozorenja.
* **Netačan uslov:**\
  Ako vrednosti dva polja ne odgovaraju navedenom uslovu, mogu se izvršiti alternativne akcije ili nikakve akcije, u zavisnosti od konfiguracije radnih tokova.

## **Podešavanje i konfiguracija:**&#x20;

* Korisnici konfigurišu karticu izborom dva polja koja treba uporediti iz liste dostupnih polja u sistemu. Operator se bira iz padajuće liste dostupnih opcija poređenja.

## **Zaključak:**

Kartica radnog toka "Compare Two Fields" je osnovni alat za poređenje podataka između polja unutar dokumenata. Automatizacijom akcija na osnovu poređenja polja, ova kartica pomaže u optimizaciji donošenja odluka, podržava validaciju podataka i poboljšava automatizaciju radnog toka.

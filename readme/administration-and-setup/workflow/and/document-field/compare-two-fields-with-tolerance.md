# Compare two Fields with Tolerance

<figure><img src="../../../../.gitbook/assets/image (12) (1) (1) (1) (1).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije poređenjem vrednosti dva navedena polja dokumenta, sa dodatnom mogućnošću primene vrednosti tolerancije. Ova funkcija omogućava sistemu da uzme u obzir marginu greške (toleranciju) pri poređenju vrednosti polja, dozvoljavajući fleksibilnije donošenje odluka unutar radnih tokova.

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
   * **Detalj:** Ovo treba da se poklapa sa tačnim identifikatorom drugog polja unutar dokumenta.&#x20;
4. **Iznos tolerancije**
   * **Opis:** Definiše prihvatljivu marginu greške za poređenje.
   * **Detalj:** Iznos tolerancije je numerička vrednost koja označava maksimalno dozvoljenu razliku između dve vrednosti polja da bi se poređenje smatralo tačnim.
5. **Tip tolerancije**
   * **Opis:** Navodi mernu jedinicu za iznos tolerancije.
   * **Opcije:**
     * **Value:** Tolerancija je apsolutna vrednost, što znači da se dva polja mogu razlikovati za navedeni iznos tolerancije.
     * **Percent:** Tolerancija se izračunava kao procenat vrednosti drugog polja, dozvoljavajući relativnu marginu greške.

## **Funkcionalnost:**

* **Procena uslova:** Sistem procenjuje da li vrednosti u dva navedena polja zadovoljavaju uslov poređenja, uzimajući u obzir definisanu toleranciju. Ako apsolutna ili relativna razlika između dva polja pada unutar tolerancije, uslov se smatra tačnim.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako vrednosti dva polja, nakon uzimanja u obzir tolerancije, odgovaraju uslovu poređenja, sistem pokreće povezane akcije. Ove akcije mogu uključivati napredovanje radnog toka, ažuriranje zapisa, pokretanje upozorenja ili omogućavanje određenih operacija.
  * **Netačan uslov:**\
    Ako vrednosti dva polja, nakon uzimanja u obzir tolerancije, ne odgovaraju navedenom uslovu, mogu se izvršiti alternativne akcije ili nikakve akcije, u zavisnosti od konfiguracije radnog toka.

## **Podešavanje i konfiguracija:**

* Korisnici konfigurišu karticu izborom dva polja koja treba uporediti iz liste dostupnih polja u sistemu. Operator se bira iz padajuće liste dostupnih opcija poređenja. Korisnici unose iznos tolerancije i biraju tip tolerancije (vrednost ili procenat).&#x20;

## **Zaključak:**

Kartica radnog toka "Compare Two Fields with Tolerance" je moćan alat za poređenje polja dokumenta uz uzimanje u obzir dozvoljenih odstupanja u podacima. Primenom tolerancije na poređenja polja, ova kartica dodaje fleksibilnost radnom toku, omogućavajući mu da rukuje varijacijama stvarnih podataka. Ona poboljšava donošenje odluka, podržava validaciju podataka i poboljšava ukupnu automatizaciju radnog toka.

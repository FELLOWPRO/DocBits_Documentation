# Docfield is

<figure><img src="../../../../.gitbook/assets/image (8) (1) (1) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Ova kartica radnog toka je dizajnirana da automatizuje akcije poređenjem vrednosti navedenog polja dokumenta sa referentnom vrednošću ili uslovom. Obezbeđuje dinamičko i tačno donošenje odluka u radnim tokovima na osnovu validacije podataka dokumenta.

## **Komponente kartice:**

1. **Field Name**
   * **Opis:** Navodi ime polja dokumenta koje treba proceniti.
   * **Detalj:** Ovo mora da se poklapa sa tačnim identifikatorom polja unutar dokumenta.
2. **Operatori**
   * **Opis:** Definiše tip poređenja koji treba izvršiti između vrednosti polja i referentne vrednosti.
   * **Opcije:**
     * **Equals (=):** Proverava da li se vrednost polja poklapa sa referentnom vrednošću.
     * **Not Equals (≠):** Obezbeđuje da se vrednost polja razlikuje od referentne vrednosti.
     * **Greater Than (>):** Potvrđuje da je vrednost polja veća od referentne vrednosti.
     * **Greater or Equals (≥):** Proverava da li je vrednost polja jednaka ili veća od referentne vrednosti.
     * **Lesser Than (<):** Proverava da li je vrednost polja manja od referentne vrednosti.
     * **Less or Equals (≤):** Obezbeđuje da je vrednost polja manja ili jednaka referentnoj vrednosti.

## **Funkcionalnost:**

* **Procena uslova:** Sistem proverava da li vrednost polja dokumenta, u odnosu na svoju povezanu kolonu, zadovoljava uslov poređenja naveden operatorom i referentnom vrednošću.
* **Izvršavanje akcije:**
  * **Tačan uslov:**\
    Ako vrednost polja dokumenta ispunjava navedeni uslov (npr. jednaka je referentnoj vrednosti), sistem pokreće povezane akcije. One mogu uključivati ažuriranje zapisa, napredovanje radnog toka ili generisanje obaveštenja.
  * **Netačan uslov:**\
    Ako vrednost polja dokumenta ne ispunjava navedeni uslov, izvršavaju se alternativne akcije ili nikakve akcije, na osnovu konfiguracije radnog toka.

## **Podešavanje i konfiguracija:**

* Korisnik bira ime polja relevantnog dokumenta i bira operator iz padajućeg menija. Korisnik zatim navodi vrednost referentnog polja da bi dovršio konfiguraciju.

## **Zaključak:**

Kartica radnog toka "DocField Comparison Validation" je robustan alat za dinamičku obradu dokumenata. Automatizacijom akcija na osnovu poređenja polja, ova kartica pojednostavljuje radne tokove, poboljšava tačnost i podržava donošenje odluka zasnovano na podacima.

# Assign Document and Create Task/Notification for User

<figure><img src="../../../../.gitbook/assets/image (13) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka "**Assign Document and Create Task/Notification for User**" dodeljuje dokument navedenom korisniku, kreira zadatak ili obaveštenje sa podesivim detaljima i opciono šalje obaveštenje putem e-pošte korisniku. Ova kartica takođe omogućava postavljanje numeričke vrednosti prioriteta za određivanje redosleda izvršavanja.

## **Komponente kartice**

1. **User**
   * **Opis:** Navodi korisnika koji će primiti zadatak ili obaveštenje.
   * **Detalj:** Padajući meni za izbor korisnika kome će dokument i zadatak/obaveštenje biti dodeljeni.
2. **Task/Notification**
   * **Opis:** Navodi tip akcije koja se kreira za korisnika.
   * **Detalj:** Padajući meni za izbor "Task" ili "Notification" na osnovu nameravane akcije.
3. **Title**
   * **Opis:** Naslov zadatka ili obaveštenja.
   * **Detalj:** Polje za pružanje sažetog, opisnog naslova za zadatak ili obaveštenje.
4. **Description**
   * **Opis:** Dodatni detalji o zadatku ili obaveštenju.
   * **Detalj:** Polje za opisivanje svrhe zadatka ili pružanje konteksta za obaveštenje.
5. **Priority**
   * **Opis:** Definiše nivo hitnosti zadatka ili obaveštenja.
   * **Opcije:**
     * **High:** Zahteva neposrednu pažnju.
     * **Medium:** Važno ali ne hitno.
     * **Low:** Može se rešiti kasnije.
6. **Send Mail**
   * **Opis:** Konfiguriše da li se obaveštenje putem e-pošte šalje korisniku.
   * **Opcije:**
     * **True:** Šalje obaveštenje putem e-pošte korisniku.
     * **False:** Ne šalje se obaveštenje putem e-pošte.
7. **Value**
   * **Opis:** Postavlja numerički prioritet za dodelu dokumenta.
   * **Detalj:** Polje za unos numeričke vrednosti, gde niži brojevi označavaju viši prioritet.

## **Funkcionalnost**

* **Procena uslova:**\
  Kartica izvršava svoje akcije samo ako su konfigurisani uslovi radnog toka ispunjeni.
* **Dodela dokumenta i kreiranje zadatka/obaveštenja:**\
  Dokument se dodeljuje korisniku navedenom u polju "User". Kreira se zadatak ili obaveštenje sa pruženim naslovom, opisom i nivoom prioriteta.
* **Obaveštenje putem e-pošte:**\
  Ako je "Send Mail" postavljeno na True, e-pošta se šalje korisniku da ga obavesti o zadatku ili obaveštenju.

## **Podešavanje i konfiguracija**

1. **Izbor korisnika:**
   * Izaberite korisnika iz padajućeg menija User.
2. **Konfiguracija detalja zadatka/obaveštenja:**
   * Izaberite "Task" ili "Notification" iz padajućeg menija Task/Notification.
   * Unesite Title i Description za zadatak ili obaveštenje.
   * Postavite Priority izborom High, Medium ili Low iz padajućeg menija.
3. **Omogućavanje obaveštenja putem e-pošte:**
   * Konfigurišite opciju Send Mail na True ili False, u zavisnosti od toga da li obaveštenje putem e-pošte treba poslati.
4. **Postavljanje numeričkog prioriteta:**
   * Unesite numeričku vrednost u polje Value da odredite prioritet dodele, gde se niže vrednosti obrađuju prve.
5. Sačuvajte konfiguraciju kartice i aktivirajte radni tok.

## **Zaključak**

Kartica radnog toka "Assign Document and Create Task/Notification for User" obezbeđuje da se dokumenti dodeljuju odgovarajućem korisniku uz kreiranje zadataka ili obaveštenja sa definisanim prioritetima i opcionim obaveštenjima putem e-pošte. Ova kartica pomaže u pojednostavljenju delegiranja zadataka i poboljšava efikasnost radnog toka.

# Assign Document and Create Task/Notification for Group

<figure><img src="../../../../.gitbook/assets/image (12) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka "**Assign Document and Create Task/Notification for Group**" dodeljuje dokument navedenoj grupi, kreira zadatak ili obaveštenje sa prilagodljivim detaljima i opciono šalje obaveštenje putem e-pošte grupi. Ova kartica takođe podržava dodelu numeričke vrednosti prioriteta za određivanje redosleda izvršavanja.

## **Komponente kartice**

1. **Group Name**
   * **Opis:** Navodi grupu koja će primiti zadatak ili obaveštenje.
   * **Detalj:** Padajući meni za izbor imena grupe kojoj će dokument i zadatak/obaveštenje biti dodeljeni.
2. **Task/Notification**
   * **Opis:** Navodi tip akcije koja se kreira za grupu.
   * **Detalj:** Padajući meni za izbor "Task" ili "Notification" na osnovu željene akcije.
3. **Title**
   * **Opis:** Pruža naslov zadatka ili obaveštenja.
   * **Detalj:** Polje za dodavanje sažetog, opisnog naslova za zadatak ili obaveštenje.
4. **Description**
   * **Opis:** Dodatno opisuje zadatak ili obaveštenje.
   * **Detalj:** Polje za pružanje dodatnih detalja o svrsi zadatka ili sadržaju obaveštenja.
5. **Priority**
   * **Opis:** Definiše nivo hitnosti zadatka ili obaveštenja.
   * **Opcije:**
     * **High:** Zahteva neposrednu pažnju.
     * **Medium:** Važno ali ne hitno.
     * **Low:** Može se rešiti kasnije.
6. **Send Mail**
   * **Opis:** Konfiguriše da li se obaveštenje putem e-pošte šalje grupi.
   * **Opcije:**
     * **True:** Šalje obaveštenje putem e-pošte.
     * **False:** Ne šalje e-poštu.
7. **Value**
   * **Opis:** Postavlja numerički prioritet za dodelu dokumenta.
   * **Detalj:** Polje za unos numeričke vrednosti, gde niži broj označava viši prioritet.

## **Funkcionalnost**

* **Procena uslova:**\
  Kartica izvršava svoje akcije samo ako su konfigurisani uslovi radnog toka zadovoljeni.
* **Dodela dokumenta i kreiranje zadatka/obaveštenja:**\
  Dokument se dodeljuje grupi navedenoj u polju "Group Name". Kreira se zadatak ili obaveštenje sa konfigurisanim naslovom, opisom i nivoom prioriteta.
* **Obaveštenje putem e-pošte:**\
  Ako je "Send Mail" postavljeno na True, obaveštenje putem e-pošte se šalje grupi da bi je informisalo o zadatku ili obaveštenju.

## **Podešavanje i konfiguracija**

1. **Definisanje imena grupe:**
   * Unesite ime grupe u polje Group Name.
2. **Izbor Task/Notification:**
   * Izaberite "Task" ili "Notification" iz padajućeg menija Task/Notification.
3. **Postavljanje detalja zadatka/obaveštenja:**
   * Unesite Title i Description za zadatak ili obaveštenje.
   * Izaberite Priority iz padajućeg menija (High, Medium ili Low).
4. **Omogućavanje obaveštenja putem e-pošte:**
   * Konfigurišite opciju Send Mail na True ili False, u zavisnosti od toga da li obaveštenje putem e-pošte treba poslati.
5. **Dodela numeričkog prioriteta:**
   * Unesite numeričku vrednost u polje Value da odredite prioritet dodele, gde niže vrednosti imaju prednost.
6. Sačuvajte konfiguraciju kartice i aktivirajte radni tok.

## **Zaključak**

Kartica radnog toka "Assign Document and Create Task/Notification for Group" obezbeđuje da se dokumenti dodeljuju odgovarajućoj grupi uz kreiranje zadataka ili obaveštenja sa prilagodljivim opcijama prioriteta i obaveštenja putem e-pošte. Ovo pojednostavljuje upravljanje dokumentima i poboljšava efikasnost radnog toka.

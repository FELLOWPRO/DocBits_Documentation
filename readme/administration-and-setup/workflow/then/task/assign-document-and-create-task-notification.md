# Assign Document and Create Task/Notification

<figure><img src="../../../../.gitbook/assets/image (14) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka "**Assign Document and Create Task/Notification Based on Decision Table**" dodeljuje dokument i kreira zadatak ili obaveštenje sa podesivim detaljima. Osoba kojoj se dodeljuje određuje se vraćanjem tabele odlučivanja, a kartica omogućava postavljanje prioriteta i slanje obaveštenja putem e-pošte.

## **Komponente kartice**

1. **Assignee Type**
   * **Opis:** Navodi da li vraćanje tabele odlučivanja dodeljuje dokument i zadatak/obaveštenje korisniku ili grupi.
   * **Detalj:** Polje za konfigurisanje tipa osobe kojoj se dodeljuje kao "User" ili "Group" na osnovu izlaza tabele odlučivanja.
2. **Task/Notification**
   * **Opis:** Navodi tip akcije koja se kreira za osobu kojoj se dodeljuje.
   * **Detalj:** Padajući meni za izbor "Task" ili "Notification" na osnovu potreba radnog toka.
3. **Title**
   * **Opis:** Naslov zadatka ili obaveštenja.
   * **Detalj:** Polje za pružanje sažetog naslova koji identifikuje zadatak ili obaveštenje.
4. **Description**
   * **Opis:** Dodatni detalji o zadatku ili obaveštenju.
   * **Detalj:** Polje za opisivanje svrhe i konteksta zadatka ili obaveštenja.
5. **Priority**
   * **Opis:** Definiše nivo hitnosti zadatka ili obaveštenja.
   * **Opcije:**
     * **High:** Zahteva neposrednu pažnju.
     * **Medium:** Važno ali ne hitno.
     * **Low:** Može se rešiti kasnije.
6. **Assignee Type**
   * **Opis:** Ovo polje određuje tip osobe kojoj se dodeljuje (User ili Group) kome se dodeljuju dokument i zadatak/obaveštenje.
   * **Detalj:** Padajući meni za izbor da li se zadatak/obaveštenje dodeljuje korisniku ili grupi na osnovu izlaza tabele odlučivanja.
7. **Send Mail**
   * **Opis:** Konfiguriše da li se obaveštenje putem e-pošte šalje osobi kojoj se dodeljuje.
   * **Opcije:**
     * **True:** Šalje obaveštenje putem e-pošte.
     * **False:** Ne šalje se obaveštenje putem e-pošte.
8. **Value**
   * **Opis:** Postavlja numerički prioritet za dodelu dokumenta.
   * **Detalj:** Polje za unos numeričke vrednosti, gde niži brojevi označavaju viši prioritet.

## **Funkcionalnost**

* **Procena uslova:**\
  Kartica izvršava svoje akcije samo ako su uslovi radnog toka zadovoljeni.
* **Procena tabele odlučivanja:**\
  Tabela odlučivanja određuje da li se dokument i zadatak/obaveštenje dodeljuju korisniku ili grupi.
* **Dodela dokumenta i kreiranje zadatka/obaveštenja:**\
  Dokument se dodeljuje rezultatu tabele odlučivanja. Kreira se zadatak ili obaveštenje sa navedenim naslovom, opisom i nivoom prioriteta.
* **Obaveštenje putem e-pošte:**\
  Ako je "Send Mail" postavljeno na True, obaveštenje putem e-pošte se šalje osobi kojoj se dodeljuje.

## **Podešavanje i konfiguracija**

1. **Definisanje Assignee Type:**
   * Konfigurišite polje Assignee Type na "User" ili "Group" na osnovu izlaza tabele odlučivanja.
2. **Izbor Task/Notification:**
   * Izaberite "Task" ili "Notification" iz padajućeg menija Task/Notification.
3. **Postavljanje detalja zadatka/obaveštenja:**
   * Unesite Title i Description za zadatak ili obaveštenje.
   * Izaberite Priority (High, Medium ili Low) iz padajućeg menija.
4. **Omogućavanje obaveštenja putem e-pošte:**
   * Postavite opciju Send Mail na True ili False, u zavisnosti od toga da li obaveštenje putem e-pošte treba poslati.
5. **Postavljanje numeričkog prioriteta:**
   * Unesite numeričku vrednost u polje Value da odredite prioritet dodele, gde se niži brojevi obrađuju prvi.
6. Sačuvajte konfiguraciju kartice i aktivirajte radni tok.

## **Zaključak**

Kartica radnog toka "Assign Document and Create Task/Notification Based on Decision Table" obezbeđuje da se zadaci ili obaveštenja dinamično dodeljuju odgovarajućem korisniku ili grupi na osnovu rezultata tabele odlučivanja. Ova kartica olakšava efikasno delegiranje zadataka, prilagodljive prioritete i opciona obaveštenja putem e-pošte radi poboljšanja odzivnosti radnog toka.

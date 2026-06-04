# Assign to Procurement Group and Create a Task/Notification

<figure><img src="../../../../.gitbook/assets/image (2) (1) (1) (2).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka "**Assign Document to Procurement Group and Create Task/Notification**" dodeljuje dokument navedenoj nabavnoj grupi, kreira zadatak ili obaveštenje sa definisanim detaljima i opciono obaveštava grupu putem e-pošte. Prioritetizuje izvršavanje zadataka na osnovu podesive numeričke vrednosti prioriteta.

## **Komponente kartice**

1. **Group Name**
   * **Opis:** Navodi nabavnu grupu odgovornu za rukovanje dokumentom.
   * **Detalj:** Polje u kojem korisnik može ručno uneti ime nabavne grupe.
2. **Task/Notification**
   * **Opis:** Definiše da li se za grupu kreira zadatak ili obaveštenje.
   * **Detalj:** Polje u kojem korisnik može birati između kreiranja zadatka ili obaveštenja
3. **Title**
   * **Opis:** Naslov zadatka ili obaveštenja kreiranog za grupu.
   * **Detalj:** Polje za pružanje sažetog i prepoznatljivog naslova za zadatak ili obaveštenje.
4. **Description**
   * **Opis:** Dodatni detalji o zadatku ili obaveštenju.
   * **Detalj:** Polje za opisivanje svrhe zadatka i pružanje konteksta ili uputstava.
5. **Priority**
   * **Opis:** Definiše nivo hitnosti zadatka ili obaveštenja.
   * **Opcije:**
     * **High:** Zadatak zahteva neposrednu pažnju.
     * **Medium:** Zadatak je važan ali ne hitan.
     * **Low:** Zadatak se može rešiti kasnije.
6. **Send Mail**
   * **Opis:** Konfiguriše da li obaveštenje putem e-pošte treba poslati grupi.
   * **Opcije:**
     * **True:** Šalje obaveštenje putem e-pošte nabavnoj grupi.
     * **False:** Ne šalje se obaveštenje putem e-pošte.
7. **Value**
   * **Opis:** Postavlja numerički prioritet za izvršavanje zadatka.
   * **Detalj:** Polje za unos numeričke vrednosti, gde niži broj predstavlja viši prioritet.

## **Funkcionalnost**

* **Procena uslova:**\
  Kartica izvršava svoje akcije samo ako su definisani uslovi radnog toka ispunjeni.
* **Dodela grupi i kreiranje zadatka/obaveštenja:**\
  Dokument se dodeljuje navedenoj nabavnoj grupi. Kreira se zadatak ili obaveštenje sa pruženim naslovom, opisom i prioritetom.
* **Obaveštenje putem e-pošte:**\
  Ako je "Send Mail" postavljeno na True, grupa prima e-poštu o zadatku ili obaveštenju.

## **Podešavanje i konfiguracija**

1. **Definisanje imena grupe:**
   * Unesite ime nabavne grupe u polje Group Name.
2. **Konfiguracija detalja zadatka/obaveštenja:**
   * Navedite Title i Description za zadatak ili obaveštenje.
   * Izaberite Priority iz padajućeg menija (High, Medium ili Low).
3. **Omogućavanje obaveštenja putem e-pošte:**
   * Postavite "Send Mail" na True ili False na osnovu toga da li grupa treba da primi e-poštu.
4. **Postavljanje numeričkog prioriteta:**
   * Unesite numeričku vrednost u polje Value da odredite prioritet zadatka, gde se niže vrednosti obrađuju prve.
5. Sačuvajte konfiguraciju kartice i aktivirajte radni tok.

## **Zaključak**

Kartica radnog toka "Assign Document to Procurement Group and Create Task/Notification" obezbeđuje da se dokumenti usmeravaju odgovarajućoj grupi sa jasnim uputstvima za zadatak i nivoima prioriteta. Omogućavanjem opcionih obaveštenja putem e-pošte, ova kartica poboljšava vidljivost zadataka i obezbeđuje neometano izvršavanje radnog toka.

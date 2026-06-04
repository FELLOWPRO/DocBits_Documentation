# Assign a Task with Title

<figure><img src="../../../../.gitbook/assets/image (291).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka "Assign Task / Notification from Decision Table" je dizajnirana da dinamično dodeljuje zadatke ili obaveštenja na osnovu rezultata tabele odlučivanja. Ova kartica obezbeđuje da se zadaci ili obaveštenja dodeljuju ispravnom korisniku ili grupi u skladu sa logikom definisanom u tabeli odlučivanja, uz opciono obaveštenje putem e-pošte koje se šalje primaocu.

## **Komponente kartice:**

1. **Title**
   * **Opis**: Navodi naslov zadatka ili obaveštenja koje se kreira.
   * **Detalj**: Naslov treba da pruži kontekst i opiše svrhu zadatka ili obaveštenja.
2. **Description**
   * **Opis**: Definiše sadržaj ili svrhu zadatka ili obaveštenja.
   * **Detalj**: Pruža dodatne informacije o zadatku ili obaveštenju, objašnjavajući kontekst ili potrebnu akciju.
3. **Priority**
   * **Opis**: Definiše nivo hitnosti zadatka ili obaveštenja.
   * **Opcije**:
     * **High**: Zadaci ili obaveštenja koji zahtevaju neposrednu pažnju.
     * **Medium**: Važni zadaci koji treba da se reše bez odlaganja.
     * **Low**: Zadaci kojima se može posvetiti pažnja kasnije.
4. **Assignee Type**
   * **Opis**: Navodi korisnika ili grupu dodeljenu zadatku ili obaveštenju na osnovu izlaza tabele odlučivanja.
   * **Detalj**: Tabela odlučivanja dinamično procenjuje uslove i vraća odgovarajućeg korisnika ili grupu za dodelu.
5. **Email Notification**
   * **Opis**: Konfiguriše da li će se obaveštenje putem e-pošte poslati dodeljenom korisniku ili grupi.
   * **Opcije**:
     * **True**: Šalje obaveštenje putem e-pošte primaocu.
     * **False**: Ne šalje se obaveštenje putem e-pošte.

#### **Dodatne komponente u Verziji 3**

1. **Notification Type**
   * **Opis**: Navodi da li kartica kreira zadatak ili obaveštenje.
   * **Opcije**:
     * **Task**: Kreira zadatak dodeljen korisniku ili grupi iz tabele odlučivanja.
     * **Notification**: Šalje obaveštenje korisniku ili grupi iz tabele odlučivanja.

## **Funkcionalnost:**

* **Procena uslova:**\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Dodela zadatka / obaveštenja**\
  Kartica dodeljuje zadatak ili obaveštenje korisniku ili grupi identifikovanoj tabelom odlučivanja. Tabela odlučivanja dinamično procenjuje unapred definisane uslove i vraća odgovarajućeg primaoca.
* **Obaveštenje putem e-pošte**\
  Ako je tako konfigurisano, obaveštenje putem e-pošte se šalje dodeljenom korisniku ili grupi.
* **Funkcionalnost Verzije 3**\
  U Verziji 3, kartica omogućava kreiranje bilo zadatka bilo obaveštenja, pružajući veću fleksibilnost za upravljanje zadacima i komunikaciju.

## **Podešavanje i konfiguracija:**

1. **Definisanje detalja zadatka ili obaveštenja**:\
   Unesite naslov, opis i prioritet za zadatak ili obaveštenje.
2. **Konfiguracija tabele odlučivanja**:\
   Podesite tabelu odlučivanja da dinamično odredi koji korisnik ili grupa treba da budu dodeljeni zadatku ili obaveštenju.
3. **Omogućavanje obaveštenja putem e-pošte**:\
   Navedite da li obaveštenje putem e-pošte treba poslati dodeljenom korisniku ili grupi.
4. **Navođenje tipa obaveštenja (Verzija 3)**:\
   Izaberite da li će kartica kreirati zadatak ili poslati obaveštenje.

## **Zaključak:**

Kartica radnog toka **"Assign Task / Notification from Decision Table"** automatizuje dodelu zadataka ili obaveštenja na osnovu dinamičkih uslova definisanih u tabeli odlučivanja. Verzija 3 poboljšava njenu funkcionalnost omogućavajući korisnicima da biraju između kreiranja zadatka ili obaveštenja i obezbeđuje da ispravan primalac uvek bude dodeljen. Funkcija obaveštenja putem e-pošte održava korisnike informisanim, pojednostavljujući komunikaciju i upravljanje zadacima.

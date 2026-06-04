# Create a New Task and assign it to the User

<figure><img src="../../../../.gitbook/assets/image (287).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha**

Kartica radnog toka **"Create Task or Notification"** pojednostavljuje upravljanje zadacima i obaveštenjima unutar radnih tokova. U zavisnosti od verzije, kartica može kreirati zadatke, slati obaveštenja i koristiti dodatnu funkcionalnost kao što su stabla odlučivanja za dinamičku obradu.

## **Komponente kartice**

1. **Title**
   * **Opis**: Definiše naslov zadatka ili obaveštenja koje se kreira.
   * **Detalj**: Naslov pruža jasan i sažet identifikator za zadatak ili obaveštenje.
2. **Description**
   * **Opis**: Pruža detalje o zadatku ili obaveštenju.
   * **Detalj**: Pomaže da se pojasni svrha ili kontekst zadatka ili obaveštenja za dodeljenog korisnika.
3. **Priority**
   * **Opis**: Postavlja nivo hitnosti za zadatak.
   * **Opcije**:
     * **High**: Zahteva neposrednu pažnju.
     * **Medium**: Važno ali ne hitno.
     * **Low**: Može se rešiti kasnije.
4. **Assigned User**
   1. **Opis**: Navodi korisnika kome je zadatak dodeljen.
   2. **Detalj**: Korisnici se biraju iz padajuće liste dostupnog osoblja.
5. **Email Notification**
   * **Opis**: Određuje da li dodeljeni korisnik prima obaveštenje putem e-pošte.
   * **Opcije**:
     * **True**: Šalje obaveštenje putem e-pošte korisniku.
     * **False**: Ne šalje se obaveštenje putem e-pošte.

## Dodatne komponente **u Verziji 3 i Verziji 4**

1. **Decision Tree (samo Verzija 3)**
   * **Opis**: Omogućava korišćenje stabla odlučivanja za dinamičko kreiranje zadatka.
   * **Opcije**:
     * **True**: Aktivira obradu stabla odlučivanja.
     * **False**: Onemogućava obradu stabla odlučivanja.
2. **Task or Notification (samo Verzija 4)**
   * **Opis**: Omogućava izbor između kreiranja zadatka ili obaveštenja.
   * **Opcije**:
     * **Task**: Kreira zadatak.
     * **Notification**: Kreira obaveštenje umesto zadatka.

## **Funkcionalnost:**

* **Procena uslova**:\
  Ova kartica se pokreće samo ako su uslovi u odeljcima **"Where"** i **"And"** ispunjeni.
* **Kreiranje zadatka ili obaveštenja**:
  * Verzije 2 i 3: Zadatak se kreira sa navedenim naslovom, opisom, prioritetom i dodeljenim korisnikom.
  * Verzija 4: Omogućava kreiranje bilo zadatka bilo obaveštenja.
* **Dinamička dodela**:
  * U Verziji 3, stablo odlučivanja dinamično određuje korisnika kome će zadatak biti dodeljen na osnovu parametara radnog toka.
* **Obaveštenje putem e-pošte**:\
  Šalje e-poštu dodeljenom korisniku ako je opcija obaveštenja omogućena.

## **Podešavanje i konfiguracija:**

1. **Izbor verzije**: Izaberite verziju kartice na osnovu potrebne funkcionalnosti:
   * Verzija 2: Osnovno kreiranje zadatka sa ručnom dodelom korisnika i obaveštenjima putem e-pošte.
   * Verzija 3: Uključuje funkcionalnost stabla odlučivanja za dinamičku dodelu korisnika.
   * Verzija 4: Dodaje mogućnost kreiranja obaveštenja umesto zadatka.
2. **Unos detalja zadatka**: Navedite naslov, opis i prioritet zadatka ili obaveštenja.
3. **Dodela korisnika**:
   * Za Verzije 2 i 4, ručno izaberite korisnika iz padajuće liste.
   * Za Verziju 3, omogućite stablo odlučivanja da dinamično odredi dodeljenog korisnika.
4. **Omogućavanje obaveštenja putem e-pošte**: Navedite da li dodeljeni korisnik treba da primi obaveštenje putem e-pošte.
5. (Za Verziju 4) **Izbor zadatka ili obaveštenja**: Naznačite da li treba kreirati zadatak ili obaveštenje.

## **Zaključak:**

Kartica radnog toka **"Create Task or Notification"** je svestran alat za upravljanje zadacima i obaveštenjima. Podržavanjem dinamičke dodele korisnika kroz stabla odlučivanja i pružanjem opcija za kreiranje zadatka ili obaveštenja, ona poboljšava prilagodljivost radnog toka i efikasnost saradnje.

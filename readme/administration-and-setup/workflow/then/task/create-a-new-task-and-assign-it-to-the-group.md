# Create a New Task and assign it to the group

<figure><img src="../../../../.gitbook/assets/image (289).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Create Group Task or Notification"** olakšava kreiranje zadatka ili obaveštenja za navedene grupe, obezbeđujući efikasnu komunikaciju i upravljanje zadacima. Poboljšana funkcionalnošću stabla odlučivanja u kasnijim verzijama, ona dinamično određuje dodeljenu grupu ili metod, pojednostavljujući poslovanje.

## **Komponente kartice:**

1. **Title**
   * **Opis**: Navodi naslov zadatka ili obaveštenja.
   * **Detalj**: Deluje kao identifikator za kreirani zadatak ili obaveštenje.
2. **Description**
   * **Opis**: Opisuje kontekst ili detalje zadatka ili obaveštenja.
   * **Detalj**: Pruža jasnoću o njegovoj svrsi.
3. **Priority**
   * **Opis**: Postavlja nivo važnosti zadatka.
   * **Opcije**:
     * **High**: Zahteva neposrednu akciju.
     * **Medium**: Važno ali manje hitno.
     * **Low**: Može se rešiti kasnije.
4. **Assigned Group**
   * **Opis**: Navodi grupu odgovornu za zadatak ili obaveštenje.
   * **Detalj**: Bira se iz padajuće liste dostupnih grupa.
5. **Email Notification**
   * **Opis**: Omogućava slanje e-pošte za obaveštavanje dodeljene grupe.
   * **Opcije**:
     * **True**: Šalje obaveštenje putem e-pošte.
     * **False**: Ne šalje se obaveštenje putem e-pošte.

## **Dodatne komponente u Verziji 3 i Verziji 4**

1. **Decision Tree (samo Verzija 3)**
   * **Opis**: Omogućava korišćenje stabla odlučivanja za dinamičko kreiranje zadatka.
   * **Opcije**:
     * **True**: Aktivira obradu stabla odlučivanja.
     * **False**: Onemogućava obradu stabla odlučivanja.
2. **Task/Notification Option** **(samo Verzija 4)**
   * **Opis**: Omogućava kreiranje bilo zadatka bilo obaveštenja.
   * **Opcije**:
     * **Task**: Kreira zadatak za izabranu grupu.
     * **Notification**: Šalje obaveštenje umesto kreiranja zadatka.

## **Funkcionalnost:**

* **Procena uslova**:\
  Izvršava akciju kartice samo kada su odeljci **"Where"** i **"And"** tačni.
* **Kreiranje zadatka ili obaveštenja**:
  * Zadatak se kreira za izabranu grupu sa navedenim naslovom, opisom i prioritetom.
  * U Verziji 4, kartica može kreirati obaveštenje umesto zadatka.
* **Dinamička dodela (samo Verzija 3)**:\
  Ako je omogućeno, stablo odlučivanja dinamično određuje ciljnu grupu.
* **Obaveštenje putem e-pošte**:\
  Šalje obaveštenje putem e-pošte grupi ako je opcija e-pošte postavljena na true.

## **Podešavanje i konfiguracija:**

1. **Definisanje detalja zadatka ili obaveštenja**: Unesite naslov, opis i prioritet.
2. **Dodela grupi**: Izaberite grupu iz padajuće liste za dodelu zadatka ili obaveštenja.
3. **Omogućavanje obaveštenja putem e-pošte**: Naznačite da li grupa treba da bude obaveštena putem e-pošte.
4. **Korišćenje stabla odlučivanja (samo Verzija 3)**: Omogućite stablo odlučivanja za dinamičku dodelu grupe.
5. **Izbor tipa izlaza (samo Verzija 4)**: Izaberite da li kartica kreira zadatak ili obaveštenje.

## **Zaključak:**

Kartica radnog toka **"Create Group Task or Notification"** pojednostavljuje upravljanje zadacima i obaveštenjima ciljanjem grupa direktno. Njena funkcija dinamičke dodele, omogućena stablom odlučivanja, poboljšava fleksibilnost, dok obaveštenja putem e-pošte obezbeđuju pravovremenu komunikaciju. Verzije 3 i 4 dodaju naprednu funkcionalnost, čineći je svestranim alatom za efikasno izvršavanje radnog toka.

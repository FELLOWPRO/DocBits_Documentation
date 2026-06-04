# Create a New Task and assign it to the User in Document Field

<figure><img src="../../../../.gitbook/assets/image (290).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Create Field-Based Task or Notification"** se koristi za kreiranje zadataka ili obaveštenja koja se dinamično dodeljuju korisnicima identifikovanim unutar određenih polja dokumenta. Ova kartica pruža opcioni mehanizam rezerve kako bi se obezbedilo neometano izvršavanje radnog toka čak i kada polje dokumenta ne navodi validnog korisnika.

## **Komponente kartice:**&#x20;

1. **Title**
   * **Opis**: Navodi naslov zadatka ili obaveštenja.
   * **Detalj**: Koristi se za imenovanje i identifikaciju zadatka ili obaveštenja koje se kreira.
2. **Description**
   * **Opis**: Pruža dodatne detalje o zadatku ili obaveštenju.
   * **Detalj**: Obezbeđuje da primalac razume svrhu i kontekst zadatka ili obaveštenja.
3. **Priority**
   * **Opis**: Definiše hitnost zadatka ili obaveštenja.
   * **Opcije**:
     * **High**: Zahteva neposrednu pažnju.
     * **Medium**: Važno ali manje hitno.
     * **Low**: Može se rešiti kasnije.
4. **Field Name**
   * **Opis**: Navodi polje dokumenta koje će se koristiti za dodelu zadatka ili obaveštenja.
   * **Detalj**: Izabrano polje će dinamično odrediti korisnika kome će zadatak ili obaveštenje biti dodeljeni. Ako je polje prazno ili nevažeće, zadatak ili obaveštenje će biti dodeljeni rezervnom korisniku izabranom iz padajuće liste.
5. **Email Notification**
   * **Opis**: Konfiguriše da li je dodeljeni korisnik obavešten putem e-pošte.
   * **Opcije**:
     * **True**: Šalje obaveštenje putem e-pošte dodeljenom korisniku.
     * **False**: Ne šalje se obaveštenje putem e-pošte.
6. **Fallback User**
   * **Opis**: Omogućava izbor korisnika iz padajuće liste za dodelu zadatka ili obaveštenja kada se ne pronađe validan korisnik u polju dokumenta.
   * **Detalj**: Obezbeđuje da se zadatak ili obaveštenje dodele čak i ako je polje dokumenta prazno ili nevažeće.

## **Dodatne komponente u Verziji 3:**

1. **Notification Type**&#x20;
   * **Opis**: Navodi da li kartica kreira zadatak ili obaveštenje.
   * **Opcije**:
     * **Task**: Kreira zadatak dodeljen navedenom korisniku.
     * **Notification**: Šalje obaveštenje umesto kreiranja zadatka.

## **Funkcionalnost:**

* **Procena uslova**:\
  Kartica izvršava svoju akciju samo ako se oba odeljka, **"Where"** i **"And"**, procene kao tačna.
* **Kreiranje zadatka ili obaveštenja**:
  * Dodeljuje zadatak ili obaveštenje korisniku identifikovanom u polju dokumenta.
  * U Verziji 3, omogućava kreiranje bilo zadatka bilo obaveštenja.
* **Mehanizam rezerve**:\
  Ako polje dokumenta ne identifikuje validnog korisnika, kartica dodeljuje zadatak ili obaveštenje rezervnom korisniku izabranom iz padajuće liste.
* **Obaveštenje putem e-pošte**:\
  Šalje obaveštenje putem e-pošte dodeljenom korisniku ako je tako konfigurisano.

## **Podešavanje i konfiguracija:**

1. **Definisanje detalja zadatka ili obaveštenja**: Unesite naslov, opis i prioritet.
2. **Izbor polja dokumenta**: Izaberite polje koje navodi korisnika za dodelu zadatka ili obaveštenja.
3. **Omogućavanje obaveštenja putem e-pošte**: Navedite da li obaveštenje putem e-pošte treba poslati dodeljenom korisniku.
4. **Izbor rezervnog korisnika**: Izaberite rezervnog korisnika iz padajuće liste za dodelu ako polje dokumenta ne identifikuje validnog korisnika.
5. **Navođenje tipa obaveštenja (Verzija 3)**: Naznačite da li kartica kreira zadatak ili obaveštenje.

## **Zaključak:**

Kartica radnog toka **"Create Field-Based Task or Notification"** pojednostavljuje upravljanje zadacima i obaveštenjima dinamičkim dodeljivanjem odgovornosti na osnovu polja dokumenta. Njen mehanizam rezervnog korisnika i poboljšane opcije u Verziji 3 pružaju fleksibilnost, obezbeđujući da zadaci ili obaveštenja uvek budu dodeljeni, čak i kada su podaci dokumenta nepotpuni.

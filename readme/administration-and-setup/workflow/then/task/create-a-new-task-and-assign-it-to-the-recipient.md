# Create a New Task and assign it to the Recipient

<figure><img src="../../../../.gitbook/assets/image (288).png" alt="" width="563"><figcaption></figcaption></figure>

## **Svrha:**

Kartica radnog toka **"Create Task with Fallback"** obezbeđuje efikasno delegiranje zadataka dodeljivanjem zadataka određenim ulogama — disponentu ili nabavljaču — uz uključivanje mehanizma rezerve radi sprečavanja neuspeha u dodeli zadataka. Ova kartica poboljšava pouzdanost i prilagodljivost radnog toka u dinamičkim scenarijima.

## **Komponente kartice:**

1. **Title**
   * **Opis**: Navodi naslov zadatka koji se kreira.
   * **Detalj**: Pruža sažet identifikator za zadatak.
2. **Description**
   * **Opis**: Opisuje svrhu ili kontekst zadatka.
   * **Detalj**: Pojašnjava detalje zadatka.
3. **Priority**
   * **Opis**: Postavlja nivo hitnosti za zadatak.
   * **Opcije**:
     * **High**: Zahteva neposrednu pažnju.
     * **Medium**: Važno ali ne hitno.
     * **Low**: Može se rešiti kasnije.
4. **Assigned Role**
   * **Opis**: Navodi primarnu ulogu kojoj se zadatak dodeljuje.
   * **Opcije**:
     * **Disponent**: Dodeljuje zadatak disponentu.
     * **Purchaser**: Dodeljuje zadatak nabavljaču.
5. **Email Notification**
   * **Opis**: Omogućava obaveštavanje dodeljenog korisnika putem e-pošte.
   * **Opcije**:
     * **True**: Šalje obaveštenje putem e-pošte korisniku.
     * **False**: Ne šalje se obaveštenje putem e-pošte.
6. **Fallback User**
   * **Opis**: Pruža rezervnu opciju za dodelu zadatka ako se uloga primaoca ne pronađe.
   * **Detalj**: Omogućava izbor korisnika iz padajuće liste kako bi se obezbedilo delegiranje zadatka.

## **Funkcionalnost:**

* **Procena uslova**:\
  Kartica se izvršava samo ako su uslovi u odeljcima **"Where"** i **"And"** ispunjeni.
* **Dodela zadatka**:
  * Zadatak se dodeljuje izabranoj ulozi (disponentu ili nabavljaču).
  * Ako se navedena uloga ne pronađe, zadatak se dodeljuje korisniku iz rezervne padajuće liste.
* **Obaveštenje putem e-pošte**:\
  Šalje e-poštu dodeljenom korisniku ako je obaveštenje putem e-pošte omogućeno.

## **Podešavanje i konfiguracija:**

1. **Navođenje detalja zadatka**: Unesite naslov, opis i prioritet zadatka.
2. **Izbor primarne uloge**: Izaberite ulogu kojoj će zadatak biti dodeljen (disponentu ili nabavljaču).
3. **Konfiguracija rezervnog korisnika**: Izaberite rezervnog korisnika iz padajuće liste kako biste obezbedili dodelu zadatka ako se primarna uloga ne pronađe.
4. **Omogućavanje obaveštenja putem e-pošte**: Naznačite da li dodeljeni korisnik treba da primi obaveštenje putem e-pošte.

## **Zaključak:**

Kartica radnog toka **"Create Task with Fallback"** obezbeđuje neometano delegiranje zadataka integracijom mehanizma rezerve. Dodeljivanjem zadataka na osnovu uloga i pružanjem alternativne opcije korisnika, ona poboljšava pouzdanost i fleksibilnost u procesima upravljanja zadacima.
